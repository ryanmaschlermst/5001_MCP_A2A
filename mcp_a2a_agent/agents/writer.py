class Writer:

    def run(self, message, bus):

        action = message["content"]["action"]
        evidence = message["content"]["evidence"]
        risk = message["content"]["risk"]

        if action == "issue":
            draft = f"""
[Draft Issue]

Title: Code issue detected

Problem:
Potential issue found in recent changes.

Evidence:
{evidence}

Acceptance Criteria:
- Issue is resolved
- No unsafe patterns remain

Risk Level:
{risk}
"""
        else:
            draft = f"""
[Draft PR]

Title: Proposed improvements

Summary:
Refactoring and improvements based on code review.

Files Affected:
See git diff

Behavior Change:
Improves code quality

Test Plan:
- Run unit tests
- Validate manually

Risk Level:
{risk}
"""

        bus.send("writer", "gatekeeper", {
            "draft": draft,
            "type": action
        })

    def improve_issue(self, text, bus):

        improved = f"""
[Improved Issue]

Critique:
- Original issue lacks structure and clarity

Improved Version:
{text}

Acceptance Criteria:
- Clearly defined fix
- Testable outcomes
"""

        bus.send("writer", "gatekeeper", {
            "draft": improved,
            "type": "issue"
        })

    def improve_pr(self, diff, bus):

        improved = f"""
[Improved PR]

Critique:
- Original PR lacks structured summary

Improved Version:
Summary based on diff:

{diff[:300]}

Test Plan:
- Run all tests
- Validate changes
"""

        bus.send("writer", "gatekeeper", {
            "draft": improved,
            "type": "pr"
        })
