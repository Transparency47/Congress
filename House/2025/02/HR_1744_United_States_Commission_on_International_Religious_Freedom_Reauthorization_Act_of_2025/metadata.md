# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1744?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1744
- Title: United States Commission on International Religious Freedom Reauthorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1744
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-04-14T15:50:21Z
- Update date including text: 2026-04-14T15:50:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 45 - 0.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 45 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1744",
    "number": "1744",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000522",
        "district": "4",
        "firstName": "Christopher",
        "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
        "lastName": "Smith",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "United States Commission on International Religious Freedom Reauthorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T15:50:21Z",
    "updateDateIncludingText": "2026-04-14T15:50:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 45 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2025-02-27",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
            "date": "2026-03-26T16:10:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-27T14:09:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CO"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "TX"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NY"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "MI"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1744ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1744\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Smith of New Jersey (for himself, Mr. Sherman , Mr. Bilirakis , and Mr. Cuellar ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo extend and authorize annual appropriations for the United States Commission on International Religious Freedom through fiscal year 2028.\n#### 1. Short title\nThis Act may be cited as the United States Commission on International Religious Freedom Reauthorization Act of 2025 .\n#### 2. United States Commission on International Religious Freedom\n##### (a) Authorization of appropriations\nSection 207(a) of the International Religious Freedom Act of 1998 ( 22 U.S.C. 6435(a) ) is amended by striking 2025 and 2026 and inserting 2027 and 2028 .\n##### (b) Extension of authorization\nSection 209 of the International Religious Freedom Act of 1998 ( 22 U.S.C. 6436 ) is amended by striking September 30, 2026 and inserting September 30, 2028 .",
      "versionDate": "2025-02-27",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-03-04",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "3984",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "United States Commission on International Religious Freedom Reauthorization Act of 2026",
      "type": "S"
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
        "updateDate": "2025-05-22T13:49:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1744",
          "measure-number": "1744",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-05-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1744v00",
            "update-date": "2025-05-22"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>United States Commission on International Religious Freedom Reauthorization Act of 2025</strong></p><p>This bill reauthorizes the U.S. Commission on International Religious Freedom through FY2028. The commission is an independent federal commission tasked with monitoring international religious freedom conditions, reviewing U.S. government policy, and making policy recommendations.\u00a0</p>"
        },
        "title": "United States Commission on International Religious Freedom Reauthorization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1744.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Commission on International Religious Freedom Reauthorization Act of 2025</strong></p><p>This bill reauthorizes the U.S. Commission on International Religious Freedom through FY2028. The commission is an independent federal commission tasked with monitoring international religious freedom conditions, reviewing U.S. government policy, and making policy recommendations.\u00a0</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119hr1744"
    },
    "title": "United States Commission on International Religious Freedom Reauthorization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Commission on International Religious Freedom Reauthorization Act of 2025</strong></p><p>This bill reauthorizes the U.S. Commission on International Religious Freedom through FY2028. The commission is an independent federal commission tasked with monitoring international religious freedom conditions, reviewing U.S. government policy, and making policy recommendations.\u00a0</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119hr1744"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1744ih.xml"
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
      "title": "United States Commission on International Religious Freedom Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States Commission on International Religious Freedom Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To extend and authorize annual appropriations for the United States Commission on International Religious Freedom through fiscal year 2026.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:33:59Z"
    }
  ]
}
```
