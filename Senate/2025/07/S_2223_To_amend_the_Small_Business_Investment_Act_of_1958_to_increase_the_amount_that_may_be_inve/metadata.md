# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2223?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2223
- Title: Investing in Main Street Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2223
- Origin chamber: Senate
- Introduced date: 2025-07-09
- Update date: 2025-09-23T14:46:32Z
- Update date including text: 2025-09-23T14:46:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-09: Introduced in Senate
- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-09: Introduced in Senate

## Actions

- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-09",
    "latestAction": {
      "actionDate": "2025-07-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2223",
    "number": "2223",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Investing in Main Street Act of 2025",
    "type": "S",
    "updateDate": "2025-09-23T14:46:32Z",
    "updateDateIncludingText": "2025-09-23T14:46:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-09",
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
      "actionDate": "2025-07-09",
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
          "date": "2025-07-09T18:26:08Z",
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "AZ"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "ID"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2223is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2223\nIN THE SENATE OF THE UNITED STATES\nJuly 9, 2025 Mr. Young (for himself, Mr. Gallego , Mr. Risch , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Small Business Investment Act of 1958 to increase the amount that may be invested in small business investment companies.\n#### 1. Short title\nThis Act may be cited as the Investing in Main Street Act of 2025 .\n#### 2. Investment in small business investment companies\nSection 302(b) of the Small Business Investment Act of 1958 ( 15 U.S.C. 682(b) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking 5 percent and inserting 15 percent ; and\n**(2)**\nin paragraph (2), by striking 5 percent and inserting 15 percent .",
      "versionDate": "2025-07-09",
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
        "actionDate": "2025-02-25",
        "text": "Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "754",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Investing in Main Street Act of 2025",
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
        "updateDate": "2025-07-29T15:01:09Z"
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
      "date": "2025-07-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2223is.xml"
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
      "title": "Investing in Main Street Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Investing in Main Street Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-17T02:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Investment Act of 1958 to increase the amount that may be invested in small business investment companies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T02:33:24Z"
    }
  ]
}
```
