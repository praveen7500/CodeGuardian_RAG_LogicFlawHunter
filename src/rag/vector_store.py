import chromadb

class VectorStore:

    def __init__(self):

        client = chromadb.Client()

        self.collection = client.create_collection(
            name="repository"
        )

    def add_document(
        self,
        doc_id,
        content
    ):

        self.collection.add(
            ids=[doc_id],
            documents=[content]
        )

    def search(
        self,
        query,
        top_k=5
    ):

        return self.collection.query(
            query_texts=[query],
            n_results=top_k
        )
