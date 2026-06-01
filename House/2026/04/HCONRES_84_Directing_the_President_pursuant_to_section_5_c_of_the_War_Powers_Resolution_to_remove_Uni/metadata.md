# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/84?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/84
- Title: Directing the President pursuant to section 5(c) of the War Powers Resolution to remove United States Armed Forces from Lebanon.
- Congress: 119
- Bill type: HCONRES
- Bill number: 84
- Origin chamber: House
- Introduced date: 2026-04-13
- Update date: 2026-05-30T08:05:44Z
- Update date including text: 2026-05-30T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-04-13: Introduced in House
- 2026-04-13 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-13 - IntroReferral: Submitted in House
- Latest action: 2026-04-13: Submitted in House

## Actions

- 2026-04-13 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-13 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-13",
    "latestAction": {
      "actionDate": "2026-04-13",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/84",
    "number": "84",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000481",
        "district": "12",
        "firstName": "Rashida",
        "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
        "lastName": "Tlaib",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Directing the President pursuant to section 5(c) of the War Powers Resolution to remove United States Armed Forces from Lebanon.",
    "type": "HCONRES",
    "updateDate": "2026-05-30T08:05:44Z",
    "updateDateIncludingText": "2026-05-30T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
          "date": "2026-04-13T18:30:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "IL"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "AZ"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NC"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "IL"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "OR"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "CA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "MN"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "CA"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "IN"
    },
    {
      "bioguideId": "M001246",
      "district": "11",
      "firstName": "Analilia",
      "fullName": "Rep. Mejia, Analilia [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Mejia",
      "party": "D",
      "sponsorshipDate": "2026-05-22",
      "state": "NJ"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "GA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "MA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "PA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "AZ"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "IL"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres84ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. CON. RES. 84\nIN THE HOUSE OF REPRESENTATIVES\nApril 13, 2026 Ms. Tlaib submitted the following concurrent resolution; which was referred to the Committee on Foreign Affairs\nCONCURRENT RESOLUTION\nDirecting the President pursuant to section 5(c) of the War Powers Resolution to remove United States Armed Forces from Lebanon.\n#### 1. Removal of United States Armed Forces from Lebanon\nPursuant to section 5(c) of the War Powers Resolution ( 50 U.S.C. 1544(c) ), Congress directs the President to remove the United States Armed Forces from Lebanon by not later than the date that is 7 days after the date of the adoption of this concurrent resolution.",
      "versionDate": "2026-04-13",
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
        "name": "International Affairs",
        "updateDate": "2026-04-20T22:23:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-13",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hconres84",
          "measure-number": "84",
          "measure-type": "hconres",
          "orig-publish-date": "2026-04-13",
          "originChamber": "HOUSE",
          "update-date": "2026-05-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hconres84v00",
            "update-date": "2026-05-29"
          },
          "action-date": "2026-04-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This concurrent resolution directs the President to remove U.S. Armed Forces from Lebanon within seven days of the resolution's adoption.</p>"
        },
        "title": "Directing the President pursuant to section 5(c) of the War Powers Resolution to remove United States Armed Forces from Lebanon."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hconres/BILLSUM-119hconres84.xml",
    "summary": {
      "actionDate": "2026-04-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution directs the President to remove U.S. Armed Forces from Lebanon within seven days of the resolution's adoption.</p>",
      "updateDate": "2026-05-29",
      "versionCode": "id119hconres84"
    },
    "title": "Directing the President pursuant to section 5(c) of the War Powers Resolution to remove United States Armed Forces from Lebanon."
  },
  "summaries": [
    {
      "actionDate": "2026-04-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution directs the President to remove U.S. Armed Forces from Lebanon within seven days of the resolution's adoption.</p>",
      "updateDate": "2026-05-29",
      "versionCode": "id119hconres84"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres84ih.xml"
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
      "title": "Directing the President pursuant to section 5(c) of the War Powers Resolution to remove United States Armed Forces from Lebanon.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T08:19:10Z"
    },
    {
      "title": "Directing the President pursuant to section 5(c) of the War Powers Resolution to remove United States Armed Forces from Lebanon.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T08:05:25Z"
    }
  ]
}
```
