from fastapi import FastAPI
import subprocess
import os

app = FastAPI()


@app.get("/git/diff")
def git_diff(range: str):
    result = subprocess.run(
        f"git diff {range}",
        shell=True,
        capture_output=True,
        text=True
    )
    return {"diff": result.stdout}


@app.get("/git/files")
def git_files(range: str):
    result = subprocess.run(
        f"git diff --name-only {range}",
        shell=True,
        capture_output=True,
        text=True
    )
    return {"files": result.stdout.splitlines()}


@app.get("/files/read")
def read_files():
    data = []
    for root, _, files in os.walk("."):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(root, f)
                try:
                    with open(path, "r", encoding="utf8") as fh:
                        data.append(fh.read()[:200])
                except:
                    pass
    return {"files": data}
