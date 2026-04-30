import os
import re

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

from .prompt import coder_prompt

llm = ChatOllama(model="llama3", temperature=0.3)


OUTPUT_DIR = "generated_apps"


def extract_files(response_text):
    pattern = r"FILE:\s*(.+?)\n([\s\S]*?)END_FILE"
    matches = re.findall(pattern, response_text, re.DOTALL)

    files = {}

    for filename, content in matches:
        files[filename.strip()] = content.strip()

    return files


def save_files(files):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename, content in files.items():

        filepath = os.path.join(OUTPUT_DIR, filename)

        folder = os.path.dirname(filepath)

        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)


def coder_agent(state):

    prompt = coder_prompt(state)

    response = llm.invoke([HumanMessage(content=prompt)])

    print("\n===== RAW LLM OUTPUT =====\n")
    print(response.content)

    generated = extract_files(response.content)

    print("\n===== EXTRACTED FILES =====\n", generated)

    save_files(generated)

    return {
        **state,
        "generated_files": generated,
        "messages": state["messages"] + [
            "Coder agent generated project files."
        ]
    }