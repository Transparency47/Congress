# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5830?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5830
- Title: Guaranteed Income Pilot Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5830
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2025-11-21T16:12:41Z
- Update date including text: 2025-11-21T16:12:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-10-24: Introduced in House

## Actions

- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5830",
    "number": "5830",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Guaranteed Income Pilot Program Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-21T16:12:41Z",
    "updateDateIncludingText": "2025-11-21T16:12:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NJ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "MI"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "IL"
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
      "sponsorshipDate": "2025-10-24",
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
      "sponsorshipDate": "2025-10-24",
      "state": "IL"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "GA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "MI"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-24",
      "state": "PA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5830ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5830\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Mrs. Watson Coleman (for herself, Mrs. McIver , Ms. Tlaib , Mr. Davis of Illinois , Ms. Norton , Ms. Schakowsky , Ms. Jacobs , Mr. Johnson of Georgia , Mr. Thanedar , Mr. Mullin , Ms. Lee of Pennsylvania , and Mr. Torres of New York ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo establish a pilot program providing certain individuals with a guaranteed monthly income, to study the effect of a guaranteed monthly income on such individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guaranteed Income Pilot Program Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nToo many Americans cannot achieve financial stability due to income volatility, the rising cost of living, wage stagnation, and a lack of affordable housing.\n**(2)**\nReal wages have failed to keep pace with inflation, meaning the purchasing power of American households has not changed in decades.\n**(3)**\nIncome volatility, defined as an annual income fluctuation of 25 percent or more, impacts millions of American households.\n**(4)**\nTwo-thirds of Americans are worried they wouldn\u2019t be able to cover their living expenses for just 1 month if they lose their primary source of income, while 57 percent of American adults are currently unable to cover a $1,000 emergency expense. That percentage is higher for millennials at 79 percent, and Generation Z at 85 percent, unable to cover an emergency expense.\n**(5)**\nFull-time minimum wage earners cannot afford an average 2-bedroom apartment anywhere in the United States.\n**(6)**\nThe changing nature of the economy, including the rise of the gig economy, unemployment risks posed by automation, and the fluctuating nature of waged labor, will result in increased income volatility and prohibit upward economic mobility.\n**(7)**\nDuring the height of COVID\u201319, the Federal Government provided stimulus checks to the American people in response to the economic hardship of the pandemic. The Census Bureau complied an analysis that showed that material hardship in United States households fell sharply following the passage of the COVID\u201319 relief bill in late December 2020, and the American Rescue Plan in March 2021. From December 2020 to April 2021, food insufficiently fell by over 40 percent, financial instability fell by 45 percent, and reported adverse mental health symptoms fell by 20 percent.\n#### 3. Guaranteed income pilot program\n##### (a) In general\nThe Secretary, in consultation with the Commissioner of Internal Revenue, shall establish and implement a 3-year pilot program (hereinafter referred to as the program ) to provide a guaranteed monthly income to certain eligible individuals in accordance with this section.\n##### (b) Income subsidy\n**(1) Selection of participating eligible individuals**\nThe Secretary, in consultation with the Commissioner and the external partner selected pursuant to subsection (d), shall develop selection criteria that the Secretary will use to select 20,000 total eligible individuals for participation in the program.\n**(2) Amount of income subsidy**\nOf the eligible individuals participating in the program, 10,000 shall receive a cash payment each month equal to the fair market rent for a 2-bedroom home in the ZIP Code in which the eligible individual resides, or a substantially similar amount as determined by the Secretary, in consultation with the Commissioner and the external partner.\n**(3) Monthly distribution of income subsidy**\nEach participating eligible individual shall receive the cash payment on the 15th day of each month.\n##### (c) Responsibilities of Commissioner of Internal Revenue\nThe Commissioner of Internal Revenue shall be responsible for\u2014\n**(1)**\nproviding the Secretary access to tax records to administer and study the program under this section; and\n**(2)**\nupdating the Secretary and the external partner on changes to the taxable income of a participating eligible individual.\n##### (d) External partner\n**(1) Selection**\nThe Secretary shall select an external partner to provide assistance with the design, administration, and evaluation of the program.\n**(2) Qualifications**\nAn organization selected to be the external partner shall have demonstrated experience in\u2014\n**(A)**\nmixed-methods experimental design; and\n**(B)**\nimplementing cash-transfer programs.\n**(3) Confidentiality**\nThe external partner, and any employee of the external partner, shall be treated as a Federal employee for purposes of section 6103 of the Internal Revenue Code of 1986.\n**(4) Data collection**\nThe external partner shall collect data from participating eligible individuals as necessary to complete the study and reports required under section 4, and to conduct any additional research as the Secretary determines necessary.\n##### (e) Disregard of cash payments for purposes of all Federal and Federally assisted programs\nNotwithstanding any other provision of law, any payment made to participating eligible individuals under this section shall not be taken into account as income, and shall not be taken into account as resources for a period of 12 months from receipt, for purposes of determining the eligibility of such eligible individual (or any other individual) for benefits or assistance (or the amount or extent of benefits or assistance) under any Federal program or any State or local program financed in whole or in part with Federal funds.\n#### 4. Study and report\n##### (a) Study on pilot program\nThe Secretary, in collaboration with the Commissioner and the external partner, shall conduct a study on outcomes of the program.\n##### (b) Interim report\nNot later than 24 months after participating eligible individuals have been begun participating in the program, the Secretary, in consultation with the Commissioner of Internal Revenue and the external partner, shall provide an interim report on the program under section 3 to the Congress.\n##### (c) Final report\nNot later than 12 months after the conclusion of the program under section 3, the Secretary, in consultation with the Commissioner of Internal Revenue and the external partner, shall provide a final report on the program to the Congress, including\u2014\n**(1)**\nan analysis of\u2014\n**(A)**\nthe effect of the monthly income subsidy provided in section 3 on\u2014\n**(i)**\nmicro-economic outcomes of participating eligible individuals;\n**(ii)**\nthe health of participating eligible individuals; and\n**(iii)**\nthe social costs of income volatility, including connections with income fluctuation and health, housing, education, employment, childcare, and other outcomes as determined appropriate by the Secretary; and\n**(B)**\nthe feasibility of expanding the program under section 3 to include a larger number of participants; and\n**(2)**\nthe results of interviews and focus groups conducted with consenting participants of the program.\n#### 5. Definitions\nIn this Act:\n**(1) Commissioner**\nThe term Commissioner means the Commissioner of the Internal Revenue Service.\n**(2) Eligible individual**\nThe term eligible individual means an individual taxpayer between the ages of 18\u201365.\n**(3) External partner**\nThe term external partner means a non-partisan research agency or a non-profit academic institution with expertise in social science experimentation.\n**(4) Fair market rent**\nThe term fair market rent means the applicable fair market rent established under section 8(c) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(c) ).\n**(5) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n#### 6. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $495,000,000 for each of the fiscal years 2026 through 2030.",
      "versionDate": "2025-10-24",
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
        "name": "Taxation",
        "updateDate": "2025-11-21T16:12:41Z"
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
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5830ih.xml"
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
      "title": "Guaranteed Income Pilot Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guaranteed Income Pilot Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a pilot program providing certain individuals with a guaranteed monthly income, to study the effect of a guaranteed monthly income on such individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T10:18:16Z"
    }
  ]
}
```
