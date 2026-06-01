# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1293?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1293
- Title: Recognizing and celebrating "National Salvation Army Week" on May 11 through May 17, 2026.
- Congress: 119
- Bill type: HRES
- Bill number: 1293
- Origin chamber: House
- Introduced date: 2026-05-15
- Update date: 2026-05-29T15:55:21Z
- Update date including text: 2026-05-29T15:55:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-15: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-15 - IntroReferral: Submitted in House
- Latest action: 2026-05-15: Submitted in House

## Actions

- 2026-05-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-15",
    "latestAction": {
      "actionDate": "2026-05-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1293",
    "number": "1293",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "D000230",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Davis, Donald G. [D-NC-1]",
        "lastName": "Davis",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Recognizing and celebrating \"National Salvation Army Week\" on May 11 through May 17, 2026.",
    "type": "HRES",
    "updateDate": "2026-05-29T15:55:21Z",
    "updateDateIncludingText": "2026-05-29T15:55:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-15",
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
      "actionDate": "2026-05-15",
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
          "date": "2026-05-15T13:03:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1293ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1293\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2026 Mr. Davis of North Carolina submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nRecognizing and celebrating National Salvation Army Week on May 11 through May 17, 2026.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes and celebrates National Salvation Army Week ;\n**(2)**\ncommends the Salvation Army for its historic and ongoing efforts to uplift and serve individuals and families across the country; and\n**(3)**\nencourages all Americans to join in acts of service and generosity, supporting the Salvation Army\u2019s goal to combat human need with love and compassion, wherever it persists.",
      "versionDate": "2026-05-15",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-13",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "404",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing and celebrating \"National Salvation Army Week\" on May 12 through May 18, 2025.",
      "type": "HRES"
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
        "updateDate": "2026-05-29T15:55:20Z"
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
      "date": "2026-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1293ih.xml"
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
      "title": "Recognizing and celebrating \"National Salvation Army Week\" on May 11 through May 17, 2026.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-18T13:33:28Z"
    },
    {
      "title": "Recognizing and celebrating \"National Salvation Army Week\" on May 11 through May 17, 2026.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-16T08:06:55Z"
    }
  ]
}
```
