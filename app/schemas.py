from pydantic import BaseModel

class ResumeCreate(BaseModel):
    name: str
    content: str

class JobCreate(BaseModel):
    title: str
    description: str

class MatchResponse(BaseModel):
    resume_id: int
    job_id: int
    score: float
