# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4260?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4260
- Title: To ensure the appropriate administration of the Impact Aid program.
- Congress: 119
- Bill type: HR
- Bill number: 4260
- Origin chamber: House
- Introduced date: 2025-06-30
- Update date: 2025-07-30T13:53:48Z
- Update date including text: 2025-07-30T13:53:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-30: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-06-30: Introduced in House

## Actions

- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-30",
    "latestAction": {
      "actionDate": "2025-06-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4260",
    "number": "4260",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
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
    "title": "To ensure the appropriate administration of the Impact Aid program.",
    "type": "HR",
    "updateDate": "2025-07-30T13:53:48Z",
    "updateDateIncludingText": "2025-07-30T13:53:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-30",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-30",
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
          "date": "2025-06-30T18:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4260ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4260\nIN THE HOUSE OF REPRESENTATIVES\nJune 30, 2025 Mr. Ryan introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo ensure the appropriate administration of the Impact Aid program.\n#### 1. Ensuring appropriate administration of the Impact Aid program\n##### (a) In general\nThe Secretary of Education may not significantly alter the administration of the Impact Aid program under title VII of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7701 et seq. ) by the Department of Education from how such program was carried out on January 1, 2025, except as required by Federal law or a court order.\n##### (b) Annual certification\nNot later than 30 days after the date of enactment of this Act, and annually thereafter, the Secretary shall certify to Congress that the Secretary is in compliance with the requirement established under subsection (a).",
      "versionDate": "2025-06-30",
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
        "name": "Education",
        "updateDate": "2025-07-30T13:53:48Z"
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
      "date": "2025-06-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4260ih.xml"
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
      "title": "To ensure the appropriate administration of the Impact Aid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T04:48:28Z"
    },
    {
      "title": "To ensure the appropriate administration of the Impact Aid program.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-01T08:05:26Z"
    }
  ]
}
```
