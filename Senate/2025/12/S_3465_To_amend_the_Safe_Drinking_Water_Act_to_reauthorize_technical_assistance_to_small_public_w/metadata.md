# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3465?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3465
- Title: UPGRADE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3465
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-01-07T16:58:37Z
- Update date including text: 2026-01-07T16:58:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3465",
    "number": "3465",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001303",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
        "lastName": "Blunt Rochester",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "UPGRADE Act of 2025",
    "type": "S",
    "updateDate": "2026-01-07T16:58:37Z",
    "updateDateIncludingText": "2026-01-07T16:58:37Z"
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
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T20:40:06Z",
          "name": "Referred To"
        }
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3465is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3465\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Ms. Blunt Rochester (for herself and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Safe Drinking Water Act to reauthorize technical assistance to small public water systems and the assistance for small and disadvantaged communities program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Unincorporated Partnerships for Grant Resources, Assistance, and Drinking Water Enhancements Act of 2025 or the UPGRADE Act of 2025 .\n#### 2. Technical assistance to small public water systems\nSection 1442(e)(5) of the Safe Drinking Water Act ( 42 U.S.C. 300j\u20131(e)(5) ) is amended by striking 2026 and inserting 2031 .\n#### 3. Assistance for small and disadvantaged communities\nSection 1459A of the Safe Drinking Water Act ( 42 U.S.C. 300j\u201319a ) is amended\u2014\n**(1)**\nin subsection (c)(1), by striking subparagraph (C) and inserting the following:\n(C) a State, on behalf of\u2014 (i) an underserved community; or (ii) an unincorporated community, as determined by the applicable State and identified through coordination with applicable county governments; and ; and\n**(2)**\nin subsection (k)(5), by striking fiscal year 2026 and inserting each of fiscal years 2026 through 2031 .",
      "versionDate": "2025-12-11",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-07T16:58:37Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3465is.xml"
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
      "title": "UPGRADE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-31T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "UPGRADE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Unincorporated Partnerships for Grant Resources, Assistance, and Drinking Water Enhancements Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Safe Drinking Water Act to reauthorize technical assistance to small public water systems and the assistance for small and disadvantaged communities program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:48:21Z"
    }
  ]
}
```
