from abc import ABC, abstractmethod

class SecurityAgent(ABC):

    @abstractmethod
    def analyze(
        self,
        code_context,
        graph_context
    ):
        pass
