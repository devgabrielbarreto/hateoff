from pathlib import Path
import pandas as pd
import nltk
from nltk.stem import RSLPStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

for recurso in ("punkt", "punkt_tab", "stopwords", "rslp"):
    nltk.download(recurso, quiet=True)

STEMMER = RSLPStemmer()
STOPWORDS = set(nltk.corpus.stopwords.words("portuguese"))
DATASET_PATH = Path(__file__).resolve().parents[2] / "dataset" / "tweets.csv"


def tratar_texto(frase: str) -> str:
    tokens = nltk.word_tokenize(str(frase).lower(), language="portuguese")
    tokens_filtrados = [STEMMER.stem(p) for p in tokens if p not in STOPWORDS]
    return " ".join(tokens_filtrados)


def treinar_modelo(retornar_acuracia: bool = False):
    data = pd.read_csv(DATASET_PATH).dropna(subset=["text", "racismo"])
    textos_tratados = data["text"].apply(tratar_texto)

    X_train, X_test, y_train, y_test = train_test_split(
        textos_tratados, data["racismo"], test_size=0.2, random_state=42
    )

    pipeline = make_pipeline(TfidfVectorizer(), MultinomialNB())
    pipeline.fit(X_train, y_train)

    if retornar_acuracia:
        y_pred = pipeline.predict(X_test)
        return pipeline, accuracy_score(y_test, y_pred)

    return pipeline


if __name__ == "__main__":
    _, acuracia = treinar_modelo(retornar_acuracia=True)
    print(f"Modelo treinado com sucesso! Acurácia no teste: {acuracia:.2%}")