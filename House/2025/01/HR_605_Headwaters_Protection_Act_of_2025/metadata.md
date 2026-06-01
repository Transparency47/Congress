# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/605
- Title: Headwaters Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 605
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2026-04-15T20:54:30Z
- Update date including text: 2026-04-15T20:54:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-22 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-22 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/605",
    "number": "605",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Headwaters Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-15T20:54:30Z",
    "updateDateIncludingText": "2026-04-15T20:54:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-28",
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
      "actionDate": "2025-01-22",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-28T17:12:50Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-22T15:03:00Z",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CO"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NM"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "WA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "WA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CO"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr605ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 605\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Costa (for himself, Mr. Valadao , Ms. Pettersen , Ms. Stansbury , and Ms. Perez ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Healthy Forests Restoration Act of 2003 to reauthorize and improve the Water Source Protection Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Headwaters Protection Act of 2025 .\n#### 2. Water Source Protection Program reauthorization and improvements\nSection 303 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6542 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby redesignating subparagraphs (G) and (H) as subparagraphs (K) and (L), respectively; and\n**(ii)**\nby inserting after subparagraph (F) the following:\n(G) an acequia association; (H) a local, regional, or other public entity that manages stormwater or wastewater resources or other related water infrastructure; (I) a land-grant mercedes; (J) a local, regional, or other private entity that has water delivery authority; ;\n**(B)**\nby redesignating paragraphs (1) through (7) as paragraphs (2) through (8), respectively; and\n**(C)**\nby inserting before paragraph (2) (as so redesignated) the following:\n(1) Adjacent land The term adjacent land means non-Federal land, including State, local, and private land, that is adjacent to, and within the same watershed as, National Forest System land on which a watershed protection and restoration project is carried out under this section. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby inserting and adjacent land before the period at the end;\n**(B)**\nby striking The Secretary shall and inserting the following:\n(1) In general The Secretary shall ; and\n**(C)**\nby adding at the end the following:\n(2) Requirements A watershed protection and restoration project under the Program shall\u2014 (A) protect and restore watershed health, water supply and quality, a municipal or agricultural water supply system, and water-related infrastructure; (B) protect and restore forest health from insect infestation and disease or wildfire; or (C) advance any combination of the purposes described in subparagraphs (A) and (B). (3) Priorities In selecting watershed protection and restoration projects under the Program, the Secretary shall give priority to projects that would\u2014 (A) provide risk management benefits associated with drought, wildfire, post-wildfire conditions, extreme weather, or flooding, including minimizing risks to watershed health, water supply and quality, and water-related infrastructure, including municipal and agricultural water supply systems; (B) be designed to support aquatic restoration and conservation efforts that complement existing or planned forest restoration or wildfire risk reduction efforts; (C) include\u2014 (i) partners with demonstrated capacity and success in designing and implementing ecological restoration projects, wildfire risk reduction efforts, or post-wildfire restoration projects; or (ii) in the case of disadvantaged communities that have historically lacked access to adequate resources, partners with a strong likelihood of success in designing and implementing a watershed protection and restoration project; and (D) (i) include a contribution of funds or in-kind support from non-Federal partners in an amount greater than the amount required under subsection (g)(2); (ii) provide quantifiable benefits to water supply or quality and include the use of nature-based solutions, such as restoring wetland and riparian ecosystems; (iii) be designed to improve\u2014 (I) resilience to climate change; or (II) watershed and fire resilience; or (iv) include such other characteristics as the Secretary determines to be appropriate. (4) Conditions for projects on adjacent land (A) In general No project or activity may be carried out under this section on adjacent land unless the owner of the adjacent land provides express support for, and is a willing and engaged partner in, carrying out that project or activity. (B) Effect Nothing in this section authorizes any change in\u2014 (i) the ownership of adjacent land on which a project or activity is carried out under this section; or (ii) the management of adjacent land on which a project or activity is carried out under this section, except during the carrying out of that project or activity. ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby inserting and adjacent land after watersheds ;\n**(ii)**\nby striking the period at the end and inserting ; or ;\n**(iii)**\nby striking with end water users and inserting the following: \u201cwith\u2014\n(A) end water users ; and\n**(iv)**\nby adding at the end the following:\n(B) end waters users to protect and restore the condition of National Forest watersheds and adjacent land that provide water for the benefit of another end water user. ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (C), by striking or after the semicolon;\n**(ii)**\nby redesignating subparagraph (D) as subparagraph (E); and\n**(iii)**\nby inserting after subparagraph (C) the following:\n(D) a good neighbor agreement entered into under section 8206 of the Agricultural Act of 2014 ( 16 U.S.C. 2113a ); or ; and\n**(C)**\nby adding at the end the following:\n(3) Leadership by non-Federal partners The Secretary shall facilitate a leadership role for non-Federal partners in carrying out assessments, planning, project design, and project implementation under this section. ;\n**(4)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (2), by striking shall be conducted and inserting the following: \u201cshall be\u2014\n(A) designed to protect and restore ecological integrity (as defined in section 219.19 of title 36, Code of Federal Regulations (as in effect on the date of enactment of this subparagraph)); (B) based on the best available scientific information; and (C) conducted ; and\n**(B)**\nby adding at the end the following:\n(4) Reducing redundancy An existing watershed plan, such as a watershed protection and restoration action plan developed under section 304(a)(3), or other applicable watershed planning documents may be used as the basis for a water source management plan under this subsection. ;\n**(5)**\nin subsection (e)(1), by striking purpose of\u2014 in the matter preceding subparagraph (A) and all that follows through the period at the end of subparagraph (C) and inserting purpose of advancing any of the purposes described in subsection (b)(2). ; and\n**(6)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nby striking at least equal to and inserting not less than 20 percent of ;\n**(ii)**\nby striking The Secretary and inserting the following:\n(A) In general Subject to subparagraph (B), the Secretary ; and\n**(iii)**\nby adding at the end the following:\n(B) Waiver The Secretary may waive the requirement under subparagraph (A) in the discretion of the Secretary. ; and\n**(B)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (B), by striking $10,000,000 for each of fiscal years 2019 through 2023 and inserting $30,000,000 for each of fiscal years 2025 through 2033 ; and\n**(ii)**\nby adding at the end the following:\n(D) Set-aside for partner participation in planning and capacity Of the amounts made available under subparagraph (B) to carry out this section for each fiscal year, the Secretary shall use not less than 10 percent for non-Federal partner technical assistance participation and capacity-building efforts in developing or implementing a water source management plan under subsection (d). .\n#### 3. Watershed condition framework improvements\nSection 304 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6543 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (5), by striking and at the end;\n**(B)**\nin paragraph (6), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(7) that ensures that management activities and authorizations do not result in long-term degradation of watershed health or lower the classification under paragraph (1) of any watershed in a National Forest. ; and\n**(2)**\nby adding at the end the following:\n(d) Authorization of appropriations There is authorized to be appropriated to carry out this section $30,000,000 for each of fiscal years 2025 through 2029. .\n#### 4. Effect\nNothing in this Act or an amendment made by this Act shall be construed\u2014\n**(1)**\nto supersede or in any manner affect or conflict with State water law, Federal water law, interstate compacts, or treaty obligations; or\n**(2)**\nto authorize any acquisition of land by the Federal Government or any exertion of Federal control over non-Federal land.",
      "versionDate": "2025-01-22",
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
        "actionDate": "2025-09-03",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "2701",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Headwaters Protection Act of 2025",
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
            "name": "Emergency planning and evacuation",
            "updateDate": "2025-09-05T17:26:36Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-09-05T17:26:36Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-09-05T17:26:36Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-09-05T17:26:36Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-09-05T17:26:36Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2025-09-05T17:26:36Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2025-09-05T17:26:36Z"
          },
          {
            "name": "Watersheds",
            "updateDate": "2025-09-05T17:26:36Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2025-09-05T17:26:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-02T13:44:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hr605",
          "measure-number": "605",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2026-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr605v00",
            "update-date": "2026-04-15"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Headwaters Protection Act of 2025</strong></p><p>This bill reauthorizes through FY2033 and expands the Water Source Protection Program (WSPP) under which the Forest Service carries out watershed protection and restoration projects on federal land. It also requires the Forest Service's Watershed Condition Framework for National Forest System land to ensure certain activities and authorizations do not result in long-term degradation of the health of a watershed.</p><p>The bill authorizes the WSPP to support projects on state, local, or private land that is adjacent to projects on National Forest System land, so long as (1) the adjacent land is within the same watershed as the project on federal land, and (2) the owner of the adjacent land supports the project.</p><p>Further, the bill expands the types of\u00a0end water users that may participate in the program to include (1) an\u00a0acequia association (an organization that manages traditional irrigation systems found in the Southwest); (2) a public entity that manages water infrastructure, such as stormwater or wastewater resources; (3) certain land grant entities in New Mexico called land-grant\u00a0mercedes; and (4) a local, regional, or other private entity that has water delivery authority.</p><p>The bill requires projects under the program to (1) protect and restore watershed health, water supply and quality, a municipal or agricultural water supply system, and water-related infrastructure; (2) protect and restore forest health from insect infestation and disease or wildfire; or (3) advance any combination of those purposes.</p><p>Additionally, the bill reduces the cost share for nonfederal WSPP participants.</p>"
        },
        "title": "Headwaters Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr605.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Headwaters Protection Act of 2025</strong></p><p>This bill reauthorizes through FY2033 and expands the Water Source Protection Program (WSPP) under which the Forest Service carries out watershed protection and restoration projects on federal land. It also requires the Forest Service's Watershed Condition Framework for National Forest System land to ensure certain activities and authorizations do not result in long-term degradation of the health of a watershed.</p><p>The bill authorizes the WSPP to support projects on state, local, or private land that is adjacent to projects on National Forest System land, so long as (1) the adjacent land is within the same watershed as the project on federal land, and (2) the owner of the adjacent land supports the project.</p><p>Further, the bill expands the types of\u00a0end water users that may participate in the program to include (1) an\u00a0acequia association (an organization that manages traditional irrigation systems found in the Southwest); (2) a public entity that manages water infrastructure, such as stormwater or wastewater resources; (3) certain land grant entities in New Mexico called land-grant\u00a0mercedes; and (4) a local, regional, or other private entity that has water delivery authority.</p><p>The bill requires projects under the program to (1) protect and restore watershed health, water supply and quality, a municipal or agricultural water supply system, and water-related infrastructure; (2) protect and restore forest health from insect infestation and disease or wildfire; or (3) advance any combination of those purposes.</p><p>Additionally, the bill reduces the cost share for nonfederal WSPP participants.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119hr605"
    },
    "title": "Headwaters Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Headwaters Protection Act of 2025</strong></p><p>This bill reauthorizes through FY2033 and expands the Water Source Protection Program (WSPP) under which the Forest Service carries out watershed protection and restoration projects on federal land. It also requires the Forest Service's Watershed Condition Framework for National Forest System land to ensure certain activities and authorizations do not result in long-term degradation of the health of a watershed.</p><p>The bill authorizes the WSPP to support projects on state, local, or private land that is adjacent to projects on National Forest System land, so long as (1) the adjacent land is within the same watershed as the project on federal land, and (2) the owner of the adjacent land supports the project.</p><p>Further, the bill expands the types of\u00a0end water users that may participate in the program to include (1) an\u00a0acequia association (an organization that manages traditional irrigation systems found in the Southwest); (2) a public entity that manages water infrastructure, such as stormwater or wastewater resources; (3) certain land grant entities in New Mexico called land-grant\u00a0mercedes; and (4) a local, regional, or other private entity that has water delivery authority.</p><p>The bill requires projects under the program to (1) protect and restore watershed health, water supply and quality, a municipal or agricultural water supply system, and water-related infrastructure; (2) protect and restore forest health from insect infestation and disease or wildfire; or (3) advance any combination of those purposes.</p><p>Additionally, the bill reduces the cost share for nonfederal WSPP participants.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119hr605"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr605ih.xml"
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
      "title": "Headwaters Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Headwaters Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Healthy Forests Restoration Act of 2003 to reauthorize and improve the Water Source Protection Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T04:18:32Z"
    }
  ]
}
```
