from agents.architect_agt.architect import architect_agent


def test_architect():
    state = {
        "user_prompt": "Generate a simple calculator using HTML, CSS, JS",
        "plan": """
        Application Goal:
        Build a simple calculator web application.

        Main Features:
        - Addition
        - Subtraction
        - Multiplication
        - Division
        - Clear button
        - Responsive UI

        Technologies:
        - HTML
        - CSS
        - Vanilla JavaScript
        """,
        "architecture": None,
        "messages": []
    }

    result = architect_agent(state)

    print("\n===== ARCHITECT OUTPUT =====\n")
    print(result["architecture"])

    print("\n===== LOGS =====")
    for msg in result["messages"]:
        print("-", msg)


if __name__ == "__main__":
    test_architect()