from sqlalchemy.orm import Session
from app import models, schemas


# =========================
# RESUME CRUD OPERATIONS
# =========================

def create_resume(db: Session, resume: schemas.ResumeCreate):
    db_resume = models.Resume(
        name=resume.name,
        content=resume.content
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return db_resume


def get_resume(db: Session, resume_id: int):
    return db.query(models.Resume).filter(models.Resume.id == resume_id).first()


def get_all_resumes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Resume).offset(skip).limit(limit).all()


def update_resume_score(db: Session, resume_id: int, score: float):
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if resume:
        resume.embedding_score = score
        db.commit()
        db.refresh(resume)
    return resume


def delete_resume(db: Session, resume_id: int):
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if resume:
        db.delete(resume)
        db.commit()
    return resume


# =========================
# JOB CRUD OPERATIONS
# =========================

def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(
        title=job.title,
        description=job.description
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()


def get_all_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Job).offset(skip).limit(limit).all()


def delete_job(db: Session, job_id: int):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if job:
        db.delete(job)
        db.commit()
    return job
