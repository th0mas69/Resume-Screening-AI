""""from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def get_embedding(text):
    return model.encode(text)"p"""

import pandas as pd
from sentence_transformers import SentenceTransformer, util

# -------------------------
# Load cleaned datasets
# -------------------------
resumes = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/resumes_cleaned.csv")
jobs = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/job2_cleaned.csv")

# -------------------------
# Create Resume–Job Pairs
# -------------------------
resumes["key"] = 1
jobs["key"] = 1

pairs = pd.merge(resumes, jobs, on="key").drop("key", axis=1)

print("Pairs created:", len(pairs))
print("Columns in pairs:", pairs.columns)



# -------------------------
# Load embedding model
# -------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------
# Generate embeddings
# -------------------------
pairs["resume_embedding"] = pairs["resume_text"].apply(lambda x: model.encode(x))
pairs["job_embedding"] = pairs["cleaned_description"].apply(lambda x: model.encode(x))

# -------------------------
# Compute similarity
# -------------------------
pairs["similarity_score"] = pairs.apply(
    lambda row: util.cos_sim(row["resume_embedding"], row["job_embedding"]).item(),
    axis=1
)

print(pairs[["resume_id", "job_id", "similarity_score"]].head())


