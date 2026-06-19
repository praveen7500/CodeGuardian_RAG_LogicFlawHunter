class ModelRouter:

    MODELS = {
        "logic":
            "deepseek-coder",

        "race":
            "codellama",

        "authorization":
            "qwen-coder"
    }

    def select(
        self,
        analysis_type
    ):

        return self.MODELS.get(
            analysis_type
        )
