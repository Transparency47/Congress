# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/249?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/249
- Title: Access to Pediatric Technologies Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 249
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2026-01-22T22:41:14Z
- Update date including text: 2026-01-22T22:41:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-24: Introduced in Senate

## Actions

- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/249",
    "number": "249",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Access to Pediatric Technologies Act of 2025",
    "type": "S",
    "updateDate": "2026-01-22T22:41:14Z",
    "updateDateIncludingText": "2026-01-22T22:41:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-24",
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
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T19:35:27Z",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s249is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 249\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mrs. Blackburn (for herself and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to facilitate patient access to certain pediatric technologies.\n#### 1. Short title\nThis Act may be cited as the Access to Pediatric Technologies Act of 2025 .\n#### 2. Facilitating access to pediatric technologies\n##### (a) In general\nSection 1848 of the Social Security Act ( 42 U.S.C. 1395w\u20134 ) is amended by adding at the end the following new subsection:\n(u) Facilitating access to pediatric technologies (1) In general For each qualifying pediatric technology (as defined in paragraph (4)) furnished on or after January 1, 2026, the Secretary shall, upon receipt of a manufacturer request under paragraph (3), establish national relative value units under the physician fee schedule established under this section, to the extent no such national relative value units have been established for such qualifying pediatric technology under such fee schedule. (2) Payment methodology The Secretary shall establish national relative value units for a qualifying pediatric technology under this subsection\u2014 (A) in accordance with the payment methodology established under this section and applicable regulations; and (B) using available data related to the qualifying pediatric technology, which may include applicable contractor pricing information, claims data, time and motion studies, invoice information, or other information used by the Secretary in establishing payment rates. (3) Implementation (A) In general Upon written request to the Secretary from the manufacturer of a qualifying pediatric technology, the Secretary shall establish national relative value units under paragraph (1) through the annual rulemaking process for the physician fee schedule established under this section, in accordance with the timeline described in subparagraph (B). (B) Timeline (i) In the case where the Secretary receives a request under this paragraph on or before May 1 of a given year from a manufacturer with respect to a qualifying pediatric technology of the manufacturer, the Secretary shall establish national relative value units for the qualifying pediatric technology in the rulemaking process during that year for the physician fee schedule established under this section. (ii) In the case where the Secretary receives a request under this paragraph after May 1 of a given year from a manufacturer with respect to a qualifying pediatric technology of the manufacturer, the Secretary shall establish national relative value units for the qualifying pediatric technology in the rulemaking process during the following year for the physician fee schedule established under this section. (C) Content of manufacturer requests A manufacturer submitting a request under this paragraph with respect to a qualifying pediatric technology of the manufacturer shall include in such request information to verify that the technology is a qualifying pediatric technology and to allow the Secretary to establish national relative value units for such technology, including (to the extent available) contractor pricing information, claims data, time and motion studies, invoice information, or other relevant information. (4) Qualifying pediatric technology defined In this subsection, the term qualifying pediatric technology means a medical device that is\u2014 (A) covered under this title; (B) approved, cleared, or authorized under section 510(k), 513(f)(2), or 515 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360(k) , 360c(f)(2), 360e); (C) described by a temporary Level I HCPCS Code intended for emerging technologies, services, or procedures; and (D) (i) used as part of a procedure predominantly performed on pediatric patients; or (ii) has otherwise been specifically designed for safe and effective use in pediatric populations. (5) Rule of construction Nothing in this subsection shall be construed to require coverage of a qualifying pediatric technology under this title or alter the requirements of section 1862(a)(1)(A). .",
      "versionDate": "2025-01-24",
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
        "actionDate": "2025-03-06",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1931",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Access to Pediatric Technologies Act of 2025",
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
            "name": "Child health",
            "updateDate": "2025-03-27T14:48:48Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-03-27T14:49:02Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-27T14:49:07Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-03-27T14:48:57Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-03-27T14:49:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-24T14:39:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119s249",
          "measure-number": "249",
          "measure-type": "s",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-04-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s249v00",
            "update-date": "2025-04-18"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Access to Pediatric Technologies Act of 2025</strong></p><p>This bill requires the Centers for Medicare & Medicaid Services (CMS) to establish, upon request, specific payment methodologies for qualifying pediatric technologies under the Medicare physician fee schedule.\u00a0<em>Qualifying pediatric technologies</em> are medical devices that are (1) covered under Medicare, (2) approved by the Food and Drug Administration, (3) currently billed using a specified temporary billing code for emerging technologies, and (4) predominantly used or specifically designated for pediatric patients.</p><p>The CMS must develop a payment methodology for a qualifying pediatric technology upon request from the manufacturer and based on available data, including pricing information and claims data. Manufacturers must include relevant information in their requests to enable the CMS to develop the corresponding methodologies.</p>"
        },
        "title": "Access to Pediatric Technologies Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s249.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Access to Pediatric Technologies Act of 2025</strong></p><p>This bill requires the Centers for Medicare & Medicaid Services (CMS) to establish, upon request, specific payment methodologies for qualifying pediatric technologies under the Medicare physician fee schedule.\u00a0<em>Qualifying pediatric technologies</em> are medical devices that are (1) covered under Medicare, (2) approved by the Food and Drug Administration, (3) currently billed using a specified temporary billing code for emerging technologies, and (4) predominantly used or specifically designated for pediatric patients.</p><p>The CMS must develop a payment methodology for a qualifying pediatric technology upon request from the manufacturer and based on available data, including pricing information and claims data. Manufacturers must include relevant information in their requests to enable the CMS to develop the corresponding methodologies.</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119s249"
    },
    "title": "Access to Pediatric Technologies Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Access to Pediatric Technologies Act of 2025</strong></p><p>This bill requires the Centers for Medicare & Medicaid Services (CMS) to establish, upon request, specific payment methodologies for qualifying pediatric technologies under the Medicare physician fee schedule.\u00a0<em>Qualifying pediatric technologies</em> are medical devices that are (1) covered under Medicare, (2) approved by the Food and Drug Administration, (3) currently billed using a specified temporary billing code for emerging technologies, and (4) predominantly used or specifically designated for pediatric patients.</p><p>The CMS must develop a payment methodology for a qualifying pediatric technology upon request from the manufacturer and based on available data, including pricing information and claims data. Manufacturers must include relevant information in their requests to enable the CMS to develop the corresponding methodologies.</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119s249"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s249is.xml"
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
      "title": "Access to Pediatric Technologies Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Access to Pediatric Technologies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to facilitate patient access to certain pediatric technologies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:33:50Z"
    }
  ]
}
```
