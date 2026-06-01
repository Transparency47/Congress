# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1108
- Title: Diagnostics Testing Preparedness Plan Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1108
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2025-06-16T11:33:14Z
- Update date including text: 2025-06-16T11:33:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1108",
    "number": "1108",
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
    "title": "Diagnostics Testing Preparedness Plan Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-16T11:33:14Z",
    "updateDateIncludingText": "2025-06-16T11:33:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
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
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:02:30Z",
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "WA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "TX"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1108ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1108\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mrs. Miller-Meeks (for herself, Ms. Schrier , Mr. Crenshaw , and Mr. Carson ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to direct the Secretary of Health and Human Services to develop a plan to improve the development and distribution of diagnostic tests during a public health emergency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Diagnostics Testing Preparedness Plan Act of 2025 .\n#### 2. Improving development and distribution of diagnostic tests\nSection 319B of the Public Health Service Act ( 42 U.S.C. 247d\u20132 ) is amended to read as follows:\n319B. Improving development and distribution of diagnostic tests (a) Diagnostic testing preparedness plan The Secretary shall develop, make publicly available, and update a plan for the rapid development, validation, authorization, manufacture, procurement, and distribution of diagnostic tests, and for rapid scaling of testing capacity, in response to chemical, biological, radiological, or nuclear threats, including emerging infectious diseases, for which a public health emergency is declared under section 319, or that has significant potential to cause such a public health emergency. (b) Purposes The purpose of the plan under subsection (a) shall be to\u2014 (1) facilitate the development and utilization of diagnostic tests; (2) describe the processes for the rapid development, validation, authorization, manufacture, procurement, and distribution of diagnostic tests, and for rapid scaling of testing capacity; and (3) facilitate coordination and collaboration among public and private entities to improve the rapid development and utilization of diagnostic testing during a public health emergency. (c) Considerations The plan under subsection (a) shall take into consideration\u2014 (1) domestic capacity, including any such capacity established through partnerships with public and private entities pursuant to subsection (e), to support the development, validation, manufacture, procurement, and distribution of tests, and the rapid scaling of testing capacity; (2) novel technologies and platforms that\u2014 (A) may be used to improve testing capabilities, including\u2014 (i) high-throughput laboratory diagnostics; (ii) point-of-care diagnostics; and (iii) rapid at-home diagnostics; (B) improve the accessibility of diagnostic tests; and (C) facilitate the development and manufacture of diagnostic tests; (3) medical supply needs related to testing, including diagnostic testing, equipment, supplies, and component parts, and any potential vulnerabilities related to the availability of such medical supplies and related planning needs, consistent with section 2811(b)(4)(J); (4) strategies for the rapid and efficient distribution of tests locally, regionally, or nationwide and appropriate scaling of laboratory testing capacity; and (5) assessment of such strategies through drills and operational exercises carried out under section 2811(b)(4)(G), as appropriate. (d) Coordination To inform the development and update of the plan under subsection (a), and in carrying out activities to implement such plan, the Secretary shall coordinate with industry, such as device manufacturers, clinical and reference laboratories, and medical product distributors, States, local governmental entities, Indian Tribes and Tribal organizations, and other relevant public and private entities. (e) Capacity building The Secretary may contract with public and private entities, as appropriate, to increase domestic capacity in the rapid development, validation, authorization, manufacture, procurement, and distribution of diagnostic tests, as appropriate, to State, local, and Tribal health departments and other appropriate entities for immediate public health response activities to address an infectious disease with respect to which a public health emergency is declared under section 319, or that has significant potential to cause such a public health emergency. (f) Deadlines for plan (1) Public release Not later than one year after the date of enactment of the Diagnostics Testing Preparedness Plan Act of 2025 , the Secretary shall publicly release the plan developed under subsection (a). (2) Updates The Secretary shall update such plan not less frequently than once every 3 years after the date of the initial public release of the plan. .",
      "versionDate": "2025-02-07",
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
            "name": "Emergency planning and evacuation",
            "updateDate": "2025-04-24T16:14:14Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-04-24T16:14:19Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-04-24T16:14:47Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-04-24T16:14:30Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-04-24T16:14:08Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-04-24T16:14:42Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2025-04-24T16:14:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-11T15:11:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-07",
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
          "measure-id": "id119hr1108",
          "measure-number": "1108",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-07",
          "originChamber": "HOUSE",
          "update-date": "2025-04-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1108v00",
            "update-date": "2025-04-25"
          },
          "action-date": "2025-02-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Diagnostics Testing Preparedness Plan Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to develop and publish a plan for the rapid development and distribution of diagnostic tests in response to a chemical, biological, radiological, or nuclear\u00a0threat, including an emerging infectious disease, that causes or has significant potential to cause a declared public health emergency.</p><p>Specifically, HHS must coordinate with any relevant public and private entities, such as government entities\u00a0and device manufacturers, in creating the plan and facilitating its collaborative implementation. The plan must take into consideration certain factors specified in the bill, including domestic testing capacity, novel technologies, and medical supply needs. HHS must publish the plan within one year after enactment of the bill and then update the plan every three years.</p>"
        },
        "title": "Diagnostics Testing Preparedness Plan Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1108.xml",
    "summary": {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Diagnostics Testing Preparedness Plan Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to develop and publish a plan for the rapid development and distribution of diagnostic tests in response to a chemical, biological, radiological, or nuclear\u00a0threat, including an emerging infectious disease, that causes or has significant potential to cause a declared public health emergency.</p><p>Specifically, HHS must coordinate with any relevant public and private entities, such as government entities\u00a0and device manufacturers, in creating the plan and facilitating its collaborative implementation. The plan must take into consideration certain factors specified in the bill, including domestic testing capacity, novel technologies, and medical supply needs. HHS must publish the plan within one year after enactment of the bill and then update the plan every three years.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hr1108"
    },
    "title": "Diagnostics Testing Preparedness Plan Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Diagnostics Testing Preparedness Plan Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to develop and publish a plan for the rapid development and distribution of diagnostic tests in response to a chemical, biological, radiological, or nuclear\u00a0threat, including an emerging infectious disease, that causes or has significant potential to cause a declared public health emergency.</p><p>Specifically, HHS must coordinate with any relevant public and private entities, such as government entities\u00a0and device manufacturers, in creating the plan and facilitating its collaborative implementation. The plan must take into consideration certain factors specified in the bill, including domestic testing capacity, novel technologies, and medical supply needs. HHS must publish the plan within one year after enactment of the bill and then update the plan every three years.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hr1108"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1108ih.xml"
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
      "title": "Diagnostics Testing Preparedness Plan Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-08T06:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Diagnostics Testing Preparedness Plan Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to direct the Secretary of Health and Human Services to develop a plan to improve the development and distribution of diagnostic tests during a public health emergency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:37Z"
    }
  ]
}
```
