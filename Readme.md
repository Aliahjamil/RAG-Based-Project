# RAG AI Teaching Assistant

A Retrieval-Augmented Generation (RAG) based AI Teaching Assistant that allows users to query educational video content using embeddings and an LLM.

---

# Features

- Convert educational videos into searchable knowledge
- Audio transcription pipeline
- Embedding generation using local models
- Semantic search using cosine similarity
- LLM-powered answer generation
- Fully local workflow using Ollama

---

# Project Workflow

## Step 1 - Collect Your Videos

Move all your video files into the `videos/` folder.

---

## Step 2 - Convert Videos to MP3

Run:

```bash
python video_to_mp3.py
```

This converts all video files into MP3 format.

---

## Step 3 - Convert MP3 to JSON

Run:

```bash
python mp3_to_json.py
```

This transcribes audio files and stores subtitle/text chunks in JSON format.

---

## Step 4 - Generate Embeddings

Run:

```bash
python preprocess_json.py
```

This:

- Reads JSON transcript files
- Creates embeddings
- Stores embeddings in a dataframe
- Saves the dataframe as a Joblib pickle file

---

## Step 5 - Query the AI Assistant

Run:

```bash
python process_incoming.py
```

This:

- Loads the embeddings
- Finds relevant chunks using cosine similarity
- Creates a prompt
- Sends the prompt to the LLM
- Returns the generated answer

---

# Tech Stack

- Python
- Ollama
- NumPy
- Pandas
- Scikit-learn
- Joblib

---

# Models Used

## Embedding Model

- `bge-m3`

## LLM

- `gpt-4.1-mini` / Ollama-supported local LLM

---

# Folder Structure

```text
project/
│
├── videos/
├── mp3/
├── json/
├── embeddings/
│
├── video_to_mp3.py
├── mp3_to_json.py
├── preprocess_json.py
├── process_incoming.py
│
├── README.md
└── requirements.txt
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo-name.git
```

Move into the project directory:

```bash
cd your-repo-name
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Requirements

Example requirements:

```txt
numpy
pandas
scikit-learn
joblib
requests
moviepy
```

---

# Future Improvements

- FAISS integration
- Streamlit UI
- Multi-document support
- Better chunking strategies
- Hybrid search
- Web deployment
- Integration with GPT-5 for advanced response generation

---

# Author

ALIAH JAMIL
