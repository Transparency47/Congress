# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/25?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/25
- Title: Polluters Pay Climate Fund Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 25
- Origin chamber: Senate
- Introduced date: 2025-01-07
- Update date: 2026-01-10T07:22:17Z
- Update date including text: 2026-01-10T07:22:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-07: Introduced in Senate
- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-07: Introduced in Senate

## Actions

- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/25",
    "number": "25",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Polluters Pay Climate Fund Act of 2025",
    "type": "S",
    "updateDate": "2026-01-10T07:22:17Z",
    "updateDateIncludingText": "2026-01-10T07:22:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-07",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-07",
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
        "item": {
          "date": "2025-01-07T16:57:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-07",
      "state": "VT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "OR"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "MA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "VT"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s25is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 25\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2025 Mr. Van Hollen (for himself, Mr. Sanders , Mr. Merkley , Mr. Markey , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo impose an assessment related to fossil fuel emissions, to establish the Polluters Pay Climate Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Polluters Pay Climate Fund Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nclimate change, resulting primarily from the combustion of fossil fuels, is an immediate, grave threat to the communities, environment, and economy of the United States;\n**(2)**\nsevere consequences of climate change have already materialized in the United States, including rising sea levels, increasing temperatures, extreme weather events, flooding, heat waves, loss of biodiversity, and other climate change-driven ecosystem threats;\n**(3)**\nthe Federal government jointly with States and localities must develop and implement protective measures to counteract the adverse effects of climate change, protect communities, and build resilience to extreme weather;\n**(4)**\nthe government response must include protections for communities that are most vulnerable to climate change impacts, especially communities of color, low-income communities, and Tribal and Indigenous communities that are also more likely to have experienced systemic disinvestment and be overburdened by fossil fuel pollution;\n**(5)**\nthe protective measures necessary to respond to the adverse effects of climate change in the United States will require trillions of dollars of new investment during the decade after the date of enactment of this Act;\n**(6)**\nclimate change related extreme weather events, such as those described in paragraph (2), cost the United States at least $150,000,000,000 each year and disproportionately affect underserved and overburdened communities, according to the Fifth National Climate Assessment;\n**(7)**\nthe $100,000,000,000 each year that fossil fuel companies are collectively assessed for the Polluters Pay Climate Fund established in this Act represents only a small portion of the total cost to the Federal government to respond to climate change related extreme weather events and make needed climate change adaptation and resilience investments;\n**(8)**\npeer-reviewed research can now determine with great accuracy the share of carbon dioxide released into the atmosphere by the operations and products of specific fossil fuel companies, which is what informs the formulas to determine carbon dioxide emissions that are used in the amendments made by this Act;\n**(9)**\nthe fossil fuel industry has been aware of the central role that their product plays in causing climate change since before the year 2000;\n**(10)**\nthe fossil fuel industry must now increase their contribution to government expenditures to protect the Nation from climate disaster; and\n**(11)**\nthis Act and assessments under the amendments made by this Act are not intended\u2014\n**(A)**\nto be a determination of fault; or\n**(B)**\nto have any impact on the ability of any person or other government to hold polluters accountable for harms caused.\n#### 3. Tax relating to current stock of greenhouse gas emissions\n##### (a) In general\nChapter 38 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subchapter:\nE Certain fossil fuel emissions Sec. 4691. Imposition of tax. 4691. Imposition of tax (a) Imposition Each assessable person shall pay to the Secretary of the Treasury not later than the applicable payment date a tax in an amount determined under subsection (b). (b) Determination of amount (1) In general With respect to each assessable person, the tax under this section shall be equal to an amount that bears the same ratio to $1,000,000,000,000 as\u2014 (A) the assessable person's applicable share of covered carbon dioxide emissions taken into account under this section, bears to (B) the aggregate applicable shares of covered carbon dioxide emissions of all assessable persons taken into account under this section. (2) Determination of applicable share (A) In general The applicable share of covered carbon dioxide emissions taken into account under this section for any assessable person shall be the excess (if any) of\u2014 (i) the covered carbon dioxide emissions attributable to such person (determined in metric tons), as determined by the Secretary based on product-related carbon dioxide emissions of such person, over (ii) 1,000,000,000 metric tons. (B) Adjustment The Secretary may adjust the amount determined under subparagraph (A)(i) with respect to an assessable person who is described in subsection (c)(2)(B)(ii) (or who is a successor in interest to a person described in such subsection) if such person establishes to the satisfaction of the Secretary that a portion of such amount was\u2014 (i) attributable to the extraction of crude oil by another assessable person who is described in subsection (c)(2)(B)(i) (or a successor in interest to a person described in such subsection), and (ii) taken into account in determining such amount for such other assessable person. (c) Assessable person For purposes of this section\u2014 (1) In general The term assessable person means\u2014 (A) any person that is described in paragraph (2), or (B) any successor in interest to a person described in paragraph (2). (2) Person described A person is described in this paragraph if such person\u2014 (A) is a United States person or is engaged in a trade or business within the United States during the period beginning on the date of the enactment of this Act and ending on December 31, 2025, (B) during any part of the covered period, was engaged in the trade or business of\u2014 (i) extracting any fossil fuel, or (ii) refining any crude oil, and (C) is determined by the Secretary to be responsible for more than 1,000,000,000 metric tons of covered carbon dioxide emissions. (3) Controlled groups (A) In general For purposes of this subsection, all persons treated as a single employer under subsection (a) or (b) of section 52 or subsection (m) or (o) of section 414 shall be treated as a single assessable person. (B) Inclusion of foreign corporations For purposes of subparagraph (A), in applying subsections (a) and (b) of section 52 to this section, section 1563 shall be applied without regard to subsection (b)(2)(C) thereof. (4) Joint and several liability If more than one person is liable for payment of the tax under subsection (a) with respect to a single assessable person by reason of the application of paragraph (3), all such persons shall be jointly and severally liable for payment of such tax. (d) Other definitions and rules For purposes of this section\u2014 (1) Applicable payment date The term applicable payment date means September 30, 2026. (2) Covered carbon dioxide emissions The term covered carbon dioxide emissions means, with respect to any person, the total quantity of carbon dioxide released into the atmosphere during the covered period by reason such person engaging in the trade or business of extracting fossil fuels or of refining crude oil. (3) Covered period The term covered period means the period that\u2014 (A) began on January 1, 2000, and (B) ended on December 31, 2023. (4) Fossil fuel The term fossil fuel means coal, crude oil, and fuel gases. (5) Coal The term coal means anthracite, bituminous, subbituminous, and lignite coal. (6) Crude oil The term crude oil means oil or petroleum of any kind and in any form, including bitumen, oil sands, heavy oil, conventional and unconventional oil, shale oil, natural gas liquids, condensates, and related fossil fuel liquids. (7) Fuel gases The term fuel gases means natural gas, associated natural gas, conventional and unconventional gas, shale gas, and related methane gas production. (8) Determination of carbon dioxide emissions In determining the amount of carbon dioxide emissions with respect to any assessable person\u2014 (A) an amount equivalent to 942.5 metric tons of carbon dioxide shall be treated as released for every 1,000,000 pounds of coal, (B) an amount equivalent to 432,180 metric tons of carbon dioxide shall be treated as released for every 1,000,000 barrels of crude oil, and (C) an amount equivalent to 54,440 metric tons of carbon dioxide shall be treated as released for every 1,000,000,000 cubic feet of fuel gases. (e) Election To pay liability in installments (1) In general An assessable person may elect to pay the tax under this section in 9 annual installments of the following amounts: (A) 20 percent of the tax under this section in the case of the first installment. (B) 10 percent of the tax under this section in each of the following 8 installments. (2) Date for payment of installments If an election is made under paragraph (1), the first installment shall be paid on the applicable payment date and each succeeding installment shall be paid on the same date as the applicable payment date for each calendar year following the calendar year with respect to which the preceding installment was made. (3) Acceleration of payment If there is an addition to tax for failure to timely pay any installment required under this subsection, a liquidation or sale of substantially all the assets of the assessable person (including in a title 11 or similar case), a cessation of business by the assessable person, or any similar circumstance, then the unpaid portion of all remaining installments shall be due on the date of such event (or in the case of a title 11 or similar case, the day before the petition is filed). The preceding sentence shall not apply to the sale of substantially all the assets of an assessable person to a buyer if such buyer enters into an agreement with the Secretary under which such buyer is liable for the remaining installments due under this subsection in the same manner as if such buyer were the assessable person. (4) Proration of deficiency to installments If an election is made under paragraph (1) to pay the tax under this section in installments and a deficiency has been assessed with respect to such tax, the deficiency shall be prorated to the installments payable under paragraph (1). The part of the deficiency so prorated to any installment the date for payment of which has not arrived shall be collected at the same time as, and as a part of, such installment. The part of the deficiency so prorated to any installment the date for payment of which has arrived shall be paid upon notice and demand from the Secretary. This subsection shall not apply if the deficiency is due to negligence, to intentional disregard of rules and regulations, or to fraud with intent to evade tax. (5) Election Any election under paragraph (1) shall be made not later than the applicable payment date and shall be made in such manner as the Secretary shall provide. (6) Installments not to prevent credit or refund of overpayments or increase estimated taxes If an election is made under paragraph (1) to pay the tax under this section in installments\u2014 (A) no installment of such tax shall\u2014 (i) in the case of a request for credit or refund, be taken into account as a liability for purposes of determining whether an overpayment exists for purposes of section 6402 before the date on which such installment is due, or (ii) for purposes of sections 6425, 6654, and 6655, be treated as a tax imposed by section 1, section 11, or subchapter L of chapter 1, and (B) the first sentence of section 6403 shall not apply with respect to any such installment. (f) Regulations Not later than 18 months after the date of enactment of this section, the Secretary shall promulgate such regulations as are necessary to carry out this section. .\n##### (b) No deduction\nSection 275(a) of such Code is amended by adding at the end the following new paragraph:\n(7) Taxes imposed by subchapter E of chapter 38. .\n##### (c) Clerical amendment\nThe table of subchapters for chapter 38 of such Code is amended by adding at the end the following new item:\nSUBCHAPTER E\u2014Certain fossil fuel emissions .\n#### 4. Polluter Pays Climate Change Fund\n##### (a) Establishment of fund\n**(1) In general**\nSubchapter A of chapter 98 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n9512. Polluters Pay Climate Fund (a) Establishment There is established in the Treasury of the United States a trust fund, to be known as the Polluters Pay Climate Fund (hereinafter in this section referred to as the Fund ), consisting of amounts as are appropriated or credited to such Trust Fund as provided in this section and section 9602(b). (b) Transfers There are hereby appropriated to the Fund amounts equivalent to the taxes received in the Treasury under section 4691. (c) Expenditures from the Fund Amounts in the fund shall be available, as provided in appropriations Acts, for the purpose of making expenditures to carry out the purposes of section 4(b) of the Polluters Pay Climate Fund Act of 2025 . .\n**(2) Clerical amendment**\nThe table of sections for subchapter A of chapter 98 of such Code is amended by adding at the end the following new item:\nSec. 9512. Polluters Pay Climate Fund. .\n##### (b) Expenditures from fund\n**(1) Definitions**\nIn this subsection:\n**(A) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(B) Environmental justice community**\nThe term environmental justice community means a community with significant representation of communities of color, low-income communities, or Tribal and Indigenous communities that experiences, or is at risk of experiencing, higher or more adverse human health or environmental effects as compared to other communities.\n**(C) Fund**\nThe term Fund means the Polluters Pay Climate Change Fund established under section 9512 of the Internal Revenue Code of 1986.\n**(D) Secretary**\nThe term Secretary means the Secretary of the Treasury.\n**(2) Use of fund amounts**\n**(A) General purposes**\nThe Secretary, in consultation with the Administrator and the heads of other relevant agencies, shall use amounts in the Fund for the purposes of furthering a comprehensive and equitable Federal response to climate change impacts through investments in climate resilience, adaptation, disaster response, and environmental justice, including\u2014\n**(i)**\nclimate-related disaster recovery and mitigation support;\n**(ii)**\nclimate change adaptation support through climate and disaster planning assistance, funding for climate-resilient infrastructure, and improved climate and extreme weather prediction capabilities;\n**(iii)**\ninitiatives that increase the climate resilience of energy systems through energy efficiency, grid resilience, and distributed electricity generation initiatives;\n**(iv)**\ninitiatives that increase the climate resilience of the food system through support for climate-resilient farming practices;\n**(v)**\ninitiatives that increase the climate resilience of the transportation system through planning and climate change adaptation support;\n**(vi)**\ninitiatives that increase the climate resilience of ecosystems through conservation, restoration, and wildfire management activities;\n**(vii)**\nsupport for climate-related public health initiatives, including efforts to address extreme heat; and\n**(viii)**\ninitiatives that increase the climate resiliency of drinking water and stormwater infrastructure.\n**(B) Specified uses**\nIn carrying out subparagraph (A) each fiscal year and to the greatest extent practicable, the Secretary shall use amounts in the Fund\u2014\n**(i)**\nto provide funding of not less than $15,000,000,000 to the Federal Emergency Management Agency for response and resilience programs of the Federal Emergency Management Agency to address climate-related disasters, including hurricanes, flooding, extreme heat, and wildfires, of which not less than $3,000,000,000 shall be used to carry out the Building Resilient Infrastructure and Communities program under section 203 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5133 ); and\n**(ii)**\nto provide funding of not less than $6,000,000,000 for grants and technical assistance under section 138 of the Clean Air Act ( 42 U.S.C. 7438 ), subject to the condition that the Administrator may determine the appropriate amounts to be used for those grants and that technical assistance.\n**(C) Environmental justice set aside**\nOf the amounts appropriated from the Fund each fiscal year, 40 percent shall be used for investments that benefit environmental justice communities.\n**(D) Selection**\nFor the purpose of determining how to award amounts appropriated from the Fund in excess of the amounts required to be used under subparagraph (B), the Secretary, in coordination with the Administrator and the heads of other relevant agencies, shall establish selection criteria, which shall give the highest priority to projects or other activities that are most impactful in achieving the purposes described in subparagraph (A), as determined by the Secretary, in coordination with the Administrator and the heads of other relevant agencies.\n#### 5. Availability of remedies\n##### (a) In general\nNothing in this Act or the amendments made by this Act shall be construed to relieve any person from liability at common law or under any State or Federal law.\n##### (b) Effect on claims related to climate change\nNothing in this Act or the amendments made by this Act, the Clean Air Act ( 42 U.S.C. 7401 et seq. ), or Federal common law preempts, displaces, or restricts any right or remedy of any person, State, unit of local government, or Tribal government under any State or local law (including common law) relating to an allegation of\u2014\n**(1)**\ndeception concerning the effects of fossil fuel on climate change;\n**(2)**\ndamage or injury resulting from the role of fossil fuel in contributing to climate change; or\n**(3)**\nthe failure to avoid damage or injury related to climate change, including claims for nuisance, trespass, design defect, negligence, failure to warn, or deceptive or unfair practices and claims for injunctive, declaratory, monetary, or other relief.\n##### (c) Rule of construction\nNothing in this Act or the amendments made by this Act shall\u2014\n**(1)**\nrequire the repayment of any funds made available from the Polluter Pays Climate Change Fund established under section 9512 of the Internal Revenue Code of 1986 and used pursuant to section 4(b) as a result of any award of damages imposed by a court of law relating to any causes of action or allegations described in subsection (b); or\n**(2)**\npermit the use of any such funds\u2014\n**(A)**\nas evidence in such an action or allegation; or\n**(B)**\nto offset any award of damages in such an action or allegation.\n#### 6. Non-preemption of authorities\nNothing in this Act or the amendments made by this Act shall be construed to preempt or supersede any State or local law, regulation, policy, or program, including laws, regulations, polices, and programs that\u2014\n**(1)**\nlimit, set, or enforce standards for greenhouse gas emissions;\n**(2)**\nmonitor, report, and keep records of greenhouse gas emissions;\n**(3)**\nprovide cost recovery for climate adaptation, mitigation, or resilience; or\n**(4)**\nconduct or support investigations.",
      "versionDate": "2025-01-07",
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
        "actionDate": "2025-02-07",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Transportation and Infrastructure, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1135",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Polluters Pay Climate Fund Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-03-04T18:39:08Z"
          },
          {
            "name": "Air quality",
            "updateDate": "2025-03-03T18:28:10Z"
          },
          {
            "name": "Climate change and greenhouse gases",
            "updateDate": "2025-03-03T18:28:04Z"
          },
          {
            "name": "Department of the Treasury",
            "updateDate": "2025-03-04T18:39:41Z"
          },
          {
            "name": "Environmental health",
            "updateDate": "2025-03-04T18:39:24Z"
          },
          {
            "name": "Environmental regulatory procedures",
            "updateDate": "2025-03-04T18:39:31Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-03-03T18:28:46Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-03-03T18:28:25Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-03-03T18:28:17Z"
          },
          {
            "name": "Pollution liability",
            "updateDate": "2025-03-03T18:28:34Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-03T18:29:04Z"
          },
          {
            "name": "Tax administration and collection, taxpayers",
            "updateDate": "2025-03-03T18:28:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-15T13:29:00Z"
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
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s25is.xml"
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
      "title": "Polluters Pay Climate Fund Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Polluters Pay Climate Fund Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to impose an assessment related to fossil fuel emissions, to establish the Polluter Pay Climate Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:29Z"
    }
  ]
}
```
