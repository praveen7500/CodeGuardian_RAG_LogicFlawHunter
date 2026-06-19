class GraphRAG:

    def __init__(
        self,
        graph,
        vector_store
    ):

        self.graph = graph
        self.vector_store = vector_store

    def retrieve(
        self,
        query
    ):

        semantic_context = self.vector_store.search(
            query
        )

        return semantic_context
