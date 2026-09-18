from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

import os


# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Connect to Qdrant
client = QdrantClient(
    host=os.getenv("QDRANT_HOST", "localhost"),
    port=6333
)


collection_name = "support_knowledge"


# Knowledge base
documents = [
    "Users can reset their password by clicking Forgot Password on the login page. A reset link will be sent to their registered email address. The reset link expires after 30 minutes.",

    "Customers can request a refund within 14 days of purchase. Refund requests should include the order number. Approved refunds are normally processed within 5 business days.",

    "Standard shipping normally takes 3 to 5 business days. Express shipping normally takes 1 to 2 business days. Customers can track their order using the tracking number.",

    "Users can change their email address from Account Settings. Users should contact support if they no longer have access to their registered email.",

    "If an application is not working correctly, users should first restart the application. If the problem continues, they should contact technical support."
]


# Create embeddings
embeddings = model.encode(documents)

vector_size = len(embeddings[0])


# Create Qdrant collection if it doesn't exist
if not client.collection_exists(collection_name):

    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE
        )
    )

    points = []

    for i, embedding in enumerate(embeddings):

        points.append(
            PointStruct(
                id=i,
                vector=embedding.tolist(),
                payload={
                    "text": documents[i]
                }
            )
        )

    client.upsert(
        collection_name=collection_name,
        points=points
    )


def search_knowledge(query, limit=2):

    query_embedding = model.encode(query).tolist()

    results = client.query_points(
        collection_name=collection_name,
        query=query_embedding,
        limit=limit
    ).points

    return [
        result.payload["text"]
        for result in results
    ]