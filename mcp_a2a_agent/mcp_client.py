import requests

BASE = "http://localhost:8000"


def git_diff(commit_range):
    return requests.get(f"{BASE}/git/diff", params={"range": commit_range}).json()


def git_files(commit_range):
    return requests.get(f"{BASE}/git/files", params={"range": commit_range}).json()


def read_files():
    return requests.get(f"{BASE}/files/read").json()
