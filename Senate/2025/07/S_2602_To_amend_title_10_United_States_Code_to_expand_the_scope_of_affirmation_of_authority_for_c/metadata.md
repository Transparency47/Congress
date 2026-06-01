# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2602?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2602
- Title: A bill to amend title 10, United States Code, to expand the scope of affirmation of authority for cyber operations to include defense of critical infrastructure of the Department of Defense, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 2602
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-19T17:54:22Z
- Update date including text: 2025-09-19T17:54:22Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2602",
    "number": "2602",
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
    "title": "A bill to amend title 10, United States Code, to expand the scope of affirmation of authority for cyber operations to include defense of critical infrastructure of the Department of Defense, and for other purposes.",
    "type": "S",
    "updateDate": "2025-09-19T17:54:22Z",
    "updateDateIncludingText": "2025-09-19T17:54:22Z"
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
          "date": "2025-07-31T18:46:36Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2602is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2602\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Rounds introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to expand the scope of affirmation of authority for cyber operations to include defense of critical infrastructure of the Department of Defense, and for other purposes.\n#### 1. Expansion of scope of affirmation of authority for cyber operations to include defense of critical infrastructure of the Department of Defense\n##### (a) Scope of affirmation of authority\nSubsection (b) of section 394 of title 10, United States Code, is amended by inserting defense of critical infrastructure of the Department of Defense, after force protection, .\n##### (b) Amendment to definitions\nSubsection (f) of such section 394 is amended\u2014\n**(1)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4), respectively; and\n**(2)**\nby inserting after paragraph (1) the following new paragraph (2):\n(2) The term critical infrastructure of the Department of Defense means any asset of the Department of Defense of such extraordinary importance to the functioning of the Department and the operation of the armed forces that the incapacitation or destruction of such asset by a cyber attack would have a debilitating effect on the ability of the Department to fulfill its missions. .",
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
        "updateDate": "2025-09-19T17:54:22Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2602is.xml"
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
      "title": "A bill to amend title 10, United States Code, to expand the scope of affirmation of authority for cyber operations to include defense of critical infrastructure of the Department of Defense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:53Z"
    },
    {
      "title": "A bill to amend title 10, United States Code, to expand the scope of affirmation of authority for cyber operations to include defense of critical infrastructure of the Department of Defense, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T10:56:20Z"
    }
  ]
}
```
