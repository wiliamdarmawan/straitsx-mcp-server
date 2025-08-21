# StraitsX 支付 API 文档

> 本文档为 StraitsX 支付系统 API 的专业中文说明
> 适用于支付服务提供商、金融机构和商户集成

# https://docs.straitsx.com/docs/common-faqs

## Home

  * [StraitsX API Guides](/docs/introduction)
  * [快速入门 __](/docs/getting-started)
    * [沙盒环境 & 生产环境 Environments](/docs/沙盒环境-生产环境-environments)
    * [API Keys](/docs/api-keys)
  * [Download Postman Collection](/docs/download-postman-collection)

## Integration Model

  * [First Party 转账 (客户 Profile & 客户 Profile+)__](/docs/first-party-转账)
    * [客户 Profile(CP) vs 客户 Profile+(CP+)](/docs/客户-profilecp-vs-客户-profilecp)
    * [ 客户 Profile and 银行 Account Creation](/docs/客户-profile-and-银行-account-creation)
    * [客户 Profile+ and 银行 Account Creation](/docs/客户-profile-and-银行-account-creation-1)
    * [First Party 付款](/docs/first-party-付款)
    * [First Party 支付](/docs/first-party-支付)
  * [Third Party 转账 (客户 Profile)__](/docs/third-party-转账)
    * [客户 Profile Creation](/docs/客户-profile-creation)
    * [ Third Party 付款](/docs/third-party-付款)
    * [Third Party 支付](/docs/third-party-支付)
  * [Regular 转账 __](/docs/regular-转账)
    * [Regular 付款](/docs/regular-付款)
    * [ Regular 支付](/docs/regular-支付)
  * [PayNow 转账 Payments Guide](/docs/PayNow-转账-payments-guide)

## Resources

  * [API Resources __](/docs/区块链-转账-out-guide)
    * [区块链 转账 Out API](/docs/区块链-转账-out-guide)
    * [ Swap API](/docs/swap-api)
    * [Purpose Code for FAST Payouts](/docs/purpose-code-for-FAST-payouts)
  * [Webhooks / Callbacks __](/docs/source-ip-addresses)
    * [Source IP Addresses](/docs/source-ip-addresses)
    * [ Securing Your 回调](/docs/securing-your-回调)
    * [回调 Configuration](/docs/回调-configuration)
    * [回调 Samples](/docs/回调-samples)
  * [交易 Status](/docs/交易-status)
  * [客户 Profile Statuses](/docs/客户-profile-statuses)
  * [交易 Limits (For CP+ only)](/docs/交易-limits-for-cp-only)
  * [Error Responses](/docs/errors)
  * [幂等 Requests](/docs/幂等-requests)
  * [交易 Safety](/docs/交易-safety)
  * [身份认证](/docs/身份认证)
  * [API Upgrades and Backward Compatibility](/docs/backward-compatibility)
  * [Rejection Reasons](/docs/rejection-reasons)

## FAQs

  * [General FAQs](/docs/common-faqs)
  * [银行 Account FAQs](/docs/银行-account-faqs)
  * [客户 Profile FAQs](/docs/客户-profile-faqs)
  * [Integration Model FAQs](/docs/integration-model-faqs)
  * [付款 FAQs](/docs/付款-faqs)
  * [支付 & 退款 FAQs](/docs/支付-faqs)
  * [Swap FAQs](/docs/swap-faqs)
  * [区块链 FAQs](/docs/区块链-faqs)
  * [交易 Limit FAQs](/docs/交易-limit-faqs)
  * [Need help?](/docs/support)

