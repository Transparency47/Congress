# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4027?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4027
- Title: Healthy Competition for Better Care Act
- Congress: 119
- Bill type: S
- Bill number: 4027
- Origin chamber: Senate
- Introduced date: 2026-03-09
- Update date: 2026-04-30T19:51:26Z
- Update date including text: 2026-04-30T19:51:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in Senate
- 2026-03-09 - IntroReferral: Introduced in Senate
- 2026-03-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-09: Introduced in Senate

## Actions

- 2026-03-09 - IntroReferral: Introduced in Senate
- 2026-03-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4027",
    "number": "4027",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Healthy Competition for Better Care Act",
    "type": "S",
    "updateDate": "2026-04-30T19:51:26Z",
    "updateDateIncludingText": "2026-04-30T19:51:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-03-09T20:29:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
      "type": "Standing"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4027is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4027\nIN THE SENATE OF THE UNITED STATES\nMarch 9, 2026 Mr. Husted introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo ban anticompetitive terms in facility and insurance contracts that limit access to higher quality, lower cost care.\n#### 1. Short title\nThis Act may be cited as the Healthy Competition for Better Care Act .\n#### 2. Banning anticompetitive terms in facility and insurance contracts that limit access to higher quality, lower cost care\n##### (a) In general\n**(1) PHSA**\n**(A) In general**\nSection 2799A\u20139 of the Public Health Service Act ( 42 U.S.C. 300gg\u2013119 ) is amended\u2014\n**(i)**\nin the heading, by striking by removing and all that follows through information and inserting ; prohibition on anticompetitive agreements ;\n**(ii)**\nin subsection (a)(5), in the first sentence, by striking section and inserting subsection ; and\n**(iii)**\nby adding at the end the following:\n(b) Protecting health plans network design flexibility (1) In general A group health plan or a health insurance issuer offering group or individual health insurance coverage may not enter into an agreement with a covered entity if such agreement, directly or indirectly\u2014 (A) restricts (including by operation of any agreement in effect between such covered entity and another covered entity) the group health plan or health insurance issuer from\u2014 (i) directing or steering participants or beneficiaries to other health care providers who are not subject to such agreement; or (ii) offering incentives to encourage participants or beneficiaries to utilize specific health care providers; (B) requires the group health plan or health insurance issuer to enter into any additional agreement with an affiliate of the covered entity; (C) requires the group health plan or health insurance issuer to agree to payment rates or other terms for any affiliate of the covered entity not party to the agreement; or (D) restricts other group health plans or health insurance issuers not party to the agreement from paying a lower rate for items or services than the plan or issuer involved in the agreement pays for such items or services. (2) Exceptions for certain provider group and value-based network designs Paragraph (1)(A) shall not apply to a group health plan or health insurance issuer offering group or individual health insurance coverage with respect to\u2014 (A) a health maintenance organization, if such health maintenance organization operates primarily through exclusive contracts with multi-specialty physician groups, nor to any arrangement between such a health maintenance organization and its affiliates; or (B) a value-based network arrangement, such as an exclusive provider network, accountable care organization, center of excellence, a provider sponsored health insurance issuer that operates primarily through aligned multi-specialty physician group practices or integrated health systems, or such other similar network arrangements as determined by the Secretary through guidance or rulemaking. (3) Covered entity defined For purposes of this subsection, the term covered entity means a health care provider, network or association of providers, third-party administrator, or other service provider offering access to a network of providers. (4) State grandfathering option An applicable State authority may make a determination that the prohibitions under paragraph (1)(A) (relating to conditions that would direct or steer enrollees to, or offer incentives to encourage enrollees to use, other health care providers) will not apply in the State with respect to any specified agreement executed on June 19, 2019, and any agreements related to such specified agreement executed on or before December 31, 2020, for a maximum length of nonapplicability of up to 10 years from the date of execution of the contract if the applicable State authority determines that the contract is unlikely to significantly lessen competition. With respect to a specified agreement for which an applicable State authority has made a determination under the preceding sentence, an applicable State authority may determine whether renewal of the contract, within the applicable 10-year period, is allowed. (5) Rule of construction Except as provided in paragraph (1), nothing in this subsection shall be construed to limit network design or cost or quality initiatives by a group health plan or health insurance issuer, including accountable care organizations, exclusive provider organizations, networks that tier providers by cost or quality or steer enrollees to centers of excellence, or other pay-for-performance programs. .\n**(B) Regulations**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services, in consultation with the Secretary of Labor and the Secretary of the Treasury, shall promulgate regulations to carry out the amendments made by this paragraph.\n**(2) Employee Retirement Income Security Act of 1974**\n**(A) In general**\nSection 724 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185m ) is amended\u2014\n**(i)**\nin the heading, by striking by removing and all that follows through information and inserting ; prohibition on anticompetitive agreements ;\n**(ii)**\nin subsection (a)(4), in the first sentence, by striking section and inserting subsection ; and\n**(iii)**\nby adding at the end the following:\n(b) Protecting health plans network design flexibility (1) In general A group health plan or a health insurance issuer offering group health insurance coverage may not enter into an agreement with a covered entity if such agreement, directly or indirectly\u2014 (A) restricts (including by operation of any agreement in effect between such covered entity and another covered entity) the group health plan or health insurance issuer from\u2014 (i) directing or steering participants or beneficiaries to other health care providers who are not subject to such agreement; or (ii) offering incentives to encourage participants or beneficiaries to utilize specific health care providers; (B) requires the group health plan or health insurance issuer to enter into any additional agreement with an affiliate of the covered entity; (C) requires the group health plan or health insurance issuer to agree to payment rates or other terms for any affiliate of the covered entity not party to the agreement; or (D) restricts other group health plans or health insurance issuers not party to the agreement from paying a lower rate for items or services than the plan or issuer involved in the agreement pays for such items or services. (2) Exceptions for certain provider group and value-based network designs Paragraph (1)(A) shall not apply to a group health plan or health insurance issuer offering group health insurance coverage with respect to\u2014 (A) a health maintenance organization, if such health maintenance organization operates primarily through exclusive contracts with multi-specialty physician groups, nor to any arrangement between such a health maintenance organization and its affiliates; or (B) a value-based network arrangement, such as an exclusive provider network, accountable care organization, center of excellence, a provider sponsored health insurance issuer that operates primarily through aligned multi-specialty physician group practices or integrated health systems, or such other similar network arrangements as determined by the Secretary through guidance or rulemaking. (3) Covered entity defined For purposes of this subsection, the term covered entity means a health care provider, network or association of providers, third-party administrator, or other service provider offering access to a network of providers. (4) State grandfathering option An applicable State authority may make a determination that the prohibitions under paragraph (1)(A) (relating to conditions that would direct or steer enrollees to, or offer incentives to encourage enrollees to use, other health care providers) will not apply in the State with respect to any specified agreement executed on June 19, 2019, and any agreements related to such specified agreement executed on or before December 31, 2020, for a maximum length of nonapplicability of up to 10 years from the date of execution of the contract if the applicable State authority determines that the contract is unlikely to significantly lessen competition. With respect to a specified agreement for which an applicable State authority has made a determination under the preceding sentence, an applicable State authority may determine whether renewal of the contract, within the applicable 10-year period, is allowed. (5) Rule of construction Except as provided in paragraph (1), nothing in this subsection shall be construed to limit network design or cost or quality initiatives by a group health plan or health insurance issuer, including accountable care organizations, exclusive provider organizations, networks that tier providers by cost or quality or steer enrollees to centers of excellence, or other pay-for-performance programs. .\n**(B) Clerical amendment**\nThe table of contents in section 1 of such Act is amended, in the entry relating to section 724, by amending such entry to read as follows:\nSec. 724. Increasing transparency; prohibition on anticompetitive agreements. .\n**(C) Regulations**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Labor, in consultation with the Secretary of Health and Human Services and the Secretary of the Treasury, shall promulgate regulations to carry out the amendments made by this paragraph.\n**(3) IRC**\n**(A) In general**\nSection 9824 of the Internal Revenue Code of 1986 is amended\u2014\n**(i)**\nin the header, by striking by removing and all that follows through information and inserting ; prohibition on anticompetitive agreements ;\n**(ii)**\nin subsection (a)(4), in the first sentence, by striking section and inserting subsection ; and\n**(iii)**\nby adding at the end the following:\n(b) Protecting health plans network design flexibility (1) In general A group health plan may not enter into an agreement with a covered entity if such agreement, directly or indirectly\u2014 (A) restricts (including by operation of any agreement in effect between such covered entity and another covered entity) the group health plan from\u2014 (i) directing or steering participants or beneficiaries to other health care providers who are not subject to such agreement; or (ii) offering incentives to encourage participants or beneficiaries to utilize specific health care providers; (B) requires the group health plan to enter into any additional agreement with an affiliate of the covered entity; (C) requires the group health plan to agree to payment rates or other terms for any affiliate of the covered entity not party to the agreement; or (D) restricts other group health plans not party to the agreement from paying a lower rate for items or services than the plan involved in the agreement pays for such items or services. (2) Exceptions for certain provider group and value-based network designs Paragraph (1)(A) shall not apply to a group health plan with respect to\u2014 (A) a health maintenance organization, if such health maintenance organization operates primarily through exclusive contracts with multi-specialty physician groups, nor to any arrangement between such a health maintenance organization and its affiliates; or (B) a value-based network arrangement, such as an exclusive provider network, accountable care organization, center of excellence, a provider sponsored health insurance issuer that operates primarily through aligned multi-specialty physician group practices or integrated health systems, or such other similar network arrangements as determined by the Secretary through guidance or rulemaking. (3) Covered entity defined For purposes of this subsection, the term covered entity means a health care provider, network or association of providers, third-party administrator, or other service provider offering access to a network of providers. (4) State grandfathering option An applicable State authority may make a determination that the prohibitions under paragraph (1)(A) (relating to conditions that would direct or steer enrollees to, or offer incentives to encourage enrollees to use, other health care providers) will not apply in the State with respect to any specified agreement executed on June 19, 2019, and any agreements related to such specified agreement executed on or before December 31, 2020, for a maximum length of nonapplicability of up to 10 years from the date of execution of the contract if the applicable State authority determines that the contract is unlikely to significantly lessen competition. With respect to a specified agreement for which an applicable State authority has made a determination under the preceding sentence, an applicable State authority may determine whether renewal of the contract, within the applicable 10-year period, is allowed. (5) Rule of construction Except as provided in paragraph (1), nothing in this subsection shall be construed to limit network design or cost or quality initiatives by a group health plan, including accountable care organizations, exclusive provider organizations, networks that tier providers by cost or quality or steer enrollees to centers of excellence, or other pay-for-performance programs. .\n**(B) Clerical amendment**\nThe table of contents in section 1 of such Act is amended, in the entry relating to section 9824, by amending such entry to read as follows:\nSec. 9824. Increasing transparency; prohibition on anticompetitive agreements. .\n**(C) Regulations**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of the Treasury, in consultation with the Secretary of Health and Human Services and the Secretary of Labor, shall promulgate regulations to carry out the amendments made by this paragraph.\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply with respect to any contract entered into, amended, or renewed on or after the date that is 18 months after the date of enactment of this Act.",
      "versionDate": "2026-03-09",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-21",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Education and Workforce, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6248",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Healthy Competition for Better Care Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-04-02T18:38:41Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4027is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ban anticompetitive terms in facility and insurance contracts that limit access to higher quality, lower cost care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:37Z"
    },
    {
      "title": "Healthy Competition for Better Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Healthy Competition for Better Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:19Z"
    }
  ]
}
```
