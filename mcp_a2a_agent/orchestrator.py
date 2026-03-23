from a2a import MessageBus
from agents.reviewer import Reviewer
from agents.planner import Planner
from agents.writer import Writer
from agents.gatekeeper import Gatekeeper
from mcp_client import git_diff


class Orchestrator:

    def __init__(self):
        self.bus = MessageBus()
        self.reviewer = Reviewer()
        self.planner = Planner()
        self.writer = Writer()
        self.gatekeeper = Gatekeeper()

    def run_review(self, commit_range):

        self.reviewer.run(commit_range, self.bus)

        for msg in self.bus.get_messages_for("planner"):
            self.planner.run(msg, self.bus)

        for msg in self.bus.get_messages_for("writer"):
            self.writer.run(msg, self.bus)

        for msg in self.bus.get_messages_for("gatekeeper"):
            self.gatekeeper.run(msg)

    def improve_issue(self, text):
        self.writer.improve_issue(text, self.bus)

        for msg in self.bus.get_messages_for("gatekeeper"):
            self.gatekeeper.run(msg)

    def improve_pr(self, commit_range):

        diff = git_diff(commit_range)["diff"]
        self.writer.improve_pr(diff, self.bus)

        for msg in self.bus.get_messages_for("gatekeeper"):
            self.gatekeeper.run(msg)
