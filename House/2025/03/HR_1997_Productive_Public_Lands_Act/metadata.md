# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1997?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1997
- Title: Productive Public Lands Act
- Congress: 119
- Bill type: HR
- Bill number: 1997
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-02-17T20:15:04Z
- Update date including text: 2026-02-17T20:15:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1997",
    "number": "1997",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001100",
        "district": "3",
        "firstName": "Jeff",
        "fullName": "Rep. Hurd, Jeff [R-CO-3]",
        "lastName": "Hurd",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Productive Public Lands Act",
    "type": "HR",
    "updateDate": "2026-02-17T20:15:04Z",
    "updateDateIncludingText": "2026-02-17T20:15:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:07:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WY"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MT"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MT"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "CO"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1997ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1997\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Hurd of Colorado (for himself, Mr. LaMalfa , Ms. Hageman , Mr. Zinke , Mr. Downing , Mr. Evans of Colorado , and Mr. Bentz ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior to reissue certain Records of Decision and Resource Management Plans.\n#### 1. Short title\nThis Act may be cited as the Productive Public Lands Act .\n#### 2. Administration of Records of Decision\nNot later than 60 days after the date of the enactment of this Act, the Secretary of the Interior, acting through the Director of the Bureau of Land Management, shall reissue each of the following and update the preferred alternative accordingly:\n**(1)**\nThe Buffalo Field Office Record of Decision and Approved Resource Management Plan Amendment, dated November 2024, selecting alternative B as the preferred alternative.\n**(2)**\nThe Record of Decision and Approved Grand Junction Field Office Resource Management Plan, dated October 2024, selecting alternative A as the preferred alternative.\n**(3)**\nThe Record of Decision and Approved Colorado River Valley Field Office Resource Management Plan, dated October 2024, selecting alternative B as the preferred alternative.\n**(4)**\nThe Miles City Field Office Record of Decision and Approved Resource Management Plan, dated November 2024, selecting alternative A as the preferred alternative.\n**(5)**\nThe Rock Springs Field Office Record of Decision and Approved Resource Management Plan, dated December 2024, selecting alternative C as the preferred alternative.\n**(6)**\nThe Record of Decision and Approved Eastern Colorado Resource Management Plan: Royal Gorge Field Office, dated January 2024, selecting alternative A or C as the preferred alternative.\n**(7)**\nThe Record of Decision and Approved Resource Management Plan Amendment for Big Game Habitat Conservation for Oil and Gas Management in Colorado, dated October 2024, selecting alternative A as the preferred alternative.\n**(8)**\nThe Lakeview Record of Decision and Approved Resource Management Plan Amendment, dated January 2025, selecting alternative A as the preferred alternative.\n**(9)**\nThe Gunnison Sage-Grouse Record of Decision and Approved Resource Management Plan Amendment, dated October 2024, selecting alternative A as the preferred alternative.\n#### 3. Authority\nThe documents reissued under section 2 and the preferred alternatives selected therein\u2014\n**(1)**\nshall be deemed to satisfy the requirements of the National Environmental Policy Act ( 42 U.S.C. 4331 et seq. ), the Federal Land Policy and Management Act ( 43 U.S.C. 1701 et seq. ), and subchapter II of chapter 5 of title 5, United States Code (commonly referred to as the Administrative Procedure Act ); and\n**(2)**\ndo not require any additional environmental analysis.",
      "versionDate": "2025-03-10",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Colorado",
            "updateDate": "2026-02-17T20:14:51Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-02-17T20:14:39Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-02-17T20:14:43Z"
          },
          {
            "name": "Montana",
            "updateDate": "2026-02-17T20:14:56Z"
          },
          {
            "name": "Oregon",
            "updateDate": "2026-02-17T20:15:00Z"
          },
          {
            "name": "Utah",
            "updateDate": "2026-02-17T20:15:04Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2026-02-17T20:14:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T18:12:07Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1997ih.xml"
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
      "title": "Productive Public Lands Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Productive Public Lands Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to reissue certain Records of Decision and Resource Management Plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:18:23Z"
    }
  ]
}
```
