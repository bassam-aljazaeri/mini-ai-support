from fastapi import FastAPI
from pydantic import BaseModel

from huggingface_hub import InferenceClient
from dotenv import load_dotenv

from classifier import classify
from urgency import predict_urgency
from rag import search_knowledge
from prompt import create_prompt

import os

from database import save_request



load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)


app = FastAPI(
    title="Mini AI Support Assistant"
)


class Question(BaseModel):

    question: str


@app.get("/")
def home():

    return {
        "message": "Mini AI Support Assistant is running"
    }


@app.post("/query")
def query(data: Question):

    question = data.question

    # 1. Scikit-learn
    category = classify(question)

    # 2. PyTorch
    #
    # Very simple demonstration features:
    # [contains "password", contains "refund", contains "urgent"]
    features = [
        int("password" in question.lower()),
        int("refund" in question.lower()),
        int(
            any(
                word in question.lower()
                for word in ["urgent", "emergency", "immediately"]
            )
        )
    ]

    urgency = predict_urgency(features)

    # 3. RAG / Qdrant
    documents = search_knowledge(question)

    # 4. Prompt engineering
    prompt = create_prompt(
        question,
        category,
        urgency,
        documents
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
            messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=300
    )

    answer = response.choices[0].message.content
    
    save_request(
        question,
        category,
        urgency,
        answer
    )
    
    return {
        "question": question,
        "category": category,
        "urgency": urgency,
        "answer": answer,
        "sources": documents
    }