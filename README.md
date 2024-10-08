# Generative AI

**Generative AI** is a subfield of artificial intelligence that focuses on the use of machine learning models to generate new data resembling the patterns in the training data. It falls under the category of unsupervised learning and is particularly valuable for creating novel content such as images, videos, music, and text.

Generative AI models are trained on extensive datasets, where they learn to recognize patterns and structures present in the training data. These models find applications in diverse areas, including image synthesis, text generation, and music composition.

## Examples of Generative AI

1. **DeepDream**
   - Developed by Google, DeepDream is a computer vision algorithm that employs a convolutional neural network. Its purpose is to identify and enhance patterns within images. This technology can create captivating and surreal images by amplifying existing patterns in the source images.

2. **GANs (Generative Adversarial Networks)**
   - GANs are a specific type of neural network architecture that comprises two networks: a generator network and a discriminator network. The generator network is responsible for creating new data, while the discriminator network aims to distinguish between real and generated data. GANs have versatile applications, including image synthesis, video synthesis, and text generation.

3. **OpenAI's GPT-3 (Generative Pre-trained Transformer 3)**
   - Developed by OpenAI, GPT-3 is a language model that leverages deep learning techniques to generate human-like text. It has been applied in various tasks, such as language translation, question answering, and text completion.

**This repository contains:**

- Basics of AI
- Working with Generative AI models, OpenAI Chat Gpt, Hugging Face
- Prompt Engineering
- Streamlit
- FastAPI
- Microservices architecture

**Upcoming:**

- Langchain
- RAG llama models

## Update Conda to Python 3.12 by creating Virtual Environment

```bash
conda create -n py_12 python==3.12 -y
```

This will create a virtual Environment.
`-n` means name of the virtual env.
`-y` is yes for all installation questions.

## Activate Virtual Env

```bash
conda env list
```

Check the Available virtual env list.

```bash
conda activate py_12
```

Check Python Version

```bash
python --version
```
