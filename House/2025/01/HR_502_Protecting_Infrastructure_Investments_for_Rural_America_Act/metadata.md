# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/502?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/502
- Title: Protecting Infrastructure Investments for Rural America Act
- Congress: 119
- Bill type: HR
- Bill number: 502
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-02-20T13:46:07Z
- Update date including text: 2025-02-20T13:46:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-17 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-17 - Committee: Referred to the Subcommittee on Highways and Transit.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/502",
    "number": "502",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Protecting Infrastructure Investments for Rural America Act",
    "type": "HR",
    "updateDate": "2025-02-20T13:46:07Z",
    "updateDateIncludingText": "2025-02-20T13:46:07Z"
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
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
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
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
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
          "date": "2025-01-16T14:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-17T15:37:31Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MN"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "KS"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MN"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NE"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr502ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 502\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Finstad (for himself, Mr. Golden of Maine , Mr. Stauber , Mr. Mann , Mrs. Fischbach , Mr. Van Orden , and Mr. Moolenaar ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo ensure the rural surface transportation grant program is accessible to rural areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Infrastructure Investments for Rural America Act .\n#### 2. Rural surface transportation grant program\nSection 173 of title 23, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2) by striking over 200,000 and inserting 30,000 or less ; and\n**(B)**\nby adding at the end the following:\n(3) Small community The term small community means an area that is outside an urbanized area and that has a population of 5,000 or less. ;\n**(2)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (B) by striking and at the end;\n**(B)**\nin subparagraph (C) by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(D) to generate economic growth and development in rural areas to improve the quality of life for citizens in rural areas and small communities. ;\n**(3)**\nin subsection (e)(1)\u2014\n**(A)**\nin subparagraph (F) by striking or at the end;\n**(B)**\nin subparagraph (G) by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(H) a highway, road, bridge, or tunnel project that would benefit the economic development or quality of life for citizens of the community in which the project takes place. ;\n**(4)**\nby striking subsection (i);\n**(5)**\nby redesignating subsections (j), (k), (l), (m), (n), and (o) as subsections (i), (j), (k), (l), (m), and (n), respectively;\n**(6)**\nin subsection (i) (as so redesignated)\u2014\n**(A)**\nin paragraph (1) by striking paragraph (2) and inserting paragraphs (2) or (3) ;\n**(B)**\nby redesignating paragraph (3) as paragraph (4); and\n**(C)**\nby inserting after paragraph (2) the following:\n(3) Federal share for projects in small communities The Federal share of the cost of a project carried out in a small community with a grant under the program may not exceed 90 percent. ;\n**(7)**\nin subsection (j) (as so redesignated) by striking paragraph (1) and inserting the following:\n(1) Projects in small communities The Secretary shall use not less than 5 percent of the amounts made available for the program for each fiscal year to provide grants for eligible projects in a small community. ; and\n**(8)**\nin subsection (l) (as so redesignated) by striking subsection (l)(1) and inserting subsection (k)(1) .",
      "versionDate": "2025-01-16",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-13T19:59:19Z"
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
          "measure-id": "id119hr502",
          "measure-number": "502",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr502v00",
            "update-date": "2025-02-20"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Infrastructure Investments for Rural America Act </strong></p><p>This bill modifies the definition of rural area that is used for the Rural Surface Transportation Grant Program and adds provisions for small communities.</p><p>As background, the grant program supports projects that improve and expand the surface transportation infrastructure in rural areas. Eligible applicants for the grant program include states, regional transportation planning organizations, local governments, and tribal governments.</p><p>For purposes of the program, the bill defines <em>rural area </em>as an area outside an urbanized area that has a population of 30,000 or less.\u00a0Current law requires a rural area to be outside of an urbanized area with a population of over 200,000.</p><p>The bill includes provisions for small communities (i.e., an area outside an urbanized area and\u00a0that has a population of 5,000 or less). The bill sets the maximum federal cost-share at 90% for project grants carried out in a small community. The Department of Transportation (DOT) must use at least 5% of the program's annual funds to provide grants for projects in\u00a0small communities.\u00a0The bill also removes the prohibition against DOT using more than 10% of program funds for grants that are under $25 million.</p><p>Further, program grants may be used for highway, road, bridge, or tunnel projects that would benefit the economic development or quality of life for citizens of the local community.</p><p>The bill also specifies that the program's goals include the generation of economic growth and development in rural areas.\u00a0</p>"
        },
        "title": "Protecting Infrastructure Investments for Rural America Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr502.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Infrastructure Investments for Rural America Act </strong></p><p>This bill modifies the definition of rural area that is used for the Rural Surface Transportation Grant Program and adds provisions for small communities.</p><p>As background, the grant program supports projects that improve and expand the surface transportation infrastructure in rural areas. Eligible applicants for the grant program include states, regional transportation planning organizations, local governments, and tribal governments.</p><p>For purposes of the program, the bill defines <em>rural area </em>as an area outside an urbanized area that has a population of 30,000 or less.\u00a0Current law requires a rural area to be outside of an urbanized area with a population of over 200,000.</p><p>The bill includes provisions for small communities (i.e., an area outside an urbanized area and\u00a0that has a population of 5,000 or less). The bill sets the maximum federal cost-share at 90% for project grants carried out in a small community. The Department of Transportation (DOT) must use at least 5% of the program's annual funds to provide grants for projects in\u00a0small communities.\u00a0The bill also removes the prohibition against DOT using more than 10% of program funds for grants that are under $25 million.</p><p>Further, program grants may be used for highway, road, bridge, or tunnel projects that would benefit the economic development or quality of life for citizens of the local community.</p><p>The bill also specifies that the program's goals include the generation of economic growth and development in rural areas.\u00a0</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119hr502"
    },
    "title": "Protecting Infrastructure Investments for Rural America Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Infrastructure Investments for Rural America Act </strong></p><p>This bill modifies the definition of rural area that is used for the Rural Surface Transportation Grant Program and adds provisions for small communities.</p><p>As background, the grant program supports projects that improve and expand the surface transportation infrastructure in rural areas. Eligible applicants for the grant program include states, regional transportation planning organizations, local governments, and tribal governments.</p><p>For purposes of the program, the bill defines <em>rural area </em>as an area outside an urbanized area that has a population of 30,000 or less.\u00a0Current law requires a rural area to be outside of an urbanized area with a population of over 200,000.</p><p>The bill includes provisions for small communities (i.e., an area outside an urbanized area and\u00a0that has a population of 5,000 or less). The bill sets the maximum federal cost-share at 90% for project grants carried out in a small community. The Department of Transportation (DOT) must use at least 5% of the program's annual funds to provide grants for projects in\u00a0small communities.\u00a0The bill also removes the prohibition against DOT using more than 10% of program funds for grants that are under $25 million.</p><p>Further, program grants may be used for highway, road, bridge, or tunnel projects that would benefit the economic development or quality of life for citizens of the local community.</p><p>The bill also specifies that the program's goals include the generation of economic growth and development in rural areas.\u00a0</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119hr502"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr502ih.xml"
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
      "title": "Protecting Infrastructure Investments for Rural America Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Infrastructure Investments for Rural America Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure the rural surface transportation grant program is accessible to rural areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T05:18:18Z"
    }
  ]
}
```
