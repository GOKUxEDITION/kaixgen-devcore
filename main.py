from fastapi import FastAPI
from core.ai_engine import AIEngine
from core.access_control import AccessControl

app = FastAPI(title="KAIxGen DevCore API")

ai_engine = AIEngine()
access_control = AccessControl()


@app.get("/")
def root():
    return {"status": "KAIxGen DevCore Running"}


@app.get("/generate/")
def generate(prompt: str, user_id: int):
    if not access_control.validate_user(user_id):
        return {"error": "Access Denied"}

    response = ai_engine.generate_response(prompt)
    return {"response": response}
