# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/940?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/940
- Title: Electing a Member to certain standing committees of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 940
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2025-12-18T16:02:20Z
- Update date including text: 2025-12-18T16:02:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 21:24:28 - Floor: Considered as privileged matter. (consideration: CR H5555)
- 2025-12-10 21:24:44 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H5555)
- 2025-12-10 21:24:44 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.
- 2025-12-10 21:24:48 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 21:24:28 - Floor: Considered as privileged matter. (consideration: CR H5555)
- 2025-12-10 21:24:44 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H5555)
- 2025-12-10 21:24:44 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.
- 2025-12-10 21:24:48 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/940",
    "number": "940",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Electing a Member to certain standing committees of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-12-18T16:02:20Z",
    "updateDateIncludingText": "2025-12-18T16:02:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-12-10",
      "actionTime": "21:24:48",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-12-10",
      "actionTime": "21:24:44",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H5555)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-12-10",
      "actionTime": "21:24:44",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-12-10",
      "actionTime": "21:24:28",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H5555)",
      "type": "Floor"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres940eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 940\nIn the House of Representatives, U. S.,\nDecember 10, 2025\nRESOLUTION\nThat the following named Member be, and is hereby, elected to the following standing committees of the House of Representatives:\nCommittee on Homeland Security:\nMr. Van Epps.\nCommittee on Science, Space, and Technology:\nMr. Van Epps.",
      "versionDate": "2025-12-10",
      "versionType": "EH"
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
            "name": "Congressional committees",
            "updateDate": "2025-12-18T16:02:20Z"
          },
          {
            "name": "House Committee on Homeland Security",
            "updateDate": "2025-12-18T16:01:36Z"
          },
          {
            "name": "House Committee on Science, Space, and Technology",
            "updateDate": "2025-12-18T16:01:28Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-12-18T16:01:08Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-12-18T16:01:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-12-15T15:33:17Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres940eh.xml"
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
      "title": "Electing a Member to certain standing committees of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T09:07:47Z"
    },
    {
      "title": "Electing a Member to certain standing committees of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-11T09:07:47Z"
    }
  ]
}
```
