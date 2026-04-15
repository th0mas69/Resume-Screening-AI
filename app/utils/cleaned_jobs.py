import pandas as pd
import re

# ---------------------------
# Text Cleaning Function
# ---------------------------
def clean_text(text):
    if pd.isna(text):
        return ""
    
    text = text.lower()  # lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)  # remove special characters
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    
    return text

# ---------------------------
# Load CSV files
# ---------------------------
df1 = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/jobs/job_postings.csv")
df2 = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/jobs/data.csv")

# Remove hidden spaces in column names
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Print column names
print("DF1 columns:", df1.columns)
print("DF2 columns:", df2.columns)


# Replace 'YourColumnNameHere' with actual column name you see printed
df1["description"] = df1["description"].apply(clean_text)
df2["Description"] = df2["Description"].apply(clean_text)

# ---------------------------
# Save cleaned files
# ---------------------------
df1.to_csv("job1_cleaned.csv", index=False)
df2.to_csv("job2_cleaned.csv", index=False)

print("Cleaning completed successfully.")
