# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/640?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/640
- Title: Recognizing the significance of "Chicano/Chicana Heritage Month" in August as an important time to celebrate the significant contributions of Mexican Americans to the history of the United States.
- Congress: 119
- Bill type: HRES
- Bill number: 640
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2025-09-18T19:32:09Z
- Update date including text: 2025-09-18T19:32:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-08-08 - IntroReferral: Submitted in House
- 2025-08-08 - IntroReferral: Submitted in House
- Latest action: 2025-08-08: Submitted in House

## Actions

- 2025-08-08 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-08-08 - IntroReferral: Submitted in House
- 2025-08-08 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/640",
    "number": "640",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001110",
        "district": "46",
        "firstName": "J.",
        "fullName": "Rep. Correa, J. Luis [D-CA-46]",
        "lastName": "Correa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Recognizing the significance of \"Chicano/Chicana Heritage Month\" in August as an important time to celebrate the significant contributions of Mexican Americans to the history of the United States.",
    "type": "HRES",
    "updateDate": "2025-09-18T19:32:09Z",
    "updateDateIncludingText": "2025-09-18T19:32:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
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
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:33:50Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres640ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 640\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Correa submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nRecognizing the significance of Chicano/Chicana Heritage Month in August as an important time to celebrate the significant contributions of Mexican Americans to the history of the United States.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the significance of Chicano/Chicana Heritage Month as an important time to celebrate the significant contributions of Mexican Americans to the history of the United States;\n**(2)**\nrecognizes that Mexican Americans enhance the rich diversity of and strengthen the United States; and\n**(3)**\nacknowledges Chicano/Chicana Heritage Month and encourages its observation with appropriate events and activities.",
      "versionDate": "2025-08-08",
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
        "name": "Immigration",
        "updateDate": "2025-09-18T19:32:09Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres640ih.xml"
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
      "title": "Recognizing the significance of \"Chicano/Chicana Heritage Month\" in August as an important time to celebrate the significant contributions of Mexican Americans to the history of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T08:18:20Z"
    },
    {
      "title": "Recognizing the significance of \"Chicano/Chicana Heritage Month\" in August as an important time to celebrate the significant contributions of Mexican Americans to the history of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T08:05:31Z"
    }
  ]
}
```
