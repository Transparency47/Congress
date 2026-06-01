# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2949?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2949
- Title: Colorectal Cancer Payment Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 2949
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2026-01-09T12:03:23Z
- Update date including text: 2026-01-09T12:03:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2949",
    "number": "2949",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Colorectal Cancer Payment Fairness Act",
    "type": "S",
    "updateDate": "2026-01-09T12:03:23Z",
    "updateDateIncludingText": "2026-01-09T12:03:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-30",
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
            "date": "2025-09-30T19:04:02Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-30T19:04:02Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NM"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2949is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2949\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Mr. Booker (for himself and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend title XVIII of the Social Security Act to eliminate the coinsurance requirement for certain colorectal cancer screening tests furnished under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Colorectal Cancer Payment Fairness Act .\n#### 2. Eliminating the coinsurance requirement for certain colorectal cancer screening tests furnished under the Medicare program\nSection 1833(dd) of the Social Security Act ( 42 U.S.C. 1395l(dd) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking and before January 1, 2030, ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (B), by striking through 2026 and inserting through 2025 ; and\n**(B)**\nby striking subparagraph (C) and inserting the following:\n(C) for 2026 and each subsequent year, 100 percent. .",
      "versionDate": "2025-09-30",
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
        "updateDate": "2025-12-11T15:49:21Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2949is.xml"
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
      "title": "Colorectal Cancer Payment Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Colorectal Cancer Payment Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T02:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to eliminate the coinsurance requirement for certain colorectal cancer screening tests furnished under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T02:48:26Z"
    }
  ]
}
```
