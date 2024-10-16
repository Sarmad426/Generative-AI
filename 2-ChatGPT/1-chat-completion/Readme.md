# Chat Completion API

Chat models take a list of messages as input and return a model-generated message as output. Although the chat format is designed to make multi-turn conversations easy, it’s just as useful for single-turn tasks without any conversation.

Chat Completion API is stateless. It does not remember the session chat, instead all the previous chat data is passed to it on a new call. Which makes it fairly expensive as more the number of tokens the more the bill will be charged.

An example Chat Completions API call looks like the following:

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
```

The main input is the messages parameter. Messages must be an array of message objects, where each object has a role (either "system", "user", or "assistant") and content. Conversations can be as short as one message or many back and forth turns.

For more details, see the [documentation](https://platform.openai.com/docs/guides/text-generation/chat-completions-api)
