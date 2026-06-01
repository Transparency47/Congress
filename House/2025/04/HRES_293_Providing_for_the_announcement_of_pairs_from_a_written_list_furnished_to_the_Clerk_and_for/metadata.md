# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/293?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/293
- Title: Providing for the announcement of pairs from a written list furnished to the Clerk, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 293
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2025-10-09T00:11:26Z
- Update date including text: 2025-10-09T00:11:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Rules.
- 2025-04-07 - IntroReferral: Submitted in House
- 2025-04-07 - IntroReferral: Submitted in House
- 2025-04-08 15:23:30 - Floor: Passed/agreed to in House: Pursuant to the provisions of H. Res. 294, H. Res. 293 is considered passed House.
- 2025-04-08 15:23:30 - Floor: Pursuant to the provisions of H. Res. 294, H. Res. 293 is considered passed House. (consideration: CR H1481: 1; text: CR H1481)
- Latest action: 2025-04-07: Submitted in House

## Actions

- 2025-04-07 - IntroReferral: Referred to the House Committee on Rules.
- 2025-04-07 - IntroReferral: Submitted in House
- 2025-04-07 - IntroReferral: Submitted in House
- 2025-04-08 15:23:30 - Floor: Passed/agreed to in House: Pursuant to the provisions of H. Res. 294, H. Res. 293 is considered passed House.
- 2025-04-08 15:23:30 - Floor: Pursuant to the provisions of H. Res. 294, H. Res. 293 is considered passed House. (consideration: CR H1481: 1; text: CR H1481)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/293",
    "number": "293",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "L000596",
        "district": "13",
        "firstName": "Anna Paulina",
        "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
        "lastName": "Luna",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Providing for the announcement of pairs from a written list furnished to the Clerk, and for other purposes.",
    "type": "HRES",
    "updateDate": "2025-10-09T00:11:26Z",
    "updateDateIncludingText": "2025-10-09T00:11:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H1B000",
      "actionDate": "2025-04-08",
      "actionTime": "15:23:30",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Pursuant to the provisions of H. Res. 294, H. Res. 293 is considered passed House. (consideration: CR H1481: 1; text: CR H1481)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-04-08",
      "actionTime": "15:23:30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: Pursuant to the provisions of H. Res. 294, H. Res. 293 is considered passed House.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-04-07T16:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres293ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 293\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mrs. Luna submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for the announcement of pairs from a written list furnished to the Clerk, and for other purposes.\n#### 1. Announcement of pairs from a written list furnished to the Clerk\nDuring the One Hundred Nineteenth Congress, pairs shall be announced by the Clerk immediately before the announcement by the Chair of the result of the vote by the House or the Committee of the Whole from a written list furnished to the Clerk, and signed by the Member making the statement to the Clerk, which list shall be published in the Congressional Record as a part of the proceedings, immediately following the names of those not voting. However, pairs shall be announced but once during the same legislative day.",
      "versionDate": "2025-04-07",
      "versionType": "IH"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres293eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 293\nIn the House of Representatives, U. S.,\nApril 8, 2025\nRESOLUTION\nProviding for the announcement of pairs from a written list furnished to the Clerk, and for other purposes.\n#### 1. Announcement of pairs from a written list furnished to the Clerk\nDuring the One Hundred Nineteenth Congress, pairs shall be announced by the Clerk immediately before the announcement by the Chair of the result of the vote by the House or the Committee of the Whole from a written list furnished to the Clerk, and signed by the Member making the statement to the Clerk, which list shall be published in the Congressional Record as a part of the proceedings, immediately following the names of those not voting. However, pairs shall be announced but once during the same legislative day.",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-04-08",
        "actionTime": "15:23:14",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "294",
      "relationshipDetails": {
        "item": [
          {
            "identifiedBy": "House",
            "type": "Procedurally related"
          },
          {
            "identifiedBy": "House",
            "type": "Procedurally related"
          }
        ]
      },
      "title": "Providing for consideration of the joint resolution (S.J. Res. 18) disapproving the rule submitted by the Bureau of Consumer Financial Protection relating to \"Overdraft Lending: Very Large Financial Institutions\"; providing for consideration of the joint resolution (S.J. Res. 28) disapproving the rule submitted by the Bureau of Consumer Financial Protection relating to \"Defining Larger Participants of a Market for General-Use Digital Consumer Payment Applications\"; providing for consideration of the bill (H.R. 1526) to amend title 28, United States Code, to limit the authority of district courts to provide injunctive relief, and for other purposes; providing for consideration of the bill (H.R. 22) to amend the National Voter Registration Act of 1993 to require proof of United States citizenship to register an individual to vote in elections for Federal office, and for other purposes; and for other purposes.",
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
            "updateDate": "2025-06-02T15:38:01Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-06-02T15:38:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-05-23T14:17:30Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres293ih.xml"
        }
      ],
      "type": "IH"
    },
    {
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres293eh.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for the announcement of pairs from a written list furnished to the Clerk, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T10:48:16Z"
    },
    {
      "title": "Providing for the announcement of pairs from a written list furnished to the Clerk, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T08:05:30Z"
    }
  ]
}
```
