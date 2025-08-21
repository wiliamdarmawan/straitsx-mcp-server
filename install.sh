#!/bin/bash
echo "🔧 Installing StraitsX MCP Server"

# Check Python version
python3 --version || { echo "❌ Python 3 required"; exit 1; }

# Install dependencies (if any)
echo "✅ Python 3 found"

# Make scripts executable
chmod +x mcp_server_q_cli.py
chmod +x straitsx_q_tool.py

echo "✅ StraitsX MCP Server installed successfully!"
echo "📖 See README.md for usage instructions"