Powered by [ __](https://readme.com?ref_src=hub&project=straitsx)

# General FAQs

###

1\. How do I get access to your API?

Environment| Access Level| Requirements  
---|---|---  
沙盒环境(Testing mode)| ✅ By default, the Developer Tools menu is visible.✅ By
default, most APIs are available.🚧 Specialized APIs require additional
approval.| 1️⃣ Sign up for a StraitsX 企业账户 and Log in.2️⃣ Switch
to 沙盒环境 Mode.3️⃣ Log in to the StraitsX Developer Dashboard.4️⃣ Generate an
API 密钥 under Developer Tools.5️⃣ Contact StraitsX for specialized API access
if needed.  
生产环境(Live mode)| ❌ By default, the Developer Tools menu is hidden.❌ No
default access – All APIs require permission.✅ Must complete 客户身份识别 (Know Your
客户) verification.| 1️⃣ Complete business verification & 客户身份识别
客户入驻.2️⃣ 请求 API access approval from StraitsX.3️⃣ Once 已批准,
generate an API 密钥 in Developer Tools.  
  
Click on "Switch to 沙盒环境 Mode":

![](https://files.readme.io/a465b452508af4566df0e980acc48ad99243a154e210d938c700696692ec5fa0-Screenshot_2025-07-16_at_6.29.45_PM.png)  

Click on "Developer Tools" and your API will be there:

![](https://files.readme.io/b4da5e91eca4269d334fef1fce1c60ab9d35c813f19b3a9f523c7727fa5c085e-Screenshot_2025-07-16_at_6.31.29_PM.png)  

###

2.Does your API support multiple 付款 methods (e.g., credit cards, 银行
transfers, digital wallets)?

Our API supports 银行 转账 through the creation of a virtual 银行 account
or PayNow, depending on the 货币 of the 交易.

###

3\. Does the API support multi-货币 transactions?

Right now, our API supports transactions in USD and SGD.

###

4\. Can I use multiple APIs together?

Yes, our APIs are designed to be modular. For example, if your use case
requires it, it is possible to use the First-Party 付款 API coupled with
the Third-Party 支付 API. If you are not sure which APIs your use case
requires, contact our [sales team](https://www.straitsx.com/contact).

###

5\. What are the costs associated with using this API?

Our pricing is customized based on your business needs, 交易 volume,
and integration requirements. To get a personalized pricing quote, please
contact our [sales team](https://www.straitsx.com/contact).

###

6\. Are there additional fees for certain features or transactions?

Likewise, to get a personalized pricing quote, please contact our [sales
team](https://www.straitsx.com/contact).

###

7\. Are there penalties for 失败 transactions?

No penalties apply for 失败 transactions, but frequent failures due to
incorrect inputs may trigger fraud prevention checks on your account.

###

8\. How do I handle API rate limits?

If you exceed rate limits, your API requests may be throttled temporarily.
Optimize API usage by:

  * Using batch requests instead of multiple single requests.
  * Caching frequent API responses instead of repeatedly fetching the same data.

###

9\. How often does StraitsX update its API?

We continuously improve our API, and major updates are announced in our
[StraitsX Changelog](https://docs.straitsx.com/changelog#/).

###

10\. What is the API 密钥 expiry date?

The API keys are valid for 6 months. You may check when it expires on your
dashboard.

###

11\. What is the supported image file format and the upload size?

We support png, jpg and pdf at 10mb per https 请求.

###

12\. How often does StraitsX 重试 callbacks?

If the client side is down, we 重试 every 5 min up to 20 times.

###

13\. Will there be invoice for fees deducted?

No, if it's deducted on a per 交易 basis.

###

14\. Do you have a Country restrictions?

Yes, you may refer to
[this](https://support.straitsx.com/support/solutions/articles/157000366322-list-
of-restricted-countries) for the list of restricted countries.

###

15\. What are the different users in your StraitsX 企业账户?

For the different roles, you may refer to this
[link](https://support.straitsx.com/support/solutions/articles/157000366330-how-
to-manage-users-in-your-straitsx-business-account).

###

16\. What are the different contract types?

Contract Type| Description  
---|---  
AccountBalanceMigrationContract| User balance migration  
AdminContract| Transfers triggered by our internal operations team  
FiatDepositContract| Incoming fiat transactions via dashboard  
FiatWithdrawContract| Outgoing fiat transactions via dashboard  
FiatPaymentContract| Incoming fiat transactions via API  
FiatPayoutContract| Outgoing fiat transactions via API  
FiatRefundContract| SGD/USD Refunds triggered by our internal operations team  
OtcContract| OTC transactions  
StablecoinBalanceMigrationContract| Used when migrating users from our old to
new system  
StablecoinDepositContract| Incoming 区块链 transfers  
StablecoinWithdrawContract| Outgoing 区块链 transfers  
SwapContract| Swap 交易  
TransferContract| Crediting or debiting of 转账 balance to user's wallet
after the 交易 passes 合规 approval  
  
###

17\. Will I receive a reminder before my API 密钥 expires?

Yes, we will send you an email reminder 14 and 30 days in advance. Owner,
admin and developer roles will receive this email.

__Updated about 2 hours ago

* * *

[Rejection Reasons](/docs/rejection-reasons)[银行 Account FAQs](/docs/银行-
account-faqs)

Ask AI



---

**重要说明：**
- 本文档使用标准金融支付行业术语
- API 端点和参数名称保持英文以确保技术兼容性
- 所有金额均以指定货币的最小单位表示
- 请遵循相关金融监管要求

**技术支持：**
如需支付集成技术支持，请联系我们的专业团队。
