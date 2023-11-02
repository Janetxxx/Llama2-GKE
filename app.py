import gradio as gr
import requests

# GKE API endpoint
LLAMA2_API_URL = "http://35.222.166.196:8080/v1/models/model:predict"

# Define a dictionary for poet prefixes
# Define a dictionary for poet prefixes
POET_PREFIXES = {
    poet: f"{poet}'s voice" for poet in [
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
    ]
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
        input_with_prefix = f"Generate a poem using {poet_prefix}:{input_text}"
        llama2_response = invoke_llama2_model(input_with_prefix)
        # Split the generated text into lines and join with line breaks
        poem_lines = llama2_response.split("\n")
        formatted_poem = "\n".join(poem_lines)
        return formatted_poem
    else:
        return "Invalid poet selection"


def validate_poem(poet, generated_text):
    prompt = f"Does this poem {generated_text} sounds like {poet}'s voice style?"
    llama2_response = invoke_llama2_model(prompt)
    
    return llama2_response


with gr.Blocks() as demo:
    gr.Markdown("# <center>Poem Generator in Different Voices</center>")
    with gr.Tab("Poem Generator"):
        text_input = [  # Change from tuple to list
            gr.Dropdown(
                label="Select a Poet:",
                choices=list(POET_PREFIXES.keys()),
            ),
            gr.Textbox(label="Generated Poem:"),
        ]
        text_button = gr.Button("Generate Poem")
        text_output = gr.Textbox(label="Poem in Poet's Voice:")

    with gr.Tab("Poem Checker"):
        with gr.Row():
            poem_input = [  # Change from tuple to list
                gr.Dropdown(
                    label="Select a Poet:",
                    choices=list(POET_PREFIXES.keys()),
                ),
                gr.Textbox(label="Validate Poem:"),
            ]
            validate_output = gr.Textbox(label="Valid Poem (Yes/No):")
        image_button = gr.Button("Validate")

    text_button.click(generate_poem, inputs=text_input, outputs=text_output)
    image_button.click(validate_poem, inputs=poem_input, outputs=validate_output)

demo.launch()

