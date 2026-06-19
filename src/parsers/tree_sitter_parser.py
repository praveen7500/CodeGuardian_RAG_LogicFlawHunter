from tree_sitter import Language, Parser

class CodeParser:

    def __init__(self, language):

        self.parser = Parser()

        self.language = language

    def parse(self, source_code):

        tree = self.parser.parse(
            bytes(source_code, "utf8")
        )

        return tree
