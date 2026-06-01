# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1116?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1116
- Title: REAL Meat Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1116
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2025-10-09T03:26:20Z
- Update date including text: 2025-10-09T03:26:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-14 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-14 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1116",
    "number": "1116",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "REAL Meat Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-09T03:26:20Z",
    "updateDateIncludingText": "2025-10-09T03:26:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T20:36:40Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "TX"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "IN"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "SC"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1116ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1116\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Davidson (for himself, Mr. Nehls , and Mr. Baird ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo prohibit the use of Federal funds to support cell-cultured meat, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Right to Eat Authentic and Legitimate Meat Act of 2025 or the REAL Meat Act of 2025 .\n#### 2. No Federal funds supporting cell-cultured meat\n##### (a) In general\nSubject to subsection (b), no Federal funds may be used to support, directly or indirectly, the production, advancement, or enhancement of cell-cultured meat, including through\u2014\n**(1)**\nconducting or supporting research on cell-cultured meat;\n**(2)**\nsupporting meatpacking plants, organizations, or groups relating to cell-cultured meat;\n**(3)**\nallowing for the receipt of any assistance or other benefit under a program administered by the Secretary of Agriculture for any product that includes as an ingredient cell-cultured meat; and\n**(4)**\nthe promotion and advertisement of cell-cultured meat.\n##### (b) NASA exemption\nThe prohibition described in subsection (a) shall not apply to Federal funds of the National Aeronautics and Space Administration used to support, directly or indirectly, the production, advancement, or enhancement of cell-cultured meat that is intended for off-planet consumption.\n##### (c) Cell-Cultured meat defined\nIn this section, the term cell-cultured meat means meat that is sourced from the cells of animals and artificially produced in a laboratory.",
      "versionDate": "2025-02-07",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-03-20T19:02:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-07",
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
          "measure-id": "id119hr1116",
          "measure-number": "1116",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-07",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1116v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-02-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Right to Eat Authentic and Legitimate Meat Act of 2025 or the REAL Meat Act of 2025</strong></p><p>This bill prohibits the use of federal funds to support, directly or indirectly, the production, advancement, or enhancement of cell-cultured meat. Under the bill,\u00a0<em>cell-cultured meat</em> means meat that is sourced from the cells of animals and artificially produced in a laboratory.</p><p>The bill includes an exemption for federal funds of the National Aeronautics and Space Administration (NASA)\u00a0that are used for activities related to cell-cultured meat that is intended for off-planet consumption.</p>"
        },
        "title": "REAL Meat Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1116.xml",
    "summary": {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Right to Eat Authentic and Legitimate Meat Act of 2025 or the REAL Meat Act of 2025</strong></p><p>This bill prohibits the use of federal funds to support, directly or indirectly, the production, advancement, or enhancement of cell-cultured meat. Under the bill,\u00a0<em>cell-cultured meat</em> means meat that is sourced from the cells of animals and artificially produced in a laboratory.</p><p>The bill includes an exemption for federal funds of the National Aeronautics and Space Administration (NASA)\u00a0that are used for activities related to cell-cultured meat that is intended for off-planet consumption.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr1116"
    },
    "title": "REAL Meat Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Right to Eat Authentic and Legitimate Meat Act of 2025 or the REAL Meat Act of 2025</strong></p><p>This bill prohibits the use of federal funds to support, directly or indirectly, the production, advancement, or enhancement of cell-cultured meat. Under the bill,\u00a0<em>cell-cultured meat</em> means meat that is sourced from the cells of animals and artificially produced in a laboratory.</p><p>The bill includes an exemption for federal funds of the National Aeronautics and Space Administration (NASA)\u00a0that are used for activities related to cell-cultured meat that is intended for off-planet consumption.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr1116"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1116ih.xml"
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
      "title": "REAL Meat Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T04:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REAL Meat Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-11T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Right to Eat Authentic and Legitimate Meat Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-11T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of Federal funds to support cell-cultured meat, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T04:18:23Z"
    }
  ]
}
```
