# Mini AI Support Assistant

AI-powered customer support application built with **Python, FastAPI, Scikit-learn, PyTorch, RAG, Qdrant, Hugging Face, PostgreSQL, Docker, AWS, and Terraform**.

## How It Works

1. **FastAPI** receives the customer question.
2. **Scikit-learn + PyTorch** classify the question and detect urgency.
3. **RAG + Qdrant** retrieve relevant knowledge.
4. **Hugging Face LLM** generates the response.
5. **PostgreSQL** stores request data.
6. **Docker** containerizes the application.
7. **AWS EC2 + Terraform** provide cloud deployment and infrastructure management.

## Architecture

```text
User
 ↓
FastAPI
 ↓
Scikit-learn + PyTorch
 ↓
RAG → Qdrant
 ↓
Hugging Face LLM
 ↓
Response
 ↓
PostgreSQL
```

## Tech Stack

**AI:** Scikit-learn, PyTorch, RAG, SentenceTransformers, Hugging Face
**Backend:** FastAPI, PostgreSQL
**Infrastructure:** Docker, Linux, AWS EC2, Terraform

## Run Locally

```bash
git clone https://github.com/bassam-aljazaeri/mini-ai-support.git
cd mini-ai-support
```

Create `.env`:

```env
HF_TOKEN=your_huggingface_token
```

Run:

```bash
docker compose up -d --build
```

API documentation:

```text
http://localhost:8000/docs
```

## AWS

Terraform provisions the AWS infrastructure:

```bash
cd terraform
terraform init
terraform apply
```

Destroy when finished:

```bash
terraform destroy
```

## Author

**Bassam Aljazaeri**
Data Science & AI Student | AI Engineer

[GitHub](https://github.com/bassam-aljazaeri) · [LinkedIn](https://www.linkedin.com/in/bassam-aljazaeri-ba3284315/)
