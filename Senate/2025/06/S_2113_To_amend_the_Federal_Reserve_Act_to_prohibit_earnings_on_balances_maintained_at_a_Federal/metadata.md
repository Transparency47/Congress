# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2113?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2113
- Title: End the Fed’s Big Bank Bailout Act
- Congress: 119
- Bill type: S
- Bill number: 2113
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2026-01-29T16:15:02Z
- Update date including text: 2026-01-29T16:15:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-12-11 - Committee: Committee on Homeland Security and Governmental Affairs. Hearings held.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-12-11 - Committee: Committee on Homeland Security and Governmental Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2113",
    "number": "2113",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "End the Fed\u2019s Big Bank Bailout Act",
    "type": "S",
    "updateDate": "2026-01-29T16:15:02Z",
    "updateDateIncludingText": "2026-01-29T16:15:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
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
          "date": "2025-12-11T17:42:19Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-18T16:37:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2113is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2113\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Paul introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Federal Reserve Act to prohibit earnings on balances maintained at a Federal Reserve bank by or on behalf of a depository institution.\n#### 1. Short title\nThis Act may be cited as the End the Fed\u2019s Big Bank Bailout Act .\n#### 2. Prohibition on earnings\nSection 19(b) of the Federal Reserve Act ( 12 U.S.C. 461(b) ) is amended by striking paragraph (12) and inserting the following:\n(12) Earnings on balances No Federal Reserve bank may pay earnings on balances maintained at a Federal Reserve bank by or on behalf of a depository institution. .",
      "versionDate": "2025-06-18",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-01-29T16:04:07Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-01-29T16:15:01Z"
          },
          {
            "name": "Federal Reserve System",
            "updateDate": "2026-01-29T16:03:59Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-01-29T16:14:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-14T14:18:05Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2113is.xml"
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
      "title": "End the Fed\u2019s Big Bank Bailout Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "End the Fed\u2019s Big Bank Bailout Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Reserve Act to prohibit earnings on balances maintained at a Federal Reserve bank by or on behalf of a depository institution.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:34:09Z"
    }
  ]
}
```
