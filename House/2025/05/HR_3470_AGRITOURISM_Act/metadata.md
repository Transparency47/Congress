# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3470?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3470
- Title: AGRITOURISM Act
- Congress: 119
- Bill type: HR
- Bill number: 3470
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-03-25T08:06:10Z
- Update date including text: 2026-04-15T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-05-20 - IntroReferral: Sponsor introductory remarks on measure. (CR H2153)
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-05-20 - IntroReferral: Sponsor introductory remarks on measure. (CR H2153)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3470",
    "number": "3470",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "AGRITOURISM Act",
    "type": "HR",
    "updateDate": "2026-03-25T08:06:10Z",
    "updateDateIncludingText": "2026-04-15T16:27:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2153)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "OR"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "ME"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "VT"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "HI"
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
      "sponsorshipDate": "2025-05-20",
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
      "sponsorshipDate": "2025-05-20",
      "state": "NJ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "VA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NY"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "KS"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MD"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "WA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "PR"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3470ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3470\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Subramanyam (for himself, Mr. Rouzer , Ms. Bonamici , Mr. Harder of California , Mr. Panetta , Ms. Pingree , and Ms. Balint ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo establish in the Department of Agriculture an Office of Agritourism, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accelerating the Growth of Rural Innovation and Tourism Opportunities to Uphold Rural Industries and Sustainable Marketplaces Act or the AGRITOURISM Act .\n#### 2. Findings; Sense of Congress\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nagritourism provides a range of unique experiences to the public, including\u2014\n**(A)**\neducation, such as school tours, garden and nursery tours, winery tours, historical agricultural exhibits, hops and microbrewery tours, and distillery tours;\n**(B)**\noutdoor recreation, such as river activities, mountain biking, horseback riding, wildlife viewing and photography, fee fishing and hunting, wagon and sleigh rides, cross-country skiing, game preserves, and clay bird shooting;\n**(C)**\nentertainment, such as concerts and special events, culinary experiences, festivals, fairs, interaction with farm animals, and weddings;\n**(D)**\ndirect sales, such as on-farm sales, farm stands, agriculture-related crafts and gifts, u-pick operations, u-cut tree farms, wineries, breweries, cideries, distilleries, and cut flowers;\n**(E)**\naccommodations, such as bed-and-breakfast inns, farm and ranch vacations, yurts, sheep wagons, and guest ranches; and\n**(F)**\ndining on a farm;\n**(2)**\nagritourism has financial, educational, and social benefits to communities; and\n**(3)**\nagritourism continues\u2014\n**(A)**\nto offer educational opportunities for children and families;\n**(B)**\nto generate supplemental income for owners of agricultural enterprises, which are often small or family-run businesses;\n**(C)**\nto spur economic development in rural communities;\n**(D)**\nto preserve agricultural heritage; and\n**(E)**\nto help farms diversify.\n##### (b) Sense of Congress\nIt is the sense of Congress that, to further realize the benefits of agritourism to communities, the Secretary of Agriculture should incorporate agritourism into the Department of Agriculture comprehensively.\n#### 3. Office of Agritourism\n##### (a) In general\nThe Department of Agriculture Reorganization Act of 1994 is amended by inserting after section 216 ( 7 U.S.C. 6916 ) the following:\n217. Office of Agritourism (a) Definitions In this section: (1) Director The term Director means the Director of the Office of Agritourism described in subsection (c). (2) State The term State means\u2014 (A) each of the several States of the United States; (B) the District of Columbia; and (C) any territory of the United States. (b) Establishment The Secretary shall establish in the Department an Office of Agritourism. (c) Director The Secretary shall appoint a senior official to serve as the Director of the Office of Agritourism. (d) Duties The Director shall encourage and promote, in each State, agritourism activities and agritourism businesses, including\u2014 (1) educational experiences; (2) outdoor recreation; (3) entertainment and special events; (4) direct sales; (5) accommodations; and (6) any other activity or business relating to agritourism, as determined by the Secretary. (e) Means of achieving In carrying out subsection (d), the Director shall\u2014 (1) coordinate with the agencies and officials of the Department; (2) advise the Secretary on issues relating to agritourism; (3) ensure that the programs of the Department are updated to address best agritourism practices; (4) conduct outreach to stakeholders and coordinate external partnerships to share best practices, provide mentorship, and offer technical assistance to agritourism businesses; (5) facilitate interagency program coordination and develop interagency tools for the promotion of agritourism programs and resources; (6) review and improve farm enterprise development programs that provide information about financial literacy, business planning, and marketing for agritourism; (7) coordinate networks of agritourism businesses; and (8) collaborate with other Federal agencies, as needed. .\n##### (b) Technical amendment\nThe Department of Agriculture Reorganization Act of 1994 is amended by redesignating the first section 225 ( 7 U.S.C. 6925 ) (relating to the Food Access Liaison) as section 224A.\n##### (c) Conforming amendment\nSection 296(b) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 7014(b) ) is amended by adding at the end the following:\n(11) The authority of the Secretary to carry out section 217. .",
      "versionDate": "2025-05-15",
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
        "updateDate": "2025-06-10T22:56:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-15",
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
          "measure-id": "id119hr3470",
          "measure-number": "3470",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-15",
          "originChamber": "HOUSE",
          "update-date": "2025-06-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3470v00",
            "update-date": "2025-06-13"
          },
          "action-date": "2025-05-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Accelerating the Growth of Rural Innovation and Tourism Opportunities to Uphold Rural Industries and Sustainable Marketplaces Act or the AGRITOURISM Act</strong></p><p>This bill establishes an Office of Agritourism\u00a0within the Department of Agriculture to encourage and promote\u00a0agritourism activities and businesses in each state.</p><p>Under the bill, agritourism\u00a0activities and agritourism businesses include educational experiences,\u00a0outdoor recreation,\u00a0entertainment and special events,\u00a0direct sales, and accommodations.</p>"
        },
        "title": "AGRITOURISM Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3470.xml",
    "summary": {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Accelerating the Growth of Rural Innovation and Tourism Opportunities to Uphold Rural Industries and Sustainable Marketplaces Act or the AGRITOURISM Act</strong></p><p>This bill establishes an Office of Agritourism\u00a0within the Department of Agriculture to encourage and promote\u00a0agritourism activities and businesses in each state.</p><p>Under the bill, agritourism\u00a0activities and agritourism businesses include educational experiences,\u00a0outdoor recreation,\u00a0entertainment and special events,\u00a0direct sales, and accommodations.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr3470"
    },
    "title": "AGRITOURISM Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Accelerating the Growth of Rural Innovation and Tourism Opportunities to Uphold Rural Industries and Sustainable Marketplaces Act or the AGRITOURISM Act</strong></p><p>This bill establishes an Office of Agritourism\u00a0within the Department of Agriculture to encourage and promote\u00a0agritourism activities and businesses in each state.</p><p>Under the bill, agritourism\u00a0activities and agritourism businesses include educational experiences,\u00a0outdoor recreation,\u00a0entertainment and special events,\u00a0direct sales, and accommodations.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr3470"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3470ih.xml"
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
      "title": "AGRITOURISM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AGRITOURISM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Accelerating the Growth of Rural Innovation and Tourism Opportunities to Uphold Rural Industries and Sustainable Marketplaces Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish in the Department of Agriculture an Office of Agritourism, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:33:22Z"
    }
  ]
}
```
