def planner_prompt(user_prompt: str) -> str:
    return f"""
You are a senior software project planner.

User request:
{user_prompt}

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