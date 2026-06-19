class LogicFlawAgent:

    PATTERNS = [
        "admin",
        "approve",
        "authorize",
        "transfer",
        "payment"
    ]

    def analyze(self, files):

        findings = []

        for file in files:

            try:

                with open(
                    file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                for pattern in self.PATTERNS:

                    if pattern in content.lower():

                        findings.append({
                            "file": str(file),
                            "risk": "Potential Business Logic Issue",
                            "pattern": pattern
                        })

            except Exception:
                pass

        return findings
