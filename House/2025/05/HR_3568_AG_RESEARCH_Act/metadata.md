# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3568?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3568
- Title: AG RESEARCH Act
- Congress: 119
- Bill type: HR
- Bill number: 3568
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2025-12-05T21:56:10Z
- Update date including text: 2025-12-05T21:56:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3568",
    "number": "3568",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001216",
        "district": "8",
        "firstName": "Kim",
        "fullName": "Rep. Schrier, Kim [D-WA-8]",
        "lastName": "Schrier",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "AG RESEARCH Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:56:10Z",
    "updateDateIncludingText": "2025-12-05T21:56:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
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
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:01:25Z",
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
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "KS"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3568ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3568\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Ms. Schrier (for herself and Mr. Mann ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Research Facilities Act and the Agricultural Research, Extension, and Education Reform Act of 1998 to address deferred maintenance at agricultural research facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Augmenting Research and Educational Sites to Ensure Agriculture Remains Cutting-edge and Helpful Act or the AG RESEARCH Act .\n#### 2. Agricultural research facilities\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nin 2019, agriculture and related industries\u2014\n**(A)**\ncontributed $1,109,000,000,000 to the gross domestic product of the United States (5.2 percent of the total gross domestic product of the United States); and\n**(B)**\nprovided 22,200,000 jobs domestically (10.9 percent of total employment in the United States);\n**(2)**\nthe National Institute of Food and Agriculture provides more than $1,700,000,000 in research funding each year to schools of agriculture;\n**(3)**\na study published in 2015 found that deferred maintenance needs at 91 schools of agriculture across the United States totaled $8,400,000,000, with a total replacement cost of $29,000,000,000;\n**(4)**\na study published in 2021 found that deferred maintenance needs at schools of agriculture across the United States had increased to $11,500,000,000, with a total replacement cost of $38,100,000,000; and\n**(5)**\ninfrastructure investments must be made at schools of agriculture to ensure that United States agricultural research remains globally competitive.\n##### (b) Evaluation of proposals\nSection 3(d) of the Research Facilities Act ( 7 U.S.C. 390a(d) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1) and (2) as paragraphs (2) and (3), respectively; and\n**(2)**\nby inserting before paragraph (2) (as so redesignated) the following:\n(1) review the proposal in consultation with representatives of National Institute of Food and Agriculture peer review panels; .\n##### (c) Grants for agricultural research facilities\nSection 4 of the Research Facilities Act ( 7 U.S.C. 390b ) is amended to read as follows:\n4. Grants for agricultural research facilities (a) Purpose The purpose of this section is to assist agricultural research facilities in efforts to alter or repair those facilities or equipment of the facilities necessary for conducting agricultural research. (b) Grant program (1) In general The Secretary shall establish in the National Institute of Food and Agriculture a competitive grant program to provide to agricultural research facilities the Federal share of the cost of the construction, alteration, acquisition, modernization, renovation, or remodeling of\u2014 (A) the agricultural research facilities; or (B) equipment of the agricultural research facilities necessary for conducting agricultural research. (2) Secretarial waiver Notwithstanding section 3(c)(2)(A), the Secretary may provide that the Federal share described in paragraph (1) is up to 100 percent of the costs described in that paragraph on a case-by-case basis, as the Secretary determines to be appropriate. (c) Requirements (1) Amount; terms and conditions Grants awarded under this section shall be in such amounts and under such terms and conditions as the Secretary determines are necessary to carry out the purpose of this section. (2) Equitable distribution To the maximum extent practicable, grants shall be awarded under this section to ensure\u2014 (A) an equitable geographic distribution of funds; (B) an equitable distribution of funds to diverse institutions; (C) an equitable distribution of funds to institutions with diverse areas of study within agricultural science; and (D) an equitable distribution of funds to agricultural research facilities of various sizes. (3) Limitation Not greater than 20 percent of amounts made available to carry out this section shall be awarded to projects in any 1 State. (4) Administration In carrying out this section, the Secretary shall establish procedures for\u2014 (A) the submission of proposals for competitive grants; and (B) in consultation with representatives of National Institute of Food and Agriculture peer review panels, the review and selection of proposals submitted under subparagraph (A). .\n##### (d) Funding\nSection 6 of the Research Facilities Act ( 7 U.S.C. 390d ) is amended\u2014\n**(1)**\nby striking the section designation and heading and all that follows through the end of subsection (a) and inserting the following:\n6. Funding and limitations on use of funds (a) Funding (1) Mandatory funding (A) In general Subject to subsections (b) through (d), but notwithstanding any other provision of law, on October 1, 2025, and on each October 1 thereafter through October 1, 2029, out of any funds in the Treasury not otherwise appropriated, the Secretary of the Treasury shall transfer to the Secretary to carry out section 4 $500,000,000, to remain available until expended. (B) Receipt and acceptance The Secretary shall be entitled to receive, shall accept, and shall use to carry out section 4 the funds transferred under paragraph (1), without further appropriation. (2) Authorization of appropriations In addition to amounts made available under paragraph (1), subject to subsections (b) through (d), there is authorized to be appropriated to the Secretary not more than $1,000,000,000 for each of fiscal years 2026 through 2030, to remain available until expended, for the study, plan, design, structure, and related costs of agricultural research facilities under this Act. ; and\n**(2)**\nin subsection (b), by inserting Federal before administration .",
      "versionDate": "2025-05-21",
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
        "actionDate": "2025-05-21",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1825",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "AG RESEARCH Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-06-23T18:13:51Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3568ih.xml"
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
      "title": "AG RESEARCH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-31T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AG RESEARCH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Augmenting Research and Educational Sites to Ensure Agriculture Remains Cutting-edge and Helpful Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Research Facilities Act and the Agricultural Research, Extension, and Education Reform Act of 1998 to address deferred maintenance at agricultural research facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:31Z"
    }
  ]
}
```
