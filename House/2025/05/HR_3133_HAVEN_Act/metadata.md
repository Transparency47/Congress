# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3133?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3133
- Title: HAVEN Act
- Congress: 119
- Bill type: HR
- Bill number: 3133
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2025-10-04T08:05:38Z
- Update date including text: 2025-10-04T08:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3133",
    "number": "3133",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "A000381",
        "district": "3",
        "firstName": "Yassamin",
        "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
        "lastName": "Ansari",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "HAVEN Act",
    "type": "HR",
    "updateDate": "2025-10-04T08:05:38Z",
    "updateDateIncludingText": "2025-10-04T08:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-01T13:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "LA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "IL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "CA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NJ"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "MN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "MI"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3133ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3133\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Ms. Ansari (for herself, Mr. Casar , Mr. Fields , Mr. Jackson of Illinois , Mr. Lieu , Mrs. McIver , Ms. Omar , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend certain Acts related to housing to adjust rental payments with respect to certain Federal rental assistance programs, to ban source of income discrimination in housing, to reform and expand the housing choice voucher program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Accessibility and Voucher Expansion Now Act or the HAVEN Act .\n#### 2. Adjustments to rental payments with respect to certain Federal rental assistance programs\n##### (a) In general\n**(1) United States Housing Act of 1937**\nThe United States Housing Act of 1937 (42 U.S.C. 1437 et. seq.) is amended\u2014\n**(A)**\nin section 3(a)(1)(A), by striking 30 and inserting 20 ;\n**(B)**\nin section 8(o)(2)(A)(i), by striking 30 and inserting 20 ; and\n**(C)**\nin section 9(e)(2)(A)\u2014\n**(i)**\nin clause (vi), by striking and at the end;\n**(ii)**\nby redesignating clause (vii) as clause (viii) and by moving such clause 1 em to the right; and\n**(iii)**\nby inserting after clause (vi) the following:\n(vii) the amount of public housing rental income forgone by the public housing agency as a result of lowering the percentage of monthly adjusted income for the calculation of rental payments; and .\n**(2) Housing Act of 1949**\nSection 521(a)(3) of the Housing Act of 1949 ( 42 U.S.C. 1490a(a)(3) ) is amended by striking 30 in each place it occurs and inserting 20 .\n**(3) Housing Act of 1959**\nSection 202(c)(3) of the Housing Act of 1959 ( 12 U.S.C. 1701q(c)(3) ) is amended by striking 30 and inserting 20 .\n**(4) Cranston-Gonzalez National Affordable Housing Act**\nSection 811(d)(3) of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013(d)(3) ) is amended by striking 30 and inserting 20 .\n##### (b) Effect on recipients of assistance\nTo the extent practicable, the Secretary of Housing and Urban Development shall ensure that the adjustments made by subsection (a) do not reduce the number of recipients of the Federal rental assistance programs described in subsection (a).\n#### 3. Authorization of appropriations with respect to certain Federal rental assistance programs\n##### (a) United States Housing Act of 1937\nThe United States Housing Act of 1937 (42 U.S.C. 1437 et. seq.) is amended\u2014\n**(1)**\nin section 9(c)(2)(A), by striking , and 2003 and inserting 2003, 2026, and each fiscal year thereafter ; and\n**(2)**\nin section 9(c)(2)(B), by striking , and 2003 and inserting 2003, 2026, and each fiscal year thereafter .\n##### (b) Housing Act of 1959\nSection 202(m) of the Housing Act of 1959 ( 12 U.S.C. 1701q(m) ) is amended to read as follows:\n(m) Authorization of appropriations There is authorized to be appropriated such sums as may be necessary to carry out this section. .\n##### (c) Cranston-Gonzalez National Affordable Housing Act\nSubsection (m) of section 811 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013(m) ) is amended by striking the period at the end and inserting , and such sums as necessary for fiscal year 2026 and each fiscal year thereafter .\n#### 4. Unlawful discrimination based on source of income\nThe Fair Housing Act ( 42 U.S.C. 3601 et seq. ) is amended\u2014\n**(1)**\nin section 804, by striking or national origin each place it appears and inserting national origin, or lawful source of income ;\n**(2)**\nin section 805\u2014\n**(A)**\nin subsection (a), by striking or national origin and inserting national origin, or lawful source of income ; and\n**(B)**\nin subsection (e), by striking or familial status and inserting familial status, or lawful source of income ;\n**(3)**\nin section 806, by striking or national origin and inserting national origin, or lawful source of income ;\n**(4)**\nin section 807(a), by striking or national origin and inserting national origin, or lawful source of income ; and\n**(5)**\nin section 808(e)(6), by striking and family characteristics and inserting family characteristics, and lawful sources of income, .\n#### 5. Housing navigation grant for housing choice voucher program\nSection 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) is amended by adding at the end the following:\n(23) Housing navigation grant (A) In general Not later than 1 year after the date of the enactment of this paragraph, the Secretary shall establish a grant program to award housing navigation grants to public housing agencies. (B) Eligible uses A public housing agency that is awarded a grant under this paragraph shall use such grant to\u2014 (i) assist families receiving tenant-based assistance with the search to find a suitable dwelling unit; or (ii) engage with owners of dwelling units for the purpose of assisting such families in such search. (C) Subgrants A public housing agency that is awarded a grant under this paragraph may use such grant amounts to provide subgrants to nonprofit organizations to carry out the eligible uses described in subparagraph (B). (D) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this paragraph $20,000,000 for fiscal year 2026 and each fiscal year thereafter. .\n#### 6. Use of small area fair market rents for housing choice voucher program\nSection 8(o)(1) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(1) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking subparagraph (D) and inserting subparagraphs (D) and (F) ; and\n**(2)**\nby adding at the end the following:\n(F) Use of small area fair market rents Effective for fiscal year 2026 and each fiscal year thereafter, the area fair market rents used for purposes of subparagraph (B) shall be established by the Secretary by zip code areas. .\n#### 7. Technical assistance for applicants for admission to a public housing project\nSection 9(h)(1) of the United States Housing Act of 1937 ( 42 U.S.C. 1437g(h)(1) ) is amended by inserting applicants for admission to a project, after organizations, .\n#### 8. Expansion of housing choice voucher program\n##### (a) Expanded vouchers\n**(1) Funding**\nThere is appropriated, out of any money in the Treasury not otherwise appropriated, for providing incremental vouchers for rental assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) in accordance with this section for each of fiscal years 2026 through 2029, the amount necessary to fund\u2014\n**(A)**\nthe number of incremental vouchers required to be allocated under paragraph (2);\n**(B)**\nannual renewals of the vouchers allocated under paragraph (2); and\n**(C)**\nadministrative fees for vouchers allocated under paragraph (2).\n**(2) Allocation**\n**(A) Incremental vouchers**\nThe Secretary shall allocate 500,000 incremental vouchers in fiscal year 2026 and 1,500,000 incremental vouchers in increments of 500,000 in each calendar year from 2027 through 2029 under this section to public housing agencies pursuant to section 213(d) of the Housing and Community Development Act of 1974 ( 42 U.S.C. 1439(d) ).\n**(B) Selection criteria**\nThe Secretary shall, by notice in the Federal Register, establish selection criteria under section 213(d) of the Housing and Community Development Act of 1974 ( 42 U.S.C. 1439(d) ) that prioritizes housing needs among eligible households and severe housing hardship, such as experiencing homelessness, overcrowding, or evictions.\n##### (b) Entitlement to vouchers\n**(1) In general**\nOn and after the date that is 5 years after the date of enactment of this Act, any family that is otherwise eligible for tenant-based rental assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) shall be entitled to that rental assistance during any period that the family is an eligible household.\n**(2) Funding**\nThere is appropriated, out of any money in the Treasury not otherwise appropriated, such sums as may be necessary\u2014\n**(A)**\nto provide assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) in accordance with the entitlement under paragraph (1) of this subsection for each eligible household in the amount determined under such section 8(o); and\n**(B)**\nto provide administrative fees under section 8(q) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(q) ) in connection with each voucher for assistance provided pursuant to subparagraph (A) of this paragraph.\n##### (c) Eligible household defined\nIn this section, term eligible household means a family who has an income that does not exceed 80 percent of the area median income, as determined by a public housing agency.\n#### 9. Section 8 Management Assessment Program\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Housing and Urban Development shall issue a rule to consider the timeliness of approval for both eligible families and landlords with respect to the Section 8 Management Assessment Program (SEMAP) or any successor assessment program, as described in part 985 of title 24, Code of Federal Regulations.",
      "versionDate": "2025-05-01",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-05-21T14:07:59Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3133ih.xml"
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
      "title": "HAVEN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HAVEN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Accessibility and Voucher Expansion Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend certain Acts related to housing to adjust rental payments with respect to certain Federal rental assistance programs, to ban source of income discrimination in housing, to reform and expand the housing choice voucher program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:48:32Z"
    }
  ]
}
```
