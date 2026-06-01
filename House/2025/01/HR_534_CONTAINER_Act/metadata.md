# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/534?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/534
- Title: CONTAINER Act
- Congress: 119
- Bill type: HR
- Bill number: 534
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-12-05T21:58:37Z
- Update date including text: 2025-12-05T21:58:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-20 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-20 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/534",
    "number": "534",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "CONTAINER Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:58:37Z",
    "updateDateIncludingText": "2025-12-05T21:58:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-01-16",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-20T18:11:13Z",
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
          "date": "2025-01-16T14:05:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NE"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr534ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 534\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Rouzer (for himself, Mr. McCaul , Mr. Pfluger , Mr. Nehls , Mr. Meuser , Mr. Fleischmann , and Ms. Tenney ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize certain States to take certain actions on certain Federal land to secure an international border of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Creating Obstructions Necessary To Address Illegal and Nefarious Entry Rapidly Act or the CONTAINER Act .\n#### 2. Placement of movable, temporary structures on certain Federal land to secure an international border of the United States\n##### (a) Definitions\nIn this section:\n**(1) Border state**\nThe term Border State means a State that is adjacent to the northern border or southern border.\n**(2) Federal land**\nThe term Federal land means land under the jurisdiction and management of a Federal land management agency that is adjacent to the northern border or southern border.\n**(3) Federal land management agency**\nThe term Federal land management agency means\u2014\n**(A)**\nthe Bureau of Indian Affairs;\n**(B)**\nthe Bureau of Land Management;\n**(C)**\nthe Bureau of Reclamation;\n**(D)**\nthe Forest Service;\n**(E)**\nthe United States Fish and Wildlife Service; and\n**(F)**\nthe National Park Service.\n**(4) Northern border**\nThe term northern border means the international border between the United States and Canada.\n**(5) Operational control**\nThe term operational control has the meaning given such term in section 2(b) of the Secure Fence Act of 2006 ( 8 U.S.C. 1701 note; Public Law 109\u2013367 ).\n**(6) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of the Interior, with respect to Federal land under the jurisdiction and management of the Secretary of the Interior, acting through, as applicable\u2014\n**(i)**\nthe Director of the Bureau of Indian Affairs;\n**(ii)**\nthe Director of the Bureau of Land Management;\n**(iii)**\nthe Commissioner of Reclamation;\n**(iv)**\nthe Director of the United States Fish and Wildlife Service; and\n**(v)**\nthe Director of the National Park Service; and\n**(B)**\nthe Secretary of Agriculture, with respect to National Forest System land, acting through the Chief of the Forest Service.\n**(7) Southern border**\nThe term southern border means the international border between the United States and Mexico.\n##### (b) Special use authorization\nSubject to subsection (c), the Secretary concerned shall not require a Border State to obtain a special use authorization for the temporary placement on Federal land within the Border State of a movable, temporary structure for the purpose of securing the northern border or southern border, if the Border State submits to the Secretary concerned notice of the proposed placement not later than 45 days before the date of the proposed placement.\n##### (c) Temporary placement\n**(1) In general**\nA movable, temporary structure described in subsection (b) may be placed by a Border State on Federal land in accordance with that subsection for a period of not more than 1 year, subject to paragraph (2).\n**(2) Extension**\n**(A) In general**\nThe period described in paragraph (1) may be extended in 90-day increments, on approval by the Secretary concerned.\n**(B) Consultation required**\nThe Secretary concerned shall consult with the Commissioner of U.S. Customs and Border Protection for purposes of determining whether to approve an extension under subparagraph (A).\n**(C) Approval**\nThe Secretary concerned shall approve a request for an extension under this paragraph if the Commissioner of U.S. Customs and Border Protection determines that operational control has not been achieved as of the date of the consultation required under subparagraph (B).",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-21",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "157",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CONTAINER Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-03-12T13:44:40Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-03-12T13:44:46Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-12T13:44:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-02-27T18:50:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr534",
          "measure-number": "534",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-06-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr534v00",
            "update-date": "2025-06-03"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Creating Obstructions Necessary to Address Illegal and Nefarious Entry Rapidly Act or CONTAINER Act</strong></p><p>This bill requires the Department of the Interior and the Forest Service to allow border states to place temporary, movable structures on federal lands adjacent to the U.S.-Canada and U.S.-Mexico borders without a special use authorization.</p><p>Border states may place these structures on such lands for the purpose of securing the northern or southern border for a period of not more than one year. Interior and the Forest Service must approve extension requests in 90-day increments if U.S. Customs and Border Protection determines that operational control of the border area has not been achieved.</p>"
        },
        "title": "CONTAINER Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr534.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Creating Obstructions Necessary to Address Illegal and Nefarious Entry Rapidly Act or CONTAINER Act</strong></p><p>This bill requires the Department of the Interior and the Forest Service to allow border states to place temporary, movable structures on federal lands adjacent to the U.S.-Canada and U.S.-Mexico borders without a special use authorization.</p><p>Border states may place these structures on such lands for the purpose of securing the northern or southern border for a period of not more than one year. Interior and the Forest Service must approve extension requests in 90-day increments if U.S. Customs and Border Protection determines that operational control of the border area has not been achieved.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119hr534"
    },
    "title": "CONTAINER Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Creating Obstructions Necessary to Address Illegal and Nefarious Entry Rapidly Act or CONTAINER Act</strong></p><p>This bill requires the Department of the Interior and the Forest Service to allow border states to place temporary, movable structures on federal lands adjacent to the U.S.-Canada and U.S.-Mexico borders without a special use authorization.</p><p>Border states may place these structures on such lands for the purpose of securing the northern or southern border for a period of not more than one year. Interior and the Forest Service must approve extension requests in 90-day increments if U.S. Customs and Border Protection determines that operational control of the border area has not been achieved.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119hr534"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr534ih.xml"
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
      "title": "CONTAINER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T12:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CONTAINER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Creating Obstructions Necessary To Address Illegal and Nefarious Entry Rapidly Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize certain States to take certain actions on certain Federal land to secure an international border of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T12:03:28Z"
    }
  ]
}
```
