# GPT Actions

GPT Actions are stored in Custom GPTs, which enable users to customize ChatGPT for specific use cases by providing instructions, attaching documents as knowledge, and connecting to 3rd party services.

GPT Actions empower ChatGPT users to interact with external applications via RESTful APIs calls outside of ChatGPT simply by using natural language. They convert natural language text into the json schema required for an API call. GPT Actions are usually either used to do [data retrieval](#data-retrieval) to ChatGPT (e.g. query a Data Warehouse) or take action in another application (e.g. file a JIRA ticket).

## How GPT actions work

At their core, GPT Actions leverage [Function Calling](../5-function-calling/Readme.md) to execute API calls.

Similar to ChatGPT's Data Analysis capability (which generates Python code and then executes it), they leverage Function Calling to (1) decide which API call is relevant to the user's question and (2) generate the json input necessary for the API call. Then finally, the GPT Action executes the API call using that json input.

Developers can even specify the authentication mechanism of an action, and the Custom GPT will execute the API call using the third party app’s authentication. GPT Actions obfuscates the complexity of the API call to the end user: they simply ask a question in natural language, and ChatGPT provides the output in natural language as well.

Learn more: <https://platform.openai.com/docs/actions/introduction>

### Data Retrieval

One of the most common tasks an action in a GPT can perform is data retrieval. An action might:

1. Access an API to retrieve data based on a keyword search
2. Access a relational database to retrieve records based on a structured query
3. Access a vector database to retrieve text chunks based on semantic search

Learn more: <https://platform.openai.com/docs/actions/data-retrieval>

### How to create a GPT Action

To create a GPT Action, you need to have ChatGPT plus subscription, if you have then you need to follow these steps:

1. **Create a Custom GPT**: Create a Custom GPT in the ChatGPT dashboard.
2. **Add Instructions**: Add instructions to the Custom GPT to guide the user on how to use the GPT Action.
3. **Attach Knowledge**: Attach documents or links to the Custom GPT to provide context to the user.
4. **Connect to 3rd Party Services**: Connect the Custom GPT to 3rd party services by adding API keys and endpoints.
5. **Test the GPT Action**: Test the GPT Action to ensure it works as expected.
