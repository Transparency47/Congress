# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/724?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/724
- Title: Temporary Extension of Fentanyl-Related Substances Scheduling Act
- Congress: 119
- Bill type: S
- Bill number: 724
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2025-07-24T14:27:02Z
- Update date including text: 2025-07-24T14:27:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/724",
    "number": "724",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Temporary Extension of Fentanyl-Related Substances Scheduling Act",
    "type": "S",
    "updateDate": "2025-07-24T14:27:02Z",
    "updateDateIncludingText": "2025-07-24T14:27:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T22:12:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s724is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 724\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Booker introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo extend the temporary scheduling order for fentanyl-related substances for 6 months.\n#### 1. Short title\nThis Act may be cited as the Temporary Extension of Fentanyl-Related Substances Scheduling Act .\n#### 2. Extension of temporary order for fentanyl-related substances\nSection 2 of the Temporary Reauthorization and Study of the Emergency Scheduling of Fentanyl Analogues Act ( Public Law 116\u2013114 ; 134 Stat. 103) is amended by striking March 31, 2025 and inserting September 30, 2025 .",
      "versionDate": "2025-02-25",
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
      "legislativeSubjects": {
        "item": {
          "name": "Drug trafficking and controlled substances",
          "updateDate": "2025-07-24T14:27:02Z"
        }
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-14T18:01:24Z"
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s724is.xml"
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
      "title": "Temporary Extension of Fentanyl-Related Substances Scheduling Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Temporary Extension of Fentanyl-Related Substances Scheduling Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to extend the temporary scheduling order for fentanyl-related substances for 6 months.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:07Z"
    }
  ]
}
```
