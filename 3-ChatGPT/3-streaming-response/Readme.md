# Streaming Response

By default, when you request a completion from the OpenAI, the entire completion is generated before being sent back in a single response.

If you're generating long completions, waiting for the response can take many seconds.

To get responses sooner, you can 'stream' the completion as it's being generated. This allows you to start printing or processing the beginning of the completion before the full completion is finished.

To stream completions, set `stream=True` when calling the chat completions or completions endpoints. This will return an object that streams back the response as data-only server-sent events. Extract chunks from the delta field rather than the message field.

Note that using stream=True in a production application makes it more difficult to moderate the content of the completions, as partial completions may be more difficult to evaluate. This may have implications for approved usage.

Another small drawback of streaming responses is that the response no longer includes the usage field to tell you how many tokens were consumed. After receiving and combining all of the responses, you can calculate this yourself using tiktoken.
