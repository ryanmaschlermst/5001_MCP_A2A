import argparse
from orchestrator import Orchestrator

parser = argparse.ArgumentParser()

sub = parser.add_subparsers(dest="command", required=True)

review = sub.add_parser("review")
review.add_argument("--range", required=True)

improve_issue = sub.add_parser("improve-issue")
improve_issue.add_argument("--text", required=True)

improve_pr = sub.add_parser("improve-pr")
improve_pr.add_argument("--range", required=True)

args = parser.parse_args()

orch = Orchestrator()

if args.command == "review":
    orch.run_review(args.range)

elif args.command == "improve-issue":
    orch.improve_issue(args.text)

elif args.command == "improve-pr":
    orch.improve_pr(args.range)
