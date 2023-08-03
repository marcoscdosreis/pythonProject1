import os

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"
os.environ["OPENAI_API_BASE"] = "https://jp-sandbox.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "b45bc8447cbd4146b10021c22d916353"

import streamlit as st
from langchain.llms import OpenAI

st.title('Customer Service Sentiment App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')


def generate_response(input_text):
  llm = OpenAI(temperature=0.7, model_name='gpt-4')
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
 # if not openai_api_key.startswith('sk-'):
   # st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted:
    generate_response(text)
