# StraitsX 支付 API 文档

> 本文档为 StraitsX 支付系统 API 的专业中文说明
> 适用于支付服务提供商、金融机构和商户集成

# https://docs.straitsx.com/docs/PayNow-转账-payments-guide

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

# PayNow 转账 Payments Guide

客户 Profile API

> 📗
>
> Learn how to use the 付款 API to enable **Singapore PayNow 转账
> deposits** from your user.

##

Overview

Each connected user on your platform will be assigned a unique QR code for
PayNow transfers. We check the sender's name against the user's name to ensure
the 付款 is being made to the correct account. This creates a secure and
seamless experience for your users and makes it easy for your team to
reconcile these transactions.

#

Step 1 — [Display PayNow QR code](https://docs.straitsx.com/reference/create-
a-dynamic-PayNow-付款#/)

![Sample PayNow QR Code](https://files.readme.io/6bdfe96-QR_Code.png)

Sample PayNow QR Code

付款 Type| From| To  
---|---|---  
PayNow 转账| User's 银行 account| StraitsX 企业账户  
  
SandboxProduction

    
    
    curl --请求 POST \
         --url https://api-沙盒环境.straitsx.com/v1/沙盒环境/paynow_simulations \
         --请求头 'accept: application/json' \
         --请求头 'content-type: application/json' \
         --data '
    {
      "data": {
        "attributes": {
          "id": "string",
          "金额": 0,
          "sourceBankAccountHolderName": "string",
          "endToEndRef": "string"
        },
        "relationships": {
          "customerProfile": {
            "data": {
              "id": "string"
            }
          }
        }
      }
    }
    '
    
    
    curl --请求 POST \
         --url https://api-沙盒环境.straitsx.com/v1/payment_methods/PayNow \
         --请求头 'X-XFERS-APP-API-KEY: {YOUR_API_KEY}' \
         --请求头 'accept: application/json' \
         --请求头 'content-type: application/json' \
         --data '
    {
      "data": {
        "attributes": {
          "referenceId": "string"
        },
        "relationships": {
          "customerProfile": {
            "data": {
              "id": "string"
            }
          }
        }
      }
    }
    '

  * To provide 收款人 details for your user, initiate a 请求 to create a [PayNow QR code](https://docs.straitsx.com/reference/create-a-dynamic-PayNow-付款#/) to display the QR code
  * This enables your user to scan the QR code using their 银行 app

#

Step 2 — Add 回调 URL

On a successful completion of a deposit 交易, StraitsX will send a
回调 通知 to you via a 回调 URL indicated on the StraitsX
Business Dashboard.

![]()

> 📘
>
> Add the 回调 URL on the dashboard to receive a 回调 when the
> 交易 has been 已完成.

#

Step 3a — [Make a mock PayNow 转账
(沙盒环境)](https://docs.straitsx.com/reference/create-a-mock-PayNow-付款#/)

沙盒环境

    
    
    curl --请求 POST \
         --url https://api-沙盒环境.straitsx.com/v1/沙盒环境/paynow_simulations \
         --请求头 'accept: application/json' \
         --请求头 'content-type: application/json' \
         --data '
    {
      "data": {
        "attributes": {
          "id": "string",
          "金额": 0,
          "sourceBankAccountHolderName": "string",
          "endToEndRef": "string"
        },
        "relationships": {
          "customerProfile": {
            "data": {
              "id": "string"
            }
          }
        }
      }
    }
    '

  * In the 沙盒环境 environment, you can initiate a mock PayNow 转账 付款 to test the 转账 using PayNow
  * Input a name under `source_bank_account_holder_name` to test if the sender name is matched correctly to your user's name.

#

Step 3b — Make a PayNow 转账 (生产环境)

> 👍
>
> ###
>
> 银行 账户验证
>
> 银行 accounts will be verified and added to a 客户 profile on the first
> deposit when the 银行 name matches with the 客户 profile name.

To make a PayNow 转账 付款, your users can deposit funds via their 银行
app.

Scanning QR Code example

* * *

![Scanning a QR code to make a fund 转账 \(Last Updated: 31 Mar
2023\)](https://files.readme.io/84d0a4e-0291C055-71DD-4C2C-AABD-760CA6F53CAD.jpeg)

#

Step 4 — Confirm deposit has been received

###

Securing your 回调

When the 付款 is received, we will send a 回调 to the URL indicated on
the StraitsX Business Dashboard. The 回调 can be verified using the `HMAC-
SHA256` algorithm.

[Learn more about how to secure your 回调
→](https://docs.straitsx.com/docs/securing-your-回调#/)

  

回调

    
    
    {
      "end_to_end_ref": "paynow511212e2824686",
      "payment_method": {
        "id": 000,
        "owner_id": 13433,
        "unique_id": "paynow_5f46adf0cdww3-0a-b27a-be0bf61850fe",
        "created_at": "2025-07-18T07:44:46.892Z",
        "expires_at": "2025-07-20T15:44:46.000Z",
        "owner_type": "User",
        "updated_at": "2025-07-18T07:44:46.892Z",
        "external_id": "payment_method_298bed5d-3301212-121-2160e19b57ed",
        "reference_id": "BTC_POS17416_0cb7ed37-116fdwedwe0dd0e0-8_1752824686",
        "base64_encoded_image": "iVBO.....",
        "virtual_payment_address": null
      },
      "additional_info": "Others",
      "bank_account_no": "170218051",
      "bank_abbreviation": "DBS",
      "bank_account_name": "John Doe",
      "payment_method_type": "PayNow",
      "third_party_payment": true,
      "comply_advantage_submitted_at": "2025-07-18T15:46:22.290+08:00"
    }

  

* * *

#

Try it out!

快速入门 with StraitsX APIs is easy. Our business development and
integration teams will be with you every step of the way. If you have any
questions or would like to connect with our team, please do so via
[Support](https://docs.straitsx.com/docs/support)!

__Updated 14 days ago

* * *

[Regular 支付](/docs/regular-支付)[API Resources](/docs/api-resources)

Ask AI



---

**重要说明：**
- 本文档使用标准金融支付行业术语
- API 端点和参数名称保持英文以确保技术兼容性
- 所有金额均以指定货币的最小单位表示
- 请遵循相关金融监管要求

**技术支持：**
如需支付集成技术支持，请联系我们的专业团队。
