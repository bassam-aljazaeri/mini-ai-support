import os
import psycopg2


def save_request(
    question,
    category,
    urgency,
    answer
):

    connection = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=5432,
        database="support",
        user="postgres",
        password="postgres"
    )

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id SERIAL PRIMARY KEY,
            question TEXT,
            category TEXT,
            urgency TEXT,
            answer TEXT
        )
    """)

    cursor.execute(
        """
        INSERT INTO requests
        (question, category, urgency, answer)
        VALUES (%s, %s, %s, %s)
        """,
        (
            question,
            category,
            urgency,
            answer
        )
    )

    connection.commit()

    cursor.close()
    connection.close()