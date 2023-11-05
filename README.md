# Llama 2 Poem Generator and Checker

```
Research Project - Spring 2023

Author: Xinyi Cui 
Supervisor: Dr. Wei Liu
```
Check out the [Demonstration Video](https://drive.google.com/file/d/1YG93mXhW-0ym38fKk-ciLL1MndS5Xh3f/view?usp=sharing).


## Introduction

In this report, we explore the application of a pre-trained large language model (LLM) in creating unique and artistic text representations through poetry generation. Specifically, we designed and developed a web application that leverages Llama2, a powerful open-source LLM, to convert input sentences or text into poetry written in various poet styles. Our approach uses the user-friendly interface library Gradio to create an intuitive and engaging user experience. We demonstrate how our system can generate high-quality poems while also providing a means to verify their authenticity by identifying the original poet's voice.

## Prerequisites

Before getting started, make sure you have the following prerequisites:

- A Hugging Face Account
- A Hugging Face Llama 2 access token
- Docker installation on your local device
- A Docker Hub Account
- An IDE like VS Code with Python 3.11 and a virtual environment

## Model Description

Llama2 is an open-source LLM developed by researchers at Meta AI (Meta, 2023). It is designed as a versatile and efficient language model that can be used for a wide range of natural language processing tasks, such as text classification, sentiment analysis, named entity recognition, question answering, etc.

According to Meta, this release includes model weights and starting code for pre-trained and fine-tuned generative text models with parameters ranging from 7B to 70B. In this project, we deploy the Llama 2 Model with 7B parameters, which was released on July 18, 2023. This size was chosen because of its faster latency, which is beneficial for fast response times where quality is not a priority.

## Preparing the Model

### Get Permission to Access Llama 2

As of November 1st, 2023, usage of the model is governed by the Meta license. Meta has Llama 2 model gated behind the signup process. According to HuggingFace (HF), you need to request access from Meta on their website. Once you are granted access to the model, you can then request access from HF to download the model and deploy it.

## Deployment Architecture


## Testing and Evaluation



## References

