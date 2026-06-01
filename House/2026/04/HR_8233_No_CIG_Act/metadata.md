# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8233?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8233
- Title: No CIG Act
- Congress: 119
- Bill type: HR
- Bill number: 8233
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-04-14T19:36:40Z
- Update date including text: 2026-04-14T19:36:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8233",
    "number": "8233",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "No CIG Act",
    "type": "HR",
    "updateDate": "2026-04-14T19:36:40Z",
    "updateDateIncludingText": "2026-04-14T19:36:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
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
          "date": "2026-04-09T15:34:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8233ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8233\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Perry introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to repeal public transportation fixed guideway capital investment grants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No CIG Act .\n#### 2. Fixed guideway capital investment grants\n##### (a) In general\nSection 5309 of title 49, United States Code, and the item relating to such section in the analysis for chapter 53 of such title, are repealed.\n##### (b) Conforming amendments\nSection 5338 of title 49, United States Code, is amended\u2014\n**(1)**\nby repealing subsection (b); and\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nby striking subparagraph (C); and\n**(B)**\nby redesignating subparagraph (D) as subparagraph (C).",
      "versionDate": "2026-04-09",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-04-14T19:36:40Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8233ih.xml"
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
      "title": "No CIG Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No CIG Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to repeal public transportation fixed guideway capital investment grants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:33Z"
    }
  ]
}
```
