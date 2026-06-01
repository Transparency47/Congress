# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4534?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4534
- Title: Microbusiness Support Act
- Congress: 119
- Bill type: S
- Bill number: 4534
- Origin chamber: Senate
- Introduced date: 2026-05-14
- Update date: 2026-05-29T15:33:26Z
- Update date including text: 2026-05-29T15:33:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in Senate
- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2026-05-14: Introduced in Senate

## Actions

- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4534",
    "number": "4534",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Microbusiness Support Act",
    "type": "S",
    "updateDate": "2026-05-29T15:33:26Z",
    "updateDateIncludingText": "2026-05-29T15:33:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T16:52:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4534is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4534\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2026 Ms. Cortez Masto (for herself and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo amend the Small Business Act to establish a direct loan program for microbusinesses at the Small Business Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Microbusiness Support Act .\n#### 2. Direct loan program for microbusinesses\nSection 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ) is amended by adding at the end the following:\n(38) Microbusiness loan program (A) Definition (i) In general In this paragraph, the term microbusiness means an independently owned and operated for-profit business entity that\u2014 (I) employs not more than 10 full-time employees, determined on a full-time equivalent basis; and (II) has annual revenue of not more than the lesser of\u2014 (aa) $5,000,000; or (bb) the size standard in dollars, if any, for the North American Industry Classification System code assigned to the business entity for the business entity to qualify as a small business concern. (ii) Full-time For purposes of clause (i), the term full-time means that an individual\u2014 (I) is employed for consideration for not less than 35 hours each week; or (II) renders any other standard of service generally accepted by custom or specified by contract as full-time employment. (iii) Verification The Administrator may request from a business entity such documentation as may be necessary to establish that the business entity qualifies as a microbusiness under this subparagraph. (B) Authority The Administrator is authorized to originate and disburse direct loans, including through partnerships with third parties, to microbusinesses under this subsection. (C) Maximum amount The maximum amount of a loan made under this paragraph to a microbusiness is $100,000. (D) Fees With respect to each loan made under this paragraph, the Administrator, an authorized third party, or an agent may\u2014 (i) impose, collect, retain, and utilize fees, which may be charged to the borrower, to cover any costs associated with referring applications or originating, making, underwriting, disbursing, closing, servicing, or liquidating the loan, including any direct lending agent costs, other program or contract costs, or other agent administrative expenses; (ii) impose, collect, retain, and utilize fees (including unused fees and draw fees), which may be charged to the borrower on loans for revolving lines of credit; and (iii) pay third parties, including direct lending agents and financial institutions, with which the Administration partners for assistance in referring applicants or promoting, originating, making, underwriting, disbursing, closing, servicing, or liquidating loans in accordance with this paragraph on behalf of the Administration. (E) Terms (i) In general Not later than 90 days after the date of enactment of this paragraph, the Administrator shall issue interim final rules and revise any relevant rules to establish the terms and conditions for a direct loan made under this paragraph, including with respect to repayment, underwriting criteria, interest rate, maturity, and other terms. (ii) Interest rate The interest rate for a loan made under this paragraph shall be in accordance with paragraph (4)(A), except 6 percent per annum shall be substituted for 1 percent per annum . .",
      "versionDate": "2026-05-14",
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
        "name": "Commerce",
        "updateDate": "2026-05-29T15:33:26Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4534is.xml"
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
      "title": "Microbusiness Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T00:53:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Microbusiness Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T00:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Act to establish a direct loan program for microbusinesses at the Small Business Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:43Z"
    }
  ]
}
```
