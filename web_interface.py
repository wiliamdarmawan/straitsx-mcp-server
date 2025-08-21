#!/usr/bin/env python3
"""
Simple Web Interface for StraitsX MCP Server
Allows web-based access to MCP server functionality
"""

from flask import Flask, render_template, request, jsonify
import asyncio
import json
from mcp_server_q_cli import StraitsXMCPServer

app = Flask(__name__)
server = StraitsXMCPServer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search_docs():
    data = request.json
    query = data.get('query', '')
    category = data.get('category', 'all')
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        result = loop.run_until_complete(server.search_documentation(query, category))
        return jsonify(result)
    finally:
        loop.close()

@app.route('/api/get/<page_name>')
def get_doc(page_name):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        result = loop.run_until_complete(server.get_documentation(page_name))
        return jsonify(result)
    finally:
        loop.close()

@app.route('/api/list')
def list_docs():
    category = request.args.get('category', 'all')
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        result = loop.run_until_complete(server.list_documentation(category))
        return jsonify(result)
    finally:
        loop.close()

@app.route('/api/explain', methods=['POST'])
def explain_terms():
    data = request.json
    term = data.get('term', '')
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        result = loop.run_until_complete(server.explain_payment_terms(term))
        return jsonify(result)
    finally:
        loop.close()

if __name__ == '__main__':
    # Initialize server
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(server.initialize())
    loop.close()
    
    print("🌐 StraitsX MCP Server Web Interface")
    print("📡 Starting web server on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
