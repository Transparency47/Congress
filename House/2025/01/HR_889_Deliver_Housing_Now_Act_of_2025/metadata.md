# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/889?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/889
- Title: Deliver Housing Now Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 889
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-04-07T14:42:15Z
- Update date including text: 2025-04-07T14:42:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/889",
    "number": "889",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000579",
        "district": "18",
        "firstName": "Patrick",
        "fullName": "Rep. Ryan, Patrick [D-NY-18]",
        "lastName": "Ryan",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Deliver Housing Now Act of 2025",
    "type": "HR",
    "updateDate": "2025-04-07T14:42:15Z",
    "updateDateIncludingText": "2025-04-07T14:42:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:08:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr889ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 889\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Ryan introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Omnibus Consolidated Rescissions and Appropriations Act of 1996 to remove the limit on the number of public housing agencies the Secretary of Housing and Urban Development may add to the moving to work demonstration program.\n#### 1. Short title\nThis Act may be cited as the Deliver Housing Now Act of 2025 .\n#### 2. Removal of limit on number of public housing agencies that may be added to moving to work demonstration program\nSection 204(b) of the Omnibus Consolidated Rescissions and Appropriations Act of 1996 ( 42 U.S.C. 1437f note) is amended by striking up to 30 and inserting not less than 15 .",
      "versionDate": "2025-01-31",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employment and training programs",
            "updateDate": "2025-04-07T14:42:15Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2025-04-07T14:42:09Z"
          },
          {
            "name": "Low- and moderate-income housing",
            "updateDate": "2025-04-07T14:41:55Z"
          },
          {
            "name": "Public housing",
            "updateDate": "2025-04-07T14:42:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-03-04T17:13:01Z"
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
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr889ih.xml"
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
      "title": "Deliver Housing Now Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deliver Housing Now Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Consolidated Rescissions and Appropriations Act of 1996 to remove the limit on the number of public housing agencies the Secretary of Housing and Urban Development may add to the moving to work demonstration program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:32Z"
    }
  ]
}
```
