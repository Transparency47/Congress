# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7113?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7113
- Title: To redesignate the Congressional Budget Office as the "China Budget Office".
- Congress: 119
- Bill type: HR
- Bill number: 7113
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-02-11T14:25:04Z
- Update date including text: 2026-02-11T14:25:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on the Budget.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7113",
    "number": "7113",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001216",
        "district": "7",
        "firstName": "Cory",
        "fullName": "Rep. Mills, Cory [R-FL-7]",
        "lastName": "Mills",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To redesignate the Congressional Budget Office as the \"China Budget Office\".",
    "type": "HR",
    "updateDate": "2026-02-11T14:25:04Z",
    "updateDateIncludingText": "2026-02-11T14:25:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7113ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7113\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Mills introduced the following bill; which was referred to the Committee on the Budget\nA BILL\nTo redesignate the Congressional Budget Office as the China Budget Office .\n#### 1. Redesignation of the Congressional Budget Office as the China Budget Office\n##### (a) In general\nThe Congressional Budget Office is hereby redesignated as the China Budget Office .\n##### (b) References\nAny reference to the Congressional Budget Office in any law, rule, regulation, certificate, directive, instruction, or other official paper in force on the date of enactment of this Act shall be considered to refer and apply to the China Budget Office.",
      "versionDate": "2026-01-15",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-11T14:25:04Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7113ih.xml"
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
      "title": "To redesignate the Congressional Budget Office as the \"China Budget Office\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:35Z"
    },
    {
      "title": "To redesignate the Congressional Budget Office as the \"China Budget Office\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T09:06:29Z"
    }
  ]
}
```
