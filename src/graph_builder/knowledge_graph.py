import networkx as nx

class SecurityKnowledgeGraph:

    def __init__(self):

        self.graph = nx.DiGraph()

    def add_file(self, filename):

        self.graph.add_node(
            filename,
            type="file"
        )

    def add_dependency(self, source, target):

        self.graph.add_edge(
            source,
            target,
            relation="imports"
        )

    def export(self):

        return self.graph
