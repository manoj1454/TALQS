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

Built with Gradio and Hugging Face Transformers, TALQS demonstrates how modern NLP models can improve legal document accessibility and information retrieval.

---

## ✨ Features

* 📄 Upload legal judgment PDFs
* 📝 Generate concise document summaries
* ❓ Ask natural language questions about the judgment
* 🔍 Extract answers directly from document content
* 📚 Automatic text extraction using PDF parsing
* ✂️ Intelligent chunking for handling long documents
* 🌐 Simple and interactive Gradio web interface
* 🤖 Powered by pretrained Transformer models

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

#### Summarization

* `facebook/bart-large-cnn`
* Transformer-based abstractive summarization model

#### Question Answering

* `deepset/roberta-base-squad2`
* RoBERTa-based extractive question-answering model

---

## ⚙️ How It Works

### 1. PDF Upload

The user uploads a legal judgment PDF through the Gradio interface.

### 2. Text Extraction

The application extracts textual content from each page using **pdfplumber**.

### 3. Text Chunking

Long documents are split into manageable chunks to stay within transformer token limits.

### 4. Summarization

Each chunk is summarized using the pretrained **BART** model, and the summaries are combined into a final concise summary.

### 5. Question Answering

When a question is asked:

* The document is divided into chunks.
* Each chunk is searched using the pretrained **RoBERTa QA** model.
* The answer with the highest confidence score is returned to the user.

#### Processing Pipeline

```text
PDF Upload
     ↓
Text Extraction (pdfplumber)
     ↓
Document Chunking
     ↓
 ┌───────────────┬───────────────┐
 ↓               ↓
Summarization    Question Answering
(BART)           (RoBERTa)
 ↓               ↓
Summary          Answer
```

---

## 🚀 Running Locally

### Clone the Repository

```bash
git clone https://github.com/your-username/TALQS.git
cd TALQS
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

After launching, open the local Gradio URL displayed in the terminal.

---

## 🌐 Live Demo

**Live Demo:** [Add Hugging Face Space Link Here]

---

## ⚠️ Limitations

* The pretrained models are not specifically fine-tuned on Indian legal case law datasets.
* Performance may vary for highly technical or domain-specific legal terminology.
* Very long documents may lose some contextual information during chunking.
* Extractive QA returns answers found in the document and does not perform legal reasoning.
* This is currently a demonstration and portfolio-stage project.

---

## 🔮 Future Improvements

* Fine-tune models on Indian legal judgment datasets
* Improve chunking and summary coherence for lengthy documents
* Add source citations and highlighted evidence for answers
* Support multilingual legal documents
* Integrate Retrieval-Augmented Generation (RAG)
* Add document search and semantic retrieval capabilities
* Deploy optimized inference for faster response times

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
* Quick judgment review
* Academic legal studies
* Case law exploration
* Legal document summarization
* Information extraction from court judgments

---

## 👨‍💻 Author

**Manoj**
Computer Science Student
Transformer-based Legal AI Project

---

## 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project in accordance with the license terms.
