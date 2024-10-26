# Prompt Engineering

**Prompt Engineering** is the process of refining prompts that a person can input into a generative artificial intelligence (AI) service to generate text or images. It involves selecting the right words, phrases, symbols, and formats that guide the model in generating high-quality and relevant texts. The goal of prompt engineering is to create effective prompts that can help users achieve their desired outcomes and improve the performance of AI models.

## Best Practices

- Be specific, descriptive, and detailed about the desired context, outcome, length, format, style, etc.

- Use clear and concise language to ensure prompt effectiveness.

- Include relevant context to aid model understanding.

- Use examples to articulate the desired output format.

- Start with zero-shot, then few-shot, and finally fine-tune the model.

## Guidelines

### Principle 1: Write Clear and Specific instructions

**Tactics:**

1. Use delimiters: triple quotes (`"""`), triple dashes (`---`), triple backticks (``````), or XML tags.

> This avoids prompt injections, and it also makes it easier for the LLM to identify specific content.

1. Ask for structured output. like (json, xml,html, etc).
2. Check whether conditions are satisfied.
3. Few Shot Prompting. (Give Successful example).

## Principle 2: Giving the Model Time to Think

**Tactics:**

- Specify the steps to complete a task.

```txt
step 1: 
step 2:
step 3
........
........
........
step N:
```

- Instruct the Model to work on its own solution before rushing to conclusion.
