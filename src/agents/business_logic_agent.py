from llm.prompt_templates import (
    BUSINESS_LOGIC_PROMPT
)

class BusinessLogicAgent:

    def __init__(
        self,
        llm
    ):
        self.llm = llm

    def analyze(
        self,
        context
    ):

        prompt = BUSINESS_LOGIC_PROMPT.format(
            context=context
        )

        result = self.llm.invoke(
            prompt
        )

        return result
