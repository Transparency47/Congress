# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2517?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2517
- Title: Community Wood Facilities Assistance Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2517
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-04-03T08:05:52Z
- Update date including text: 2026-04-03T08:05:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-18 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-18 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2517",
    "number": "2517",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Community Wood Facilities Assistance Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-03T08:05:52Z",
    "updateDateIncludingText": "2026-04-03T08:05:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:14:00Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-31T16:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "WA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "ME"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2517ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2517\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Ms. Perez (for herself, Mr. Newhouse , and Ms. Pingree ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Farm Security and Rural Investment Act of 2002 to improve assistance to community wood facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Community Wood Facilities Assistance Act of 2025 .\n#### 2. Community Wood Facilities Grant Program\nSection 9013 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8113 ) is amended\u2014\n**(1)**\nin the section heading, by striking Energy and Wood Innovation and inserting Facilities Grant ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)(A)(iii), in the matter preceding subclause (I), by striking woody biomass, including and inserting primarily forest biomass, including processing or manufacturing ; and\n**(B)**\nin paragraph (4), by striking Energy and Wood Innovation and inserting Facilities Grant ;\n**(3)**\nin subsection (b), by striking Energy and Wood Innovation and inserting Facilities Grant ;\n**(4)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by striking 35 and inserting 50 ;\n**(B)**\nby striking paragraph (2); and\n**(C)**\nby redesignating paragraph (3) as paragraph (2);\n**(5)**\nin subsection (d), in the matter preceding paragraph (1), by striking exceed\u2014 and all that follows through $1,500,000. and inserting exceed $5,000,000. ;\n**(6)**\nin subsection (e)\u2014\n**(A)**\nby striking paragraph (1);\n**(B)**\nby redesignating paragraphs (2) through (8) as paragraphs (1) through (7), respectively; and\n**(C)**\nin paragraph (1) (as so redesignated), by inserting or market competitiveness after cost effectiveness ;\n**(7)**\nin subsection (f)\u2014\n**(A)**\nby striking paragraph (2);\n**(B)**\nby redesignating paragraphs (3) and (4) as paragraphs (2) and (3), respectively; and\n**(C)**\nin paragraph (2) (as so redesignated), by striking use or retrofitting (or both) of existing sawmill and inserting construction, use, or retrofitting of forest products manufacturing ;\n**(8)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1), by striking 5 megawatts of thermal energy or combined thermal and electric energy and inserting 15 megawatts of thermal energy ; and\n**(B)**\nin paragraph (2), by striking 25 percent and inserting 50 percent ; and\n**(9)**\nin subsection (h), by striking $25,000,000 for each of fiscal years 2019 through 2023 and inserting $50,000,000 for each of fiscal years 2026 through 2030 .\n#### 3. Wood Innovations Grant Program\nSection 8643 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 7655d ) is amended\u2014\n**(1)**\nin the section heading, by striking Innovation and inserting Innovations ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin the subsection heading, by striking Incentivizing use of existing milling and inserting Expanding forest products manufacturing ; and\n**(B)**\nby striking use or retrofitting (or both) of existing sawmill and inserting construction, use, or retrofitting for forest products manufacturing ; and\n**(3)**\nin subsection (d), by inserting 50 percent of before the amount .",
      "versionDate": "2025-03-31",
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
        "actionDate": "2025-06-26",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "2183",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Community Wood Facilities Assistance Act of 2025",
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
        "updateDate": "2025-05-06T20:46:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
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
          "measure-id": "id119hr2517",
          "measure-number": "2517",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-31",
          "originChamber": "HOUSE",
          "update-date": "2026-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2517v00",
            "update-date": "2026-03-26"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Community Wood Facilities Assistance Act of 2025 </strong></p><p>This bill makes changes to grant programs administered by the Forest Service to promote wood products.</p><p>Specifically, the bill reauthorizes through FY2030, modifies, and renames the Community Wood Facilities Grant program. Currently named the Community Wood Energy and Wood Innovation Program, this program provides competitive grants to fund a portion of the capital costs for installing community wood energy systems or building innovative wood products facilities. \u00a0</p><p>Modifications to the program include increasing the maximum grant amount per facility, increasing the portion of a project's cost that may be covered by a grant,\u00a0and changing\u00a0the grant selection criteria.</p><p>The bill also modifies the\u00a0Wood Innovation Grant Program, which provides grants to develop and expand the market for innovative wood products. Specifically, the bill increases the portion of a project's cost that may be covered by such a grant.</p><p>The bill also modifies both programs to prioritize grants for the construction, use, or retrofitting of forest products manufacturing.</p>"
        },
        "title": "Community Wood Facilities Assistance Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2517.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Community Wood Facilities Assistance Act of 2025 </strong></p><p>This bill makes changes to grant programs administered by the Forest Service to promote wood products.</p><p>Specifically, the bill reauthorizes through FY2030, modifies, and renames the Community Wood Facilities Grant program. Currently named the Community Wood Energy and Wood Innovation Program, this program provides competitive grants to fund a portion of the capital costs for installing community wood energy systems or building innovative wood products facilities. \u00a0</p><p>Modifications to the program include increasing the maximum grant amount per facility, increasing the portion of a project's cost that may be covered by a grant,\u00a0and changing\u00a0the grant selection criteria.</p><p>The bill also modifies the\u00a0Wood Innovation Grant Program, which provides grants to develop and expand the market for innovative wood products. Specifically, the bill increases the portion of a project's cost that may be covered by such a grant.</p><p>The bill also modifies both programs to prioritize grants for the construction, use, or retrofitting of forest products manufacturing.</p>",
      "updateDate": "2026-03-26",
      "versionCode": "id119hr2517"
    },
    "title": "Community Wood Facilities Assistance Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Community Wood Facilities Assistance Act of 2025 </strong></p><p>This bill makes changes to grant programs administered by the Forest Service to promote wood products.</p><p>Specifically, the bill reauthorizes through FY2030, modifies, and renames the Community Wood Facilities Grant program. Currently named the Community Wood Energy and Wood Innovation Program, this program provides competitive grants to fund a portion of the capital costs for installing community wood energy systems or building innovative wood products facilities. \u00a0</p><p>Modifications to the program include increasing the maximum grant amount per facility, increasing the portion of a project's cost that may be covered by a grant,\u00a0and changing\u00a0the grant selection criteria.</p><p>The bill also modifies the\u00a0Wood Innovation Grant Program, which provides grants to develop and expand the market for innovative wood products. Specifically, the bill increases the portion of a project's cost that may be covered by such a grant.</p><p>The bill also modifies both programs to prioritize grants for the construction, use, or retrofitting of forest products manufacturing.</p>",
      "updateDate": "2026-03-26",
      "versionCode": "id119hr2517"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2517ih.xml"
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
      "title": "Community Wood Facilities Assistance Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Wood Facilities Assistance Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Farm Security and Rural Investment Act of 2002 to improve assistance to community wood facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:56Z"
    }
  ]
}
```
