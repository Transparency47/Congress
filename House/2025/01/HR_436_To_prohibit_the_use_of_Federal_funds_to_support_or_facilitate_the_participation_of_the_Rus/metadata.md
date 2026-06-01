# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/436?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/436
- Title: To prohibit the use of Federal funds to support or facilitate the participation of the Russian Federation in the Group of Seven, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 436
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-10-18T08:05:55Z
- Update date including text: 2025-10-18T08:05:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/436",
    "number": "436",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000375",
        "district": "9",
        "firstName": "William",
        "fullName": "Rep. Keating, William R. [D-MA-9]",
        "lastName": "Keating",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "To prohibit the use of Federal funds to support or facilitate the participation of the Russian Federation in the Group of Seven, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-10-18T08:05:55Z",
    "updateDateIncludingText": "2025-10-18T08:05:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:04:15Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NJ"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "DE"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "GU"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "SC"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NE"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "OH"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NJ"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NY"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "TX"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NV"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MD"
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
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr436ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 436\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Keating (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit the use of Federal funds to support or facilitate the participation of the Russian Federation in the Group of Seven, and for other purposes.\n#### 1. Prohibition on Russian participation in the G7\n##### (a) Statement of policy\nIt is the policy of the United States to exclude the Russian Federation from the Group of Seven or reconstitute a Group of Eight that includes the Russian Federation.\n##### (b) Limitation\nNotwithstanding any other provision of law, no Federal funds are authorized to be appropriated or otherwise made available to take any action to support or facilitate\u2014\n**(1)**\nthe participation of the Russian Federation in a Group of Seven proceeding; or\n**(2)**\nthe reconstitution of a Group of Eight that includes the Russian Federation.",
      "versionDate": "2025-01-15",
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
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-05-09T18:03:46Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-05-09T18:03:46Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-05-09T18:03:46Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-05-09T18:03:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-02-21T12:24:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr436",
          "measure-number": "436",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr436v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill prohibits using federal funds to support or facilitate (1) Russia's participation in a Group of Seven (G-7) proceeding, or (2) a reconstituted Group of Eight (G-8) that includes Russia. (The G-7 is an informal group consisting of seven of the world's largest advanced economies. In 2014, the G-8 became the G-7 when Russia 's membership was suspended following Russia's annexation of the Crimea region of Ukraine.)</p>"
        },
        "title": "To prohibit the use of Federal funds to support or facilitate the participation of the Russian Federation in the Group of Seven, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr436.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits using federal funds to support or facilitate (1) Russia's participation in a Group of Seven (G-7) proceeding, or (2) a reconstituted Group of Eight (G-8) that includes Russia. (The G-7 is an informal group consisting of seven of the world's largest advanced economies. In 2014, the G-8 became the G-7 when Russia 's membership was suspended following Russia's annexation of the Crimea region of Ukraine.)</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr436"
    },
    "title": "To prohibit the use of Federal funds to support or facilitate the participation of the Russian Federation in the Group of Seven, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits using federal funds to support or facilitate (1) Russia's participation in a Group of Seven (G-7) proceeding, or (2) a reconstituted Group of Eight (G-8) that includes Russia. (The G-7 is an informal group consisting of seven of the world's largest advanced economies. In 2014, the G-8 became the G-7 when Russia 's membership was suspended following Russia's annexation of the Crimea region of Ukraine.)</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr436"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr436ih.xml"
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
      "title": "To prohibit the use of Federal funds to support or facilitate the participation of the Russian Federation in the Group of Seven, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T06:48:20Z"
    },
    {
      "title": "To prohibit the use of Federal funds to support or facilitate the participation of the Russian Federation in the Group of Seven, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-16T09:05:42Z"
    }
  ]
}
```
