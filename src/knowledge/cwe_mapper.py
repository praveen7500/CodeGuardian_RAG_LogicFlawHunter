class CWEMapper:

    RULES = {
        "authorization": "CWE-285",
        "race condition": "CWE-362",
        "idor": "CWE-639",
        "state machine": "CWE-841"
    }

    def map(self, finding):

        text = str(finding).lower()

        for keyword, cwe in self.RULES.items():

            if keyword in text:
                return cwe

        return "UNKNOWN"
