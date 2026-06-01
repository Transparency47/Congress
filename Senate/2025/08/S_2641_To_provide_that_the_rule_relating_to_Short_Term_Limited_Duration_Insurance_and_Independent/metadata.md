# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2641?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2641
- Title: Health Care Freedom and Choice Act
- Congress: 119
- Bill type: S
- Bill number: 2641
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-12-05T12:03:29Z
- Update date including text: 2025-12-05T12:03:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2641",
    "number": "2641",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000293",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Johnson, Ron [R-WI]",
        "lastName": "Johnson",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Health Care Freedom and Choice Act",
    "type": "S",
    "updateDate": "2025-12-05T12:03:29Z",
    "updateDateIncludingText": "2025-12-05T12:03:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T15:24:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "IA"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2641is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2641\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Johnson introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide that the rule relating to Short-Term, Limited-Duration Insurance and Independent, Noncoordinated Excepted Benefits Coverage shall have no force or effect.\n#### 1. Short title\nThis Act may be cited as the Health Care Freedom and Choice Act .\n#### 2. Short-term, limited duration insurance rule nullification\nThe final interagency rule published by the Internal Revenue Service, the Employee Benefits Security Administration, and the Centers for Medicare & Medicaid Services relating to Short-Term, Limited-Duration Insurance and Independent, Noncoordinated Excepted Benefits Coverage (89 Fed. Reg. 23338 (April 3, 2024)) shall have no force or effect.",
      "versionDate": "2025-08-01",
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
        "updateDate": "2025-09-18T19:02:38Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2641is.xml"
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
      "title": "Health Care Freedom and Choice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T12:03:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Health Care Freedom and Choice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide that the rule relating to \"Short-Term, Limited-Duration Insurance and Independent, Noncoordinated Excepted Benefits Coverage\" shall have no force or effect.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:33Z"
    }
  ]
}
```
