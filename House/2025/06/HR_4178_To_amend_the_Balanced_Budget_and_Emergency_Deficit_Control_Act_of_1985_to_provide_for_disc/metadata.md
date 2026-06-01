# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4178?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4178
- Title: Enforce the Caps Act
- Congress: 119
- Bill type: HR
- Bill number: 4178
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2025-07-23T15:03:02Z
- Update date including text: 2025-07-23T15:03:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Budget.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4178",
    "number": "4178",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "G000576",
        "district": "6",
        "firstName": "Glenn",
        "fullName": "Rep. Grothman, Glenn [R-WI-6]",
        "lastName": "Grothman",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Enforce the Caps Act",
    "type": "HR",
    "updateDate": "2025-07-23T15:03:02Z",
    "updateDateIncludingText": "2025-07-23T15:03:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "KY"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "SC"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4178ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4178\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Grothman (for himself, Mr. Barr , Mr. Norman , and Mr. Rouzer ) introduced the following bill; which was referred to the Committee on the Budget\nA BILL\nTo amend the Balanced Budget and Emergency Deficit Control Act of 1985 to provide for discretionary spending limits for each of fiscal years 2026 through 2029, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enforce the Caps Act .\n#### 2. Discretionary spending limits for fiscal years 2026 through 2029\nSection 251(c) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 901(c) ), as amended by the Fiscal Responsibility Act of 2023, is further amended\u2014\n**(1)**\nin paragraph (9)(B), by striking and at the end; and\n**(2)**\nby inserting after paragraph (10) the following:\n(11) for fiscal year 2026, for the discretionary category, $1,621,959,000,000 in new budget authority; (12) for fiscal year 2027, for the discretionary category, $1,638,179,000,000 in new budget authority; (13) for fiscal year 2028, for the discretionary category, $1,654,560,000,000 in new budget authority; and (14) for fiscal year 2029, for the discretionary category, $1,671,106,000,000 in new budget authority; .",
      "versionDate": "2025-06-26",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-07-22T19:32:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-26",
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
          "measure-id": "id119hr4178",
          "measure-number": "4178",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-26",
          "originChamber": "HOUSE",
          "update-date": "2025-07-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4178v00",
            "update-date": "2025-07-23"
          },
          "action-date": "2025-06-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Enforce the Caps Act</strong></p><p>This bill establishes annual discretionary spending limits for FY2026-FY2029. </p>"
        },
        "title": "Enforce the Caps Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4178.xml",
    "summary": {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Enforce the Caps Act</strong></p><p>This bill establishes annual discretionary spending limits for FY2026-FY2029. </p>",
      "updateDate": "2025-07-23",
      "versionCode": "id119hr4178"
    },
    "title": "Enforce the Caps Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Enforce the Caps Act</strong></p><p>This bill establishes annual discretionary spending limits for FY2026-FY2029. </p>",
      "updateDate": "2025-07-23",
      "versionCode": "id119hr4178"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4178ih.xml"
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
      "title": "Enforce the Caps Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-09T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Enforce the Caps Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-09T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Balanced Budget and Emergency Deficit Control Act of 1985 to provide for discretionary spending limits for each of fiscal years 2026 through 2029, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-09T04:19:01Z"
    }
  ]
}
```
