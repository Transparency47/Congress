# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6684?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6684
- Title: Zero Food Waste Act
- Congress: 119
- Bill type: HR
- Bill number: 6684
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-04-13T12:04:27Z
- Update date including text: 2026-04-13T12:04:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-12: Introduced in House

## Actions

- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6684",
    "number": "6684",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Zero Food Waste Act",
    "type": "HR",
    "updateDate": "2026-04-13T12:04:27Z",
    "updateDateIncludingText": "2026-04-13T12:04:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
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
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:00:20Z",
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
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "ME"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "IL"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "HI"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6684ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6684\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Ms. Brownley (for herself, Ms. Pingree , Mr. Casten , and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide grants to reduce the amount of food waste, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Zero Food Waste Act .\n#### 2. Food waste reduction grants\n##### (a) In general\n**(1) Establishment**\nThe Administrator shall establish and carry out a program to award competitive grants as provided in paragraph (3).\n**(2) Purpose**\nThe purpose of the program established under paragraph (1) is to help reduce the amount of food waste by 50 percent by 2035, relative to such amount in 2015.\n**(3) Grants**\n**(A) Study on food waste generation and food waste management planning**\nUnder the program established under paragraph (1), the Administrator may award a grant to an eligible entity, excluding any eligible entity that is a nonprofit organization, to\u2014\n**(i)**\nstudy\u2014\n**(I)**\nthe generation of food waste in the State or area in which the eligible entity is located or otherwise serves; and\n**(II)**\npolicies and programs that significantly reduce the amount of food waste, including policies and programs to carry out food waste reduction activities; and\n**(ii)**\ndevelop a plan under which such eligible entity will carry out at least one food waste reduction activity, prioritizing prevention to the extent practicable.\n**(B) Food waste data and reports**\nUnder the program established under paragraph (1), the Administrator may award a grant to an eligible entity, excluding any eligible entity that is a nonprofit organization, to\u2014\n**(i)**\ncollect data on the amount of food waste generated in the State or area in which the eligible entity is located or otherwise serves; and\n**(ii)**\npublish, on any publicly available website (which may include the website of a nongovernmental organization), a monthly or quarterly report on the data collected under clause (i).\n**(C) Food waste reduction projects**\nUnder the program established under paragraph (1), the Administrator may award a grant to an eligible entity to\u2014\n**(i)**\n**(I)**\ncarry out or otherwise support a food waste reduction activity;\n**(II)**\nimplement a differential pricing policy on the disposal of food waste to\u2014\n**(aa)**\ndisincentivize disposing of food waste by incineration or deposit in a landfill; and\n**(bb)**\nincentivize carrying out food waste reduction activities;\n**(III)**\npay for or provide technical assistance to carry out a food waste reduction activity;\n**(IV)**\nimplement restrictions on disposing of food waste by incineration or deposit in a landfill;\n**(V)**\nimplement food waste reduction activity requirements;\n**(VI)**\nimplement demand-stimulating policies for recycling end-markets; or\n**(VII)**\ncarry out any other activity the Administrator determines will reduce the amount of food waste in the applicable area; and\n**(ii)**\ncollect data and publish reports as described in subparagraph (B).\n##### (b) Applications\n**(1) In general**\nTo apply for a grant under this section, an eligible entity shall submit to the Administrator an application at such time and in such form as the Administrator may require, which such application shall demonstrate how the eligible entity will use the grant in accordance with subsection (a)(3).\n**(2) Nonprofit organizations**\nIn the case of an application from an eligible entity that is a nonprofit organization, the application shall include\u2014\n**(A)**\na letter of support for the proposed use of the grant from\u2014\n**(i)**\nthe relevant local government, territorial government, Tribal government, or State; or\n**(ii)**\nanother nonprofit organization that\u2014\n**(I)**\nhas a demonstrated history of undertaking work in the geographic region where the proposed use of the grant is to take place, as determined by the Administrator; and\n**(II)**\nwould not be involved in the proposed use of the grant; and\n**(B)**\nany other information the Administrator may require.\n**(3) Prioritization**\nIn awarding grants under this section, the Administrator shall\u2014\n**(A)**\nseek to award grants for use in diverse locations and for diverse uses; and\n**(B)**\nprioritize awarding grants to\u2014\n**(i)**\nany eligible entity, excluding any eligible entity that is a nonprofit organization, that\u2014\n**(I)**\nimplements a program to carry out food waste reduction activities; or\n**(II)**\nhas a demonstrated need, as determined by the Administrator, for additional investment in infrastructure or other resources to be able to implement a program to carry out food waste reduction activities; or\n**(ii)**\nan eligible entity that will use such grant as provided in subsection (a)(3)(C)(i) in a community of color, low-income community, or Tribal community that has been disproportionately affected by adverse human health or environmental effects.\n**(4) Anaerobic digestion projects**\nWith respect to any grant awarded under subsection (a)(3)(C) to carry out an anaerobic digestion project, the Administrator shall\u2014\n**(A)**\nrequire that the applicant submit a plan for end-product recycling that, in accordance with guidelines the Administrator shall establish\u2014\n**(i)**\nprovides for the use of the material resulting from the project as a soil amendment; and\n**(ii)**\nensures that the use of the material resulting from the project does not create an environmental hazard; and\n**(B)**\nrequire the eligible entity that is carrying out the project\u2014\n**(i)**\nto limit its use of animal waste to not more than 20 percent of the total feedstock of the project; and\n**(ii)**\nto only use source separated organics as the portion of the total feedstock that is not animal waste.\n##### (c) Reporting\n**(1) Effect of use of grant**\nEach eligible entity that receives a grant under this section shall submit to the Administrator a report, at such time and in such form as the Administrator may require, on the results of the use of the grant, which such report shall include any relevant data requested by the Administrator for purposes of tracking the effectiveness of the program established under subsection (a)(1).\n**(2) Annual report**\nThe Administrator shall submit to Congress and make publicly available on the website of the Environmental Protection Agency an annual report describing\u2014\n**(A)**\nthe effectiveness of the program established under subsection (a)(1) at reducing the amount of food waste by 50 percent by 2035, relative to such amount in 2015, including information on the progress of such reduction; and\n**(B)**\nhow the Administrator is promoting learning among grantees and other stakeholders to better achieve results.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $650,000,000 for each of fiscal years 2026 through 2035, to remain available until expended.\n##### (e) Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State, a local government, a territorial government, or a Tribal government;\n**(B)**\na nonprofit organization; or\n**(C)**\na partnership of two or more of any of the entities described in subparagraphs (A) and (B).\n**(3) Food waste**\nThe term food waste means any uneaten food and inedible parts of food.\n**(4) Food waste reduction activity**\nThe term food waste reduction activity means any method or activity that reduces the amount of food waste disposed of in landfills or incinerated, including through prevention, rescue, upcycling, and recycling.\n**(5) Nonprofit organization**\nThe term nonprofit organization means an organization that is described in section 501(c)(3) of the Internal Revenue Code of 1986 ( 26 U.S.C. 501(c)(3) ) and is exempt from taxation under section 501(a) of such Code.\n**(6) Prevent**\nThe term prevent means to forestall the generation of food waste.\n**(7) Recycle**\nThe term recycle means to reuse food waste as a feedstock for a non-food product.\n**(8) Rescue**\nThe term rescue means to redirect surplus food for consumption.\n**(9) Source separated organics**\n**(A) In general**\nThe term source separated organics means organic waste that is separated from other waste by the waste generator.\n**(B) Inclusion**\nThe term source separated organics includes materials that are certified to meet ASTM standard D6400 or D6868.\n**(C) Exclusion**\nThe term source separated organics excludes mixed solid waste.\n**(10) Upcycle**\nThe term upcycle means to make new food from ingredients that otherwise would become food waste.",
      "versionDate": "2025-12-12",
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
        "actionDate": "2025-12-11",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "3443",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Zero Food Waste Act",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-08T14:42:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-12",
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
          "measure-id": "id119hr6684",
          "measure-number": "6684",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-12",
          "originChamber": "HOUSE",
          "update-date": "2026-04-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6684v00",
            "update-date": "2026-04-13"
          },
          "action-date": "2025-12-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Zero Food Waste Act</strong></p><p>This bill directs the Environmental Protection Agency to establish a grant program to study and reduce food waste. States, local governments, territorial governments, tribal governments, and nonprofit organizations may apply for the grants.</p>"
        },
        "title": "Zero Food Waste Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6684.xml",
    "summary": {
      "actionDate": "2025-12-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Zero Food Waste Act</strong></p><p>This bill directs the Environmental Protection Agency to establish a grant program to study and reduce food waste. States, local governments, territorial governments, tribal governments, and nonprofit organizations may apply for the grants.</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119hr6684"
    },
    "title": "Zero Food Waste Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Zero Food Waste Act</strong></p><p>This bill directs the Environmental Protection Agency to establish a grant program to study and reduce food waste. States, local governments, territorial governments, tribal governments, and nonprofit organizations may apply for the grants.</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119hr6684"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6684ih.xml"
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
      "title": "Zero Food Waste Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Zero Food Waste Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide grants to reduce the amount of food waste, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T05:48:17Z"
    }
  ]
}
```
