# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8647?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8647
- Title: Representative Green's Original Legislation to increase from 9 to 13 the number of justices of the Supreme Court.
- Congress: 119
- Bill type: HR
- Bill number: 8647
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-21T15:08:36Z
- Update date including text: 2026-05-21T15:08:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-04: Introduced in House

## Actions

- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-04",
    "latestAction": {
      "actionDate": "2026-05-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8647",
    "number": "8647",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "G000553",
        "district": "9",
        "firstName": "Al",
        "fullName": "Rep. Green, Al [D-TX-9]",
        "lastName": "Green",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Representative Green's Original Legislation to increase from 9 to 13 the number of justices of the Supreme Court.",
    "type": "HR",
    "updateDate": "2026-05-21T15:08:36Z",
    "updateDateIncludingText": "2026-05-21T15:08:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-04",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-04",
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
          "date": "2026-05-04T14:32:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8647ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8647\nIN THE HOUSE OF REPRESENTATIVES\nMay 4, 2026 Mr. Green of Texas introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nRepresentative Green\u2019s Original Legislation to increase from 9 to 13 the number of justices of the Supreme Court.\n#### 1. Expansion of the supreme court\nSection 1 of title 28, United States Code, is amended\u2014\n**(1)**\nby striking eight and inserting twelve ; and\n**(2)**\nby striking six and inserting eight .",
      "versionDate": "2026-05-04",
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
        "name": "Law",
        "updateDate": "2026-05-21T15:08:35Z"
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
      "date": "2026-05-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8647ih.xml"
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
      "title": "Representative Green's Original Legislation to increase from 9 to 13 the number of justices of the Supreme Court.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-09T05:18:36Z"
    },
    {
      "title": "Representative Green's Original Legislation to increase from 9 to 13 the number of justices of the Supreme Court.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T08:05:48Z"
    }
  ]
}
```
