#!/bin/bash

# StraitsX MCP Server - Lambda Deployment Script
# Quick serverless deployment to AWS Lambda

set -e

echo "🚀 StraitsX MCP Server - Lambda Deployment"
echo "=========================================="

# Configuration
PROJECT_NAME="straitsx-mcp-server"
REGION="us-east-1"
STAGE="prod"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Check if SAM CLI is installed
check_sam_cli() {
    if ! command -v sam &> /dev/null; then
        log_warning "SAM CLI not found. Installing..."
        
        # Install SAM CLI on macOS
        if [[ "$OSTYPE" == "darwin"* ]]; then
            if command -v brew &> /dev/null; then
                brew tap aws/tap
                brew install aws-sam-cli
            else
                log_info "Please install Homebrew first, then run: brew install aws-sam-cli"
                exit 1
            fi
        else
            log_info "Please install SAM CLI: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html"
            exit 1
        fi
    fi
    
    log_success "SAM CLI is available"
}

# Build the application
build_application() {
    log_info "Building SAM application..."
    
    sam build --template-file sam-template.yaml
    
    log_success "Application built successfully"
}

# Deploy the application
deploy_application() {
    log_info "Deploying to AWS Lambda..."
    
    sam deploy \
        --template-file sam-template.yaml \
        --stack-name "${PROJECT_NAME}-lambda" \
        --capabilities CAPABILITY_IAM \
        --region $REGION \
        --parameter-overrides Stage=$STAGE \
        --no-confirm-changeset \
        --no-fail-on-empty-changeset
    
    log_success "Deployment completed successfully"
}

# Get deployment information
get_deployment_info() {
    log_info "Getting deployment information..."
    
    # Get API Gateway URL
    API_URL=$(aws cloudformation describe-stacks \
        --stack-name "${PROJECT_NAME}-lambda" \
        --query 'Stacks[0].Outputs[?OutputKey==`ApiGatewayUrl`].OutputValue' \
        --output text \
        --region $REGION)
    
    # Get Lambda Function ARN
    LAMBDA_ARN=$(aws cloudformation describe-stacks \
        --stack-name "${PROJECT_NAME}-lambda" \
        --query 'Stacks[0].Outputs[?OutputKey==`LambdaFunctionArn`].OutputValue' \
        --output text \
        --region $REGION)
    
    echo ""
    echo "🎉 Lambda Deployment Complete!"
    echo "============================="
    echo ""
    log_success "API Gateway URL: $API_URL"
    log_success "Lambda Function: $LAMBDA_ARN"
    log_success "Region: $REGION"
    echo ""
    echo "📋 Available Endpoints:"
    echo "  • API Root: $API_URL/"
    echo "  • Health Check: $API_URL/health"
    echo "  • Search: $API_URL/api/search"
    echo "  • Get Doc: $API_URL/api/get/{page_name}"
    echo "  • List Docs: $API_URL/api/list"
    echo "  • Explain Terms: $API_URL/api/explain"
    echo ""
    echo "🧪 Quick Test:"
    echo "curl $API_URL/health"
    echo ""
}

# Test the deployment
test_deployment() {
    log_info "Testing deployment..."
    
    # Get API URL
    API_URL=$(aws cloudformation describe-stacks \
        --stack-name "${PROJECT_NAME}-lambda" \
        --query 'Stacks[0].Outputs[?OutputKey==`ApiGatewayUrl`].OutputValue' \
        --output text \
        --region $REGION)
    
    # Test health endpoint
    echo "Testing health endpoint..."
    curl -s "$API_URL/health" | python3 -m json.tool
    
    echo ""
    log_success "Deployment test completed"
}

# Main function
main() {
    echo "Starting Lambda deployment..."
    echo "Project: $PROJECT_NAME"
    echo "Region: $REGION"
    echo "Stage: $STAGE"
    echo ""
    
    check_sam_cli
    build_application
    deploy_application
    get_deployment_info
    test_deployment
    
    echo ""
    log_success "🚀 StraitsX MCP Server successfully deployed to AWS Lambda!"
    echo ""
    echo "💰 Cost Benefits:"
    echo "  • Pay per request (no idle costs)"
    echo "  • Automatic scaling"
    echo "  • No server management"
    echo "  • Free tier: 1M requests/month"
    echo ""
    echo "📖 Next Steps:"
    echo "1. Test all API endpoints"
    echo "2. Configure custom domain (optional)"
    echo "3. Set up monitoring and alerts"
    echo "4. Update your LLM configurations"
}

# Run main function
main "$@"
