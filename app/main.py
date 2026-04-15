from fastapi import FastAPI
from app.api.routes import router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Resume Screening Tool")

app.include_router(router)
