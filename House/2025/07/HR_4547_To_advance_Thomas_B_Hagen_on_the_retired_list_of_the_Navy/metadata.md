# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4547?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4547
- Title: To advance Thomas B. Hagen on the retired list of the Navy.
- Congress: 119
- Bill type: HR
- Bill number: 4547
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2025-09-19T17:09:53Z
- Update date including text: 2025-09-19T17:09:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4547",
    "number": "4547",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000376",
        "district": "16",
        "firstName": "Mike",
        "fullName": "Rep. Kelly, Mike [R-PA-16]",
        "lastName": "Kelly",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "To advance Thomas B. Hagen on the retired list of the Navy.",
    "type": "HR",
    "updateDate": "2025-09-19T17:09:53Z",
    "updateDateIncludingText": "2025-09-19T17:09:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4547ih.xml",
      "text": "V\n119th CONGRESS\n1st Session\nH. R. 4547\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. Kelly of Pennsylvania introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo advance Thomas B. Hagen on the retired list of the Navy.\n#### 1. Advancement of Captain Thomas B. Hagen, United States Navy, on the retired list\n##### (a) Advancement\nCaptain Thomas B. Hagen, United States Navy (retired), is entitled to hold the rank of rear admiral (lower half) while on the retired list of the Navy.\n##### (b) Additional benefits not To accrue\nThe advancement of Thomas B. Hagen on the retired list of the Navy under subsection (a) shall not affect\u2014\n**(1)**\nthe retired pay or other benefits from the United States to which Thomas B. Hagen would have been entitled based upon his military service; or\n**(2)**\nany benefits to which any other person may become entitled based on such military service.",
      "versionDate": "2025-07-17",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-19T17:09:53Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4547ih.xml"
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
      "title": "To advance Thomas B. Hagen on the retired list of the Navy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-19T07:03:32Z"
    },
    {
      "title": "To advance Thomas B. Hagen on the retired list of the Navy.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-18T11:10:19Z"
    }
  ]
}
```
