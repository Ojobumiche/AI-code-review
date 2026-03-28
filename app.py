import streamlit as st
from openai import OpenAI
import re

# Load API key securely
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🧠 AI Code Reviewer (Python)")
st.caption("Analyze, optimize, and improve your Python code using AI")

# Sidebar
st.sidebar.header("⚙️ Review Settings")

model = st.sidebar.selectbox(
    "Select Model",
    ["gpt-4o-mini", "gpt-4o"]
)

temperature = st.sidebar.slider(
    "Temperature",
    0.0, 1.0, 0.2
)

focus = st.sidebar.multiselect(
    "Review Focus",
    ["Security", "Efficiency", "Readability", "Bugs"],
    default=["Bugs"]
)

# File upload
uploaded_file = st.file_uploader("Upload a Python file", type=["py"])

if uploaded_file:
    code_input = uploaded_file.read().decode("utf-8")
else:
    code_input = st.text_area("Paste your Python code here:")

# Helper function
def extract_section(text, title):
    pattern = rf"{title}:\n(.*?)(\n\n|$)"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else "Not provided"

# Button
if st.button("Analyze Code"):
    if code_input:

        prompt = f"""
You are an expert Python engineer and AI code reviewer.

Focus on: {", ".join(focus)}

Analyze the following code and respond in this format:

Bugs:
- ...

Improvements:
- ...

Time Complexity:
- ...

Refactored Code:
```python
...

    with st.spinner("Analyzing code..."):

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )

    result = response.choices[0].message.content

    # Extract sections
    bugs = extract_section(result, "Bugs")
    improvements = extract_section(result, "Improvements")
    complexity = extract_section(result, "Time Complexity")
    refactored = extract_section(result, "Refactored Code")
    score = extract_section(result, "Code Quality Score")

    # Display results
    st.subheader("🔍 Bugs")
    st.write(bugs)

    st.subheader("⚡ Improvements")
    st.write(improvements)

    st.subheader("📈 Time Complexity")
    st.write(complexity)

    st.subheader("🏆 Code Quality Score")
    st.metric("Score", score)

    st.subheader("✅ Refactored Code")
    st.code(refactored, language="python")

else:
    st.warning("Please provide code input.")

st.write("_Built by Joshua")

"""
