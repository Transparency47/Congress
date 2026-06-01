# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/709?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/709
- Title: Condemning the September 10, 2025, political assassination of Charlie Kirk and honoring his life and legacy.
- Congress: 119
- Bill type: HRES
- Bill number: 709
- Origin chamber: House
- Introduced date: 2025-09-15
- Update date: 2026-04-01T23:39:40Z
- Update date including text: 2026-04-01T23:39:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-15 - IntroReferral: Submitted in House
- 2025-09-15 - IntroReferral: Submitted in House
- Latest action: 2025-09-15: Submitted in House

## Actions

- 2025-09-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-15 - IntroReferral: Submitted in House
- 2025-09-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/709",
    "number": "709",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Condemning the September 10, 2025, political assassination of Charlie Kirk and honoring his life and legacy.",
    "type": "HRES",
    "updateDate": "2026-04-01T23:39:40Z",
    "updateDateIncludingText": "2026-04-01T23:39:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
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
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T16:04:45Z",
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
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres709ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 709\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 15, 2025 Mr. Carter of Georgia (for himself, Mr. McCormick , Mr. Loudermilk , Mr. Austin Scott of Georgia , and Mr. Clyde ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nCondemning the September 10, 2025, political assassination of Charlie Kirk and honoring his life and legacy.\nThat the House of Representatives\u2014\n**(1)**\ncondemns, in the strongest possible terms, the September 10, 2025, assassination of Charlie Kirk;\n**(2)**\napplauds the quick response and dedicated service of the first responders and hospital medical team who cared for Charlie Kirk;\n**(3)**\nexpresses sorrow and heartfelt condolences to the Kirk family; and\n**(4)**\nreaffirms its commitment to protecting the rights of all Americans to assemble peacefully and to express their political views without fear of violence.",
      "versionDate": "2025-09-15",
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
        "actionDate": "2025-09-11",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "702",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Condemning in the strongest possible terms the September 10, 2025, assassination of Charlie Kirk.",
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
        "updateDate": "2025-09-17T19:34:37Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres709ih.xml"
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
      "title": "Condemning the September 10, 2025, political assassination of Charlie Kirk and honoring his life and legacy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-17T02:48:19Z"
    },
    {
      "title": "Condemning the September 10, 2025, political assassination of Charlie Kirk and honoring his life and legacy.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T08:05:48Z"
    }
  ]
}
```
