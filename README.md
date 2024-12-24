# ClickHouse MCP Server

An MCP server for ClickHouse.

## Features

### Tools

* `run-select-query`
  - Execute SQL queries on your ClickHouse cluster.
  - Input: `sql` (string): The SQL query to execute.
  - All ClickHouse queries are run with `readonly = 1` to ensure they are safe.

* `list-databases`
  - List all databases on your ClickHouse cluster.

* `list-tables`
  - List all tables in a database.
  - Input: `database` (string): The name of the database.

## Configuration

1. Configure Claude Desktop to use the MCP server.
  - On MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
  - On Windows: `%APPDATA%/Claude/claude_desktop_config.json`
  - Paste the following temmplate in the file and replace the values with your ClickHouse credentials.

```json
  {
    "mcpServers": {
        "mcp-clickhouse": {
            "command": "uvx",
            "args": [
                "mcp-clickhouse"
            ],
            "env": {
                "CLICKHOUSE_HOST": "<CLICKHOUSE_HOST>",
                "CLICKHOUSE_PORT": "<CLICKHOUSE_PORT>",
                "CLICKHOUSE_USER": "<CLICKHOUSE_USER>",
                "CLICKHOUSE_PASSWORD": "<CLICKHOUSE_PASSWORD>"
            }
        }
    }
}
```

2. Restart Claude Desktop.

## Development

1. Add the following variables to a `.env` file in the root of the repository.

```
CLICKHOUSE_HOST=localhost
CLICKHOUSE_PORT=8123
CLICKHOUSE_USER=default
CLICKHOUSE_PASSWORD=
```

2. Update the `mcp-clickhouse` command in the `claude_desktop_config.json` file to use the `uvx` command.

```json
{
    "mcpServers": {
        "mcp-clickhouse-dev": {
            "command": "uv",
            "args": [
                "--directory",
                "/path/to/repo/mcp-clickhouse",
                "run",
                "mcp-clickhouse"
            ],
        }
    }
}
```

3. Restart Claude Desktop.