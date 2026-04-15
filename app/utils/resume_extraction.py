import os
from pdfminer.high_level import extract_text
import pandas as pd

DATA_PATH = r"C:\Users\tluke\Desktop\Resume Screening Project\data\resumes"
records = []

for root, dirs, files in os.walk(DATA_PATH):
    for file in files:
        if file.endswith(".pdf"):
            file_path = os.path.join(root, file)

            try:
                text = extract_text(file_path)

                # Extract domain from folder name
                domain = os.path.basename(root)

                records.append({
                    "file_name": file,
                    "domain": domain,
                    "resume_text": text
                })

            except Exception as e:
                print(f"Error reading {file}: {e}")

df = pd.DataFrame(records)
df.to_csv("data/resumes_extracted.csv", index=False)

print("Extraction complete.")
