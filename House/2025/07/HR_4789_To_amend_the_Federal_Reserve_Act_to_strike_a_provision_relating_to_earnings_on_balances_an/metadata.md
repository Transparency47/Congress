# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4789?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4789
- Title: FAIR Act
- Congress: 119
- Bill type: HR
- Bill number: 4789
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2025-12-05T22:56:42Z
- Update date including text: 2025-12-05T22:56:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4789",
    "number": "4789",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "FAIR Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:56:42Z",
    "updateDateIncludingText": "2025-12-05T22:56:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4789ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4789\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mr. Davidson introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Federal Reserve Act to strike a provision relating to earnings on balances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fiscal Accountability for Interest on Reserves Act or the FAIR Act .\n#### 2. Earnings on balances\n##### (a) In general\nSection 19(b) of the Federal Reserve Act ( 12 U.S.C. 461(b) ) is amended by striking paragraph (12).\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-07-29",
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
        "actionDate": "2025-07-29",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2499",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FAIR Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-17T15:50:24Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4789ih.xml"
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
      "title": "FAIR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T08:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T08:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fiscal Accountability for Interest on Reserves Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T08:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Reserve Act to strike a provision relating to earnings on balances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T08:04:16Z"
    }
  ]
}
```
