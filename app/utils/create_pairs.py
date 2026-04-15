import pandas as pd
from sentence_transformers import SentenceTransformer, util
from app.services.feature_engineering import extract_skills, compute_skill_overlap

# -------------------------
# Load cleaned datasets
# -------------------------
resumes = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/resumes_cleaned.csv")
jobs = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/job2_cleaned.csv")

# -------------------------
# Fix column names (IMPORTANT)
# -------------------------
resumes.columns = resumes.columns.str.strip().str.lower()
jobs.columns = jobs.columns.str.strip().str.lower()

print("Resumes columns:", resumes.columns)
print("Jobs columns:", jobs.columns)



# -------------------------
# Create all combinations
# -------------------------
resumes["key"] = 1
jobs["key"] = 1

pairs = pd.merge(resumes, jobs, on="key").drop("key", axis=1)

print("Total pairs:", len(pairs))


# -------------------------
# Load embedding model
# -------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# Encode all at once 
print("Encoding resumes...")
resume_embeddings = model.encode(resumes['resume_text'].astype(str).tolist(), show_progress_bar=True)

print("Encoding jobs...")
job_embeddings = model.encode(jobs['description'].astype(str).tolist(), show_progress_bar=True)


# -------------------------
# Create pairs + similarity
# -------------------------
results = []

for i, r_id in resumes.iterrows():
    r_skills = extract_skills(r_id['cleaned_text'])
    for j, j_id in jobs.iterrows():
        j_skills = extract_skills(j_id['description'])

        
        sim = util.cos_sim(resume_embeddings[i], job_embeddings[j]).item()
        overlap = compute_skill_overlap(r_skills, j_skills)
        
        results.append({
            "file_name": r_id,
            "job_title": j_id,
            "similarity_score": sim,
            "skill_overlap": overlap,
            "label": 1 if sim > 0.7 else 0
        })

# -------------------------
# Save
# -------------------------
df = pd.DataFrame(results)
df.to_csv("data/pairs.csv", index=False)

print("pairs.csv created successfully!")

