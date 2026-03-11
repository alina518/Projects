import sqlite3
import numpy as np
import faiss
import gradio as gr

from pypdf import PdfReader
from docx import Document
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# -----------------------------
# CONFIG
# -----------------------------

DB_NAME = "documents.db"
TOP_K = 3
EMBED_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "google/flan-t5-base"

# -----------------------------
# LOAD LLM
# -----------------------------

print("Loading FLAN-T5 model...")

tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
model_llm = AutoModelForSeq2SeqLM.from_pretrained(LLM_MODEL)

print("Model loaded successfully")

# global variables
embed_model = None
index = None
titles = None
documents = None


# -----------------------------
# EXTRACT TEXT
# -----------------------------

def read_pdf(path):

    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def read_docx(path):

    doc = Document(path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def read_txt(path):

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_text(file_path):

    if file_path.endswith(".pdf"):
        return read_pdf(file_path)

    elif file_path.endswith(".docx"):
        return read_docx(file_path)

    elif file_path.endswith(".txt"):
        return read_txt(file_path)

    return ""


# -----------------------------
# TEXT CHUNKING
# -----------------------------

def chunk_text(text, chunk_size=500, overlap=100):

    chunks = []
    start = 0

    while start < len(text):

        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += chunk_size - overlap

    return chunks


# -----------------------------
# DATABASE
# -----------------------------

def setup_database(chunks):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents(
        id INTEGER PRIMARY KEY,
        title TEXT,
        content TEXT
    )
    """)

    cursor.execute("DELETE FROM documents")

    records = []

    for i, chunk in enumerate(chunks, start=1):
        records.append((i, f"Chunk {i}", chunk))

    cursor.executemany(
        "INSERT INTO documents(id,title,content) VALUES (?,?,?)",
        records
    )

    conn.commit()
    conn.close()

    print(f"{len(records)} chunks stored in database")


# -----------------------------
# LOAD DOCUMENTS
# -----------------------------

def load_documents():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id,title,content FROM documents")

    rows = cursor.fetchall()

    conn.close()

    ids = [r[0] for r in rows]
    titles = [r[1] for r in rows]
    docs = [r[2] for r in rows]

    return ids, titles, docs


# -----------------------------
# VECTOR DATABASE
# -----------------------------

def build_vector_index(docs):

    global embed_model

    embed_model = SentenceTransformer(EMBED_MODEL)

    embeddings = embed_model.encode(docs)

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    idx = faiss.IndexFlatL2(dimension)

    idx.add(embeddings)

    print("FAISS index created")

    return idx


# -----------------------------
# RETRIEVE
# -----------------------------

def retrieve(query):

    query_vector = embed_model.encode([query])
    query_vector = np.array(query_vector).astype("float32")

    distances, indices = index.search(query_vector, TOP_K)

    results = []

    for idx in indices[0]:
        results.append((titles[idx], documents[idx]))

    return results


# -----------------------------
# GENERATE ANSWER
# -----------------------------

def generate_answer(query):

    retrieved_docs = retrieve(query)

    context = "\n\n".join(
        [f"{i+1}. {title}: {content}" for i,(title,content) in enumerate(retrieved_docs)]
    )

    prompt = f"""
Answer the question using ONLY the context.

Context:
{context}

Question: {query}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model_llm.generate(
        **inputs,
        max_new_tokens=150
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer


# -----------------------------
# PROCESS DOCUMENTS
# -----------------------------

def process_files(files):

    global index, titles, documents

    all_text = ""

    for file in files:

        text = extract_text(file.name)

        all_text += text + "\n"

    chunks = chunk_text(all_text)

    setup_database(chunks)

    ids, titles, documents = load_documents()

    index = build_vector_index(documents)

    return "Documents processed successfully!"


# -----------------------------
# GRADIO UI
# -----------------------------

import gradio as gr

with gr.Blocks(title="RAG Document QA System", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 📘 RAG Document Question Answering System
        Upload your **PDF / DOCX / TXT** files, process them, and ask questions from the extracted content.
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## 📂 Document Upload")
            file_input = gr.File(
                file_count="multiple",
                label="Upload Files",
                file_types=[".pdf", ".docx", ".txt"]
            )

            process_btn = gr.Button("⚙️ Process Documents", variant="primary")
            clear_files_btn = gr.Button("🗑️ Clear Files")

            status = gr.Textbox(
                label="Processing Status",
                lines=4,
                interactive=False,
                placeholder="Document processing status will appear here..."
            )

        with gr.Column(scale=2):
            gr.Markdown("## ❓ Ask Questions")

            question = gr.Textbox(
                label="Enter your Question",
                lines=2,
                placeholder="Type your question here and press Enter..."
            )

            with gr.Row():
                submit_btn = gr.Button("💬 Get Answer", variant="primary")
                clear_q_btn = gr.Button("🧹 Clear Question")

            answer = gr.Textbox(
                label="Answer",
                lines=10,
                interactive=False,
                placeholder="The answer will appear here in a structured format..."
            )

    with gr.Accordion("ℹ️ Instructions", open=False):
        gr.Markdown(
            """
            ### How to use
            1. Upload one or more **PDF, DOCX, or TXT** files.
            2. Click **Process Documents**.
            3. Enter your question in the question box.
            4. Press **Enter** or click **Get Answer**.

            ### Notes
            - Make sure documents are processed before asking questions.
            - You can upload multiple files at once.
            """
        )

    process_btn.click(
        fn=process_files,
        inputs=file_input,
        outputs=status
    )

    question.submit(
        fn=generate_answer,
        inputs=question,
        outputs=answer
    )

    submit_btn.click(
        fn=generate_answer,
        inputs=question,
        outputs=answer
    )

    clear_files_btn.click(
        fn=lambda: (None, ""),
        inputs=None,
        outputs=[file_input, status]
    )

    clear_q_btn.click(
        fn=lambda: ("", ""),
        inputs=None,
        outputs=[question, answer]
    )

demo.launch()
