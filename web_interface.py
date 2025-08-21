#!/usr/bin/env python3
"""
StraitsX MCP Server Web Interface
Production-ready web interface for MCP server functionality
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import asyncio
import json
import os
from datetime import datetime
from mcp_server_q_cli import StraitsXMCPServer

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

server = StraitsXMCPServer()

@app.route('/')
def index():
    """Root endpoint with API information"""
    return jsonify({
        'service': 'StraitsX MCP Server',
        'version': '1.0.0',
        'description': 'Professional MCP server for StraitsX payment documentation',
        'features': [
            'Bilingual documentation (English/Chinese)',
            'Customer Profile management (CP vs CP+)',
            'Payment terminology explanations',
            'Real-time search capabilities'
        ],
        'endpoints': {
            'health': '/health',
            'search': '/api/search (POST)',
            'get_doc': '/api/get/{page_name}',
            'list_docs': '/api/list?category={category}',
            'explain_terms': '/api/explain (POST)'
        },
        'documentation': 'https://github.com/wiliamdarmawan/straitsx-mcp-server',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/health')
def health_check():
    """Health check endpoint for load balancers"""
    return jsonify({
        'status': 'healthy',
        'service': 'StraitsX MCP Server',
        'version': '1.0.0',
        'timestamp': datetime.utcnow().isoformat(),
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'documentation_loaded': len(server.doc_index) > 0
    })

@app.route('/api/search', methods=['POST'])
def search_docs():
    """Search documentation endpoint"""
    try:
        data = request.json or {}
        query = data.get('query', '')
        category = data.get('category', 'all')
        
        if not query:
            return jsonify({'error': 'Query parameter is required'}), 400
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            result = loop.run_until_complete(server.search_documentation(query, category))
            return jsonify(result)
        finally:
            loop.close()
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/get/<page_name>')
def get_doc(page_name):
    """Get specific documentation page"""
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            result = loop.run_until_complete(server.get_documentation(page_name))
            return jsonify(result)
        finally:
            loop.close()
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/list')
def list_docs():
    """List available documentation"""
    try:
        category = request.args.get('category', 'all')
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            result = loop.run_until_complete(server.list_documentation(category))
            return jsonify(result)
        finally:
            loop.close()
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/explain', methods=['POST'])
def explain_terms():
    """Explain payment terminology"""
    try:
        data = request.json or {}
        term = data.get('term', '')
        
        if not term:
            return jsonify({'error': 'Term parameter is required'}), 400
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            result = loop.run_until_complete(server.explain_payment_terms(term))
            return jsonify(result)
        finally:
            loop.close()
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status')
def status():
    """Detailed status information"""
    return jsonify({
        'service': 'StraitsX MCP Server',
        'status': 'operational',
        'version': '1.0.0',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'documentation': {
            'total_pages': len(server.doc_index),
            'categories': list(set(doc['category'] for doc in server.doc_index.values())),
            'loaded': len(server.doc_index) > 0
        },
        'features': {
            'search': True,
            'get_documentation': True,
            'list_documentation': True,
            'explain_terms': True,
            'bilingual_support': True,
            'customer_profiles': True
        },
        'timestamp': datetime.utcnow().isoformat()
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Not Found',
        'message': 'The requested endpoint was not found',
        'available_endpoints': [
            '/',
            '/health',
            '/api/search',
            '/api/get/{page_name}',
            '/api/list',
            '/api/explain',
            '/api/status'
        ]
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An internal server error occurred'
    }), 500

def initialize_server():
    """Initialize the MCP server"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(server.initialize())
        print(f"✅ Server initialized with {len(server.doc_index)} documentation pages")
    except Exception as e:
        print(f"❌ Error initializing server: {e}")
        raise
    finally:
        loop.close()

if __name__ == '__main__':
    print("🌐 StraitsX MCP Server Web Interface")
    print("📚 Initializing documentation...")
    
    initialize_server()
    
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('ENVIRONMENT', 'development') == 'development'
    
    print(f"📡 Starting web server on http://0.0.0.0:{port}")
    print(f"🔧 Debug mode: {debug}")
    print(f"🌍 Environment: {os.getenv('ENVIRONMENT', 'development')}")
    
    app.run(debug=debug, host='0.0.0.0', port=port)
