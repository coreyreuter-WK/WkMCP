from workiva_mcp.server import mcp, ping


def test_ping_returns_ok():
    assert ping() == "ok"


async def test_ping_is_registered():
    tools = await mcp.list_tools()
    assert [t.name for t in tools] == ["ping"]
