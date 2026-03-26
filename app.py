import streamlit as st
from openai import OpenAI

client = OpenAI(OPENAI_API_KEY)

st.title("AI Code Reviewer (Python)")

# Sidebar for configuration
st.sidebar.header("Review Settings")
model = st.sidebar.selectbox("Select Model", ["GPT-4", "Claude 3.5 Sonnet"])
temp = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2)
focus = st.sidebar.multiselect("Review Focus", ["Security", "Efficiency", "Readability", "Bugs"], default=["Bugs"])


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
