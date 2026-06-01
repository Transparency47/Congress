# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/207?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/207
- Title: Recognizing and commemorating the contributions of contemporary Latinas in the State of Illinois.
- Congress: 119
- Bill type: HRES
- Bill number: 207
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-03-12T13:22:03Z
- Update date including text: 2025-03-12T13:22:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-10 - IntroReferral: Submitted in House
- 2025-03-10 - IntroReferral: Submitted in House
- Latest action: 2025-03-10: Submitted in House

## Actions

- 2025-03-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-10 - IntroReferral: Submitted in House
- 2025-03-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/207",
    "number": "207",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000617",
        "district": "3",
        "firstName": "Delia",
        "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
        "lastName": "Ramirez",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Recognizing and commemorating the contributions of contemporary Latinas in the State of Illinois.",
    "type": "HRES",
    "updateDate": "2025-03-12T13:22:03Z",
    "updateDateIncludingText": "2025-03-12T13:22:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:00:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres207ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 207\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mrs. Ramirez submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nRecognizing and commemorating the contributions of contemporary Latinas in the State of Illinois.\nThat the House of Representatives\u2014\n**(1)**\ncelebrates the impact and contributions of contemporary Latinas in the State of Illinois;\n**(2)**\nacknowledges the value of Latinas and the essential role they play in this Nation\u2019s multicultural, multigenerational democracy; and\n**(3)**\nrecognizes the importance of accurate and timely data on Latinas living in the United States and the role that the United States Census Bureau plays in delivering data that impacts the political and economic power and influence of Latinas.",
      "versionDate": "2025-03-10",
      "versionType": "IH"
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
        "name": "Health",
        "updateDate": "2025-03-12T13:22:03Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres207ih.xml"
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
      "title": "Recognizing and commemorating the contributions of contemporary Latinas in the State of Illinois.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T08:48:23Z"
    },
    {
      "title": "Recognizing and commemorating the contributions of contemporary Latinas in the State of Illinois.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T08:07:03Z"
    }
  ]
}
```
