# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3064?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3064
- Title: Relief of Chronic Pain Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3064
- Origin chamber: Senate
- Introduced date: 2025-10-28
- Update date: 2026-05-19T11:03:44Z
- Update date including text: 2026-05-19T11:03:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-28: Introduced in Senate
- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-10-28: Introduced in Senate

## Actions

- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3064",
    "number": "3064",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Relief of Chronic Pain Act of 2025",
    "type": "S",
    "updateDate": "2026-05-19T11:03:44Z",
    "updateDateIncludingText": "2026-05-19T11:03:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-28",
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
        "item": [
          {
            "date": "2025-10-28T20:10:43Z",
            "name": "Referred To"
          },
          {
            "date": "2025-10-28T20:10:43Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "WA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "NC"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MT"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3064is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3064\nIN THE SENATE OF THE UNITED STATES\nOctober 28, 2025 Mr. Daines (for himself and Ms. Cantwell ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to ensure appropriate access to non-opioid pain management drugs for chronic pain conditions under part D of the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Relief of Chronic Pain Act of 2025 .\n#### 2. Appropriate cost-sharing for qualifying non-opioid chronic pain management drugs under Medicare part D\n##### (a) Medicare part D\nSection 1860D\u20132 of the Social Security Act ( 42 U.S.C. 1395w\u2013102 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)(A), in the matter preceding clause (i), by striking and (9) and inserting (9), and (10) ;\n**(B)**\nin paragraph (2)(A), in the matter preceding clause (i), by striking and (9) and inserting (9), and (10) ; and\n**(C)**\nby adding at the end the following new paragraph:\n(10) Treatment of cost-sharing for qualifying non-opioid chronic pain management drugs (A) In general For plan years beginning on or after January 1, 2026, with respect to a covered part D drug that is a qualifying non-opioid chronic pain management drug (as defined in subparagraph (B))\u2014 (i) the deductible under paragraph (1) shall not apply; and (ii) such drug shall be placed on the lowest cost-sharing tier, if any, for purposes of determining the maximum co-insurance or other cost-sharing for such drug. (B) Qualifying non-opioid chronic pain management drugs In this paragraph, the term qualifying non-opioid chronic pain management drug means a non-opioid drug or biological product\u2014 (i) that has a label indication approved by the Food and Drug Administration to treat chronic pain or a chronic pain condition (as defined in subparagraph (C)); (ii) that does not act upon the body\u2019s opioid receptors; (iii) for which there is no other drug or product that is\u2014 (I) rated as therapeutically equivalent (under the Food and Drug Administration\u2019s most recent publication of Approved Drug Products with Therapeutic Equivalence Evaluations ); and (II) sold or marketed in the United States; and (iv) for which the wholesale acquisition cost (as defined in section 1847A(c)(6)(B)), for a monthly supply does not exceed the monthly specialty-tier cost threshold, as determined by the Secretary. (C) Chronic pain condition In this paragraph, the term chronic pain condition means the following conditions, each characterized by pain persisting for a period of greater than 3 months: (i) Diabetic peripheral neuropathic pain. (ii) Endometriosis. (iii) Fibromyalgia. (iv) Musculoskeletal pain. (v) Neuropathic pain. (vi) Post-herpetic neuralgia. (vii) Trigeminal neuralgia. ; and\n**(2)**\nin subsection (c), by adding at the end the following new paragraph:\n(7) Treatment of cost-sharing for qualifying non-opioid chronic pain management drugs The coverage is provided in accordance with subsection (b)(10). .\n##### (b) Conforming amendments to cost-Sharing for low-Income individuals\nSection 1860D\u201314(a) of the Social Security Act ( 42 U.S.C. 1395w\u2013114(a) ) is amended\u2014\n**(1)**\nin paragraph (1)(D), in each of the clauses (ii) and (iii), by striking Subject to paragraph (6) and inserting Subject to paragraphs (6) and (7) ; and\n**(2)**\nby adding at the end the following new paragraph:\n(7) Treatment of cost-sharing or deductible for qualifying non-opioid pain management drugs For plan years beginning on or after January 1, 2026, with respect to a covered part D drug that is a qualifying non-opioid chronic pain management drug (as defined in section 1860D\u20132(b)(10)(B))\u2014 (A) the deductible under section 1860D\u20132(b)(1) shall not apply; and (B) such drug shall be placed on the lowest cost-sharing tier, if any, for purposes of determining the maximum co-insurance or other cost-sharing for such drug. .\n#### 3. Prohibition on the use of step therapy and prior authorization for qualifying non-opioid chronic pain management drugs under Medicare part D\nSection 1860D\u20134(c) of the Social Security Act ( 42 U.S.C. 1395w\u2013104 ) is amended\u2014\n**(1)**\nby redesignating paragraph (6), as added by section 50354 of division E of the Bipartisan Budget Act of 2018 ( Public Law 115\u2013123 ), as paragraph (7); and\n**(2)**\nby adding at the end the following new paragraph:\n(8) Prohibition on use of step therapy and prior authorization for qualifying non-opioid chronic pain management drugs (A) In general For plan years beginning on or after January 1, 2026, a prescription drug plan or an MA\u2013PD plan may not, with respect to a qualifying non-opioid chronic pain management drug (as defined in section 1860D\u20132(b)(10)(B)) for which coverage is provided under such plan, impose any\u2014 (i) step therapy requirement under which an individual enrolled under such plan is required to use an opioid prior to receiving such drug; or (ii) prior authorization requirement. (B) Step therapy In this paragraph, the term step therapy means a drug therapy utilization management protocol or program that requires use of an alternative, preferred prescription drug or drugs before the plan approves coverage for the non-preferred drug therapy prescribed. (C) Prior authorization In this paragraph, the term prior authorization means any requirement to obtain approval from a plan prior to the furnishing of a drug. .",
      "versionDate": "2025-10-28",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-11-25T20:26:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-28",
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
          "measure-id": "id119s3064",
          "measure-number": "3064",
          "measure-type": "s",
          "orig-publish-date": "2025-10-28",
          "originChamber": "SENATE",
          "update-date": "2026-01-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3064v00",
            "update-date": "2026-01-15"
          },
          "action-date": "2025-10-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Relief of Chronic Pain Act of 2025</strong></p><p>This bill reduces\u00a0cost-sharing and prohibits the imposition of certain utilization requirements under the Medicare prescription drug benefit for certain non-opioid drugs for chronic pain management.</p><p>Specifically, the bill requires such drugs to be covered without a deductible and to be placed on the lowest cost-sharing tier (if any). The bill also prohibits the imposition of prior authorization requirements (i.e., requiring prior approval from a plan) or step therapy requirements (i.e., requiring the use of alternative drugs before a drug is covered under a plan) with respect to such drugs.</p>"
        },
        "title": "Relief of Chronic Pain Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3064.xml",
    "summary": {
      "actionDate": "2025-10-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Relief of Chronic Pain Act of 2025</strong></p><p>This bill reduces\u00a0cost-sharing and prohibits the imposition of certain utilization requirements under the Medicare prescription drug benefit for certain non-opioid drugs for chronic pain management.</p><p>Specifically, the bill requires such drugs to be covered without a deductible and to be placed on the lowest cost-sharing tier (if any). The bill also prohibits the imposition of prior authorization requirements (i.e., requiring prior approval from a plan) or step therapy requirements (i.e., requiring the use of alternative drugs before a drug is covered under a plan) with respect to such drugs.</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119s3064"
    },
    "title": "Relief of Chronic Pain Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Relief of Chronic Pain Act of 2025</strong></p><p>This bill reduces\u00a0cost-sharing and prohibits the imposition of certain utilization requirements under the Medicare prescription drug benefit for certain non-opioid drugs for chronic pain management.</p><p>Specifically, the bill requires such drugs to be covered without a deductible and to be placed on the lowest cost-sharing tier (if any). The bill also prohibits the imposition of prior authorization requirements (i.e., requiring prior approval from a plan) or step therapy requirements (i.e., requiring the use of alternative drugs before a drug is covered under a plan) with respect to such drugs.</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119s3064"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3064is.xml"
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
      "title": "Relief of Chronic Pain Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T11:03:44Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Relief of Chronic Pain Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to ensure appropriate access to non-opioid pain management drugs for chronic pain conditions under part D of the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T06:18:18Z"
    }
  ]
}
```
