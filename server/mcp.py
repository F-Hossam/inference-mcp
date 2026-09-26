from fastmcp import FastMCP

mcp = FastMCP(name="cavemcp")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


if __name__ == "__main__":
    #mcp.run()
    mcp.run(transport="http", host="127.0.0.1", port=8000)