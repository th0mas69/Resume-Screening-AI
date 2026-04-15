SKILLS = [
    "python", "java", "sql", "machine learning", "data analysis",
    "deep learning", "nlp", "excel", "power bi", "tableau",
    "communication", "project management", "aws", "docker", "problem-solving", "leadership", 
    "organization", "adapatability", "teamwork", "digital literacy", "written communication",
    "active listening", "reporting", "documenting", "web design", "data visualization", 
    "web design", "photo and video editing", "typography", "user interface", "user experience",
    "Statistical analysis", "Information processing", "compliance", "microsoft office", "microsoft excel", "sheets", "powerpoint",
    "accounting", "digital marketing", "SEO", "Game developer", "quality control", "testing", "manual QA"
]

def extract_skills(text):
    text = str(text).lower()
    return {skill for skill in SKILLS if skill in text}


def compute_skill_overlap(resume_skills, job_skills):
    if len(job_skills) == 0:
        return 0
    return len(resume_skills & job_skills) / len(job_skills)