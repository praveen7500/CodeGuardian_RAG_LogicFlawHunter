from neo4j import GraphDatabase

class Neo4jGraph:

    def __init__(
        self,
        uri,
        username,
        password
    ):

        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password)
        )

    def create_file_node(
        self,
        filename
    ):

        query = """
        MERGE (f:File {name:$filename})
        """

        with self.driver.session() as session:
            session.run(
                query,
                filename=filename
            )

    def create_import_relation(
        self,
        source,
        target
    ):

        query = """
        MATCH (a:File {name:$source})
        MATCH (b:File {name:$target})

        MERGE (a)-[:IMPORTS]->(b)
        """

        with self.driver.session() as session:
            session.run(
                query,
                source=source,
                target=target
            )
