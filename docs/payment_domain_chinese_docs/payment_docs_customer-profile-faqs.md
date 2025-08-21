# StraitsX 支付 API 文档

> 本文档为 StraitsX 支付系统 API 的专业中文说明
> 适用于支付服务提供商、金融机构和商户集成

# https://docs.straitsx.com/docs/客户-profile-faqs

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

# 客户 Profile FAQs

###

1\. What are the fields required to create a 客户 profile for an end user?

[Business CP](https://docs.straitsx.com/reference/create-a-business-客户-
profile#/)| [Personal CP](https://docs.straitsx.com/reference/create-a-
personal-客户-profile#/)| [Business
CP+](https://docs.straitsx.com/reference/create-a-客户-profile-api#/)|
[Personal CP+](https://docs.straitsx.com/reference/create-a-personal-客户-
profile-api#/)  
---|---|---|---  
  
###

2\. What is the difference between CP and CP+?

CP| CP+  
---|---  
Offer named collections and payouts| Offer named collections and payouts  
Require basic info which does not go through 客户身份识别/KYB verification| Require
extensive info which needs to be fully 客户身份识别/KYB-ed  
| 交易 limit imposed for each 客户 profile  
| Additional 合规 requirements on 交易 notifications  
| Transactions under the CP+ model are currently in USD only  
  
###

3\. What are the differences in fields for Personal CP+ and CP+?

**Legend:**

✅ (Field is available but not mandatory), ❌ (Field is not available), ❗️(Field
is available and mandatory)

Field| Personal CP+| Personal CP  
---|---|---  
customerName| ✅| ❗️  
customerFirstName| ❗️| ❌  
customerLastName| ❗️| ❌  
customerNativeName| ✅| ✅  
registrationType| ❗️| ❗️  
registrationIdCountry| ❗️| ❗️  
registrationIdType| ❗️| ❗️  
registrationId| ❗️| ❗️  
registrationIdExpiryDate| ✅| ❌  
countryOfResidence| ❗️| ❌  
dateOfBirth| ❗️| ❗️  
nationality| ❗️| ❗️  
gender| ❗️| ✅  
email| ❗️| ✅  
phoneNo| ✅| ✅  
address| ❗️| ❗️  
businessIndustry| ❗️| ❌  
occupation| ❗️| ❌  
expectedAnnualTransactionAmount| ❗️| ❌  
expectedTransactionSize| ❗️| ❌  
expectedTransactionFrequency| ❗️| ❌  
annualIncome| ❗️| ❌  
totalWealth| ❗️| ❌  
sourceOfWealth| ✅| ❌  
ipAddresses| ❗️| ❌  
identityDocuments| ❗️| ❌  
  
###

4\. What are the differences in fields for business CP+ and CP+?

**Legend:**

✅ (Field is available but not mandatory), ❌ (Field is not available), ❗️(Field
is available and mandatory)

Field| Business CP+| Business CP  
---|---|---  
customerName| ❗️| ❗️  
customerNativeName| ✅| ❌  
registrationType| ❗️| ❗️  
registrationIdCountry| ❌| ✅  
registrationIdType| ❗️| ✅  
registrationId| ❗️| ❗️  
placeOfBiz| ❌| ✅  
placeOfBizCountry| ❌| ✅  
countryOfIncorporation| ❗️| ✅  
dateOfIncorporation| ❗️| ✅  
address| ❗️| ✅  
merchantRef| ✅| ❌  
entityLegalForm| ❗️| ❌  
businessContact| ❗️| ❌  
website| ✅| ❌  
operatingAddress| ❗️| ❌  
natureOfBusiness| ❗️| ❌  
otherNatureOfBusiness| ✅| ❌  
usOwnership| ❗️| ❌  
intermediaries| ❗️| ❌  
intermediariesDocuments| ✅| ❌  
monthlyTransactionVolume| ❗️| ❌  
sourceOfWealth| ✅| ❌  
sourceOfFunds| ❗️| ❌  
otherSourceOfFunds| ✅| ❌  
directors| ❗️| ❌  
beneficialOwners| ❗️| ❌  
trader| ❗️| ❌  
documents| ❗️| ❌  
  
###

5\. How long does it take to review a CP+ profile? If it’s 已拒绝, will a
reason be provided, and would you recommend retrying?

Typical 处理中 time takes no more than 30mins. If 已拒绝, a reason will
be provided and decision to 重试 is reliant on the type of rejection message.
e.g If rejection message is surrounding quality of documents, resubmission is
possible but only with remediation of the documents submitted. If rejection is
due to internal policy, such as sanctioned user, then recommendation is not to
重试. You can refer to the list of rejection reasons
[here](https://docs.straitsx.com/docs/rejection-reasons#/).

###

6\. Will you restrict the CP+ user's deposit or withdrawal to the IP address
submitted?

No, it's just for record purposes, providing the IP addresses record you have
of the user is sufficient.

__Updated 1 day ago

* * *

[银行 Account FAQs](/docs/银行-account-faqs)[Integration Model
FAQs](/docs/integration-model-faqs)

Ask AI



---

**重要说明：**
- 本文档使用标准金融支付行业术语
- API 端点和参数名称保持英文以确保技术兼容性
- 所有金额均以指定货币的最小单位表示
- 请遵循相关金融监管要求

**技术支持：**
如需支付集成技术支持，请联系我们的专业团队。
