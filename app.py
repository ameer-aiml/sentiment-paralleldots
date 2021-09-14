import streamlit as st
import paralleldots
import os

st.title("Sentiment Analyser")
api_key = os.getenv('api_key')
paralleldots.set_api_key(api_key)


# for single sentence
text=st.text_input("Enter your sentence")
lang_code="en"
response=paralleldots.sentiment(text,lang_code)
if st.button("Analyse"):
    st.write(f"Negative :{response['sentiment']['negative']*100 :.2f} %")
    st.write(f"Neutral :{response['sentiment']['neutral']*100 :.2f} %")
    st.write(F"Positive :{response['sentiment']['positive']*100 :.2f} %")
    
