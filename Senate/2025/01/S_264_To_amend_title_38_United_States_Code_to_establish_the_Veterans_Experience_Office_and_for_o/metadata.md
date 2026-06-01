# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/264?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/264
- Title: Improving Veterans’ Experience Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 264
- Origin chamber: Senate
- Introduced date: 2025-01-28
- Update date: 2026-04-10T17:00:47Z
- Update date including text: 2026-04-10T17:00:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in Senate
- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-01-28: Introduced in Senate

## Actions

- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/264",
    "number": "264",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "Improving Veterans\u2019 Experience Act of 2025",
    "type": "S",
    "updateDate": "2026-04-10T17:00:47Z",
    "updateDateIncludingText": "2026-04-10T17:00:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:05:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s264is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 264\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mr. King (for himself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish the Veterans Experience Office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Veterans\u2019 Experience Act of 2025 .\n#### 2. Establishment of Veterans Experience Office\n##### (a) Establishment\n**(1) In general**\nChapter 3 of title 38, United States Code, is amended by adding at the end the following new section:\n325. Veterans Experience Office (a) Establishment There is established in the Department within the Office of the Secretary an office to be known as the Veterans Experience Office (in this section referred to as the Office ). (b) Head of Office (1) The head of the Office shall be the Chief Veterans Experience Officer. (2) The Chief Veterans Experience Officer shall\u2014 (A) be appointed by the Secretary from among individuals the Secretary considers qualified to perform the duties of the position; (B) report directly to the Secretary; and (C) be responsible for carrying out the functions of the Office set forth under subsection (c). (c) Function The functions of the Office are as follows: (1) Carrying out the key customer experience initiatives of the Department relating to veterans' and other beneficiaries' satisfaction with and usage of benefits and services furnished under laws administered by the Secretary for which they are eligible, including setting the strategy, framework, policy, and other guidance for the Department relating to customer experience, including ensuring the activities of the Office and those of other organizations and offices within the Department are coordinated and not duplicative. (2) Requiring the heads of other organizations and offices within the Department to report regularly on customer experience metrics, action plans, and other customer experience improvement efforts to the Chief Veterans Experience Officer. (3) Collecting veteran-derived data\u2014 (A) to determine veteran and beneficiary satisfaction with and usage of the benefits and services furnished under laws administered by the Secretary for which they are eligible; and (B) to be considered during policymaking. (4) Providing strategic guidance and strategies to Department entities for engaging with veterans and beneficiaries regarding benefits and services furnished under laws administered by the Secretary, including those not using such benefits and services. (5) Assessing and advising the Secretary on the accuracy and helpfulness of the websites and other customer-facing information of the Department, be it available electronically or in any other format. (6) Assessing and advising the Secretary on the status and opportunities for improvement of the customer service efforts of the Department. (d) Reports (1) Each year, the Chief Veterans Experience Officer shall submit to the Secretary a summary of the data received by the Chief Veterans Experience Officer under subsection (c)(2). (2) Each year, not later than 180 days after the date on which the Secretary receives the summary under paragraph (1), the Secretary shall submit to Congress an annual summary and analysis of the matters summarized pursuant to such paragraph. (3) Each annual summary submitted pursuant to paragraph (2) shall include the following: (A) Data regarding customer service and experience feedback, disaggregated by benefit or service furnished under laws administered by the Secretary, and relevant demographic data of the veterans and beneficiaries providing the feedback. (B) Data regarding veteran and beneficiary satisfaction with and usage of benefits or services, disaggregated by benefit or service furnished under laws administered by the Secretary, and relevant demographic data of the veterans and beneficiaries providing the feedback, including\u2014 (i) potential reasons for not using the benefits or services, such as\u2014 (I) eligibility; (II) lack of knowledge or awareness of existence of benefit or service; (III) barriers of technology, information, or time; and (IV) other related reasons; and (ii) an analysis of how such reasons may be addressed. (e) Staff and resources (1) The Secretary shall ensure that\u2014 (A) the Office has such staff, resources, and access to customer service and experience information as may be necessary to carry out the functions of the Office; and (B) any information provided to the Office does not include personally identifiable information of an individual veteran, survivor, dependent, or other beneficiary unless such individual provides appropriate consent to allow such information to be shared with the Office. (2) Funds available for basic pay and other administrative expenses of other Department organizations and offices may be available to reimburse the Office for all services provided at rates which will recover actual costs for services provided to such organizations if the Secretary determines that contributing to such costs will not undermine the ability of any such organization or office to provide services required by such office. (3) Nothing in this subsection shall be construed to authorize an increase in the number of full-time employees otherwise authorized for the Department. (f) Privacy Nothing in this section shall be construed to authorize the Chief Veterans Experience Officer to disclose any record in contravention of section 552a of title 5 (commonly referred to as the Privacy Act of 1974 ). (g) Sunset The requirements and authorities of this section shall terminate on September 30, 2028. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 3 of such title is amended by adding at the end the following new item:\n325. Veterans Experience Office. .\n##### (b) Comptroller General of the United States review of Veterans Experience Office and customer service improvement efforts\nNot later than 540 days after the date of the enactment of this Act, the Comptroller General of the United States shall\u2014\n**(1)**\ncomplete an analysis of the methodology, effectiveness, and implementation of findings and feedback of veterans and beneficiaries used by the Department of Veterans Affairs, including the Veterans Experience Office, to improve veteran and beneficiary customer experience and satisfaction, including through the use of what are known as trust-scores , Veteran Signals also known as VSignals , and related survey and data collection activities, processes, and initiatives; and\n**(2)**\nsubmit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans' Affairs of the House of Representatives a report setting forth the findings of the Comptroller General with respect to the analysis completed pursuant to paragraph (1).",
      "versionDate": "2025-01-28",
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
        "actionDate": "2025-08-14",
        "text": "Became Public Law No: 119-33."
      },
      "number": "423",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PRO Veterans Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-19",
        "text": "Referred to the Subcommittee on Oversight and Investigations."
      },
      "number": "3578",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Improving Veterans\u2019 Experience Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-01T15:17:10Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-10T17:00:47Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-04-01T15:16:53Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-04-01T15:16:47Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-01T15:17:04Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-01T15:17:15Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-04-01T15:16:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-05T21:12:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s264",
          "measure-number": "264",
          "measure-type": "s",
          "orig-publish-date": "2025-01-28",
          "originChamber": "SENATE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s264v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Improving Veterans\u2019 Experience Act of 2025</strong></p><p>This bill establishes the Veterans Experience Office within the Department of Veterans Affairs (VA) to carry out the key customer experience initiatives of the VA relating to veterans\u2019 and beneficiaries\u2019 satisfaction with and usage of VA benefits and services.</p><p>Additionally, the office must</p><ul><li>require the heads of other organizations and offices within the VA to report regularly on customer experience metrics, action plans, and other customer experience improvement efforts;</li><li>collect veteran-derived data to determine satisfaction and for use in policymaking;</li><li>provide strategic guidance and strategies to VA entities for engaging with veterans and beneficiaries;</li><li>assess and advise the VA on the accuracy and helpfulness of websites and customer-facing information of the VA; and</li><li>assess and advise the VA on the status and opportunities for improvement of the customer service efforts of the VA.</li></ul><p>The requirements of this bill terminate on September 30, 2028.</p><p>The Government Accountability Office must analyze and report on the methodology, effectiveness, and implementation of the VA\u2019s approach to improving veteran and beneficiary customer experience and satisfaction.</p>"
        },
        "title": "Improving Veterans\u2019 Experience Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s264.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Improving Veterans\u2019 Experience Act of 2025</strong></p><p>This bill establishes the Veterans Experience Office within the Department of Veterans Affairs (VA) to carry out the key customer experience initiatives of the VA relating to veterans\u2019 and beneficiaries\u2019 satisfaction with and usage of VA benefits and services.</p><p>Additionally, the office must</p><ul><li>require the heads of other organizations and offices within the VA to report regularly on customer experience metrics, action plans, and other customer experience improvement efforts;</li><li>collect veteran-derived data to determine satisfaction and for use in policymaking;</li><li>provide strategic guidance and strategies to VA entities for engaging with veterans and beneficiaries;</li><li>assess and advise the VA on the accuracy and helpfulness of websites and customer-facing information of the VA; and</li><li>assess and advise the VA on the status and opportunities for improvement of the customer service efforts of the VA.</li></ul><p>The requirements of this bill terminate on September 30, 2028.</p><p>The Government Accountability Office must analyze and report on the methodology, effectiveness, and implementation of the VA\u2019s approach to improving veteran and beneficiary customer experience and satisfaction.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119s264"
    },
    "title": "Improving Veterans\u2019 Experience Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Improving Veterans\u2019 Experience Act of 2025</strong></p><p>This bill establishes the Veterans Experience Office within the Department of Veterans Affairs (VA) to carry out the key customer experience initiatives of the VA relating to veterans\u2019 and beneficiaries\u2019 satisfaction with and usage of VA benefits and services.</p><p>Additionally, the office must</p><ul><li>require the heads of other organizations and offices within the VA to report regularly on customer experience metrics, action plans, and other customer experience improvement efforts;</li><li>collect veteran-derived data to determine satisfaction and for use in policymaking;</li><li>provide strategic guidance and strategies to VA entities for engaging with veterans and beneficiaries;</li><li>assess and advise the VA on the accuracy and helpfulness of websites and customer-facing information of the VA; and</li><li>assess and advise the VA on the status and opportunities for improvement of the customer service efforts of the VA.</li></ul><p>The requirements of this bill terminate on September 30, 2028.</p><p>The Government Accountability Office must analyze and report on the methodology, effectiveness, and implementation of the VA\u2019s approach to improving veteran and beneficiary customer experience and satisfaction.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119s264"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s264is.xml"
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
      "title": "Improving Veterans\u2019 Experience Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Veterans\u2019 Experience Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to establish the Veterans Experience Office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T03:48:26Z"
    }
  ]
}
```
