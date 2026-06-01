# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/388?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/388
- Title: Cattle Fever Tick Eradication Program Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 388
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2026-03-24T20:06:16Z
- Update date including text: 2026-03-24T20:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2025-02-14 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-01-14: Introduced in House

## Actions

- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2025-02-14 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/388",
    "number": "388",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "D000594",
        "district": "15",
        "firstName": "Monica",
        "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
        "lastName": "De La Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Cattle Fever Tick Eradication Program Enhancement Act",
    "type": "HR",
    "updateDate": "2026-03-24T20:06:16Z",
    "updateDateIncludingText": "2026-03-24T20:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
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
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-02-14T18:04:12Z",
                "name": "Referred to"
              }
            },
            "name": "Conservation, Research, and Biotechnology Subcommittee",
            "systemCode": "hsag14"
          },
          {
            "activities": {
              "item": {
                "date": "2025-02-14T18:04:12Z",
                "name": "Referred to"
              }
            },
            "name": "Livestock, Dairy, and Poultry Subcommittee",
            "systemCode": "hsag29"
          }
        ]
      },
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
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr388ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 388\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2025 Ms. De La Cruz (for herself, Ms. Crockett , and Mr. Ellzey ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo direct the Secretary of Agriculture to review the Cattle Fever Tick Eradication Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cattle Fever Tick Eradication Program Enhancement Act .\n#### 2. Cattle Fever Tick Eradication Program review and report\n##### (a) Program review\n**(1) In general**\nNot later than 1 year after the date of the enactment of this section, the Secretary of Agriculture shall offer to enter into a contract with a covered institution under which the covered institution shall conduct a review of the Program.\n**(2) Review elements**\nThe review conducted pursuant to paragraph (1) shall include an evaluation of\u2014\n**(A)**\nthe effectiveness of the Program with respect to preventing and reducing the spread of tick-borne illnesses in cattle;\n**(B)**\nwith respect to cattle producers\u2014\n**(i)**\nthe benefits of the Program; and\n**(ii)**\nthe burden of compliance with the Program;\n**(C)**\nthe treatment protocols developed and implemented under the Program; and\n**(D)**\nthe Federal and State funds allocated to support the Program for the most recent fiscal year, including the funds allocated to each research project associated with the Program.\n##### (b) Report\nNot later than 1 year after the date on which the Secretary of Agriculture and a covered institution enter into a contract pursuant to subsection (a)(1), the Secretary of Agriculture shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report that includes\u2014\n**(1)**\nthe results of the review conducted pursuant to subsection (a); and\n**(2)**\nrecommendations for improvements to the Program, including recommendations for reducing the burden of compliance with the Program with respect to cattle producers.\n##### (c) Definitions\nIn this section:\n**(1) Covered institution**\nThe term covered institution means\u2014\n**(A)**\na land-grant college or university; or\n**(B)**\na non-land-grant college of agriculture.\n**(2) Land-grant college or university**\nThe term land-grant college or university means an institution from among the land-grant colleges and universities (as defined in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 )).\n**(3) Non-land-grant college of agriculture**\nThe term non-land-grant college of agriculture has the meaning given such term in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 ).\n**(4) Program**\nThe term Program means the Cattle Fever Tick Eradication Program carried out by the Animal and Plant Health Inspection Service of the Department of Agriculture in coordination with the Texas Animal Health Commission.",
      "versionDate": "2025-01-14",
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
        "updateDate": "2025-02-19T15:29:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119hr388",
          "measure-number": "388",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr388v00",
            "update-date": "2025-02-25"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Cattle Fever Tick Eradication Program Enhancement Act</strong></p><p>This bill requires the Department of Agriculture (USDA) to enter into a contract to evaluate the Cattle Fever Tick Eradication Program.</p><p> Under the program, the Animal and Plant Health Inspection Service works in coordination with the Texas Animal Health Commission to combat the spread of cattle fever ticks, which can spread a serious cattle disease called bovine\u00a0babesiosis or cattle fever.</p><p>Specifically, USDA must enter into a contract to review and report on the Cattle Fever Tick Eradication Program with a (1) land-grant college or university, or (2) non-land-grant college of agriculture.</p><p>The review must include an evaluation of the program's (1) effectiveness with respect to preventing and reducing the spread of tick-borne illnesses in cattle; and (2) benefits, and the burdens of compliance, to cattle producers.</p><p>The review must also evaluate the treatment protocols developed and implemented under the program.</p><p>Further, the review must evaluate the federal and state funds allocated to support the program for the most recent fiscal year.</p><p>\u00a0</p>"
        },
        "title": "Cattle Fever Tick Eradication Program Enhancement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr388.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cattle Fever Tick Eradication Program Enhancement Act</strong></p><p>This bill requires the Department of Agriculture (USDA) to enter into a contract to evaluate the Cattle Fever Tick Eradication Program.</p><p> Under the program, the Animal and Plant Health Inspection Service works in coordination with the Texas Animal Health Commission to combat the spread of cattle fever ticks, which can spread a serious cattle disease called bovine\u00a0babesiosis or cattle fever.</p><p>Specifically, USDA must enter into a contract to review and report on the Cattle Fever Tick Eradication Program with a (1) land-grant college or university, or (2) non-land-grant college of agriculture.</p><p>The review must include an evaluation of the program's (1) effectiveness with respect to preventing and reducing the spread of tick-borne illnesses in cattle; and (2) benefits, and the burdens of compliance, to cattle producers.</p><p>The review must also evaluate the treatment protocols developed and implemented under the program.</p><p>Further, the review must evaluate the federal and state funds allocated to support the program for the most recent fiscal year.</p><p>\u00a0</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr388"
    },
    "title": "Cattle Fever Tick Eradication Program Enhancement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cattle Fever Tick Eradication Program Enhancement Act</strong></p><p>This bill requires the Department of Agriculture (USDA) to enter into a contract to evaluate the Cattle Fever Tick Eradication Program.</p><p> Under the program, the Animal and Plant Health Inspection Service works in coordination with the Texas Animal Health Commission to combat the spread of cattle fever ticks, which can spread a serious cattle disease called bovine\u00a0babesiosis or cattle fever.</p><p>Specifically, USDA must enter into a contract to review and report on the Cattle Fever Tick Eradication Program with a (1) land-grant college or university, or (2) non-land-grant college of agriculture.</p><p>The review must include an evaluation of the program's (1) effectiveness with respect to preventing and reducing the spread of tick-borne illnesses in cattle; and (2) benefits, and the burdens of compliance, to cattle producers.</p><p>The review must also evaluate the treatment protocols developed and implemented under the program.</p><p>Further, the review must evaluate the federal and state funds allocated to support the program for the most recent fiscal year.</p><p>\u00a0</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr388"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr388ih.xml"
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
      "title": "Cattle Fever Tick Eradication Program Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cattle Fever Tick Eradication Program Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture to review the Cattle Fever Tick Eradication Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:32Z"
    }
  ]
}
```
