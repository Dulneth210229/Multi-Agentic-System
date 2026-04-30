def security_prompt(code_output: str) -> str:
	return f"""
You are a senior security reviewer.

Review the following generated code or output for security problems:

{code_output}

Check for:
1. Use of eval()
2. Inline JavaScript risks
3. Unsafe DOM manipulation
4. Input validation issues
5. XSS risks
6. General frontend security issues

If security is okay, reply exactly:
SECURITY_OK

If there are issues, reply in this format:
SECURITY_ISSUES:
- issue 1
- issue 2
- suggested fixes

Return only the security result.
"""
