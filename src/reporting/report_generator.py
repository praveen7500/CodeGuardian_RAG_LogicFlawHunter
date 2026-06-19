import json

class ReportGenerator:

    @staticmethod
    def generate(findings, output):

        with open(output, "w") as f:

            json.dump(
                findings,
                f,
                indent=4
            )
