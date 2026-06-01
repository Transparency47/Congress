# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1782?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1782
- Title: SHOPP Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1782
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-03-26T15:27:59Z
- Update date including text: 2026-03-26T15:27:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1782",
    "number": "1782",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001130",
        "district": "30",
        "firstName": "Jasmine",
        "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
        "lastName": "Crockett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "SHOPP Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-26T15:27:59Z",
    "updateDateIncludingText": "2026-03-26T15:27:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:47:54Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
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
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "MO"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CT"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "IN"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "IL"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "NE"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "PA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "AL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MI"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "WA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MO"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "AL"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "VA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "OH"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1782ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1782\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Ms. Crockett (for herself, Mr. Alford , and Mrs. Hayes ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food, Conservation, and Energy Act of 2008 to provide families year-round access to nutrition incentives under the Gus Schumacher Nutrition Incentive Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting all Healthy Options when Purchasing Produce Act of 2025 or the SHOPP Act of 2025 .\n#### 2. Nutrition incentives under Gus Schumacher Nutrition Incentive Program\nSection 4405 of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 7517 ) is amended\u2014\n**(1)**\nin subsection (b)(2)(B)\u2014\n**(A)**\nby redesignating clauses (ix) and (x) as clauses (x) and (xi), respectively; and\n**(B)**\nby inserting after clause (viii) the following:\n(ix) increase the year-round availability of the incentive described in subparagraph (A)(ii)(II) by offering fresh frozen fruits or vegetables; ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(A), by striking fruits and vegetables and inserting fruits, vegetables, and legumes ; and\n**(B)**\nin paragraph (3), by striking fresh fruits and vegetables each place it appears and inserting fresh or fresh frozen fruits, vegetables, and legumes .",
      "versionDate": "2025-03-03",
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
        "actionDate": "2025-03-03",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "813",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SHOPP Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-09T19:01:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119hr1782",
          "measure-number": "1782",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-03",
          "originChamber": "HOUSE",
          "update-date": "2026-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1782v00",
            "update-date": "2026-03-26"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supporting all Healthy Options when Purchasing Produce Act of 2025 or the SHOPP Act\u00a0of 2025</strong></p><p>This bill modifies the\u00a0Gus Schumacher Nutrition Incentive Program\u00a0(GusNIP) to include fresh frozen fruits and vegetables.</p><p>GusNIP is\u00a0a Department of Agriculture\u00a0(USDA) program that provides grants for projects that increase low-income consumers' purchases of fruits and vegetables. It\u00a0is made up of three competitive grant programs, including the GusNIP Nutrition Incentive Program, which provides grants for projects that provide incentives for Supplemental Nutrition Assistance Program (SNAP) participants to purchase\u00a0fruits and vegetables.</p><p>The bill\u00a0directs USDA, in awarding GusNIP Nutrition Incentive Program grants, to give priority to projects that\u00a0increase year-round availability of nutrition incentives by offering fresh frozen fruits or vegetables in the program.</p><p>In addition, the bill amends another GusNIP program,\u00a0the Produce Prescription Program, to include fresh frozen fruits and vegetables, as well as fresh and fresh frozen legumes. Currently, only fresh fruits and vegetables are covered under the program.</p><p>The\u00a0GusNIP Produce Prescription Program supports projects that demonstrate and evaluate the impact of fruit and vegetable prescriptions on\u00a0increasing procurement and consumption of fruits and vegetables, reducing individual and household food insecurity, and reducing healthcare usage and associated costs.</p>"
        },
        "title": "SHOPP Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1782.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting all Healthy Options when Purchasing Produce Act of 2025 or the SHOPP Act\u00a0of 2025</strong></p><p>This bill modifies the\u00a0Gus Schumacher Nutrition Incentive Program\u00a0(GusNIP) to include fresh frozen fruits and vegetables.</p><p>GusNIP is\u00a0a Department of Agriculture\u00a0(USDA) program that provides grants for projects that increase low-income consumers' purchases of fruits and vegetables. It\u00a0is made up of three competitive grant programs, including the GusNIP Nutrition Incentive Program, which provides grants for projects that provide incentives for Supplemental Nutrition Assistance Program (SNAP) participants to purchase\u00a0fruits and vegetables.</p><p>The bill\u00a0directs USDA, in awarding GusNIP Nutrition Incentive Program grants, to give priority to projects that\u00a0increase year-round availability of nutrition incentives by offering fresh frozen fruits or vegetables in the program.</p><p>In addition, the bill amends another GusNIP program,\u00a0the Produce Prescription Program, to include fresh frozen fruits and vegetables, as well as fresh and fresh frozen legumes. Currently, only fresh fruits and vegetables are covered under the program.</p><p>The\u00a0GusNIP Produce Prescription Program supports projects that demonstrate and evaluate the impact of fruit and vegetable prescriptions on\u00a0increasing procurement and consumption of fruits and vegetables, reducing individual and household food insecurity, and reducing healthcare usage and associated costs.</p>",
      "updateDate": "2026-03-26",
      "versionCode": "id119hr1782"
    },
    "title": "SHOPP Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting all Healthy Options when Purchasing Produce Act of 2025 or the SHOPP Act\u00a0of 2025</strong></p><p>This bill modifies the\u00a0Gus Schumacher Nutrition Incentive Program\u00a0(GusNIP) to include fresh frozen fruits and vegetables.</p><p>GusNIP is\u00a0a Department of Agriculture\u00a0(USDA) program that provides grants for projects that increase low-income consumers' purchases of fruits and vegetables. It\u00a0is made up of three competitive grant programs, including the GusNIP Nutrition Incentive Program, which provides grants for projects that provide incentives for Supplemental Nutrition Assistance Program (SNAP) participants to purchase\u00a0fruits and vegetables.</p><p>The bill\u00a0directs USDA, in awarding GusNIP Nutrition Incentive Program grants, to give priority to projects that\u00a0increase year-round availability of nutrition incentives by offering fresh frozen fruits or vegetables in the program.</p><p>In addition, the bill amends another GusNIP program,\u00a0the Produce Prescription Program, to include fresh frozen fruits and vegetables, as well as fresh and fresh frozen legumes. Currently, only fresh fruits and vegetables are covered under the program.</p><p>The\u00a0GusNIP Produce Prescription Program supports projects that demonstrate and evaluate the impact of fruit and vegetable prescriptions on\u00a0increasing procurement and consumption of fruits and vegetables, reducing individual and household food insecurity, and reducing healthcare usage and associated costs.</p>",
      "updateDate": "2026-03-26",
      "versionCode": "id119hr1782"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1782ih.xml"
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
      "title": "SHOPP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHOPP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting all Healthy Options when Purchasing Produce Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food, Conservation, and Energy Act of 2008 to provide families year-round access to nutrition incentives under the Gus Schumacher Nutrition Incentive Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T10:18:35Z"
    }
  ]
}
```
