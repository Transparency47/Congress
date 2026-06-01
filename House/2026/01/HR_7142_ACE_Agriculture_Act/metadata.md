# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7142?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7142
- Title: ACE Agriculture Act
- Congress: 119
- Bill type: HR
- Bill number: 7142
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-04-16T16:07:05Z
- Update date including text: 2026-04-16T16:07:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7142",
    "number": "7142",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "ACE Agriculture Act",
    "type": "HR",
    "updateDate": "2026-04-16T16:07:05Z",
    "updateDateIncludingText": "2026-04-16T16:07:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
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
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
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
          "date": "2026-01-16T20:00:05Z",
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
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "IA"
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
      "sponsorshipDate": "2026-01-27",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7142ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7142\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mr. Panetta (for himself and Mr. Feenstra ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the National Agricultural Research, Extension, and Teaching Policy Act of 1977 to extend and permanently authorize the Agriculture Advanced Research and Development Authority, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Cutting Edge Agriculture Act or the ACE Agriculture Act .\n#### 2. Reauthorization of AGARDA\nSection 1473H of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3319k ) is amended\u2014\n**(1)**\nin the section heading, by striking pilot ;\n**(2)**\nin subsection (a)(6), by striking growing, and inserting growing (including water conservation technologies and innovation), ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking pilot ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby amending subparagraph (B) to read as follows:\n(B) to overcome the long term and high-risk technological barriers in the development of agricultural technologies, research tools, and qualified products and projects that enhance export competitiveness, environmental sustainability, water conservation, the reduction, avoidance, sequestration, or mitigation of greenhouse gas emissions, and resilience to extreme weather, drought, infectious diseases, plant and animal pathogens, and plant and animal pests; ; and\n**(ii)**\nin subparagraph (D), by inserting or economic cost after financial uncertainty ;\n**(C)**\nin paragraph (3)(B)\u2014\n**(i)**\nin clause (ii), in the matter preceding subclause (I), by striking advise the Chief Scientist on, and ; and\n**(ii)**\nby amending clause (iii) to read as follows:\n(iii) Relationship within the department of agriculture (I) Chief scientist The Director shall report to the Chief Scientist. (II) Other programs No other official who is the head of any other program of the Department of Agriculture shall report to the Director. ;\n**(D)**\nin paragraph (6), by striking pilot each place it appears in subparagraphs (A) and (B); and\n**(E)**\nby amending paragraph (9) to read as follows:\n(9) Personnel matters (A) In general The Director shall establish and maintain within the AGARDA a staff with sufficient qualifications and expertise to enable the AGARDA to carry out the responsibilities of the AGARDA under this section in conjunction with other operations of the Department of Agriculture. (B) Use of existing personnel authorities In carrying out this subsection, the Secretary may appoint highly qualified individuals to scientific or professional positions on the same terms and conditions as provided in subsections (b)(3), (b)(4), (c), (d), (e), and (f) of section 620 of the Agricultural Research, Extension, and Education Reform Act of 1998 ( 7 U.S.C. 7657 ). ;\n**(4)**\nin subsection (c), by adding at the end the following:\n(4) Use of strategic plan The Secretary shall use the strategic plan developed under paragraph (1) to inform the administration of the AGARDA under this section. ;\n**(5)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (2), by striking subparagraph (C);\n**(B)**\nin paragraph (3), by striking $50,000,000 for each of fiscal years 2019 through 2023 and inserting $100,000,000 for each of fiscal years 2027 through 2032 ; and\n**(C)**\nby adding at the end the following:\n(4) Other funding In addition to amounts otherwise made available to carry out this section, the Secretary may use to carry out this section other funds available to the Secretary for any other purpose. (5) Clarification Nothing in paragraph (2) or (4) authorizes the use of the funds of the Commodity Credit Corporation to carry out this section. ; and\n**(6)**\nby striking subsection (e).",
      "versionDate": "2026-01-16",
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
        "updateDate": "2026-02-13T16:33:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-16",
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
          "measure-id": "id119hr7142",
          "measure-number": "7142",
          "measure-type": "hr",
          "orig-publish-date": "2026-01-16",
          "originChamber": "HOUSE",
          "update-date": "2026-04-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7142v00",
            "update-date": "2026-04-16"
          },
          "action-date": "2026-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Advancing Cutting Edge Agriculture Act or the ACE Agriculture Act</strong></p><p>This bill reauthorizes the Agriculture Advanced Research and Development Authority (AGARDA) through FY2032 and expands the program's environmental sustainability goals. This Department of Agriculture (USDA) program supports innovative research and development of technology, research tools, and products to address long-term and high-risk challenges related to food and agriculture.</p><p>The bill expands the program's goals to include</p><ul><li>water conservation;</li><li>responding to greenhouse gas emissions; and</li><li>resilience to drought, infectious diseases, and plant and animal pathogens and pests.</li></ul><p>The bill also expands the program's goals to include undertaking advanced research and development in areas in which industry by itself is not likely to do so because of economic cost.</p><p>Further, the bill removes the current pilot program designation and requires USDA to establish and maintain an AGARDA staff.</p><p>Finally, the bill allows USDA to use any unobligated USDA funds to implement the program.</p>"
        },
        "title": "ACE Agriculture Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7142.xml",
    "summary": {
      "actionDate": "2026-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Advancing Cutting Edge Agriculture Act or the ACE Agriculture Act</strong></p><p>This bill reauthorizes the Agriculture Advanced Research and Development Authority (AGARDA) through FY2032 and expands the program's environmental sustainability goals. This Department of Agriculture (USDA) program supports innovative research and development of technology, research tools, and products to address long-term and high-risk challenges related to food and agriculture.</p><p>The bill expands the program's goals to include</p><ul><li>water conservation;</li><li>responding to greenhouse gas emissions; and</li><li>resilience to drought, infectious diseases, and plant and animal pathogens and pests.</li></ul><p>The bill also expands the program's goals to include undertaking advanced research and development in areas in which industry by itself is not likely to do so because of economic cost.</p><p>Further, the bill removes the current pilot program designation and requires USDA to establish and maintain an AGARDA staff.</p><p>Finally, the bill allows USDA to use any unobligated USDA funds to implement the program.</p>",
      "updateDate": "2026-04-16",
      "versionCode": "id119hr7142"
    },
    "title": "ACE Agriculture Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Advancing Cutting Edge Agriculture Act or the ACE Agriculture Act</strong></p><p>This bill reauthorizes the Agriculture Advanced Research and Development Authority (AGARDA) through FY2032 and expands the program's environmental sustainability goals. This Department of Agriculture (USDA) program supports innovative research and development of technology, research tools, and products to address long-term and high-risk challenges related to food and agriculture.</p><p>The bill expands the program's goals to include</p><ul><li>water conservation;</li><li>responding to greenhouse gas emissions; and</li><li>resilience to drought, infectious diseases, and plant and animal pathogens and pests.</li></ul><p>The bill also expands the program's goals to include undertaking advanced research and development in areas in which industry by itself is not likely to do so because of economic cost.</p><p>Further, the bill removes the current pilot program designation and requires USDA to establish and maintain an AGARDA staff.</p><p>Finally, the bill allows USDA to use any unobligated USDA funds to implement the program.</p>",
      "updateDate": "2026-04-16",
      "versionCode": "id119hr7142"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7142ih.xml"
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
      "title": "ACE Agriculture Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ACE Agriculture Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advancing Cutting Edge Agriculture Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Agricultural Research, Extension, and Teaching Policy Act of 1977 to extend and permanently authorize the Agriculture Advanced Research and Development Authority, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T05:03:25Z"
    }
  ]
}
```
