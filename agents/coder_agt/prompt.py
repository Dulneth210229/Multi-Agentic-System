def coder_prompt(state) -> str:
    return f"""
You are a strict coding agent.

User Request:
{state["user_prompt"]}

Planner Output:
{state["plan"]}

Architecture Output:
{state["architecture"]}

Generate FULL working project code.

⚠️ VERY IMPORTANT:
You MUST follow this format EXACTLY.
If you fail, the system will break.

Output ONLY this format:

FILE: index.html
<html>
...
</html>
END_FILE

FILE: style.css
body {{
...
}}
END_FILE

FILE: script.js
document.addEventListener(...)
END_FILE

Rules:
- NO markdown (no ``` symbols)
- NO explanations
- NO extra text
- ONLY FILE blocks
- Use clean modern UI
- Use safe JavaScript (no eval)
"""