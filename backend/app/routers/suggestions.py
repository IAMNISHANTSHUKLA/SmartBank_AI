from fastapi import APIRouter
from app.rl_agent import generate_suggestion

router = APIRouter(prefix="/suggestions", tags=["suggestions"])

@router.get("/smart/{user_id}")
def smart_suggestions(user_id: int):
    suggestion = generate_suggestion(user_id)
    return {"suggestion": suggestion}
