from langchain_ollama import ChatOllama # type: ignore
from langchain_core.messages import HumanMessage, SystemMessage
from .prompt import planner_prompt

llm = ChatOllama(model="llama3", temperature=0.5)

def planner_agent(state):
        prompt = planner_prompt(state["user_prompt"])
        response = llm.invoke([HumanMessage(content = prompt)])

        return {
                **state,
                "plan": response.content,
                "messages": state["messages"] + [f"Planner completed the software plan."]
        }