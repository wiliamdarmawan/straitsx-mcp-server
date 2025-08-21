# StraitsX MCP Server - AWS Deployment Guide

## 🚀 Multiple AWS Deployment Options

Choose the deployment method that best fits your needs:

### 1. 🔥 AWS Lambda (Serverless) - **RECOMMENDED**
**Best for**: Cost-effective, automatic scaling, pay-per-use
**Cost**: ~$0.20 per 1M requests (Free tier: 1M requests/month)

```bash
# Quick deployment
./deploy-lambda.sh

# Manual deployment
sam build --template-file sam-template.yaml
sam deploy --guided
```

**Pros:**
- ✅ No server management
- ✅ Automatic scaling
- ✅ Pay only for requests
- ✅ Built-in high availability
- ✅ Free tier available

**Cons:**
- ❌ Cold start latency (~1-2 seconds)
- ❌ 15-minute timeout limit

### 2. 🐳 ECS Fargate (Containerized)
**Best for**: Consistent performance, always-on service
**Cost**: ~$15-30/month for small instance

```bash
# Full infrastructure deployment
./deploy-to-aws.sh

# Manual steps
aws cloudformation create-stack --stack-name straitsx-mcp-infrastructure --template-body file://cloudformation-template.yaml --capabilities CAPABILITY_IAM
```

**Pros:**
- ✅ No cold starts
- ✅ Consistent performance
- ✅ Full container control
- ✅ Easy scaling

**Cons:**
- ❌ Higher cost (always running)
- ❌ More complex setup

### 3. 🖥️ EC2 (Virtual Machine)
**Best for**: Full control, custom configurations
**Cost**: ~$8-50/month depending on instance size

```bash
# Launch EC2 instance and run:
git clone https://github.com/wiliamdarmawan/straitsx-mcp-server.git
cd straitsx-mcp-server
./install.sh
python3 web_interface.py
```

## 📋 Prerequisites

### Required Tools:
```bash
# AWS CLI
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /

# Configure AWS credentials
aws configure

# For Lambda deployment - SAM CLI
brew install aws-sam-cli

# For ECS deployment - Docker
brew install docker
```

### AWS Permissions Required:
- CloudFormation (create/update stacks)
- Lambda (create/update functions)
- API Gateway (create/manage APIs)
- ECS (create clusters/services)
- ECR (push/pull images)
- IAM (create roles)
- VPC (create networking)

## 🎯 Quick Start - Lambda Deployment

### 1. Clone and Setup
```bash
git clone https://github.com/wiliamdarmawan/straitsx-mcp-server.git
cd straitsx-mcp-server/aws-deployment
```

### 2. Configure AWS
```bash
aws configure
# Enter your AWS Access Key ID, Secret, Region (us-east-1), and output format (json)
```

### 3. Deploy
```bash
./deploy-lambda.sh
```

### 4. Test
```bash
# The script will output your API URL, test it:
curl https://YOUR-API-ID.execute-api.us-east-1.amazonaws.com/prod/health
```

## 🔧 Configuration Options

### Environment Variables
```bash
# Set in CloudFormation parameters or Lambda environment
ENVIRONMENT=production
PORT=5000
REGION=us-east-1
```

### Scaling Configuration
```yaml
# For ECS Fargate
DesiredCount: 2
MinCapacity: 1
MaxCapacity: 10

# For Lambda
ReservedConcurrency: 100
ProvisionedConcurrency: 10
```

## 📊 Cost Comparison

| Deployment | Monthly Cost | Use Case |
|------------|-------------|----------|
| **Lambda** | $0-5 | Low to medium traffic, cost-sensitive |
| **ECS Fargate** | $15-30 | Consistent traffic, performance-critical |
| **EC2 t3.micro** | $8-12 | Development, testing |
| **EC2 t3.small** | $15-20 | Production, moderate load |

## 🌐 Post-Deployment Setup

### 1. Custom Domain (Optional)
```bash
# Create Route 53 hosted zone
aws route53 create-hosted-zone --name yourdomain.com --caller-reference $(date +%s)

# Create SSL certificate
aws acm request-certificate --domain-name api.yourdomain.com --validation-method DNS
```

### 2. Monitoring Setup
```bash
# CloudWatch alarms
aws cloudwatch put-metric-alarm \
  --alarm-name "StraitsX-MCP-HighErrorRate" \
  --alarm-description "High error rate for MCP server" \
  --metric-name Errors \
  --namespace AWS/Lambda \
  --statistic Sum \
  --period 300 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold
```

### 3. Security Hardening
```bash
# Enable AWS WAF (Web Application Firewall)
aws wafv2 create-web-acl \
  --name StraitsX-MCP-WAF \
  --scope CLOUDFRONT \
  --default-action Allow={}
```

## 🧪 Testing Your Deployment

### Health Check
```bash
curl https://your-api-url/health
```

### Search Documentation
```bash
curl -X POST https://your-api-url/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "customer profile", "category": "all"}'
```

### Get Specific Documentation
```bash
curl https://your-api-url/api/get/customer-profile-faqs
```

### List All Documentation
```bash
curl https://your-api-url/api/list?category=payment
```

### Explain Payment Terms
```bash
curl -X POST https://your-api-url/api/explain \
  -H "Content-Type: application/json" \
  -d '{"term": "customer profile"}'
```

## 🔍 Troubleshooting

### Common Issues:

#### 1. Lambda Cold Starts
```bash
# Solution: Enable provisioned concurrency
aws lambda put-provisioned-concurrency-config \
  --function-name straitsx-mcp-server-prod \
  --qualifier '$LATEST' \
  --provisioned-concurrency-config ProvisionedConcurrencyUnits=2
```

#### 2. ECS Task Failures
```bash
# Check logs
aws logs describe-log-streams --log-group-name /ecs/straitsx-mcp-server
aws logs get-log-events --log-group-name /ecs/straitsx-mcp-server --log-stream-name STREAM_NAME
```

#### 3. API Gateway Timeout
```bash
# Increase timeout (max 29 seconds for API Gateway)
aws apigateway update-integration \
  --rest-api-id YOUR-API-ID \
  --resource-id YOUR-RESOURCE-ID \
  --http-method POST \
  --patch-ops op=replace,path=/timeoutInMillis,value=29000
```

## 📈 Performance Optimization

### Lambda Optimization
```python
# Optimize cold starts
import json
import asyncio

# Global variables for reuse
server = None
loop = None

def lambda_handler(event, context):
    global server, loop
    if server is None:
        # Initialize once
        server = StraitsXMCPServer()
        loop = asyncio.new_event_loop()
```

### ECS Optimization
```yaml
# Resource allocation
Cpu: 512
Memory: 1024
# Health check optimization
HealthCheckGracePeriodSeconds: 60
HealthCheckIntervalSeconds: 30
```

## 🔒 Security Best Practices

1. **API Rate Limiting**
2. **WAF Protection**
3. **VPC Security Groups**
4. **IAM Least Privilege**
5. **CloudTrail Logging**
6. **Secrets Manager for sensitive data**

## 📞 Support

- 📖 [Full Documentation](https://github.com/wiliamdarmawan/straitsx-mcp-server)
- 🐛 [Report Issues](https://github.com/wiliamdarmawan/straitsx-mcp-server/issues)
- 💬 [Discussions](https://github.com/wiliamdarmawan/straitsx-mcp-server/discussions)

---

**Choose Lambda for cost-effectiveness, ECS for performance, EC2 for control** 🚀
