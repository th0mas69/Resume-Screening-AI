from app.utils.text_cleaner import preprocess_text
from app.services.embedding import get_embedding
from sklearn.metrics.pairwise import cosine_similarity


def match_resume_job(resume_text, job_text):

    resume_text = preprocess_text(resume_text)
    job_text = preprocess_text(job_text)

    resume_vec = get_embedding(resume_text)
    job_vec = get_embedding(job_text)

    score = cosine_similarity(
        [resume_vec], [job_vec]
    )[0][0]

    return float(score)
