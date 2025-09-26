### Math Ai Helper - CLI program using Jac + byLLM((Jac + Gemini))

This project demonstrates a simple Jac program that uses Gemini 2.0 via the `byllm` Python library to explain addition problems.

It combines:

- Jac language for defining walkers and behaviors.
- Gemini AIfor natural language explanations.
- Python to manage environment variables and run Jac scripts securely.

## Features

- Performs addition of two numbers.
- Calls Gemini API to generate a step-by-step explanation of the addition.
.env — (local) environment file storing your OPENAI_API_KEY (do not commit this file).

## Setup

1. **Clone the repository**
2.  **Create a Python environment**
python -m venv jac-env-3.12
source jac-env-3.12/bin/activate

3.**Install dependencies**
pip install python-dotenv byllm

4 **Add your Gemini API key**
-Create a .env file in the project root: and put your API_KEY there
-GEMINI_API_KEY=your_gemini_api_key_here
-Make sure .env is included in .gitignore so your API key is not pushed to GitHub.

5.**Running the Program**
python run_math_helper.py

**my output examples**
5 + 3 = 8
AI Explains:
1. Start with the number 5...
2. Add 3 to it step by step...


**License & Security**

This repository may contain examples that call external LLM APIs. Do not store secrets in version control. Treat GEMINI_API_KEY as sensitive.