# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/109?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/109
- Title: Disapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.
- Congress: 119
- Bill type: HJRES
- Bill number: 109
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-12-05T21:32:35Z
- Update date including text: 2025-12-05T21:32:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/109",
    "number": "109",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Disapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.",
    "type": "HJRES",
    "updateDate": "2025-12-05T21:32:35Z",
    "updateDateIncludingText": "2025-12-05T21:32:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:07:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres109ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 109\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Hageman submitted the following joint resolution; which was referred to the Committee on Oversight and Government Reform\nJOINT RESOLUTION\nDisapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.\nThat the Congress disapproves of the action of the District of Columbia Council described as follows: The Open Meetings Clarification Temporary Amendment Act of 2025 (D.C. Act 26\u201386), enacted by the Council of the District of Columbia on June 26, 2025, and transmitted to Congress pursuant to section 602(c)(1) of the District of Columbia Home Rule Act on July 7, 2025.",
      "versionDate": "2025-07-23",
      "versionType": "IH"
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
        "actionDate": "2025-07-23",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "68",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution disapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.",
      "type": "SJRES"
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
        "updateDate": "2025-07-30T23:05:06Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres109ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Disapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T04:48:35Z"
    },
    {
      "title": "Disapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T08:06:05Z"
    }
  ]
}
```
