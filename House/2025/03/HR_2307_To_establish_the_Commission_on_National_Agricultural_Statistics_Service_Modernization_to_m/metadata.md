# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2307?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2307
- Title: To establish the Commission on National Agricultural Statistics Service Modernization to modernize the data collection and reporting processes of the National Agricultural Statistics Service, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 2307
- Origin chamber: House
- Introduced date: 2025-03-24
- Update date: 2026-03-05T09:06:35Z
- Update date including text: 2026-03-05T09:06:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-03-24: Introduced in House

## Actions

- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2307",
    "number": "2307",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "To establish the Commission on National Agricultural Statistics Service Modernization to modernize the data collection and reporting processes of the National Agricultural Statistics Service, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-03-05T09:06:35Z",
    "updateDateIncludingText": "2026-03-05T09:06:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
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
      "actionDate": "2025-03-24",
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
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T16:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:08:00Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NC"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "TN"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2307ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2307\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2025 Mr. Moore of Alabama (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo establish the Commission on National Agricultural Statistics Service Modernization to modernize the data collection and reporting processes of the National Agricultural Statistics Service, and for other purposes.\n#### 1. Commission on National Agricultural Statistics Service Modernization\n##### (a) Establishment\nThere is established a commission to be known as the Commission on National Agricultural Statistics Service Modernization (referred to in this section as the Commission ).\n##### (b) Study\nThe Commission shall conduct a study of the National Agricultural Statistics Service and provide recommendations on\u2014\n**(1)**\nhow data collection can be modernized and streamlined to\u2014\n**(A)**\nimprove the quality of statistics reported;\n**(B)**\naccount for differences of national, regional, and local production;\n**(C)**\naccelerate adoption of new and innovative technologies to reduce the number of surveys needed;\n**(D)**\nimprove producer response rates in statistical surveys and identifying ways to reduce survey fatigue;\n**(E)**\nincrease transparency and confidence in statistical reports through improved collaboration with agricultural stakeholders;\n**(F)**\nuse more real-time statistical and environmental data to complement existing survey-based data and reporting; and\n**(G)**\nimprove collection and generation of timely data on the specialty crop industry; and\n**(2)**\nhow the modernization and streamlining determined under paragraph (1) can be implemented and the estimated costs of such implementation.\n##### (c) Membership\n**(1) Composition**\nThe Commission shall consist of the following 11 members:\n**(A)**\nThe Administrator of the National Agricultural Statistics Service of the Department of Agriculture.\n**(B)**\nThe Administrator of the Economic Research Service of the Department of Agriculture.\n**(C)**\nThe Chief Economist of the Department of Agriculture.\n**(D)**\nThe Chair of the World Agricultural Outlook Board of the Department of Agriculture.\n**(E)**\nA representative from the Bureau of Labor Statistics.\n**(F)**\n3 members appointed by the Committee on Agriculture, Nutrition, and Forestry of the Senate, of which\u2014\n**(i)**\n1 shall be appointed by the Chairman of the Committee;\n**(ii)**\n1 shall be appointed by the Ranking Member of the Committee; and\n**(iii)**\n1 shall be appointed jointly by the Chairman and Ranking Member of the Committee.\n**(G)**\n3 members appointed by the Committee on Agriculture of the House of Representatives, of which\u2014\n**(i)**\n1 shall be appointed by the Chairman of the Committee;\n**(ii)**\n1 shall be appointed by the Ranking Member of the Committee; and\n**(iii)**\n1 shall be appointed jointly by the Chairman and Ranking Member of the Committee.\n**(2) Date of appointments**\nThe appointment of all members of the Commission shall be made not later than 60 days after the date of enactment of this Act.\n**(3) Term; vacancies**\n**(A) Term**\nA member shall be appointed for the duration of the Commission.\n**(B) Vacancies**\nA vacancy on the Commission\u2014\n**(i)**\nshall not affect the powers of the Commission; and\n**(ii)**\nshall be filled in the same manner as the original appointment was made.\n**(4) Initial meeting**\nNot later than 60 days after the date on which all members of the Commission have been first appointed, the Commission shall hold the initial meeting of the Commission.\n##### (d) Quorum\nA majority of the members of the Commission shall constitute a quorum for the transaction of business, but a lesser number of members may hold hearings.\n##### (e) Chairperson\nThe Chairperson of the Commission shall be selected by a majority of the Members of the Commission.\n##### (f) Report\nNot later than 2 years after the date of enactment of this Act, the Commission shall submit to the President, the Committee on Agriculture of the House of Representatives, and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report containing the results of the study required by subsection (b), including\u2014\n**(1)**\nan inventory of surveys conducted by the National Agricultural Statistics Service and the frequency with which they are conducted; and\n**(2)**\nsuch recommendations for administrative, regulatory, and legislative changes as the Commission considers appropriate.\n##### (g) Hearings\nThe Commission shall hold such hearings, meet and act at such times and places, take such testimony, and receive such evidence as the Commission considers appropriate to carry out this section.\n##### (h) Stakeholder engagement\nThe Commission shall establish a process to collect feedback from agricultural stakeholders to inform the results of the study required under subsection (b) and the report required under subsection (f).\n##### (i) Information from Federal agencies\n**(1) In general**\nThe Commission may secure directly from a Federal agency such information as the Commission considers necessary to carry out this section.\n**(2) Authority to request information**\nAt the request of the Chairperson of the Commission for information described in paragraph (1), the head of a Federal agency shall provide such information to the Commission.\n##### (j) Postal services\nThe Commission may use the United States mail in the same manner and under the same conditions as other agencies of the Federal Government.\n##### (k) Assistance from the Secretary\nThe Secretary of Agriculture shall provide to the Commission appropriate office space and such reasonable administrative and support services as the Commission may request.\n##### (l) Compensation of members\n**(1) Non-Federal employees**\nA member of the Commission who is not an officer or employee of the Federal Government shall be compensated at a rate equal to the daily equivalent of the annual rate of basic pay prescribed for level IV of the Executive Schedule under section 5315 of title 5, United States Code, for each day (including travel time) during which the member is engaged in the performance of the duties of the Commission.\n**(2) Federal employees**\nA member of the Commission who is an officer or employee of the Federal Government shall serve without compensation in addition to the compensation received for the services of the member as an officer or employee of the Federal Government.\n**(3) Travel expenses**\nA member of the Commission shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for an employee of an agency under subchapter I of chapter 57 of title 5, United States Code, while away from the home or regular place of business of the member in the performance of the duties of the Commission.\n##### (m) Federal Advisory Committee Act\nSections 1008 and 1013 of title 5, United States Code, shall not apply to the Commission or any proceeding of the Commission.\n##### (n) Termination\nThe Commission shall terminate on September 30, 2030.\n##### (o) Funding\nThere is authorized to be appropriated to carry out this section $1,000,000 for fiscal year 2026, to remain available until expended.",
      "versionDate": "2025-03-24",
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
        "actionDate": "2026-02-13",
        "text": "Referred to the House Committee on Agriculture."
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
        "updateDate": "2025-05-14T12:21:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
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
          "measure-id": "id119hr2307",
          "measure-number": "2307",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-24",
          "originChamber": "HOUSE",
          "update-date": "2025-05-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2307v00",
            "update-date": "2025-05-30"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill establishes the Commission on National Agricultural Statistics Service (NASS) Modernization to study and provide recommendations on modernizing and streamlining data collection at NASS. As background, NASS conducts the Census of Agriculture and provides official statistics on agricultural production and other farm sector indicators.</p><p>The 11-member commission must include 4 specified members from the Department of Agriculture, 1 member from the Bureau of Labor Statistics, and 6 members appointed by the House and Senate Agriculture Committees.</p><p>At the request of the commission chair, federal agencies must provide the commission information related to the study.</p><p>The commission must submit a report to the President and Congress on the results of the study within two years of the bill's enactment. The report must include (1) an inventory of surveys conducted by NASS and their frequency; and (2) recommendations for administrative, regulatory, and legislative changes.</p>"
        },
        "title": "To establish the Commission on National Agricultural Statistics Service Modernization to modernize the data collection and reporting processes of the National Agricultural Statistics Service, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2307.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill establishes the Commission on National Agricultural Statistics Service (NASS) Modernization to study and provide recommendations on modernizing and streamlining data collection at NASS. As background, NASS conducts the Census of Agriculture and provides official statistics on agricultural production and other farm sector indicators.</p><p>The 11-member commission must include 4 specified members from the Department of Agriculture, 1 member from the Bureau of Labor Statistics, and 6 members appointed by the House and Senate Agriculture Committees.</p><p>At the request of the commission chair, federal agencies must provide the commission information related to the study.</p><p>The commission must submit a report to the President and Congress on the results of the study within two years of the bill's enactment. The report must include (1) an inventory of surveys conducted by NASS and their frequency; and (2) recommendations for administrative, regulatory, and legislative changes.</p>",
      "updateDate": "2025-05-30",
      "versionCode": "id119hr2307"
    },
    "title": "To establish the Commission on National Agricultural Statistics Service Modernization to modernize the data collection and reporting processes of the National Agricultural Statistics Service, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill establishes the Commission on National Agricultural Statistics Service (NASS) Modernization to study and provide recommendations on modernizing and streamlining data collection at NASS. As background, NASS conducts the Census of Agriculture and provides official statistics on agricultural production and other farm sector indicators.</p><p>The 11-member commission must include 4 specified members from the Department of Agriculture, 1 member from the Bureau of Labor Statistics, and 6 members appointed by the House and Senate Agriculture Committees.</p><p>At the request of the commission chair, federal agencies must provide the commission information related to the study.</p><p>The commission must submit a report to the President and Congress on the results of the study within two years of the bill's enactment. The report must include (1) an inventory of surveys conducted by NASS and their frequency; and (2) recommendations for administrative, regulatory, and legislative changes.</p>",
      "updateDate": "2025-05-30",
      "versionCode": "id119hr2307"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2307ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Commission on National Agricultural Statistics Service Modernization to modernize the data collection and reporting processes of the National Agricultural Statistics Service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T04:48:21Z"
    },
    {
      "title": "To establish the Commission on National Agricultural Statistics Service Modernization to modernize the data collection and reporting processes of the National Agricultural Statistics Service, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T08:05:29Z"
    }
  ]
}
```
