from pathlib import Path

SUPPORTED = [
    ".py",
    ".java",
    ".js",
    ".ts",
    ".go",
    ".cpp"
]

class RepositoryLoader:

    def __init__(self, repo_path):
        self.repo_path = Path(repo_path)

    def load_repository(self):

        code_files = []

        for ext in SUPPORTED:
            code_files.extend(
                self.repo_path.rglob(f"*{ext}")
            )

        return code_files
