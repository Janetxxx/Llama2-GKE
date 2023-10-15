import gradio as gr
import requests

# GKE API endpoint
LLAMA2_API_URL = "http://35.222.166.196:8080/v1/models/model:predict"

# Define a dictionary for poet prefixes
POET_PREFIXES = {
    "William Shakespeare": "William Shakespeare's voice",
    "Edgar Allan Poe": "Edgar Allan Poe's voice",
    "Maya Angelou": "Maya Angelou's voice",
    "Emily Dickinson": "Emily Dickinson's voice",
    "Shel Silverstein": "Shel Silverstein's voice",
    "Robert Frost": "Robert Frost's voice",
    "Pablo Neruda": "Pablo Neruda's voice",
    "William Butler Yeats": "William Butler Yeats's voice",
    "Sylvia Plath": "Sylvia Plath's voice",
    "William Wordsworth": "William Wordsworth's voice",
    "John Keats": "John Keats's voice",
}

# Define a function to invoke your Llama2 model
def invoke_llama2_model(text):
    data = {"prompt": text}
    headers = {"Content-Type": "application/json"}
    response = requests.post(LLAMA2_API_URL, json=data, headers=headers)
    result = response.json()
    generated_text = result["data"]["generated_text"]
    return generated_text


# Define a function to generate text in the style of a poet
def generate_poem(poet, input_text):
    poet_prefix = POET_PREFIXES.get(poet)
    if poet_prefix is not None:
        input_with_prefix = f"Generate a poem using {poet_prefix}: '{input_text}'"
        llama2_response = invoke_llama2_model(input_with_prefix)
        return llama2_response
    else:
        return "Invalid poet selection"


# Create a Gradio interface with a Dropdown component for poet selection
iface = gr.Interface(
    fn=generate_poem,
    inputs=[
        gr.Dropdown(
            label="Select a Poet:",
            choices=[
                "William Shakespeare",
                "Edgar Allan Poe",
                "Maya Angelou",
                "Emily Dickinson",
                "Shel Silverstein",
                "Robert Frost",
                "Pablo Neruda",
                "William Butler Yeats",
                "Sylvia Plath",
                "William Wordsworth",
                "John Keats",
            ],
        ),
        gr.Textbox(label="Enter a sentence:"),
    ],
    outputs=gr.Textbox(label="Poem in Poet's Voice:"),
    title="Poem Generator in Different Voices",
)

# Launch the Gradio interface
iface.launch()
