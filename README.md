# Llama 2 Poem Generator in different voices

```
Research Project - Spring 2023

Author: Xinyi Cui 
Supervisor: Dr. Wei Liu
```
Check out the [Demonstration Video](https://drive.google.com/file/d/1YG93mXhW-0ym38fKk-ciLL1MndS5Xh3f/view?usp=sharing).


## Introduction

We're excited to share a creative project that explores the world of poetry generation using a powerful language model (LLM). We've built a web application that utilizes Llama2, an open-source LLM, to turn ordinary sentences into unique poems inspired by different poet styles. Our goal was to create an easy and enjoyable user experience, so we've integrated the user-friendly Gradio interface. With this repository, we will demonstrate how our system can generate high-quality poems and even verify their authenticity by preserving the original poet's voice. Join us on this artistic journey and dive into our project!

## Take a Visual Tour
### Screenshots of our Poem Generator Web App
### Screenshots

![Poem Generation Interface](./images/poem-generator.png?raw=true "Poem Generation Interface")
   - Description: This screenshot showcases the user interface for generating poem.

![Poet Styles Selection](./images/poets.png?raw=true "Poet Styles Selection")
   - Description: Explore different poet styles with this user-friendly feature.

![Poem Authenticity Checker](./images/poem-checker.png?raw=true "Poem Authenticity Checker")
   - Description: Use this tool to validate if the generated poems match specific poet styles.


## Prerequisites

Before getting started, make sure you have the following prerequisites:

- A Hugging Face Account
- A Hugging Face Llama 2 access token
- Docker installation on your local device
- A Docker Hub Account
- An IDE like VS Code with Python 3.11 and a virtual environment

## Model Description

[Llama2](https://ai.meta.com/llama/]) is an open-source LLM developed by researchers at Meta AI (Meta, 2023). It is designed as a versatile and efficient language model that can be used for a wide range of natural language processing tasks, such as text classification, sentiment analysis, named entity recognition, question answering, etc.

According to Meta, this release includes model weights and starting code for pre-trained and fine-tuned generative text models with parameters ranging from 7B to 70B. In this project, we deploy the [Llama 2 Model with 7B parameters](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf), which was released on July 18, 2023. This size was chosen because of its faster latency, which is beneficial for fast response times where quality is not a priority.

## Preparing the Model

### Get Permission to Access Llama 2

As of November 1st, 2023, usage of the model is governed by the Meta license. Meta has Llama 2 model gated behind the signup process. According to HuggingFace (HF), you will need to request access from Meta on their website. Once you are granted access to the model, you can then request access from HF to download the model and deploy it by replacing the value in the `hf_access_token` within the `kubernetes_deployment.yaml` file.


## How to use it 
### 1. Run the Application
Open terminal, Run the app.py script to start the Gradio interface:
```
python3 app.py
```

### 2. Access the Web Interface
If it runs successfully, you will see something like below in your terminal:
![url](./images/url.png?raw=true "url")

Once the application is running, you can access the web interface by opening a web browser and visiting the URL.

You can now explore the various poet styles and generate unique poetry with our application!

## Deployment Architecture
![Overview of Llama2-7b Deployment in GCP Architecture](./images/architecture.png?raw=true "Overview of Llama2-7b Deployment in GCP Architecture")
   - Description: Overview of Llama2-7b Deployment in GCP Architecture.


## Testing and Evaluation
To evaluate the effectiveness and accuracy of our web application's poetry generator functionality, we developed a poetry checker that uses custom hints to invoke the Llama2-7b model and evaluates the consistency of the generated content with the expected poet's style, returns a result describing whether the poem fits the creative style of the selected poet and why.


Poetry Generator artfully creates poetry that captures the unique style and voice of the chosen poet. The poetry checker then plays a key role in reviewing the authenticity of these generated poems. Our evaluation process involves an astute evaluation by Poetry Checker of a variety of poems generated by Poetry Generator and attributed to specific poets.


## Future work 
### Enhancing User Experience with Visual Poetry
To enhance the user experience and expand the creative possibilities, future work may include the integration of image generation capabilities. This synergy of text and images could open a field of artistic expression, integrating poetry with visual storytelling.

### Breathing Life into Words
Imagining future iterations, we aspire to enable the application to generate corresponding images that visually encapsulate the essence of the poetry it creates. By taking an advanced image generation model and associating it with the generated text, the app will breathe life into text and provide users with a multi-sensory experience. This creative evolution is not only a testament to the ever-expanding boundaries of artificial intelligence and art, but also an exploration of how technology can enrich our aesthetic endeavours.

### Tailoring the Llama2-7B Model for Poetry
Another promising avenue to explore lies in the enhancement and customization of the basic Llama2-7B model. In the following stages, we aim to further refine and fine-tune the model to fit a specific poetic style, era, or voice. This tailored approach can provide users with a more nuanced and personalized poetic experience. 

### Enriching Generative Poetry
Moreover, the combination of extensive data sets and continuous training are crucial to improve the generative power of the model, ensuring richer and more evocative outputs. Our vision is to explore the realms of interpretability and controlled generation, empowering users to shape the thematic and emotional aspects of poetry.  This future work promises to improve the performance and user satisfaction of the Llama2-7B model while pushing the boundaries of artificial intelligence generative art.





## References
Hugging Face. (2023). Llama 2. meta-llama/Llama-2-7b-chat-hf. https://huggingface.co/meta-llama/Llama-2-7b-chat-hf 

Meta. (2023). Introducing Llama 2 The next generation of our open source large language model. https://ai.meta.com/llama/ 

