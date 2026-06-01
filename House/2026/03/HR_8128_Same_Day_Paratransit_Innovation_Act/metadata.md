# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8128?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8128
- Title: Same-Day Paratransit Innovation Act
- Congress: 119
- Bill type: HR
- Bill number: 8128
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-04-21T17:54:48Z
- Update date including text: 2026-04-21T17:54:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8128",
    "number": "8128",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001231",
        "district": "12",
        "firstName": "Lateefah",
        "fullName": "Rep. Simon, Lateefah [D-CA-12]",
        "lastName": "Simon",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Same-Day Paratransit Innovation Act",
    "type": "HR",
    "updateDate": "2026-04-21T17:54:48Z",
    "updateDateIncludingText": "2026-04-21T17:54:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-03-26T14:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8128ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8128\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Ms. Simon introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo foster greater deployment of same-day paratransit services for individuals with disabilities and to establish minimum standards for paratransit technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Same-Day Paratransit Innovation Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMobility access is a fundamental pillar of independence, equity, and dignity for individuals with disabilities, enabling access to daily necessities and the opportunity to participate in a well-rounded, connected life that would otherwise be out of reach.\n**(2)**\nAccording to the Department of Transportation Bureau of Transportation Statistics (BTS), an estimated 18,600,000 Americans have travel-limiting disabilities that could necessitate reliance on paratransit services to access employment, education, healthcare, and community life, yet they face significant and ongoing barriers to achieve mobility, equity, and inclusion.\n**(3)**\nOver 80 percent of the young adults with disabilities surveyed by the National Aging and Disability Transportation Center (NADTC) stated that they\u2019re often held back from activities because of lack of transportation or inability to drive, resulting in them feeling isolated, frustrated, and even trapped without reliable same-day transit, with access barriers compounded by income level, vehicle ownership, and strict or outdated eligibility and scheduling policies.\n**(4)**\nThe Census Bureau projects that almost 1 in 4 Americans will be aged 65 or older and the number of people over age 85 will triple by 2060, thereby increasing already constrained paratransit demand.\n**(5)**\nThe transportation provisions of the Americans with Disabilities Act of 1990 (ADA) only require that complementary paratransit be operated on a next-day basis, requiring riders with disabilities to know and schedule all trips at least 24 hours in advance and leaving no flexibility to adjust to last minute or day-of changes in plans.\n**(6)**\nThe lack of flexible, same-day transportation options hinders the lives and opportunities of persons with disabilities, negatively impacting their independence and participation in civic life and contributing to the 10 percent unemployment rate among working-age Americans with disabilities in July 2025, as reported by the Bureau of Labor Statistics.\n**(7)**\nTechnological advancements and product offerings now allow transit agencies to schedule and provide same-day paratransit services through dynamic trip matching, real-time route optimization, and the integration of multiple service providers through API or related mechanisms, all accessible through user-friendly mobile applications.\n**(8)**\nIn 2023, the Federal Transit Administration published a Dear Colleague letter to the transit industry extolling the benefits and opportunities for deploying same-day paratransit using existing formula funding.\n**(9)**\nWhereas, same-day paratransit has been proven to improve transit agency cost and service efficiencies, highlighted by MBTA\u2019s RIDE Flex program, which saw total trips increase by 53 percent and operational spend decrease by 6 percent over 3 years with the integration of a same-day service, per the Federal Transit Administration\u2019s Transit Cooperative Research Program (TCRP).\n**(10)**\nCongress recognizes the urgent need to modernize and expand same-day paratransit options through formula funding to incentivize transit agencies to provide same-day paratransit services that foster innovation and empower individuals with disabilities to choose the mobility solution that best fits their needs.\n#### 3. Accessibility innovation same-day paratransit\n##### (a) In general\nSection 5310(d) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by inserting except that a grant for a capital project directly related to the provision of same-day paratransit services shall be in an amount equal to 90 percent of the net capital costs of the project, as determined by the Secretary. after Secretary ; and\n**(2)**\nby amending paragraph (2) to read as follows:\n(2) Operating assistance A grant made under this section for operating assistance may not exceed an amount equal to\u2014 (A) 50 percent of the net operating costs of the project, as determined by the Secretary; (B) 70 percent of the net operating costs of a project to provide same-day paratransit service in compliance with the minimum standards established by the Administrator; or (C) 80 percent of the net operating costs of a project to provide same-day paratransit service in compliance with the minimum standards established by the Administrator and using vehicles operated exclusively by personnel employed by the recipient for same-day paratransit service. .\n##### (b) Urbanized area formula grants\nSection 5307(d) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by inserting , except that a grant for a capital project directly related to the provision of same-day paratransit services shall be in an amount equal to 90 percent of the net capital costs of the project, as determined by the Secretary. after the project ; and\n**(2)**\nby amending paragraph (2), to read as follows:\n(2) Operating assistance A grant made under this section for operating assistance may not exceed an amount equal to\u2014 (A) 50 percent of the net operating costs of the project, as determined by the Secretary; or (B) 70 percent of the net operating costs of a project to provide same-day paratransit service in compliance with the minimum standards established by the Administrator; or (C) 80 percent of the net operating costs of a project to provide same-day paratransit service in compliance with the minimum standards established by the Administrator and using vehicles operated exclusively by personnel employed by the recipient for same-day paratransit service. .\n##### (c) Formula grants for rural areas\nSection 5311(g) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)(A), by inserting , except that a grant for a capital project directly related to the provision of same-day paratransit services shall be in an amount equal to 90 percent of the net capital costs of the project, as determined by the Secretary. after Secretary ; and\n**(2)**\nby amending paragraph (2), to read as follows:\n(2) Operating assistance (A) A grant made under this section for operating assistance may not exceed an amount equal to\u2014 (i) 50 percent of the net operating costs of the project, as determined by the Secretary; (ii) 70 percent of the net operating costs of a project to provide same-day paratransit service in compliance with the minimum standards established by the Administrator; or (iii) 80 percent of the net operating costs of a project to provide same-day paratransit service in compliance with the minimum standards established by the administrator, as determined by the secretary and using vehicles operated exclusively by personnel employed by the recipient for same-day paratransit service. (B) Exception A State described in section 120(b) of title 23 shall receive a Government share of the net operating costs equal to 62.5 percent of the Government share provided for under paragraph (1)(B). .\n#### 4. Paratransit software and technology minimum standards\n##### (a) In general\nSection 5310 of title 49, United States Code, is amended by adding at the end\u2014\n(j) Paratransit software minimum standards (1) In general No later than 1 year after enactment of this Act, the Administrator shall issue minimum standards for Americans with Disabilities (ADA) paratransit software and technologies procured pursuant to this section. (2) Standards The Administrator shall consider the following in developing the guidance described in the subsection (a): (A) Accessibility of applications including compliance with Web Content Accessibility Guidelines 2.1 (WCAG 2.1) or any subsequent version of such Guidelines. (B) Cybersecurity of applications including compliance with System and Organization Controls 2 (SOC 2) and ISO 27001, and any successor standard. (C) Data storage on cloud infrastructure located in the United States. (D) Integration of multiple service providers\u2014including but not limited to paratransit operated by a transit agency or contractor, taxis, and transportation networking companies (TNC)\u2014through API or related mechanisms, and the ability to move trips between service providers. (E) Real-time route optimization and dynamic trip scheduling, with the ability to utilize some of the extra capacity on ADA paratransit fleet to provide same-day paratransit service. (F) Ability to book on digital booking interfaces that can integrate all service providers. (G) Data sharing and agency portal systems, including an open API to enable integration to third party systems while protecting personally identifiable information of riders and capable, if approved by the recipient, of providing the recipient with the ability to share data with their metropolitan planning organization, State, and local government access to anonymized data for transportation planning, real time operations data, and rules. (H) Safeguards necessary to ensure that all data generated by the provision of service or paid for by the recipient is owned by the recipient and cannot be withheld or limited, nor may the provider condition access to such data, in any manner. (I) Such other considerations as the Administrator determines necessary to advance the needs of riders, transit agencies and providers, and that ensure that investments are future-proofed to accommodate emerging technological and operational developments. (3) Stakeholder consultation In developing the minimum standards described in paragraph (1), the Administrator shall consult with relevant stakeholders including\u2014 (A) transit agencies and transit industry associations; (B) paratransit riders with disabilities; (C) organizations representing riders with disabilities; (D) United States Access Board; (E) labor organizations representing frontline public transportation workers; (F) transit technology providers; (G) for-hire transportation providers; and (H) cybersecurity experts. (4) Limitation Beginning not later than 1 year after final minimum standards are published by the Administrator, no funds awarded under section 5307 or 5310 shall be used to acquire or utilize third-party software for the provision of paratransit services that does not meet the minimum standards established under paragraph (1). (5) Final standards Beginning not later than 2 years after final minimum standards are published by the Administrator, no funds awarded under section 5311 shall be used to acquire or utilize third-party software for the provision of paratransit services that does not meet the minimum standards established under paragraph (1). .",
      "versionDate": "2026-03-26",
      "versionType": "Introduced in House"
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-04-21T17:54:47Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8128ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Same-Day Paratransit Innovation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T08:23:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Same-Day Paratransit Innovation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T08:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To foster greater deployment of same-day paratransit services for individuals with disabilities and to establish minimum standards for paratransit technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T08:18:47Z"
    }
  ]
}
```
