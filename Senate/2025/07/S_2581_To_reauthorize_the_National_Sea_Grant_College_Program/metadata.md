# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2581?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2581
- Title: A bill to reauthorize the National Sea Grant College Program.
- Congress: 119
- Bill type: S
- Bill number: 2581
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-18T20:26:46Z
- Update date including text: 2025-09-18T20:26:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2581",
    "number": "2581",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C000127",
        "district": "",
        "firstName": "Maria",
        "fullName": "Sen. Cantwell, Maria [D-WA]",
        "lastName": "Cantwell",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "A bill to reauthorize the National Sea Grant College Program.",
    "type": "S",
    "updateDate": "2025-09-18T20:26:46Z",
    "updateDateIncludingText": "2025-09-18T20:26:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T16:58:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "MS"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "DE"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2581is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2581\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Ms. Cantwell (for herself, Mr. Wicker , Ms. Blunt Rochester , and Mr. Sullivan ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo reauthorize the National Sea Grant College Program.\n#### 1. Authorization of appropriations for National Sea Grant College Program\nSection 212(a) of the National Sea Grant College Program Act ( 33 U.S.C. 1131(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking this title and all that follows through (E) and inserting this title ; and\n**(B)**\nby striking for fiscal year 2025 and inserting for each of fiscal years 2025 through 2031 ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin the paragraph heading, by striking for fiscal years 2021 through 2025 ; and\n**(B)**\nin the matter preceding subparagraph (A), by striking fiscal years 2021 through 2025 and inserting fiscal years 2025 through 2031 .",
      "versionDate": "2025-07-31",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-18T20:26:46Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2581is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the National Sea Grant College Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:37Z"
    },
    {
      "title": "A bill to reauthorize the National Sea Grant College Program.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T10:56:33Z"
    }
  ]
}
```
