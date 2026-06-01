# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5066?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5066
- Title: Safe Students Act
- Congress: 119
- Bill type: HR
- Bill number: 5066
- Origin chamber: House
- Introduced date: 2025-08-29
- Update date: 2026-05-22T14:31:02Z
- Update date including text: 2026-05-22T14:31:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-08-29: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-08-29: Introduced in House

## Actions

- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-29",
    "latestAction": {
      "actionDate": "2025-08-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5066",
    "number": "5066",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Safe Students Act",
    "type": "HR",
    "updateDate": "2026-05-22T14:31:02Z",
    "updateDateIncludingText": "2026-05-22T14:31:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-29",
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
        "item": {
          "date": "2025-08-29T17:31:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "GA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "CO"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "AZ"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "TX"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "PA"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "OH"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "MO"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "AZ"
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
      "sponsorshipDate": "2025-08-29",
      "state": "GA"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "IL"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "OK"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "TX"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5066ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5066\nIN THE HOUSE OF REPRESENTATIVES\nAugust 29, 2025 Mr. Massie (for himself, Ms. Greene of Georgia , Ms. Boebert , Mr. Gosar , Mr. Roy , Mr. Perry , Mr. Davidson , Mr. Burlison , Mr. Crane , Mr. Clyde , and Mrs. Miller of Illinois ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo repeal the Gun-Free School Zones Act of 1990 and amendments to that Act.\n#### 1. Short title\nThis Act may be cited as the Safe Students Act .\n#### 2. Repeal of the gun-free school zones act of 1990 and amendments to that act\n##### (a) In general\nSection 922 of title 18, United States Code, is amended by striking subsection (q).\n##### (b) Related amendments\n**(1)**\nSection 921(a) of such title is amended by striking paragraphs (25) through (27) and redesignating paragraphs (28), (29), and (32) through (37) as paragraphs (25) through (32), respectively.\n**(2)**\nSection 924(a) of such title is amended\u2014\n**(A)**\nin paragraph (1)(B), by striking (k), or (q) and inserting or (k) ; and\n**(B)**\nby striking paragraph (4) and redesignating paragraphs (5) through (8) as paragraphs (4) through (7), respectively.\n**(3)**\nThe Gun-Free School Zones Act of 1990 ( 18 U.S.C. 921 note, 922 note; section 1702 of Public Law 101\u2013647 ; 104 Stat. 4844\u20134845) is repealed.",
      "versionDate": "2025-08-29",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-19T17:20:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-29",
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
          "measure-id": "id119hr5066",
          "measure-number": "5066",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-29",
          "originChamber": "HOUSE",
          "update-date": "2026-05-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5066v00",
            "update-date": "2026-05-22"
          },
          "action-date": "2025-08-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Safe Students Act</b></p> <p>This bill repeals provisions of federal criminal law that prohibit the possession or discharge of a firearm in a school zone.</p>"
        },
        "title": "Safe Students Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5066.xml",
    "summary": {
      "actionDate": "2025-08-29",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Safe Students Act</b></p> <p>This bill repeals provisions of federal criminal law that prohibit the possession or discharge of a firearm in a school zone.</p>",
      "updateDate": "2026-05-22",
      "versionCode": "id119hr5066"
    },
    "title": "Safe Students Act"
  },
  "summaries": [
    {
      "actionDate": "2025-08-29",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Safe Students Act</b></p> <p>This bill repeals provisions of federal criminal law that prohibit the possession or discharge of a firearm in a school zone.</p>",
      "updateDate": "2026-05-22",
      "versionCode": "id119hr5066"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5066ih.xml"
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
      "title": "Safe Students Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-03T05:23:19Z"
    },
    {
      "title": "Safe Students Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal the Gun-Free School Zones Act of 1990 and amendments to that Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-03T05:18:21Z"
    }
  ]
}
```
