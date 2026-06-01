# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4561?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4561
- Title: SUE Act
- Congress: 119
- Bill type: HR
- Bill number: 4561
- Origin chamber: House
- Introduced date: 2025-07-21
- Update date: 2025-09-11T14:16:05Z
- Update date including text: 2025-09-11T14:16:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-07-21: Introduced in House

## Actions

- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4561",
    "number": "4561",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000484",
        "district": "6",
        "firstName": "Randy",
        "fullName": "Rep. Fine, Randy [R-FL-6]",
        "lastName": "Fine",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "SUE Act",
    "type": "HR",
    "updateDate": "2025-09-11T14:16:05Z",
    "updateDateIncludingText": "2025-09-11T14:16:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-21",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T16:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4561ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4561\nIN THE HOUSE OF REPRESENTATIVES\nJuly 21, 2025 Mr. Fine introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo prohibit the use of Federal funds to pay for a subscription to the Wall Street Journal for Members of Congress, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Unnecessary Expenditures Act or the SUE Act .\n#### 2. Prohibition with respect to use of certain funds for Wall Street Journal subscription\n##### (a) In general\nNotwithstanding any other provision of law, no Federal funds may be used to pay for a subscription to the Wall Street Journal for any office of a Member of Congress (including a Delegate or Resident Commissioner to the Congress) or for any committee of Congress.\n##### (b) Effective date\nThis section shall apply with respect to fiscal year 2025 and each succeeding fiscal year.",
      "versionDate": "2025-07-21",
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
        "name": "Congress",
        "updateDate": "2025-09-11T14:16:05Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4561ih.xml"
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
      "title": "SUE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SUE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Unnecessary Expenditures Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of Federal funds to pay for a subscription to the Wall Street Journal for Members of Congress, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:42Z"
    }
  ]
}
```
