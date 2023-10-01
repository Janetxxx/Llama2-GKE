import gradio as gr
import requests

# Define a function to invoke your Llama2 model
def invoke_llama2_model(text):
    api_url = "http://35.222.166.196:8080/v1/models/model:predict"  # Replace with your GKE API endpoint
    data = {
        "prompt": text
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(api_url, json=data, headers=headers)
    result = response.json()
    generated_text = result["data"]["generated_text"]
    return generated_text

# Define a function to generate text in the format of a Shakespearean poem
def generate_shakespeare_poem(input_text):
    # Add a Shakespearean-style prefix to the input text
    input_with_prefix = f"Can you generate text in the format of a Shakespearean poem: {input_text}"
    
    # Call the Llama2 model with the input containing the prefix
    llama2_response = invoke_llama2_model(input_with_prefix)
    
    # Remove the prefix from the response
    response_lines = llama2_response.split('\n')
    if len(response_lines) > 1:
        response_lines.pop(0)
    
    return ''.join(response_lines)

# Create a Gradio interface
iface = gr.Interface(
   fn=generate_shakespeare_poem,
   inputs=gr.Textbox(label="Enter a sentence:"),
   outputs=gr.Textbox(label="Shakespearean-Style Text:"),
   title="Llama2 Shakespearean-Style Text Generator",
)

# Launch the Gradio interface
iface.launch()
