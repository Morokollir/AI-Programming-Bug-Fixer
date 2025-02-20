import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def fix_bug(code, bug_description):
    prompt = (
        f"Below is a Python code snippet with a bug:\n\n{code}\n\n"
        f"Bug description: {bug_description}\n\n"
        "Please provide a corrected version of the code with an explanation of the fix."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert Python developer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=250
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("Enter the problematic code (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    code_snippet = "\n".join(lines)
    
    bug_description = input("Describe the bug: ")
    fixed_code = fix_bug(code_snippet, bug_description)
    print("\nFixed Code and Explanation:\n", fixed_code)
