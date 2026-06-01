# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1254?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1254
- Title: Recognizing the roles and contributions of elementary and secondary school teachers in building and enhancing the civic, cultural, and economic well-being of the United States.
- Congress: 119
- Bill type: HRES
- Bill number: 1254
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-18T15:53:51Z
- Update date including text: 2026-05-18T15:53:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-04 - IntroReferral: Submitted in House
- Latest action: 2026-05-04: Submitted in House

## Actions

- 2026-05-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-04 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-04",
    "latestAction": {
      "actionDate": "2026-05-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1254",
    "number": "1254",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "G000546",
        "district": "6",
        "firstName": "Sam",
        "fullName": "Rep. Graves, Sam [R-MO-6]",
        "lastName": "Graves",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Recognizing the roles and contributions of elementary and secondary school teachers in building and enhancing the civic, cultural, and economic well-being of the United States.",
    "type": "HRES",
    "updateDate": "2026-05-18T15:53:51Z",
    "updateDateIncludingText": "2026-05-18T15:53:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-04",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-04",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
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
          "date": "2026-05-04T14:32:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "MO"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "MO"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-05-04",
      "state": "MO"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1254ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1254\nIN THE HOUSE OF REPRESENTATIVES\nMay 4, 2026 Mr. Graves (for himself, Mr. Bell , Mr. Cleaver , and Mr. Alford ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nRecognizing the roles and contributions of elementary and secondary school teachers in building and enhancing the civic, cultural, and economic well-being of the United States.\nThat the House of Representatives\u2014\n**(1)**\nthanks elementary and secondary school teachers of the United States; and\n**(2)**\npromotes the profession of teaching and the contributions of educators by encouraging students, parents, school administrators, and public officials to recognize National Teacher Appreciation Week.",
      "versionDate": "2026-05-04",
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
        "actionDate": "2025-05-05",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "379",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the roles and contributions of elementary and secondary school teachers in building and enhancing the civic, cultural, and economic well-being of the United States.",
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
        "name": "Education",
        "updateDate": "2026-05-18T15:53:50Z"
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
      "date": "2026-05-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1254ih.xml"
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
      "title": "Recognizing the roles and contributions of elementary and secondary school teachers in building and enhancing the civic, cultural, and economic well-being of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T08:18:32Z"
    },
    {
      "title": "Recognizing the roles and contributions of elementary and secondary school teachers in building and enhancing the civic, cultural, and economic well-being of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T08:06:25Z"
    }
  ]
}
```
