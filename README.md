# 🩺 MiStory AI

> **An AI-powered longitudinal symptom tracker and physician copilot that transforms patient-reported symptoms into structured clinical histories and enables grounded AI-assisted clinical review.**

---

## Overview

MiStory helps patients capture symptoms over time using text, voice, and images, creating a longitudinal health timeline that can be shared with physicians. Rather than relying on memory during appointments, patients build a structured history that grows over time.

On the physician side, MiStory provides an AI copilot that retrieves relevant patient history and answers questions using only the patient's recorded data.

---

## Key Features

### 👤 Patient Dashboard

- Log symptoms using text (voice & image support ready)
- Record symptoms for past or current dates
- AI-powered symptom extraction
- Longitudinal symptom timeline
- Structured health history

### 🤖 AI Clinical Extraction

Each entry is automatically analyzed to extract:

- Symptoms
- Body system
- Severity
- Structured clinical metadata

Example:

**Input**

> "My right ear has been bleeding for three days."

**Extracted**

```json
{
  "symptoms": [
    {
      "name": "Ear bleeding",
      "confidence": 0.91
    }
  ],
  "body_system": "ENT",
  "severity": "high"
}
```

### 👨‍⚕️ Physician Dashboard

- Patient summary
- Symptom timeline
- Symptom clustering
- Severity overview
- AI Physician Copilot

### 🧠 AI Copilot

Ask natural language questions such as:

- Did headaches and nausea occur together?
- When did symptoms first begin?
- Has fatigue worsened over time?

Responses are grounded **only** in the patient's recorded history.

---

# System Architecture

```text
Patient Entry
      │
      ▼
AI Symptom Extraction
      │
      ▼
Structured Clinical Record
      │
      ├── SQLite Database
      └── FAISS Vector Store
               │
               ▼
      Physician AI Copilot (RAG)
```

---

# Tech Stack

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

### Backend

- FastAPI
- SQLModel
- SQLite

### AI

- Hugging Face Transformers
- Sentence Transformers
- FAISS
- Zero-shot Clinical Classification

---

# Running the Project

## Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend:

```
http://localhost:8000
```

API Docs:

```
http://localhost:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```
http://localhost:3000
```

---

# API Endpoints

### Create Symptom Entry

```
POST /api/entry
```

### Patient Context

```
GET /api/patient/context/{patient_id}
```

### Physician Copilot

```
POST /api/copilot/ask
```

---

# Current MVP

- ✅ AI-powered symptom extraction
- ✅ Longitudinal patient timeline
- ✅ Structured patient records
- ✅ SQLite persistence
- ✅ Semantic search with FAISS
- ✅ Physician dashboard
- ✅ Retrieval-Augmented AI Copilot

---

# Future Improvements

- Voice transcription
- Medical image understanding
- Timeline visualizations
- PDF physician summaries
- BioBERT / ClinicalBERT integration
- FHIR & EHR integration
- Wearable device support

---

# Disclaimer

MiStory is a research and demonstration project designed to organize and summarize patient health history. It does **not** provide medical diagnoses or replace professional medical advice.

---

## Author

**Priyanka Ganesan**

Machine Learning Engineer • Healthcare AI • Clinical Decision Support Systems
