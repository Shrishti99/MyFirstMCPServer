from mcp.server.fastmcp import FastMCP

# create MCP server
mcp = FastMCP("My-first-server")

@mcp.tool()
def getWeatherData(city: str) -> str:
    """Return weather for a city"""

    if city.lower() == "delhi":
        return "20 degree"
    elif city.lower() == "mumbai":
        return "25 degree"
    else:
        return "No data found for the asked city"


if __name__ == "__main__":
    mcp.run()