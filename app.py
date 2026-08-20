import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer, util
import tempfile
import os
import datetime

st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# --------------------------------------------------
# SKILLS
# --------------------------------------------------

SKILLS = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "data analysis",
    "excel",
    "power bi",
    "tableau",
    "aws",
    "docker",
    "kubernetes",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "communication",
    "project management"
]


def extract_skills(text):
    text = text.lower()

    return {
        skill
        for skill in SKILLS
        if skill.lower() in text
    }


# --------------------------------------------------
# PDF EXTRACTION
# --------------------------------------------------

def extract_resume_text(file):

    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp:

            temp.write(file.getbuffer())
            temp_path = temp.name

        text = extract_text(temp_path)

        os.remove(temp_path)

        return text or ""

    except Exception as e:
        st.warning(f"Could not read {file.name}: {e}")
        return ""


# --------------------------------------------------
# SAMPLE RESUMES
# --------------------------------------------------

def load_existing_resumes():

    folder = Path("sample_resumes")

    if not folder.exists():
        return []

    return list(folder.glob("*.pdf"))


# --------------------------------------------------
# MAIN SCREEN
# --------------------------------------------------

st.title("🧠 AI Resume Screening & Job Matching")

st.markdown("""
### 📌 About the System

This application automatically evaluates resumes against a job
description using Natural Language Processing.

The system combines:

- 🧠 Semantic similarity
- 🛠️ Skill extraction
- 📊 Skill overlap
- 🏆 Candidate ranking
- 📈 Similarity visualisation
- 📥 CSV report generation
""")

st.divider()

# --------------------------------------------------
# JOB DESCRIPTION
# --------------------------------------------------

st.subheader("1️⃣ Job Description")

job_description = st.text_area(
    "Enter the job description",
    height=200,
    placeholder="Paste the job description here..."
)

# --------------------------------------------------
# RESUMES
# --------------------------------------------------

st.subheader("2️⃣ Resumes")

uploaded_files = st.file_uploader(
    "Upload PDF resumes",
    type=["pdf"],
    accept_multiple_files=True
)

existing_button = st.button(
    "📂 Use Existing Resumes"
)

existing_files = []

if existing_button:

    existing_files = load_existing_resumes()

    if existing_files:
        st.success(
            f"{len(existing_files)} existing resumes loaded."
        )
    else:
        st.warning(
            "No PDFs found in sample_resumes folder."
        )

# --------------------------------------------------
# FILTER
# --------------------------------------------------

threshold = st.slider(
    "Minimum similarity score",
    min_value=0.0,
    max_value=1.0,
    value=0.60,
    step=0.05
)

top_n = st.selectbox(
    "Number of candidates to display",
    [5, 10, 20],
    index=0
)

# --------------------------------------------------
# ANALYZE
# --------------------------------------------------

analyze = st.button(
    "🚀 Analyze Candidates",
    type="primary"
)

if analyze:

    if not job_description.strip():

        st.error("Please enter a job description.")

        st.stop()

    if not uploaded_files and not existing_files:

        st.error("Please upload resumes or use existing resumes.")

        st.stop()

    # Choose files
    if uploaded_files:
        resumes = uploaded_files
    else:
        resumes = existing_files

    with st.spinner("Analysing resumes..."):

        # Job embedding
        job_embedding = model.encode(
            job_description,
            convert_to_tensor=True
        )

        job_skills = extract_skills(job_description)

        results = []

        progress = st.progress(0)

        total = len(resumes)

        for i, resume in enumerate(resumes):

            # Extract text
            if hasattr(resume, "getbuffer"):
                text = extract_resume_text(resume)
                filename = resume.name
            else:
                filename = resume.name
                text = extract_text(str(resume))

            if not text.strip():
                continue

            # Resume embedding
            resume_embedding = model.encode(
                text,
                convert_to_tensor=True
            )

            similarity = util.cos_sim(
                job_embedding,
                resume_embedding
            ).item()

            # Skills
            resume_skills = extract_skills(text)

            matched_skills = (
                job_skills &
                resume_skills
            )

            if job_skills:

                skill_match = (
                    len(matched_skills) /
                    len(job_skills)
                )

            else:

                skill_match = 0

            # Combined score
            final_score = (
                similarity * 0.7
                +
                skill_match * 0.3
            )

            results.append({

                "Resume": filename,

                "Similarity":
                    round(similarity, 3),

                "Skill Match":
                    round(skill_match, 3),

                "Final Score":
                    round(final_score, 3),

                "Skills Found":
                    ", ".join(sorted(resume_skills)),

                "Matched Skills":
                    ", ".join(sorted(matched_skills))
            })

            progress.progress(
                (i + 1) / total
            )

        progress.empty()

    # --------------------------------------------------
    # DATAFRAME
    # --------------------------------------------------

    if not results:

        st.error(
            "No readable resumes were found."
        )

        st.stop()

    df = pd.DataFrame(results)

    df = df.sort_values(
        "Final Score",
        ascending=False
    ).reset_index(drop=True)

    df.insert(
        0,
        "Rank",
        range(1, len(df) + 1)
    )

    # --------------------------------------------------
    # FILTER
    # --------------------------------------------------

    filtered_df = df[
        df["Similarity"] >= threshold
    ]

    # --------------------------------------------------
    # TOP CANDIDATE
    # --------------------------------------------------

    st.divider()

    st.subheader("🏆 Top Candidate")

    top = df.iloc[0]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Candidate",
        top["Resume"]
    )

    col2.metric(
        "Final Score",
        top["Final Score"]
    )

    col3.metric(
        "Skill Match",
        top["Skill Match"]
    )

    # --------------------------------------------------
    # RANKING TABLE
    # --------------------------------------------------

    st.subheader("📊 Candidate Ranking")

    st.dataframe(
        filtered_df.head(top_n),
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # GRAPH
    # --------------------------------------------------

    st.subheader("📈 Similarity Graph")

    graph_df = df.head(top_n).copy()

    graph_df["Short Name"] = (
        graph_df["Resume"]
        .apply(lambda x: Path(x).name[:25])
    )

    fig, ax = plt.subplots(
        figsize=(12, 6)
    )

    ax.barh(
        graph_df["Short Name"],
        graph_df["Similarity"]
    )

    ax.invert_yaxis()

    ax.set_xlabel(
        "Similarity Score"
    )

    ax.set_ylabel(
        "Candidate"
    )

    ax.set_title(
        "Resume–Job Similarity"
    )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------
    # REPORT
    # --------------------------------------------------

    timestamp = datetime.datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    csv_filename = (
        f"resume_screening_{timestamp}.csv"
    )

    csv_data = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "📥 Download CSV Report",
        data=csv_data,
        file_name=csv_filename,
        mime="text/csv"
    )

    # --------------------------------------------------
    # DETAILS
    # --------------------------------------------------

    st.subheader("🧠 Candidate Insights")

    for _, row in df.head(top_n).iterrows():

        with st.expander(
            f"#{row['Rank']} — {row['Resume']}"
        ):

            st.write(
                f"**Similarity:** {row['Similarity']}"
            )

            st.write(
                f"**Skill Match:** {row['Skill Match']}"
            )

            st.write(
                f"**Final Score:** {row['Final Score']}"
            )

            st.write(
                f"**Matched Skills:** "
                f"{row['Matched Skills']}"
            )
