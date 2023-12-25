# Guidelines

## Principle 1: Write Clear and Specific instructions

### Tactics

1. Use delimiters: triple quotes (`"""`), triple dashes (`---`), triple backticks (`````), or XML tags.

> This avoids prompt injections, and it also makes it easier for the LLM to identify specific content.

1. Ask for structured output. like (json, xml,html, etc).
2. Check whether conditions are satisfied.
3. Few Shot Prompting. (Give Successful example).

## Principle 2: Giving the Model Time to Think

### - Tactics

* Specify the steps to complete a task.

```pseudo
step 1: 
step 2:
step ...
........
step N:
```

* Instruct the Model to work on its own solution before rushing to conclusion.
