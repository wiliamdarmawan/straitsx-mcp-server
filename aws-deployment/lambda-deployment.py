#!/usr/bin/env python3
"""
StraitsX MCP Server - AWS Lambda Deployment
Serverless deployment option for cost-effective hosting
"""

import json
import asyncio
import logging
from typing import Dict, Any
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp_server_q_cli import StraitsXMCPServer

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Global server instance
server = None

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler for StraitsX MCP Server
    """
    global server
    
    try:
        # Initialize server if not already done
        if server is None:
            server = StraitsXMCPServer()
            # Run initialization in event loop
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(server.initialize())
            loop.close()
        
        # Extract request information
        http_method = event.get('httpMethod', 'GET')
        path = event.get('path', '/')
        query_params = event.get('queryStringParameters') or {}
        body = event.get('body')
        
        # Parse body if present
        request_data = {}
        if body:
            try:
                request_data = json.loads(body)
            except json.JSONDecodeError:
                pass
        
        # Create new event loop for async operations
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            # Route requests
            if path == '/health':
                result = handle_health()
            elif path == '/api/search' and http_method == 'POST':
                result = loop.run_until_complete(handle_search(request_data))
            elif path.startswith('/api/get/'):
                page_name = path.replace('/api/get/', '')
                result = loop.run_until_complete(handle_get_doc(page_name))
            elif path == '/api/list':
                category = query_params.get('category', 'all')
                result = loop.run_until_complete(handle_list_docs(category))
            elif path == '/api/explain' and http_method == 'POST':
                result = loop.run_until_complete(handle_explain_terms(request_data))
            elif path == '/':
                result = handle_root()
            else:
                result = {
                    'error': 'Not Found',
                    'message': f'Path {path} not found'
                }
                return create_response(404, result)
            
            return create_response(200, result)
            
        finally:
            loop.close()
            
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return create_response(500, {
            'error': 'Internal Server Error',
            'message': str(e)
        })

def create_response(status_code: int, body: Dict[str, Any]) -> Dict[str, Any]:
    """Create Lambda response object"""
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
        },
        'body': json.dumps(body, ensure_ascii=False, indent=2)
    }

def handle_health() -> Dict[str, Any]:
    """Health check endpoint"""
    return {
        'status': 'healthy',
        'service': 'StraitsX MCP Server',
        'version': '1.0.0',
        'deployment': 'AWS Lambda',
        'message': 'MCP Server is running successfully'
    }

def handle_root() -> Dict[str, Any]:
    """Root endpoint with API information"""
    return {
        'service': 'StraitsX MCP Server',
        'version': '1.0.0',
        'description': 'Professional MCP server for StraitsX payment documentation',
        'endpoints': {
            'health': '/health',
            'search': '/api/search (POST)',
            'get_doc': '/api/get/{page_name}',
            'list_docs': '/api/list?category={category}',
            'explain_terms': '/api/explain (POST)'
        },
        'documentation': 'https://github.com/wiliamdarmawan/straitsx-mcp-server'
    }

async def handle_search(request_data: Dict[str, Any]) -> Dict[str, Any]:
    """Handle search requests"""
    query = request_data.get('query', '')
    category = request_data.get('category', 'all')
    
    if not query:
        return {'error': 'Query parameter is required'}
    
    result = await server.search_documentation(query, category)
    return result

async def handle_get_doc(page_name: str) -> Dict[str, Any]:
    """Handle get document requests"""
    if not page_name:
        return {'error': 'Page name is required'}
    
    result = await server.get_documentation(page_name)
    return result

async def handle_list_docs(category: str) -> Dict[str, Any]:
    """Handle list documents requests"""
    result = await server.list_documentation(category)
    return result

async def handle_explain_terms(request_data: Dict[str, Any]) -> Dict[str, Any]:
    """Handle explain terms requests"""
    term = request_data.get('term', '')
    
    if not term:
        return {'error': 'Term parameter is required'}
    
    result = await server.explain_payment_terms(term)
    return result

# For local testing
if __name__ == '__main__':
    # Test event
    test_event = {
        'httpMethod': 'GET',
        'path': '/health',
        'queryStringParameters': None,
        'body': None
    }
    
    class MockContext:
        def __init__(self):
            self.function_name = 'test'
            self.memory_limit_in_mb = 128
            self.invoked_function_arn = 'test'
            self.aws_request_id = 'test'
    
    result = lambda_handler(test_event, MockContext())
    print(json.dumps(result, indent=2))
