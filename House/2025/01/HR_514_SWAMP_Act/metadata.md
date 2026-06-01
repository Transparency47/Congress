# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/514?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/514
- Title: SWAMP Act
- Congress: 119
- Bill type: HR
- Bill number: 514
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-12-05T21:47:34Z
- Update date including text: 2025-12-05T21:47:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-17 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-17 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/514",
    "number": "514",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001091",
        "district": "2",
        "firstName": "Ashley",
        "fullName": "Rep. Hinson, Ashley [R-IA-2]",
        "lastName": "Hinson",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "SWAMP Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:47:34Z",
    "updateDateIncludingText": "2025-12-05T21:47:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-17",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-01-16T14:07:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-17T15:38:56Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-16T14:07:20Z",
          "name": "Referred To"
        }
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr514ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 514\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mrs. Hinson (for herself and Mr. Golden of Maine ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a competitive bidding process for the relocation of the headquarters of Executive agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strategic Withdrawal of Agencies for Meaningful Placement Act or the SWAMP Act .\n#### 2. Relocation of headquarters of Executive agencies\n##### (a) Definitions\nIn this section:\n**(1) Executive agency**\nThe term Executive agency \u2014\n**(A)**\nhas the meaning given the term in section 105 of title 5, United States Code; and\n**(B)**\ndoes not include\u2014\n**(i)**\nthe Executive Office of the President;\n**(ii)**\nthe Department of Defense, including\u2014\n**(I)**\nthe Defense Intelligence Agency;\n**(II)**\nthe National Security Agency; and\n**(III)**\nthe National Geospatial-Intelligence Agency;\n**(iii)**\nthe Department of Energy;\n**(iv)**\nthe Department of Homeland Security;\n**(v)**\nthe Department of State;\n**(vi)**\nthe Office of the Director of National Intelligence; or\n**(vii)**\nthe Central Intelligence Agency.\n**(2) Headquarters**\nThe term headquarters \u2014\n**(A)**\nmeans the place or building serving as the managerial and administrative center of an Executive agency; and\n**(B)**\ndoes not include an office that the head of an Executive agency may maintain separately from a place or building in the Washington metropolitan area.\n**(3) State**\nThe term State means each of the 50 States.\n**(4) Washington metropolitan area**\nThe term Washington metropolitan area means the geographic area located within the boundaries of\u2014\n**(A)**\nthe District of Columbia;\n**(B)**\nMontgomery and Prince George\u2019s Counties in the State of Maryland; and\n**(C)**\nArlington, Fairfax, Loudoun, and Prince William Counties and the City of Alexandria in the Commonwealth of Virginia.\n##### (b) Prohibition on location of headquarters in Washington metropolitan area\n**(1) In general**\nSubject to paragraph (2), the headquarters of an Executive agency may not be located in the Washington metropolitan area.\n**(2) Exception**\nSubject to paragraph (3), the headquarters of an Executive agency located in the Washington metropolitan area on the date of enactment of this Act may remain in the Washington metropolitan area.\n**(3) Condition**\nWith respect to the headquarters of an Executive agency that remains in the Washington metropolitan area under paragraph (2), after the date of enactment of this Act and except as otherwise expressly provided by law\u2014\n**(A)**\nno new construction or major renovation may be undertaken on the headquarters;\n**(B)**\na lease agreement for the headquarters may not be renewed; and\n**(C)**\na new lease agreement for the headquarters may not be entered into.\n##### (c) Competitive bidding process for relocation of headquarters\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Administrator of General Services shall establish a process, in accordance with the requirements under paragraph (2), through which\u2014\n**(A)**\nthe head of an Executive agency may submit a request for the Administrator of General Services to issue a solicitation for the relocation of the headquarters of the Executive agency; or\n**(B)**\nif determined necessary, the Administrator of General Services may issue a solicitation for the relocation of the headquarters of an Executive agency.\n**(2) Requirements**\nWith respect to any solicitation issued for the relocation of the headquarters of an Executive agency under paragraph (1), the Administrator of General Services shall\u2014\n**(A)**\nallow any State and any political subdivision of a State to submit a proposal for the relocation of the headquarters of the Executive agency;\n**(B)**\nprovide the public with notice and an opportunity to comment on any proposal submitted under subparagraph (A); and\n**(C)**\nin consultation with the head of the Executive agency, select a State, or a political subdivision of a State, for the relocation of the headquarters using a competitive bidding procedure that considers\u2014\n**(i)**\nthe extent to which the relocation of the headquarters would impact the economy and workforce development of a State or political subdivision of a State;\n**(ii)**\nwhether a State, or a political subdivision of a State, has expertise in carrying out activities substantially similar to the mission and goals of the Executive agency; and\n**(iii)**\nthe extent to which the relocation of the headquarters to a State, or a political subdivision of a State, would implicate national security interests.\n##### (d) Rule of construction\nNothing in this Act shall be construed to prohibit a political subdivision of the State of Maryland or the Commonwealth of Virginia that is located outside the Washington metropolitan area from submitting a proposal under subsection (c)(2)(A).\n##### (e) Offset Allowed\nThe Administrator of General Services may use the proceeds from the sale of any Federal building or land to offset the cost of relocating the headquarters of an Executive agency.\n##### (f) No additional funds authorized\nThe Administrator of General Services shall carry out this Act using amounts otherwise made available to the Administrator of General Services, and no additional amounts are authorized to be appropriated to carry out this Act.",
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
        "actionDate": "2025-01-07",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "22",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SWAMP Act",
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
            "name": "Building construction",
            "updateDate": "2025-02-19T21:23:29Z"
          },
          {
            "name": "District of Columbia",
            "updateDate": "2025-02-19T21:23:29Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-02-19T21:23:29Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-02-19T21:23:29Z"
          },
          {
            "name": "Maryland",
            "updateDate": "2025-02-19T21:23:29Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2025-02-19T21:23:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-15T14:51:18Z"
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
          "measure-id": "id119hr514",
          "measure-number": "514",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr514v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Strategic Withdrawal of Agencies for Meaningful Placement Act or the SWAMP Act</strong></p><p>This bill prohibits new construction, major renovation, leasing, or renewing a lease of certain executive agency headquarters in the District of Columbia metropolitan area and establishes a competitive bidding process for the relocation of such headquarters.</p><p>The General Services Administration (GSA) must (1) establish a process to allow an executive agency to request the GSA to issue a solicitation for the relocation of its headquarters or allow the GSA to issue such a solicitation without a request, if necessary; (2) allow any state or political subdivision of a state to respond to a solicitation with a proposal for the relocation of the agency's headquarters; and (3) in consultation with the executive agency, select a state or political subdivision of a state for the relocation of the agency's headquarters using a competitive bidding procedure based on certain considerations.</p>"
        },
        "title": "SWAMP Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr514.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strategic Withdrawal of Agencies for Meaningful Placement Act or the SWAMP Act</strong></p><p>This bill prohibits new construction, major renovation, leasing, or renewing a lease of certain executive agency headquarters in the District of Columbia metropolitan area and establishes a competitive bidding process for the relocation of such headquarters.</p><p>The General Services Administration (GSA) must (1) establish a process to allow an executive agency to request the GSA to issue a solicitation for the relocation of its headquarters or allow the GSA to issue such a solicitation without a request, if necessary; (2) allow any state or political subdivision of a state to respond to a solicitation with a proposal for the relocation of the agency's headquarters; and (3) in consultation with the executive agency, select a state or political subdivision of a state for the relocation of the agency's headquarters using a competitive bidding procedure based on certain considerations.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr514"
    },
    "title": "SWAMP Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strategic Withdrawal of Agencies for Meaningful Placement Act or the SWAMP Act</strong></p><p>This bill prohibits new construction, major renovation, leasing, or renewing a lease of certain executive agency headquarters in the District of Columbia metropolitan area and establishes a competitive bidding process for the relocation of such headquarters.</p><p>The General Services Administration (GSA) must (1) establish a process to allow an executive agency to request the GSA to issue a solicitation for the relocation of its headquarters or allow the GSA to issue such a solicitation without a request, if necessary; (2) allow any state or political subdivision of a state to respond to a solicitation with a proposal for the relocation of the agency's headquarters; and (3) in consultation with the executive agency, select a state or political subdivision of a state for the relocation of the agency's headquarters using a competitive bidding procedure based on certain considerations.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr514"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr514ih.xml"
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
      "title": "SWAMP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SWAMP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T09:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strategic Withdrawal of Agencies for Meaningful Placement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T09:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a competitive bidding process for the relocation of the headquarters of Executive agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T09:18:20Z"
    }
  ]
}
```
