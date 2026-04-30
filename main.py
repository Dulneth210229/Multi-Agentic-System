from langgraph.graph import StateGraph, END

from state import MASState
from agents.planner_agt.planner import planner_agent
from agents.architect_agt.architect import architect_agent
from agents.coder_agt.coder import coder_agent

def build_graph():
    graph = StateGraph(MASState)

    #initialize the node
    graph.add_node("planner", planner_agent)
    graph.add_node("architect", architect_agent)
    graph.add_node("coder", coder_agent)

    #set the entry point for the graph
    graph.set_entry_point("planner")

    #add edges between the nodes
    graph.add_edge("planner", "architect")
    graph.add_edge("architect", "coder")
    return graph.compile()

if __name__ == "__main__":
    app = build_graph()

    user_prompt = input("Enter your software requirements: ")

    initial_state = {
        "user_prompt": user_prompt,
        "plan": None,
        "architecture": None,
        "generated_files": None,
        "security_report": None,
        "security_status": None,
        "fix_count": 0,
        "messages": []
    }

    result = app.invoke(initial_state)

    print("\n===== PLANNER OUTPUT =====\n")
    print(result.get("plan", "No plan generated."))

    print("\n===== ARCHITECT OUTPUT =====\n")
    print(result.get("architecture", "No architecture generated."))

    print("\n===== CODER OUTPUT =====")
    print("Files generated inside generated_apps/")

    # print("\n===== WORKFLOW COMPLETED =====")
    # print("\nSecurity Status:", final_state["security_status"])
    # print("\nSecurity Report:\n", final_state["security_report"])
    # print("\nMessages:")
    # for message in final_state["messages"]:
    #     print("-", message)

    # print("\nGenerated files are saved inside the generated_apps folder.")