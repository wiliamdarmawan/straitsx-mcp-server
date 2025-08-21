# StraitsX MCP Server Deployment Guide

## 🌍 Making Your MCP Server Accessible to Other LLMs

This guide explains how to deploy and share your StraitsX MCP server so other LLM applications can use it.

## 📋 What is Customer Profile?

Based on the MCP server documentation, **Customer Profile** in StraitsX refers to:

### Customer Profile (CP) vs Customer Profile+ (CP+)

**Customer Profile (CP):**
- Basic customer information for payment processing
- Requires minimal KYC verification
- Suitable for standard payment flows
- No transaction limits imposed

**Customer Profile+ (CP+):**
- Enhanced customer verification with full KYC/KYB
- Extensive information requirements
- Transaction limits imposed for compliance
- Additional regulatory requirements
- Currently USD transactions only
- Longer processing time (~30 minutes)

### Key Differences:

| Feature | CP | CP+ |
|---------|----|----|
| KYC Requirements | Basic info, no full verification | Full KYC/KYB verification required |
| Transaction Limits | None | Yes, imposed per profile |
| Compliance | Standard | Enhanced regulatory requirements |
| Currency Support | Multiple | USD only currently |
| Processing Time | Immediate | ~30 minutes review |

## 🚀 Deployment Options

### Option 1: GitHub Repository (Recommended)

1. **Create GitHub Repository:**
```bash
# Repository is already initialized locally
# Push to GitHub:
git push -u origin main
```

2. **Create Release:**
- Go to GitHub repository
- Create a new release
- Upload `straitsx-mcp-server.tar.gz`
- Tag as `v1.0.0`

### Option 2: NPM Package (For Node.js LLMs)

```bash
# Create package.json for npm
cd straitsx-mcp-server
npm init -y
npm publish
```

### Option 3: Docker Container

```bash
# Create Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN chmod +x mcp_server_q_cli.py
RUN chmod +x install.sh

EXPOSE 8080

CMD ["python3", "mcp_server_q_cli.py"]
EOF

# Build and push
docker build -t straitsx-mcp-server .
docker tag straitsx-mcp-server:latest your-registry/straitsx-mcp-server:latest
docker push your-registry/straitsx-mcp-server:latest
```

## 🔧 Integration Instructions for Other LLMs

### For Q CLI Users:
```bash
# Download and install
wget https://github.com/wiliamdarmawan/straitsx-mcp-server/archive/main.zip
unzip main.zip
cd straitsx-mcp-server-main
./install.sh

# Configure Q CLI
mkdir -p ~/.config/q
cp config/.q-mcp-config.json ~/.config/q/mcp-servers.json

# Start Q CLI
q chat
```

### For Claude Desktop:
```json
{
  "mcpServers": {
    "straitsx-docs": {
      "command": "python3",
      "args": ["/path/to/straitsx-mcp-server/mcp_server_q_cli.py"],
      "env": {
        "PYTHONPATH": "/path/to/straitsx-mcp-server"
      }
    }
  }
}
```

### For Other MCP-Compatible LLMs:
```bash
# Direct usage
python3 mcp_server_q_cli.py

# Or use the standalone tool
python3 straitsx_q_tool.py search "customer profile"
```

## 📚 Available Tools

1. **search_straitsx_docs** - Search documentation
   ```bash
   # Example: Search for customer profile information
   python3 straitsx_q_tool.py search "customer profile"
   ```

2. **get_straitsx_doc** - Get specific documentation
   ```bash
   # Example: Get customer profile FAQ
   python3 straitsx_q_tool.py get "customer-profile-faqs"
   ```

3. **list_straitsx_docs** - List available documentation
   ```bash
   # Example: List all payment-related docs
   python3 straitsx_q_tool.py list "payment"
   ```

4. **explain_payment_terms** - Explain terminology
   ```bash
   # Example: Explain customer profile
   python3 straitsx_q_tool.py explain "customer profile"
   ```

## 🌐 Sharing Your MCP Server

### 1. MCP Registry (When Available)
- Submit to official MCP registry
- Include comprehensive documentation
- Provide usage examples

### 2. Community Sharing
- Share on LLM community forums
- Post on Reddit (r/LocalLLaMA, r/MachineLearning)
- Share on Discord servers
- Tweet about it with #MCP hashtags

### 3. Documentation Sites
- Create documentation on GitBook
- Add to Awesome MCP lists
- Submit to tool directories

## 📖 Usage Examples

### Customer Profile Queries:
```
"What is the difference between CP and CP+?"
"How do I create a customer profile?"
"What fields are required for business CP+?"
"How long does CP+ review take?"
```

### Payment Integration:
```
"How do I implement first party payments?"
"What's the difference between payment and payout?"
"Show me PayNow integration guide"
```

## 🔒 Security Considerations

- MCP server runs locally - no data sent to external servers
- Documentation is static - no API keys required
- Safe for production environments
- No sensitive data exposure

## 📞 Support

For issues with the MCP server:
1. Check GitHub issues
2. Review documentation in `docs/` directory
3. Test with standalone tool first
4. Verify MCP configuration

## 🎯 Next Steps

1. **Push to GitHub** - Make repository public
2. **Create Release** - Tag v1.0.0 with archive
3. **Share Widely** - Post in LLM communities
4. **Gather Feedback** - Improve based on usage
5. **Add Features** - Expand based on requests

---

**Your MCP server is now ready for global deployment! 🚀**
