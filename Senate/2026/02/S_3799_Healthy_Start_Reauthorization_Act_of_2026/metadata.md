# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3799?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3799
- Title: Healthy Start Reauthorization Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3799
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-02-27T16:55:21Z
- Update date including text: 2026-02-27T16:55:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-02-05: Introduced in Senate

## Actions

- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3799",
    "number": "3799",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Healthy Start Reauthorization Act of 2026",
    "type": "S",
    "updateDate": "2026-02-27T16:55:21Z",
    "updateDateIncludingText": "2026-02-27T16:55:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-05",
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
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T20:12:03Z",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3799is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3799\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Mr. Marshall (for himself, Mrs. Gillibrand , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to reauthorize the Healthy Start Initiative.\n#### 1. Short title\nThis Act may be cited as the Healthy Start Reauthorization Act of 2026 .\n#### 2. Reauthorization of Healthy Start Initiative\nSection 330H(e)(1) of the Public Health Service Act ( 42 U.S.C. 254c\u20138(e)(1) ) is amended by striking appropriated and all that follows through the period at the end and inserting appropriated $145,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2026-02-05",
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
        "updateDate": "2026-02-27T16:55:21Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3799is.xml"
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
      "title": "Healthy Start Reauthorization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T06:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Healthy Start Reauthorization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T06:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to reauthorize the Healthy Start Initiative.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T06:18:30Z"
    }
  ]
}
```
