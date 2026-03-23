# 5001_MCP_A2A
Week 7 "In-Class" Activity

## Setup

bash:
pip install -r requirements.txt
uvicorn mcp_server:app --reload
python main.py review --range HEAD~2..HEAD

### 1. Start MCP server

bash:
uvicorn mcp_server:app --reload

Run Agent:
python main.py review --range HEAD~2..HEAD
