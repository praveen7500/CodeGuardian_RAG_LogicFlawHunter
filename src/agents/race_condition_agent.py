class RaceConditionAgent:

    KEYWORDS = [
        "thread",
        "lock",
        "mutex",
        "synchronized"
    ]

    def analyze(self, content):

        findings = []

        for keyword in self.KEYWORDS:

            if keyword in content.lower():

                findings.append({
                    "issue": "Potential Race Condition",
                    "keyword": keyword
                })

        return findings
