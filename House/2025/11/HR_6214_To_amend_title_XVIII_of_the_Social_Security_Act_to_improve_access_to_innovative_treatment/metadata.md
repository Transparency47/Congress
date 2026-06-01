# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6214?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6214
- Title: Kidney Care Access Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 6214
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-27T08:06:26Z
- Update date including text: 2026-05-27T08:06:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6214",
    "number": "6214",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Kidney Care Access Protection Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:26Z",
    "updateDateIncludingText": "2026-05-27T08:06:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-20T15:05:35Z",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "AL"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NY"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "OH"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "NY"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "PA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-17",
      "state": "LA"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NC"
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
      "sponsorshipDate": "2026-03-16",
      "state": "NC"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "SC"
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
      "sponsorshipDate": "2026-04-20",
      "state": "PA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "NY"
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
      "sponsorshipDate": "2026-05-26",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6214ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6214\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mrs. Miller of West Virginia (for herself and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to improve access to innovative treatment options for end-stage renal disease under the Medicare program, and for other purposes.\n#### 1. Short title\n##### (a) In general\nThis Act may be cited as the Kidney Care Access Protection Act .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title.\nTitle I\u2014Protecting Patient Access to Kidney Care Innovation\nSec. 101. Refining the end-stage renal disease payment system to improve access to innovative treatment options.\nSec. 102. Ensuring Medicare Advantage supports kidney care innovative therapies.\nTitle II\u2014Addressing Staffing Barriers with ESRD Market Basket Labor Adjustments\nSec. 201. Ensuring accuracy and stability in kidney care payment.\nTitle III\u2014Preventing Kidney Disease and Expanding Awareness and Education\nSec. 301. Expanding medicare annual wellness benefit to include kidney disease screening.\nSec. 302. Increasing access to medicare kidney disease education benefit.\nI\nProtecting Patient Access to Kidney Care Innovation\n#### 101. Refining the end-stage renal disease payment system to improve access to innovative treatment options\n##### (a) Extension of Transitional Drug Add-On Payment Adjustment (TDAPA) period\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ) shall pay the transitional drug add-on payment adjustment under section 413.234(c) of title 42, Code of Federal Regulations (or a successor regulation), for not less than 3 years for any new renal dialysis drug or biological product\u2014\n**(1)**\napproved by the Food and Drug Administration on or after January 1, 2020, under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or section 351 of the Public Health Service Act ( 42 U.S.C. 262 );\n**(2)**\nthat qualifies for such adjustment under such section; and\n**(3)**\nthat is furnished on or after January 1, 2026.\n##### (b) Permanent post-TDAPA adjustment\nSection 1881(b)(14) of the Social Security Act ( 42 U.S.C. 1395rr(b)(14) ) is amended by adding at the end the following new subparagraph:\n(J) Payment for new and innovative drugs, biologicals, and devices that are renal dialysis services (i) In general For any new renal dialysis drug or biological product that is used to treat or manage a condition as defined in section 413.234(a) of title 42, Code of Federal Regulations that received a transitional drug add-on payment adjustment (referred to in this subparagraph as TDAPA ) under section 413.234(c) of such title, and was furnished on or after January 1, 2024, the Secretary shall establish a permanent add-on adjustment to the base rate for claims submitted on or after January 1, 2026, that includes the administration of such drugs or biologicals. (ii) Calculation of the post-TDAPA add-on adjustment In calculating the add-on adjustment described in clause (i), the Secretary shall\u2014 (I) base the calculation on\u2014 (aa) except as provided in items (bb) and (cc), the most recent 12-month period of utilization for the new renal dialysis drug or biological product and the most recent available full calendar quarter of average sales price data for such drug or product; (bb) if the most recent available full calendar quarter of average sales price data reflects 0 or negative sales, 100 percent of the wholesale acquisition cost (as defined in section 1847A(c)(6)) of such drug or product; or (cc) if the wholesale acquisition cost is not available, the drug manufacturer\u2019s invoice; (II) calculate the post-TDAPA add-on payment adjustment as the expenditures for the new renal dialysis drug or biological product divided by the total number of renal dialysis services during which such drug or biological was administered during the same period; (III) set the amount of the add-on adjustment as an amount equal to 65 percent of the amount calculated under subclause (II); (IV) update the add-on adjustment annually to account for inflationary changes; and (V) apply the add-on adjustment amount immediately upon the expiration of the TDAPA period and availability of the post-TDAPA add-on adjustment. (iii) Implementation This subparagraph shall not be implemented in a budget neutral manner and shall not be adjusted by any applicable patient-level case-mix adjustments described in section 413.235 of title 42, Code of Federal Regulations (or any successor regulation). .\n##### (c) Clarification to definition of renal dialysis services\nSection 1881(b)(14)(B) of the Social Security Act ( 42 U.S.C. 1395rr(b)(14)(B) ) is amended\u2014\n**(1)**\nby redesignating clauses (i) through (iv) as subclauses (I) through (IV), respectively;\n**(2)**\nby inserting (i) after (B) ;\n**(3)**\nin clause (i)(IV), as added by paragraph (2), by striking clause (i) and inserting subclause (I) ;\n**(4)**\nin the flush text at the end, by striking Such term does not and inserting the following:\n(ii) Such term\u2014 (I) does not ;\n**(5)**\nin clause (ii), as added by paragraph (2)\u2014\n**(A)**\nin subclause (I), by striking the period at the end and inserting ; and ; and\n**(B)**\nby adding at the end the following:\n(II) does not include drugs or biological products used to treat a comorbid disease or condition (including cardiovascular disease, an inflammatory condition, cancer, diabetes, and obesity) that may occur in an individual who has been determined to have end-stage renal diseases and is receiving dialysis and\u2014 (aa) that have been approved by the Food and Drug Administration after December 31, 2025; and (bb) do not substitute for a drug or biological included in the ESRD prospective payment system base rate. ; and\n**(6)**\nby adding at the end the following new clause:\n(iii) Implementation Beginning on the date of enactment of this clause, for purposes of implementing clause (ii)(II), the Secretary shall require that a claim for a drug or biological product described in such clause, that is payable under this part and is furnished by a provider of services or renal dialysis facility, contain the AY modifier (or a successor modifier). .\n##### (d) Revisions to Transitional Add-On Payment Adjustment for New and Innovative Equipment and Supplies (TPNIES)\n**(1) Extension of period**\nThe Secretary shall pay the transitional add-on payment adjustment for new and innovative equipment and supplies under section 413.236 of title 42, Code of Federal Regulations (or a successor regulation), for not less than 3 years for any new renal dialysis device that\u2014\n**(A)**\nqualifies for such adjustment; and\n**(B)**\nis furnished on or after January 1, 2026.\n**(2) Eligibility of breakthrough devices**\nBeginning January 1, 2026, a device designated for expedited development and priority review under section 515B of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360e\u20133 ) shall be eligible for a transitional add-on payment adjustment for new and innovative equipment and supplies under section 413.236 of title 42, Code of Federal Regulations (or a successor regulation).\n**(3) Inclusion of capital-related assets in the transitional add-on payment adjustment for new and innovative equipment and supplies and post-Transitional Add-On Payment Adjustment for New and Innovative Equipment and Supplies**\nBeginning January 1, 2026, the Secretary shall not apply the criterion described in section 413.236(b)(6) of title 42, Code of Federal Regulations (or a successor regulation), that excludes capital-related assets from the transitional add-on payment adjustment for new and innovative equipment and supplies and shall calculate such adjustment for capital-related assets that are devices that otherwise meet the requirements for the transitional add-on payment adjustment for new and innovative equipment.\n##### (e) Effective date\nThe amendments made by this section shall take effect on January 1, 2026, and apply to items and services furnished on or after such date.\n#### 102. Ensuring Medicare Advantage supports kidney care innovative therapies\n##### (a) In general\nSection 1853(c) of the Social Security Act ( 42 U.S.C. 1395w\u201323(c) ) is amended by adding at the end the following new paragraph:\n(8) Treatment of innovative products for enrollees with end stage renal disease (A) In general Beginning January 1, 2026, the Secretary shall make direct payment adjustments to providers of services or renal dialysis facilities for\u2014 (i) any new renal dialysis drug or biological product that receives a transitional drug add-on payment adjustment under section 413.234(c) of title 42, Code of Federal Regulations; or (ii) an item or service that receives a transitional add-on payment adjustment for new and innovative equipment and supplies under section 413.236 of such title. (B) Amount of direct payment The amount of the adjustment shall equal the amount determined under the end-stage renal disease prospective payment system described in section 1881(b)(14). (C) Duration of direct payment The Secretary shall make payments under subparagraph (A) for the duration of the transitional payment under the end-stage renal disease prospective payment system described in such section. .\n##### (b) Conforming amendments\nSection 1851(i) of the Social Security Act ( 42 U.S.C. 1395w\u201321 ) is amended\u2014\n**(1)**\nin paragraph (1), by inserting 1853(c)(8), after 1886(h)(3)(D), ; and\n**(2)**\nin paragraph (2), by inserting 1853(c)(8), after 1853(h), .\nII\nAddressing Staffing Barriers with ESRD Market Basket Labor Adjustments\n#### 201. Ensuring accuracy and stability in kidney care payment\nSection 1881(b)(14)(F)(i) of the Social Security Act ( 42 U.S.C. 1395rr(b)(14)(F)(i) ) is amended\u2014\n**(1)**\nin subclause (I), by striking subclauses (II) and (III) and inserting subclauses (II), (III), and (IV) ;\n**(2)**\nin subclause (II), by inserting and after application of subclause (IV) after subclause (I) ; and\n**(3)**\nby adding at the end the following new subclause:\n(IV) Beginning with 2026, the Secretary shall compute an adjustment to the increase factor described in subclause (I) for the annual update of the payment amounts established under this paragraph for the previous year to account for forecast error (referred to in this subclause as the forecast error adjustment ). The initial adjustment (in 2026) to the increase factor shall take into account the cumulative forecast error for 2021 and 2022. Subsequent adjustments in succeeding years shall take into account the forecast error from the most recently available year for which there is final data. The forecast error adjustment under this subclause shall apply whenever the difference between the forecasted and actual percentage change in the prices of an appropriate mix of goods and services included in renal dialysis services exceeds 0.5 percentage points. .\nIII\nPreventing Kidney Disease and Expanding Awareness and Education\n#### 301. Expanding medicare annual wellness benefit to include kidney disease screening\n##### (a) In general\nSection 1861(ww)(2) of the Social Security Act ( 42 U.S.C. 1395x(ww)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraph (O) as subparagraph (P); and\n**(2)**\nby inserting after subparagraph (N) the following new subparagraph:\n(O) Chronic kidney disease screening as defined by the Secretary. .\n##### (b) Effective date\nThe amendments made by this section shall apply to items and services furnished on or after January 1, 2026.\n#### 302. Increasing access to medicare kidney disease education benefit\n##### (a) In general\nSection 1861(ggg) of the Social Security Act ( 42 U.S.C. 1395x(ggg) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A), by inserting or stage V after stage IV ; and\n**(B)**\nin subparagraph (B), by inserting or of a physician assistant, nurse practitioner, or clinical nurse specialist (as defined in section 1861(aa)(5)) assisting in the treatment of the individual\u2019s kidney condition after kidney condition ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking subparagraph (B); and\n**(B)**\nin subparagraph (A)\u2014\n**(i)**\nby striking (A) after (2) ;\n**(ii)**\nby striking and at the end of clause (i);\n**(iii)**\nby striking the period at the end of clause (ii) and inserting ; and ;\n**(iv)**\nby redesignating clauses (i) and (ii) as subparagraphs (A) and (B), respectively; and\n**(v)**\nby adding at the end the following:\n(C) a renal dialysis facility subject to the requirements of section 1881(b)(1) with personnel who\u2014 (i) provide the services described in paragraph (1); and (ii) is a physician (as defined in subsection (r)(1)) or a physician assistant, nurse practitioner, or clinical nurse specialist (as defined in subsection (aa)(5)). .\n##### (b) Payment to renal dialysis facilities\nSection 1881(b) of the Social Security Act ( 42 U.S.C. 1395rr(b) ) is amended by adding at the end the following new paragraph:\n(15) For purposes of paragraph (14), the single payment for renal dialysis services under such paragraph shall not take into account the amount of payment for kidney disease education services (as defined in section 1861(ggg)). Instead, payment for such services shall be made to the renal dialysis facility on an assignment-related basis under section 1848. .\n##### (c) Effective date\nThe amendments made by this section shall apply to kidney disease education services furnished on or after January 1, 2026.",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-09-08",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2730",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Kidney Care Access Protection Act",
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
        "name": "Health",
        "updateDate": "2025-12-10T16:40:26Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6214ih.xml"
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
      "title": "Kidney Care Access Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Kidney Care Access Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to improve access to innovative treatment options for end-stage renal disease under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:22Z"
    }
  ]
}
```
