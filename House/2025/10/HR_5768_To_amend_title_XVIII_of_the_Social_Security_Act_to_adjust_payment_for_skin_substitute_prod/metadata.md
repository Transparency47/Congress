# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5768?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5768
- Title: Skin Substitute Access and Payment Reform Act
- Congress: 119
- Bill type: HR
- Bill number: 5768
- Origin chamber: House
- Introduced date: 2025-10-17
- Update date: 2026-02-24T22:26:18Z
- Update date including text: 2026-02-24T22:26:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-17: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-17: Introduced in House

## Actions

- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-17",
    "latestAction": {
      "actionDate": "2025-10-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5768",
    "number": "5768",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Skin Substitute Access and Payment Reform Act",
    "type": "HR",
    "updateDate": "2026-02-24T22:26:18Z",
    "updateDateIncludingText": "2026-02-24T22:26:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
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
      "actionDate": "2025-10-17",
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
      "actionDate": "2025-10-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-17",
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
          "date": "2025-10-17T18:03:45Z",
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
          "date": "2025-10-17T18:03:40Z",
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
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "TX"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "FL"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "GA"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "TX"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "VA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "AZ"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-12-26",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5768ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5768\nIN THE HOUSE OF REPRESENTATIVES\nOctober 17, 2025 Mr. Carter of Georgia (for himself, Mr. Veasey , Mr. Steube , and Mr. McCormick ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to adjust payment for skin substitute products under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Skin Substitute Access and Payment Reform Act .\n#### 2. Payment reform for skin substitute products\n##### (a) Coverage of skin substitute products\nSection 1861(s)(2) of the Social Security Act ( 42 U.S.C. 1395x(s)(2) ) is amended\u2014\n**(1)**\nin subparagraph (JJ), by adding and at the end; and\n**(2)**\nby inserting after subparagraph (JJ) the following new subparagraph:\n(KK) skin substitute products (as defined in section 1847A(c)(6)(J)). .\n##### (b) Payment\n**(1) Payment amount**\nSection 1847A of the Social Security Act ( 42 U.S.C. 1395w\u20133a ) is amended\u2014\n**(A)**\nin subsection (a)(1)\u2014\n**(i)**\nby striking the period at the end and inserting ; and ;\n**(ii)**\nby striking shall apply to and inserting\nshall apply\u2014 (A) to ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(B) to payment for skin substitute products (as defined in subsection (c)(6)(J)) that are furnished on or after January 1, 2026. ;\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nin the text preceding subparagraph (A), by inserting or a skin substitute product after drug or biological ;\n**(II)**\nin subparagraph (B), by striking or at the end;\n**(III)**\nin subparagraph (C), by striking the period at the end and inserting ; or ; and\n**(IV)**\nby adding at the end the following new subparagraph:\n(D) in the case of a skin substitute product (as defined in subsection (c)(6)(J)), the amount determined under paragraph (9). ; and\n**(ii)**\nin paragraph (2)\u2014\n**(I)**\nin subparagraph (A), by inserting or a skin substitute product after drug or biological ; and\n**(II)**\nin subparagraph (B), by inserting , and, with respect to a skin substitute product, a square centimeter after pertaining to liquids ; and\n**(iii)**\nby adding at the end the following:\n(9) Skin substitute products (A) Payment amount (i) Initial payment amount For 2026, the amount determined under this paragraph for a skin substitute product is the volume-weighted average of the Medicare payment allowance limits for skin substitute products, as determined under subparagraph (B). (ii) Annual update For 2027 and each subsequent year, the amount determined under this paragraph for a skin substitute product for such year is equal to the amount determined under this paragraph for the previous year, adjusted by the percentage increase in the Consumer Price Index for All Urban Consumers (United States city average) for the 12-month period ending with June of such previous year. (B) Volume-weighted average payment limit For purposes of subparagraph (A)(i), the volume-weighted average of the Medicare payment allowance limits for skin substitute products is determined by\u2014 (i) calculating, with respect to each billing and payment code listed in the October 2023 ASP Pricing File for each skin substitute product, an amount equal to the product of\u2014 (I) the payment limit included in such file with respect to such code; and (II) the number of units (as specified under paragraph (2))\u2014 (aa) billed with respect to such code for a date of service in 2023; and (bb) listed in the CMS Integrated Data Repository for Part B (Carrier & DME) claims data; (ii) calculating the sum of all amounts determined under clause (i); and (iii) dividing the sum calculated under clause (ii) by the total number of units determined under clause (i)(II). .\n**(2) Conforming amendments**\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a)(1) ) is amended\u2014\n**(A)**\nin subparagraph (S)(i), by striking subject to subparagraph (EE) and inserting subject to subparagraphs (EE) and (II) ;\n**(B)**\nby striking and (HH) and inserting (HH) ; and\n**(C)**\nby inserting , and (II) with respect to skin substitute products under section 1861(s)(2)(KK), the amount paid shall be 80 percent of the lesser of the actual charge or the payment amount established under section 1847A(b)(9) before the semicolon at the end.\n##### (c) Skin substitute product defined\nSection 1847A(c)(6) of the Social Security Act (42 U.S.C. 1395w\u20133a(c)(6)) is amended by adding at the end the following:\n(J) Skin substitute products The term skin substitute product \u2014 (i) means a cellular, tissue, biological or synthetic material that\u2014 (I) is applied to a wound and intended to remain within the wound bed; and (II) is marketed pursuant to section 510(k), 513(f)(2), or 515 of the Federal Food, Drug, and Cosmetic Act, or section 361 of the Public Health Service Act; and (ii) does not include\u2014 (I) a product that is intended to temporarily protect or cover the wound bed and be removed before complete resorption (such as a dressing); or (II) a liquid, gel, powder, or other similarly constituted item. .\n##### (d) Exclusion from reporting requirements\nSection 1847A(f)(2)(A) of the Social Security Act (42 U.S.C. 1395w\u20133a(f)(2)(A)) is amended by inserting (except that, beginning January 1, 2026, a drug or biological so described does not include a skin substitute product (as defined in subsection (c)(6)(J))) after products that are payable under this part as a drug or biological .\n##### (e) Consolidated billing and payment code\nNot later than January 1, 2026, the Secretary of Health and Human Services shall establish a new billing and payment code for all skin substitute products (as defined in subparagraph (J) of section 1847A(c)(6) of the Social Security Act (42 U.S.C. 1395w\u20133a(c)(6)), as added by subsection (b)).\n#### 3. Enhancing program integrity for skin substitute products\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395m ) is amended by adding at the end the following new subsection:\n(aa) Special payment rules for skin substitute products (1) Identification of outlier providers of skin substitute products (A) In general Not later than December 1, 2025, and every 2 years thereafter through December 1, 2035, the Secretary shall determine the 3 percent of the total number of providers of skin substitute products that are outlier providers of skin substitute products. (B) Outlier providers of skin substitute products The determination of an outlier provider of skin substitute products under this paragraph shall be based upon the providers (as identified by national provider identification number) that received the greatest total payment under this title for skin substitute products furnished in the year preceding the year in which the determination under subparagraph (A) is made. (C) Referral to oig The Secretary shall\u2014 (i) make publicly available the list of outlier providers of skin substitute products identified under each determination under subparagraph (A); and (ii) transmit such list to the Inspector General of the Department of Health and Human Services for the assessment of potential fraud, waste, or abuse. (2) Initial prepayment claim review for certain outlier providers (A) In general Beginning January 1, 2026, the Secretary shall conduct prepayment review of claims for skin substitute products submitted under this title by an outlier provider of skin substitute products unless 1 or more of the conditions described in subparagraph (B) is met with respect to such provider. (B) Limitation For purposes of subparagraph (A), the conditions described in this subparagraph are, with respect to an outlier provider of skin substitute products, the following: (i) Skin substitute products furnished by the provider are subject to prior authorization under paragraph (3). (ii) The rate of approval for claims for skin substitute products furnished by such provider that are subject to prepayment review under this paragraph exceeds 90 percent (as determined over a period of time or number of claims specified by the Secretary). (iii) The Secretary determines that the billing practices of the provider are consistent with the applicable coverage criteria and requirements under this title. (3) Prior authorization for outlier providers of skin substitute products (A) In general Beginning not later than January 1, 2027, subject to subparagraph (B), the Secretary shall, for a period determined appropriate by the Secretary, apply prior authorization for skin substitute products that are furnished by an outlier provider of skin substitute products identified under paragraph (1). (B) Removal from prior authorization In the event that the Secretary determines, with respect to an outlier provider of skin substitute products, that the rate of approval for requests for prior authorization under this paragraph for skin substitute products furnished by such provider exceeds 90 percent (as determined over a period of time or number of claims specified by the Secretary), the Secretary shall cease to apply prior authorization under this paragraph for skin substitute products furnished by such provider. (C) Funding For purposes of carrying out this paragraph, the Secretary shall provide for the transfer, from the Federal Supplementary Medical Insurance Trust Fund under section 1841, to the Centers for Medicare & Medicaid Services Program Management Account, of $5,000,000 for each of fiscal years 2027 through 2030, to remain available until expended. (4) Enrollment revocation or exclusion of noncompliant outlier providers (A) In general Beginning January 1, 2028, if the rate of denial for requests for prior authorization under paragraph (3) for skin substitute products furnished by an outlier provider of skin substitute products exceeds 75 percent over a period of 6 or more consecutive months, the Secretary shall determine that an abuse of billing privileges exists with respect to such provider for purposes of section 424.535(a)(8)(ii) of title 42, Code of Federal Regulations. (B) Referral for exclusion If the Secretary determines under subparagraph (A) that an abuse of billing privileges exists with respect to an outlier provider of skin substitute products, the Secretary shall direct the Inspector General of the Department of Health and Human Services to determine whether such provider should be excluded from participation in any Federal health care program under section 1128(b)(6). (5) Medicare coverage criteria for skin substitute products Any skin substitute product defined in section 1847A(c)(6)(J) of the Social Security Act and furnished during 2026 shall be subject to the same coverage criteria when determining whether the skin substitute product is covered under section 1862(a)(1)(A), unless such product is determined by the Secretary to be unsafe based on evidence of contamination, serious infectious disease, or serious adverse reactions caused by the product. Neither the Secretary nor any Medicare administrative contractor may determine, including through a determination made pursuant to the prepayment review program or prior authorization program described in paragraphs (2) and (3), that a specific skin substitute product furnished in 2026 is not covered by Medicare based solely on analysis of the clinical evidence relating to that skin substitute product. (6) Skin substitute product defined In this subsection, the term skin substitute product has the meaning given such term in section 1847A(c)(6)(J). .",
      "versionDate": "2025-10-17",
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
        "updateDate": "2025-12-08T16:40:05Z"
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
      "date": "2025-10-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5768ih.xml"
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
      "title": "Skin Substitute Access and Payment Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-22T10:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Skin Substitute Access and Payment Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T10:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to adjust payment for skin substitute products under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-22T10:48:11Z"
    }
  ]
}
```
