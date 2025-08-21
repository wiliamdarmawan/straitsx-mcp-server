#!/usr/bin/env python3
"""
Q CLI Compatible MCP Server for StraitsX API Documentation
Implements the MCP protocol for Q CLI integration
"""

import asyncio
import json
import sys
import logging
from typing import Any, Dict, List, Optional
from pathlib import Path
import os

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("StraitsXMCP")

class StraitsXMCPServer:
    """MCP Server compatible with Q CLI"""
    
    def __init__(self):
        self.docs_directory = Path("payment_domain_chinese_docs")
        self.doc_index = {}
        self.server_info = {
            "name": "straitsx-docs-mcp-server",
            "version": "1.0.0"
        }
        
    async def initialize(self):
        """Initialize the MCP server"""
        print(f"[MCP SERVER] 🚀 Initializing StraitsX Documentation MCP Server for Q CLI")
        logger.info("Initializing StraitsX Documentation MCP Server for Q CLI")
        await self.load_documentation_index()
        print(f"[MCP SERVER] ✅ Server initialization completed")
        
    async def load_documentation_index(self):
        """Load and index all documentation files"""
        print(f"[MCP SERVER] 📚 Loading documentation index from {self.docs_directory}")
        self.doc_index = {}
        
        if not self.docs_directory.exists():
            print(f"[MCP SERVER] ⚠️  Documentation directory not found: {self.docs_directory}")
            logger.warning(f"Documentation directory not found: {self.docs_directory}")
            return
            
        # Index Chinese documentation
        file_count = 0
        for doc_file in self.docs_directory.glob("payment_*.md"):
            doc_name = doc_file.stem.replace("payment_docs_", "")
            print(f"[MCP SERVER] 📄 Processing document: {doc_name}")
            
            try:
                with open(doc_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                self.doc_index[doc_name] = {
                    "file": str(doc_file),
                    "content": content,
                    "category": self.categorize_document(doc_name)
                }
                file_count += 1
                print(f"[MCP SERVER] ✅ Loaded {doc_name} (category: {self.categorize_document(doc_name)})")
            except Exception as e:
                print(f"[MCP SERVER] ❌ Error loading {doc_file}: {e}")
                logger.error(f"Error loading {doc_file}: {e}")
                
        print(f"[MCP SERVER] 📊 Successfully loaded {len(self.doc_index)} documentation pages")
        logger.info(f"Loaded {len(self.doc_index)} documentation pages")
        
    def categorize_document(self, doc_name: str) -> str:
        """Categorize documentation based on filename"""
        print(f"[MCP SERVER] 🏷️  Categorizing document: {doc_name}")
        
        if "payment" in doc_name:
            category = "payment"
        elif "payout" in doc_name:
            category = "payout"
        elif "authentication" in doc_name or "auth" in doc_name:
            category = "authentication"
        elif "api-keys" in doc_name or "keys" in doc_name:
            category = "api-keys"
        elif "error" in doc_name:
            category = "errors"
        else:
            category = "general"
            
        print(f"[MCP SERVER] 📂 Document {doc_name} categorized as: {category}")
        return category
    
    async def handle_initialize(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle MCP initialize request"""
        print(f"[MCP SERVER] 🔧 Handling initialize request with params: {params}")
        await self.initialize()
        
        response = {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {},
                "resources": {}
            },
            "serverInfo": self.server_info
        }
        
        print(f"[MCP SERVER] ✅ Initialize response prepared: {self.server_info}")
        return response
    
    async def handle_tools_list(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle tools/list request"""
        print(f"[MCP SERVER] 🛠️  Handling tools/list request with params: {params}")
        
        tools_response = {
            "tools": [
                {
                    "name": "search_straitsx_docs",
                    "description": "Search through StraitsX API documentation for specific topics. Supports both English and Chinese content with payment industry expertise.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Search query for documentation (e.g., 'PayNow payment', 'authentication', '第一方付款')"
                            },
                            "category": {
                                "type": "string",
                                "enum": ["payment", "payout", "authentication", "api-keys", "errors", "all"],
                                "default": "all",
                                "description": "Documentation category to search in"
                            }
                        },
                        "required": ["query"]
                    }
                },
                {
                    "name": "get_straitsx_doc",
                    "description": "Get specific StraitsX API documentation page content with payment industry accurate Chinese translations.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "page_name": {
                                "type": "string",
                                "description": "Name of the documentation page (e.g., 'getting-started', 'authentication', 'first-party-payment')"
                            }
                        },
                        "required": ["page_name"]
                    }
                },
                {
                    "name": "list_straitsx_docs",
                    "description": "List all available StraitsX API documentation pages with categories and descriptions.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "category": {
                                "type": "string",
                                "enum": ["payment", "payout", "authentication", "api-keys", "errors", "all"],
                                "default": "all",
                                "description": "Filter by documentation category"
                            }
                        }
                    }
                },
                {
                    "name": "explain_payment_terms",
                    "description": "Explain StraitsX payment industry terminology with accurate Chinese translations. Helps distinguish between 付款 (payment/money in) vs 支付 (payout/money out).",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "term": {
                                "type": "string",
                                "description": "Payment term to explain (e.g., 'first party payment', 'payout', 'PayNow', 'KYC')"
                            }
                        },
                        "required": ["term"]
                    }
                }
            ]
        }
        
        print(f"[MCP SERVER] 📋 Returning {len(tools_response['tools'])} available tools")
        for tool in tools_response['tools']:
            print(f"[MCP SERVER] 🔧 Tool: {tool['name']}")
            
        return tools_response
    
    async def handle_tools_call(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle tools/call request"""
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        
        print(f"[MCP SERVER] 🔧 Handling tools/call request")
        print(f"[MCP SERVER] 🛠️  Tool: {tool_name}")
        print(f"[MCP SERVER] 📝 Arguments: {arguments}")
        
        try:
            if tool_name == "search_straitsx_docs":
                print(f"[MCP SERVER] 🔍 Executing search_straitsx_docs")
                result = await self.search_documentation(
                    query=arguments["query"],
                    category=arguments.get("category", "all")
                )
                
            elif tool_name == "get_straitsx_doc":
                print(f"[MCP SERVER] 📄 Executing get_straitsx_doc")
                result = await self.get_documentation(
                    page_name=arguments["page_name"]
                )
                
            elif tool_name == "list_straitsx_docs":
                print(f"[MCP SERVER] 📋 Executing list_straitsx_docs")
                result = await self.list_documentation(
                    category=arguments.get("category", "all")
                )
                
            elif tool_name == "explain_payment_terms":
                print(f"[MCP SERVER] 💡 Executing explain_payment_terms")
                result = await self.explain_payment_terms(
                    term=arguments["term"]
                )
                
            else:
                print(f"[MCP SERVER] ❌ Unknown tool: {tool_name}")
                result = {"error": f"Unknown tool: {tool_name}"}
            
            # Format result for Q CLI
            if isinstance(result, dict) and "error" not in result:
                formatted_result = json.dumps(result, indent=2, ensure_ascii=False)
                print(f"[MCP SERVER] ✅ Tool execution successful, result length: {len(formatted_result)} chars")
            else:
                formatted_result = str(result)
                print(f"[MCP SERVER] ⚠️  Tool execution completed with result: {formatted_result[:100]}...")
                
            response = {
                "content": [
                    {
                        "type": "text",
                        "text": formatted_result
                    }
                ]
            }
            
            print(f"[MCP SERVER] 📤 Returning response for tool: {tool_name}")
            return response
            
        except Exception as e:
            print(f"[MCP SERVER] ❌ Error in tool call {tool_name}: {e}")
            logger.error(f"Error in tool call {tool_name}: {e}")
            return {
                "content": [
                    {
                        "type": "text", 
                        "text": f"Error: {str(e)}"
                    }
                ]
            }
    
    async def search_documentation(self, query: str, category: str = "all") -> Dict[str, Any]:
        """Search through documentation"""
        print(f"[MCP SERVER] 🔍 Starting documentation search")
        print(f"[MCP SERVER] 🔎 Query: '{query}', Category: '{category}'")
        
        results = []
        query_lower = query.lower()
        
        print(f"[MCP SERVER] 📚 Searching through {len(self.doc_index)} documents")
        
        for doc_name, doc_data in self.doc_index.items():
            # Filter by category
            if category != "all" and doc_data["category"] != category:
                continue
                
            content = doc_data["content"].lower()
            if query_lower in content:
                print(f"[MCP SERVER] ✅ Match found in document: {doc_name}")
                
                # Extract relevant snippet
                lines = doc_data["content"].split('\n')
                relevant_lines = []
                
                for i, line in enumerate(lines):
                    if query_lower in line.lower():
                        # Get context around the match
                        start = max(0, i-2)
                        end = min(len(lines), i+3)
                        relevant_lines.extend(lines[start:end])
                        break  # Just get first match for brevity
                        
                results.append({
                    "document": doc_name,
                    "category": doc_data["category"],
                    "snippet": '\n'.join(relevant_lines[:8]),  # Limit snippet size
                    "relevance": "high" if query_lower in doc_name.lower() else "medium"
                })
        
        final_results = {
            "query": query,
            "results_count": len(results),
            "results": results[:10]  # Limit to top 10 results
        }
        
        print(f"[MCP SERVER] 📊 Search completed: {len(results)} results found")
        return final_results
    
    async def get_documentation(self, page_name: str) -> Dict[str, Any]:
        """Get specific documentation page"""
        print(f"[MCP SERVER] 📄 Getting documentation for page: '{page_name}'")
        
        if page_name not in self.doc_index:
            print(f"[MCP SERVER] ❌ Page '{page_name}' not found")
            print(f"[MCP SERVER] 📋 Available pages: {list(self.doc_index.keys())}")
            return {
                "error": f"Documentation page '{page_name}' not found",
                "available_pages": list(self.doc_index.keys())
            }
            
        doc_data = self.doc_index[page_name]
        content_length = len(doc_data["content"])
        is_truncated = content_length > 2000
        
        print(f"[MCP SERVER] ✅ Found page '{page_name}' (category: {doc_data['category']})")
        print(f"[MCP SERVER] 📊 Content length: {content_length} chars, truncated: {is_truncated}")
        
        result = {
            "page_name": page_name,
            "category": doc_data["category"],
            "content": doc_data["content"][:2000] + "..." if is_truncated else doc_data["content"],
            "full_content_available": is_truncated
        }
        
        return result
    
    async def list_documentation(self, category: str = "all") -> Dict[str, Any]:
        """List all available documentation"""
        print(f"[MCP SERVER] 📋 Listing documentation for category: '{category}'")
        
        docs = []
        
        for doc_name, doc_data in self.doc_index.items():
            if category == "all" or doc_data["category"] == category:
                doc_info = {
                    "name": doc_name,
                    "category": doc_data["category"],
                    "description": self.get_doc_description(doc_name)
                }
                docs.append(doc_info)
                print(f"[MCP SERVER] 📄 Added document: {doc_name} ({doc_data['category']})")
        
        result = {
            "total_documents": len(docs),
            "category_filter": category,
            "documents": docs
        }
        
        print(f"[MCP SERVER] 📊 Listed {len(docs)} documents for category '{category}'")
        return result
    
    def get_doc_description(self, doc_name: str) -> str:
        """Get description for a document"""
        print(f"[MCP SERVER] 📝 Getting description for document: {doc_name}")
        
        descriptions = {
            "getting-started": "Quick start guide for StraitsX API integration",
            "authentication": "API authentication and security setup",
            "api-keys": "API key management and configuration",
            "first-party-payment": "Direct customer-to-merchant payments (第一方付款)",
            "first-party-payout": "Direct merchant-to-customer payouts (第一方支付)",
            "third-party-payment": "Third-party mediated payments (第三方付款)",
            "third-party-payout": "Third-party mediated payouts (第三方支付)",
            "paynow-transfer-payments-guide": "Singapore PayNow instant payment system",
            "errors": "Error codes and troubleshooting guide",
            "webhooks-callbacks": "Webhook configuration and callback handling"
        }
        
        description = descriptions.get(doc_name, f"Documentation for {doc_name}")
        print(f"[MCP SERVER] 💬 Description: {description}")
        return description
    
    async def explain_payment_terms(self, term: str) -> Dict[str, Any]:
        """Explain payment terminology"""
        print(f"[MCP SERVER] 💡 Explaining payment term: '{term}'")
        term_lower = term.lower()
        
        explanations = {
            "payment": {
                "english": "Payment - Money flowing INTO the merchant account from customers",
                "chinese": "付款 - 客户向商户账户转入资金",
                "example": "Customer pays merchant for goods/services"
            },
            "payout": {
                "english": "Payout - Money flowing OUT from merchant account to recipients",
                "chinese": "支付 - 商户账户向收款人转出资金", 
                "example": "Merchant pays suppliers, employees, or refunds customers"
            },
            "first party": {
                "english": "First Party - Direct transaction between customer and merchant",
                "chinese": "第一方 - 客户与商户之间的直接交易",
                "example": "Customer directly pays merchant without intermediary"
            },
            "third party": {
                "english": "Third Party - Transaction through an intermediary",
                "chinese": "第三方 - 通过中介机构进行的交易",
                "example": "Payment processed through payment service provider"
            },
            "paynow": {
                "english": "PayNow - Singapore's instant payment system",
                "chinese": "PayNow - 新加坡即时支付系统",
                "example": "Real-time transfers using mobile numbers or NRIC"
            },
            "kyc": {
                "english": "KYC - Know Your Customer compliance requirements",
                "chinese": "KYC - 了解您的客户合规要求",
                "example": "Identity verification for regulatory compliance"
            }
        }
        
        # Find matching explanation
        for key, explanation in explanations.items():
            if key in term_lower:
                print(f"[MCP SERVER] ✅ Found explanation for term containing: '{key}'")
                result = {
                    "term": term,
                    "explanation": explanation,
                    "context": "StraitsX Payment API terminology"
                }
                return result
        
        print(f"[MCP SERVER] ❌ No explanation found for term: '{term}'")
        result = {
            "term": term,
            "explanation": {
                "english": f"Term '{term}' not found in payment terminology database",
                "chinese": f"术语 '{term}' 在支付术语数据库中未找到",
                "suggestion": "Try terms like: payment, payout, first party, third party, PayNow, KYC"
            }
        }
        return result

async def main():
    """Main MCP server loop for Q CLI"""
    print(f"[MCP SERVER] 🚀 Starting StraitsX MCP Server for Q CLI")
    server = StraitsXMCPServer()
    
    print(f"[MCP SERVER] 📡 Listening for JSON-RPC requests on stdin...")
    
    # Read from stdin and write to stdout for MCP protocol
    while True:
        try:
            # Read JSON-RPC request from stdin
            line = sys.stdin.readline()
            if not line:
                print(f"[MCP SERVER] 🔚 No more input, shutting down server")
                break
                
            print(f"[MCP SERVER] 📥 Received request: {line.strip()[:100]}...")
            request = json.loads(line.strip())
            method = request.get("method")
            params = request.get("params", {})
            request_id = request.get("id")
            
            print(f"[MCP SERVER] 🔧 Processing method: {method}, ID: {request_id}")
            
            # Handle different MCP methods
            if method == "initialize":
                print(f"[MCP SERVER] 🔧 Handling initialize method")
                result = await server.handle_initialize(params)
            elif method == "tools/list":
                print(f"[MCP SERVER] 🛠️  Handling tools/list method")
                result = await server.handle_tools_list(params)
            elif method == "tools/call":
                print(f"[MCP SERVER] 🔧 Handling tools/call method")
                result = await server.handle_tools_call(params)
            else:
                print(f"[MCP SERVER] ❌ Unknown method: {method}")
                result = {"error": f"Unknown method: {method}"}
            
            # Send JSON-RPC response to stdout
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": result
            }
            
            response_json = json.dumps(response)
            print(f"[MCP SERVER] 📤 Sending response (length: {len(response_json)} chars)")
            print(response_json)
            sys.stdout.flush()
            
        except EOFError:
            print(f"[MCP SERVER] 🔚 EOF received, shutting down server")
            break
        except Exception as e:
            print(f"[MCP SERVER] ❌ Error processing request: {e}")
            logger.error(f"Error processing request: {e}")
            error_response = {
                "jsonrpc": "2.0", 
                "id": request.get("id") if 'request' in locals() else None,
                "error": {"code": -1, "message": str(e)}
            }
            error_json = json.dumps(error_response)
            print(f"[MCP SERVER] 📤 Sending error response: {error_json}")
            print(error_json)
            sys.stdout.flush()

if __name__ == "__main__":
    asyncio.run(main())
