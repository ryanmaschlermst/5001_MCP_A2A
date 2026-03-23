from mcp_client import git_diff, read_files


class Reviewer:

    def run(self, commit_range, bus):

        diff = git_diff(commit_range)["diff"]
        files = read_files()["files"]

        findings = []

        if "TODO" in diff:
            findings.append("Found TODO comment")

        if "password" in diff.lower():
            findings.append("Possible password exposure")

        if "except:" in diff:
            findings.append("Bare except detected")

        evidence = [l for l in diff.splitlines() if l.startswith("+")][:5]

        bus.send("reviewer", "planner", {
            "findings": findings,
            "evidence": evidence,
            "diff": diff,
            "files": files
        })
