# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1428?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1428
- Title: Poverty Line Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1428
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-04-10T08:05:36Z
- Update date including text: 2026-04-10T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1428",
    "number": "1428",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Poverty Line Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T08:05:36Z",
    "updateDateIncludingText": "2026-04-10T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-18T18:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "DC"
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
      "sponsorshipDate": "2025-02-18",
      "state": "IL"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "RI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "MI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NJ"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "PA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "IL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "PA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "DE"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "NY"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "WA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1428ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1428\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Mullin (for himself, Ms. Norton , Ms. Schakowsky , Mr. Magaziner , Ms. Tlaib , Mrs. Watson Coleman , Mr. Gomez , Mr. Fitzpatrick , Mrs. Ramirez , Ms. Lee of Pennsylvania , and Ms. McBride ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Community Services Block Grant Act to update the Federal poverty line, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Poverty Line Act of 2025 .\n#### 2. Statement of purpose\nThe purpose of this Act is to update the calculation of the Federal poverty line, updated periodically in the Federal Register under the authority of section 673 of the Community Services Block Grant Act ( 42 U.S.C. 9902(2) ), to expand eligibility for and utilization of Federal assistance and benefits such that it incorporates more accurate costs of basic needs, keeps pace with changing household spending norms, accounts for regional variations in the cost of living, and reflects the minimum expenditures required by a household to have the opportunity to achieve social and economic mobility.\n#### 3. Amendment to definition of poverty line\nSection 673(2) of the Community Services Block Grant Act ( 42 U.S.C. 9902(2) ) is amended to read as follows:\n(2) Poverty line (A) In general The term poverty line means the official poverty line defined by the Office of Management and Budget according to the Secretary\u2019s published poverty line under subparagraph (B). (B) Revision and publication In coordination with the Bureau of the Census, the Secretary shall revise and publish the poverty line in the manner described in subparagraph (C) at least annually (or at any shorter interval the Secretary determines to be feasible and desirable). (C) Revision (i) The poverty line as revised shall be calculated at household sizes from 1 to 8 members and shall be the sum of\u2014 (I) a 5-year rolling average of household expenditures for food, clothing, telephone, and internet, calculated at 83 percent of the averages of the 47th through the 53rd percentiles of spending in the Consumer Expenditure Survey of the Bureau of Labor Statistics, adjusted for inflation as measured by the Consumer Price Index for All Urban Consumers (CPI\u2013U), and multiplied by the other basic goods factor set under clause (iv); (II) the cost of a rental housing unit with the number of bedrooms appropriate for the household size as determined by the Secretary of Housing and Urban Development under Fair Market Rents estimate determined by such Secretary as required under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ), and multiplied by the other basic goods factor set under clause (iv); (III) for up to 6 household members who are under 5 years, the cost of average child care prices for such children as determined by National Database of Childcare Prices of the Department of Labor; (IV) for up to 6 household members enrolled in employer-sponsored health care plans, the median non-premium out-of-pocket costs for such members as determined by the Secretary based on the Household Component of the Medical Expenditure Panel Survey to the extent practicable; (V) for up to 6 household members who are not otherwise enrolled in an employer-sponsored health care plan or are eligible for Medicare, the sum of the premium of an Essential Health Benefits Benchmark Plan defined by the Secretary as required under title I of the Patient Protection and Affordable Care Act and, to the extent practicable, the median non-premium out-of-pocket costs for those enrolled in such a plan as determined by the Secretary based on the Household Component of the Medical Expenditure Panel Survey; and (VI) for up to 6 household members who are eligible for Medicare, the sum of the cost of the premium for the lowest cost Medicare Advantage plan available that provides prescription drug coverage and, to the extent practicable, the median non-premium out-of-pocket costs for those enrolled in such a plan as determined by the Secretary based on the Household Component of the Medical Expenditure Panel Survey. (ii) The Secretary shall calculate the average incremental cost of each additional household member for households with more than 8 members. (iii) For each factor determined under clauses (i) and (ii), the Secretary shall\u2014 (I) use State-level data, any available county-level data, and, for clauses (i)(V) and (VI), geographic rating area data, and (II) subject to clause (viii), produce poverty line variants for each such geographic area. (iv) The Secretary shall set the other basic goods factor at the county level at a number that reflects spending on goods and services on which a household relies for basic needs, including transportation (where appropriate), and is otherwise not reflected in such clause but at not less than at 1.2. (v) The Secretary may issue rules that require the use of data sources in lieu of the data sources specified in clause (i) for determining any factor applicable under this subparagraph if the Secretary determines that such specified sources do not accurately reflect changes in otherwise applicable average household expenditures due to a significant economic event (such as a national emergency or above-average price inflation) or a substantial change in the underlying methodology or availability of such sources. (vi) The Secretary shall apply appropriate multipliers to each factor determined under in clause (i) to reflect economies or diseconomies of scale with additional household members. (vii) The Director may create simplified poverty line variants or per-person cost calculations for administrative purposes in determining household program eligibility as long as such variants or calculations materially incorporate all applicable costs specified under this subparagraph. (viii) The Director shall provide a lookup tool on the website of the Department of Health and Human Services for use by States, counties, and the public to determine the poverty line of a given household based on the factors in this paragraph. (D) Block grant program usage (i) If a State determines that it serves the objectives of the block grant program established under this subtitle, the State may revise the poverty line to not to exceed 125 percent of the official poverty line otherwise applicable under this paragraph. (ii) The poverty line shall be used as a criterion of eligibility in the community services block grant program established under this subtitle. (E) Safe harbors (i) The poverty line applicable to a participant or household in a Federal program on the date the participant moves from one geographic location to another shall not be reduced by reason of the move for the 2-year period beginning on the date of the move. (ii) The Secretary shall not set the poverty line for any State or county below the poverty line as determined under this paragraph prior to the date of enactment of the Poverty Line Act of 2025 and adjusted for inflation up to the present time. .\n#### 4. Transition\nNot later than 1 year after the effective date of this Act, the Director of Office of Management and Budget shall submit to Congress a report that specifies the Federal laws and regulations that apply the Federal poverty line in effect under section 673(2) of the Community Services Block Grant Act ( 42 U.S.C. 9902(2) ) as a factor in determining eligibility for Federal programs and that the Director recommends be updated to reflect the changes required by the amendment made by this Act.\n#### 5. Evaluation and Report\nIn the 4th year after the effective date of this Act, and at least once every 4 years thereafter, the Secretary of Health and Human Services shall\u2014\n**(1)**\nevaluate the efficacy of the poverty line as determined under section 673(2) of the Community Services Block Grant Act ( 42 U.S.C. 9902(2) ), as amended by this Act,\n**(2)**\npublish a report on the results of the evaluation, and\n**(3)**\npropose any change to such poverty line that would better achieve the purpose of this Act.\n#### 6. Rule of construction\nNothing in this Act shall be construed to preclude the Bureau of the Census or any other Federal agency from collecting, calculating, or publishing other measures of poverty for other purposes.\n#### 7. Effective date\nThis Act and the amendment made by this Act shall take effect 3 years after the date of the enactment of this Act.",
      "versionDate": "2025-02-18",
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
            "name": "Congressional oversight",
            "updateDate": "2025-07-09T14:04:12Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-09T14:03:50Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-07-09T14:03:42Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-07-09T14:04:07Z"
          },
          {
            "name": "Poverty and welfare assistance",
            "updateDate": "2025-07-09T14:03:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-03-18T13:40:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119hr1428",
          "measure-number": "1428",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-04-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1428v00",
            "update-date": "2025-04-25"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Poverty Line Act of 2025</strong></p><p>This bill revises the methodology used to calculate the federal poverty guidelines. The federal poverty guidelines are used to determine eligibility for many federal and state public assistance programs, including the Supplemental Nutrition Assistance Program (SNAP), the Children\u2019s Health Insurance Program (CHIP), and the National School Lunch Program. The poverty guidelines are currently calculated by adjusting the Census Bureau\u2019s poverty thresholds to account for changes in the Consumer Price Index.</p><p>The bill requires the Department of Health and Human Services (HHS) to calculate regional poverty guidelines based on a combination of factors including average household expenditures on food, clothing, utilities, and transportation; the average cost of rental housing; and the average cost of health insurance. These factors must be calculated using regional data as applicable. HHS must make available to the public a tool for determining the poverty guideline applicable to a given household.\u00a0</p><p>The new regional poverty guidelines established by HHS may not be lower than existing, corresponding poverty guidelines as of the date of enactment of the bill. HHS must review and evaluate the poverty guidelines at least every four years and propose changes to this methodology as appropriate.\u00a0</p><p>The bill takes effect three years after its enactment.</p>"
        },
        "title": "Poverty Line Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1428.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Poverty Line Act of 2025</strong></p><p>This bill revises the methodology used to calculate the federal poverty guidelines. The federal poverty guidelines are used to determine eligibility for many federal and state public assistance programs, including the Supplemental Nutrition Assistance Program (SNAP), the Children\u2019s Health Insurance Program (CHIP), and the National School Lunch Program. The poverty guidelines are currently calculated by adjusting the Census Bureau\u2019s poverty thresholds to account for changes in the Consumer Price Index.</p><p>The bill requires the Department of Health and Human Services (HHS) to calculate regional poverty guidelines based on a combination of factors including average household expenditures on food, clothing, utilities, and transportation; the average cost of rental housing; and the average cost of health insurance. These factors must be calculated using regional data as applicable. HHS must make available to the public a tool for determining the poverty guideline applicable to a given household.\u00a0</p><p>The new regional poverty guidelines established by HHS may not be lower than existing, corresponding poverty guidelines as of the date of enactment of the bill. HHS must review and evaluate the poverty guidelines at least every four years and propose changes to this methodology as appropriate.\u00a0</p><p>The bill takes effect three years after its enactment.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hr1428"
    },
    "title": "Poverty Line Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Poverty Line Act of 2025</strong></p><p>This bill revises the methodology used to calculate the federal poverty guidelines. The federal poverty guidelines are used to determine eligibility for many federal and state public assistance programs, including the Supplemental Nutrition Assistance Program (SNAP), the Children\u2019s Health Insurance Program (CHIP), and the National School Lunch Program. The poverty guidelines are currently calculated by adjusting the Census Bureau\u2019s poverty thresholds to account for changes in the Consumer Price Index.</p><p>The bill requires the Department of Health and Human Services (HHS) to calculate regional poverty guidelines based on a combination of factors including average household expenditures on food, clothing, utilities, and transportation; the average cost of rental housing; and the average cost of health insurance. These factors must be calculated using regional data as applicable. HHS must make available to the public a tool for determining the poverty guideline applicable to a given household.\u00a0</p><p>The new regional poverty guidelines established by HHS may not be lower than existing, corresponding poverty guidelines as of the date of enactment of the bill. HHS must review and evaluate the poverty guidelines at least every four years and propose changes to this methodology as appropriate.\u00a0</p><p>The bill takes effect three years after its enactment.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hr1428"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1428ih.xml"
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
      "title": "Poverty Line Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Poverty Line Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Community Services Block Grant Act to update the Federal poverty line, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:38Z"
    }
  ]
}
```
