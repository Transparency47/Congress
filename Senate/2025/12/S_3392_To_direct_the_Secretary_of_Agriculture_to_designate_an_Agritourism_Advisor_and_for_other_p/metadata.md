# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3392?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3392
- Title: AGRITOURISM Act
- Congress: 119
- Bill type: S
- Bill number: 3392
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-04-08T14:01:01Z
- Update date including text: 2026-04-08T14:01:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3392",
    "number": "3392",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "AGRITOURISM Act",
    "type": "S",
    "updateDate": "2026-04-08T14:01:01Z",
    "updateDateIncludingText": "2026-04-08T14:01:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-12-09T19:27:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "NC"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "OR"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "NC"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "VT"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CO"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "WI"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NM"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "WA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NV"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CT"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "WY"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "WV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "IL"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3392is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3392\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. Wyden (for himself, Mr. Budd , Mr. Merkley , Mr. Tillis , Mr. Welch , Mr. Bennet , Ms. Baldwin , Mrs. Gillibrand , Mr. Heinrich , Mrs. Murray , Ms. Rosen , Mr. Blumenthal , Ms. Lummis , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo direct the Secretary of Agriculture to designate an Agritourism Advisor, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accelerating the Growth of Rural Innovation and Tourism Opportunities to Uphold Rural Industries and Sustainable Marketplaces Act or the AGRITOURISM Act .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nagritourism provides a range of unique experiences to the public, including\u2014\n**(A)**\neducation, such as school tours, garden and nursery tours, winery tours, historical agricultural exhibits, hops and microbrewery tours, and distillery tours;\n**(B)**\noutdoor recreation, such as river activities, mountain biking, horseback riding, wildlife viewing and photography, fee fishing and hunting, wagon and sleigh rides, cross-country skiing, game preserves, and clay bird shooting;\n**(C)**\nentertainment, such as concerts and special events, culinary experiences, festivals, fairs, interaction with farm animals, and weddings;\n**(D)**\ndirect sales, such as on-farm sales, farm stands, agriculture-related crafts and gifts, u-pick operations, u-cut tree farms, wineries, breweries, cideries, distilleries, and cut flowers;\n**(E)**\naccommodations, such as bed-and-breakfast inns, farm and ranch vacations, yurts, sheep wagons, and guest ranches; and\n**(F)**\ndining on a farm;\n**(2)**\nagritourism has financial, educational, and social benefits to communities; and\n**(3)**\nagritourism continues\u2014\n**(A)**\nto offer educational opportunities for children and families;\n**(B)**\nto generate supplemental income for owners of agricultural enterprises, which are often small or family-run businesses;\n**(C)**\nto spur economic development in rural communities;\n**(D)**\nto preserve agricultural heritage;\n**(E)**\nto help farms diversify; and\n**(F)**\nto provide alternative revenue opportunities to keep working farms in production.\n##### (b) Sense of Congress\nIt is the sense of Congress that, to further realize the benefits of agritourism to communities, the Secretary of Agriculture should incorporate agritourism into the Department of Agriculture comprehensively.\n#### 3. Agritourism Advisor\n##### (a) In general\nSubtitle C of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6941 et seq. ) is amended by adding at the end the following:\n237. Agritourism Advisor (a) Definitions In this section: (1) Advisor The term Advisor means the Agritourism Advisor described in subsection (b). (2) State The term State means\u2014 (A) each of the several States of the United States; (B) the District of Columbia; and (C) any territory of the United States. (b) Advisor The Secretary shall designate a senior official in the Office of the Under Secretary for Rural Development to serve as the Agritourism Advisor. (c) Duties The Advisor shall encourage and promote, in each State and on land under the jurisdiction of Indian Tribes (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )), agritourism activities and agritourism businesses, including\u2014 (1) educational experiences; (2) outdoor recreation; (3) entertainment and special events; (4) direct sales; (5) accommodations; and (6) any other activity or business relating to agritourism, as determined by the Secretary. (d) Means of achieving In carrying out subsection (c), the Advisor shall\u2014 (1) coordinate with the agencies and officials of the Department; (2) advise the Secretary on issues relating to agritourism; (3) ensure that the programs of the Department are updated to address best agritourism practices; (4) conduct outreach to stakeholders and coordinate external partnerships to share best practices, provide mentorship, and offer technical assistance to agritourism businesses; (5) facilitate interagency program coordination and develop interagency tools for the promotion of agritourism programs and resources; (6) review and improve farm enterprise development programs that provide information about financial literacy, business planning, and marketing for agritourism; (7) coordinate networks of agritourism businesses; (8) consolidate access to Federal resources to help agritourism businesses effectively navigate available programs and assistance; and (9) collaborate with other Federal agencies, as needed. .\n##### (b) Technical amendment\nThe Department of Agriculture Reorganization Act of 1994 is amended by redesignating the first section 225 ( 7 U.S.C. 6925 ) (relating to the Food Access Liaison) as section 224A.\n##### (c) Conforming amendment\nSection 296(b) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 7014(b) ) is amended by adding at the end the following:\n(11) The authority of the Secretary to carry out section 237. .",
      "versionDate": "2025-12-09",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-01-07T16:08:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-09",
    "originChamber": "Senate",
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
          "measure-id": "id119s3392",
          "measure-number": "3392",
          "measure-type": "s",
          "orig-publish-date": "2025-12-09",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3392v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-12-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Accelerating the Growth of Rural Innovation and Tourism Opportunities to Uphold Rural Industries and Sustainable Marketplaces Act or the AGRITOURISM Act</strong></p><p>This bill directs the Department of Agriculture to designate an\u00a0Agritourism Advisor within the\u00a0Office of the Under Secretary for Rural Development. The advisor must encourage and promote\u00a0agritourism activities and businesses in each state and on land under the jurisdiction of Indian tribes.</p><p>Under the bill, agritourism\u00a0activities and agritourism businesses include educational experiences,\u00a0outdoor recreation,\u00a0entertainment and special events,\u00a0direct sales, and accommodations.</p>"
        },
        "title": "AGRITOURISM Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3392.xml",
    "summary": {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Accelerating the Growth of Rural Innovation and Tourism Opportunities to Uphold Rural Industries and Sustainable Marketplaces Act or the AGRITOURISM Act</strong></p><p>This bill directs the Department of Agriculture to designate an\u00a0Agritourism Advisor within the\u00a0Office of the Under Secretary for Rural Development. The advisor must encourage and promote\u00a0agritourism activities and businesses in each state and on land under the jurisdiction of Indian tribes.</p><p>Under the bill, agritourism\u00a0activities and agritourism businesses include educational experiences,\u00a0outdoor recreation,\u00a0entertainment and special events,\u00a0direct sales, and accommodations.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3392"
    },
    "title": "AGRITOURISM Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Accelerating the Growth of Rural Innovation and Tourism Opportunities to Uphold Rural Industries and Sustainable Marketplaces Act or the AGRITOURISM Act</strong></p><p>This bill directs the Department of Agriculture to designate an\u00a0Agritourism Advisor within the\u00a0Office of the Under Secretary for Rural Development. The advisor must encourage and promote\u00a0agritourism activities and businesses in each state and on land under the jurisdiction of Indian tribes.</p><p>Under the bill, agritourism\u00a0activities and agritourism businesses include educational experiences,\u00a0outdoor recreation,\u00a0entertainment and special events,\u00a0direct sales, and accommodations.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3392"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3392is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-12-31T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AGRITOURISM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Accelerating the Growth of Rural Innovation and Tourism Opportunities to Uphold Rural Industries and Sustainable Marketplaces Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Agriculture to designate an Agritourism Advisor, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:33:14Z"
    }
  ]
}
```
