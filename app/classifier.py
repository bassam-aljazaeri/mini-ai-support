from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


training_texts = [
    "I forgot my password",
    "How do I reset my password",
    "I cannot login",
    "I need to change my password",

    "I want a refund",
    "Can I get my money back",
    "How do refunds work",
    "I want to return my purchase",

    "Where is my order",
    "How long does shipping take",
    "Can I track my package",
    "When will my package arrive",

    "I want to change my email",
    "I cannot access my account",
    "How do I change my account information",

    "The application is not working",
    "The app keeps crashing",
    "I have a technical problem",
    "Something is broken"
]

labels = [
    "password",
    "password",
    "password",
    "password",

    "refund",
    "refund",
    "refund",
    "refund",

    "shipping",
    "shipping",
    "shipping",
    "shipping",

    "account",
    "account",
    "account",

    "technical",
    "technical",
    "technical",
    "technical"
]


vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(training_texts)

model = LogisticRegression(max_iter=1000)

model.fit(X, labels)


def classify(text):
    X_test = vectorizer.transform([text])
    prediction = model.predict(X_test)[0]

    return prediction