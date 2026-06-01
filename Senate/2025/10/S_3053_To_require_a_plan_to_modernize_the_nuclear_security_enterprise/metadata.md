# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3053?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3053
- Title: A bill to require a plan to modernize the nuclear security enterprise.
- Congress: 119
- Bill type: S
- Bill number: 3053
- Origin chamber: Senate
- Introduced date: 2025-10-23
- Update date: 2025-12-03T15:06:20Z
- Update date including text: 2025-12-03T15:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-23: Introduced in Senate
- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-10-23: Introduced in Senate

## Actions

- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-23",
    "latestAction": {
      "actionDate": "2025-10-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3053",
    "number": "3053",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "A bill to require a plan to modernize the nuclear security enterprise.",
    "type": "S",
    "updateDate": "2025-12-03T15:06:20Z",
    "updateDateIncludingText": "2025-12-03T15:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-23",
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
      "actionDate": "2025-10-23",
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
          "date": "2025-10-23T19:50:03Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3053is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3053\nIN THE SENATE OF THE UNITED STATES\nOctober 23, 2025 Mr. Cornyn introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require a plan to modernize the nuclear security enterprise.\n#### 1. Plan to modernize nuclear security enterprise\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Administrator for Nuclear Security shall develop a plan\u2014\n**(1)**\nto accelerate and modernize Material Staging Capabilities to replace aged, over-subscribed facilities within the nuclear security enterprise, which shall include a description of all phases and an estimate of the costs required to carry out such plan; and\n**(2)**\nto accelerate near-term Critical Decisions milestones in fiscal year 2026.\n##### (b) Execution\nThe Administrator for Nuclear Security shall carry out the plan required by subsection (a) concurrently with an infrastructure modernization program for high explosives capabilities, including continued construction of the High Explosives Synthesis Formulation and Production facility (21\u2013D\u2013510).\n##### (c) Briefings\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Administrator for Nuclear Security shall brief the appropriate congressional committees on the Material Staging Capabilities plan required by subsection (a).\n**(2) Appropriate congressional committees defined**\nIn this subsection, the term appropriated congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Armed Services and the Committee on Appropriations of the House of Representatives.",
      "versionDate": "2025-10-23",
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
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
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
        "updateDate": "2025-12-02T20:49:09Z"
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
      "date": "2025-10-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3053is.xml"
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
      "title": "A bill to require a plan to modernize the nuclear security enterprise.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T03:48:21Z"
    },
    {
      "title": "A bill to require a plan to modernize the nuclear security enterprise.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-24T10:56:17Z"
    }
  ]
}
```
