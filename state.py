from typing import TypedDict, List, Dict, Any, Optional

class MASState(TypedDict):
    user_prompt: str
    plan: Optional[str]
    architecture: Optional[str]
    generated_files: Optional[Dict[str, str]]
    security_report: Optional[str]
    security_status: Optional[str]
    fix_count: int
    messages : List[str]

# class MASState(TypedDict):
#     user_prompt: str
#     plan: Optional[str]
#     messages: List[str]