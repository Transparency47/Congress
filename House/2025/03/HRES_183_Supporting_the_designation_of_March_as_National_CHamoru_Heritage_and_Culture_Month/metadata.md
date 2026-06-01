# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/183?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/183
- Title: Supporting the designation of March as National CHamoru Heritage and Culture Month.
- Congress: 119
- Bill type: HRES
- Bill number: 183
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2025-05-14T12:21:05Z
- Update date including text: 2025-05-14T12:21:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-03 - Committee: Submitted in House
- Latest action: 2025-03-03: Submitted in House

## Actions

- 2025-03-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-03 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/183",
    "number": "183",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "Supporting the designation of March as National CHamoru Heritage and Culture Month.",
    "type": "HRES",
    "updateDate": "2025-05-14T12:21:05Z",
    "updateDateIncludingText": "2025-05-14T12:21:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionCode": "H12100",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-03-03T17:02:35Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres183ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 183\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Moylan submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nSupporting the designation of March as National CHamoru Heritage and Culture Month.\nThat the House of Representatives acknowledges the contributions and achievements of the CHamoru people and encourages the people of the United States to observe National CHamoru Heritage and Culture Month.",
      "versionDate": "2025-03-03",
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
        "updateDate": "2025-05-14T12:21:05Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres183ih.xml"
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
      "title": "Supporting the designation of March as National CHamoru Heritage and Culture Month.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:26Z"
    },
    {
      "title": "Supporting the designation of March as National CHamoru Heritage and Culture Month.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T09:06:03Z"
    }
  ]
}
```
