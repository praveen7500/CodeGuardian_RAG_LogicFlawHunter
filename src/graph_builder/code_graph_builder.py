import networkx as nx

class CodeGraphBuilder:

    def __init__(self):

        self.graph = nx.DiGraph()

    def add_file(self, file):

        self.graph.add_node(
            file,
            type="file"
        )

    def add_dependency(
        self,
        source,
        target
    ):

        self.graph.add_edge(
            source,
            target
        )

    def shortest_attack_path(
        self,
        source,
        target
    ):

        return nx.shortest_path(
            self.graph,
            source,
            target
        )
