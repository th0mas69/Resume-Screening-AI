import pandas as pd

# Load cleaned datasets
resumes = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/resumes_cleaned.csv")
jobs = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/job2_cleaned.csv")

# Create Cartesian product
resumes["key"] = 1
jobs["key"] = 1

pairs = pd.merge(resumes, jobs, on="key").drop("key", axis=1)

print(pairs.head())
