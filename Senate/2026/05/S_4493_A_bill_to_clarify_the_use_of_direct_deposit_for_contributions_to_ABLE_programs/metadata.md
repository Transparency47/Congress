# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4493?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4493
- Title: A bill to clarify the use of direct deposit for contributions to ABLE programs.
- Congress: 119
- Bill type: S
- Bill number: 4493
- Origin chamber: Senate
- Introduced date: 2026-05-12
- Update date: 2026-05-20T03:03:24Z
- Update date including text: 2026-05-20T03:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-12: Introduced in Senate
- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-12: Introduced in Senate

## Actions

- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4493",
    "number": "4493",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "A bill to clarify the use of direct deposit for contributions to ABLE programs.",
    "type": "S",
    "updateDate": "2026-05-20T03:03:24Z",
    "updateDateIncludingText": "2026-05-20T03:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T18:46:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "KS"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4493is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4493\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2026 Mr. Van Hollen (for himself, Mr. Moran , Ms. Klobuchar , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo clarify the use of direct deposit for contributions to ABLE programs.\n#### 1. Use of direct deposit for contributions to ABLE programs\nNo provision of law shall be construed to prevent the use of direct deposit for making contributions to qualified ABLE programs (as defined in section 529A of the Internal Revenue Code of 1986).",
      "versionDate": "2026-05-12",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4493is.xml"
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
      "title": "A bill to clarify the use of direct deposit for contributions to ABLE programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T03:03:24Z"
    },
    {
      "title": "A bill to clarify the use of direct deposit for contributions to ABLE programs.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T10:56:25Z"
    }
  ]
}
```
