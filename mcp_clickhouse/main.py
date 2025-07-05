import os
from mcp_clickhouse.mcp_server import mcp

if __name__ == "__main__":
    # Get port from Render environment or default to 8000
    port = int(os.environ.get("PORT", 8000))
    
    # Run the server with SSE transport
    mcp.run(
        transport="sse",
        host="0.0.0.0", 
        port=port
    )