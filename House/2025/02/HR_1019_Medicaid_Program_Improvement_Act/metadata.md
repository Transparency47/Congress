# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1019?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1019
- Title: Medicaid Program Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 1019
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-06-16T11:33:16Z
- Update date including text: 2025-06-16T11:33:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1019",
    "number": "1019",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001215",
        "district": "1",
        "firstName": "Mariannette",
        "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
        "lastName": "Miller-Meeks",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Medicaid Program Improvement Act",
    "type": "HR",
    "updateDate": "2025-06-16T11:33:16Z",
    "updateDateIncludingText": "2025-06-16T11:33:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
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
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:01:50Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1019ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1019\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mrs. Miller-Meeks (for herself and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to ensure the reliability of address information provided under the Medicaid program.\n#### 1. Short title\nThis Act may be cited as the Medicaid Program Improvement Act .\n#### 2. Ensuring the reliability of address information provided under the Medicaid program\n##### (a) In general\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ) is amended\u2014\n**(1)**\nin paragraph (86), by striking and at the end;\n**(2)**\nin paragraph (87)(D), by striking the period at the end and inserting ; and ; and\n**(3)**\nby inserting after paragraph (87) the following new paragraph:\n(88) beginning January 1, 2026, provide for a process to regularly obtain address information for individuals enrolled under such plan (or a waiver of such plan) from reliable data sources (as described in section 435.919(f)(1)(iii) of title 42, Code of Federal Regulations (or a successor regulation)) and act on any changes to such an address based on such information in accordance with such section (or successor regulation), except that this paragraph shall only apply in the case of the 50 States and the District of Columbia. .\n##### (b) Application to CHIP\nSection 2107(e)(1) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (H) through (U) as subparagraphs (I) through (V), respectively; and\n**(2)**\nby inserting after subparagraph (G) the following new subparagraph:\n(H) Section 1902(a)(88) (relating to regularly obtaining address information for enrollees). .\n##### (c) Ensuring transmission of address information from managed care organizations\nSection 1932 of the Social Security Act ( 42 U.S.C. 1396u\u20132 ) is amended by adding at the end the following new subsection:\n(j) Transmission of address information Beginning January 1, 2026, each contract under a State plan with a managed care entity under section 1903(m) shall provide that the entity transmits to the State any address information for an individual enrolled with the entity that is provided to such entity directly from, or verified by such entity directly with, such individual. .",
      "versionDate": "2025-02-05",
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
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
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
            "name": "Child health",
            "updateDate": "2025-04-11T18:42:02Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-04-11T18:42:02Z"
          },
          {
            "name": "Poverty and welfare assistance",
            "updateDate": "2025-04-11T18:42:02Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-04-11T18:42:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-10T15:01:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119hr1019",
          "measure-number": "1019",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-05",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1019v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Medicaid Program Improvement Act</strong></p><p>This bill provides statutory authority for the requirement that state Medicaid programs and the Children's Health Insurance Program (CHIP) have a process in place to obtain updated addresses for enrollees. It also requires contracted managed care plans to report addresses that have been directly verified by enrollees to states.</p>"
        },
        "title": "Medicaid Program Improvement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1019.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicaid Program Improvement Act</strong></p><p>This bill provides statutory authority for the requirement that state Medicaid programs and the Children's Health Insurance Program (CHIP) have a process in place to obtain updated addresses for enrollees. It also requires contracted managed care plans to report addresses that have been directly verified by enrollees to states.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr1019"
    },
    "title": "Medicaid Program Improvement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicaid Program Improvement Act</strong></p><p>This bill provides statutory authority for the requirement that state Medicaid programs and the Children's Health Insurance Program (CHIP) have a process in place to obtain updated addresses for enrollees. It also requires contracted managed care plans to report addresses that have been directly verified by enrollees to states.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr1019"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1019ih.xml"
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
      "title": "Medicaid Program Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T03:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicaid Program Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to ensure the reliability of address information provided under the Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:29Z"
    }
  ]
}
```
