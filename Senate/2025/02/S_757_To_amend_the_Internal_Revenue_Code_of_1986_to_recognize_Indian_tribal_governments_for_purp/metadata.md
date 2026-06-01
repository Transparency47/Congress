# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/757?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/757
- Title: Tribal Adoption Parity Act
- Congress: 119
- Bill type: S
- Bill number: 757
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2025-05-07T18:24:26Z
- Update date including text: 2025-05-07T18:24:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/757",
    "number": "757",
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
    "title": "Tribal Adoption Parity Act",
    "type": "S",
    "updateDate": "2025-05-07T18:24:26Z",
    "updateDateIncludingText": "2025-05-07T18:24:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T21:16:07Z",
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
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s757is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 757\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Ms. Klobuchar (for herself and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to recognize Indian tribal governments for purposes of determining under the adoption credit whether a child has special needs.\n#### 1. Short title\nThis Act may be cited as the Tribal Adoption Parity Act .\n#### 2. Recognizing Indian tribal governments for purposes of determining under the adoption credit whether a child has special needs\n##### (a) In general\nParagraph (3) of section 23(d) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subparagraph (A), by inserting or Indian tribal government after the words a State , and\n**(2)**\nin subparagraph (B), by inserting or Indian tribal government after the words such State .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-02-26",
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
        "updateDate": "2025-05-07T18:24:26Z"
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
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s757is.xml"
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
      "title": "Tribal Adoption Parity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tribal Adoption Parity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to recognize Indian tribal governments for purposes of determining under the adoption credit whether a child has special needs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T03:48:21Z"
    }
  ]
}
```
