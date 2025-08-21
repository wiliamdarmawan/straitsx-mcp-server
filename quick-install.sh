#!/bin/bash
# StraitsX MCP Server - One-line installer
# Usage: curl -sSL https://raw.githubusercontent.com/wiliamdarmawan/straitsx-mcp-server/main/quick-install.sh | bash

echo "🚀 Installing StraitsX MCP Server..."

# Download latest release
wget -q https://github.com/wiliamdarmawan/straitsx-mcp-server/releases/download/v1.0.0/straitsx-mcp-server.tar.gz

# Extract
tar -xzf straitsx-mcp-server.tar.gz
cd straitsx-mcp-server

# Install
chmod +x install.sh
./install.sh

echo "✅ StraitsX MCP Server installed successfully!"
echo "📖 See README.md for usage instructions"
echo "🔧 Configure your LLM with the MCP server settings"
echo ""
echo "🎯 Quick test:"
echo "python3 straitsx_q_tool.py search 'customer profile'"
