# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/381?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/381
- Title: LNG Public Interest Determination Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 381
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2026-05-30T08:05:39Z
- Update date including text: 2026-05-30T08:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-14: Introduced in House

## Actions

- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/381",
    "number": "381",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "LNG Public Interest Determination Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:39Z",
    "updateDateIncludingText": "2026-05-30T08:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T15:02:30Z",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "AZ"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "RI"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "MA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "DC"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "ME"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "MI"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "WA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NV"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MN"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "VA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NM"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MN"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "CA"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "VA"
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
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MI"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr381ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 381\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2025 Mr. Casten (for himself, Ms. Barrag\u00e1n , Ms. Castor of Florida , Mr. Grijalva , Mr. Huffman , Mr. Levin , Mr. Magaziner , Mr. McGovern , Mr. Mullin , Mr. Nadler , Ms. Norton , Ms. Pingree , Ms. Schakowsky , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Natural Gas Act to require that impacts to climate stability, consumer energy costs, and environmental justice be considered in a determination of whether proposed exportation of natural gas is in the public interest, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the LNG Public Interest Determination Act of 2025 .\n#### 2. Exportation of natural gas\n##### (a) Exportation of natural gas\nSection 3 of the Natural Gas Act ( 15 U.S.C. 717b ) is amended by adding at the end the following:\n(g) Exportation of natural gas (1) Order required No person shall export any natural gas from the United States to a foreign country without first having secured an order of the Secretary of Energy authorizing it to do so. The Secretary of Energy may issue such order upon application only if, after opportunity for hearing, the Secretary of Energy finds that the proposed exportation will be consistent with the public interest. The Secretary of Energy may by its order grant such application, in whole or in part, with such modification and upon such terms and conditions as the Secretary of Energy may find necessary or appropriate, and may from time to time, after opportunity for hearing, and for good cause shown, issue such supplemental order for such exportation as it may find necessary or appropriate. (2) Deadline The Secretary of Energy shall find whether proposed exportation of natural gas will be consistent with the public interest under paragraph (1) by not later than the date that is 1 year after the later of\u2014 (A) the date on which the Secretary of Energy receives the final environmental impact statement for such proposed exportation from the Federal Energy Regulatory Commission; and (B) the date on which the Secretary completes each assessment required by paragraph (4). (3) Public interest finding The Secretary of Energy may find that proposed exportation of natural gas for which an application is submitted under paragraph (1) will be consistent with the public interest under such paragraph only if the Secretary of Energy determines, based on the applicable assessment under paragraph (4), that the proposed exportation of natural gas will not be likely to\u2014 (A) significantly contribute to climate change, including by slowing the global energy transition needed to achieve deep reductions of global greenhouse gas emissions within the next decade and net-zero global greenhouse gas emissions not later than 2050; (B) materially increase energy prices or energy price volatility for any segment of United States consumers; or (C) create a disproportionate cumulative burden of adverse human or environmental impacts on rural, low-income, minority, and other vulnerable communities. (4) Assessments (A) Climate change assessment A determination under paragraph (3)(A) shall be based on an assessment of the expected impact of the proposed exportation of natural gas on climate change. Such assessment shall be based on the latest scientific information and use the 20-year global warming potential of methane, and shall include\u2014 (i) quantified estimates of the greenhouse gas emissions associated with the full lifecycle of the natural gas proposed for exportation, including emissions associated with the extraction, transportation, liquefaction, storage, regasification, and consumption of such natural gas; (ii) a comparison of the estimated greenhouse gas emissions in clause (i) to a baseline that is consistent with United States international commitments to achieve deep reductions of global greenhouse gas emissions within the next decade and deep decarbonization pathways toward net-zero global greenhouse gas emissions not later than 2050; (iii) an assessment of the potential effects of the proposed exportation of natural gas on clean energy alternatives, including\u2014 (I) any decrease in global investment in and deployment of renewable energy, electrification, and energy efficiency and conservation technologies; and (II) any decrease in United States exports of clean energy technologies; (iv) quantified estimates of the social cost of the estimated greenhouse gas emissions in clause (i); and (v) an identification of the extent to which climate change is accelerating the loss of economic value in the United States due to rising sea levels, more intense storms, eroding coasts, increased risk and severity of wild fires, and other impacts associated with climate change. (B) Economic assessment A determination under paragraph (3)(B) shall be based on an assessment of the expected economic impact of the proposed exportation of natural gas, including an assessment of the impact of the proposed exportation on all United States consumers, with specific estimates regarding each of the following consumer subgroups: (i) Low-income consumers. (ii) Working families. (iii) Small businesses. (iv) Manufacturers. (v) State and local governments. (vi) Producers and users of fertilizer. (C) Environmental justice assessment A determination under paragraph (3)(C) shall be based on an assessment of the expected impact of the proposed exportation of natural gas on environmental justice (which shall be consistent with Executive Order 14096 ( 42 U.S.C. 4321 note; relating to revitalizing our Nation's commitment to environmental justice for all), as published April 21, 2023), including assessments of impacts on\u2014 (i) the preexisting cumulative environmental burdens and social and health risks posed to rural, low-income, minority, and other vulnerable communities; (ii) local fisheries and the economic livelihood of the people employed by local fisheries; (iii) racial and socioeconomic disparities in impacted communities; and (iv) compliance with civil rights laws. (5) Public participation The Secretary of Energy shall\u2014 (A) provide to the public an opportunity to meaningfully participate, including by providing comments, in\u2014 (i) the finding of the Secretary of Energy on whether proposed exportation will be consistent with the public interest under paragraph (1); and (ii) any study by the Department of Energy intended to inform such finding; and (B) ensure that opportunities to meaningfully participate under subparagraph (A) address barriers that affect members of communities with environmental justice concerns, including those related to disability, language access, and lack of resources. (6) Major Federal action Issuing an order authorizing the exportation of natural gas under this subsection shall be considered a major Federal action under section 102(2)(C) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332(2)(C) ). .\n##### (b) Conforming amendments\nSection 3 of the Natural Gas Act ( 15 U.S.C. 717b ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking export any natural gas from the United States to a foreign country or ;\n**(B)**\nby inserting to the United States after from a foreign country ; and\n**(C)**\nby striking exportation or ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby striking , or the exportation of natural gas to a nation with which there is in effect a free trade agreement requiring national treatment for trade in natural gas, ; and\n**(B)**\nby striking or exportation .\n#### 3. Process coordination; hearings; rules of procedure\nSection 15(b)(1) of the Natural Gas Act ( 15 U.S.C. 717n(b)(1) ) is amended by striking Commission and inserting Federal Energy Regulatory Commission .\n#### 4. Termination of categorical exclusion for approval or disapproval of the exportation of natural gas\nThe categorical exclusion under B5.7 of appendix B to subpart D of part 1021 of title 10, Code of Federal Regulations, (relating to export of natural gas and associated transportation by marine vessel) shall have no force or effect.\n#### 5. Rulemaking\nNot later than one year after the date of enactment of this Act, the Secretary of Energy shall issue a rule to carry out this Act and the amendments made by this Act.",
      "versionDate": "2025-01-14",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alternative and renewable resources",
            "updateDate": "2025-04-25T16:55:59Z"
          },
          {
            "name": "Climate change and greenhouse gases",
            "updateDate": "2025-04-25T16:54:58Z"
          },
          {
            "name": "Department of Energy",
            "updateDate": "2025-04-25T16:55:29Z"
          },
          {
            "name": "Energy prices",
            "updateDate": "2025-04-25T16:55:07Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-04-25T16:55:48Z"
          },
          {
            "name": "Environmental regulatory procedures",
            "updateDate": "2025-04-25T16:55:20Z"
          },
          {
            "name": "Marine and inland water transportation",
            "updateDate": "2025-04-25T16:55:38Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-04-25T16:54:42Z"
          },
          {
            "name": "Public participation and lobbying",
            "updateDate": "2025-04-25T16:56:07Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-04-25T16:54:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-04-17T20:27:13Z"
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
          "measure-id": "id119hr381",
          "measure-number": "381",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr381v00",
            "update-date": "2025-04-14"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>LNG Public Interest Determination Act of 2025</strong></p><p>This bill modifies and expands requirements for exporting natural gas, including liquefied natural gas (LNG).</p><p>Under the existing provisions of the Natural Gas Act, exporters of natural gas must obtain authorization to make such exports\u00a0from the Federal Energy Regulatory Commission (FERC). Additionally, FERC must authorize such exports if they are consistent with the public interest.</p><p>The bill directs exporters of natural gas to obtain authorization from the Department of Energy (DOE) rather than from FERC. Before granting an authorization, DOE must determine that the export would not likely (1) contribute significantly to climate change; (2) materially increase energy prices or energy price volatility for U.S. consumers; or (3) create a disproportionate health or environmental burden on rural, low-income, minority, and other vulnerable communities.</p><p>The bill also classifies an authorization of the exportation of natural gas as a major federal action that triggers the environmental review process required under the National Environmental Policy Act of 1969 (NEPA).</p><p>Additionally, the bill terminates the categorical exclusion for\u00a0exports of natural gas, and any associated transportation of LNG by marine vessels, from\u00a0NEPA environmental review requirements. A categorical exclusion is a class of actions that a federal agency has determined do not significantly affect the quality of the human environment and, thus, do not require either an environmental assessment nor an environmental impact statement.</p>"
        },
        "title": "LNG Public Interest Determination Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr381.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>LNG Public Interest Determination Act of 2025</strong></p><p>This bill modifies and expands requirements for exporting natural gas, including liquefied natural gas (LNG).</p><p>Under the existing provisions of the Natural Gas Act, exporters of natural gas must obtain authorization to make such exports\u00a0from the Federal Energy Regulatory Commission (FERC). Additionally, FERC must authorize such exports if they are consistent with the public interest.</p><p>The bill directs exporters of natural gas to obtain authorization from the Department of Energy (DOE) rather than from FERC. Before granting an authorization, DOE must determine that the export would not likely (1) contribute significantly to climate change; (2) materially increase energy prices or energy price volatility for U.S. consumers; or (3) create a disproportionate health or environmental burden on rural, low-income, minority, and other vulnerable communities.</p><p>The bill also classifies an authorization of the exportation of natural gas as a major federal action that triggers the environmental review process required under the National Environmental Policy Act of 1969 (NEPA).</p><p>Additionally, the bill terminates the categorical exclusion for\u00a0exports of natural gas, and any associated transportation of LNG by marine vessels, from\u00a0NEPA environmental review requirements. A categorical exclusion is a class of actions that a federal agency has determined do not significantly affect the quality of the human environment and, thus, do not require either an environmental assessment nor an environmental impact statement.</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119hr381"
    },
    "title": "LNG Public Interest Determination Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>LNG Public Interest Determination Act of 2025</strong></p><p>This bill modifies and expands requirements for exporting natural gas, including liquefied natural gas (LNG).</p><p>Under the existing provisions of the Natural Gas Act, exporters of natural gas must obtain authorization to make such exports\u00a0from the Federal Energy Regulatory Commission (FERC). Additionally, FERC must authorize such exports if they are consistent with the public interest.</p><p>The bill directs exporters of natural gas to obtain authorization from the Department of Energy (DOE) rather than from FERC. Before granting an authorization, DOE must determine that the export would not likely (1) contribute significantly to climate change; (2) materially increase energy prices or energy price volatility for U.S. consumers; or (3) create a disproportionate health or environmental burden on rural, low-income, minority, and other vulnerable communities.</p><p>The bill also classifies an authorization of the exportation of natural gas as a major federal action that triggers the environmental review process required under the National Environmental Policy Act of 1969 (NEPA).</p><p>Additionally, the bill terminates the categorical exclusion for\u00a0exports of natural gas, and any associated transportation of LNG by marine vessels, from\u00a0NEPA environmental review requirements. A categorical exclusion is a class of actions that a federal agency has determined do not significantly affect the quality of the human environment and, thus, do not require either an environmental assessment nor an environmental impact statement.</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119hr381"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr381ih.xml"
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
      "title": "LNG Public Interest Determination Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LNG Public Interest Determination Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T12:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Natural Gas Act to require that impacts to climate stability, consumer energy costs, and environmental justice be considered in a determination of whether proposed exportation of natural gas is in the public interest, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T12:48:17Z"
    }
  ]
}
```
