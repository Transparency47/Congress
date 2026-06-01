# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4267?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4267
- Title: Strengthening American Nuclear Energy Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4267
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-13T16:15:49Z
- Update date including text: 2026-04-13T16:15:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4267",
    "number": "4267",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Strengthening American Nuclear Energy Act of 2026",
    "type": "S",
    "updateDate": "2026-04-13T16:15:49Z",
    "updateDateIncludingText": "2026-04-13T16:15:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T21:21:07Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4267is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4267\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Ms. Lummis (for herself and Mr. Cotton ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo codify certain Executive orders relating to nuclear energy.\n#### 1. Short title\nThis Act may be cited as the Strengthening American Nuclear Energy Act of 2026 .\n#### 2. Codification of Executive orders relating to nuclear energy\nThe following Executive orders, signed on May 23, 2025, shall have the force and effect of law:\n**(1)**\nExecutive Order 14301 (90 Fed. Reg. 22591 (May 29, 2025); relating to reforming nuclear reactor testing at the Department of Energy).\n**(2)**\nExecutive Order 14299 (90 Fed. Reg. 22581 (May 29, 2025); relating to deploying advanced nuclear reactor technologies for national security).\n**(3)**\nExecutive Order 14300 (90 Fed. Reg. 22587 (May 29, 2025); relating to ordering the reform of the Nuclear Regulatory Commission).\n**(4)**\nExecutive Order 14302 (90 Fed. Reg. 22595 (May 29, 2025); relating to reinvigorating the nuclear industrial base).",
      "versionDate": "2026-03-26",
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
        "name": "Energy",
        "updateDate": "2026-04-13T16:15:49Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4267is.xml"
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
      "title": "Strengthening American Nuclear Energy Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-10T02:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening American Nuclear Energy Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-10T02:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to codify certain Executive orders relating to nuclear energy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-10T02:33:19Z"
    }
  ]
}
```
