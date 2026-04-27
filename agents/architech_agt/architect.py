from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from .prompt import architect_prompt

llm = ChatOllama(model="llama3", temperature=0.5)

def architect_agent(state):
    prompt = architect_prompt(state["user_prompt"]["plan"])
    response = llm.invoke([HumanMessage(content = prompt)])

    return {
        **state,
        "architecture": response.content,
        "messages": state["messages"] + [f"Architect completed the software architecture."]
    }