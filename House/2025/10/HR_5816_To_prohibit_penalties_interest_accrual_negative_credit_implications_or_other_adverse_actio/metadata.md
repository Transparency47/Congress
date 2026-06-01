# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5816?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5816
- Title: HELP FEDs Act
- Congress: 119
- Bill type: HR
- Bill number: 5816
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2025-11-18T09:05:17Z
- Update date including text: 2025-11-18T09:05:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-10-24: Introduced in House

## Actions

- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5816",
    "number": "5816",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001130",
        "district": "30",
        "firstName": "Jasmine",
        "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
        "lastName": "Crockett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "HELP FEDs Act",
    "type": "HR",
    "updateDate": "2025-11-18T09:05:17Z",
    "updateDateIncludingText": "2025-11-18T09:05:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "LA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MN"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "LA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "AL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
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
      "sponsorshipDate": "2025-10-28",
      "state": "DC"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "OH"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NJ"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MS"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "PA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "FL"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "IL"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5816ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5816\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Ms. Crockett introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo prohibit penalties, interest accrual, negative credit implications, or other adverse actions for qualified student loans for Federal employees during a lapse in Federal funding.\n#### 1. Short title\nThis Act may be cited as the Halting Education Loan Payments during Federal Employment Disruptions Act or the HELP FEDs Act .\n#### 2. Definitions\nIn this Act:\n**(1) Federal employee**\nThe term Federal employee means\u2014\n**(A)**\nan employee as defined in section 2105 of title 5, United States Code;\n**(B)**\nan employee as defined in section 2107 of title 5, United States Code; and\n**(C)**\na judicial employee as defined in section 13101(9) of title 5, United States Code.\n**(2) Qualified education loan**\nThe term qualified education loan means any loan made, insured, or guaranteed under the Higher Education Act of 1965 ( 20 U.S.C. 1071\u20131087ii ), including loans held by the Department of Education or contracted loan servicers.\n**(3) Involuntary disruption of pay**\nThe term involuntary disruption of pay means a situation where a Federal employee does not receive their scheduled wages due to a lapse in funding resulting in the Federal Government to cease operations as identified under section 1341 of title 31, United States Code.\n#### 3. Protection from penalties and adverse credit actions during involuntary disruption of pay\n##### (a) Waiver of penalties and late fees\nNo Federal employee shall be assessed any late fee, penalty, or other adverse action on any qualified education loan for any payment missed due during a period of involuntary disruption of pay.\n##### (b) Waiver on interest accrual\nNo Federal employee shall incur additional interest on any qualified education loan during a period of involuntary disruption of pay.\n##### (c) No adverse credit reporting\nThe Secretary of Education shall coordinate with credit reporting agencies and loan servicers to ensure that no adverse information related to delayed or missed payments of a Federal employee described in subsection (a) is furnished to any consumer reporting agency, as defined in section 603 of the Fair Credit Reporting Act ( 15 U.S.C. 1681a ).\n##### (d) Retroactive application\nThis section shall apply retroactively to any instance of involuntary disruption of pay occurring on or after October 1, 2025. The Secretary shall coordinate with credit reporting agencies and loan servicers to remove any adverse credit information that was inappropriately reported.\n#### 4. Implementation\n##### (a) In general\nThe Secretary of Education, in coordination with the Director of the Office of Personnel Management, the Administrative Office of the United States Courts, the Clerk of the House of Representatives, and Secretary of the Senate, shall issue regulations and guidance for the Department, borrowers, loan servicers, and credit agencies necessary to implement this Act within 30 days of the date of enactment of this Act.\n##### (b) Compliance and enforcement\nLoan servicers and credit reporting agencies shall cooperate fully with the Secretary of Education in implementing this Act.\n#### 5. Rule of construction\nNothing in this Act shall be construed to excuse the full repayment of qualified education loans or to eliminate any otherwise existing repayment obligation.\n#### 6. Severability\nIf any provision of this Act, or the application of such provision to any person or circumstance, is held to be invalid, the remainder of this Act shall not be affected.",
      "versionDate": "2025-10-24",
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
        "name": "Education",
        "updateDate": "2025-10-29T13:22:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-24",
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
          "measure-id": "id119hr5816",
          "measure-number": "5816",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-24",
          "originChamber": "HOUSE",
          "update-date": "2025-10-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5816v00",
            "update-date": "2025-10-29"
          },
          "action-date": "2025-10-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Halting Education Loan Payments during Federal Employment Disruptions Act or the HELP FEDs Act</strong></p><p>This bill waives late fees, penalties, and other adverse actions for federal employees who miss student loan payments during a lapse in appropriations (i.e., government shutdown). \u00a0</p><p>The bill applies to education loans made, insured, or guaranteed under the Higher Education Act of 1965, including loans held by the Department of Education (ED) or contracted loan servicers.</p><p>Under the bill, a federal employee who misses a student loan payment that is due during a period of involuntary disruption of pay (i.e., the employee did not receive scheduled wages due to a lapse in appropriations) may not be assessed a late fee or penalty or be subject to other adverse actions. The bill also prohibits federal employees from incurring additional interest on such loans during an involuntary disruption of pay.\u00a0</p><p>In addition, the bill requires ED to coordinate with credit reporting agencies and loan\u00a0servicers to ensure that no adverse information related to delayed or missed student loan payments of a federal employee during an involuntary disruption of pay is furnished to any consumer reporting agency.\u00a0</p><p>The bill applies retroactively to any involuntary disruption of pay occurring on or after October 1, 2025.\u00a0</p>"
        },
        "title": "HELP FEDs Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5816.xml",
    "summary": {
      "actionDate": "2025-10-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Halting Education Loan Payments during Federal Employment Disruptions Act or the HELP FEDs Act</strong></p><p>This bill waives late fees, penalties, and other adverse actions for federal employees who miss student loan payments during a lapse in appropriations (i.e., government shutdown). \u00a0</p><p>The bill applies to education loans made, insured, or guaranteed under the Higher Education Act of 1965, including loans held by the Department of Education (ED) or contracted loan servicers.</p><p>Under the bill, a federal employee who misses a student loan payment that is due during a period of involuntary disruption of pay (i.e., the employee did not receive scheduled wages due to a lapse in appropriations) may not be assessed a late fee or penalty or be subject to other adverse actions. The bill also prohibits federal employees from incurring additional interest on such loans during an involuntary disruption of pay.\u00a0</p><p>In addition, the bill requires ED to coordinate with credit reporting agencies and loan\u00a0servicers to ensure that no adverse information related to delayed or missed student loan payments of a federal employee during an involuntary disruption of pay is furnished to any consumer reporting agency.\u00a0</p><p>The bill applies retroactively to any involuntary disruption of pay occurring on or after October 1, 2025.\u00a0</p>",
      "updateDate": "2025-10-29",
      "versionCode": "id119hr5816"
    },
    "title": "HELP FEDs Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Halting Education Loan Payments during Federal Employment Disruptions Act or the HELP FEDs Act</strong></p><p>This bill waives late fees, penalties, and other adverse actions for federal employees who miss student loan payments during a lapse in appropriations (i.e., government shutdown). \u00a0</p><p>The bill applies to education loans made, insured, or guaranteed under the Higher Education Act of 1965, including loans held by the Department of Education (ED) or contracted loan servicers.</p><p>Under the bill, a federal employee who misses a student loan payment that is due during a period of involuntary disruption of pay (i.e., the employee did not receive scheduled wages due to a lapse in appropriations) may not be assessed a late fee or penalty or be subject to other adverse actions. The bill also prohibits federal employees from incurring additional interest on such loans during an involuntary disruption of pay.\u00a0</p><p>In addition, the bill requires ED to coordinate with credit reporting agencies and loan\u00a0servicers to ensure that no adverse information related to delayed or missed student loan payments of a federal employee during an involuntary disruption of pay is furnished to any consumer reporting agency.\u00a0</p><p>The bill applies retroactively to any involuntary disruption of pay occurring on or after October 1, 2025.\u00a0</p>",
      "updateDate": "2025-10-29",
      "versionCode": "id119hr5816"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5816ih.xml"
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
      "title": "HELP FEDs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HELP FEDs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Halting Education Loan Payments during Federal Employment Disruptions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit penalties, interest accrual, negative credit implications, or other adverse actions for qualified student loans for Federal employees during a lapse in Federal funding.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T04:18:12Z"
    }
  ]
}
```
