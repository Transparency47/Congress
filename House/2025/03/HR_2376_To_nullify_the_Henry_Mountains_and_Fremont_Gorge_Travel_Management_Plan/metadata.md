# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2376?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2376
- Title: To nullify the Henry Mountains and Fremont Gorge Travel Management Plan.
- Congress: 119
- Bill type: HR
- Bill number: 2376
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2025-05-21T18:26:50Z
- Update date including text: 2025-05-21T18:26:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2376",
    "number": "2376",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001228",
        "district": "2",
        "firstName": "Celeste",
        "fullName": "Rep. Maloy, Celeste [R-UT-2]",
        "lastName": "Maloy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "To nullify the Henry Mountains and Fremont Gorge Travel Management Plan.",
    "type": "HR",
    "updateDate": "2025-05-21T18:26:50Z",
    "updateDateIncludingText": "2025-05-21T18:26:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-03-26T14:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2376ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2376\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Ms. Maloy introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo nullify the Henry Mountains and Fremont Gorge Travel Management Plan.\n#### 1. Nullification of Henry Mountains and Fremont Gorge TMP\nThe Secretary of the Interior shall not implement, administer, or enforce the decision record titled Decision Record Henry Mountains and Fremont Gorge Travel Management Plan published by the Bureau of Land Management and dated January 2025, and such decision record shall have no force or effect.",
      "versionDate": "2025-03-26",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-05-21T18:26:50Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2376ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To nullify the Henry Mountains and Fremont Gorge Travel Management Plan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:21Z"
    },
    {
      "title": "To nullify the Henry Mountains and Fremont Gorge Travel Management Plan.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T08:06:56Z"
    }
  ]
}
```
