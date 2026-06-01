# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1021?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1021
- Title: Dairy Nutrition Incentive Program Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1021
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-01-09T12:03:22Z
- Update date including text: 2026-01-09T12:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1021",
    "number": "1021",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Dairy Nutrition Incentive Program Act of 2025",
    "type": "S",
    "updateDate": "2026-01-09T12:03:22Z",
    "updateDateIncludingText": "2026-01-09T12:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-03-13T16:42:14Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-13T16:42:14Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "KS"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "MN"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "NY"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "ID"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "AL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "PA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "VT"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MI"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1021is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1021\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Ms. Klobuchar (for herself, Mr. Marshall , Ms. Smith , Mrs. Gillibrand , and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food and Nutrition Act of 2008 to establish a dairy nutrition incentive program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dairy Nutrition Incentive Program Act of 2025 .\n#### 2. Dairy nutrition incentive program\n##### (a) In general\nThe Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) is amended by adding at the end the following:\n31. Dairy nutrition incentive program (a) Definitions In this section: (1) Dairy product The term dairy product means a product for which cow\u2019s milk is listed as\u2014 (A) the first ingredient on the labeled ingredients list of the product; or (B) the second ingredient on the labeled ingredients list of the product, if the first listed ingredient is water. (2) Eligible entity The term eligible entity means\u2014 (A) a State or local governmental entity; and (B) a nonprofit organization. (3) Fluid milk The term fluid milk means any variety of pasteurized cow\u2019s milk that\u2014 (A) is packaged in liquid form; and (B) contains vitamins A and D at levels consistent with the Food and Drug Administration standards, and applicable State and local standards, for fluid milk. (4) Naturally nutrient-rich dairy The term naturally nutrient-rich dairy means\u2014 (A) fluid milk; (B) yogurt and other cultured cow\u2019s milk dairy products; and (C) cheese (including nonstandardized cheese) made from cow\u2019s milk. (5) Program The term program means the dairy nutrition incentive program established under subsection (b). (b) Establishment Not later than 180 days after the date of enactment of this section, the Secretary shall establish a dairy nutrition incentive program under which the Secretary shall develop and test methods to increase the purchase and consumption of naturally nutrient-rich dairy by members of households that receive benefits under the supplemental nutrition assistance program by providing an incentive for the purchase of naturally nutrient-rich dairy at the point of purchase to members of households purchasing food using those benefits. (c) Grants or cooperative agreements (1) In general To carry out the program, the Secretary shall enter into cooperative agreements with, or provide grants to, eligible entities, on a competitive basis, for projects that meet the purpose of the program described in subsection (b). (2) Application An eligible entity seeking to enter into a cooperative agreement or receive a grant under the program shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (3) Selection criteria The Secretary shall develop and make public criteria for evaluating proposed projects in applications submitted under paragraph (2), which shall incorporate a scientifically based strategy designed to improve diet quality and nutritional outcomes through the increased purchase of naturally nutrient-rich dairy. (4) Priority In entering into cooperative agreements and awarding grants under the program, the Secretary shall give priority to projects that\u2014 (A) maximize the percentage of funds used for direct incentives for participants in the supplemental nutrition assistance program; (B) include a project design\u2014 (i) that provides incentives when naturally nutrient-rich dairy is purchased using benefits under the supplemental nutrition assistance program; and (ii) in which the incentives earned may be used only to purchase naturally nutrient-rich dairy; (C) include project sites that serve members of households that participate in the supplemental nutrition assistance program; and (D) incorporate the use of point-of-sale systems that can electronically issue incentives earned under the program. (5) Additional financial assistance An eligible entity may request funds from the Secretary, pursuant to section 16, to offset initial costs to enable electronic benefits transfer technology for electronic point-of-sale systems described in paragraph (4)(D) for project sites selected under the program. (d) Evaluation (1) In general The Secretary shall provide for an independent evaluation of each project carried out under the program that measures, to the maximum extent practicable, the effect of incentives on purchases of naturally nutrient-rich dairy by members of households that receive benefits under the supplemental nutrition assistance program. (2) Methodology requirement The independent evaluation under paragraph (1) shall use rigorous methodologies, such as random assignment or other methods that are capable of producing scientifically valid information regarding activities that are effective. (3) Discontinuance (A) In general Except as provided in subparagraph (B), subject to availability of funds, nothing in this section shall limit the continuation of a project carried out under the program. (B) Noncompliance The Secretary may discontinue a project or close a project site under the program if the project\u2014 (i) does not comply with the requirements under this section; (ii) does not comply with the requirements of the grant awarded or cooperative agreement entered into under the program, as applicable; or (iii) if the Secretary determines that the results of the independent evaluation of the project under paragraph (1) are not satisfactory. (4) Public dissemination The Secretary shall make publicly available the results of each independent evaluation carried out under paragraph (1). (e) Report Not later than December 31 of the first full calendar year following the date of establishment of the program, and biennially thereafter, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report that includes a description of\u2014 (1) the status of each project carried out under the program; and (2) the results of each completed evaluation under paragraph (1) during the period covered by the report. (f) Funding (1) Mandatory funding There is appropriated to the Secretary, out of any funds in the Treasury not otherwise appropriated, $10,000,000 for each fiscal year to carry out this section. (2) Authorization of appropriations (A) In general In addition to the funds made available under paragraph (1), there is authorized to be appropriated to the Secretary to carry out this section $10,000,000 for fiscal year 2025 and each fiscal year thereafter. (B) Appropriations in advance With respect to any funds made available under subparagraph (A), only funds appropriated in advance specifically to carry out this section shall be available to carry out this section. (3) Evaluation costs Of the funds made available to carry out this section for a fiscal year, the Secretary shall use not more than 7 percent to carry out subsection (d). (4) Limitation on use Funds made available to carry out this section shall not be used for any project that limits the use of benefits under the supplemental nutrition assistance program. .\n##### (b) Transition from healthy fluid milk incentives projects\n**(1) In general**\nThe Secretary of Agriculture (referred to in this subsection as the Secretary ) shall transition projects carried out under section 4208 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2026a ) to be carried out as part of the dairy nutrition incentive program established under section 31 of the Food and Nutrition Act of 2008.\n**(2) No interruption**\nIn carrying out paragraph (1), the Secretary shall ensure that\u2014\n**(A)**\nthere is no interruption in projects being carried out under section 4208 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2026a ) during the transition described in that paragraph; and\n**(B)**\nany additional authorities or flexibilities under the dairy nutrition incentive program established under section 31 of the Food and Nutrition Act of 2008 shall be applied to the projects described in subparagraph (A).\n**(3) Repeal**\nEffective 1 year after the date on which the Secretary certifies that the Secretary has completed carrying out paragraph (1), section 4208 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2026a ) is repealed.",
      "versionDate": "2025-03-13",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-18",
        "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry."
      },
      "number": "2496",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Dairy Nutrition Incentive Program Act of 2025",
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
        "updateDate": "2025-05-05T21:01:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-13",
    "originChamber": "Senate",
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
          "measure-id": "id119s1021",
          "measure-number": "1021",
          "measure-type": "s",
          "orig-publish-date": "2025-03-13",
          "originChamber": "SENATE",
          "update-date": "2025-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1021v00",
            "update-date": "2025-05-12"
          },
          "action-date": "2025-03-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Dairy Nutrition Incentive Program Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a dairy nutrition incentive program to develop and test methods to increase the purchase and consumption of dairy under the Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the program must provide an incentive to SNAP benefit recipients for the purchase of naturally nutrient-rich dairy, which the bill defines to include fluid milk, yogurt, and cheese made from cow's milk. To carry out the program, USDA must enter into cooperative agreements with, or provide competitive grants to, state or local governments and nonprofit organizations for projects. The bill provides funding for the program for each fiscal year.</p><p>USDA must provide for an independent evaluation of each project that measures, to the maximum extent practicable, the effect of incentives on purchases of naturally nutrient-rich dairy by SNAP recipients.</p><p>Projects currently carried out by the USDA Healthy Fluid Milk Incentives (HFMI) program must be transitioned to the new dairy nutrition incentive program; the bill repeals the HFMI program one year after USDA certifies that the transition is complete.</p>"
        },
        "title": "Dairy Nutrition Incentive Program Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1021.xml",
    "summary": {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dairy Nutrition Incentive Program Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a dairy nutrition incentive program to develop and test methods to increase the purchase and consumption of dairy under the Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the program must provide an incentive to SNAP benefit recipients for the purchase of naturally nutrient-rich dairy, which the bill defines to include fluid milk, yogurt, and cheese made from cow's milk. To carry out the program, USDA must enter into cooperative agreements with, or provide competitive grants to, state or local governments and nonprofit organizations for projects. The bill provides funding for the program for each fiscal year.</p><p>USDA must provide for an independent evaluation of each project that measures, to the maximum extent practicable, the effect of incentives on purchases of naturally nutrient-rich dairy by SNAP recipients.</p><p>Projects currently carried out by the USDA Healthy Fluid Milk Incentives (HFMI) program must be transitioned to the new dairy nutrition incentive program; the bill repeals the HFMI program one year after USDA certifies that the transition is complete.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119s1021"
    },
    "title": "Dairy Nutrition Incentive Program Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dairy Nutrition Incentive Program Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a dairy nutrition incentive program to develop and test methods to increase the purchase and consumption of dairy under the Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the program must provide an incentive to SNAP benefit recipients for the purchase of naturally nutrient-rich dairy, which the bill defines to include fluid milk, yogurt, and cheese made from cow's milk. To carry out the program, USDA must enter into cooperative agreements with, or provide competitive grants to, state or local governments and nonprofit organizations for projects. The bill provides funding for the program for each fiscal year.</p><p>USDA must provide for an independent evaluation of each project that measures, to the maximum extent practicable, the effect of incentives on purchases of naturally nutrient-rich dairy by SNAP recipients.</p><p>Projects currently carried out by the USDA Healthy Fluid Milk Incentives (HFMI) program must be transitioned to the new dairy nutrition incentive program; the bill repeals the HFMI program one year after USDA certifies that the transition is complete.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119s1021"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1021is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Dairy Nutrition Incentive Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dairy Nutrition Incentive Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food and Nutrition Act of 2008 to establish a dairy nutrition incentive program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T02:48:31Z"
    }
  ]
}
```
