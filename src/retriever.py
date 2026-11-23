
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class KnowledgeRetriever:
    """Retrieve relevant knowledge entries using TF-IDF similarity."""

    def __init__(self, knowledge: list[dict]):
        if not knowledge:
            raise ValueError("Knowledge base cannot be empty.")

        self.knowledge = knowledge

        self.documents = [
            f"{item['title']} {item['category']} {item['content']}"
            for item in knowledge
        ]

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2)
        )

        self.document_vectors = self.vectorizer.fit_transform(
            self.documents
        )

    
    def search(
        self,
        query: str,
        top_k: int = 3,
        min_score: float = 0.05
    ) -> list[dict]:

        if not query or not query.strip():
            return []

        if top_k <= 0:
            return []

        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            self.document_vectors
        ).flatten()

        ranked_indices = scores.argsort()[::-1]

        results = []

        for index in ranked_indices:

            score = float(scores[index])

            # Ignore irrelevant results
            if score < min_score:
                continue

            results.append({
                **self.knowledge[index],
                "score": round(score, 4)
            })

            if len(results) == top_k:
                break

        return results

