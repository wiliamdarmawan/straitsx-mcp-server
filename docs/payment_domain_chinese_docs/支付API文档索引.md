# StraitsX 支付 API 中文文档索引

欢迎使用 StraitsX 支付系统专业中文文档！

## 文档概述

本文档集合专为支付行业设计，包含 20 个专业翻译页面，使用标准金融支付术语。

### 💳 支付集成核心
- **快速入门** - 支付系统集成指南
- **身份认证** - API 访问和安全配置
- **API 密钥** - 密钥管理和权限控制

### 🏦 支付模式
- **第一方转账** - 直接账户间转账
- **第三方转账** - 通过中介机构转账
- **定期转账** - 预设周期性转账

### 💰 付款和支付处理
- **付款处理** - 商户向客户付款
- **支付处理** - 客户向商户付款  
- **PayNow 集成** - 新加坡即时支付系统

### 🔐 合规和风险管理
- **交易监控** - 实时交易风险控制
- **合规检查** - 监管要求和合规流程
- **反洗钱** - AML 和 KYC 流程

### 🛠️ 技术集成
- **错误处理** - 支付错误代码和解决方案
- **网络钩子** - 支付状态回调配置
- **交易安全** - 支付安全最佳实践

### ❓ 支付常见问题
- **集成问题** - 支付集成常见问题
- **交易问题** - 交易处理相关问题
- **合规问题** - 监管合规相关问题

## 专业术语说明

### 核心概念区分
- **付款 (Payment)**: 资金流入，客户向商户付款
- **支付 (Payout)**: 资金流出，商户向客户支付
- **转账 (Transfer)**: 账户间资金转移
- **交易 (Transaction)**: 完整的资金处理过程

### 账户类型
- **客户档案 (Customer Profile)**: 基础客户信息
- **客户档案增强版 (Customer Profile+)**: 增强验证客户信息
- **银行账户**: 实际资金存储账户

## 使用指南

### 支付服务提供商 (PSP)
1. 从**快速入门**了解集成流程
2. 配置**身份认证**和**API 密钥**
3. 选择适合的**支付模式**
4. 实施**合规检查**流程

### 商户集成
1. 理解**付款**和**支付**的区别
2. 配置**客户档案**管理
3. 设置**交易限额**和**风险控制**
4. 实施**网络钩子**接收交易状态

### 金融机构
1. 了解**监管合规**要求
2. 配置**反洗钱**和**KYC**流程
3. 设置**交易监控**系统
4. 实施**风险评估**机制

## 文件列表

1. [Api Keys](payment_docs_api-keys.md)
2. [身份认证](payment_docs_authentication.md)
3. [区块链 转账 Out Guide](payment_docs_blockchain-transfer-out-guide.md)
4. [Common Faqs](payment_docs_common-faqs.md)
5. [客户 Profile Faqs](payment_docs_customer-profile-faqs.md)
6. [客户 Profilecp Vs 客户 Profilecp](payment_docs_customer-profilecp-vs-customer-profilecp.md)
7. [Errors](payment_docs_errors.md)
8. [First Party 付款](payment_docs_first-party-payment.md)
9. [First Party 支付](payment_docs_first-party-payout.md)
10. [First Party 转账](payment_docs_first-party-transfer.md)
11. [快速入门](payment_docs_getting-started.md)
12. [PayNow 转账 Payments Guide](payment_docs_paynow-transfer-payments-guide.md)
13. [Purpose Code For FAST Payouts](payment_docs_purpose-code-for-fast-payouts.md)
14. [Regular 支付](payment_docs_regular-payout.md)
15. [Source Ip Addresses](payment_docs_source-ip-addresses.md)
16. [Swap Api](payment_docs_swap-api.md)
17. [Third Party 付款](payment_docs_third-party-payment.md)
18. [Third Party 支付](payment_docs_third-party-payout.md)
19. [Third Party 转账](payment_docs_third-party-transfer.md)
20. [Webhooks Callbacks](payment_docs_webhooks-callbacks.md)


## 监管合规提醒

使用本 API 时请注意：

1. **反洗钱 (AML)** - 遵循当地反洗钱法规
2. **了解您的客户 (KYC)** - 完成客户身份验证
3. **数据保护** - 遵循数据隐私法规
4. **交易报告** - 按要求报告大额交易
5. **制裁筛查** - 检查制裁名单

## 技术支持

### 支付集成支持
- **技术文档**: 详细的 API 集成指南
- **测试环境**: 沙盒环境用于集成测试
- **专业支持**: 支付行业专家技术支持

### 合规咨询
- **监管指导**: 各地区监管要求说明
- **合规流程**: 标准合规操作流程
- **风险管理**: 支付风险控制建议

---

**文档版本：** 支付领域专业版 v1.0  
**生成时间：** 2025年08月21日 15:03:42  
**适用对象：** 支付服务提供商、金融机构、商户
