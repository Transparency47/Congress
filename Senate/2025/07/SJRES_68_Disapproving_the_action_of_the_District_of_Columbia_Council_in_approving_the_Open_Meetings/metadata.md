# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/68?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/68
- Title: A joint resolution disapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.
- Congress: 119
- Bill type: SJRES
- Bill number: 68
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2025-12-05T21:32:35Z
- Update date including text: 2025-12-05T21:32:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/68",
    "number": "68",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A joint resolution disapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.",
    "type": "SJRES",
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
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-07-23T18:18:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres68is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 68\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Lee introduced the following joint resolution; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nJOINT RESOLUTION\nDisapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.\nThat the Congress disapproves of the action of the District of Columbia Council described as follows: The Open Meetings Clarification Temporary Amendment Act of 2025 (D.C. Act 26\u201386), enacted by the Council of the District of Columbia on June 26, 2025, and transmitted to Congress pursuant to section 602(c)(1) of the District of Columbia Home Rule Act on July 7, 2025.",
      "versionDate": "2025-07-23",
      "versionType": "IS"
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
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "109",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Disapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.",
      "type": "HJRES"
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
        "updateDate": "2025-07-30T23:04:33Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres68is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution disapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T02:18:33Z"
    },
    {
      "title": "A joint resolution disapproving the action of the District of Columbia Council in approving the Open Meetings Clarification Temporary Amendment Act of 2025.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T10:56:26Z"
    }
  ]
}
```
