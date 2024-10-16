# Session State

For each browser tab that connects to the Streamlit server, a new session is created. Streamlit reruns your script from top to bottom every time you interact with your app. Each reruns takes place in a blank slate: no variables are shared between runs.

Session State is a way to share variables between reruns, for each user session. In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks. Session state also persists across apps inside a multipage app.

<https://docs.streamlit.io/library/api-reference/session-state>

<https://docs.streamlit.io/library/advanced-features/session-state>
