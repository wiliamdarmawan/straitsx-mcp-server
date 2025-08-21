# StraitsX MCP Server

Professional MCP (Model Context Protocol) server providing access to StraitsX API documentation with accurate Chinese translations for payment industry terminology.

## 🎯 Features

- **Bilingual Documentation**: English and Chinese payment industry documentation
- **Payment Expertise**: Accurate financial terminology (付款 vs 支付)
- **MCP Compatible**: Works with Q CLI and other MCP-enabled LLMs
- **Real-time Search**: Search through 20+ documentation pages
- **Industry Focus**: PSP, merchant, and compliance-oriented content

## 🚀 Quick Start

### Installation
```bash
chmod +x install.sh
./install.sh
```

### Usage with Q CLI
```bash
# Configure Q CLI
mkdir -p ~/.config/q
cp config/.q-mcp-config.json ~/.config/q/mcp-servers.json

# Start Q CLI
q chat

# Test integration
# Ask: "Search StraitsX documentation for PayNow payments"
```

### Direct Usage
```bash
# Search documentation
python3 straitsx_q_tool.py search "PayNow payment"

# Get specific page
python3 straitsx_q_tool.py get "authentication"

# List all documentation
python3 straitsx_q_tool.py list "payment"

# Explain payment terms
python3 straitsx_q_tool.py explain "first party payment"
```

## 🛠️ Available Tools

1. **search_straitsx_docs** - Search documentation with Chinese/English support
2. **get_straitsx_doc** - Retrieve specific documentation pages
3. **list_straitsx_docs** - List available documentation by category
4. **explain_payment_terms** - Explain payment industry terminology

## 📚 Documentation Categories

- **Payment** (付款) - Money flowing into merchant accounts
- **Payout** (支付) - Money flowing out from merchant accounts  
- **Authentication** - API security and access
- **API Keys** - Key management
- **Errors** - Troubleshooting guide

## 🌐 Supported Languages

- **English** - Original StraitsX documentation
- **Simplified Chinese** - Professional payment industry translations

## 🏢 Target Users

- Payment Service Providers (PSP)
- Financial Institutions
- Merchants integrating payments
- Compliance teams
- Chinese-speaking developers

## 📞 Support

For issues or questions about StraitsX API integration, refer to the comprehensive documentation included in the `docs/` directory.

---

**Built for the global payment industry** 🌍💳
