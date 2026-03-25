import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="mczwPSvwafFci001pBHB")

st.title("AI Code Reviewer (Python)")

code_input = st.text_area("Paste your Python code here:")

if st.button("Analyze Code"):
    if code_input:
        prompt = f"""
        You are a senior Python engineer.

        Analyze this code:
        {code_input}

        Provide:
        1. Bugs/issues
        2. Improvements
        3. Time complexity
        4. Refactored version
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.write(response.choices[0].message.content)
