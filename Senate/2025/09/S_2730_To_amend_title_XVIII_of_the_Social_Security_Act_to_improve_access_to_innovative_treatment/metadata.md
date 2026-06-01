# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2730?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2730
- Title: Kidney Care Access Protection Act
- Congress: 119
- Bill type: S
- Bill number: 2730
- Origin chamber: Senate
- Introduced date: 2025-09-08
- Update date: 2026-03-25T11:03:19Z
- Update date including text: 2026-03-25T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in Senate
- 2025-09-08 - IntroReferral: Introduced in Senate
- 2025-09-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-08: Introduced in Senate

## Actions

- 2025-09-08 - IntroReferral: Introduced in Senate
- 2025-09-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2730",
    "number": "2730",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Kidney Care Access Protection Act",
    "type": "S",
    "updateDate": "2026-03-25T11:03:19Z",
    "updateDateIncludingText": "2026-03-25T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-08",
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
      "actionDate": "2025-09-08",
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
        "item": [
          {
            "date": "2025-09-08T21:06:10Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-08T21:06:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NJ"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2730is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2730\nIN THE SENATE OF THE UNITED STATES\nSeptember 8, 2025 Mrs. Blackburn (for herself and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to improve access to innovative treatment options for end-stage renal disease under the Medicare program, and for other purposes.\n#### 1. Short title\n##### (a) In general\nThis Act may be cited as the Kidney Care Access Protection Act .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title.\nTITLE I\u2014Protecting patient access to kidney care innovation\nSec. 101. Refining the end-stage renal disease payment system to improve access to innovative treatment options.\nSec. 102. Ensuring Medicare Advantage supports kidney care innovative therapies.\nTITLE II\u2014Addressing staffing barriers with ESRD market basket labor adjustments\nSec. 201. Ensuring accuracy and stability in kidney care payment.\nI\nProtecting patient access to kidney care innovation\n#### 101. Refining the end-stage renal disease payment system to improve access to innovative treatment options\n##### (a) Extension of Transitional Drug Add-On Payment Adjustment (TDAPA) period\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ) shall pay the transitional drug add-on payment adjustment under section 413.234(c) of title 42, Code of Federal Regulations (or a successor regulation), for not less than 3 years for any new renal dialysis drug or biological product\u2014\n**(1)**\napproved by the Food and Drug Administration on or after January 1, 2020, under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or section 351 of the Public Health Service Act ( 42 U.S.C. 262 );\n**(2)**\nthat qualifies for such adjustment under such section; and\n**(3)**\nthat is furnished on or after January 1, 2026.\n##### (b) Permanent post-TDAPA adjustment\nSection 1881(b)(14) of the Social Security Act ( 42 U.S.C. 1395rr(b)(14) ) is amended by adding at the end the following new subparagraph:\n(J) Payment for new and innovative drugs, biologicals, and devices that are renal dialysis services (i) In general For any new renal dialysis drug or biological product that is used to treat or manage a condition as defined in section 413.234(a) of title 42, Code of Federal Regulations that received a transitional drug add-on payment adjustment (referred to in this subparagraph as TDAPA ) under section 413.234(c) of such title, and was furnished on or after January 1, 2024, the Secretary shall establish a permanent add-on adjustment to the base rate for claims submitted on or after January 1, 2026, that includes the administration of such drugs or biologicals. (ii) Calculation of the post-TDAPA add-on adjustment In calculating the add-on adjustment described in clause (i), the Secretary shall\u2014 (I) base the calculation on\u2014 (aa) except as provided in items (bb) and (cc), the most recent 12-month period of utilization for the new renal dialysis drug or biological product and the most recent available full calendar quarter of average sales price data for such drug or product; (bb) if the most recent available full calendar quarter of average sales price data reflects 0 or negative sales, 100 percent of the wholesale acquisition cost (as defined in section 1847A(c)(6)) of such drug or product; or (cc) if the wholesale acquisition cost is not available, the drug manufacturer\u2019s invoice; (II) calculate the post-TDAPA add-on payment adjustment as the expenditures for the new renal dialysis drug or biological product divided by the total number of renal dialysis services during which such drug or biological was administered during the same period; (III) set the amount of the add-on adjustment as an amount equal to 65 percent of the amount calculated under subclause (II); (IV) update the add-on adjustment annually to account for inflationary changes; and (V) apply the add-on adjustment amount immediately upon the expiration of the TDAPA period and availability of the post-TDAPA add-on adjustment. (iii) Implementation This subparagraph shall not be implemented in a budget neutral manner and shall not be adjusted by any applicable patient-level case-mix adjustments described in section 413.235 of title 42, Code of Federal Regulations (or any successor regulation). .\n##### (c) Clarification to definition of renal dialysis services\nSection 1881(b)(14)(B) of the Social Security Act ( 42 U.S.C. 1395rr(b)(14)(B) ) is amended\u2014\n**(1)**\nby redesignating clauses (i) through (iv) as subclauses (I) through (IV), respectively;\n**(2)**\nby inserting (i) after (B) ;\n**(3)**\nin clause (i)(IV), as added by paragraph (2), by striking clause (i) and inserting subclause (I) ;\n**(4)**\nin the flush text at the end, by striking Such term does not and inserting the following:\n(ii) Such term\u2014 (I) does not ;\n**(5)**\nin clause (ii), as added by paragraph (2)\u2014\n**(A)**\nin subclause (I), by striking the period at the end and inserting ; and ; and\n**(B)**\nby adding at the end the following:\n(II) does not include drugs or biological products used to treat a comorbid disease or condition (including cardiovascular disease, an inflammatory condition, cancer, diabetes, and obesity) that may occur in an individual who has been determined to have end-stage renal diseases and is receiving dialysis and\u2014 (aa) that have been approved by the Food and Drug Administration after December 31, 2025; and (bb) do not substitute for a drug or biological included in the ESRD prospective payment system base rate. ; and\n**(6)**\nby adding at the end the following new clause:\n(iii) Implementation Beginning on the date of enactment of this clause, for purposes of implementing clause (ii)(II), the Secretary shall require that a claim for a drug or biological product described in such clause, that is payable under this part and is furnished by a provider of services or renal dialysis facility, contain the AY modifier (or a successor modifier). .\n##### (d) Revisions to Transitional Add-On Payment Adjustment for New and Innovative Equipment and Supplies (TPNIES)\n**(1) Extension of period**\nThe Secretary shall pay the transitional add-on payment adjustment for new and innovative equipment and supplies under section 413.236 of title 42, Code of Federal Regulations (or a successor regulation), for not less than 3 years for any new renal dialysis device that\u2014\n**(A)**\nqualifies for such adjustment; and\n**(B)**\nis furnished on or after January 1, 2026.\n**(2) Eligibility of breakthrough devices**\nBeginning January 1, 2026, a device designated for expedited development and priority review under section 515B of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360e\u20133 ) shall be eligible for a transitional add-on payment adjustment for new and innovative equipment and supplies under section 413.236 of title 42, Code of Federal Regulations (or a successor regulation).\n**(3) Inclusion of capital-related assets in the transitional add-on payment adjustment for new and innovative equipment and supplies and post-Transitional Add-On Payment Adjustment for New and Innovative Equipment and Supplies**\nBeginning January 1, 2026, the Secretary shall not apply the criterion described in section 413.236(b)(6) of title 42, Code of Federal Regulations (or a successor regulation), that excludes capital-related assets from the transitional add-on payment adjustment for new and innovative equipment and supplies and shall calculate such adjustment for capital-related assets that are devices that otherwise meet the requirements for the transitional add-on payment adjustment for new and innovative equipment.\n##### (e) Effective date\nThe amendments made by this section shall take effect on January 1, 2026, and apply to items and services furnished on or after such date.\n#### 102. Ensuring Medicare Advantage supports kidney care innovative therapies\n##### (a) In general\nSection 1853(c) of the Social Security Act ( 42 U.S.C. 1395w\u201323(c) ) is amended by adding at the end the following new paragraph:\n(8) Treatment of innovative products for enrollees with end-stage renal disease (A) In general Beginning January 1, 2026, the Secretary shall make direct payment adjustments to providers of services or renal dialysis facilities for\u2014 (i) any new renal dialysis drug or biological product that receives a transitional drug add-on payment adjustment under section 413.234(c) of title 42, Code of Federal Regulations; or (ii) an item or service that receives a transitional add-on payment adjustment for new and innovative equipment and supplies under section 413.236 of such title. (B) Amount of direct payment The amount of the adjustment shall equal the amount determined under the end-stage renal disease prospective payment system described in section 1881(b)(14). (C) Duration of direct payment The Secretary shall make payments under subparagraph (A) for the duration of the transitional payment under the end-stage renal disease prospective payment system described in such section. .\n##### (b) Conforming amendments\nSection 1851(i) of the Social Security Act ( 42 U.S.C. 1395w\u201321 ) is amended\u2014\n**(1)**\nin paragraph (1), by inserting 1853(c)(8), after 1886(h)(3)(D), ; and\n**(2)**\nin paragraph (2), by inserting 1853(c)(8), after 1853(h), .\nII\nAddressing staffing barriers with ESRD market basket labor adjustments\n#### 201. Ensuring accuracy and stability in kidney care payment\nSection 1881(b)(14)(F)(i) of the Social Security Act ( 42 U.S.C. 1395rr(b)(14)(F)(i) ) is amended\u2014\n**(1)**\nin subclause (I), by striking subclauses (II) and (III) and inserting subclauses (II), (III), and (IV) ;\n**(2)**\nin subclause (II), by inserting and after application of subclause (IV) after subclause (I) ; and\n**(3)**\nby adding at the end the following new subclause:\n(IV) Beginning with 2026, the Secretary shall compute an adjustment to the increase factor described in subclause (I) for the annual update of the payment amounts established under this paragraph for the previous year to account for forecast error (referred to in this subclause as the forecast error adjustment ). The initial adjustment (in 2026) to the increase factor shall take into account the cumulative forecast error for 2021 and 2022. Subsequent adjustments in succeeding years shall take into account the forecast error from the most recently available year for which there is final data. The forecast error adjustment under this subclause shall apply whenever the difference between the forecasted and actual percentage change in the prices of an appropriate mix of goods and services included in renal dialysis services exceeds 0.5 percentage points. .",
      "versionDate": "2025-09-08",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6214",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Kidney Care Access Protection Act",
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
        "name": "Health",
        "updateDate": "2025-09-23T15:22:23Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2730is.xml"
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
      "title": "Kidney Care Access Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Kidney Care Access Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-16T04:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to improve access to innovative treatment options for end-stage renal disease under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-16T04:48:16Z"
    }
  ]
}
```
