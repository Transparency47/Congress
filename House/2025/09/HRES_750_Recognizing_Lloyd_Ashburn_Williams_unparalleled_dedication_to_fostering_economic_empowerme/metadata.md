# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/750?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/750
- Title: Recognizing Lloyd Ashburn Williams' unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.
- Congress: 119
- Bill type: HRES
- Bill number: 750
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2025-09-24T16:42:02Z
- Update date including text: 2025-09-24T16:42:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-19 - IntroReferral: Submitted in House
- 2025-09-19 - IntroReferral: Submitted in House
- Latest action: 2025-09-19: Submitted in House

## Actions

- 2025-09-19 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-19 - IntroReferral: Submitted in House
- 2025-09-19 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/750",
    "number": "750",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "E000297",
        "district": "13",
        "firstName": "Adriano",
        "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
        "lastName": "Espaillat",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Recognizing Lloyd Ashburn Williams' unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.",
    "type": "HRES",
    "updateDate": "2025-09-24T16:42:02Z",
    "updateDateIncludingText": "2025-09-24T16:42:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-19",
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
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T13:04:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres750ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 750\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Mr. Espaillat submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nRecognizing Lloyd Ashburn Williams\u2019 unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.\nThat the House of Representatives recognizes Lloyd Ashburn Williams\u2019 unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.",
      "versionDate": "2025-09-19",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-09-24T16:42:02Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres750ih.xml"
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
      "title": "Recognizing Lloyd Ashburn Williams' unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-22T17:41:00Z"
    },
    {
      "title": "Recognizing Lloyd Ashburn Williams' unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-22T15:31:48Z"
    }
  ]
}
```
