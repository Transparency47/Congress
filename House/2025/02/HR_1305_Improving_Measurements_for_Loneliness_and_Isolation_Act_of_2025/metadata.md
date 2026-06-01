# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1305?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1305
- Title: Improving Measurements for Loneliness and Isolation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1305
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-03-31T19:28:46Z
- Update date including text: 2026-03-31T19:28:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1305",
    "number": "1305",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Improving Measurements for Loneliness and Isolation Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-31T19:28:46Z",
    "updateDateIncludingText": "2026-03-31T19:28:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:04:15Z",
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
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
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
      "sponsorshipDate": "2025-05-29",
      "state": "VA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "RI"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NH"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1305ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1305\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Flood (for himself and Mr. Bera ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to establish a working group to formulate recommendations for standardizing the measurements of loneliness and isolation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Measurements for Loneliness and Isolation Act of 2025 .\n#### 2. Working Group on Unifying Loneliness Research\n##### (a) Definitions\nIn this section:\n**(1)**\nThe term isolation means the objective lack of social relationships or limited social contact with others.\n**(2)**\nThe term loneliness means a subjective feeling of being isolated.\n##### (b) Establishment\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ) shall establish a national working group, to be known as the Working Group on Unifying Loneliness Research (in this section referred to as the Working Group ), to formulate recommendations for standardizing the measurements of loneliness and isolation.\n##### (c) Goals\nThe goals of the recommendations under subsection (b) shall be the following:\n**(1)**\nCollaboration, cooperation, and consultation among Federal departments and agencies with respect to developing standardized measurements of loneliness and isolation for the purposes of\u2014\n**(A)**\nhaving standardized measurements for use in public and private research, including surveys across varying populations, with the ability to capture the level of granularity needed to guide strategic decisionmaking, planning, and evaluation of strategies to combat loneliness and isolation; and\n**(B)**\nproviding reliable, consistent measurement tools for use across fields and industries in health care.\n**(2)**\nCollaboration, cooperation, and consultation among Federal departments and agencies with respect to developing standardized definitions of loneliness, isolation, and relevant terms associated with loneliness and isolation for the purposes of education, awareness, and understanding of the terms for the general public.\n**(3)**\nAssessment of the alignment of previous methods of measuring loneliness and isolation in the public and private sectors.\n##### (d) Composition\nThe Working Group shall be composed of\u2014\n**(1)**\nsenior-level representatives of\u2014\n**(A)**\nthe Department of Health and Human Services;\n**(B)**\nthe Centers for Medicare & Medicaid Services;\n**(C)**\nthe Centers for Disease Control and Prevention;\n**(D)**\nthe Administration for Community Living;\n**(E)**\nthe National Institutes of Health;\n**(F)**\nthe Substance Abuse and Mental Health Services Administration;\n**(G)**\nthe Health Resources and Services Administration;\n**(H)**\nthe Agency for Healthcare Research and Quality; and\n**(I)**\nother agencies, groups, subject matter experts, or researchers the Secretary deems beneficial to be represented in the Working Group consistent with the goals specified in subsection (c);\n**(2)**\n1 representative of each of the three States with the highest numbers of practitioners needed to remove the designations of all mental health care health professional shortage areas in the respective State (as reflected in the report of the Health Resources and Services Administration titled Designated Health Professional Shortage Areas Statistics (June 30, 2023), with each such representative designated by the Governor of the respective State; and\n**(3)**\n1 representative of the each of the three States with the lowest numbers of practitioners needed to remove such designations, with each such representative designated by the Governor of the respective State.\n##### (e) Report to Congress\n**(1) In general**\nNot later than one year after the date of enactment of this Act, the Working Group shall\u2014\n**(A)**\nsubmit to the committees listed in paragraph (3) a report describing the work and recommendations of the Working Group; and\n**(B)**\nmake such report publicly available on the internet.\n**(2) Meetings**\nThe Working Group shall meet not less than 3 times in the course of developing its report.\n**(3) Committees**\nThe committees referred to in paragraph (1)(A) are the following:\n**(A)**\nThe Committee on Education and Workforce of the House of Representatives.\n**(B)**\nThe Committee on Energy and Commerce of the House of Representatives.\n**(C)**\nThe Committee on Ways and Means of the House of Representatives.\n**(D)**\nThe Committee on Finance of the Senate.\n**(E)**\nThe Committee on Health, Education, Labor, and Pensions of the Senate.\n##### (f) Definition\nIn this section, the term State means the 50 States.\n##### (g) Sunset\nThis section shall cease to be effective at the end of calendar year 2027.",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-12-11",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3431",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Improving Measurements for Loneliness and Isolation Act of 2025",
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
            "name": "Advisory bodies",
            "updateDate": "2025-07-08T12:34:08Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-08T12:34:08Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-07-08T12:34:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-17T14:35:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1305",
          "measure-number": "1305",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-07-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1305v00",
            "update-date": "2025-07-30"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Improving Measurements for Loneliness and Isolation Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services to establish a Working Group on Unifying Loneliness Research. The working group must recommend standardized measurements of loneliness and social isolation for use in research and educating the public. The working group must report to Congress on its work and recommendations and make this information publicly available online. The working group sunsets on December 31, 2027.</p>"
        },
        "title": "Improving Measurements for Loneliness and Isolation Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1305.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Measurements for Loneliness and Isolation Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services to establish a Working Group on Unifying Loneliness Research. The working group must recommend standardized measurements of loneliness and social isolation for use in research and educating the public. The working group must report to Congress on its work and recommendations and make this information publicly available online. The working group sunsets on December 31, 2027.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119hr1305"
    },
    "title": "Improving Measurements for Loneliness and Isolation Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Measurements for Loneliness and Isolation Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services to establish a Working Group on Unifying Loneliness Research. The working group must recommend standardized measurements of loneliness and social isolation for use in research and educating the public. The working group must report to Congress on its work and recommendations and make this information publicly available online. The working group sunsets on December 31, 2027.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119hr1305"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1305ih.xml"
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
      "title": "Improving Measurements for Loneliness and Isolation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T06:38:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Measurements for Loneliness and Isolation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T06:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to establish a working group to formulate recommendations for standardizing the measurements of loneliness and isolation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T06:33:46Z"
    }
  ]
}
```
