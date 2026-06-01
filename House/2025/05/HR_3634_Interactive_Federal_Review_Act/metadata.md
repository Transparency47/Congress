# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3634?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3634
- Title: Interactive Federal Review Act
- Congress: 119
- Bill type: HR
- Bill number: 3634
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-12-20T09:07:03Z
- Update date including text: 2025-12-20T09:07:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3634",
    "number": "3634",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Interactive Federal Review Act",
    "type": "HR",
    "updateDate": "2025-12-20T09:07:03Z",
    "updateDateIncludingText": "2025-12-20T09:07:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-30",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-30T19:45:31Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "AZ"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "KS"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "PA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "NY"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3634ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3634\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Johnson of South Dakota (for himself and Mr. Stanton ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo improve the environmental review process for highway projects through the use of interactive, digital, cloud-based platforms and digital twins, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Interactive Federal Review Act .\n#### 2. Digital platforms and digital twins for NEPA reviews for highway projects\n##### (a) Definitions\nIn this section:\n**(1) Covered project**\nThe term covered project means a highway project that received a grant under any of the following:\n**(A)**\nThe nationally significant freight and highway projects program under section 117 of title 23, United States Code (commonly known as the Infrastructure for Rebuilding America (INFRA) grant program ).\n**(B)**\nThe national infrastructure project assistance program under section 6701 of title 49, United States Code (commonly known as the Mega grant program ).\n**(C)**\nThe local and regional project assistance program under section 6702 of title 49, United States Code (commonly known as the Rebuilding American Infrastructure with Sustainability and Equity (RAISE) grant program ).\n**(D)**\nThe program for national infrastructure investments (commonly known as the Rebuilding American Infrastructure with Sustainability and Equity (RAISE) grant program and formerly known as the Better Utilizing Investments to Leverage Development (BUILD) grant program ).\n**(2) Secretary**\nThe term Secretary means the Secretary of Transportation.\n##### (b) Purposes\nThe purposes of this section are\u2014\n**(1)**\nto expedite the environmental review process at Federal agencies and for the general public; and\n**(2)**\nto facilitate interactive public stakeholder engagement and understanding of environmental impacts of projects under the Federal-aid highway system.\n##### (c) Encouraged use of digital platforms and digital twins\n**(1) In general**\nThe Secretary shall encourage recipients of Federal funds from the Secretary to utilize interactive, digital, cloud-based platforms and high fidelity, 3-dimensional digital models of infrastructure project elements, such as digital twins, when carrying out environmental reviews under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) by publishing the guidance described in paragraph (2).\n**(2) Guidance**\nNot later than 90 days after the date of enactment of this Act, the Secretary shall publish technology-neutral best practice guidance to encourage sponsors of projects that receive Federal funds from the Secretary to use an interactive, digital, cloud-based platform and high fidelity, 3-dimensional digital models of infrastructure project elements, such as digital twins, in carrying out the environmental impact analysis and community engagement processes required under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).\n##### (d) Use of digital platforms and digital twins in covered projects\n**(1) In general**\nThe Secretary shall select not less than 10 covered projects to demonstrate the use of interactive, digital, cloud-based platforms and high fidelity, 3-dimensional digital models of infrastructure project elements, such as digital twins, in carrying out the environmental impact analysis and community engagement processes required under that Act, which may include projects in States participating in the surface transportation project delivery program under section 327 of title 23, United States Code.\n**(2) Additional projects**\nIn addition to the covered projects selected by the Secretary under paragraph (1), the Secretary shall include additional projects that utilize interactive, digital, cloud-based platforms and high fidelity, 3-dimensional digital models of infrastructure project elements, such as digital twins, in the report under subsection (e), on request of the sponsors of those projects.\n**(3) Priority**\nNotwithstanding any other provision of law, in selecting covered projects under a program described in subparagraphs (A) through (D) of subsection (a)(1), the Secretary shall give priority to applications for projects that demonstrate a plan to implement an interactive, cloud-based platform and high fidelity, 3-dimensional digital models of infrastructure project elements, such as digital twins, to carry out the environmental impact analysis and community engagement processes required under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).\n##### (e) Reports\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall submit to the Committee on Environment and Public Works of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report on the efficacy of using interactive, cloud-based platforms and high fidelity, 3-dimensional digital models of infrastructure project elements, such as digital twins, in carrying out environmental impact analysis and community engagement requirements under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), including\u2014\n**(A)**\nmetrics that describe estimates of achieved efficiencies, community engagement measures, and efficiencies enjoyed across Federal agencies; and\n**(B)**\nexamples of digital workflows enabled.\n**(2) Publication of examples**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall publish on the website of the Department of Transportation, and submit to the Committee on Environment and Public Works of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives, not less than 5 examples of an environmental impact statement, environmental assessment, or categorical exclusion document developed using an interactive, digital, cloud-based platform and high fidelity, 3-dimensional digital models of infrastructure project elements, such as digital twins.\n##### (f) Savings provision\nNothing in this section affects or interferes with the authorities or responsibilities assumed by a State under section 327 of title 23, United States Code.",
      "versionDate": "2025-05-29",
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "1430",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Interactive Federal Review Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-03T13:17:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-29",
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
          "measure-id": "id119hr3634",
          "measure-number": "3634",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-29",
          "originChamber": "HOUSE",
          "update-date": "2025-07-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3634v00",
            "update-date": "2025-07-31"
          },
          "action-date": "2025-05-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Interactive Federal Review Act</strong></p><p>This bill revises the environmental review process for federal-aid highway projects to encourage the use of certain digital platforms and models.</p><p>Specifically,\u00a0the Department of Transportation (DOT) must encourage recipients of federal highway funding who are carrying out environmental reviews under the National Environmental Policy Act of 1969 (NEPA) to utilize\u00a0(1)\u00a0interactive, digital, cloud-based platforms;\u00a0and (2)\u00a0high fidelity, three-dimensional digital models of infrastructure project elements, such as digital twins.\u00a0</p><p>DOT must also\u00a0select at least 10 federal-aid highway projects to demonstrate the use of\u00a0these platforms and\u00a0models\u00a0in carrying out the environmental impact analysis and community engagement processes required under\u00a0NEPA.</p><p>Further, DOT must publish technology-neutral best practice guidance to encourage sponsors of projects that receive federal funds from DOT to use these platforms and\u00a0models\u00a0in carrying out the environmental impact analysis and community engagement processes required under NEPA.</p>"
        },
        "title": "Interactive Federal Review Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3634.xml",
    "summary": {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Interactive Federal Review Act</strong></p><p>This bill revises the environmental review process for federal-aid highway projects to encourage the use of certain digital platforms and models.</p><p>Specifically,\u00a0the Department of Transportation (DOT) must encourage recipients of federal highway funding who are carrying out environmental reviews under the National Environmental Policy Act of 1969 (NEPA) to utilize\u00a0(1)\u00a0interactive, digital, cloud-based platforms;\u00a0and (2)\u00a0high fidelity, three-dimensional digital models of infrastructure project elements, such as digital twins.\u00a0</p><p>DOT must also\u00a0select at least 10 federal-aid highway projects to demonstrate the use of\u00a0these platforms and\u00a0models\u00a0in carrying out the environmental impact analysis and community engagement processes required under\u00a0NEPA.</p><p>Further, DOT must publish technology-neutral best practice guidance to encourage sponsors of projects that receive federal funds from DOT to use these platforms and\u00a0models\u00a0in carrying out the environmental impact analysis and community engagement processes required under NEPA.</p>",
      "updateDate": "2025-07-31",
      "versionCode": "id119hr3634"
    },
    "title": "Interactive Federal Review Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Interactive Federal Review Act</strong></p><p>This bill revises the environmental review process for federal-aid highway projects to encourage the use of certain digital platforms and models.</p><p>Specifically,\u00a0the Department of Transportation (DOT) must encourage recipients of federal highway funding who are carrying out environmental reviews under the National Environmental Policy Act of 1969 (NEPA) to utilize\u00a0(1)\u00a0interactive, digital, cloud-based platforms;\u00a0and (2)\u00a0high fidelity, three-dimensional digital models of infrastructure project elements, such as digital twins.\u00a0</p><p>DOT must also\u00a0select at least 10 federal-aid highway projects to demonstrate the use of\u00a0these platforms and\u00a0models\u00a0in carrying out the environmental impact analysis and community engagement processes required under\u00a0NEPA.</p><p>Further, DOT must publish technology-neutral best practice guidance to encourage sponsors of projects that receive federal funds from DOT to use these platforms and\u00a0models\u00a0in carrying out the environmental impact analysis and community engagement processes required under NEPA.</p>",
      "updateDate": "2025-07-31",
      "versionCode": "id119hr3634"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3634ih.xml"
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
      "title": "Interactive Federal Review Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Interactive Federal Review Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve the environmental review process for highway projects through the use of interactive, digital, cloud-based platforms and digital twins, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:30Z"
    }
  ]
}
```
