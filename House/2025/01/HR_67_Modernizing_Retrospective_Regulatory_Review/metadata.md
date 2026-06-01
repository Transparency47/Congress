# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/67?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/67
- Title: Modernizing Retrospective Regulatory Review
- Congress: 119
- Bill type: HR
- Bill number: 67
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-01-26T20:20:18Z
- Update date including text: 2026-01-26T20:20:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported by the Yeas and Nays: 24 - 18.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported by the Yeas and Nays: 24 - 18.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/67",
    "number": "67",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Modernizing Retrospective Regulatory Review",
    "type": "HR",
    "updateDate": "2026-01-26T20:20:18Z",
    "updateDateIncludingText": "2026-01-26T20:20:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 24 - 18.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
        "item": [
          {
            "date": "2025-05-21T20:25:18Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-03T16:08:25Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr67ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 67\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Mr. Crane ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo improve retrospective reviews of Federal regulations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modernizing Retrospective Regulatory Review Act .\n#### 2. Improving retrospective reviews of existing Federal regulations\n##### (a) Report on availability of existing regulations in machine-Readable format\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Director of the Office of Management and Budget, acting through the Administrator and in consultation with the Director of GPO, the Archivist, and the Director of the Federal Register, shall submit to the appropriate congressional committees, a report on the progress of the Federal Government in making regulations of agencies available in machine-readable format.\n**(2) Contents of report**\nThe report required by paragraph (1) shall include\u2014\n**(A)**\nan assessment of whether regulations of agencies have been made available in a machine-readable format to the public; and\n**(B)**\ninformation regarding the recognition by the Administrative Committee of the Federal Register of the eCFR maintained by the Director of the Federal Register and the Director of GPO as an official legal edition of the Code of Federal Regulations.\n##### (b) Guidance on using technology To conduct retrospective reviews\n**(1) In general**\nNot later than 18 months after the date of the enactment of this Act, the Director of the Office of Management and Budget, acting through the Administrator, shall issue guidance on how the head of the agency can\u2014\n**(A)**\nidentify, procure, and use technology (including algorithmic tools and artificial intelligence) to more efficiently, cost-effectively, and accurately conduct any retrospective review of the existing regulations of the agency, including to more efficiently, cost-effectively, and accurately identify through any such review regulations of the agency that\u2014\n**(i)**\nare obsolete, ineffective, insufficient, excessively burdensome, or redundant;\n**(ii)**\nshould be improved;\n**(iii)**\ncontain typographic errors;\n**(iv)**\ncontain inaccurate cross-references; or\n**(v)**\ncontradict or overlap with each other, or any standards of the agency; and\n**(B)**\nadequately train personnel of the agency on how to use such technology.\n**(2) Development of guidance**\nIn developing the guidance required pursuant to paragraph (1), the Administrator shall take into account any assessment or information included in the report required by subsection (a).\n##### (c) Agency retrospective review plan\nNot later than 2 years after the date of the enactment of this Act, the head of each agency shall submit to the Administrator and the appropriate congressional committees a plan that\u2014\n**(1)**\nincludes a detailed strategy for implementing the guidance issued pursuant to subsection (b) with respect to the regulations of the agency;\n**(2)**\nidentifies any regulation of the agency, or categories of regulations of the agency, that the head of the agency\u2014\n**(A)**\nis required by law to review after the applicable regulation is issued; or\n**(B)**\ndetermines would benefit from being reviewed after the regulation is issued; and\n**(3)**\nincludes any additional information, data, or ex-post analysis determined necessary or useful by the head of the agency.\n##### (d) Agency implementation\nNot later than 180 days after the date on which the head of an agency submits the plan required by subsection (c), the head of the agency shall implement the strategy included in such plan with respect to any retrospective review of an existing regulation of the agency.\n##### (e) Definitions\nIn this section:\n**(1) Administrative Committee of the Federal Register**\nThe term Administrative Committee of the Federal Register means the Committee established under section 1506 of title 44, United States Code.\n**(2) Administrator**\nThe term Administrator means the Administrator of the Office of Information and Regulatory Affairs.\n**(3) Agency**\nThe term agency has the meaning given that term in section 3502 of title 44, United States Code.\n**(4) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Oversight and Government Reform of the House of Representatives; and\n**(B)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate.\n**(5) Director of GPO**\nThe term Director of GPO means the Director of the Government Publishing Office.\n**(6) Machine-readable**\nThe term machine-readable has the meaning given the term in section 3502 of title 44, United States Code.\n**(7) Retrospective review of an existing regulation of the agency**\nThe term retrospective review of an existing regulation of the agency means a review of a regulation of the agency conducted after the regulation has been issued, including any such review required by law or determined appropriate by the head of the agency.",
      "versionDate": "2025-01-03",
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
        "actionDate": "2025-02-20",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "644",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Modernizing Retrospective Regulatory Review Act",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-05T15:24:56Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-03-05T15:24:56Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-05T15:24:56Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-05T15:24:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-27T16:03:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr67",
          "measure-number": "67",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr67v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Modernizing Retrospective Regulatory Review Act</strong></p><p>This bill requires the Office of Information and Regulatory Affairs (OIRA) to issue guidance for using technology to retrospectively review existing federal regulations and, in consultation with relevant agencies, report on the progress of the federal government in making agency regulations available in a machine-readable format.</p><p>Specifically, the OIRA\u00a0report must (1) assess whether regulations of agencies have been made available to the public in a machine-readable format, and (2) provide information about the recognition by the Administrative\u00a0Committee of the Federal Register of the Electronic Code of Federal Regulations (eCFR) as an official legal edition of the Code of Federal Regulations. Currently, the content of the eCFR is authoritative but unofficial.</p><p>Additionally, not later than 18 months after the enactment of this bill, the OIRA must issue guidance about how a federal agency can use technology to retrospectively review the agency's existing regulations. Each agency must plan and implement a strategy to comply with the\u00a0OIRA's guidance for the retrospective review.</p>"
        },
        "title": "Modernizing Retrospective Regulatory Review"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr67.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Modernizing Retrospective Regulatory Review Act</strong></p><p>This bill requires the Office of Information and Regulatory Affairs (OIRA) to issue guidance for using technology to retrospectively review existing federal regulations and, in consultation with relevant agencies, report on the progress of the federal government in making agency regulations available in a machine-readable format.</p><p>Specifically, the OIRA\u00a0report must (1) assess whether regulations of agencies have been made available to the public in a machine-readable format, and (2) provide information about the recognition by the Administrative\u00a0Committee of the Federal Register of the Electronic Code of Federal Regulations (eCFR) as an official legal edition of the Code of Federal Regulations. Currently, the content of the eCFR is authoritative but unofficial.</p><p>Additionally, not later than 18 months after the enactment of this bill, the OIRA must issue guidance about how a federal agency can use technology to retrospectively review the agency's existing regulations. Each agency must plan and implement a strategy to comply with the\u00a0OIRA's guidance for the retrospective review.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr67"
    },
    "title": "Modernizing Retrospective Regulatory Review"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Modernizing Retrospective Regulatory Review Act</strong></p><p>This bill requires the Office of Information and Regulatory Affairs (OIRA) to issue guidance for using technology to retrospectively review existing federal regulations and, in consultation with relevant agencies, report on the progress of the federal government in making agency regulations available in a machine-readable format.</p><p>Specifically, the OIRA\u00a0report must (1) assess whether regulations of agencies have been made available to the public in a machine-readable format, and (2) provide information about the recognition by the Administrative\u00a0Committee of the Federal Register of the Electronic Code of Federal Regulations (eCFR) as an official legal edition of the Code of Federal Regulations. Currently, the content of the eCFR is authoritative but unofficial.</p><p>Additionally, not later than 18 months after the enactment of this bill, the OIRA must issue guidance about how a federal agency can use technology to retrospectively review the agency's existing regulations. Each agency must plan and implement a strategy to comply with the\u00a0OIRA's guidance for the retrospective review.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr67"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr67ih.xml"
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
      "title": "Modernizing Retrospective Regulatory Review",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modernizing Retrospective Regulatory Review",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve retrospective reviews of Federal regulations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T03:33:20Z"
    }
  ]
}
```
