class CAPECMapper:

    RULES = {
        "idor": "CAPEC-593",
        "workflow": "CAPEC-233",
        "race": "CAPEC-26"
    }

    def map(self, finding):

        text = str(finding).lower()

        for keyword, capec in self.RULES.items():

            if keyword in text:
                return capec

        return "UNKNOWN"
