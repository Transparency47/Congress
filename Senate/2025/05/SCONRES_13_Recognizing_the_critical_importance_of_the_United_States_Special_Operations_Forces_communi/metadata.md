# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sconres/13?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/13
- Title: A concurrent resolution recognizing the critical importance of the United States Special Operations Forces community and expressing support for the designation of SOF Week.
- Congress: 119
- Bill type: SCONRES
- Bill number: 13
- Origin chamber: Senate
- Introduced date: 2025-05-06
- Update date: 2025-12-05T22:59:05Z
- Update date including text: 2025-12-05T22:59:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-06: Introduced in Senate
- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S2778)
- Latest action: 2025-05-06: Introduced in Senate

## Actions

- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S2778)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/13",
    "number": "13",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "A concurrent resolution recognizing the critical importance of the United States Special Operations Forces community and expressing support for the designation of SOF Week.",
    "type": "SCONRES",
    "updateDate": "2025-12-05T22:59:05Z",
    "updateDateIncludingText": "2025-12-05T22:59:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Armed Services. (text: CR S2778)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T19:45:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres13is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. CON. RES. 13\nIN THE SENATE OF THE UNITED STATES\nMay 6, 2025 Ms. Ernst submitted the following concurrent resolution; which was referred to the Committee on Armed Services\nCONCURRENT RESOLUTION\nRecognizing the critical importance of the United States Special Operations Forces community and expressing support for the designation of SOF Week.\nThat Congress\u2014\n**(1)**\nrecognizes the critical importance of the United States Special Operations Forces community to the defense and security of the United States;\n**(2)**\ncommits to honoring the skill, dedication, bravery, and selfless service of SOF personnel and their families; and\n**(3)**\nsupports the designation of SOF Week in appreciation of the courage, commitment, and contributions of the SOF community.",
      "versionDate": "2025-05-06",
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
        "actionDate": "2025-05-06",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "95",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the critical importance of the United States Special Operations Forces community and expressing support for the designation of SOF Week.",
      "type": "HJRES"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-11T14:45:10Z"
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
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres13is.xml"
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
      "title": "A concurrent resolution recognizing the critical importance of the United States Special Operations Forces community and expressing support for the designation of SOF Week.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-08T04:33:33Z"
    },
    {
      "title": "A concurrent resolution recognizing the critical importance of the United States Special Operations Forces community and expressing support for the designation of SOF Week.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T10:56:20Z"
    }
  ]
}
```
