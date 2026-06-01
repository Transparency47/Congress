# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/258?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/258
- Title: A resolution honoring the lives and service of Natalie and Davy Lloyd and expressing condolence to the family of Natalie and Davy Lloyd.
- Congress: 119
- Bill type: SRES
- Bill number: 258
- Origin chamber: Senate
- Introduced date: 2025-06-02
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-02: Introduced in Senate
- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3171)
- Latest action: 2025-06-02: Introduced in Senate

## Actions

- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3171)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-02",
    "latestAction": {
      "actionDate": "2025-06-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/258",
    "number": "258",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "A resolution honoring the lives and service of Natalie and Davy Lloyd and expressing condolence to the family of Natalie and Davy Lloyd.",
    "type": "SRES",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-02",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S3171)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-02",
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
          "date": "2025-06-02T19:22:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres258is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 258\nIN THE SENATE OF THE UNITED STATES\nJune 2, 2025 Mr. Hawley (for himself and Mr. Schmitt ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the lives and service of Natalie and Davy Lloyd and expressing condolence to the family of Natalie and Davy Lloyd.\nThat the Senate\u2014\n**(1)**\nextends heartfelt condolences to the family and friends of Natalie and David ( Davy ) Lloyd;\n**(2)**\nrecognizes and honors Natalie and Davy Lloyd as extraordinarily faithful missionaries who selflessly dedicated their entire lives to God and serving others; and\n**(3)**\ncommemorates the amazing work Natalie and Davy Lloyd completed as missionaries in Haiti and the powerful legacy that the young couple leaves.",
      "versionDate": "2025-06-02",
      "versionType": "IS"
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
        "name": "International Affairs",
        "updateDate": "2025-07-15T17:26:16Z"
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
      "date": "2025-06-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres258is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution honoring the lives and service of Natalie and Davy Lloyd and expressing condolence to the family of Natalie and Davy Lloyd.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:40Z"
    },
    {
      "title": "A resolution honoring the lives and service of Natalie and Davy Lloyd and expressing condolence to the family of Natalie and Davy Lloyd.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T10:56:19Z"
    }
  ]
}
```
