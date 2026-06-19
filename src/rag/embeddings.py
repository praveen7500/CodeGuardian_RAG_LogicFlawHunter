from sentence_transformers import SentenceTransformer

class EmbeddingEngine:

    def __init__(self):

        self.model = SentenceTransformer(
            "BAAI/bge-base-en-v1.5"
        )

    def embed(self, text):

        return self.model.encode(text)
