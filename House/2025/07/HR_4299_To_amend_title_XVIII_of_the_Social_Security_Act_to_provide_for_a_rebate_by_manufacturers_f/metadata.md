# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4299?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4299
- Title: Protecting Patient Access to Cancer and Complex Therapies Act
- Congress: 119
- Bill type: HR
- Bill number: 4299
- Origin chamber: House
- Introduced date: 2025-07-07
- Update date: 2026-05-22T08:07:49Z
- Update date including text: 2026-05-30T16:27:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-07: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-07 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-07: Introduced in House

## Actions

- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-07 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-07",
    "latestAction": {
      "actionDate": "2025-07-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4299",
    "number": "4299",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Protecting Patient Access to Cancer and Complex Therapies Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:49Z",
    "updateDateIncludingText": "2026-05-30T16:27:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-07",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-07",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-07",
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
          "date": "2025-07-07T14:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-07T14:00:50Z",
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
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-07-07",
      "state": "CA"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-07-07",
      "state": "FL"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "GA"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "PA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "WV"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "MD"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "NJ"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "OH"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "IA"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "TN"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "OH"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "UT"
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
      "sponsorshipDate": "2025-12-16",
      "state": "PA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "PA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NC"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "UT"
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
      "sponsorshipDate": "2026-02-02",
      "state": "NY"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "TX"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "CA"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "FL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "NY"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "TX"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "OH"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "NC"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4299ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4299\nIN THE HOUSE OF REPRESENTATIVES\nJuly 7, 2025 Mr. Murphy (for himself, Mr. Gray , and Mr. Dunn of Florida ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide for a rebate by manufacturers for selected drugs and biological products subject to maximum fair price negotiation.\n#### 1. Short title\nThis Act may be cited as the Protecting Patient Access to Cancer and Complex Therapies Act .\n#### 2. Rebate by manufacturers for selected drugs and biological products subject to maximum fair price negotiation\n##### (a) Maintaining payments under part B based on ASP+6\nSection 1847A(b)(1)(B) of the Social Security Act (42 U.S.C. 1395w\u20133a(b)(1)(B)) is amended by striking or in the case of such a drug or biological product that is a selected drug and all that follows through the semicolon and inserting a semicolon.\n##### (b) Rebate by manufacturers for selected drugs and biological products subject to maximum fair price negotiation\n**(1) In general**\nSection 1847A of the Social Security Act ( 42 U.S.C. 1395w\u20133a ) is amended\u2014\n**(A)**\nby redesignating subsection (j) as subsection (k); and\n**(B)**\nby inserting after subsection (i) the following new subsection:\n(j) Rebate by manufacturers for selected drugs and biological products subject to maximum fair price negotiation (1) Requirements (A) Secretarial provision of information Not later than 6 months after the end of each calendar quarter beginning on or after the first day of the initial price applicability period (as defined in section 1191(b)(2)), the Secretary shall, for each selected drug (as defined in section 1192(c)) of each manufacturer with an agreement under section 1193 for which a maximum fair price is in effect and for which payment may be made under this part, report to each manufacturer of such selected drug the following for such calendar quarter during such price applicability period: (i) Information on the total number of units of the billing and payment code for such selected drug furnished under this part during such calendar quarter. (ii) Information on the sum of\u2014 (I) the amount (if any) by which\u2014 (aa) the ASP+6 payment amount (as defined in paragraph (5)) for such drug and calendar quarter, less the ASP+6 coinsurance amount for such drug and calendar quarter; exceeds (bb) the MFP+6 payment amount (as so defined) for such drug and calendar quarter, less the MFP+6 coinsurance amount for such drug and calendar quarter; and (II) the amount (if any) by which\u2014 (aa) the ASP+6 coinsurance amount (as defined in paragraph (5)) for such drug and calendar quarter; exceeds (bb) the MFP+6 coinsurance amount (as so defined) for such drug and calendar quarter. (iii) The rebate amount specified under subparagraph (B) for such drug and calendar quarter. (B) Manufacturer requirement For each calendar quarter beginning on or after the first day of the initial price applicability period (as defined in section 1191(b)(2)), the manufacturer of a selected drug shall, for such drug, not later than 30 days after the date of receipt from the Secretary of the information described in subparagraph (A) for such calendar quarter, provide to the Secretary a rebate that is equal to the amount specified in subparagraph (A)(ii) multiplied by the number of units specified in subparagraph (A)(i) for such drug for such calendar quarter. The rebate required under this subparagraph shall be in addition to any other rebates required under this title or title XIX, including the payments required under subsections (h) and (i). (2) Calculation of beneficiary coinsurance based on mfp+6 (A) In general Subject to subparagraph (B), in the case of a selected drug with respect to which a rebate is paid under this subsection\u2014 (i) the amount of any coinsurance applicable under this part to an individual to whom such drug is furnished during a calendar quarter shall be equal to the MFP+6 coinsurance amount; and (ii) the amount of such coinsurance for such calendar quarter shall be applied as a percent, as determined by the Secretary, to the payment amount that would otherwise apply under subsection (b)(1)(B). (B) Clarification regarding application of inflation rebate If a rebate is required under subsection (i) with respect to a selected drug for a calendar quarter, the lesser of the amount of coinsurance computed under subparagraph (A) or the coinsurance computed under subsection (i)(5) shall apply for such drug and calendar quarter. (3) Rebate deposits Amounts paid as rebates under paragraph (1)(B) shall be deposited into the Federal Supplementary Medical Insurance Trust Fund established under section 1841. (4) Civil money penalty The civil money penalty established under paragraph (7) of subsection (i) shall apply to the failure to comply with this subsection in the same manner as such penalty applies to failures to comply with the requirements under paragraph (1)(B) of subsection (i). (5) Definitions In this subsection, with respect to a selected drug for a calendar quarter during a price applicability period: (A) ASP+6 coinsurance amount The ASP+6 coinsurance amount is equal to 20 percent of the ASP+6 payment amount. (B) ASP+6 payment amount The ASP+6 payment amount is equal to 106 percent of the amount determined under paragraph (4) of subsection (b) for such drug during such calendar quarter. (C) MFP+6 coinsurance amount The MFP+6 coinsurance amount is equal to 20 percent of the MFP+6 payment amount. (D) MFP+6 payment amount The MFP+6 payment amount is equal to 106 percent of the maximum fair price (as defined in section 1191(c)(2)) applicable for such drug during such calendar quarter. (6) Clarification Nothing in part E of title XI or this subsection shall be construed to require a manufacturer to provide selected drugs at maximum fair prices other than through the rebate required under this subsection. .\n**(2) Amounts payable; cost-sharing**\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a)(1) ) is amended\u2014\n**(A)**\nin subparagraph (G), by striking subsection (i)(9) and inserting paragraphs (9) and (10) of subsection (i) ;\n**(B)**\nin subparagraph (S), by striking subparagraph (EE) and inserting subparagraphs (EE) and (II) ;\n**(C)**\nby striking and (HH) and inserting (HH) ; and\n**(D)**\nby inserting before the semicolon at the end the following: , and (II) with respect to a selected drug (as defined in section 1192(c)) that is subject to a rebate under section 1847A(j), the amounts paid shall be equal to the percent of the payment amount otherwise determined under section 1847A(b)(1)(B) that equals the difference between (i) 100 percent, and (ii) the percent applied under section 1847A(j)(2)(A)(ii) .\n**(3) ASC conforming amendments**\nSection 1833(i) of the Social Security Act ( 42 U.S.C. 1395l(i) ) is amended by adding at the end the following new paragraph:\n(11) In the case of a selected drug (as defined in section 1192(c)), subject to a rebate under section 1847A(j) for which payment under this subsection is not packaged into a payment for a service furnished on or after the initial price applicability year for the selected drug under the revised payment system under this subsection, in lieu of calculation of coinsurance and the amount of payment otherwise applicable under this subsection, the provisions of section 1847(j)(2) and paragraph (1)(II) of subsection (a), shall, as determined appropriate by the Secretary, apply under this subsection in the same manner as such provisions of section 1847A(j)(2) and subsection (a) apply under such section and subsection. .\n**(4) Opps conforming amendment**\nSection 1833(t)(8) of the Social Security Act ( 42 U.S.C. 1395l(t)(8) ) is amended by adding at the end the following new subparagraph:\n(G) Selected drugs subject to rebate In the case of a selected drug (as defined in section 1192(c)), subject to a rebate under section 1847A(j) for which payment under this subsection is not packaged into a payment for a covered OPD service (or group of services) furnished on or after the initial price applicability year for the selected drug, and the payment for such drug is the same as the amount for a calendar quarter under section 1847A(b)(1)(B), under the system under this subsection, in lieu of the calculation of the copayment amount and the amount otherwise applicable under this subsection (other than the application of the limitation described in subparagraph (C)), the provisions of section 1847A(j)(2) and paragraph (1)(II) of subsection (a), shall, as determined by the Secretary apply under this section in the same manner as such provisions of section 1847A(j)(2) and subsection (a) apply under such section and subsection. .\n**(5) Exclusion of selected drug mfp rebates from asp calculation**\nSection 1847A(c)(3) of the Social Security Act (42 U.S.C. 1395w\u20133a(c)(3)) is amended by striking subsection (i) and inserting subsection (i), subsection (j) .\n**(6) Coordination with medicaid rebate information disclosures**\nSection 1927(b)(3)(D)(i) of the Social Security Act ( 42 U.S.C. 1396r\u20138(b)(3)(D)(i) ) is amended by striking and the rebate and inserting and the rebates .\n**(7) Provision of rebates**\nSection 1193(a) of the Social Security Act ( 42 U.S.C. 1320f\u20132(a) ) is amended\u2014\n**(A)**\nin paragraph (1), by striking subparagraph (B) and inserting the following:\n(B) by paying rebates in accordance with section 1847A(j); ;\n**(B)**\nin paragraph (2), by striking subparagraph (B) and inserting the following:\n(B) by paying rebates in accordance with section 1847A(j); ; and\n**(C)**\nin paragraph (3), by striking subparagraph (B) and inserting the following:\n(B) by paying rebates in accordance with section 1847A(j); .\n##### (c) Conforming amendments\n**(1)**\nSection 1847A(i)(5) of the Social Security Act (42 U.S.C. 1395w\u20133a(i)(5)) is amended, in the matter preceding subparagraph (A)\u2014\n**(A)**\nby striking In the case and inserting Subsection to subsection (j)(2)(B), in the case ; and\n**(B)**\nby striking (or, in the case of a part B rebatable drug that is a selected drug (as defined in section 1192(c)), the payment amount described in subsection (b)(1)(B) for such drug) ; and\n**(2)**\nSection 1833(a)(1)(EE) of the Social Security Act ( 42 U.S.C. 1395l(a)(1)(EE) ) is amended\u2014\n**(A)**\nby striking (or, in the case of a part B rebatable drug that is a selected drug (as defined in section 1192(c) for which, the payment amount described in section 1847A(b)(1)(B)) for such drug for such quarter ; and\n**(B)**\nby striking or section 1847A(b)(1)(B), as applicable, .",
      "versionDate": "2025-07-07",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-11T17:12:56Z"
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
      "date": "2025-07-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4299ih.xml"
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
      "title": "Protecting Patient Access to Cancer and Complex Therapies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Patient Access to Cancer and Complex Therapies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-26T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide for a rebate by manufacturers for selected drugs and biological products subject to maximum fair price negotiation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-26T03:18:17Z"
    }
  ]
}
```
