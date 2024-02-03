# LLM types

There are two type of LLM's.

- Base LLM's
- Instruction Tuned LLM's

## Based Language Models (BLMs)

BLMs are the foundational models upon which various natural language processing tasks are built. They are pre-trained on vast amounts of text data and excel at predicting the next word in a sequence of words. The pre-training process is unsupervised, meaning the model learns to predict words based on patterns in the text data, without any specific task in mind.

**Characteristics of BLMs:**

- Pre-trained on a large corpus of text data.
- Unsupervised pre-training process.
- General-purpose models.
- Can be used for a wide range of tasks.

## Instruction Tuned Language Models (ITLMs)

ITLMs are a specialized type of BLMs that undergo a fine-tuning process tailored to a specific task. During fine-tuning, these models are provided with explicit instructions to follow, enabling them to generate output in line with those instructions. The fine-tuning process is supervised, as it involves training the model with specific examples of inputs and desired outputs for the given task.

**Characteristics of ITLMs:**

- Fine-tuned on a specific task with explicit instructions.
- Supervised fine-tuning process.
- Task-specific models.
- Designed to perform a particular task with precision.

## A Practical Example

To illustrate the difference between BLMs and ITLMs, let's consider a scenario:

**Scenario**: Building a Customer Query Chatbot

Suppose you aim to develop a chatbot capable of addressing customer queries about your product. You could utilize a BLM like GPT-3 as the foundational model for your chatbot. However, since GPT-3 is a general-purpose model, it may not consistently provide accurate answers to all customer queries.

To enhance the accuracy of your chatbot, you can fine-tune GPT-3 for the specific task of answering customer queries about your product. During this fine-tuning process, you would provide GPT-3 with examples of customer queries and their corresponding answers. GPT-3 would then learn to generate accurate responses based on these examples.

## Summary

In summary, BLMs are versatile models trained on a wide range of text data, suitable for a variety of tasks, while ITLMs are fine-tuned models tailored to perform specific tasks with precision.

| **Based Language Models (BLMs)** | **Instruction Tuned Language Models (ITLMs)** |
|-----------------------------|----------------------------------------|
| Pre-trained on large corpus of text data | Fine-tuned on specific task |
| Unsupervised pre-training process | Supervised fine-tuning process |
| General-purpose models | Task-specific models |
| Can be used for a wide range of tasks | Designed to perform a specific task |

These distinctions are crucial in understanding how language models are harnessed for different applications in natural language processing.

*Sources:*

1. [Large Language Models and the Future of Custom, Fine-tuned LLMs](https://outerbounds.com/blog/custom-llm-tuning/).
2. [Instruction Tuning of Large Language Models](https://self-supervised.cs.jhu.edu/sp2023/files/Instruction%20tuning%20of%20LLMs%20-%20Talk@JHU.pdf).
3. [Table-GPT: Empower LLMs To Understand Tables - Medium](https://medium.com/@aipapers/table-gpt-empower-llms-to-understand-tables-9b60a3df1eae).
4. [Instruction Tuning for Large Language Models: A Survey](https://arxiv.org/abs/2308.10792).
