# StraitsX MCP Server 🚀

[![GitHub release](https://img.shields.io/github/release/wiliamdarmawan/straitsx-mcp-server.svg)](https://github.com/wiliamdarmawan/straitsx-mcp-server/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue.svg)](https://modelcontextprotocol.io/)

Professional MCP (Model Context Protocol) server providing access to StraitsX API documentation with accurate Chinese translations for payment industry terminology.

## 🎯 Features

- **🌐 Bilingual Documentation**: English and Chinese payment industry documentation
- **💰 Payment Expertise**: Accurate financial terminology (付款 vs 支付)
- **🤖 MCP Compatible**: Works with Q CLI, Claude Desktop, and other MCP-enabled LLMs
- **🔍 Real-time Search**: Search through 20+ documentation pages
- **🏢 Industry Focus**: PSP, merchant, and compliance-oriented content
- **👥 Customer Profile Support**: Complete CP vs CP+ documentation

## 📋 What is Customer Profile?

### Customer Profile (CP) vs Customer Profile+ (CP+)

| Feature | CP | CP+ |
|---------|----|----|
| **KYC Requirements** | Basic info, no full verification | Full KYC/KYB verification required |
| **Transaction Limits** | None | Yes, imposed per profile |
| **Compliance** | Standard | Enhanced regulatory requirements |
| **Currency Support** | Multiple | USD only currently |
| **Processing Time** | Immediate | ~30 minutes review |
| **Use Case** | Standard payments | High-value, regulated transactions |

## 🚀 Quick Installation

### One-line Install
```bash
curl -sSL https://raw.githubusercontent.com/wiliamdarmawan/straitsx-mcp-server/main/quick-install.sh | bash
```

### Manual Install
```bash
# Download latest release
wget https://github.com/wiliamdarmawan/straitsx-mcp-server/releases/download/v1.0.0/straitsx-mcp-server.tar.gz
tar -xzf straitsx-mcp-server.tar.gz
cd straitsx-mcp-server
./install.sh
```

## 🔧 Integration

### Q CLI
```bash
# Configure Q CLI
mkdir -p ~/.config/q
cp config/.q-mcp-config.json ~/.config/q/mcp-servers.json

# Start Q CLI
q chat

# Test: Ask "What is the difference between CP and CP+?"
```

### Claude Desktop
Add to your Claude Desktop config:
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

### Web Interface
```bash
# Start web interface
python3 web_interface.py
# Open http://localhost:5000
```

## 🛠️ Available Tools

1. **🔍 search_straitsx_docs** - Search documentation with Chinese/English support
2. **📄 get_straitsx_doc** - Retrieve specific documentation pages
3. **📋 list_straitsx_docs** - List available documentation by category
4. **💡 explain_payment_terms** - Explain payment industry terminology

## 📚 Documentation Categories

- **💳 Payment** (付款) - Money flowing into merchant accounts
- **💸 Payout** (支付) - Money flowing out from merchant accounts  
- **🔐 Authentication** - API security and access
- **🔑 API Keys** - Key management
- **❌ Errors** - Troubleshooting guide
- **👤 Customer Profiles** - CP vs CP+ management

## 🌐 Supported Languages

- **🇺🇸 English** - Original StraitsX documentation
- **🇨🇳 Simplified Chinese** - Professional payment industry translations

## 💼 Target Users

- 🏦 Payment Service Providers (PSP)
- 🏛️ Financial Institutions
- 🛒 Merchants integrating payments
- ⚖️ Compliance teams
- 🇨🇳 Chinese-speaking developers

## 🧪 Quick Test

```bash
# Search for customer profile information
python3 straitsx_q_tool.py search "customer profile"

# Get customer profile FAQ
python3 straitsx_q_tool.py get "customer-profile-faqs"

# List payment documentation
python3 straitsx_q_tool.py list "payment"

# Explain payment terminology
python3 straitsx_q_tool.py explain "first party payment"
```

## 📖 Example Queries

Try these with your LLM:
- "What is the difference between CP and CP+?"
- "How do I create a customer profile?"
- "What fields are required for business CP+?"
- "How long does CP+ review take?"
- "Show me PayNow integration guide"
- "Explain the difference between 付款 and 支付"

## 🐳 Docker Deployment

```bash
# Build Docker image
docker build -t straitsx-mcp-server .

# Run container
docker run -p 5000:5000 straitsx-mcp-server
```

## 📁 Project Structure

```
straitsx-mcp-server/
├── mcp_server_q_cli.py      # Main MCP server
├── straitsx_q_tool.py       # Standalone CLI tool
├── web_interface.py         # Web interface
├── install.sh               # Installation script
├── quick-install.sh         # One-line installer
├── config/                  # Configuration files
├── docs/                    # Documentation
│   └── payment_domain_chinese_docs/  # Chinese translations
├── DEPLOYMENT_GUIDE.md      # Comprehensive deployment guide
└── README.md               # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support

- 📖 Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions
- 🐛 Report issues on [GitHub Issues](https://github.com/wiliamdarmawan/straitsx-mcp-server/issues)
- 💬 Join discussions in [GitHub Discussions](https://github.com/wiliamdarmawan/straitsx-mcp-server/discussions)

## 🌟 Star History

If this project helps you, please consider giving it a ⭐!

---

**Built for the global payment industry** 🌍💳

*Empowering LLMs with professional payment documentation in multiple languages*
