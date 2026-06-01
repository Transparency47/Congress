# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4412?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4412
- Title: No FED in West Texas Act
- Congress: 119
- Bill type: S
- Bill number: 4412
- Origin chamber: Senate
- Introduced date: 2026-04-28
- Update date: 2026-05-15T18:21:34Z
- Update date including text: 2026-05-15T18:21:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in Senate
- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-04-28: Introduced in Senate

## Actions

- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4412",
    "number": "4412",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "No FED in West Texas Act",
    "type": "S",
    "updateDate": "2026-05-15T18:21:34Z",
    "updateDateIncludingText": "2026-05-15T18:21:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-28",
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
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T20:43:12Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4412is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4412\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2026 Mr. Cruz introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo prohibit the implementation of a Land Protection Plan for Muleshoe National Wildlife Refuge.\n#### 1. Short title\nThis Act may be cited as the No Federal Expansion Designation in West Texas Act or the No FED in West Texas Act .\n#### 2. Implementation of Land Protection Plan for Muleshoe National Wildlife Refuge prohibited\nThe Secretary of the Interior may not finalize, implement, administer, or enforce the Land Protection Plan described in the document published by the United States Fish and Wildlife Service entitled Final Land Protection Plan & Environmental Assessment Muleshoe National Wildlife Refuge and dated February 2023, or a substantially similar land protection plan.",
      "versionDate": "2026-04-28",
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
        "actionDate": "2026-01-08",
        "text": "Placed on the Union Calendar, Calendar No. 374."
      },
      "number": "839",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No FED in West Texas Act",
      "type": "HR"
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-05-15T18:21:34Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4412is.xml"
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
      "title": "No FED in West Texas Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T02:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No FED in West Texas Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T02:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Federal Expansion Designation in West Texas Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T02:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the implementation of a Land Protection Plan for Muleshoe National Wildlife Refuge.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T02:48:25Z"
    }
  ]
}
```
