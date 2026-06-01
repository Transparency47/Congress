# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2770?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2770
- Title: Share the Savings with Seniors Act
- Congress: 119
- Bill type: S
- Bill number: 2770
- Origin chamber: Senate
- Introduced date: 2025-09-11
- Update date: 2025-12-02T16:56:21Z
- Update date including text: 2025-12-02T16:56:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-11: Introduced in Senate
- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-11: Introduced in Senate

## Actions

- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2770",
    "number": "2770",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Share the Savings with Seniors Act",
    "type": "S",
    "updateDate": "2025-12-02T16:56:21Z",
    "updateDateIncludingText": "2025-12-02T16:56:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T16:08:47Z",
          "name": "Referred To"
        }
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NV"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "NC"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2770is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2770\nIN THE SENATE OF THE UNITED STATES\nSeptember 11, 2025 Mr. Cornyn (for himself, Ms. Rosen , Mr. Tillis , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to ensure appropriate cost-sharing for chronic care drugs under Medicare part D.\n#### 1. Short title\nThis Act may be cited as the Share the Savings with Seniors Act .\n#### 2. Appropriate cost-sharing for chronic care drugs under Medicare part D\n##### (a) In general\nSection 1860D\u20132 of the Social Security Act ( 42 U.S.C. 1395w\u2013102 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)(A), in the matter preceding clause (i), by striking and (9) and inserting , (9), and (10) ;\n**(B)**\nin paragraph (2)(A), in the matter preceding clause (i), by striking and (9) and inserting , (9), and (10) ; and\n**(C)**\nby adding at the end the following new paragraph:\n(10) Cost-sharing for chronic care drugs (A) In general For plan years beginning on or after January 1, 2027, in the case of a chronic care drug, the following shall apply: (i) For costs below the annual deductible specified in paragraph (1), cost-sharing for such drug shall not exceed the net price of such drug. (ii) Subject to subparagraph (B), for costs above the annual deductible specified in paragraph (1) and below the out-of-pocket threshold specified in paragraph (4), any coinsurance amount for such drug shall be based on a percentage of the net price of such drug. (B) Exception The requirement under subparagraph (A)(ii) shall not apply to a chronic care drug under a prescription drug plan if the cost-sharing amount for such drug under such plan is based on a copayment that is not tied to a percentage of a drug price (such as the negotiated price, list price, or wholesale acquisition cost), a drug benchmark price (such as the average wholesale price), or a drug cost. (C) Definitions In this paragraph: (i) Chronic care drug The term chronic care drug means a covered part D drug that is included under any of the following United States Pharmacopeia Convention (USP) categories and classes of drugs, as included in the most recent version of the USP Medicare Model Guidelines: (I) Blood glucose regulators, other than insulins. (II) Anti-inflammatories, inhaled corticosteroids. (III) Bronchodilators, anticholinergic. (IV) Bronchodilators, sympathomimetic. (V) Respiratory tract agents, other. (VI) Anticoagulants. (VII) Cardiovascular agents, other. (VIII) Any category or class identified by the Secretary or USP as a successor to the categories and classes described in subclauses (I) through (VII) based on the most recent USP Medicare Model Guidelines at the time of such identification. (ii) Net price The term net price means the negotiated price of the drug net of all price concessions originating from manufacturers that are received or expected to be received by the plan or pharmacy benefit manager on behalf of the plan for such product and that are not already reflected in the negotiated price. ; and\n**(2)**\nin subsection (c), by adding at the end the following new paragraph:\n(7) Cost-sharing for covered chronic care drugs The coverage is provided in accordance with subsection (b)(10). .\n##### (b) Conforming amendments to cost-Sharing for low-Income individuals\nSection 1860D\u201314(a)(1)(D)(iii) of the Social Security Act ( 42 U.S.C. 1395w\u2013114(a)(1)(D)(iii) ) is amended by adding at the end the following new sentence: For plan year 2027 and subsequent plan years, the copayment amount applicable under the first sentence of this subclause for a chronic drug (as defined in section 1860D\u20132(b)(10)(B)) furnished to the individual may not exceed the applicable cost-sharing for such drug under the prescription drug plan or MA\u2013PD plan in which the individual is enrolled. .\n##### (c) Regulations\nNotwithstanding any other provision of law, the Secretary of Health and Human Services shall initially implement the amendments made by this section through interim final regulations.",
      "versionDate": "2025-09-11",
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
        "updateDate": "2025-09-23T17:00:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-11",
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
          "measure-id": "id119s2770",
          "measure-number": "2770",
          "measure-type": "s",
          "orig-publish-date": "2025-09-11",
          "originChamber": "SENATE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2770v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-09-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Share the Savings with Seniors Act</strong></p><p>This bill limits cost-sharing for chronic care drugs under the Medicare prescription drug benefit. <em>Chronic care drugs</em> include blood glucose regulators other than insulin, anticoagulants, and other categories of drugs as specified in the bill.</p><p>Specifically, for costs below the annual deductible, the bill caps cost-sharing for chronic care drugs at the net price of the drug (i.e., the negotiated price net of all manufacturer price concessions); for costs above the annual deductible and below the annual out-of-pocket threshold, cost-sharing must be based on a percentage of the drug's net price (if cost-sharing for that drug is tied to the price or cost of the drug).</p>"
        },
        "title": "Share the Savings with Seniors Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2770.xml",
    "summary": {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Share the Savings with Seniors Act</strong></p><p>This bill limits cost-sharing for chronic care drugs under the Medicare prescription drug benefit. <em>Chronic care drugs</em> include blood glucose regulators other than insulin, anticoagulants, and other categories of drugs as specified in the bill.</p><p>Specifically, for costs below the annual deductible, the bill caps cost-sharing for chronic care drugs at the net price of the drug (i.e., the negotiated price net of all manufacturer price concessions); for costs above the annual deductible and below the annual out-of-pocket threshold, cost-sharing must be based on a percentage of the drug's net price (if cost-sharing for that drug is tied to the price or cost of the drug).</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2770"
    },
    "title": "Share the Savings with Seniors Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Share the Savings with Seniors Act</strong></p><p>This bill limits cost-sharing for chronic care drugs under the Medicare prescription drug benefit. <em>Chronic care drugs</em> include blood glucose regulators other than insulin, anticoagulants, and other categories of drugs as specified in the bill.</p><p>Specifically, for costs below the annual deductible, the bill caps cost-sharing for chronic care drugs at the net price of the drug (i.e., the negotiated price net of all manufacturer price concessions); for costs above the annual deductible and below the annual out-of-pocket threshold, cost-sharing must be based on a percentage of the drug's net price (if cost-sharing for that drug is tied to the price or cost of the drug).</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2770"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2770is.xml"
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
      "title": "Share the Savings with Seniors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-20T06:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Share the Savings with Seniors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T06:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to ensure appropriate cost-sharing for chronic care drugs under Medicare part D.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-20T06:03:47Z"
    }
  ]
}
```
