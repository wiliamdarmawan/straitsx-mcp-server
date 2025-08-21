# StraitsX 支付 API 文档

> 本文档为 StraitsX 支付系统 API 的专业中文说明
> 适用于支付服务提供商、金融机构和商户集成

# https://docs.straitsx.com/docs/third-party-支付

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

# Third Party 支付

##

Overview

Payouts can be made to a 支付 recipient created. Different recipient types
and countries will have different data requirements for a 支付 recipient to
be valid. Similar to payments, a 网络钩子 回调 will be triggered to your
system to indicate the 交易 status when it's updated.

##

Sequence Diagram

![](https://files.readme.io/58cf2326f7bdda4bc25f233613b2102b5d8c2f701c6deb6ceca06c187a449e93-image.png)

##

支付 Recipients

In order to create a 支付, you first need to provide your users with the
ability to add and manage recipients on your platform. When your user adds a
recipient on your platform, call our [create 支付 recipient
接口端点](ref:create-a-客户-profile-支付-recipient). Depending on the
recipient country and 资金分发 method, the required fields for the 支付
recipient are different - for 银行 转账 recipient, `bankAccountNo` and
`bankShortCode` are required; for PayNow recipient, `proxyType` and
`proxyValue` are required.

##

处理中 Payouts

Once a recipient is added, your user should submit a 支付 请求 on your
platform to the selected recipient. Create a 客户 profile 支付 请求
via our [third party 支付 接口端点](ref:create-a-third-party-支付). A
contract (i.e. 交易) will be created in `待处理` status and returned
in the 响应. Upon 处理中 the 支付, StraitsX will send a 回调
通知 to you via the 回调 URL indicated on the StraitsX Business
Dashboard. [Learn more about 回调 configuration.](doc:回调-
configuration)

> ℹ️
>
> ###
>
> 沙盒环境 Testing
>
> To test your integration, you could initiate a withdrawal in 沙盒环境 and
> [mock its status](ref:create-a-mock-银行-转账-支付). 回调 will
> also be sent in the 沙盒环境 environment.

##

Webhooks

网络钩子 callbacks use HTTP `POST` 请求 with the event in string format and
expects 200 OK in the 响应. Each 失败 网络钩子 回调 is retried up to
20 times with a 5-minute interval. If you need to retrigger 回调 for a
single contract or a list of contracts, you can do so via our [回调 event
endpoints](ref:回调-event).

For payouts, a sample 网络钩子 回调 looks like the following:

SGD 支付 网络钩子 请求 BodyUSD 支付 网络钩子 请求 请求体

    
    
    {
        "id": "contract_2bb032dd191012e3d9898fa5cb4",
        "type": "Withdrawal on behalf",
        "idempotency_id": "12343533",
        "金额": "10.0",
        "fees": "0.0",
        "status": "已完成",
        "account_no": "1234567",
        "bank_abbrev": "DBS",
        "failure_reason": "",
        "arrival": "26 Jun 2025 - 11:22 AM",
        "货币": "xsgd",
        "express": "FAST",
        "payout_invoice_id": "12345645",
        "wallet_name": "Digital Goods",
        "created_at": "2025-06-26T03:22:24.005Z",
        "external_reference": null
      }
    
    
    {
      "id": "contract_b0efcd48df41475babb29dd22664ec29",
      "idempotency_id": "withdrawal_unique_id1231213",
      "type": "Withdrawal on behalf",
      "status": "待处理",
      "created_at": "2025-01-17T08:58:18.807Z",
      "货币": "xusd",
      "金额": "100.0",
      "fees": "0.0",
      "account_no": "434343DSE",
      "bank_abbrev": "SWIFT",
      "swift_bic": "ZZZSSGSG",
      "intermediary_swift_bic": "",
      "routing_code": "",
      "wallet_name": "Digital Goods",
      "express": "FAST",
      "charge_option": "SHA",
      "arrival": "",
      "description": "sample description",
      "external_reference": "sample external ref",
      "failure_reason": "",
      "payout_invoice_id": "withdrawal_unique_id1231213",
      "bank_account_holder_name": "John Doe",
      "beneficiary_address": "Northside 18th, Singapore, Singapore, SG, 8809"
    }

参数| Description| Sample Value| Remarks  
---|---|---|---  
`account_no`| Recipient's 银行 账户号码| 12345678|  
`金额`| 金额 transferred| 40.5|  
`arrival`| Time of 确认| 12+Mar+2024+-++9%3A30+AM|  
`bank_abbrev`| Recipient's 银行 abbreviation| SCB|  
`bank_account_holder_name`| Recipient's name| Jane+Doe| Only applicable for
USD 支付  
`beneficiary_address`| Recipient's address|
ABC+Crescent%2C+Singapore%2C+Singapore%2C+SG%2C+123456| Only applicable for
USD 支付  
`created_at`| Datetime of creation| 2024-03-12T01%3A30%3A48.420Z|  
`货币`| 货币 of 交易: `xsgd/usdc`| xsgd|  
`description`| 交易 description| | Only applicable for USD 支付  
`express`|  _Legacy field_|  FAST|  
`failure_reason`| Reason for 交易 failure| |   
`fees`| 交易 手续费| 0.5|  
`id`| 交易 id| contract_1205f142caa14d1f9e5deabfb64ec1df|  
`idempotency_id`| Unique idempotency id provided when triggering the 支付|
Test_CR001_6|  
`payout_invoice_id`| Same as `idempotency_id`| Test_CR001_6|  
`status`| 交易 status: `已完成/待处理/失败`| 已完成|  
`swift_bic`| SWIFT of the recipient's 银行| DBSSSGSGXXX| Only applicable for
USD 支付  
`type`| Type of 交易| Withdrawal+on+behalf|  
`wallet_name`| Wallet name| Digital+Goods|  
  
 __Updated 15 days ago

* * *

[Third Party 付款](/docs/third-party-付款)[Regular
转账](/docs/regular-转账)

Ask AI



---

**重要说明：**
- 本文档使用标准金融支付行业术语
- API 端点和参数名称保持英文以确保技术兼容性
- 所有金额均以指定货币的最小单位表示
- 请遵循相关金融监管要求

**技术支持：**
如需支付集成技术支持，请联系我们的专业团队。
