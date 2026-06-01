# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2811?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2811
- Title: SNAP Staffing Flexibility Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2811
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-03-10T15:54:56Z
- Update date including text: 2026-03-10T15:54:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2811",
    "number": "2811",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "SNAP Staffing Flexibility Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-10T15:54:56Z",
    "updateDateIncludingText": "2026-03-10T15:54:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:03:05Z",
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
      "sponsorshipDate": "2025-04-10",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2811ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2811\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Bacon (for himself and Mr. Rouzer ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to allow for blended workforces to carry out the supplemental nutrition assistance program under certain conditions, and for other purposes.\n#### 1. Short title\n##### (a)\nThis Act may be cited as the SNAP Staffing Flexibility Act of 2025 .\n#### 2. SNAP staffing flexibility\n##### (a)\nSection 11 of the Food and Nutrition Act ( 7 U.S.C. 2020 ) is amended by adding at the end the following:\n(y) SNAP staffing flexibility (1) In general Notwithstanding section 11(e)(6)(B) of the Food and Nutrition Act of 2008, a State agency (as defined in section 3 of the Food and Nutrition Act of 2008) may, by contract with the State agency at a reasonable cost in accordance with the State agency\u2019s standard contracting rules, hire a contractor to undertake supplemental nutrition assistance program certification or carry out any other function of the State agency under such program so long as\u2014 (A) the contract does not provide incentives for the agency or contractor to delay eligibility determinations or to deny eligibility for individuals otherwise eligible for supplemental nutrition assistance program benefits; and (B) the contractor has no direct or indirect financial interest in an approved retail store. (2) Use A State agency may use the authority provided in paragraph (1) when the State experiences increases in supplemental nutrition assistance program applications or an inability to timely process such applications from causes that include but are not limited to\u2014 (A) pandemics and other health emergencies, (B) seasonal workforce cycles, (C) temporary staffing shortages, and (D) weather or other natural disasters. (3) Requirements A State agency that hires a contractor under paragraph (1) shall ensure such action\u2014 (A) is consistent with all principles under section 900.603 of title 5 of the Code of Federal Regulations; and (B) is part of a blended workforce and does not supplant existing merit-based personnel in the State. (4) Notification A State agency shall notify the Secretary of its intent to use the authority provided in this section and shall provide any information or data supporting State agency increases in supplemental nutrition assistance program applications or any inability to timely process such applications. (5) Public availability Not later than 10 days after the date of the receipt of a notification submitted by a State agency under paragraph (4), the Secretary shall make publicly available on the website of the Department of Agriculture the notification submitted by such State agency and any accompanying information or data supporting such notification so submitted. (6) Annual report The Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate, an annual report that contains\u2014 (A) a description of measures taken to address increases in supplemental nutrition assistance program applications and any inability to timely process such applications; (B) information or data supporting State agency notifications provided pursuant to paragraph (4); and (C) recommendations for changes to the Secretary\u2019s authority under this Act to assist the Secretary, States, and local governments of States in preparing for any future increases in supplemental nutrition assistance program applications or inability to timely process such applications. (7) Temporary staffing shortages In cases of temporary staffing shortages, the authority provided to State agencies under paragraph (1) shall\u2014 (A) expire when the backlog of supplemental nutrition assistance program applications has been eliminated; and (B) not override any collective bargaining agreement or memorandum of understanding in effect between the State and employees of the State or of a local government of such State. .",
      "versionDate": "2025-04-10",
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
        "actionDate": "2026-03-04",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 17."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-05-07T13:26:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2811",
          "measure-number": "2811",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2026-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2811v00",
            "update-date": "2026-03-10"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>SNAP Staffing Flexibility Act of 2025</strong></p><p>This bill allows a state agency to hire a contractor to perform Supplemental Nutrition Assistance Program (SNAP) certification or other state functions for SNAP\u00a0under certain conditions.</p><p>Specifically, a state agency may hire a contractor when the state experiences an increase in SNAP applications or an inability to timely process such applications from causes that include\u00a0(1) pandemics and other health emergencies, (2) seasonal workforce cycles, (3) temporary staffing shortages, and (4) weather or other natural disasters.\u00a0The bill includes specific parameters for a state agency that hires a contractor based on\u00a0temporary staffing shortages.</p><p>A contractor hired under this bill must be part of a blended workforce and\u00a0may not supplant existing merit-based personnel in the state.\u00a0</p><p>Further, a state agency must notify the Department of Agriculture (USDA) of the intent to hire a contractor and provide any information or data supporting state agency increases in SNAP applications or the inability to timely process applications. USDA must make the notification and accompanying information publicly available on the USDA website.</p><p>Finally, USDA must submit an annual report to Congress that includes specific information and recommendations, including information on the measures taken by USDA to address increases in SNAP applications.</p>"
        },
        "title": "SNAP Staffing Flexibility Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2811.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>SNAP Staffing Flexibility Act of 2025</strong></p><p>This bill allows a state agency to hire a contractor to perform Supplemental Nutrition Assistance Program (SNAP) certification or other state functions for SNAP\u00a0under certain conditions.</p><p>Specifically, a state agency may hire a contractor when the state experiences an increase in SNAP applications or an inability to timely process such applications from causes that include\u00a0(1) pandemics and other health emergencies, (2) seasonal workforce cycles, (3) temporary staffing shortages, and (4) weather or other natural disasters.\u00a0The bill includes specific parameters for a state agency that hires a contractor based on\u00a0temporary staffing shortages.</p><p>A contractor hired under this bill must be part of a blended workforce and\u00a0may not supplant existing merit-based personnel in the state.\u00a0</p><p>Further, a state agency must notify the Department of Agriculture (USDA) of the intent to hire a contractor and provide any information or data supporting state agency increases in SNAP applications or the inability to timely process applications. USDA must make the notification and accompanying information publicly available on the USDA website.</p><p>Finally, USDA must submit an annual report to Congress that includes specific information and recommendations, including information on the measures taken by USDA to address increases in SNAP applications.</p>",
      "updateDate": "2026-03-10",
      "versionCode": "id119hr2811"
    },
    "title": "SNAP Staffing Flexibility Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>SNAP Staffing Flexibility Act of 2025</strong></p><p>This bill allows a state agency to hire a contractor to perform Supplemental Nutrition Assistance Program (SNAP) certification or other state functions for SNAP\u00a0under certain conditions.</p><p>Specifically, a state agency may hire a contractor when the state experiences an increase in SNAP applications or an inability to timely process such applications from causes that include\u00a0(1) pandemics and other health emergencies, (2) seasonal workforce cycles, (3) temporary staffing shortages, and (4) weather or other natural disasters.\u00a0The bill includes specific parameters for a state agency that hires a contractor based on\u00a0temporary staffing shortages.</p><p>A contractor hired under this bill must be part of a blended workforce and\u00a0may not supplant existing merit-based personnel in the state.\u00a0</p><p>Further, a state agency must notify the Department of Agriculture (USDA) of the intent to hire a contractor and provide any information or data supporting state agency increases in SNAP applications or the inability to timely process applications. USDA must make the notification and accompanying information publicly available on the USDA website.</p><p>Finally, USDA must submit an annual report to Congress that includes specific information and recommendations, including information on the measures taken by USDA to address increases in SNAP applications.</p>",
      "updateDate": "2026-03-10",
      "versionCode": "id119hr2811"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2811ih.xml"
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
      "title": "SNAP Staffing Flexibility Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T05:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SNAP Staffing Flexibility Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to allow for blended workforces to carry out the supplemental nutrition assistance program under certain conditions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T05:34:10Z"
    }
  ]
}
```
