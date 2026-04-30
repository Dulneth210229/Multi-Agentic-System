from agents.coder_agt.coder import coder_agent


def test_coder():
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

        "architecture": """
        Architecture Style:
        Simple frontend (static web app)

        Folder Structure:
        generated_apps/
            index.html
            style.css
            script.js

        File Responsibilities:
        - index.html → UI structure
        - style.css → Styling
        - script.js → Logic

        Data Flow:
        User input → JS logic → Update display
        """,

        "generated_files": None,
        "security_report": None,
        "security_status": None,
        "fix_count": 0,
        "messages": []
    }

    result = coder_agent(state)

    print("\n===== CODER OUTPUT =====")

    generated = result.get("generated_files", {})

    if generated:
        print("Generated files:")
        for file in generated:
            print("-", file)
    else:
        print("No files generated.")

    print("\n===== LOGS =====")
    for msg in result["messages"]:
        print("-", msg)


if __name__ == "__main__":
    test_coder()