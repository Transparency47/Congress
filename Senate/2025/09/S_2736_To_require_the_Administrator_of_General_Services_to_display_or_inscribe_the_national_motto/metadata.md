# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2736?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2736
- Title: In God We Trust Act
- Congress: 119
- Bill type: S
- Bill number: 2736
- Origin chamber: Senate
- Introduced date: 2025-09-09
- Update date: 2025-09-16T22:11:37Z
- Update date including text: 2025-09-16T22:11:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in Senate
- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-09-09: Introduced in Senate

## Actions

- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2736",
    "number": "2736",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "In God We Trust Act",
    "type": "S",
    "updateDate": "2025-09-16T22:11:37Z",
    "updateDateIncludingText": "2025-09-16T22:11:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
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
      "actionDate": "2025-09-09",
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
          "date": "2025-09-09T15:27:48Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2736is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2736\nIN THE SENATE OF THE UNITED STATES\nSeptember 9, 2025 Mr. Hawley introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo require the Administrator of General Services to display or inscribe the national motto of the United States on all Federal buildings, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the In God We Trust Act .\n#### 2. Display of national motto on Federal buildings\n##### (a) Definition of public building\nIn this section, the term public building has the meaning given the term in section 3301(a) of title 40, United States Code.\n##### (b) Requirement\nNot later than 1 year after the date of enactment of this Act, the Administrator of General Services shall inscribe or display in a place of prominence on every public building the national motto of the United States, as described in section 302 of title 36, United States Code.",
      "versionDate": "2025-09-09",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-16T22:11:37Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2736is.xml"
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
      "title": "In God We Trust Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "In God We Trust Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-16T04:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of General Services to display or inscribe the national motto of the United States on all Federal buildings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-16T04:48:15Z"
    }
  ]
}
```
