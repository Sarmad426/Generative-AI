# Multi pages

As apps grow large, it becomes useful to organize them into multiple pages. This makes the app easier to manage as a developer and easier to navigate as a user. Streamlit provides a frictionless way to create multi-page apps. Pages are automatically shown in a nice navigation widget inside the app sidebar, and clicking on a page will navigate to the page without reloading the frontend — making app browsing incredibly fast! In this guide, let’s learn how to create multi-page apps.

Docs: <https://docs.streamlit.io/library/advanced-features/multipage-apps#multipage-apps>

## Process

In order to add multiple pages in the application, create a `pages` folder in the project and create files inside this folder. Streamlit automatically converts these files to an individual route. Name the files as `1_file.py` , `2_file.py` to sort them.
