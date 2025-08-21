#!/bin/bash

# StraitsX MCP Server - AWS Deployment Script
# This script deploys the MCP server to AWS using ECS Fargate

set -e

echo "🚀 StraitsX MCP Server - AWS Deployment"
echo "======================================="

# Configuration
PROJECT_NAME="straitsx-mcp-server"
REGION="us-east-1"
ENVIRONMENT="production"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check prerequisites
check_prerequisites() {
    log_info "Checking prerequisites..."
    
    # Check AWS CLI
    if ! command -v aws &> /dev/null; then
        log_error "AWS CLI not found. Please install AWS CLI first."
        exit 1
    fi
    
    # Check Docker
    if ! command -v docker &> /dev/null; then
        log_error "Docker not found. Please install Docker first."
        exit 1
    fi
    
    # Check AWS credentials
    if ! aws sts get-caller-identity &> /dev/null; then
        log_error "AWS credentials not configured. Please run 'aws configure' first."
        exit 1
    fi
    
    log_success "Prerequisites check passed"
}

# Get AWS Account ID
get_account_id() {
    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    log_info "AWS Account ID: $ACCOUNT_ID"
}

# Create CloudFormation stack
deploy_infrastructure() {
    log_info "Deploying AWS infrastructure..."
    
    STACK_NAME="${PROJECT_NAME}-infrastructure"
    
    # Check if stack exists
    if aws cloudformation describe-stacks --stack-name $STACK_NAME --region $REGION &> /dev/null; then
        log_info "Stack exists, updating..."
        aws cloudformation update-stack \
            --stack-name $STACK_NAME \
            --template-body file://cloudformation-template.yaml \
            --parameters ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
                        ParameterKey=Environment,ParameterValue=$ENVIRONMENT \
            --capabilities CAPABILITY_IAM \
            --region $REGION
        
        aws cloudformation wait stack-update-complete --stack-name $STACK_NAME --region $REGION
    else
        log_info "Creating new stack..."
        aws cloudformation create-stack \
            --stack-name $STACK_NAME \
            --template-body file://cloudformation-template.yaml \
            --parameters ParameterKey=ProjectName,ParameterValue=$PROJECT_NAME \
                        ParameterKey=Environment,ParameterValue=$ENVIRONMENT \
            --capabilities CAPABILITY_IAM \
            --region $REGION
        
        aws cloudformation wait stack-create-complete --stack-name $STACK_NAME --region $REGION
    fi
    
    log_success "Infrastructure deployed successfully"
}

# Build and push Docker image
build_and_push_image() {
    log_info "Building and pushing Docker image..."
    
    # Get ECR repository URI
    ECR_URI="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${PROJECT_NAME}"
    
    # Login to ECR
    aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ECR_URI
    
    # Build image
    log_info "Building Docker image..."
    docker build -t $PROJECT_NAME -f Dockerfile ..
    
    # Tag image
    docker tag $PROJECT_NAME:latest $ECR_URI:latest
    docker tag $PROJECT_NAME:latest $ECR_URI:$(date +%Y%m%d-%H%M%S)
    
    # Push image
    log_info "Pushing Docker image to ECR..."
    docker push $ECR_URI:latest
    docker push $ECR_URI:$(date +%Y%m%d-%H%M%S)
    
    log_success "Docker image pushed successfully"
}

# Update ECS service
update_ecs_service() {
    log_info "Updating ECS service..."
    
    # Force new deployment
    aws ecs update-service \
        --cluster "${PROJECT_NAME}-cluster" \
        --service "${PROJECT_NAME}-service" \
        --force-new-deployment \
        --region $REGION
    
    log_info "Waiting for service to stabilize..."
    aws ecs wait services-stable \
        --cluster "${PROJECT_NAME}-cluster" \
        --services "${PROJECT_NAME}-service" \
        --region $REGION
    
    log_success "ECS service updated successfully"
}

# Get deployment information
get_deployment_info() {
    log_info "Getting deployment information..."
    
    # Get Load Balancer URL
    LB_URL=$(aws cloudformation describe-stacks \
        --stack-name "${PROJECT_NAME}-infrastructure" \
        --query 'Stacks[0].Outputs[?OutputKey==`LoadBalancerURL`].OutputValue' \
        --output text \
        --region $REGION)
    
    # Get ECR Repository URI
    ECR_REPO=$(aws cloudformation describe-stacks \
        --stack-name "${PROJECT_NAME}-infrastructure" \
        --query 'Stacks[0].Outputs[?OutputKey==`ECRRepositoryURI`].OutputValue' \
        --output text \
        --region $REGION)
    
    echo ""
    echo "🎉 Deployment Complete!"
    echo "======================"
    echo ""
    log_success "MCP Server URL: $LB_URL"
    log_success "ECR Repository: $ECR_REPO"
    log_success "Region: $REGION"
    echo ""
    echo "📋 Available Endpoints:"
    echo "  • Web Interface: $LB_URL"
    echo "  • Health Check: $LB_URL/health"
    echo "  • API Search: $LB_URL/api/search"
    echo "  • API List: $LB_URL/api/list"
    echo ""
    echo "🔧 Integration Examples:"
    echo "  • MCP Server URL: $LB_URL"
    echo "  • Docker Image: $ECR_REPO:latest"
    echo ""
}

# Add health endpoint to web interface
add_health_endpoint() {
    log_info "Adding health endpoint to web interface..."
    
    # Add health endpoint to web_interface.py
    cat >> ../web_interface.py << 'EOF'

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "StraitsX MCP Server",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat()
    })
EOF
    
    log_success "Health endpoint added"
}

# Main deployment function
main() {
    echo "Starting deployment process..."
    echo "Project: $PROJECT_NAME"
    echo "Region: $REGION"
    echo "Environment: $ENVIRONMENT"
    echo ""
    
    check_prerequisites
    get_account_id
    add_health_endpoint
    deploy_infrastructure
    build_and_push_image
    update_ecs_service
    get_deployment_info
    
    echo ""
    log_success "🚀 StraitsX MCP Server successfully deployed to AWS!"
    echo ""
    echo "📖 Next Steps:"
    echo "1. Test the web interface at the provided URL"
    echo "2. Configure your LLMs to use the MCP server"
    echo "3. Monitor the service in AWS Console"
    echo "4. Set up custom domain (optional)"
    echo "5. Configure SSL certificate (optional)"
}

# Run main function
main "$@"
