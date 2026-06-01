# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/54?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/54
- Title: Expressing support for designation of the first Friday of October as "Manufacturing Day".
- Congress: 119
- Bill type: HCONRES
- Bill number: 54
- Origin chamber: House
- Introduced date: 2025-10-03
- Update date: 2025-12-15T16:56:39Z
- Update date including text: 2025-12-15T16:56:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-03: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-10-03 - IntroReferral: Submitted in House
- 2025-10-03 - IntroReferral: Submitted in House
- Latest action: 2025-10-03: Submitted in House

## Actions

- 2025-10-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-10-03 - IntroReferral: Submitted in House
- 2025-10-03 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/54",
    "number": "54",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for designation of the first Friday of October as \"Manufacturing Day\".",
    "type": "HCONRES",
    "updateDate": "2025-12-15T16:56:39Z",
    "updateDateIncludingText": "2025-12-15T16:56:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-03",
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
          "date": "2025-10-03T19:32:10Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres54ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 54\nIN THE HOUSE OF REPRESENTATIVES\nOctober 3, 2025 Mrs. Torres of California (for herself and Mr. Fleischmann ) submitted the following concurrent resolution; which was referred to the Committee on Oversight and Government Reform\nCONCURRENT RESOLUTION\nExpressing support for designation of the first Friday of October as Manufacturing Day .\nThat Congress supports the designation of Manufacturing Day .",
      "versionDate": "2025-10-03",
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
        "name": "Commerce",
        "updateDate": "2025-12-15T16:56:39Z"
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
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres54ih.xml"
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
      "title": "Expressing support for designation of the first Friday of October as \"Manufacturing Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:12Z"
    },
    {
      "title": "Expressing support for designation of the first Friday of October as \"Manufacturing Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T08:05:42Z"
    }
  ]
}
```
