# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/976?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/976
- Title: Providing for the hour of meeting of the House.
- Congress: 119
- Bill type: HRES
- Bill number: 976
- Origin chamber: House
- Introduced date: 2026-01-06
- Update date: 2026-01-12T15:53:07Z
- Update date including text: 2026-01-12T15:53:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-06: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 19:01:45 - Floor: Considered as privileged matter. (consideration: CR H4)
- 2026-01-06 19:02:03 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H4)
- 2026-01-06 19:02:03 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H4)
- 2026-01-06 19:02:25 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2026-01-06: Introduced in House

## Actions

- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 19:01:45 - Floor: Considered as privileged matter. (consideration: CR H4)
- 2026-01-06 19:02:03 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H4)
- 2026-01-06 19:02:03 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H4)
- 2026-01-06 19:02:25 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-06",
    "latestAction": {
      "actionDate": "2026-01-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/976",
    "number": "976",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Providing for the hour of meeting of the House.",
    "type": "HRES",
    "updateDate": "2026-01-12T15:53:07Z",
    "updateDateIncludingText": "2026-01-12T15:53:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2026-01-06",
      "actionTime": "19:02:25",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2026-01-06",
      "actionTime": "19:02:03",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H4)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2026-01-06",
      "actionTime": "19:02:03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H4)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2026-01-06",
      "actionTime": "19:01:45",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H4)",
      "type": "Floor"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-06",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres976eh.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 976\nIn the House of Representatives, U. S.,\nJanuary 6, 2026\nRESOLUTION\nProviding for the hour of meeting of the House.\nThat unless otherwise ordered, the hour of daily meeting of the House shall be 2 p.m. on Mondays; noon on Tuesdays (or 2 p.m. if no legislative business was conducted on the preceding Monday); noon on Wednesdays and Thursdays; and 9 a.m. on all other days of the week.",
      "versionDate": "2026-01-06",
      "versionType": "EH"
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
        "actionDate": "2025-01-03",
        "actionTime": "18:13:30",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "6",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fixing the daily hour of meeting of the First Session of the One Hundred Nineteenth Congress.",
      "type": "HRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "House of Representatives",
            "updateDate": "2026-01-12T15:53:07Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2026-01-12T15:52:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2026-01-09T13:10:56Z"
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
      "date": "2026-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres976eh.xml"
        }
      ],
      "type": "EH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Providing for the hour of meeting of the House.",
      "titleType": "Official Titles from EH (Engrossed in House) bill text",
      "titleTypeCode": "259",
      "updateDate": "2026-01-08T06:08:16Z"
    },
    {
      "title": "Providing for the hour of meeting of the House.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T09:05:47Z"
    },
    {
      "title": "Providing for the hour of meeting of the House.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-07T09:05:47Z"
    }
  ]
}
```
