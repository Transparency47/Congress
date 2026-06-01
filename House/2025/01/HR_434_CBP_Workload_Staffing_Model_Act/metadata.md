# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/434?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/434
- Title: CBP Workload Staffing Model Act
- Congress: 119
- Bill type: HR
- Bill number: 434
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-06-25T16:34:26Z
- Update date including text: 2025-06-25T16:34:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-01-15 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-01-15 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/434",
    "number": "434",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001077",
        "district": "3",
        "firstName": "Clay",
        "fullName": "Rep. Higgins, Clay [R-LA-3]",
        "lastName": "Higgins",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "CBP Workload Staffing Model Act",
    "type": "HR",
    "updateDate": "2025-06-25T16:34:26Z",
    "updateDateIncludingText": "2025-06-25T16:34:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-15T18:44:37Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr434ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 434\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Higgins of Louisiana introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to improve U.S. Customs and Border Protection (CBP) identification of staffing needs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the CBP Workload Staffing Model Act .\n#### 2. Establishment of workload staffing models for U.S. Border Patrol and Air and Marine Operations of U.S. Customs and Border Protection\n##### (a) In general\nThe Commissioner of U.S. Customs and Border Protection shall, in coordination with the Under Secretary for Management, Chief Human Capital Officer, and Chief Financial Officer of the Department of Homeland Security, develop and implement, by not later than one year after the date of the enactment of this Act, a workload staffing model for each of the following:\n**(1)**\nThe U.S. Border Patrol.\n**(2)**\nAir and Marine Operations.\n##### (b) Responsibilities of the Commissioner of CBP\nSubsection (c) of section 411 of the Homeland Security Act of 2002 ( 6 U.S.C. 211 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (18) and (19) as paragraphs (20) and (21), respectively; and\n**(2)**\nby inserting after paragraph (17) the following new paragraphs:\n(18) implement a staffing model that includes consideration for essential frontline operator activities and functions, variations in operating environments, present and planned infrastructure, present and planned technology, and required operations support levels for the U.S. Border Patrol, Air and Marine Operations, and the Office of Field Operations, to manage and assign personnel of such entities to ensure field and support posts possess adequate resources to carry out duties specified in this section; (19) develop standard operating procedures for a workforce tracking system within the U.S. Border Patrol, Air and Marine Operations, and the Office of Field Operations, train the workforce of each of such entities on the use, capabilities, and purpose of such system, and implement internal controls to ensure timely and accurate scheduling and reporting of actual completed work hours and activities; .\n##### (c) Report\nNot later than one year after the date of the enactment of this Act with respect to subsection (a) and paragraphs (18) and (19) of section 411(c) of the Homeland Security Act of 2002 (as amended by subsection (b)), and annually thereafter with respect to such paragraphs (18) and (19), the Secretary of Homeland Security shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a status update on the implementation of this Act and such paragraphs (18) and (19), and annual status updates regarding such paragraphs (18) and (19), as well as all relevant workload staffing models. Such status updates shall include information on data sources and methodology used to generate such staffing models.\n##### (d) Inspector General review\nNot later than 120 days after the Commissioner of U.S. Customs and Border Protection develops a workload staffing model pursuant to subsection (a), the Inspector General of the Department of Homeland Security shall review such model and provide feedback to the Secretary of Homeland Security and the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate regarding the degree to which such model is responsive to Inspector General recommendations, including recommendations from the Inspector General\u2019s February 2019 audit, and as appropriate, any further recommendations to improve such model.",
      "versionDate": "2025-01-15",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-02-26T14:43:44Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-26T14:43:44Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-02-26T14:43:44Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-02-26T14:43:44Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-26T14:43:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-19T17:58:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr434",
          "measure-number": "434",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-06-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr434v00",
            "update-date": "2025-06-25"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>CBP Workload Staffing Model Act</strong></p><p>This bill requires the U.S. Customs and Border Protection (CBP) to develop and implement a workload staffing model for each of the U.S. Border Patrol and Air and Marine Operations.</p><p>Such model shall include (1) consideration for essential frontline operator activities and functions, (2) variations in operating environments, and (3) present and planned infrastructure and technology. The CBP must also develop standard operating procedures for a workforce tracking system, train the workforce on the use of such system, and implement internal controls to ensure timely and accurate scheduling and reporting.</p><p>The Department of Homeland Security (DHS) must review the model and provide feedback regarding the degree to which it is responsive to certain DHS recommendations.</p>"
        },
        "title": "CBP Workload Staffing Model Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr434.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>CBP Workload Staffing Model Act</strong></p><p>This bill requires the U.S. Customs and Border Protection (CBP) to develop and implement a workload staffing model for each of the U.S. Border Patrol and Air and Marine Operations.</p><p>Such model shall include (1) consideration for essential frontline operator activities and functions, (2) variations in operating environments, and (3) present and planned infrastructure and technology. The CBP must also develop standard operating procedures for a workforce tracking system, train the workforce on the use of such system, and implement internal controls to ensure timely and accurate scheduling and reporting.</p><p>The Department of Homeland Security (DHS) must review the model and provide feedback regarding the degree to which it is responsive to certain DHS recommendations.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr434"
    },
    "title": "CBP Workload Staffing Model Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>CBP Workload Staffing Model Act</strong></p><p>This bill requires the U.S. Customs and Border Protection (CBP) to develop and implement a workload staffing model for each of the U.S. Border Patrol and Air and Marine Operations.</p><p>Such model shall include (1) consideration for essential frontline operator activities and functions, (2) variations in operating environments, and (3) present and planned infrastructure and technology. The CBP must also develop standard operating procedures for a workforce tracking system, train the workforce on the use of such system, and implement internal controls to ensure timely and accurate scheduling and reporting.</p><p>The Department of Homeland Security (DHS) must review the model and provide feedback regarding the degree to which it is responsive to certain DHS recommendations.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr434"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr434ih.xml"
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
      "title": "CBP Workload Staffing Model Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CBP Workload Staffing Model Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to improve U.S. Customs and Border Protection (CBP) identification of staffing needs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:33Z"
    }
  ]
}
```
