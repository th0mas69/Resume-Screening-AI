import re
import string
import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")


def clean_text(text: str) -> str:
    """
    Basic cleaning:
    - Lowercase
    - Remove URLs
    - Remove emails
    - Remove numbers
    - Remove punctuation
    - Remove extra spaces
    """

    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()

    return text


def lemmatize_text(text: str) -> str:
    """
    Lemmatize and remove stopwords
    """
    doc = nlp(text)
    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_space
    ]
    return " ".join(tokens)


def preprocess_text(text: str) -> str:
    """
    Full preprocessing pipeline
    """
    cleaned = clean_text(text)
    lemmatized = lemmatize_text(cleaned)
    return lemmatized
