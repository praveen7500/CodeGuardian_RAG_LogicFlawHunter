class AuthorizationAgent:

    KEYWORDS = [
        "is_admin",
        "authorize",
        "permission",
        "role"
    ]

    def analyze(
        self,
        content
    ):

        findings = []

        for keyword in self.KEYWORDS:

            if keyword in content:

                findings.append(
                    {
                        "type":
                        "Authorization Issue",

                        "keyword":
                        keyword
                    }
                )

        return findings
