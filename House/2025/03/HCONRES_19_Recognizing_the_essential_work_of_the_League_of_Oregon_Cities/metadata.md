# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/19?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/19
- Title: Recognizing the essential work of the League of Oregon Cities.
- Congress: 119
- Bill type: HCONRES
- Bill number: 19
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2025-12-05T22:56:47Z
- Update date including text: 2025-12-05T22:56:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-11 - IntroReferral: Submitted in House
- 2025-03-11 - IntroReferral: Submitted in House
- Latest action: 2025-03-11: Submitted in House

## Actions

- 2025-03-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-11 - IntroReferral: Submitted in House
- 2025-03-11 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/19",
    "number": "19",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Recognizing the essential work of the League of Oregon Cities.",
    "type": "HCONRES",
    "updateDate": "2025-12-05T22:56:47Z",
    "updateDateIncludingText": "2025-12-05T22:56:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:05:00Z",
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
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OR"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OR"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OR"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres19ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 19\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Ms. Bonamici (for herself, Ms. Salinas , Ms. Bynum , Ms. Hoyle of Oregon , and Ms. Dexter ) submitted the following concurrent resolution; which was referred to the Committee on Oversight and Government Reform\nCONCURRENT RESOLUTION\nRecognizing the essential work of the League of Oregon Cities.\nThat Congress recognizes the essential work of the League of Oregon Cities since 1925 and the role the League of Oregon Cities will play in the future in supporting municipalities in the State of Oregon with unparalleled research, technical expertise, and relentless advocacy as a key partner in preserving and strengthening the Federal-local partnership.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-03-11",
        "text": "Referred to the Committee on the Judiciary. (text: CR S1668)"
      },
      "number": "10",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A concurrent resolution recognizing the essential work of the League of Oregon Cities.",
      "type": "SCONRES"
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
        "updateDate": "2025-05-14T14:57:41Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres19ih.xml"
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
      "title": "Recognizing the essential work of the League of Oregon Cities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T09:48:19Z"
    },
    {
      "title": "Recognizing the essential work of the League of Oregon Cities.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T08:07:18Z"
    }
  ]
}
```
