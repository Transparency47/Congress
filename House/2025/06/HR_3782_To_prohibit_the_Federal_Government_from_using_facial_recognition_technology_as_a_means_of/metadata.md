# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3782?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3782
- Title: To prohibit the Federal Government from using facial recognition technology as a means of identity verification, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 3782
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2025-07-18T13:06:09Z
- Update date including text: 2025-07-18T13:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3782",
    "number": "3782",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "To prohibit the Federal Government from using facial recognition technology as a means of identity verification, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-07-18T13:06:09Z",
    "updateDateIncludingText": "2025-07-18T13:06:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:04:30Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3782ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3782\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Ogles introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the Federal Government from using facial recognition technology as a means of identity verification, and for other purposes.\n#### 1. Prohibition on certain Federal Government use of facial recognition technology\n##### (a) In general\nAn agency of the Federal Government may not use facial recognition technology as a means of identity verification.\n##### (b) Facial recognition technology defined\nIn this section, the term facial recognition technology means a contemporary security system that automatically identifies and verifies the identity of an individual from a digital image or video frame.",
      "versionDate": "2025-06-05",
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
        "updateDate": "2025-07-18T13:06:09Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3782ih.xml"
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
      "title": "To prohibit the Federal Government from using facial recognition technology as a means of identity verification, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T06:18:36Z"
    },
    {
      "title": "To prohibit the Federal Government from using facial recognition technology as a means of identity verification, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-06T08:06:40Z"
    }
  ]
}
```
