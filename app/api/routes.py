from fastapi import APIRouter
from app.services.matcher import match_resume_job

router = APIRouter()

@router.post("/match/")
def match(resume_text: str, job_text: str):
    score = match_resume_job(resume_text, job_text)
    return {"match_score": score}
