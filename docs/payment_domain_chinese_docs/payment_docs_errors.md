# StraitsX 支付 API 文档

> 本文档为 StraitsX 支付系统 API 的专业中文说明
> 适用于支付服务提供商、金融机构和商户集成

# https://docs.straitsx.com/docs/errors

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

# Error Responses

The API categorises the various failures by their respective error codes. The
请求体 of the 响应 will be JSON in the following format:

JSON

    
    
    error: "string"
    error_code: "string"
    error_handling: "string"

The field `error` returns the 错误信息 specific to your 请求,
`error_code` returns the unique code identifying the error and
`error_handling` returns the instruction on how to resolve the error.

The string for `error_code_description` is used internally for our reference
as some error codes have the same `error_handling` instructions but under
completely different contexts. Should you face any difficulties with solving
the errors, please contact Developer Support.

##

XFE0XX: General

General Errors (XFE0XX)| 错误信息  
---|---  
XFE1|  _Error 响应 has been deprecated_  
XFE2|  _Error 响应 has been deprecated_  
XFE3| :error_code_description: "Internal"  
:error_handling: "Unexpected error. Try again later or contact 客户
support at <https://support.straitsx.com/hc/en-us/requests/new>."  
XFE4|  _Error 响应 has been deprecated_  
XFE5| :error_code_description: "Api token is invalid"  
:error_handling: "Make sure you entered the correct API 密钥 or contact
客户 support at <https://support.straitsx.com/hc/en-us/requests/new>."  
XFE6| :error_code_description: "Access to this 接口端点 is denied"  
:error_handling: "You do not have the necessary permissions to access this
接口端点. Please contact 客户 support at
<https://support.straitsx.com/hc/en-us/requests/new> for assistance."  
XFE7|  _Error 响应 has been deprecated_  
XFE8|  _Error 响应 has been deprecated_  
XFE9|  _Error 响应 has been deprecated_  
XFE10| :error_code_description: "Invalid environment"  
:error_handling: "请求 not supported for this environment."  
XFE11|  _Error 响应 has been deprecated_  
XFE12| :error_code_description: "Invalid 参数"  
:error_handling: "Make sure you entered the correct parameters."  
XFE13| :error_code_description: "Record not found"  
:error_handling: "Please check that you provided the correct API 密钥 and the
correct parameters."  
XFE14|  _Error 响应 has been deprecated_  
XFE15| :error_code_description: "Required 参数 empty"  
:error_handling: "Make sure you entered the correct required 参数."  
XFE16| :error_code_description: "Invalid 请求" or "Duplicated 请求"  
:error_handling: "API 请求 not supported. Make sure you entered the correct
API 密钥 or contact 客户 support at <https://support.straitsx.com/hc/en-
us/requests/new>."  
XFE17| :error_code_description: "Insufficient 客户 profile data for USD"  
:error_handling: "Please supplement missing information on 客户 Profile
required for USD capability"  
XFE18| :error_code_description: "Invalid 银行 account for USD withdrawal"  
:error_handling: "SWIFT code of this 银行 account is invalid"  
XFE19| :error_code_description: "Invalid 银行 account for USD withdrawal"  
:error_handling: "银行 account from a nonbank 金融机构 is not
allowed for USD withdrawal"  
XFE21| :error_code_description: "Insufficient 账户余额"  
:error_handling: "Make sure you have sufficient balance and try again."  
XFE22| :error_code_description: "Insufficient user kyb data for USD"  
:error_handling: "Please supplement missing information on User KYB required
for USD capability"  
  
##

XFE5XX: 银行

银行 Errors (XFE5XX)| 错误信息  
---|---  
XFE501|  _Error 响应 has been deprecated_  
XFE502|  _Error 响应 has been deprecated_  
XFE503| :error_code_description: "失败 name check"  
:error_handling: "银行 account name and name provided have to be similar."  
XFE504| :error_code_description: "Maximum number of 银行 accounts"  
:error_handling: "Delete existing 银行 accounts."  
XFE505| :error_code_description: "银行 abbrev provided invalid"  
:error_handling: "Use GET {{base-api-url}}api/v3/banks to get the correct 银行
abbrev."  
XFE506| :error_code_description: "Required 银行 data are empty"  
:error_handling: "银行 abbrev, 银行 account no, and 银行 account name are
required."  
XFE507|  _Error 响应 has been deprecated_  
  
##

XFE6XX: Withdrawal

Withdrawal Errors (XFE6XX)| 错误信息  
---|---  
XFE601| :error_code_description: "Conditions to withdraw not met. Can be
solved by changing 金额"  
:error_handling: "Your withdrawal does not meet the conditions required.
Please follow the instructions in the 响应."  
XFE602| :error_code_description: "Exceeds limit. Need to wait it out."  
:error_handling: "Your withdrawal exceeds the limit for the time period.
Please change the 金额 or verify your account."  
XFE603| :error_code_description: "Not allowed to carry out 请求"  
:error_handling: "Invalid 请求. Please call another API or contact 客户
support at [https://bit.ly/XfersSupport."](https://bit.ly/XfersSupport.%22)  
XFE604| :error_code_description: "Maximum Limit 商户 Withdrawal"  
:error_handling: "You have reached the maximum number of withdrawal 请求
per day. Please try again tomorrow. If you still wish to make a withdrawal,
please contact our 客户 support."  
  
__Updated about 1 month ago

* * *

[交易 Limits (For CP+ only)](/docs/交易-limits-for-cp-
only)[幂等 Requests](/docs/幂等-requests)

Ask AI



---

**重要说明：**
- 本文档使用标准金融支付行业术语
- API 端点和参数名称保持英文以确保技术兼容性
- 所有金额均以指定货币的最小单位表示
- 请遵循相关金融监管要求

**技术支持：**
如需支付集成技术支持，请联系我们的专业团队。
