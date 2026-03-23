# 5001_MCP_A2A
Week 7 "In-Class" Activity

## Setup
Repeat line 2 to restart the MCP server
Repeat line 3 to tun the agent again

```bash
pip install -r requirements.txt
uvicorn mcp_server:app --reload
python main.py review --range HEAD~2..HEAD
