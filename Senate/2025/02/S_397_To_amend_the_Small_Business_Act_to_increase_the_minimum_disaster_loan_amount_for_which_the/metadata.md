# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/397?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/397
- Title: Small Business Disaster Damage Fairness Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 397
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2026-02-25T17:01:21Z
- Update date including text: 2026-02-25T17:01:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/397",
    "number": "397",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Small Business Disaster Damage Fairness Act of 2025",
    "type": "S",
    "updateDate": "2026-02-25T17:01:21Z",
    "updateDateIncludingText": "2026-02-25T17:01:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T21:54:53Z",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s397is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 397\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Kennedy (for himself, Mr. Booker , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo amend the Small Business Act to increase the minimum disaster loan amount for which the Small Business Administration may require collateral, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Disaster Damage Fairness Act of 2025 .\n#### 2. Collateral requirements for disaster loans\nSection 7(d)(6) of the Small Business Act ( 15 U.S.C. 636(d)(6) ) is amended, in the second sentence, in the third proviso\u2014\n**(1)**\nby striking $14,000 and inserting $50,000 ; and\n**(2)**\nby striking major disaster and inserting disaster .\n#### 3. GAO report on default rates\nNot later than 3 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business of the House of Representatives a report on the performance, including the default rate, of loans made under section 7(b)(1) of the Small Business Act ( 15 U.S.C. 636(b)(1) ), and the impact of the amendments to collateral amounts made under section 2 of this Act on the performance of those loans, during the period\u2014\n**(1)**\nbeginning on September 30, 2020; and\n**(2)**\nending on the date on that is 2 years after the date of enactment of this Act.\n#### 4. Distinguishing between rural and urban communities in marketing and outreach\n##### (a) Definitions\nIn this section:\n**(1) Administration**\nThe term Administration means the Small Business Administration.\n**(2) Administrator**\nThe term Administrator means the Administrator of the Administration.\n**(3) Associate Administrator**\nThe term Associate Administrator means the Associate Administrator of the Office of Disaster Recovery and Resilience of the Administration.\n**(4) Covered program**\nThe term covered program means the disaster loan program authorized by section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ).\n##### (b) Requirement\nBeginning on the date of enactment of this Act, consistent with the recommendations of the Government Accountability Office in the report entitled Small Business Administration: Targeted Outreach about Disaster Assistance Could Benefit Rural Communities (GAO\u201324\u2013106755) (February 22, 2024), the Administrator shall ensure that the Associate Administrator\u2014\n**(1)**\ndistinguishes between rural and urban communities in the outreach and marketing plan of the Administration with respect to the covered program; and\n**(2)**\nincorporates actions to mitigate challenges encountered by rural communities in accessing loans under the covered program.",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-02-05",
        "text": "Referred to the House Committee on Small Business."
      },
      "number": "1021",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Small Business Disaster Damage Fairness Act of 2025",
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
        "name": "Commerce",
        "updateDate": "2025-03-10T14:09:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119s397",
          "measure-number": "397",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2026-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s397v00",
            "update-date": "2026-02-25"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Small Business Disaster Damage Fairness Act of 2025</strong></p><p>This bill increases from $14,000 to $50,000 the threshold loan amount over which the Small Business Administration\u00a0(SBA) may require collateral for a disaster loan.</p><p>The Government Accountability Office must report on the performance, including the default rate, of such loans.</p><p>Additionally, the SBA must (1) distinguish between rural and urban communities in the outreach and marketing for disaster loans, and (2)\u00a0incorporate actions to mitigate challenges encountered by rural communities in accessing such loans.</p>"
        },
        "title": "Small Business Disaster Damage Fairness Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s397.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Small Business Disaster Damage Fairness Act of 2025</strong></p><p>This bill increases from $14,000 to $50,000 the threshold loan amount over which the Small Business Administration\u00a0(SBA) may require collateral for a disaster loan.</p><p>The Government Accountability Office must report on the performance, including the default rate, of such loans.</p><p>Additionally, the SBA must (1) distinguish between rural and urban communities in the outreach and marketing for disaster loans, and (2)\u00a0incorporate actions to mitigate challenges encountered by rural communities in accessing such loans.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s397"
    },
    "title": "Small Business Disaster Damage Fairness Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Small Business Disaster Damage Fairness Act of 2025</strong></p><p>This bill increases from $14,000 to $50,000 the threshold loan amount over which the Small Business Administration\u00a0(SBA) may require collateral for a disaster loan.</p><p>The Government Accountability Office must report on the performance, including the default rate, of such loans.</p><p>Additionally, the SBA must (1) distinguish between rural and urban communities in the outreach and marketing for disaster loans, and (2)\u00a0incorporate actions to mitigate challenges encountered by rural communities in accessing such loans.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s397"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s397is.xml"
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
      "title": "Small Business Disaster Damage Fairness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T02:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Small Business Disaster Damage Fairness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Act to increase the minimum disaster loan amount for which the Small Business Administration may require collateral, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T02:48:24Z"
    }
  ]
}
```
