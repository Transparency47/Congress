# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8071?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8071
- Title: Strengthening and Improving Mobilization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8071
- Origin chamber: House
- Introduced date: 2026-03-25
- Update date: 2026-04-25T15:56:20Z
- Update date including text: 2026-04-25T15:56:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-25: Introduced in House

## Actions

- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8071",
    "number": "8071",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "Strengthening and Improving Mobilization Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-25T15:56:20Z",
    "updateDateIncludingText": "2026-04-25T15:56:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T14:02:30Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8071ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8071\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2026 Mr. Green of Texas introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Defense Production Act of 1950 to require the Defense Production Act Committee to conduct discussion-based simulations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening and Improving Mobilization Act of 2026 .\n#### 2. Discussion-based simulations\nTitle III of the Defense Production Act of 1950 ( 50 U.S.C. 4531 et seq. ) is amended by adding at the end the following:\n306. Discussion-based simulations At least once every 5 years, the Defense Production Act Committee shall conduct a discussion-based simulation (commonly known as a table-top exercise ) to determine the resources needed and the best use of the authorities under title I and this title. .\n#### 3. Short title correction\nThe first undesignated section of the the Defense Production Act of 1950 is amended, effective on the date of enactment of such Act, by striking cited as \u201cthe Defense and inserting cited as the \u201cDefense .",
      "versionDate": "2026-03-25",
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
        "updateDate": "2026-04-20T23:34:40Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8071ih.xml"
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
      "title": "Strengthening and Improving Mobilization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T06:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening and Improving Mobilization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T06:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Defense Production Act of 1950 to require the Defense Production Act Committee to conduct a discussion-based simulations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T06:18:46Z"
    }
  ]
}
```
