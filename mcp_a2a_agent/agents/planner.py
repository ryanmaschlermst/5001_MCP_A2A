class Planner:

    def run(self, message, bus):

        findings = message["content"]["findings"]
        evidence = message["content"]["evidence"]

        if findings:
            action = "issue"
            risk = "medium"
        else:
            action = "pr"
            risk = "low"

        bus.send("planner", "writer", {
            "action": action,
            "evidence": evidence,
            "risk": risk
        })
