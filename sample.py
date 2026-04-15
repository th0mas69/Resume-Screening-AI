import os
from pdfminer.high_level import extract_text

DATA_PATH = r"C:\Users\tluke\Desktop\Resume Screening Project\data\resumes"

print("Checking folder:", DATA_PATH)

if not os.path.exists(DATA_PATH):
    print("Folder does NOT exist!")
    exit()

file_count = 0

for root, dirs, files in os.walk(DATA_PATH):
    for file in files:
        if file.endswith(".pdf"):
            file_count += 1
            file_path = os.path.join(root, file)
            print("Reading:", file_path)

            try:
                text = extract_text(file_path)

                if text.strip() == "":
                    print("⚠ No text extracted (possibly scanned PDF)")
                else:
                    print("Text length:", len(text))

            except Exception as e:
                print("Error:", e)

print("Total PDF files found:", file_count)
