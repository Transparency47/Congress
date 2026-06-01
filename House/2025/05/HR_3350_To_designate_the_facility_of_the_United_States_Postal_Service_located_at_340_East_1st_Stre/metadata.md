# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3350?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3350
- Title: To designate the facility of the United States Postal Service located at 340 East 1st Street in Tustin, California, as the "Ursula Ellen Kennedy Post Office Building".
- Congress: 119
- Bill type: HR
- Bill number: 3350
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2026-05-21T08:08:54Z
- Update date including text: 2026-05-21T08:08:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported by Voice Vote.
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3350",
    "number": "3350",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 340 East 1st Street in Tustin, California, as the \"Ursula Ellen Kennedy Post Office Building\".",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:54Z",
    "updateDateIncludingText": "2026-05-21T08:08:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
        "item": [
          {
            "date": "2026-05-20T13:22:59Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-13T16:02:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "CA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "False",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3350ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3350\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mrs. Kim introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 340 East 1st Street in Tustin, California, as the Ursula Ellen Kennedy Post Office Building .\n#### 1. Ursula ellen kennedy post office building\n##### (a) Designation\nThe facility of the United States Postal Service located at 340 East 1st Street in Tustin, California, shall be known and designated as the Ursula Ellen Kennedy Post Office Building .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Ursula Ellen Kennedy Post Office Building .",
      "versionDate": "2025-05-13",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "California",
            "updateDate": "2025-08-13T13:40:46Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-08-13T13:40:30Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-08-13T13:40:42Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-08-13T13:40:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-26T22:32:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-13",
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
          "measure-id": "id119hr3350",
          "measure-number": "3350",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-13",
          "originChamber": "HOUSE",
          "update-date": "2025-08-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3350v00",
            "update-date": "2025-08-01"
          },
          "action-date": "2025-05-13",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 340 East 1st Street in Tustin, California, as the \"Ursula Ellen Kennedy Post Office Building\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 340 East 1st Street in Tustin, California, as the \"Ursula Ellen Kennedy Post Office Building\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3350.xml",
    "summary": {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 340 East 1st Street in Tustin, California, as the \"Ursula Ellen Kennedy Post Office Building\".",
      "updateDate": "2025-08-01",
      "versionCode": "id119hr3350"
    },
    "title": "To designate the facility of the United States Postal Service located at 340 East 1st Street in Tustin, California, as the \"Ursula Ellen Kennedy Post Office Building\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 340 East 1st Street in Tustin, California, as the \"Ursula Ellen Kennedy Post Office Building\".",
      "updateDate": "2025-08-01",
      "versionCode": "id119hr3350"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3350ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "title": "To designate the facility of the United States Postal Service located at 340 East 1st Street in Tustin, California, as the \"Ursula Ellen Kennedy Post Office Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:43Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 340 East 1st Street in Tustin, California, as the \"Ursula Ellen Kennedy Post Office Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T08:05:51Z"
    }
  ]
}
```
