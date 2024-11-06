import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests
import pandas as pd
# from langchain.llms import OpenAI
from openai import OpenAI


def create_example_page():
    """
    Below is an example of what you can do with just a few lines of code:
    """

    st.title("🦜🔗 Langchain Quickstart App")

    openai_api_key = st.text_input("OpenAI API Key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

    def generate_response(input_text):
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": input_text
                },
            ],
            temperature=0.7,
        )
        comment = response.choices[0].message.content
        # text = f"This is a LLM-generated comment for `{filename}`: \n{comment if comment else 'Tests passed. No feedback generated for testing purposes.'}"
        st.info(comment)
        
        # llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        # st.info(llm(input_text))

    with st.form("my_form"):
        text = st.text_area("Enter text:",
                            "What are 3 key advice for learning how to code?")
        submitted = st.form_submit_button("Submit")
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
        elif submitted:
            client = OpenAI(api_key=openai_api_key)
            # generate_response(text)

    st.markdown("""
              This page was created by and copied from Streamlit. See the application deployed [here](https://llm-examples.streamlit.app/Chat_with_search).
              
              Source code: [https://github.com/streamlit/llm-examples/blob/main/pages/3_Langchain_Quickstart.py](https://github.com/streamlit/llm-examples/blob/main/pages/3_Langchain_Quickstart.py)
              """)


if __name__ == '__main__':
    create_example_page()
