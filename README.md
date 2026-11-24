# workiva-mcp

A Python MCP server (FastMCP + httpx) that exposes the Workiva Public API as tools an AI agent can call. See https://developers.workiva.com.

## Setup

1. Install [uv](https://docs.astral.sh/uv/) and run `uv sync`.
2. Copy `.env.example` to `.env` and fill in Workiva-provisioned credentials and the sandbox workspace ID. Never commit `.env`.
3. Run tests: `uv run pytest`.
4. Cursor picks up the server from `.cursor/mcp.json`.

## Rules

- Private repo in a Workiva GitHub org. Workiva-provisioned credentials only.
- Fake data only. Write tools are locked to `WORKIVA_WORKSPACE_ID`.
- Every tool is listed in `TOOLS.md`; every proven platform limit in `CAPABILITIES.md`.
