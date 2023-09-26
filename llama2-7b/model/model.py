"""
The `Model` class is an interface between the ML model that you're packaging and the model
server that you're running it on.

The main methods to implement here are:
* `load`: runs exactly once when the model server is spun up or patched and loads the
   model onto the model server. Include any logic for initializing your model, such
   as downloading model weights and loading the model into memory.
* `predict`: runs every time the model server is called. Include any logic for model
  inference and return the model output.

See https://truss.baseten.co/quickstart for more.
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, LlamaForCausalLM, LlamaTokenizer
from typing import Dict
from huggingface_hub import login
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
DEFAULT_MAX_LENGTH = 256

class Model:
    def __init__(self, data_dir: str, config: Dict, **kwargs) -> None:
        self._data_dir = data_dir
        self._config = config
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print("THE DEVICE INFERENCE IS RUNNING ON IS: ", self.device)
        self.tokenizer = None
        self.pipeline = None
        self._secrets = kwargs["secrets"]
            
    def load(self):
  
        self._model = LlamaForCausalLM.from_pretrained(
            "meta-llama/Llama-2-7b-chat-hf", 
            token=self._secrets["hf_access_token"], 
            torch_dtype=torch.float16,
            device_map="auto"
        )
        self._tokenizer = LlamaTokenizer.from_pretrained(
            "meta-llama/Llama-2-7b-chat-hf", 
            token=self._secrets["hf_access_token"]
        )

        print("Model Loaded.")

        self.pipeline = pipeline(
            "text-generation",
            model=self._model,
            tokenizer=self._tokenizer,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            device_map="auto",
        )

    def predict(self, request: Dict) -> Dict:
        with torch.no_grad():
            try:
                prompt = request.pop("prompt")
                data = self.pipeline(
                    prompt,
                    eos_token_id=self._tokenizer.eos_token_id,
                    max_length=DEFAULT_MAX_LENGTH,
                    **request
                )[0]
                return {"data": data}

            except Exception as exc:
                return {"status": "error", "data": None, "message": str(exc)}
            