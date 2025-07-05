import os
from mcp_clickhouse.mcp_server import mcp
from fastmcp import FastMCP

# Create FastMCP app with SSE transport
app = FastMCP(mcp, transport="sse")

if __name__ == "__main__":
    import uvicorn
    
    # Get port from Render environment or default to 8000
    port = int(os.environ.get("PORT", 8000))
    
    # Run the server
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=port,
        log_level="info"
    )