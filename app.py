import gradio as gr
import pdfplumber
from transformers import pipeline
import torch

# -----------------------------
# Load Hugging Face Pipelines
# -----------------------------

device = 0 if torch.cuda.is_available() else -1

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    tokenizer="facebook/bart-large-cnn",
    device=device,
)

qa_pipeline = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2",
    tokenizer="deepset/roberta-base-squad2",
    device=device
)

# -----------------------------
# Global Document Storage
# -----------------------------

document_text = ""

# -----------------------------
# PDF Text Extraction
# -----------------------------


def extract_text_from_pdf(pdf_file):
    """
    Extract text from uploaded PDF using pdfplumber.
    """
    text = ""

    with pdfplumber.open(pdf_file.name) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.strip()


# -----------------------------
# Text Chunking
# -----------------------------


def chunk_text(text, max_words=200):
    """
    Split long text into manageable chunks.
    """
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks


# -----------------------------
# Summarization
# -----------------------------


def summarize_document(pdf_file):
    """
    Extract and summarize PDF content.
    """
    global document_text

    if pdf_file is None:
        return "Please upload a PDF."

    try:
        document_text = extract_text_from_pdf(pdf_file)

        if not document_text:
            return "No text could be extracted from the PDF."

        chunks = chunk_text(document_text)

        chunk_summaries = []

        for chunk in chunks:
            summary = summarizer(
                chunk,
                max_length=150,
                min_length=40,
                do_sample=False,
                no_repeat_ngram_size=3,
                truncation=True
            )

            chunk_summaries.append(summary[0]["summary_text"])

        # If multiple chunk summaries exist, summarize again
        combined_summary = " ".join(chunk_summaries)

        # Manually limit word count to avoid exceeding BART's position embedding limit
        combined_summary_words = combined_summary.split()
        if len(combined_summary_words) > 600:
            combined_summary = " ".join(combined_summary_words[:600])

        if len(chunk_summaries) > 1:
            final_summary = summarizer(
                combined_summary,
                max_length=200,
                min_length=60,
                do_sample=False,
                truncation=True
            )[0]["summary_text"]

            return final_summary

        return combined_summary
    except Exception as e:
            import traceback
            traceback.print_exc()
            return f"Error: {str(e)}"


# -----------------------------
# Question Answering
# -----------------------------


def answer_question(question):
    """
    Answer a user question from the extracted document.
    """
    global document_text

    if not document_text:
        return "Please upload and process a PDF first."

    if not question.strip():
        return "Please enter a question."

    try:
        chunks = chunk_text(document_text, max_words=500)

        best_answer = ""
        best_score = -1

        for chunk in chunks:
            result = qa_pipeline(
                question=question,
                context=chunk
            )

            if result["score"] > best_score:
                best_score = result["score"]
                best_answer = result["answer"]

        if best_answer.strip() == "":
            return "Answer not found."

        return best_answer

    except Exception as e:
        return f"Error: {str(e)}"


# -----------------------------
# Gradio UI
# -----------------------------

with gr.Blocks(title="Legal Judgment Summarizer & QA") as app:

    gr.Markdown("# Legal Judgment Summarizer & Question Answering")
    gr.Markdown(
        "Upload a legal judgment PDF, generate a summary, "
        "and ask questions about the document."
    )

    pdf_input = gr.File(
    label="Upload Legal Judgment PDF"
    )

    summarize_btn = gr.Button("Summarize")
    summary_output = gr.Textbox(
        label="Summary",
        lines=10
    )

    summarize_btn.click(
        fn=summarize_document,
        inputs=pdf_input,
        outputs=summary_output
    )

    gr.Markdown("## Ask Questions About the Document")

    question_input = gr.Textbox(
        label="Question",
        placeholder="Enter your question here..."
    )

    answer_btn = gr.Button("Answer")

    answer_output = gr.Textbox(
        label="Answer",
        lines=3
    )

    answer_btn.click(
        fn=answer_question,
        inputs=question_input,
        outputs=answer_output
    )

# -----------------------------
# Launch App
# -----------------------------

if __name__ == "__main__":
    app.launch()