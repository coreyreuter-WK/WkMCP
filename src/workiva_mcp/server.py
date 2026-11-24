from mcp.server.fastmcp import FastMCP

mcp = FastMCP("workiva")


@mcp.tool()
def ping() -> str:
    """Health check. Returns "ok" so you can confirm the server is connected."""
    return "ok"


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
