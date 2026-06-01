# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2756?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2756
- Title: Affordable Inhalers and Nebulizers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2756
- Origin chamber: Senate
- Introduced date: 2025-09-10
- Update date: 2026-02-04T12:03:15Z
- Update date including text: 2026-02-04T12:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in Senate
- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-10: Introduced in Senate

## Actions

- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2756",
    "number": "2756",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "A000382",
        "district": "",
        "firstName": "Angela",
        "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
        "lastName": "Alsobrooks",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Affordable Inhalers and Nebulizers Act of 2025",
    "type": "S",
    "updateDate": "2026-02-04T12:03:15Z",
    "updateDateIncludingText": "2026-02-04T12:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
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
            "date": "2025-09-10T16:55:42Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-10T16:55:42Z",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MD"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2756is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2756\nIN THE SENATE OF THE UNITED STATES\nSeptember 10, 2025 Ms. Alsobrooks (for herself and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XXVII of the Public Health Service Act, the Internal Revenue Code of 1986, and the Employee Retirement Income Security Act of 1974 to reduce patient cost-sharing for prescription drug inhaler products used to treat breathing disorders such as asthma and chronic obstructive pulmonary disease, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Affordable Inhalers and Nebulizers Act of 2025 .\n#### 2. Reducing patient cost-sharing for prescription drug inhaler products used to treat breathing disorders such as asthma and chronic obstructive pulmonary disease\n##### (a) Coverage and cost-Sharing requirements\n**(1) Private insurance**\n**(A) PHSA**\nPart D of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111 et seq. ) is amended by adding at the end the following new section:\n2799A\u201311. Coverage and cost-sharing requirements for specified inhaler products (a) In general A group health plan, and a health insurance issuer offering group or individual health insurance coverage, shall provide benefits under such plan or coverage (as applicable) for all specified inhaler products and, with respect to such a product, may not\u2014 (1) apply any deductible; or (2) impose any cost-sharing requirement in excess of $15 per 30-day supply of such product. (b) Counting cost-Sharing towards deductible and out-of-Pocket maximum A group health plan, and a health insurance issuer offering group or individual health insurance coverage, shall count any cost-sharing requirement described in subsection (a)(2) incurred by a participant, beneficiary, or enrollee of such plan or coverage with respect to a specified inhaler product towards any out-of-pocket maximum and any deductible that, but for application of subsection (a), would have applied to such participant, beneficiary, or enrollee with respect to such product. (c) Specified inhaler product defined For purposes of this section, the term specified inhaler product means any maintenance or reliever or rescue inhalation drug (including inhalation aerosols, metered dose inhalers, dry powder inhalers, inhalation solutions, bronchodilators, and corticosteroids) with a medically accepted indication (as defined in section 1927(k)(6) of the Social Security Act) for the treatment for lung diseases such as asthma and chronic obstructive pulmonary disease. Such term includes any equipment used in the administration of such drug (such as masks and tubing, spacers, nebulizers, and valve-holding chambers). .\n**(B) IRC**\n**(i) In general**\nSubchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n9826. Coverage and cost-sharing requirements for specified inhaler products (a) In general A group health plan shall provide benefits under such plan for all specified inhaler products and, with respect to such a product, may not\u2014 (1) apply any deductible; or (2) impose any cost-sharing requirement in excess of $15 per 30-day supply of such product. (b) Counting cost-Sharing towards deductible and out-of-Pocket maximum A group health plan shall count any cost-sharing requirement described in subsection (a)(2) incurred by a participant or beneficiary of such plan with respect to a specified inhaler product towards any out-of-pocket maximum and any deductible that, but for application of subsection (a), would have applied to such participant or beneficiary with respect to such product. (c) Specified inhaler product defined For purposes of this section, the term specified inhaler product means any maintenance or reliever or rescue inhalation drug (including inhalation aerosols, metered dose inhalers, dry powder inhalers, inhalation solutions, bronchodialators, and corticosteroids) with a medically accepted indication (as defined in section 1927(k)(6) of the Social Security Act ( 42 U.S.C. 13964\u20138(k)(6) )) for the treatment of asthma or of chronic obstructive pulmonary disease. Such term includes any equipment used in the administration of such drug (such as masks and tubing, spacers, nebulizers, and valve-holding chambers). .\n**(ii) Clerical amendment**\nThe table of sections for subchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 9826. Coverage and cost-sharing requirements for specified inhaler products. .\n**(C) ERISA**\n**(i) In general**\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 is amended by adding at the end the following new section:\n726. Coverage and cost-sharing requirements for specified inhaler products (a) In general A group health plan, and a health insurance issuer offering group health insurance coverage, shall provide benefits under such plan or coverage (as applicable) for all specified inhaler products and, with respect to such a product, may not\u2014 (1) apply any deductible; or (2) impose any cost-sharing requirement in excess of $15 per 30-day supply of such product. (b) Counting cost-Sharing towards deductible and out-of-Pocket maximum A group health plan, and a health insurance issuer offering group health insurance coverage, shall count any cost-sharing requirement described in subsection (a)(2) incurred by a participant or beneficiary of such plan with respect to a specified inhaler product towards any out-of-pocket maximum and any deductible that, but for application of subsection (a), would have applied to such participant or beneficiary with respect to such product. (c) Specified inhaler product defined For purposes of this section, the term specified inhaler product means any maintenance or reliever or rescue inhalation drug (including inhalation aerosols, metered dose inhalers, dry powder inhalers, inhalation solutions, bronchodialators, and corticosteroids) with a medically accepted indication (as defined in section 1927(k)(6) of the Social Security Act ( 42 U.S.C. 13964\u20138(k)(6) )) for the treatment of asthma or of chronic obstructive pulmonary disease. Such term includes any equipment used in the administration of such drug (such as masks and tubing, spacers, nebulizers, and valve-holding chambers). .\n**(ii) Clerical amendment**\nThe table of contents in section 1 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 note) is amended by inserting after the item relating to section 725 the following new item:\nSec. 726. Coverage and cost-sharing requirements for specified inhaler products. .\n**(D) Conforming amendments**\n**(i) HDHP safe harbor**\nSection 223(c)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(I) Safe harbor for absence of deductible for specified inhaler products For plan years beginning on or after January 1, 2026, a plan shall not fail to be treated as a high deductible health plan by reason of failing to have a deductible for specified inhaler products (as defined in section 2799A\u201311 of the Public Health Service Act). .\n**(ii) Catastrophic plan safe harbor**\nSection 1302(e)(1)(B)(i) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18022(e)(1)(B)(i) ) is amended by inserting or 2799A\u201311 of the Public Health Service Act after section 2713 .\n**(E) Effective date**\nThe amendments made by this paragraph shall apply to plan years beginning on or after January 1, 2026.\n**(2) Medicare**\n**(A) Part B**\nSection 1833 of the Social Security Act ( 42 U.S.C. 1395l ) is amended\u2014\n**(i)**\nin subsection (a)(1)(S)\u2014\n**(I)**\nin clause (i), by inserting or (iii) after clause (ii) ; and\n**(II)**\nby adding at the end the following new clause: and (iii) with respect to a specified inhaler product (as defined in section 2799A\u201311 of the Public Health Service Act) furnished on or after January 1, 2026, the amounts paid shall be 100 percent of the lesser of the actual charge or the payment amount established in section 1842(o) (or, if applicable, under section 1847, 1847A, or 1847B), less, per 30-day supply of such product, $15, ; and\n**(ii)**\nin subsection (b), in the first sentence\u2014\n**(I)**\nin paragraph (12), by striking , and ; and\n**(II)**\nby striking .. and inserting , and (14) such deductible shall not apply with respect to a specified inhaler product (as defined in section 2799A\u201311 of the Public Health Service Act) furnished on or after January 1, 2026. .\n**(B) Part D**\n**(i) In general**\nSection 1860D\u20132(b) of the Social Security Act ( 42 U.S.C. 1395w\u2013102(b) ) is amended\u2014\n**(I)**\nin paragraph (1)(A), by striking paragraphs (8) and (9) and inserting paragraphs (8), (9), and (10) ;\n**(II)**\nin paragraph (2)(A), by striking paragraphs (8) and (9) and inserting paragraphs (8), (9), and (10) ;\n**(III)**\nin paragraph (4)(A)(i), by striking paragraphs (8) and (9) and inserting paragraphs (8), (9), and (10) ; and\n**(IV)**\nby adding at the end the following new paragraph:\n(10) Treatment of cost-sharing for specified inhaler products (A) No application of deductible For plan year 2026 and subsequent plan years, the deductible under paragraph (1) shall not apply with respect to any specified inhaler product. (B) Application of cost-sharing For plan year 2026 and subsequent plan years, the coverage provides benefits for any specified inhaler product with cost-sharing for a month\u2019s supply that does not exceed $15. (C) Definition For purposes of this paragraph, the term specified inhaler product has the meaning given such term in section 2799A\u201311 of the Public Health Service Act. .\n**(ii) Conforming amendment for alternative prescription drug coverage**\nSection 1860D\u20132(c) of the Social Security Act ( 42 U.S.C. 1395w\u2013102(c) ) is amended by adding at the end the following new paragraph:\n(7) Treatment of cost-sharing for specified insulin products The coverage in provided in accordance with subsection (b)(10). .\n**(iii) Conforming amendments to cost-sharing for low-income individuals**\nSection 1860D\u201314(a)(1) of the Social Security Act ( 42 U.S.C. 1395w\u2013114(a)(1) ) is amended\u2014\n**(I)**\nin subparagraph (D)(iii), by adding at the end the following new sentence: For plan year 2026 and subsequent plan years, the copayment amount applicable under the preceding sentence to a month's supply of a specified inhaler product (as defined in section 1860D\u20132(b)(10)) dispensed to the individual may not exceed $15. ; and\n**(II)**\nin subparagraph (E), by inserting or under section 1860D\u20132(b)(10) in the case of a specified inhaler product (as defined in such section) after (as defined in subparagraph (C) of such section) .\n##### (b) Payment program for uninsured individuals\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following new section:\n399V\u20138. Specified inhaler product payment program (a) In general Beginning January 1, 2026, the Secretary shall establish a program under which\u2014 (1) program-registered providers submit claims to the Secretary with respect to the furnishing of specified inhaler products (as defined in subsection (b)) to uninsured individuals; and (2) the Secretary, subject to the availability of appropriations, pays each such provider for such products in an amount determined appropriate by the Secretary. (b) Definitions In this section: (1) Program-registered provider The term program-registered provider means a health care provider that\u2014 (A) is licensed or otherwise authorized to administer or dispense specified inhaler products in the State in which such provider so administers or dispenses such products under the program established under this section; and (B) enters into an agreement with the Secretary under which the provider agrees not to hold an uninsured individual liable for the cost of any such product administered or dispensed to such individual in an amount exceeding $15 for a month\u2019s supply of such product if a payment is made under subsection (a)(2) with respect to such product so administered or dispensed. (2) Specified inhaler product The term specified inhaler product has the meaning given such term in section 2799A\u201311. (3) Uninsured individual The term uninsured individual means, with respect to an individual furnished a specified inhaler product, an individual who is not enrolled in\u2014 (A) a Federal health care program (as defined in section 1128B(f) of the Social Security Act); (B) a group health plan or health insurance coverage offered by a health insurance issuer in the group or individual market (as such terms are defined in section 2791); or (C) a health plan offered under chapter 89 of title 5, United States Code. .\n##### (c) Implementation\nThe Secretary of Health and Human Services may implement the amendments made by this section by program instruction, subregulatory guidance, or otherwise.",
      "versionDate": "2025-09-10",
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
        "actionDate": "2025-09-10",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5278",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Affordable Inhalers and Nebulizers Act of 2025",
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
        "updateDate": "2025-09-23T16:50:30Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2756is.xml"
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
      "title": "Affordable Inhalers and Nebulizers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Affordable Inhalers and Nebulizers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XXVII of the Public Health Service Act, the Internal Revenue Code of 1986, and the Employee Retirement Income Security Act of 1974 to reduce patient cost-sharing for prescription drug inhaler products used to treat breathing disorders such as asthma and chronic obstructive pulmonary disease, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:22Z"
    }
  ]
}
```
