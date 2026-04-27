from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOllama(model="qwen3-coder", temperature=0.5)

def planner_agent(state):
        prompt = f"""
You are a senior software project planner.

User request:
{state["user_prompt"]}

Create a clear software development plan.

Include:
1. Project goal
2. Main features
3. Technologies
4. Pages/components needed
5. Development steps
6. Testing expectations

Return only the plan.
"""
        response = llm.invoke([HumanMessage(content = prompt)])

        return {
                **state,
                "plan": response.content,
                "messages": state["messages"] + [f"Planner completed the software plan."]
        }