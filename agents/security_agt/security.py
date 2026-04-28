from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

from .prompt import security_prompt


llm = ChatOllama(model="llama3", temperature=0.5)


def _get_code_output(state):
	return (
		state.get("code_output")
		or state.get("generated_files")
		or state.get("architecture")
		or ""
	)


def security_agent(state):
	prompt = security_prompt(_get_code_output(state))
	response = llm.invoke([HumanMessage(content=prompt)])
	result = response.content.strip()

	if result == "SECURITY_OK":
		return {
			**state,
			"security_status": "OK",
			"security_report": "",
			"messages": state.get("messages", []) + ["Security check passed."],
		}

	return {
		**state,
		"security_status": "ISSUES",
		"security_report": result,
		"messages": state.get("messages", []) + ["Security issues found. Sending back to coder."],
	}
