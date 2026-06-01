# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1262?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1262
- Title: Recognizing and congratulating the Martinsville Missile's land speed record for a stock car.
- Congress: 119
- Bill type: HRES
- Bill number: 1262
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-12T19:59:23Z
- Update date including text: 2026-05-12T19:59:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-07 - IntroReferral: Submitted in House
- Latest action: 2026-05-07: Submitted in House

## Actions

- 2026-05-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-07 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1262",
    "number": "1262",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000568",
        "district": "9",
        "firstName": "H.",
        "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
        "lastName": "Griffith",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Recognizing and congratulating the Martinsville Missile's land speed record for a stock car.",
    "type": "HRES",
    "updateDate": "2026-05-12T19:59:23Z",
    "updateDateIncludingText": "2026-05-12T19:59:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "actionCode": "1025",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
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
          "date": "2026-05-07T13:06:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1262ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1262\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Griffith submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nRecognizing and congratulating the Martinsville Missile\u2019s land speed record for a stock car.\nThat the House of Representatives extends its congratulations to the VA250 Car Project\u2019s record-setting land speed record for a stock car of 253 miles per hour.",
      "versionDate": "2026-05-07",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-12T19:59:23Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1262ih.xml"
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
      "title": "Recognizing and congratulating the Martinsville Missile's land speed record for a stock car.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T08:18:32Z"
    },
    {
      "title": "Recognizing and congratulating the Martinsville Missile's land speed record for a stock car.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T08:05:59Z"
    }
  ]
}
```
