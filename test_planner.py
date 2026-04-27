from agents.planner_agt.planner import planner_agent


def test_planner():
    state = {
        "user_prompt": "Generate a simple calculator using HTML, CSS, JS",
        "plan": None,
        "messages": []
    }

    result = planner_agent(state)

    print("\n===== PLANNER OUTPUT =====\n")
    print(result["plan"])

    print("\n===== LOGS =====")
    for msg in result["messages"]:
        print("-", msg)


if __name__ == "__main__":
    test_planner()