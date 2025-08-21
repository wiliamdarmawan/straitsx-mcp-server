#!/usr/bin/env python3
"""
Q CLI Tool for StraitsX Documentation
Direct integration without MCP protocol
"""

import sys
import json
import asyncio
from pathlib import Path

# Import our MCP server functionality
from mcp_server_q_cli import StraitsXMCPServer

async def main():
    if len(sys.argv) < 2:
        print("🔧 StraitsX Documentation Tool")
        print("=" * 40)
        print("Usage: python3 straitsx_q_tool.py <command> [args...]")
        print("")
        print("Commands:")
        print("  search <query>     - Search documentation")
        print("  get <page_name>    - Get specific page")
        print("  list [category]    - List available docs")
        print("  explain <term>     - Explain payment terms")
        print("")
        print("Examples:")
        print("  python3 straitsx_q_tool.py search 'PayNow payment'")
        print("  python3 straitsx_q_tool.py get 'authentication'")
        print("  python3 straitsx_q_tool.py list 'payment'")
        print("  python3 straitsx_q_tool.py explain 'first party payment'")
        return
    
    server = StraitsXMCPServer()
    await server.initialize()
    
    command = sys.argv[1]
    
    try:
        if command == "search":
            query = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "payment"
            print(f"🔍 Searching StraitsX documentation for: '{query}'")
            print("=" * 50)
            result = await server.search_documentation(query)
            
            if result["results_count"] > 0:
                for i, doc in enumerate(result["results"], 1):
                    print(f"\n📄 Result {i}: {doc['document']} ({doc['category']})")
                    print(f"📝 Snippet:")
                    print(doc['snippet'])
                    print("-" * 30)
            else:
                print("❌ No results found. Try different search terms.")
                
        elif command == "get":
            page_name = sys.argv[2] if len(sys.argv) > 2 else "authentication"
            print(f"📖 Getting StraitsX documentation: '{page_name}'")
            print("=" * 50)
            result = await server.get_documentation(page_name)
            
            if "error" not in result:
                print(f"📄 Page: {result['page_name']}")
                print(f"🏷️  Category: {result['category']}")
                print(f"📝 Content:")
                print(result['content'])
                if result.get('full_content_available'):
                    print("\n💡 Note: Content truncated. Full content available in file.")
            else:
                print(f"❌ Error: {result['error']}")
                if 'available_pages' in result:
                    print(f"📋 Available pages: {', '.join(result['available_pages'])}")
                
        elif command == "list":
            category = sys.argv[2] if len(sys.argv) > 2 else "all"
            print(f"📋 Listing StraitsX documentation (category: {category})")
            print("=" * 50)
            result = await server.list_documentation(category)
            
            print(f"📊 Total documents: {result['total_documents']}")
            print("")
            for doc in result['documents']:
                print(f"📄 {doc['name']}")
                print(f"   🏷️  Category: {doc['category']}")
                print(f"   📝 {doc['description']}")
                print("")
                
        elif command == "explain":
            term = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "payment"
            print(f"💡 Explaining StraitsX term: '{term}'")
            print("=" * 50)
            result = await server.explain_payment_terms(term)
            
            explanation = result['explanation']
            print(f"🔤 Term: {result['term']}")
            print(f"🇺🇸 English: {explanation['english']}")
            print(f"🇨🇳 Chinese: {explanation['chinese']}")
            if 'example' in explanation:
                print(f"💼 Example: {explanation['example']}")
            if 'suggestion' in explanation:
                print(f"💡 Suggestion: {explanation['suggestion']}")
                
        else:
            print(f"❌ Unknown command: {command}")
            print("💡 Use 'python3 straitsx_q_tool.py' to see available commands")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("💡 Make sure you're in the correct directory with documentation files")

if __name__ == "__main__":
    asyncio.run(main())
