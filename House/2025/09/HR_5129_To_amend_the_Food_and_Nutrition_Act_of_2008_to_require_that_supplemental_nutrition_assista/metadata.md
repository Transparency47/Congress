# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5129?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5129
- Title: Closing the Meal Gap Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5129
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2026-05-16T08:07:31Z
- Update date including text: 2026-05-16T08:07:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-12-05 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-12-05 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5129",
    "number": "5129",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "A000370",
        "district": "12",
        "firstName": "Alma",
        "fullName": "Rep. Adams, Alma S. [D-NC-12]",
        "lastName": "Adams",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Closing the Meal Gap Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:31Z",
    "updateDateIncludingText": "2026-05-16T08:07:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-05",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T13:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-05T19:46:10Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NY"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CT"
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
      "sponsorshipDate": "2025-09-04",
      "state": "PA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5129ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5129\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Ms. Adams (for herself, Ms. Vel\u00e1zquez , Mrs. Hayes , and Ms. Lee of Pennsylvania ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to require that supplemental nutrition assistance program benefits be calculated using the value of the low-cost food plan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Closing the Meal Gap Act of 2025 .\n#### 2. Calculation of program benefits using low-cost food plan\n##### (a) Definition of low-Cost food plan\nSection 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 ) is amended\u2014\n**(1)**\nby striking subsection (u);\n**(2)**\nby redesignating subsections (n) through (t) as subsections (o) through (u), respectively; and\n**(3)**\nby inserting after subsection (m) the following:\n(n) Low-Cost food plan (1) In general The term low-cost food plan means the diet, determined in accordance with the calculations of the Secretary, required to feed a 4-person family that consists of\u2014 (A) a man and a woman who are each between 19 and 50 years of age; (B) a child who is between 6 and 8 years of age; and (C) a child who is between 9 and 11 years of age. (2) Reevaluation By December 31, 2029, and at 5-year intervals thereafter, the Secretary shall reevaluate and publish the market baskets of the low-cost food plan, based on current food prices, food composition data, consumption patterns, and dietary guidance. (3) Cost For purposes of paragraph (1), the cost of the diet described in that paragraph shall be the basis for uniform allotments for all households regardless of the actual composition of the household, except that the Secretary shall\u2014 (A) make household-size adjustments (based on the unrounded cost of that diet) taking into account economies of scale; (B) make cost adjustments in the low-cost food plan for the State of Hawaii and the urban and rural parts of the State of Alaska to reflect the cost of food in Hawaii and urban and rural Alaska, respectively; and (C) on October 1, 2023, and each October 1 thereafter, adjust the cost of the diet to reflect the cost of the diet in the immediately preceding June, and round the result to the nearest lower-dollar increment for each household size. .\n##### (b) Value of allotment\nSection 8(a) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2017(a) ) is amended\u2014\n**(1)**\nby striking thrifty food plan each place it appears and inserting low-cost food plan ; and\n**(2)**\nin the proviso, by striking 8 percent and inserting 10 percent .\n##### (c) Quality control system\nSection 16(c)(1)(A)(ii) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2025(c)(1)(A)(ii) ) is amended\u2014\n**(1)**\nin subclause (II)\u2014\n**(A)**\nby striking thrifty food plan is adjusted under section 3(u)(4) and inserting low-cost food plan is adjusted under section 3(n)(3)(D) ; and\n**(B)**\nby striking 2013 and inserting 2023 ;\n**(2)**\nby redesignating subclause (II) as subclause (III); and\n**(3)**\nby striking subclause (I) and inserting the following:\n(I) for fiscal year 2023, at an amount not greater than $50; (II) for fiscal year 2024, the amount specified in subclause (I) adjusted by the difference between the thrifty food plan (as defined in section 3 (as in effect on the day before the date of enactment of the Closing the Meal Gap Act of 2025 )) and the low-cost food plan; and .\n##### (d) Conforming amendments\n**(1)**\nSection 10 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2019 ) is amended, in the first sentence, by striking 3(o)(4) and inserting 3(p)(4) .\n**(2)**\nSection 11 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2020 ) is amended\u2014\n**(A)**\nin subsection (a)(2), by striking 3(s)(1) and inserting 3(t)(1) ;\n**(B)**\nin subsection (d)\u2014\n**(i)**\nby striking 3(s)(1) each place it appears and inserting 3(t)(1) ;\n**(ii)**\nby striking 3(s)(2) each place it appears and inserting 3(t)(2) ; and\n**(iii)**\nby striking Act ( 25 U.S.C. 450 ) and inserting and Education Assistance Act ( 25 U.S.C. 3501 et seq. ) ; and\n**(C)**\nin subsection (e)(17), by striking 3(s)(1) and inserting 3(t)(1) .\n**(3)**\nSection 19(a)(2)(A)(ii) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2028(a)(2)(A)(ii) ) is amended by striking thrifty food plan has been adjusted under section 3(u)(4) and inserting low-cost food plan has been adjusted under section 3(n)(3)(D) .\n**(4)**\nSection 27(a)(2) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2036(a)(2) ) is amended\u2014\n**(A)**\nin subparagraph (C), by inserting (as in effect on the day before the date of enactment of the Closing the Meal Gap Act of 2025 ) after section 3(u)(4) ;\n**(B)**\nin subparagraph (D)(ix), by striking and at the end;\n**(C)**\nby redesignating subparagraph (E) as subparagraph (F);\n**(D)**\nby inserting after subparagraph (D) the following:\n(E) for fiscal year 2023, the sum obtained by adding\u2014 (i) the dollar amount of commodities specified in subparagraph (B) adjusted by the percentage by which the low-cost food plan has been adjusted under section 3(u)(4) between June 30, 2021, and June 30 of the immediately preceding fiscal year; and (ii) $35,000,000; and ; and\n**(E)**\nin subparagraph (F) (as so redesignated), by striking subparagraph (D)(ix) adjusted by the percentage by which the thrifty food plan has been adjusted under section 3(u)(4) and inserting subparagraph (F) adjusted by the percentage by which the low-cost food plan has been adjusted under section 3(n)(3)(D) .\n**(5)**\nSection 408(a)(12)(B)(i) of the Social Security Act ( 42 U.S.C. 608(a)(12)(B)(i) ) is amended by striking (r) each place it appears.\n#### 3. Deductions from income\n##### (a) Standard medical expense deduction\nSection 5(e)(5) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014(e)(5) ) is amended\u2014\n**(1)**\nin the paragraph heading, by striking Excess medical and inserting Medical ;\n**(2)**\nin subparagraph (A), by striking an excess medical and all that follows through the period at the end and inserting a standard medical deduction or a medical expense deduction of actual costs for the allowable medical expenses incurred by the elderly or disabled member, exclusive of special diets. ;\n**(3)**\nin subparagraph (B)(i), by striking excess ; and\n**(4)**\nby adding at the end the following:\n(D) Standard medical expense deduction amount (i) In general Except as provided in clause (ii), the standard medical expense deduction shall be\u2014 (I) for fiscal year 2023, $140; and (II) for each subsequent fiscal year, equal to the applicable amount for the immediately preceding fiscal year as adjusted to reflect changes for the 12-month period ending the preceding June 30 in the Consumer Price Index for All Urban Consumers: Medical Care published by the Bureau of Labor Statistics of the Department of Labor. (ii) Exception For any fiscal year, a State agency may establish a greater standard medical expense deduction than described in clause (i) if the greater deduction satisfies cost neutrality standards established by the Secretary for that fiscal year. .\n##### (b) Elimination of cap of excess shelter expenses\n**(1) In general**\nSection 5(e)(6) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014(e)(6) ) is amended\u2014\n**(A)**\nby striking subparagraph (B); and\n**(B)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (B) and (C), respectively.\n**(2) Conforming amendment**\nSection 2605(f)(2)(A) of the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8624(f)(2)(A) ) is amended by striking 5(e)(6)(C)(iv)(I) of that Act ( 7 U.S.C. 2014(e)(6)(C)(iv)(I) ) and inserting 5(e)(6)(B)(iv)(I) of that Act ( 7 U.S.C. 2014(e)(6)(B)(iv)(I) ) .\n#### 4. Elimination of time limit\n##### (a) In general\nSection 6 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015 ) is amended\u2014\n**(1)**\nby striking subsection (o); and\n**(2)**\nby redesignating subsections (p) through (s) as subsections (o) through (r), respectively.\n##### (b) Conforming amendments\n**(1)**\nSection 5(a) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014(a) ) is amended, in the second sentence, by striking (r) and inserting (q) .\n**(2)**\nSection 6(d)(4) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(d)(4) ) is amended\u2014\n**(A)**\nin subparagraph (B)(ii)(I)(bb)(DD), by striking or subsection (o) ; and\n**(B)**\nin subparagraph (N), by striking or subsection (o) each place it appears.\n**(3)**\nSection 7(i)(1) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2016(i)(1) ) is amended by striking section 6(o)(2) of this Act or .\n**(4)**\nSection 16(h) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2025(h) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (B), in the matter preceding clause (i), by striking that\u2014 and all that follows through the period at the end of clause (ii) and inserting that is determined and adjusted by the Secretary. ;\n**(ii)**\nby striking subparagraph (E);\n**(iii)**\nby redesignating subparagraph (F) as subparagraph (E); and\n**(iv)**\nin clause (ii)(III)(ee)(AA) of subparagraph (E) (as so redesignated), by striking , individuals subject to the requirements under section 6(o), ; and\n**(B)**\nin paragraph (5)(C)\u2014\n**(i)**\nin clause (ii), by adding and at the end;\n**(ii)**\nin clause (iii), by striking ; and and inserting a period; and\n**(iii)**\nby striking clause (iv).\n**(5)**\nSection 51(d)(8)(A)(ii) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin subclause (I), by striking , or at the end and inserting a period;\n**(B)**\nin the matter preceding subclause (I), by striking family\u2014 and all that follows through receiving in subclause (I) and inserting family receiving ; and\n**(C)**\nby striking subclause (II).\n**(6)**\nSection 103(a)(2) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3113 ) is amended\u2014\n**(A)**\nby striking subparagraph (D); and\n**(B)**\nby redesignating subparagraphs (E) through (K) as subparagraphs (D) through (J), respectively.\n**(7)**\nSection 121(b)(2)(B) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3151 ) is amended\u2014\n**(A)**\nby striking clause (iv); and\n**(B)**\nby redesignating clauses (v) through (vii) as clauses (iv) through (vi), respectively.",
      "versionDate": "2025-09-04",
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
        "actionDate": "2025-09-11",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "2792",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Closing the Meal Gap Act of 2025",
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
        "updateDate": "2025-09-11T15:39:06Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5129ih.xml"
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
      "title": "Closing the Meal Gap Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Closing the Meal Gap Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to require that supplemental nutrition assistance program benefits be calculated using the value of the low-cost food plan, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:36Z"
    }
  ]
}
```
