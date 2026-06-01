# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4148?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4148
- Title: Homegrown Fertilizer Act
- Congress: 119
- Bill type: S
- Bill number: 4148
- Origin chamber: Senate
- Introduced date: 2026-03-19
- Update date: 2026-05-13T11:03:32Z
- Update date including text: 2026-05-13T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in Senate
- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-19: Introduced in Senate

## Actions

- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4148",
    "number": "4148",
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
    "title": "Homegrown Fertilizer Act",
    "type": "S",
    "updateDate": "2026-05-13T11:03:32Z",
    "updateDateIncludingText": "2026-05-13T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
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
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T19:29:16Z",
          "name": "Referred To"
        }
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
      "sponsorshipDate": "2026-03-19",
      "state": "KS"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NC"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4148is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4148\nIN THE SENATE OF THE UNITED STATES\nMarch 19, 2026 Ms. Klobuchar (for herself and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo direct the Secretary of Agriculture to provide grants and direct or guaranteed loans to increase domestic fertilizer production for United States farmers.\n#### 1. Short title\nThis Act may be cited as the Homegrown Fertilizer Act .\n#### 2. Fertilizer for American farmers\n##### (a) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means an entity eligible for a grant or loan under this section in accordance with subsection (c).\n**(2) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Under Secretary for Rural Development.\n**(3) State**\nThe term State means\u2014\n**(A)**\nthe 50 States; and\n**(B)**\nthe District of Columbia.\n**(4) United States**\nThe term United States means\u2014\n**(A)**\nthe States;\n**(B)**\nthe territories of the United States; and\n**(C)**\nthe territory of Indian Tribes.\n##### (b) Grants and loans\nThe Secretary shall provide grants and direct or guaranteed loans to assist eligible entities in increasing or expanding the manufacturing, processing, and storage of fertilizer and nutrient alternatives in the United States.\n##### (c) Eligible entities\n**(1) In general**\nTo be eligible for a grant or loan under this section, an entity shall be\u2014\n**(A)**\nan independently owned and operated\u2014\n**(i)**\nfor-profit business or corporation;\n**(ii)**\nnonprofit organization;\n**(iii)**\nproducer-owned cooperative or corporation; or\n**(iv)**\ncertified benefit corporation;\n**(B)**\nan Indian Tribe or Tribal organization; or\n**(C)**\na State or local government.\n**(2) Requirements**\nTo be eligible for a grant or loan under this section, an entity described in paragraph (1) shall\u2014\n**(A)**\nbe physically located within the United States;\n**(B)**\ncomply with all Federal, State, Tribal, and local regulations governing fertilizer and nutrient manufacturing, processing, storage, distribution, and waste management; and\n**(C)**\ncertify to the Secretary that the entity does not hold a market share (in manufacturing, processing, or distribution) greater than or equal to the entity that holds the fourth-largest share of that market for nitrogen, phosphate, potash, or any combination of thereof.\n##### (d) Priorities\nIn awarding grants and loans under this section, the Secretary shall give priority to eligible entities that will use the grant or loan for a proposal for a project\u2014\n**(1)**\nthat will improve on fertilizer production methods and efficient use technologies to promote innovation in fertilizers, nutrient alternatives, and biostimulants;\n**(2)**\nthe additional fertilizer or nutrient alternative manufacturing, processing, or storage capacity created by which will be dedicated to United States agricultural commodity production; or\n**(3)**\nthat demonstrates the project will improve competition, increase options, and reduce prices or volatility of fertilizer products or nutrient alternatives important for farmers.\n##### (e) Eligible activities\nAn eligible entity that receives a grant or loan under this section may use the grant or loan for\u2014\n**(1)**\nbuilding a new facility, buying an existing facility, or purchasing land for a facility;\n**(2)**\ncovering predevelopment costs, such as engineering and other professional fees;\n**(3)**\nproviding working capital to expand capacity or increase outputs;\n**(4)**\nmodernizing or expanding an existing facility, including making updates to existing buildings or constructing new buildings on site;\n**(5)**\npurchasing or modernizing processing and manufacturing equipment;\n**(6)**\ndeveloping, customizing, and installing equipment, devices, and technology to improve processing functions, worker conditions, or safety;\n**(7)**\ninstalling or updating equipment that reduces emissions, increases fertilizer use efficiency, or improves air and water quality;\n**(8)**\nensuring legal compliance with packaging and labeling requirements, such as sealing, boxing, labeling, and conveying;\n**(9)**\nconfirming legal compliance with occupational and safety regulations;\n**(10)**\nengaging in workforce recruitment, training, apprenticeships, and retention to ensure expansion projects are adequately staffed;\n**(11)**\nincreasing domestic storage of fertilizer or nutrient alternatives; and\n**(12)**\nsuch other activities as the Secretary determines to be appropriate.\n##### (f) Grant amount\n**(1) In general**\nThe amount of a grant under this section shall not exceed $100,000,000.\n**(2) Matching funds**\nAn eligible entity that receives a grant under this section shall provide non-Federal matching funds in an amount that is equal to the amount of the grant.\n##### (g) Loan terms and conditions\nExcept as otherwise provided in this section, the terms and conditions of a loan under this section shall be the same as the terms and conditions of a business and industry direct or guaranteed loan under section 310B(g) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1932(g) ).\n##### (h) Duration\n**(1) In general**\nThe Secretary may provide a grant or loan under this section for a project that is not longer than 5 years.\n**(2) Extension**\nThe Secretary may extend the period described in paragraph (1) if the Secretary determines an extension is appropriate.\n##### (i) Combination and nonsupplantation of other funds\n**(1) In general**\nThe Secretary shall use the amounts made available to carry out this section to supplement, and not supplant, funds provided under other Federal, State, or local laws.\n**(2) Coordination**\nThe Secretary shall coordinate with other Federal agencies, such as the Department of Energy, and State, regional, or local agencies to allow applicants under this section to package proposals to be considered under relevant authorities jointly.\n##### (j) Condition\nAs a condition on receipt of a grant or loan under this section, the grant or loan recipient shall repay the grant or loan in full if any company or facility developed through the project using the grant or loan, or most or all of the assets of such company or facility, is sold, is transferred, or otherwise changes ownership, during the 10-year period beginning on the completion of the project, to an entity that holds a market share (in manufacturing, processing, or distribution) greater than or equal to the entity that holds the fourth-largest share of that market for nitrogen, phosphate, potash, or any combination of thereof.\n##### (k) Funding\nIn addition to other available funds, the Secretary may use the authority under section 5 of the Commodity Credit Corporation Charter Act ( 15 U.S.C. 714c ) to transfer such sums of the funds of the Commodity Credit Corporation from available borrowing authority as the Secretary determines to be appropriate to carry out this section.",
      "versionDate": "2026-03-19",
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
        "actionDate": "2026-04-22",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "8457",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Homegrown Fertilizer Act",
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
        "updateDate": "2026-03-30T16:16:27Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4148is.xml"
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
      "title": "Homegrown Fertilizer Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Homegrown Fertilizer Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-27T02:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Agriculture to provide grants and direct or guaranteed loans to increase domestic fertilizer production for United States farmers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-27T02:48:22Z"
    }
  ]
}
```
