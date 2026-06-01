# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2599?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2599
- Title: A bill to provide for modifications to the State Partnership Program selection analysis.
- Congress: 119
- Bill type: S
- Bill number: 2599
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-19T17:55:46Z
- Update date including text: 2025-09-19T17:55:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2599",
    "number": "2599",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "A bill to provide for modifications to the State Partnership Program selection analysis.",
    "type": "S",
    "updateDate": "2025-09-19T17:55:46Z",
    "updateDateIncludingText": "2025-09-19T17:55:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T18:36:27Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2599is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2599\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Rounds introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo provide for modifications to the State Partnership Program selection analysis.\n#### 1. State partnership program selection analysis\nThe Secretary of Defense shall make such changes to Department of Defense Instruction 5111.20 (relating to the State Partnership Program) (or a successor instruction) as may be necessary to ensure that, in performing selection analysis for the State Partnership Program under section 341 of title 10, United States Code, the Chief of the National Guard Bureau\u2014\n**(1)**\nconsiders the number of current partnerships assigned to the National Guard of a State; and\n**(2)**\ngives preference to States that have only one active assigned country under the program.",
      "versionDate": "2025-07-31",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-09-17",
        "text": "Considered by Senate. (consideration: CR S6667: 5)"
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
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
        "updateDate": "2025-09-19T17:55:46Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2599is.xml"
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
      "title": "A bill to provide for modifications to the State Partnership Program selection analysis.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:19Z"
    },
    {
      "title": "A bill to provide for modifications to the State Partnership Program selection analysis.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T10:56:27Z"
    }
  ]
}
```
