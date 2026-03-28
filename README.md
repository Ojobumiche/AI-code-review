🧠 AI Code Reviewer (Python)

An AI-powered code analysis tool that reviews Python code, detects bugs, suggests improvements, evaluates time complexity, and generates optimized refactored versions using large language models.

---------------------------------------------------------------------------------------------------------------

🚀 Overview

The AI Code Reviewer is designed to simulate how developers interact with AI systems for code analysis and improvement.  
It focuses on structured reasoning, clear feedback, and actionable insights, rather than just generating text.

This project demonstrates practical skills in:
- AI integration
- Prompt engineering
- Backend logic
- Developer tooling

-------------------------------------------------------------------------------------------------------------------

✨ Features

🔍 Bug Detection** — Identifies logical and syntactical issues  
⚡ Code Improvements** — Suggests optimizations and best practices  
📈 Time Complexity Analysis** — Evaluates algorithm efficiency  
✅ Refactored Code Generation** — Produces cleaner, optimized code  
🏆 Code Quality Score (1–10)** — Rates overall code quality  
📂 File Upload Support** — Analyze `.py` files directly  
🎯 Custom Review Focus** — Choose between:
  - Security
  - Efficiency
  - Readability
  - Bugs  

-------------------------------------------------------------------------------------------------------------------

🛠 Tech Stack

- Language: Python  
- Framework: Streamlit  
- AI Integration: OpenAI API  
- Libraries:  
  - streamlit 
  - openai`  
  - re (for structured parsing)

-----------------------------------------------------------------------------------------------------------------

🧠 How It Works

1. User inputs Python code (via text or file upload)  
2. A structured prompt is sent to the AI model  
3. The model analyzes the code and returns:
   - Bugs
   - Improvements
   - Time complexity
   - Refactored version
4. The app parses and displays results in a clean UI  

------------------------------------------------------------------------------------------------------------

📸 Demo (Optional)



------------------------------------------------------------------------------------------------------------------

▶️ Run Locally

 1. Clone the repository

bash
git clone https://github.com/Ojobumiche/AI-code-review.git
cd AI-code-review

2. Create a virtual environment

python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies

bash>
pip install -r requirements.txt

4. Set up environment variables

bash>
.streamlit/secrets.toml
Add:
OPENAI_API_KEY = "your-api-key"

5. Run the app

python -m streamlit run app.py

----------------------------------------------------------------------------------------

👨‍💻 Author:

Joshua Alfa Monday

GitHub: https://github.com/Ojobumiche
Email: bumiche@gmail.com
