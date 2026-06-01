# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/325?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/325
- Title: Commemorating the 100th anniversary of the city of Hialeah, Florida.
- Congress: 119
- Bill type: HRES
- Bill number: 325
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2025-05-22T18:24:52Z
- Update date including text: 2025-05-22T18:24:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-04-10 - IntroReferral: Submitted in House
- 2025-04-10 - IntroReferral: Submitted in House
- Latest action: 2025-04-10: Submitted in House

## Actions

- 2025-04-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-04-10 - IntroReferral: Submitted in House
- 2025-04-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/325",
    "number": "325",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "D000600",
        "district": "26",
        "firstName": "Mario",
        "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
        "lastName": "Diaz-Balart",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Commemorating the 100th anniversary of the city of Hialeah, Florida.",
    "type": "HRES",
    "updateDate": "2025-05-22T18:24:52Z",
    "updateDateIncludingText": "2025-05-22T18:24:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:01:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres325ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 325\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Diaz-Balart submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nCommemorating the 100th anniversary of the city of Hialeah, Florida.\nThat the House of Representatives\u2014\n**(1)**\ncongratulates the city of Hialeah on the occasion of its 100th anniversary;\n**(2)**\nrecognizes and appreciates the significant economic and cultural impact of the city of Hialeah on the South Florida region and the United States as a whole; and\n**(3)**\ncommends and honors the people of Hialeah for their unique and significant contributions to the prosperity, culture, and history of the United States.",
      "versionDate": "2025-04-10",
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
        "updateDate": "2025-05-22T18:24:52Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres325ih.xml"
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
      "title": "Commemorating the 100th anniversary of the city of Hialeah, Florida.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T08:18:18Z"
    },
    {
      "title": "Commemorating the 100th anniversary of the city of Hialeah, Florida.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T08:06:38Z"
    }
  ]
}
```
