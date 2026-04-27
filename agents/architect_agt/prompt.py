def architect_prompt(state) -> str:
    return f"""
You are a senior software architect.

User request:
{state["user_prompt"]}

Planner output:
{state["plan"]}

Design a simple but clean architecture.

Include:
1. Architecture style
2. Folder structure
3. File list
4. Responsibility of each file
5. Data flow
6. Security considerations

For this assignment, use simple frontend architecture if the request is HTML/CSS/JS.

Return only the architecture design.
"""