# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1334?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1334
- Title: A bill to amend the Internal Revenue Code of 1986 to increase the percentage limitation on assets of real estate investment trusts which may be held in taxable REIT subsidiaries.
- Congress: 119
- Bill type: S
- Bill number: 1334
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2025-05-09T17:45:42Z
- Update date including text: 2025-05-09T17:45:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1334",
    "number": "1334",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to increase the percentage limitation on assets of real estate investment trusts which may be held in taxable REIT subsidiaries.",
    "type": "S",
    "updateDate": "2025-05-09T17:45:42Z",
    "updateDateIncludingText": "2025-05-09T17:45:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T17:16:33Z",
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1334is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1334\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Tillis (for himself and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase the percentage limitation on assets of real estate investment trusts which may be held in taxable REIT subsidiaries.\n#### 1. Increase in percentage limitation on assets of REIT which may be taxable REIT subsidiaries\n##### (a) In general\nSection 856(c)(4)(B)(ii) of the Internal Revenue Code of 1986 is amended by striking 20 percent and inserting 25 percent .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-04-08",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T17:45:42Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1334is.xml"
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
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase the percentage limitation on assets of real estate investment trusts which may be held in taxable REIT subsidiaries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-22T03:48:27Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase the percentage limitation on assets of real estate investment trusts which may be held in taxable REIT subsidiaries.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T10:56:20Z"
    }
  ]
}
```
