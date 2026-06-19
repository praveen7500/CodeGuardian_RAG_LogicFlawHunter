class RiskEngine:

    def score(self, finding):

        if "payment" in str(finding):
            return "CRITICAL"

        if "authorize" in str(finding):
            return "HIGH"

        return "MEDIUM"
