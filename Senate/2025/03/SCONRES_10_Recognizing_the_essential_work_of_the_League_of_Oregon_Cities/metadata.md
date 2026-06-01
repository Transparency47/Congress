# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sconres/10?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/10
- Title: A concurrent resolution recognizing the essential work of the League of Oregon Cities.
- Congress: 119
- Bill type: SCONRES
- Bill number: 10
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2025-12-05T22:57:05Z
- Update date including text: 2025-12-05T22:57:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1668)
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1668)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/10",
    "number": "10",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "A concurrent resolution recognizing the essential work of the League of Oregon Cities.",
    "type": "SCONRES",
    "updateDate": "2025-12-05T22:57:05Z",
    "updateDateIncludingText": "2025-12-05T22:57:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1668)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T19:44:04Z",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres10is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. CON. RES. 10\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Merkley (for himself and Mr. Wyden ) submitted the following concurrent resolution; which was referred to the Committee on the Judiciary\nCONCURRENT RESOLUTION\nRecognizing the essential work of the League of Oregon Cities.\nThat Congress recognizes the essential work of the League of Oregon Cities since 1925 and the role the League of Oregon Cities will play in the future in supporting municipalities in the State of Oregon with unparalleled research, technical expertise, and relentless advocacy as a key partner in preserving and strengthening the Federal-local partnership.",
      "versionDate": "2025-03-11",
      "versionType": "IS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "19",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the essential work of the League of Oregon Cities.",
      "type": "HCONRES"
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
        "updateDate": "2025-05-14T15:11:07Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres10is.xml"
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
      "title": "A concurrent resolution recognizing the essential work of the League of Oregon Cities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:18:21Z"
    },
    {
      "title": "A concurrent resolution recognizing the essential work of the League of Oregon Cities.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T10:56:24Z"
    }
  ]
}
```
