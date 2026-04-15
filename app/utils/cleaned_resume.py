import pandas as pd
from app.utils.text_cleaner import preprocess_text

# Load extracted data
df = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/resumes_extracted.csv")

print("Cleaning resumes...")

# Apply preprocessing
df["cleaned_text"] = df["resume_text"].apply(
    lambda x: preprocess_text(str(x))
)

# Save cleaned file
df.to_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/resumes_cleaned.csv", index=False)

print("Cleaning complete.")
print("Total resumes processed:", len(df))
