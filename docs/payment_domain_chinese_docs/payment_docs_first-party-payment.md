# StraitsX 支付 API 文档

> 本文档为 StraitsX 支付系统 API 的专业中文说明
> 适用于支付服务提供商、金融机构和商户集成

# https://docs.straitsx.com/docs/first-party-付款

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

# First Party 付款

##

Overview

For each CP/CP+, you can generate a unique virtual 银行 account or PayNow QR
for 付款 collections. When our system successfully receive payments from
your users, we will trigger a 网络钩子 回调 to your system for you to
complete the transactions or credit the users for their top-ups.

##

Sequence Diagram

![](https://files.readme.io/1f1813c-image.png)

##

Create a Virtual 银行 Account (VA) or PayNow QR

To accept payments, you have the option to either create a virtual 银行
account or generate a persistent/dynamic PayNow QR code.

**Virtual 银行 Account (VA)** : You can [create a virtual 银行
account](ref:create-virtual-银行-accounts) to obtain 银行 转账 details,
which you can then provide to your users. This allows users to add a 收款人 in
their banking app and complete the 转账.

  * SGD VA: This account is created instantly.
  * USD VA: Activation typically takes 1 day. StraitsX will send a 回调 to the URL specified on your StraitsX Business Dashboard once the 账户状态 is updated. Note that additional information might be requested, and in some cases, the USD account application may be 已拒绝.

**PayNow QR** : Alternatively, you can also create PayNow QR which you can
display to your user for them to easily scan and make 转账.

  * Persistent PayNow: You can [create a persistent PayNow 付款 method](ref:create-a-persistent-PayNow-付款-method) and provide a QR code to your users. This allows users to make multiple payments using the same QR code. Note that each user can have only one persistent PayNow 付款 method.
  * Dynamic PayNow: You can [create a dynamic PayNow 付款](ref:create-a-dynamic-PayNow-付款) to generate a unique QR code for each individual 交易. When creating a dynamic PayNow QR code, you need to specify the 金额 and expiry date. Once a 付款 is made to a dynamic PayNow QR code, it cannot be used for additional payments.
  * _Note: Ensure that users do not alter the 参考号码 that is automatically populated after scanning the PayNow QR code, as modifications may result in 付款 rejection._

##

Sequence Diagram

![](https://files.readme.io/3823ebd-image.png)

##

Accepting 付款

Once your user make a 付款 to the VA or PayNow QR provided, StraitsX will
send a 回调 通知 to you via the 回调 URL indicated on the
StraitsX Business Dashboard. [Learn more about 回调
configuration.](doc:回调-configuration)

In the event that a 付款 is blocked by StraitsX, a 回调 will be fired
to you with the blocked code. In some cases, supplementary information or
proof may be required to continue 处理中 the 付款. Once the first
付款 is 已完成, the 客户 profile 银行 account will be verified
automatically.

_Note: If a 付款 is less than the 交易 fees charged, no 金额 will
be credited to your account._

> ℹ️
>
> ###
>
> 沙盒环境 Testing
>
> To test your integration, you could initiate a [mock 银行
> 转账](ref:create-a-mock-银行-转账-付款) or [mock PayNow
> 付款](ref:create-a-mock-PayNow-付款). 回调 will also be sent in
> the 沙盒环境 environment.

##

Webhooks

网络钩子 callbacks use HTTP `POST` 请求 with the event in string format and
expects 200 OK in the 响应. Each 失败 网络钩子 回调 is retried up to
20 times with a 5-minute interval. If you need to retrigger 回调 for a
single contract or a list of contracts, you can do so via our [回调 event
endpoints](ref:回调-event).

For incoming payments, a sample 网络钩子 回调 looks like the following:

网络钩子 请求 请求体

    
    
    {
      "additional_info": "",
      "金额": 0.01,
      "bank_account_no": "3225300696000",
      "blocked_reasons": [
        {
          "code": "NM-001"
        }
      ],
      "created_at": "2024-06-03T07:28:09.908Z",
      "货币": "xsgd",
      "customer_profile_id": "customer_profile_6972bb6a-2a5f-48dd-8ea7-2e07c50e94b3",
      "end_to_end_ref": "转账",
      "fees": 0.01,
      "id": "contract_d176576dfb1a498ead53d2b5f77e4122",
      "idempotency_id": "SUBSCRIPTION_0cd2163dc32dfdb76250db29f58da2ec",
      "merchant_ref": "ref_0d1w4m0xepp40",
      "sender_bank": "DBS 银行 Ltd",
      "sender_bank_account_holder_name": "JOHN DOE",
      "sender_bank_account_no": "01234567",
      "sender_bank_swift_bic": "DBSSSGSGXXX",
      "status": "待处理",
      "transaction_remarks": "abc",
      "type": "Direct 银行 转账"
    }

参数 Name| Description| Example Value  
---|---|---  
`additional_info`| Additional info of the 交易 (for FAST only)|  
`金额`| 金额 transferred| 0.01  
`bank_account_no`| Virtual 账户号码 receiving the 付款| 3225300696000  
`blocked_reasons`| Reason for the 交易 being blocked (if any)|
`[{"code":"NM-001"}]`  
`created_at`| 交易 created time| 2024-06-03T07%3A28%3A09.908Z  
`货币`| 交易 货币| xsgd  
`customer_profile_id`| 客户 profile ID|
customer_profile_6972bb6a-2a5f-48dd-8ea7-2e07c50e94b3  
`end_to_end_ref`| Sender's 交易 remarks| 转账  
`fees`| Fees incurred| 0.01  
`id`| Contract ID| contract_d176576dfb1a498ead53d2b5f77e4122  
`idempotency_id`| Unique reference no|
SUBSCRIPTION_0cd2163dc32dfdb76250db29f58da2ec  
`merchant_ref`| Unique `referenceId` indicated in [Create a virtual 银行
account](ref:create-a-virtual-银行-account)| ref_0d1w4m0xepp40  
`sender_bank`| Sender's 银行| DBS+银行+Ltd  
`sender_bank_account_holder_name`| Sender's name| JOHN+DOE  
`sender_bank_account_no`| Sender's 银行 account no| 01234567  
`sender_bank_swift_bic`| Sender's 银行 SWIFT (if available)| DBSSSGSGXXX  
`status`| 交易 Status| 待处理  
`transaction_remarks`| 交易 Remarks provided by sender| abc  
`type`| Type of 交易| Direct+银行+转账  
  
 __Updated about 1 month ago

* * *

What’s Next

Next, learn how to create a 支付 to facilitate your user's withdrawal
requests.

  * [First Party 支付](/docs/first-party-支付)

Ask AI



---

**重要说明：**
- 本文档使用标准金融支付行业术语
- API 端点和参数名称保持英文以确保技术兼容性
- 所有金额均以指定货币的最小单位表示
- 请遵循相关金融监管要求

**技术支持：**
如需支付集成技术支持，请联系我们的专业团队。
