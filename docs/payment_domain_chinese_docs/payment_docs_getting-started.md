# StraitsX 支付 API 文档

> 本文档为 StraitsX 支付系统 API 的专业中文说明
> 适用于支付服务提供商、金融机构和商户集成

# https://docs.straitsx.com/docs/getting-started

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

# 快速入门

##

Before you begin

Ensure that you have the following prerequisites:

  * You have signed up for a [StraitsX 企业账户](https://www.straitsx.com/sg/sign-up)
  * You have been given the admin/developer role access for your StraitsX 企业账户

To learn more, see [Signing up for a StraitsX Business
Account.](https://support.straitsx.com/hc/en-
us/articles/4410453392409-Signing-up-for-a-StraitsX-business-account)

##

Using API Keys

> 🔐
>
> StraitsX is secured from unauthorized use by restricting API calls to those
> that provide proper 身份认证 credentials. These credentials are in the
> form of an API 密钥 - a unique alphanumeric string that associates your
> StraitsX 企业账户 with your users, and with the specific API.

![1. Access 沙盒环境
Mode](https://files.readme.io/c49208f-f2272c8-production_mode.png)

  1. Access 沙盒环境 Mode

![2. Access 沙盒环境 API 密钥](https://files.readme.io/1a86bbf-sandbox_key.png)

  2. Access 沙盒环境 API 密钥

You can retrieve your 沙盒环境 API keys on the 沙盒环境 Developer Tools Page.

> 👍
>
> 沙盒环境 API keys are now available when you [sign up for a StraitsX Business
> Account](https://www.straitsx.com/sg/sign-up).

##

沙盒环境 & 生产环境 Environments

The StraitsX APIs are available on two separate environments: 沙盒环境 and
生产环境.

> 🚧
>
> ###
>
> Host Update
>
> Note that we have officially moved to the latest API host since March 2024.
> If you are new to StraitsX API, please integrate using the latest host
> (`api-沙盒环境.straitsx.com` and `api.straitsx.com`).
>
> For existing partners, we will continue to support the old host until
> further notice, so there's nothing you need to do now. However, we strongly
> encourage you to switch over to the latest host whenever possible. If you
> require any support, feel free to reach out to us directly.

Environment| API Host (Latest)| API Host (Outdated)  
---|---|---  
沙盒环境| api-沙盒环境.straitsx.com| 沙盒环境.xfers.io/api  
生产环境| api.straitsx.com| xfers.io/api  
  
##

Integration Steps

Here’s a summary of the steps involved to integrate with StraitsX APIs.

  1. [Sign up for a StraitsX 企业账户](https://www.straitsx.com/sg/sign-up)
  2. [Create a developer role under the Team tab](https://support.straitsx.com/hc/en-us/articles/4410434330777-How-to-add-more-users-into-my-account-)
  3. [Switch to 沙盒环境 environment](doc:沙盒环境-生产环境-environments)
  4. [Get 沙盒环境 API Keys](doc:api-keys)
  5. [Test 客户 Profile API on 沙盒环境](doc:get-started)
  6. [Configure 回调 URL via Developer Tools](doc:回调-configuration)
  7. Test [付款](doc:get-started-with-付款-api) / [支付](doc:get-started-with-支付-api) API on 沙盒环境
  8. Test APIs on 生产环境 environment

__Updated 23 days ago

* * *

[StraitsX API Guides](/docs/introduction)[沙盒环境 & 生产环境
Environments](/docs/沙盒环境-生产环境-environments)

Ask AI



---

**重要说明：**
- 本文档使用标准金融支付行业术语
- API 端点和参数名称保持英文以确保技术兼容性
- 所有金额均以指定货币的最小单位表示
- 请遵循相关金融监管要求

**技术支持：**
如需支付集成技术支持，请联系我们的专业团队。
