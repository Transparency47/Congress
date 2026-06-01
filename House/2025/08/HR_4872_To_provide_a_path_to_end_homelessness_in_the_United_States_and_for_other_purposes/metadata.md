# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4872?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4872
- Title: Ending Homelessness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4872
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2026-03-27T08:06:37Z
- Update date including text: 2026-03-27T08:06:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-05 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-05 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4872",
    "number": "4872",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "W000187",
        "district": "43",
        "firstName": "Maxine",
        "fullName": "Rep. Waters, Maxine [D-CA-43]",
        "lastName": "Waters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Ending Homelessness Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:37Z",
    "updateDateIncludingText": "2026-03-27T08:06:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "actionDate": "2025-08-05",
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
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:04:45Z",
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
          "date": "2025-08-05T14:04:40Z",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "MI"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "MO"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "GA"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "NY"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "NY"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "PA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "OH"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "MA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "MI"
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
      "sponsorshipDate": "2025-08-12",
      "state": "IL"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "TX"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "NY"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "TX"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "AZ"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "AZ"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-11-28",
      "state": "TX"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "MO"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CO"
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
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4872ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4872\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Ms. Waters introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide a path to end homelessness in the United States, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Ending Homelessness Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Expansion of housing choice voucher program.\nSec. 3. Entitlement program for housing choice vouchers.\nSec. 4. Repeal of ineligibility criteria.\nSec. 5. Prohibiting housing discrimination based on source of income.\nSec. 6. Funding to address unmet need.\nSec. 7. Housing Trust Fund.\nSec. 8. Technical assistance funds to help States and local organizations align health and housing systems.\nSec. 9. Permanent authorization of appropriations for McKinney-Vento Homeless Assistance Act grants.\nSec. 10. Permanent extension of United States Interagency Council on Homelessness.\nSec. 11. Eligibility of private nonprofit organizations for funding.\nSec. 12. Eligibility of faith-based organizations.\nSec. 13. Conforming amendments.\nSec. 14. Funding priority.\n#### 2. Expansion of housing choice voucher program\n##### (a) Funding\nThere is appropriated out of any money in the Treasury not otherwise appropriated, for providing incremental voucher assistance in accordance with this section for each of fiscal years 2025 through 2028, the amount necessary to fund\u2014\n**(1)**\nthe number of incremental vouchers required to be allocated under subsection (c);\n**(2)**\nannual renewals of the vouchers allocated under subsection (c); and\n**(3)**\nadministrative fees for vouchers allocated under subsection (c).\n##### (b) Eligible households\nAmounts made available under subsection (a) may be used only for providing rental housing assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) for an eligible family who initially\u2014\n**(1)**\nhas an income that does not exceed 50 percent of the maximum income limitation for extremely low-income families established by the Secretary of Housing and Urban Development (in this section referred to as the Secretary ) pursuant to section 3(b)(2)(C) of the United States Housing Act of 1937; or\n**(2)**\nis an extremely low-income family that includes an individual who is an individual who is a recipient of supplemental security income benefits under title XVI of the Social Security Act.\n##### (c) Allocation\n**(1) Incremental vouchers**\nThe Secretary of Housing and Urban Development shall allocate 500,000 incremental vouchers in fiscal year 2025 and 1,000,000 incremental vouchers in increments of 500,000 in each calendar year from 2026 through 2028 under this section to public housing agencies pursuant to section 213(d) of the Housing and Community Development Act of 1974 ( 42 U.S.C. 1439 ).\n**(2) Selection criteria**\nThe Secretary shall, by notice in the Federal Register, establish selection criteria under such section 213(d) that prioritizes housing needs among families targeted under subsection (b) and severe housing hardship, such as experiencing homelessness, overcrowding or evictions.\n**(3) Rental assistance**\nVouchers allocated under this subsection shall be vouchers for rental assistance under section 8(o) of the United States Housing Act of 1937.\n#### 3. Entitlement program for housing choice vouchers\n##### (a) Entitlement\nDuring fiscal year 2029 and each fiscal year thereafter, any family that is otherwise eligible for tenant-based rental assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) shall be entitled to such rental assistance in accordance with this section during such period that such family meets the requirements under subsection (c) or (d) as a qualified family.\n##### (b) Funding\nFor fiscal year 2029 and each fiscal year thereafter, there is appropriated out of any money in the Treasury not otherwise appropriated the amount necessary\u2014\n**(1)**\nto provide assistance under section 8(o) of the United States Housing Act of 1937 in accordance with the entitlement under subsection (a) of this section for each qualified family in the amount determined under such section 8(o); and\n**(2)**\nto provide administrative fees under such section 8(q), as modified pursuant to subsection (i) of this section, in connection with each voucher for assistance provided pursuant to paragraph (1) of this subsection.\n##### (c) Qualified families\nFor purposes of this section, the term qualified family means the following:\n**(1) Fiscal year 2029**\nFor fiscal year 2029, a family that meets the requirements under section 2(b) of this Act.\n**(2) Fiscal year 2030**\nFor fiscal year 2030, a family having an income that\u2014\n**(A)**\nmeets the requirements under section 2(b) of this Act; or\n**(B)**\ndoes not exceed 75 percent of the maximum income limitation for extremely low-income families established by the Secretary pursuant to section 3(b)(2)(C) of the United States Housing Act of 1937.\n**(3) Fiscal year 2031**\nFor fiscal year 2031, an extremely low-income family.\n**(4) Fiscal year 2032**\nFor fiscal year 2032, a very low-income family.\n**(5) Fiscal year 2033 and after**\nFor fiscal year 2033 and each fiscal year thereafter, a low-income family.\n##### (d) Continuing eligibility\nA family shall meet the requirements under this subsection as a qualifying family if the family\u2014\n**(1)**\ndoes not meet the requirements under subsection (c); and\n**(2)**\nwas initially assisted under this section or section 2 of this Act and continues to be assisted.\n##### (e) Repeal of income targeting requirement\nEffective October 1, 2030, section 16 of the United States Housing Act of 1937 ( 42 U.S.C. 1437n ) is amended by striking subsection (b).\n##### (f) Administering agencies\n**(1) Regional consortia**\nThe Secretary shall encourage and provide for public housing agencies to form regional consortia to administer the program for rental assistance under this section with respect to geographical areas.\n**(2) PHA designation**\nThe Secretary shall designate a public housing agency to administer assistance under this section in any area where no existing public housing agency has jurisdiction or where no agency with jurisdiction is adequately administering such assistance, subject to public comment and after consultation with States, public housing agencies, local governments, Indian tribes, and tribally designated housing agencies.\n##### (g) Use of small area fair market rents\nParagraph (1) of section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(1) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking subparagraph (D) and inserting subparagraphs (D) and (F) ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(F) Use of small area fair market rents Except with respect to any metropolitan statistical area with a vacancy rate of 4 percent or less, effective for fiscal year 2025 and each fiscal year thereafter, the area fair market rents used for purposes of subparagraph (B) shall be established by the Secretary for ZIP Code areas. .\n##### (h) Project-Basing\n**(1) In general**\nNotwithstanding subparagraph (A) of paragraph (13) of section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(13)(A) ), a public housing agency administering assistance under this section may enter into agreements to attach such assistance to a project in accordance with such paragraph, except that\u2014\n**(A)**\na qualified family residing in a dwelling unit so assisted may at any time opt to use such assistance on a tenant-based basis for a different dwelling unit and, upon such a move, the public housing agency shall provide the qualified family with tenant-based rental assistance under this section; and\n**(B)**\nsubparagraph (B) of such section 8(o)(13) (relating to percentage limitation) shall not apply with respect to assistance under this section.\n**(2) Percentage limitation**\nFor purposes of section 8(o)(13)(B) of the United States Housing Act of 1937, all families assisted by a public housing agency under this section shall be counted as authorized units for the agency.\n##### (i) Security deposits\n**(1) Authority**\nAn agency administering assistance under this section may authorize a qualified family assisted under this section to use such assistance for security deposits and broker and application fees relating to obtaining a dwelling unit, except that the Secretary may establish a limitation on the amount of such assistance used pursuant to this subsection and for each authorized purpose under this subsection.\n**(2) Recapture**\nThe Secretary shall require the return to the Secretary of any amounts used for a security deposit with respect to a dwelling unit upon the termination of the residence in such unit by an assisted family.\n##### (j) Administrative fees\nNotwithstanding the administrative fee with respect to tenant-based assistance in effect on October 1, 2023, pursuant to section 8(q) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(q) ), the Secretary shall, by regulation, establish a new administrative fee for such assistance, applicable to fiscal year 2025 and thereafter, that reflects local variation in the cost of administering a well-run housing choice voucher program and which encourages public housing agencies to expand housing choice for assisted families and increase the rate at which families issued vouchers use them successfully to lease housing.\n##### (k) Prohibition of use under Moving to Work program\nNone of the amounts made available by subsection (b) of this section or by section 2 of this Act may be used under, to carry out, or otherwise in connection with the Moving to Work demonstration program authorized by section 204 of the Departments of Veterans Affairs and Housing and Urban Development and Independent Agencies Appropriations Act, 1996 ( Public Law 104\u2013134 ; 110 Stat. 1321), as expanded by section 239 of the Transportation, Housing and Urban Development, and Related Agencies Appropriations Act, 2016 (division L of Public Law 114\u2013113 ; 129 Stat. 2897) or any other provision of law.\n##### (l) Definitions\nFor purposes of this section, the following definitions shall apply:\n**(1) Indian tribe; tribally designated housing agency**\nThe terms Indian tribe and tribally designated housing agency have the meanings given such terms in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ).\n**(2) Low-income family; very low-income family; extremely low-income family**\nThe terms low-income family , very low-income family , and extremely low-income family have the meanings given such terms in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) ).\n**(3) Public housing agency**\nThe term public housing agency has the meaning given such term in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) ).\n**(4) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(5) State**\nThe term State has the meaning given such term in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) ).\n#### 4. Repeal of ineligibility criteria\n##### (a) United States Housing Act of 1937\nEffective October 1, 2027, section 6 of the United States Housing Act of 1937 ( 42 U.S.C. 1437d ) is amended\u2014\n**(1)**\nin subsection (q)(1), by adding at the end the following new subparagraph:\n(D) Inapplicability This subsection shall not apply to applicants for, or families assisted under, the entitlement program for housing choice vouchers under section 3 of the Ending Homelessness Act of 2025 . ; and\n**(2)**\nin subsection (s), by striking or assisted housing program .\n##### (b) Quality Housing and Work Responsibility Act of 1998\nThe Quality Housing and Work Responsibility Act of 1998 is amended\u2014\n**(1)**\nin section 576 ( 42 U.S.C. 13661 )\u2014\n**(A)**\nby inserting covered before federally assisted housing each place such term appears; and\n**(B)**\nby adding at the end the following new subsection:\n(f) Definition of covered federally assisted housing The term covered federally assisted housing has the meaning given the term federally assisted housing in section 579, except that the former term shall not include housing specified in subsection (a)(2)(B) of such section. ; and\n**(2)**\nin section 577(a) ( 42 U.S.C. 13662(a) ), by adding after and below paragraph (2) the following new flush material:\nThis subsection shall not apply to applicants for, or families assisted under, the entitlement program for housing choice vouchers under section 3 of the Ending Homelessness Act of 2025 . .\n#### 5. Prohibiting housing discrimination based on source of income\n##### (a) In general\nThe Fair Housing Act ( 42 U.S.C. 3601 et seq. ) is amended\u2014\n**(1)**\nin section 802 ( 42 U.S.C. 3602 ), by adding at the end the following:\n(p) Source of income includes\u2014 (1) current and future use of a tenant- or project-based housing voucher under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ) and any form of Federal, State, or local housing assistance provided to a person or family or provided to a housing owner on behalf of a person or family, including rental vouchers, rental assistance, down payment assistance, other homeownership assistance, assistance to cover housing costs, and other rental and homeownership subsidies, or guarantees or financial assistance provided through government and nongovernment organizations, including both receipt of such assistance and compliance with its terms thereof; (2) income received as a monthly benefit under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ), as a supplemental security income benefit under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ), or as a benefit under the Railroad Retirement Act of 1974 ( 45 U.S.C. 231 et seq. ) or income provided through Federal, State, or local governments or nongovernment organizations, or through any public or State-supported general or disability income assistance program or the terms of such income; (3) income received by court order, including spousal support and child support; (4) any payment from a trust, guardian, conservator, co-signer, or relative; and (5) any other source of income or funds, including savings accounts and investments. ;\n**(2)**\nin section 804 ( 42 U.S.C. 3604 )\u2014\n**(A)**\nby inserting source of income, after familial status, each place that term appears;\n**(3)**\nin section 805 ( 42 U.S.C. 3605 )\u2014\n**(A)**\nin subsection (a), by inserting source of income, after familial status, ; and\n**(B)**\nin subsection (c), by inserting source of income, after handicap, ;\n**(4)**\nin section 806 ( 42 U.S.C. 3606 ), by inserting source of income, after familial status, ;\n**(5)**\nin section 807 ( 42 U.S.C. 3607 ), by adding at the end the following new subsection:\n(c) Nothing under this title shall be construed to prohibit any entity from providing a preference for veterans or based on veteran status in the sale or rental of a dwelling or in the provision of services or facilities in connection therewith. ;\n**(6)**\nin section 808(e)(6) ( 42 U.S.C. 3608(e)(6) ), by inserting source of income, after handicap, ; and\n**(7)**\nin section 810(f) ( 42 U.S.C. 3610(f) ), by striking paragraph (4) and inserting the following:\n(4) During the period beginning on the date of enactment of the Ending Homelessness Act of 2025 and ending on the date that is 40 months after such date of enactment, each agency certified for purposes of this title on the day before such date of enactment shall, for purposes of this subsection, be considered certified under this subsection with respect to those matters for which the agency was certified on that date. If the Secretary determines in an individual case that an agency has not been able to meet the certification requirements within this 40-month period due to exceptional circumstances, such as the infrequency of legislative sessions in that jurisdiction, the Secretary may extend such period by not more than 6 months. .\n##### (b) Prevention of intimidation in fair housing cases\nSection 901 of the Civil Rights Act of 1968 ( 42 U.S.C. 3631 ) is amended by inserting source of income (as defined in section 802), before or national origin each place that term appears.\n##### (c) Authorization of appropriations for enforcement\nThere is authorized to be appropriated for contracts, grants, and other assistance\u2014\n**(1)**\n$90,000,000 for each of fiscal years 2025 through 2034 for the Fair Housing Initiatives Program under section 561 of the Housing and Community Development Act of 1987 ( 42 U.S.C. 3616a );\n**(2)**\n$47,000,000 for each of fiscal years 2025 through 2034 for the Fair Housing Assistance Program under the Fair Housing Act ( 42 U.S.C. 3601 et seq. ); and\n**(3)**\n$3,000,000 for each of fiscal years 2025 through 2027 to the Secretary of Housing and Urban Development for a carrying out national media campaign to raise public awareness to help individuals understand their expanded rights under the Fair Housing Act and learn how to report incidents of housing discrimination.\n#### 6. Funding to address unmet need\nTitle IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 491 ( 42 U.S.C. 11408 ; relating to rural housing stability grant program) as section 441;\n**(2)**\nby redesignating section 592 ( 42 U.S.C. 11408a ; relating to use of FMHA inventory for transitional housing for homeless persons and for turnkey housing) as section 442; and\n**(3)**\nby adding at the end the following new subtitle:\nE\u2014Emergency Funding To Address Unmet Need 451. Funding to address unmet needs (a) Direct appropriations There is appropriated out of any money in the Treasury not otherwise appropriated for each of fiscal years 2025 through 2029, $1,000,000,000, to remain available until expended, for emergency relief grants under this section to address the unmet needs of homeless populations in jurisdictions with the highest need. (b) Formula grants (1) Allocation Amounts appropriated under subsection (a) for a fiscal year shall be allocated among collaborative applicants that comply with section 402, in accordance with the funding formula established under paragraph (2) of this subsection. (2) Formula The Secretary shall, in consultation with the United States Interagency Council on Homeless, establish a formula for allocating grant amounts under this section to address the unmet needs of homeless populations in jurisdictions with the highest need, using the best currently available data that targets need based on key structural determinants of homelessness in the geographic area represented by a collaborative applicant, which shall include data providing accurate counts of\u2014 (A) the poverty rate in the geographic area represented by the collaborative applicant; (B) shortages of affordable housing for low-, very low-, and extremely low-income households in the geographic area represented by the collaborative applicant; (C) the number of overcrowded housing units in the geographic area represented by the collaborative applicant; (D) the number of unsheltered homeless individuals and the number of chronically homeless individuals; and (E) any other factors that the Secretary considers appropriate. The formula shall provide priority to (i) collaborative applicants for which the local governments, within the area served by the applicant, have adopted local policies, such as through zoning and regulation, that leverage the private sector\u2019s participation to provide housing that is reserved and affordable to low-, very low-, and extremely low-income households, as defined by the Secretary, for a minimum term of 15 years, and (ii) collaborative applicants for which the local governments have adopted policies that decriminalize homelessness. The Secretary shall establish by regulation the process and manner that local governments will be evaluated. The Secretary shall ensure that local governments are not incentivized or otherwise rewarded for eliminating or undermining the intent of zoning regulations or other regulations or policies that establish fair wages for laborers, ensure health and safety of buildings for residents and the general public, protect fair housing, establish environmental protections, establish standards for resiliency, prevent tenant displacement, or any other requirements that the Secretary determines it is in the public interest to preserve. (3) Grants For each fiscal year for which amounts are made available under subsection (a), the Secretary shall make a grant to each collaborative applicant for which an amount is allocated pursuant to application of the formula established pursuant to paragraph (2) of this subsection in an amount that is equal to the formula amount determined for such collaborative applicant. (4) Timing The funding formula required under paragraph (2) shall be established by regulations issued, after notice and opportunity for public comment, not later than 6 months after the date of enactment of this section. (c) Use of grants (1) In general Subject to paragraphs (2) through (4), a collaborative applicant that receives a grant under this section may use such grant amounts only for eligible activities under section 415, 423, or 441(b). (2) Permanent supportive housing requirement (A) Requirement Except as provided in subparagraph (B), each collaborative applicant that receives a grant under this section shall use not less than 75 percent of such grant amount for permanent supportive housing, including capital costs, rental subsidies, and services. (B) Exemption The Secretary shall exempt a collaborative applicant from the applicability of the requirement under subparagraph (A) if the applicant demonstrates, in accordance with such standards and procedures as the Secretary shall establish, that\u2014 (i) chronic homelessness has been functionally eliminated in the geographic area served by the applicant; or (ii) the permanent supportive housing under development in the geographic area served by the applicant is sufficient to functionally eliminate chronic homelessness once such units are available for occupancy. The Secretary shall consider and make a determination regarding each request for an exemption under this subparagraph not later than 60 days after receipt of such request. (3) Limitation on use for administrative expenses Not more than 5 percent of the total amount of any grant under this section to a collaborative applicant may be used for costs of administration. (4) Housing First requirement The Secretary shall ensure that each collaborative applicant that receives a grant under this section is implementing, to the extent possible, and will use such grant amounts in accordance with, a Housing First model for assistance for homeless persons. (d) Renewal funding Expiring contracts for leasing, rental assistance, or permanent housing shall be treated, for purposes of section 429, as expiring contracts referred to in subsection (a) of such section. (e) Reporting to Congress (1) Annual reports Not later than the expiration of the 12-month period beginning upon the first allocation of amounts made after the date of the enactment of this Act pursuant to subsection (b)(1), and annually thereafter, the Secretary and the United States Interagency Council on Homelessness shall submit a report to the Committees on Financial Services and Appropriations of the House of Representatives and the Committees on Banking, Housing, and Urban Affairs and Appropriations of the Senate providing detailed information regarding the grants made under this section during the preceding year, the activities funded with such grant amounts, and the impact of such activities on the communities where such activities took place. (2) Collection of information by Secretary The Secretary shall require each collaborative applicant that receives a grant under this section to submit such information to the Secretary as may be necessary for the Secretary to comply with the reporting requirement under paragraph (1). 452. Outreach funding (a) Direct appropriation There is appropriated out of any money in the Treasury not otherwise appropriated for each of fiscal years 2025 through 2029, $100,000,000, to remain available until expended, to the Secretary for grants under this section to provide outreach and coordinate services for persons and households who are homeless or formerly homeless. (b) Grants (1) In general The Secretary shall make grants under this section on a competitive basis only to collaborative applicants who comply with section 402. (2) Priority The competition for grants under this section shall provide priority\u2014 (A) to collaborative applicants who submit plans to make innovative and effective use of staff funded with grant amounts pursuant to subsection (c); (B) to collaborative applicants for which the local governments, within the area served by the applicant, have adopted local policies, such as through zoning and regulation, that leverage the private sector\u2019s participation to provide housing that is reserved and affordable to low-, very low-, and extremely low-income households, as defined by Secretary, for a minimum term of 15 years; and (C) to collaborative applicants for which the local governments have adopted policies that decriminalize homelessness. The Secretary shall establish by regulation the process and manner that local governments will be evaluated. The Secretary shall ensure that local governments are not incentivized or otherwise rewarded for eliminating or undermining the intent of zoning regulations or other regulations or policies that establish fair wages for laborers, ensure health and safety of buildings for residents and the general public, protect fair housing, establish environmental protections, establish standards for resiliency, prevent tenant displacement, or any other requirements that the Secretary determines it is in the public interest to preserve. (c) Use of grants A collaborative applicant that receives a grant under this section\u2014 (1) may use such grant amounts only for providing case managers, social workers, or other staff who conduct outreach and coordinate services for persons and households who are homeless or formerly homeless; and (2) shall not use grant amounts for any law enforcement purposes. (d) Timing The Secretary shall establish the criteria for the competition for grants under this section required under subsection (b) by regulations issued, after notice and opportunity for public comment, not later than 6 months after the date of enactment of this section. .\n#### 7. Housing Trust Fund\n##### (a) Funding\n**(1) Annual funding**\nThere is appropriated, out of any money in the Treasury not otherwise appropriated, for each of fiscal years 2025 through 2029, $1,000,000,000, to remain available until expended, which shall be credited to the Housing Trust Fund established pursuant to section 1338 of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4568 ) for use under such section.\n**(2) Priority for housing the homeless**\n**(A) Priority**\nDuring the first 5 fiscal years that amounts are made available under this subsection, the Secretary of Housing and Urban Development shall ensure that priority for occupancy in dwelling units described in subparagraph (B) that become available for occupancy shall be given to persons and households who are homeless (as such term is defined in section 103 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11302 )).\n**(B) Covered dwelling units**\nA dwelling unit described in this subparagraph is any dwelling unit that\u2014\n**(i)**\nis located in housing that was at any time provided assistance with any amounts from the Housing Trust Fund referred to paragraph (1) that were credited to such Trust Fund by such paragraph; or\n**(ii)**\nis receiving assistance described in paragraph (2) with amounts made available under such paragraph.\n##### (b) Tenant rent contribution\n**(1) Limitation**\nSubparagraph (A) of section 1338(c)(7) of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4568(c)(7)(A) ) is amended\u2014\n**(A)**\nby striking except that not less than 75 percent and inserting the following:\nexcept that\u2014 (i) not less than 75 percent ;\n**(B)**\nby adding at the end the following new clause:\n(ii) notwithstanding any other provision of law, all rental housing dwelling units shall be subject to legally binding commitments that ensure that the contribution toward rent by a family residing in the dwelling unit shall not exceed 30 percent of the adjusted income (as such term is defined in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) )) of such family; and .\n**(2) Regulations**\nThe Secretary of Housing and Urban Development shall issue regulations to implement section 1338(c)(7)(A)(ii) of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992, as added by the amendment made by paragraph (1)(B) of this section, not later than the expiration of the 90-day period beginning on the date of the enactment of this Act.\n#### 8. Technical assistance funds to help States and local organizations align health and housing systems\n##### (a) Funding\nThere is hereby made available to the Secretary of Housing and Urban Development $20,000,000, to remain available until expended, for providing technical assistance under section 405 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11361(b) ) to integrate and coordinate assistance provided under the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11301 et seq. ) with health care funded by Federal programs, in collaboration with the United States Interagency Council on Homelessness and the Secretary of Health and Human Services.\n##### (b) Use\nIn allocating amounts made available by subsection (a), the Secretary shall seek to\u2014\n**(1)**\nassist States and localities in integrating and aligning policies and funding between Medicaid programs, behavioral health providers, and housing providers to create supportive housing opportunities; and\n**(2)**\nengage State Medicaid program directors, Governors, State housing and homelessness agencies, any other relevant State offices, and any relevant local government entities, to assist States in increasing use of their Medicaid programs to finance supportive services for homeless persons.\n##### (c) Priority\nIn using amounts made available under this section, the Secretary shall give priority\u2014\n**(1)**\nto use for States and localities having the highest numbers of chronically homeless persons; and\n**(2)**\nto assist localities that have adopted local policies, such as through zoning and regulation, that leverage the private sector\u2019s participation to provide and make housing affordable for low-, very low-, and extremely low-income household, as defined by the Secretary, for a minimum of 15 years. The Secretary shall establish by regulation the process and manner that local governments will be evaluated. The Secretary shall ensure that local governments are not incentivized or otherwise rewarded for eliminating or undermining the intent of zoning regulations or other regulations or policies that establish fair wages for laborers, ensure health and safety of buildings for residents and the general public, protect fair housing, establish environmental protections, establish standards for resiliency, prevent tenant displacement, or any other requirements that the Secretary determines it is in the public interest to preserve.\n#### 9. Permanent authorization of appropriations for McKinney-Vento Homeless Assistance Act grants\nSection 408 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11364 ) is amended to read as follows:\n408. Authorization of appropriations There are authorized to be appropriated to carry out this title such sums as may be necessary for each fiscal year. .\n#### 10. Permanent extension of United States Interagency Council on Homelessness\nSection 209 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11319 ) is hereby repealed.\n#### 11. Eligibility of private nonprofit organizations for funding\nNotwithstanding any other provision of law, the Secretary of Housing and Urban Development shall provide that private nonprofit organizations (as such term is defined in section 401 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 )) that are eligible entities (as such term is defined in such section 401), including faith-based such organizations that are eligible entities, shall be eligible for assistance made available or authorized by this Act or by the amendments made by this Act (but not including assistance under section 452 of the McKinney-Vento Homeless Assistance Act, as added by section 3 of this Act), and shall be eligible to be subgrantees for entities receiving amounts made available or authorized by this Act or by the amendments made by this Act.\n#### 12. Eligibility of faith-based organizations\nNotwithstanding any other provision of law, in determining eligibility for assistance made available by this Act or the amendments made by this Act or for which appropriations are authorized by this Act or the amendments made by this Act, the status of an entity as faith-based or the possibility that an entity may be faith-based may not be a basis for any discrimination against such entity in any manner or for any purpose.\n#### 13. Conforming amendments\nThe table of sections in section 101(b) of the McKinney-Vento Homeless Assistance Act is amended\u2014\n**(1)**\nin the item relating to title II, by striking INTERAGENCY COUNCIL ON THE HOMELESS and inserting UNITED STATES INTERAGENCY COUNCIL ON HOMELESSNESS ;\n**(2)**\nby striking the item relating to section 209;\n**(3)**\nin the item relating to section 491, by striking 491 and inserting 441 ;\n**(4)**\nin the item relating to section 492, by striking 492 and inserting 442 ; and\n**(5)**\nby inserting before the item relating to title V the following:\nSubtitle E\u2014Emergency Funding To Address Unmet Need Sec. 451. Funding to address unmet needs. Sec. 452. Outreach funding. .\n#### 14. Funding priority\nIn selecting entities to receive amounts authorized to be appropriated by this Act and amounts made available by this Act, the Secretary of Housing and Urban Development shall provide priority to entities serving areas for which the local governments having jurisdiction have adopted policies that decriminalize homelessness.",
      "versionDate": "2025-08-05",
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
        "updateDate": "2025-09-18T17:58:59Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4872ih.xml"
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
      "title": "Ending Homelessness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ending Homelessness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide a path to end homelessness in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:37Z"
    }
  ]
}
```
