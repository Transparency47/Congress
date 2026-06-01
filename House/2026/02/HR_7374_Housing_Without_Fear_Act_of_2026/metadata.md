# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7374?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7374
- Title: Housing Without Fear Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7374
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-02-18T17:24:26Z
- Update date including text: 2026-02-18T17:24:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7374",
    "number": "7374",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000620",
        "district": "29",
        "firstName": "Luz",
        "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
        "lastName": "Rivas",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Housing Without Fear Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-18T17:24:26Z",
    "updateDateIncludingText": "2026-02-18T17:24:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7374ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7374\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Ms. Rivas introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo nullify a memorandum of understanding signed by the Secretary of Housing and Urban Development and the Secretary of Homeland Security.\n#### 1. Short title\nThis Act may be cited as the Housing Without Fear Act of 2026 .\n#### 2. Nullification of memorandum of understanding between HUD and DHS\nThe Secretary of Housing and Urban Development and the Secretary of Homeland Security may not carry out the memorandum of understanding signed by the Secretaries on March 24, 2025.",
      "versionDate": "2026-02-04",
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
        "name": "Housing and Community Development",
        "updateDate": "2026-02-18T17:24:26Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7374ih.xml"
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
      "title": "Housing Without Fear Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T06:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Without Fear Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T06:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To nullify a memorandum of understanding signed by the Secretary of Housing and Urban Development and the Secretary of Homeland Security.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T06:03:27Z"
    }
  ]
}
```
