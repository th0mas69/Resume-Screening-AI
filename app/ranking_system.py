import pandas as pd

df = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/pairs.csv")

# Rank resumes per job
df["rank"] = df.groupby("job_id")["similarity_score"].rank(ascending=False)

# Get top 5 resumes per job
top_matches = df.sort_values(["job_id", "rank"]).groupby("job_id").head(5)

print(top_matches[["job_id", "resume_id", "similarity_score", "rank"]])