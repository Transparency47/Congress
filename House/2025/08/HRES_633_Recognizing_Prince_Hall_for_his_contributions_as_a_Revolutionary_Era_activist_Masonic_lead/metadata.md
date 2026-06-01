# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/633?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/633
- Title: Original Resolution Honoring Prince Hall
- Congress: 119
- Bill type: HRES
- Bill number: 633
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2025-09-17T16:13:27Z
- Update date including text: 2025-09-17T16:13:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-08-05 - IntroReferral: Submitted in House
- 2025-08-05 - IntroReferral: Submitted in House
- Latest action: 2025-08-05: Submitted in House

## Actions

- 2025-08-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-08-05 - IntroReferral: Submitted in House
- 2025-08-05 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/633",
    "number": "633",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "G000553",
        "district": "9",
        "firstName": "Al",
        "fullName": "Rep. Green, Al [D-TX-9]",
        "lastName": "Green",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Original Resolution Honoring Prince Hall",
    "type": "HRES",
    "updateDate": "2025-09-17T16:13:27Z",
    "updateDateIncludingText": "2025-09-17T16:13:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres633ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 633\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mr. Green of Texas submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing Prince Hall for his contributions as a Revolutionary Era activist, Masonic leader, and his lasting impact in the African-American fight for justice.\nThat the House of Representatives recognizes and thanks Prince Hall for his contributions as a Revolutionary Era activist and Masonic leader, as well as for his lasting impact in the African-American fight for justice.",
      "versionDate": "2025-08-05",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-09-17T16:13:27Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres633ih.xml"
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
      "title": "Original Resolution Honoring Prince Hall",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T15:58:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Original Resolution Honoring Prince Hall",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T15:58:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Recognizing Prince Hall for his contributions as a Revolutionary Era activist, Masonic leader, and his lasting impact in the African-American fight for justice.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T08:19:02Z"
    }
  ]
}
```
