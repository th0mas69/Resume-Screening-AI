import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import pdfplumber
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer, util
import datetime



filename = f"results_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# -------------------------
# Load model
# -------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------
# Skill list (can be extended)
# -------------------------
SKILLS = [
    "python", "java", "sql", "machine learning", "data analysis",
    "deep learning", "nlp", "excel", "power bi", "tableau",
    "communication", "project management", "aws", "docker", "problem-solving", "leadership", 
    "organization", "adapatability", "teamwork", "digital literacy", "written communication",
    "active listening", "reporting", "documenting", "web design", "data visualization", 
    "web design", "photo and video editing", "typography", "user interface", "user experience",
    "Statistical analysis", "Information processing", "compliance", "microsoft office", "microsoft excel", "sheets", "powerpoint",
    "accounting", "digital marketing", "SEO", "Game developer", "quality control", "testing", "manual QA"
]

# -------------------------
# Functions
# -------------------------

def extract_resume_text(file):
    try:
        return extract_text(file)
    except:
        try:
            with pdfplumber.open(file) as pdf:
                return " ".join([page.extract_text() or "" for page in pdf.pages])
        except:
            return ""

def extract_skills(text):
    text = text.lower()
    return {s for s in SKILLS if s in text}

def process(job_desc, files, filter_option):
    if not job_desc or not files:
        return "⚠️ Provide input", None, None

    job_emb = model.encode(job_desc)
    job_skills = extract_skills(job_desc)

    results = []

    for file in files:
        try:
            text = extract_text(file.name)
            text = extract_resume_text(file.name)
        except:
            text = ""

        if not text.strip():
            continue

        res_emb = model.encode(text)
        sim = util.cos_sim(job_emb, res_emb).item()

        res_skills = extract_skills(text)
        overlap = len(res_skills & job_skills) / len(job_skills) if job_skills else 0

        results.append({
            "Resume": file.name.split("\\")[-1],
            "Similarity": round(sim, 3),
            "Skill Match": round(overlap, 2),
            "Skills Found": ", ".join(res_skills),
            "Decision": "Selected" if sim > 0.6 else "Rejected"
        })

    if not results:
        return "❌ No valid resumes", None, None
    


    df = pd.DataFrame(results)
    df = df.sort_values(by="Similarity", ascending=False)

    #Handle Empty case & filtering

    if not df.empty and "Similarity" in df.columns:
        if filter_option == "Top Matches Only":
            df = df[df["Similarity"] > 0.6]
        d



    #Adding Filters

    threshold = 0.6  # adjustable

    df["Selected"] = df["Similarity"] > threshold

    filtered_df = df[df["Selected"] == True]

    # Top candidate
    top_candidate = df.iloc[0]

    #Skill Match Score

    df["Final Score"] = (df["Similarity"] * 0.7 + df["Skill Match"] * 0.3)

    df = df.sort_values(by="Final Score", ascending=False)


    # Graph
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(df["Resume"][:5], df["Similarity"][:5])
    ax.invert_yaxis()
    plt.tight_layout()

    summary = f"""
    🏆 **Top Candidate:** {top_candidate['Resume']}  
    📊 Similarity: {top_candidate['Similarity']}  
    🧠 Skill Match: {top_candidate['Skill Match']}
    """


    csv_path = "results.csv"
    df.to_csv(csv_path, index=False)
    return summary, df.head(5), fig, csv_path


with gr.Blocks() as app:
    gr.Markdown("<h2> AI Resume Screening Dashboard <h2>")

    with gr.Row():
        job_input = gr.Textbox(label="📄 Job Description", lines=6)

    with gr.Row():
        file_input = gr.File(file_count="multiple", type="file", label="📂 Upload Resumes")
    with gr.Row():
        file_output = gr.File(label="📥 Download Report (CSV)")

    run_btn = gr.Button("🖥️ Analyze Candidates")

    summary_output = gr.Markdown()
    table_output = gr.Dataframe()
    graph_output = gr.Plot()

    filter_option = gr.Dropdown(
    ["All Candidates", "Top Matches Only"],
    value="All Candidates",
    label="Filter Candidates")


    run_btn.click(
        process,
        inputs=[job_input, file_input, filter_option],
        outputs=[summary_output, table_output, graph_output, file_output]
    )


    reset_btn = gr.Button("🔄 Clear")

    reset_btn.click(
        lambda: ("", [], "", None, None),
        outputs=[job_input, file_input, summary_output, table_output, graph_output, file_output]
    )


app.launch(inbrowser=True)