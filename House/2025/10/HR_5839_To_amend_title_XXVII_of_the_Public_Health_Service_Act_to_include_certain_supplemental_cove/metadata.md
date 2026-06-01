# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5839?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5839
- Title: Supplemental Benefits for Individuals Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5839
- Origin chamber: House
- Introduced date: 2025-10-28
- Update date: 2025-11-26T15:18:59Z
- Update date including text: 2025-11-26T15:18:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-10-28: Introduced in House

## Actions

- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5839",
    "number": "5839",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001306",
        "district": "12",
        "firstName": "Troy",
        "fullName": "Rep. Balderson, Troy [R-OH-12]",
        "lastName": "Balderson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Supplemental Benefits for Individuals Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-26T15:18:59Z",
    "updateDateIncludingText": "2025-11-26T15:18:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T17:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5839ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5839\nIN THE HOUSE OF REPRESENTATIVES\nOctober 28, 2025 Mr. Balderson introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XXVII of the Public Health Service Act to include certain supplemental coverage provided to individual health insurance coverage as an excepted benefit.\n#### 1. Short title\nThis Act may be cited as the Supplemental Benefits for Individuals Act of 2025 .\n#### 2. Including certain supplemental coverage provided to individual health insurance coverage as an excepted benefit\nSection 2791(c)(4) of the Public Health Service Act ( 42 U.S.C. 300gg\u201391(c)(4) ) is amended by inserting or individual health insurance coverage before the period at the end.",
      "versionDate": "2025-10-28",
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
        "name": "Health",
        "updateDate": "2025-11-26T15:18:59Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5839ih.xml"
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
      "title": "Supplemental Benefits for Individuals Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supplemental Benefits for Individuals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T09:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XXVII of the Public Health Service Act to include certain supplemental coverage provided to individual health insurance coverage as an excepted benefit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T09:48:18Z"
    }
  ]
}
```
