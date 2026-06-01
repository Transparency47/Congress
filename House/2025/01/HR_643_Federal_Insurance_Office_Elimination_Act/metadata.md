# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/643?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/643
- Title: Federal Insurance Office Elimination Act
- Congress: 119
- Bill type: HR
- Bill number: 643
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-10-11T08:05:15Z
- Update date including text: 2025-10-11T08:05:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/643",
    "number": "643",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000634",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Downing, Troy [R-MT-2]",
        "lastName": "Downing",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Federal Insurance Office Elimination Act",
    "type": "HR",
    "updateDate": "2025-10-11T08:05:15Z",
    "updateDateIncludingText": "2025-10-11T08:05:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:09:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "VA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "SC"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TN"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "KS"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WI"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "UT"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "KY"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "OH"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WV"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "OH"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NC"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "OK"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "SC"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "FL"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "WI"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "AL"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "IN"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "NC"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr643ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 643\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Downing (for himself, Mr. Cline , Mr. Haridopolos , Mr. Norman , Mr. Ogles , Mr. Loudermilk , Mr. Schmidt , Mr. Moore of Alabama , Mr. Grothman , and Mr. Kennedy of Utah ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo eliminate the Federal Insurance Office of the Department of the Treasury, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Insurance Office Elimination Act .\n#### 2. Elimination of Federal Insurance Office\n##### (a) In general\nThe Federal Insurance Office of the Department of the Treasury, and the position of the Director of the Federal Insurance Office, are hereby eliminated.\n##### (b) Amendment\nTitle 31, United States Code, is amended\u2014\n**(1)**\nby striking section 313; and\n**(2)**\nin the table of sections for subchapter I of chapter 3, by striking the item relating to section 313.\n##### (c) Treasury authority\nThis section, and the amendment made by this section, may not be construed to repeal or otherwise limit any authority of the Secretary of the Treasury with respect matters relating to insurance.\n#### 3. Related amendments\n##### (a) Dodd-Frank Wall Street Reform and Consumer Protection Act amendments\nThe Dodd-Frank Wall Street Reform and Consumer Protection Act ( 12 U.S.C. 5301 et seq. ) is amended\u2014\n**(1)**\nin section 111(b)(2) ( 12 U.S.C. 5321(b)(2) )\u2014\n**(A)**\nby striking subparagraph (B); and\n**(B)**\nby redesignating subparagraphs (C), (D), and (E) as subparagraphs (B), (C), and (D), respectively;\n**(2)**\nin section 112 ( 12 U.S.C. 5322 )\u2014\n**(A)**\nin subsection (a)(2)(A), by striking member agencies, other Federal and State financial regulatory agencies, the Federal Insurance Office and inserting the following: member agencies and other Federal and State financial regulatory agencies ; and\n**(B)**\nin subsection (d)\u2014\n**(i)**\nin paragraph (1), in the matter preceding subparagraph (A), by striking the Office of Financial Research, member agencies, and the Federal Insurance Office and inserting the Office of Financial Research and member agencies ; and\n**(ii)**\nin paragraph (2), by striking , any member agency, and the Federal Insurance Office, and inserting and any member agency ;\n**(3)**\nin section 165(i) ( 12 U.S.C. 5365(i) )\u2014\n**(A)**\nin paragraph (1)(A), by striking and the Federal Insurance Office and inserting and the Secretary of the Treasury ; and\n**(B)**\nin paragraph (2)(C), in the matter preceding clause (i), by striking and the Federal Insurance Office and inserting and the Secretary of the Treasury ; and\n**(4)**\nin section 203(a)(1)(C) ( 12 U.S.C. 5383(a)(1)(C) )\u2014\n**(A)**\nin the first sentence\u2014\n**(i)**\nby striking the Director of the Federal Insurance Office and ; and\n**(ii)**\nby striking on their own initiative and inserting on the initiative of the Board of Governors ; and\n**(B)**\nin the second sentence, by striking and the affirmative approval of the Director of the Federal Insurance Office .\n##### (b) Economic Growth, Regulatory Relief, and Consumer Protection Act amendments\nSection 211(a) of the Economic Growth, Regulatory Relief, and Consumer Protection Act ( 31 U.S.C. 313 note) is amended\u2014\n**(1)**\nin paragraph (1), by striking the Secretary of the Treasury, Board of Governors of the Federal Reserve System, and Director of the Federal Insurance Office and inserting the following: the Secretary of the Treasury and the Board of Governors of the Federal Reserve System ; and\n**(2)**\nin paragraph (2), by striking the Secretary of the Treasury, the Board of Governors of the Federal Reserve System, and the Director of the Federal Insurance Office each place that term occurs and inserting the following: the Secretary of the Treasury and the Board of Governors of the Federal Reserve System .",
      "versionDate": "2025-01-23",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-02-24T20:52:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr643",
          "measure-number": "643",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr643v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Federal Insurance Office Elimination Act</b></p> <p>This bill eliminates the Federal Insurance Office (FIO) within the Department of the Treasury. The bill also removes the FIO director as a nonvoting member of the Financial Stability Oversight Council.</p>"
        },
        "title": "Federal Insurance Office Elimination Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr643.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Federal Insurance Office Elimination Act</b></p> <p>This bill eliminates the Federal Insurance Office (FIO) within the Department of the Treasury. The bill also removes the FIO director as a nonvoting member of the Financial Stability Oversight Council.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr643"
    },
    "title": "Federal Insurance Office Elimination Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Federal Insurance Office Elimination Act</b></p> <p>This bill eliminates the Federal Insurance Office (FIO) within the Department of the Treasury. The bill also removes the FIO director as a nonvoting member of the Financial Stability Oversight Council.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr643"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr643ih.xml"
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
      "title": "Federal Insurance Office Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:49Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Insurance Office Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To eliminate the Federal Insurance Office of the Department of the Treasury, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:36Z"
    }
  ]
}
```
