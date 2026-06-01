# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5526?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5526
- Title: Biosimilar Red Tape Elimination Act
- Congress: 119
- Bill type: HR
- Bill number: 5526
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2026-05-22T08:07:27Z
- Update date including text: 2026-05-22T08:07:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-19: Introduced in House

## Actions

- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5526",
    "number": "5526",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Biosimilar Red Tape Elimination Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:27Z",
    "updateDateIncludingText": "2026-05-22T08:07:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-19",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T13:03:00Z",
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "OH"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "MA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "TX"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NM"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "UT"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "FL"
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
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5526ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5526\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Mr. Pfluger (for himself and Mr. Landsman ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo improve the requirements for making a determination of interchangeability of a biological product and its reference product.\n#### 1. Short title\nThis Act may be cited as the Biosimilar Red Tape Elimination Act .\n#### 2. Biosimilar biological products\n##### (a) In general\nSection 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ) is amended\u2014\n**(1)**\nin the subsection heading, by striking or interchangeable ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking subparagraph (B);\n**(B)**\nby redesignating clauses (ii) and (iii) of subparagraph (A) as subparagraphs (B) and (C), respectively, and adjusting the margins accordingly;\n**(C)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (i), by redesignating subclauses (I) through (V) as clauses (i) through (v), respectively, and adjusting the margins accordingly;\n**(ii)**\nin clause (i), as so redesignated by clause (i) of this subparagraph, by redesignating items (aa) through (cc) as subclauses (I) through (III), respectively, and adjusting the margins accordingly;\n**(iii)**\nin subclause (II) of clause (i), as so redesignated by clause (ii) of this subparagraph, by striking item (aa) or (cc) and inserting subclause (I) or (III) ; and\n**(iv)**\nby striking (A) In General and all that follows through An application submitted under this subsection shall include information and inserting the following:\n(A) In general An application submitted under this subsection shall include information ;\n**(D)**\nin subparagraph (B), as so redesignated by subparagraph (B) of this paragraph, by striking clause (i)(I) and inserting subparagraph (A)(i) ; and\n**(E)**\nin subparagraph (C), as so redesignated by subparagraph (B) of this paragraph, by redesignating subclauses (I) through (III) as clauses (i) through (iii), respectively, and by adjusting the margins accordingly;\n**(3)**\nby amending subparagraph (A) of paragraph (3) to read as follows:\n(A) the Secretary determines that the information submitted in the application (or the supplement) is sufficient to show that the biological product is biosimilar to the reference product; and ;\n**(4)**\nby amending paragraph (4) to read as follows:\n(4) Interchangeability (A) In general A biological product licensed under this subsection shall be deemed to be interchangeable with the reference product, subject to subparagraph (B). (B) Timing of deemed interchangeability (i) Licensure on or after transition date A biological product licensed under this subsection on or after the transition date described in subparagraph (C) (referred to in this clause as the applicable biological product ) shall be deemed to be interchangeable with the reference product upon such licensure, unless the applicable biological product relied on the same reference product as another biological product for which\u2014 (I) licensure under this subsection was in effect on the day before the date of enactment of the Biosimilar Red Tape Elimination Act ; and (II) a first interchangeable exclusivity period under paragraph (6) (as in effect on the day before the date of enactment of the Biosimilar Red Tape Elimination Act ) is in effect on the date of licensure of the applicable biological product, in which case the applicable biological product shall be deemed interchangeable with the reference product under this paragraph on the date on which the exclusivity period described in subclause (II) ends. (ii) Licensure prior to transition date A biological product licensed under this subsection prior to the transition date described in subparagraph (C) (referred to in this clause as the applicable biological product ) shall be deemed to be interchangeable with the reference product on such transition date, unless the applicable biological product relied on the same reference product as another biological product for which\u2014 (I) licensure under this subsection was in effect on the day before the date of enactment of the Biosimilar Red Tape Elimination Act ; and (II) a first interchangeable exclusivity period under paragraph (6) (as in effect on the day before the date of enactment of the Biosimilar Red Tape Elimination Act ) is in effect on the transition date, in which case the applicable biological product shall be deemed interchangeable with the reference product under this paragraph on the date on which the exclusivity period described in subclause (II) ends. (C) Transition date The transition date described in this subparagraph is the date that is 60 days after the date of enactment of the Biosimilar Red Tape Elimination Act . ;\n**(5)**\nby amending paragraph (6) to read as follows:\n(6) Transition with respect to preserving first interchangeable exclusivity with respect to certain biological products With respect to a biological product licensed under this subsection before the date of enactment of the Biosimilar Red Tape Elimination Act , for which there was an unexpired period of first interchangeable exclusivity under this subsection (as then in effect), such unexpired exclusivity period shall remain in effect for the duration of such period. ; and\n**(6)**\nin paragraph (8)(D)\u2014\n**(A)**\nin clause (i), by striking class; and and inserting class. ;\n**(B)**\nby striking clause (ii); and\n**(C)**\nby striking description of\u2014 and all that follows through criteria that the Secretary and inserting description of the criteria that the Secretary .\n##### (b) Conforming amendments\n**(1)**\nSection 351(i)(3) of the Public Health Service Act ( 42 U.S.C. 262(i)(3) ) is amended by striking that is shown to meet the standards described in subsection (k)(4) and inserting licensed under subsection (k) .\n**(2)**\nSection 352A of the Public Health Service Act ( 42 U.S.C. 263\u20131 ) is amended by striking and interchangeable biosimilar biological products each place it appears.\n**(3)**\nSection 744G(14) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201351(14) ) is amended by striking , including a supplement requesting that the Secretary determine that the biosimilar biological product meets the standards for interchangeability described in section 351(k)(4) of the Public Health Service Act .\n**(4)**\nSection 505B(l) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355c(l) ) to read as follows:\n(l) Biosimilar biological products A biological product for which an application is submitted under section 351(k) of the Public Health Service Act shall not be considered to have a new active ingredient for purposes of this section, unless the application seeks licensure for\u2014 (1) a claimed indication that has been approved for the reference product in a relevant pediatric population or for which there is a deferral of the pediatric assessment under paragraph (4) for the reference product; and (2) the assessment would not involve the development of a biological product with a strength, dosage form, route of administration, or condition of use that could not be licensed under section 351(k) of the Public Health Service Act. .\n##### (c) Guidance\nThe Secretary shall\u2014\n**(1)**\nnot later than 18 months after the date of enactment of this Act, update existing draft and final guidance to reflect the amendments made by this Act, including by revising or revoking the guidance document titled Considerations in Demonstrating Interchangeability With a Reference Product (May 2019) and Considerations in Demonstrating Interchangeability With a Reference Product: Update (June 2024);\n**(2)**\nnot later than 18 months after the date of enactment of this Act, issue or revise guidance on review and approval of biosimilar biological products under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ) relating to the data and information that an applicant is required to submit to support a determination that a biosimilar biological product that is the subject of an application under such section is biosimilar to the reference product (as defined in section 351(i) of such Act ( 42 U.S.C. 262(i) )); and\n**(3)**\nnot later than 18 months after the comment period closes on the guidance under paragraphs (1) and (2), issue revised draft or final versions of such guidances.\n##### (d) Rules of construction\nThe amendments made by this section shall not be construed\u2014\n**(1)**\nto alter the standard or the information required for licensure of a biological product as biosimilar to a reference product pursuant to section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ); or\n**(2)**\nto limit the information that may be required by the Secretary of Health and Human Services to support the licensure of a biological product as biosimilar to a reference product pursuant to such section.",
      "versionDate": "2025-09-19",
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
        "actionDate": "2025-06-04",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1954",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Biosimilar Red Tape Elimination Act",
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
        "updateDate": "2025-12-17T16:43:53Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5526ih.xml"
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
      "title": "Biosimilar Red Tape Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Biosimilar Red Tape Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve the requirements for making a determination of interchangeability of a biological product and its reference product.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T04:48:27Z"
    }
  ]
}
```
