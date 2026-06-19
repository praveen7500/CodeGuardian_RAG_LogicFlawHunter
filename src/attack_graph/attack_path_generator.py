class AttackPathGenerator:

    def generate(
        self,
        findings
    ):

        attack_paths = []

        for finding in findings:

            attack_paths.append(
                {
                    "entry_point":
                        finding["file"],

                    "exploit":

                        "Potential privilege escalation",

                    "impact":

                        "Unauthorized access"
                }
            )

        return attack_paths
