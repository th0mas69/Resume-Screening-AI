#  AI Resume Screening & Job Matching System

## 📌 Overview

An AI-powered resume screening and job matching system developed as an MSc Computer Science project.

The system uses Natural Language Processing (NLP), semantic embeddings, skill extraction and candidate ranking to automatically compare resumes against a given job description.

Recruiters often need to review a large number of resumes against a single job description. Manual screening can be time-consuming and may result in inconsistent candidate evaluation.

This project aims to automate part of the initial screening process by analysing resumes and comparing them with job requirements.

The system extracts text from PDF resumes, calculates semantic similarity between resumes and job descriptions, identifies relevant skills, calculates skill overlap and produces a ranked list of candidates.

The application also provides visual candidate insights and downloadable screening reports.

## 🎯 Project Objectives

The main objectives of the system are:

- Automate initial resume screening
- Compare resumes with job descriptions
- Identify relevant candidate skills
- Calculate semantic similarity
- Calculate skill overlap
- Rank candidates according to their suitability
- Provide interpretable candidate information
- Reduce manual screening effort
- Generate downloadable screening reports
- Provide an easy-to-use recruiter dashboard

## 🚀 Features

### 📄 PDF Resume Processing

The system accepts PDF resumes and extracts their textual content using PDF parsing libraries.

### 🧠 Semantic Resume Matching

Sentence Transformer embeddings are used to represent resumes and job descriptions in vector form.

The system calculates semantic similarity between the job description and each resume.

### 🛠️ Skill Extraction

The system identifies relevant technical and professional skills from resumes and job descriptions.

Example skills include:

- Python
- Java
- SQL
- Machine Learning
- Deep Learning
- NLP
- Data Analysis
- AWS
- Docker
- TensorFlow
- PyTorch
- Power BI
- Tableau

### 📊 Skill Overlap Analysis

The system compares skills found in the job description with skills found in each resume.

The skill match score is calculated based on the proportion of required skills found in the candidate's resume.

### 🏆 Candidate Ranking

Candidates are ranked using a combined score based on:

- Semantic similarity
- Skill overlap

### 📈 Similarity Visualisation

The system generates a similarity graph showing the highest-ranked candidates.

### 🔎 Candidate Filtering

Recruiters can set a minimum similarity threshold to filter candidates.

### 📂 Existing Resume Dataset

The application supports a sample resume directory so that recruiters can test the system without uploading files individually.

### 📥 Downloadable Reports

Screening results can be exported as CSV reports with timestamped filenames.

## 🖥️ User Interface

The application provides a recruiter-oriented dashboard containing:

Job description input
PDF resume upload
Existing resumes option
Similarity threshold
Candidate ranking table
Top candidate summary
Skill overlap information
Similarity graph
Candidate insights
Downloadable CSV report

## System Architecture

                    ┌──────────────────────┐
                    │   Recruiter/User     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Dashboard  │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │ Job Description │        │ PDF Resumes     │
        └────────┬────────┘        └────────┬────────┘
                 │                          │
                 │                          ▼
                 │                 ┌─────────────────┐
                 │                 │ PDF Text        │
                 │                 │ Extraction      │
                 │                 └────────┬────────┘
                 │                          │
                 └────────────┬─────────────┘
                              ▼
                    ┌──────────────────────┐
                    │ Text Preprocessing   │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │ Sentence        │        │ Skill Extraction│
        │ Transformer     │        │                 │
        │ Embeddings      │        └────────┬────────┘
        └────────┬────────┘                 │
                 │                          │
                 ▼                          ▼
        ┌─────────────────┐        ┌─────────────────┐
        │ Semantic        │        │ Skill Overlap   │
        │ Similarity      │        │ Score           │
        └────────┬────────┘        └────────┬────────┘
                 │                          │
                 └─────────────┬────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Combined Ranking     │
                    │ Score                │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Candidate Ranking    │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼─────────────────┐
              ▼                ▼                 ▼
       ┌────────────┐   ┌────────────┐   ┌────────────┐
       │ Top        │   │ Similarity │   │ Download   │
       │ Candidates │   │ Graph      │   │ Report     │
       └────────────┘   └────────────┘   └────────────┘

       
## 🛠️ Technologies Used

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| Python                | Core programming language       |
| Streamlit             | Web application interface       |
| Pandas                | Data processing                 |
| NumPy                 | Numerical operations            |
| Matplotlib            | Data visualisation              |
| Sentence Transformers | Semantic text embeddings        |
| Scikit-learn          | Machine learning and evaluation |
| PDFMiner              | PDF text extraction             |
| pdfplumber            | Alternative PDF parsing         |
| ReportLab             | PDF report generation           |
| PyTorch               | Deep learning backend           |

## 🧠 NLP and Machine Learning Approach

1. Resume Text Extraction

PDF resumes are converted into machine-readable text.
PDF Resume
     ↓
Text Extraction
     ↓
Raw Resume Text

2. Text Processing

Extracted text is cleaned and normalised before being processed by the matching system.

3. Semantic Embeddings

The project uses:
all-MiniLM-L6-v2

from Sentence Transformers.

The model converts text into numerical vector representations.

4. Semantic Similarity

The system compares the job description embedding with each resume embedding.

Higher similarity indicates stronger semantic relevance.

5. Skill Matching

Skills extracted from the job description are compared with skills identified in each resume.

6. Candidate Ranking

The final candidate score combines semantic similarity and skill match.

Final Score =
(Semantic Similarity × 0.70)
+
(Skill Match × 0.30)

Candidates are then sorted in descending order.

## ▶️ How to Run

### https://resume-screening-ai-gca9tc993fxlpxntslqbrr.streamlit.app/ - Currently live

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/resume-screening-ai.git
```
```bash
cd resume-screening-ai
```

2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Run:

```bash
streamlit run app.py
```

The application will normally be available at:

http://localhost:8501

## 🧪 Testing

The system can be evaluated using:

Resume parsing accuracy
Semantic similarity scores
Skill matching accuracy
Candidate ranking performance
Classification metrics
Confusion matrix
ROC curve
Cross-validation

Testing should verify that the system correctly processes valid PDF files, handles invalid documents, generates candidate rankings and produces downloadable reports.

## 🎓 Academic Context

This system was developed as an MSc Computer Science project investigating the use of Artificial Intelligence and Natural Language Processing for automated resume screening and job matching.

The project demonstrates the application of:

Natural Language Processing
Machine Learning
Semantic embeddings
Information extraction
Similarity measurement
Candidate ranking
Data visualisation

## 📊 Project Status

🟢 Core resume screening       Completed
🟢 PDF processing              Completed
🟢 Semantic matching           Completed
🟢 Skill overlap               Completed
🟢 Candidate ranking            Completed
🟢 Similarity visualisation     Completed
🟢 CSV report generation        Completed
🟢 Recruiter dashboard          Completed
🟡 Advanced parsing             Future improvement
🟡 Advanced explainability      Future improvement
🟡 Production ATS integration   Future improvement

## 👨‍💻 Author

Thomas Luke
MSc. CS Student @ IU University

## ⚖️ Disclaimer

This application is an academic prototype intended to support resume screening and candidate comparison. It should not be used as the sole basis for employment decisions. Human review and appropriate fairness, privacy and legal safeguards should be applied when using automated recruitment systems.
