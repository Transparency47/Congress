# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3615?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3615
- Title: Multiemployer Plan Relief Act
- Congress: 119
- Bill type: S
- Bill number: 3615
- Origin chamber: Senate
- Introduced date: 2026-01-12
- Update date: 2026-02-04T22:58:14Z
- Update date including text: 2026-02-04T22:58:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-12: Introduced in Senate
- 2026-01-12 - IntroReferral: Introduced in Senate
- 2026-01-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-12: Introduced in Senate

## Actions

- 2026-01-12 - IntroReferral: Introduced in Senate
- 2026-01-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-12",
    "latestAction": {
      "actionDate": "2026-01-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3615",
    "number": "3615",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Multiemployer Plan Relief Act",
    "type": "S",
    "updateDate": "2026-02-04T22:58:14Z",
    "updateDateIncludingText": "2026-02-04T22:58:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-12",
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
      "actionDate": "2026-01-12",
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
          "date": "2026-01-12T23:00:49Z",
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
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3615is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3615\nIN THE SENATE OF THE UNITED STATES\nJanuary 12, 2026 Ms. Klobuchar (for herself and Mr. Moreno ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish an exception for multiemployer plan participants to the requirements for automatic enrollment.\n#### 1. Short title\nThis Act may be cited as the Multiemployer Plan Relief Act .\n#### 2. Exception to requirements related to automatic enrollment\n##### (a) In general\nSection 414A(c)(3) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin the heading, by striking governmental and church plans and inserting governmental, church plans, and multiemployer plans , and\n**(2)**\nby striking 414(d)) or any church plan (within the meaning of section 414(e)) and inserting 414(d)), any church plan (within the meaning of section 414(e)), or any multiemployer plan (within the meaning of section 414(f)) .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2026-01-12",
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
        "updateDate": "2026-02-04T22:58:14Z"
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
      "date": "2026-01-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3615is.xml"
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
      "title": "A bill to amend the Internal Revenue Code of 1986 to establish an exception for multiemployer plan participants to the requirements for automatic enrollment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:48Z"
    },
    {
      "title": "Multiemployer Plan Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T10:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Multiemployer Plan Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:15Z"
    }
  ]
}
```
