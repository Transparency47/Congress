# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1722?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1722
- Title: Billion Dollar Boondoggle Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1722
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-04-15T08:05:54Z
- Update date including text: 2026-04-15T08:05:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 39 - 0.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 39 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1722",
    "number": "1722",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "Billion Dollar Boondoggle Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:54Z",
    "updateDateIncludingText": "2026-04-15T08:05:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 39 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
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
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
            "date": "2026-03-18T13:00:28Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-27T14:15:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-27T14:15:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "AZ"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "OK"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1722ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1722\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mrs. Miller-Meeks introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require an annual report of taxpayer-funded projects that are over budget and behind schedule.\n#### 1. Short title\nThis Act may be cited as the Billion Dollar Boondoggle Act of 2025 .\n#### 2. Annual report\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term covered agency means\u2014\n**(A)**\nan Executive agency, as defined in section 105 of title 5, United States Code; and\n**(B)**\nan independent regulatory agency, as defined in section 3502 of title 44, United States Code;\n**(2)**\nthe term covered project means a project funded by a covered agency\u2014\n**(A)**\nthat is more than 5 years behind schedule, as measured against the original expected date for completion; or\n**(B)**\nfor which the amount spent on the project is not less than $1,000,000,000 more than the original cost estimate for the project;\n**(3)**\nthe term Director means the Director of the Office of Management and Budget; and\n**(4)**\nthe term project means a major acquisition, a major defense acquisition program (as defined in section 4201 of title 10, United States Code), a procurement, a construction project, a remediation or clean-up effort, or any other time-limited endeavor, that is not funded through direct spending (as defined in section 250(c) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 900(c) )).\n##### (b) Requirements\n**(1) Submission**\nNot later than 1 year after the date of enactment of this Act, the Director shall issue guidance requiring covered agencies to, on an annual basis, submit to the Director information relating to each covered project of the covered agency, which shall include\u2014\n**(A)**\na brief description of the covered project, including\u2014\n**(i)**\nthe purpose of the covered project;\n**(ii)**\neach location in which the covered project is carried out;\n**(iii)**\nthe contract or award number of the covered project, where applicable;\n**(iv)**\nthe year in which the covered project was initiated;\n**(v)**\nthe Federal share of the total cost of the covered project; and\n**(vi)**\neach primary contractor, subcontractor, grant recipient, and subgrantee recipient of the covered project;\n**(B)**\nan explanation of any change to the original scope of the covered project, including by the addition or narrowing of the initial requirements of the covered project;\n**(C)**\nthe original expected date for completion of the covered project;\n**(D)**\nthe current expected date for completion of the covered project;\n**(E)**\nthe original cost estimate for the covered project, as adjusted to reflect increases in the Consumer Price Index for All Urban Consumers, as published by the Bureau of Labor Statistics;\n**(F)**\nthe current cost estimate for the covered project, as adjusted to reflect increases in the Consumer Price Index for All Urban Consumers, as published by the Bureau of Labor Statistics;\n**(G)**\nan explanation for a delay in completion or an increase in the original cost estimate for the covered project, including, where applicable, any impact of insufficient or delayed appropriations; and\n**(H)**\nthe amount of and rationale for any award, incentive fee, or other type of bonus, if any, awarded for the covered project.\n**(2) Report**\nThe Director shall submit to Congress and post on the website of the Office of Management and Budget an annual report containing the information submitted under paragraph (1) for the relevant year.",
      "versionDate": "2025-02-27",
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
        "actionDate": "2026-03-18",
        "text": "Committee on Small Business and Entrepreneurship. Hearings held."
      },
      "number": "766",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Billion Dollar Boondoggle Act of 2025",
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
            "name": "Congressional oversight",
            "updateDate": "2025-08-07T15:44:10Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-08-07T15:44:10Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-08-07T15:44:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-06T15:50:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1722",
          "measure-number": "1722",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1722v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Billion Dollar Boondoggle Act of 2025</strong></p><p>This bill requires the Office of Management and Budget (OMB) to collect information from federal agencies and report to Congress regarding projects that are behind schedule or have expenditures that have exceeded the original cost estimate.\u00a0</p><p>Specifically, the bill requires OMB to issue guidance directing federal agencies to annually submit specified information to OMB regarding certain federally funded projects that (1) are more than five years behind schedule, or (2) have expenditures that are at least $1 billion more than the original cost estimate for the project.\u00a0</p><p>Among other information, the agencies must submit to OMB</p><ul><li>a description of each project;</li><li>an explanation of any change to the original scope of the project;</li><li>the original and current expected dates for the completion of the project;</li><li>the original and current cost estimates adjusted for inflation;\u00a0</li><li>an explanation for any delays in completing the project or increases in the cost; and</li><li>the amount of and rationale for any award, incentive fee, or other type of bonus awarded for the project.</li></ul><p>The bill also requires OMB to submit an annual report to Congress containing the information submitted by the agencies\u00a0and post the report on the OMB website.\u00a0</p>"
        },
        "title": "Billion Dollar Boondoggle Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1722.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Billion Dollar Boondoggle Act of 2025</strong></p><p>This bill requires the Office of Management and Budget (OMB) to collect information from federal agencies and report to Congress regarding projects that are behind schedule or have expenditures that have exceeded the original cost estimate.\u00a0</p><p>Specifically, the bill requires OMB to issue guidance directing federal agencies to annually submit specified information to OMB regarding certain federally funded projects that (1) are more than five years behind schedule, or (2) have expenditures that are at least $1 billion more than the original cost estimate for the project.\u00a0</p><p>Among other information, the agencies must submit to OMB</p><ul><li>a description of each project;</li><li>an explanation of any change to the original scope of the project;</li><li>the original and current expected dates for the completion of the project;</li><li>the original and current cost estimates adjusted for inflation;\u00a0</li><li>an explanation for any delays in completing the project or increases in the cost; and</li><li>the amount of and rationale for any award, incentive fee, or other type of bonus awarded for the project.</li></ul><p>The bill also requires OMB to submit an annual report to Congress containing the information submitted by the agencies\u00a0and post the report on the OMB website.\u00a0</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1722"
    },
    "title": "Billion Dollar Boondoggle Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Billion Dollar Boondoggle Act of 2025</strong></p><p>This bill requires the Office of Management and Budget (OMB) to collect information from federal agencies and report to Congress regarding projects that are behind schedule or have expenditures that have exceeded the original cost estimate.\u00a0</p><p>Specifically, the bill requires OMB to issue guidance directing federal agencies to annually submit specified information to OMB regarding certain federally funded projects that (1) are more than five years behind schedule, or (2) have expenditures that are at least $1 billion more than the original cost estimate for the project.\u00a0</p><p>Among other information, the agencies must submit to OMB</p><ul><li>a description of each project;</li><li>an explanation of any change to the original scope of the project;</li><li>the original and current expected dates for the completion of the project;</li><li>the original and current cost estimates adjusted for inflation;\u00a0</li><li>an explanation for any delays in completing the project or increases in the cost; and</li><li>the amount of and rationale for any award, incentive fee, or other type of bonus awarded for the project.</li></ul><p>The bill also requires OMB to submit an annual report to Congress containing the information submitted by the agencies\u00a0and post the report on the OMB website.\u00a0</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1722"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1722ih.xml"
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
      "title": "Billion Dollar Boondoggle Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T15:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Billion Dollar Boondoggle Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T15:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require an annual report of taxpayer-funded projects that are over budget and behind schedule.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T15:18:19Z"
    }
  ]
}
```
