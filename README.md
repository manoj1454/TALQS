# ⚖️ TALQS - Transformer-based AI for Legal Question-answering and Summarization

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Gradio](https://img.shields.io/badge/Gradio-Web_App-orange)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep_Learning-red)
![License](https://img.shields.io/badge/License-MIT-green)

**An AI-powered legal document assistant that summarizes legal judgments and answers questions directly from uploaded PDF documents.**

---

## 📖 Overview

TALQS (Transformer-based AI for Legal Question-answering and Summarization) is a web-based application designed to help users quickly understand lengthy legal judgments. The system extracts text from uploaded PDF documents, generates concise summaries using a pretrained transformer model, and enables users to ask natural language questions about the document.

Built with Gradio and Hugging Face Transformers, TALQS demonstrates how modern Natural Language Processing (NLP) models can improve legal document accessibility, analysis, and information retrieval.

---

## 🌐 Live Demo

🚀 **Try TALQS Online**

**Hugging Face Space:**
https://huggingface.co/spaces/manoj1454/TALQS

No installation required. Upload a legal judgment PDF, generate summaries, and ask questions directly from your browser.

---

## ✨ Features

* 📄 Upload legal judgment PDFs
* 📝 Generate concise AI-powered summaries
* ❓ Ask natural language questions about the uploaded document
* 🔍 Extract answers directly from document content
* 📚 PDF text extraction using pdfplumber
* ✂️ Automatic chunking for handling long documents
* ⚡ Interactive Gradio web interface
* 🤖 Powered by state-of-the-art Transformer models
* 🌐 Available online through Hugging Face Spaces

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Frameworks & Libraries

* Gradio
* Hugging Face Transformers
* PyTorch
* pdfplumber

### NLP Models

#### Document Summarization

* `facebook/bart-large-cnn`
* Transformer-based abstractive summarization model

#### Question Answering

* `deepset/roberta-base-squad2`
* RoBERTa-based extractive question-answering model

---

## ⚙️ How It Works

### Step 1: Upload PDF

Users upload a legal judgment PDF through the Gradio interface.

### Step 2: Text Extraction

Text is extracted page-by-page using **pdfplumber**.

### Step 3: Document Chunking

Large documents are divided into smaller chunks to fit within transformer model token limits.

### Step 4: Summarization

Each chunk is summarized using the pretrained **BART** model. The generated summaries are then combined to produce a concise final summary.

### Step 5: Question Answering

When a question is submitted:

* The document is split into chunks.
* Each chunk is evaluated using the pretrained **RoBERTa QA** model.
* The answer with the highest confidence score is returned.

### Processing Pipeline

```text
PDF Upload
     ↓
Text Extraction (pdfplumber)
     ↓
Document Chunking
     ↓
 ┌──────────────────┬──────────────────┐
 ↓                  ↓
Summarization       Question Answering
(BART)              (RoBERTa)
 ↓                  ↓
Summary             Answer
```

---

## 🚀 Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/TALQS.git
cd TALQS
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

After launching, Gradio will provide a local URL such as:

```text
http://127.0.0.1:7860
```

Open the URL in your browser to start using TALQS.

---

## 📂 Project Structure

```text
TALQS/
│
├── app.py
├── requirements.txt
├── README.md
│
└── assets/
```

---

## 🎯 Use Cases

* Legal research assistance
* Rapid judgment review
* Academic legal studies
* Case law exploration
* Legal document summarization
* Information extraction from court judgments
* Educational demonstrations of NLP in the legal domain

---

## ⚠️ Limitations

* The pretrained models are not specifically fine-tuned on Indian legal case law datasets.
* Performance may vary on highly technical or domain-specific legal documents.
* Very long judgments may experience some loss of context due to chunking.
* The QA model performs extractive question answering and does not provide legal reasoning or interpretation.
* TALQS is currently a demonstration and portfolio-stage project.

---

## 🔮 Future Improvements

* Fine-tune transformer models on Indian legal case law datasets
* Improve chunking and summary coherence for lengthy judgments
* Add source citations and evidence highlighting for answers
* Support multilingual legal documents
* Integrate Retrieval-Augmented Generation (RAG)
* Add semantic search capabilities
* Improve response speed with optimized inference pipelines
* Deploy specialized legal-domain language models

---

## 🎓 Academic Context

TALQS was developed as a project exploring the application of Transformer-based Natural Language Processing techniques in the legal domain. The project combines document summarization and question answering to improve accessibility and understanding of lengthy legal judgments.

---

## 👨‍💻 Author

**Manoj**
Computer Science Student
Neil Gogte Institute of Technology

Project Focus:

* Natural Language Processing (NLP)
* Transformer Models
* Legal AI Applications
* Information Retrieval
* Question Answering Systems

---

## 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software in accordance with the terms of the license.

---

### ⭐ If you found this project useful, consider giving it a star on GitHub and sharing feedback to help improve future versions of TALQS.
