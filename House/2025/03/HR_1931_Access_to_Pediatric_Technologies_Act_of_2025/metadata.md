# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1931?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1931
- Title: Access to Pediatric Technologies Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1931
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2026-02-13T21:04:43Z
- Update date including text: 2026-02-13T21:04:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1931",
    "number": "1931",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000302",
        "district": "13",
        "firstName": "John",
        "fullName": "Rep. Joyce, John [R-PA-13]",
        "lastName": "Joyce",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Access to Pediatric Technologies Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-13T21:04:43Z",
    "updateDateIncludingText": "2026-02-13T21:04:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:10:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-06T14:10:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "MD"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "NC"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "TN"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "MA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "MN"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "MA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "WA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "TN"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "TN"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "IA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1931ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1931\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Joyce of Pennsylvania (for himself and Mrs. Trahan ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to facilitate patient access to certain pediatric technologies.\n#### 1. Short title\nThis Act may be cited as the Access to Pediatric Technologies Act of 2025 .\n#### 2. Facilitating access to pediatric technologies\n##### (a) In general\nSection 1848 of the Social Security Act ( 42 U.S.C. 1395w\u20134 ) is amended by adding at the end the following new subsection:\n(u) Facilitating access to pediatric technologies (1) In general For each qualifying pediatric technology (as defined in paragraph (4)) furnished on or after January 1, 2026, the Secretary shall, upon receipt of a manufacturer request under paragraph (3), establish national relative value units under the physician fee schedule established under this section, to the extent no such national relative value units have been established for such qualifying pediatric technology under such fee schedule. (2) Payment methodology The Secretary shall establish national relative value units for a qualifying pediatric technology under this subsection\u2014 (A) in accordance with the payment methodology established under this section and applicable regulations; and (B) using available data related to the qualifying pediatric technology, which may include applicable contractor pricing information, claims data, time and motion studies, invoice information, or other information used by the Secretary in establishing payment rates. (3) Implementation (A) In general Upon written request to the Secretary from the manufacturer of a qualifying pediatric technology, the Secretary shall establish national relative value units under paragraph (1) through the annual rulemaking process for the physician fee schedule established under this section, in accordance with the timeline described in subparagraph (B). (B) Timeline (i) In the case where the Secretary receives a request under this paragraph on or before May 1 of a given year from a manufacturer with respect to a qualifying pediatric technology of the manufacturer, the Secretary shall establish national relative value units for the qualifying pediatric technology in the rulemaking process during that year for the physician fee schedule established under this section. (ii) In the case where the Secretary receives a request under this paragraph after May 1 of a given year from a manufacturer with respect to a qualifying pediatric technology of the manufacturer, the Secretary shall establish national relative value units for the qualifying pediatric technology in the rulemaking process during the following year for the physician fee schedule established under this section. (C) Content of manufacturer requests A manufacturer submitting a request under paragraph with respect to a qualifying pediatric technology of the manufacturer shall include in such request information to verify that the technology is a qualifying pediatric technology and to allow the Secretary to establish national relative value units for such technology, including (to the extent available) contractor pricing information, claims data, time and motion studies, invoice information, or other relevant information. (4) Qualifying pediatric technology defined In this subsection, the term qualifying pediatric technology means a medical device that is\u2014 (A) covered under this title; (B) approved, cleared, or authorized under section 510(k), 513(f)(2), or 515 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360(k) , 360c(f)(2), 360e); (C) described by a temporary Level I HCPCS Code intended for emerging technologies, services, or procedures; and (D) (i) used as part of a procedure predominantly performed on pediatric patients; or (ii) has otherwise been specifically designed for safe and effective use in pediatric populations. (5) Rule of construction Nothing in this subsection shall be construed to require coverage of a qualifying pediatric technology under this title or alter the requirements of section 1862(a)(1)(A). .",
      "versionDate": "2025-03-06",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-01-24",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "249",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Access to Pediatric Technologies Act of 2025",
      "type": "S"
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
        "updateDate": "2025-03-25T13:15:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
    "originChamber": "House",
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
          "measure-id": "id119hr1931",
          "measure-number": "1931",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2026-02-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1931v00",
            "update-date": "2026-02-13"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Access to Pediatric Technologies Act of 2025</strong></p><p>This bill requires the Centers for Medicare & Medicaid Services (CMS) to establish, upon request, specific payment methodologies for qualifying pediatric technologies under the Medicare physician fee schedule.\u00a0<em>Qualifying pediatric technologies</em> are medical devices that are (1) covered under Medicare, (2) approved by the Food and Drug Administration, (3) currently billed using a specified temporary billing code for emerging technologies, and (4) predominantly used or specifically designated for pediatric patients.</p><p>The CMS must develop a payment methodology for a qualifying pediatric technology upon request from the manufacturer and based on available data, including pricing information and claims data. Manufacturers must include relevant information in their requests to enable the CMS to develop the corresponding methodologies.</p>"
        },
        "title": "Access to Pediatric Technologies Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1931.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Access to Pediatric Technologies Act of 2025</strong></p><p>This bill requires the Centers for Medicare & Medicaid Services (CMS) to establish, upon request, specific payment methodologies for qualifying pediatric technologies under the Medicare physician fee schedule.\u00a0<em>Qualifying pediatric technologies</em> are medical devices that are (1) covered under Medicare, (2) approved by the Food and Drug Administration, (3) currently billed using a specified temporary billing code for emerging technologies, and (4) predominantly used or specifically designated for pediatric patients.</p><p>The CMS must develop a payment methodology for a qualifying pediatric technology upon request from the manufacturer and based on available data, including pricing information and claims data. Manufacturers must include relevant information in their requests to enable the CMS to develop the corresponding methodologies.</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr1931"
    },
    "title": "Access to Pediatric Technologies Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Access to Pediatric Technologies Act of 2025</strong></p><p>This bill requires the Centers for Medicare & Medicaid Services (CMS) to establish, upon request, specific payment methodologies for qualifying pediatric technologies under the Medicare physician fee schedule.\u00a0<em>Qualifying pediatric technologies</em> are medical devices that are (1) covered under Medicare, (2) approved by the Food and Drug Administration, (3) currently billed using a specified temporary billing code for emerging technologies, and (4) predominantly used or specifically designated for pediatric patients.</p><p>The CMS must develop a payment methodology for a qualifying pediatric technology upon request from the manufacturer and based on available data, including pricing information and claims data. Manufacturers must include relevant information in their requests to enable the CMS to develop the corresponding methodologies.</p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr1931"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1931ih.xml"
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
      "title": "Access to Pediatric Technologies Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Access to Pediatric Technologies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to facilitate patient access to certain pediatric technologies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:18:22Z"
    }
  ]
}
```
