from openai import OpenAI
import streamlit as st
import json
import code 


st.markdown("""
    <style>
    h1 {
        color: #8B0000;  /* Dark red color for the header */
    }
    </style>
    """, unsafe_allow_html=True)


st.title("💬Code Review")


code = st.text_area("Enter your python code here",height=200)


client = OpenAI(api_key = "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")


if st.button("Review Code") == True:

    response = client.chat.completions.create(
                model = 'gpt-3.5-turbo-0125',
                messages=[

            {"role": "system", "content": """
             
             You are a friendly AI Assistant. You take a python code as an input from the user.

             Your job is to explain the bugs and generate the fixed code as an output.

             Your output is a JSON with the following structure:

             {"Bugs": "review_on_code": python fixed_code}

             """},

             {"role": "user", "content": f"fix and explain the bugs in the following python code: {code}"}

        ],
        
        temperature=0.5
    )

    review = (response.choices[0].message.content)



    st.subheader("Code Review")


    st.write(review)