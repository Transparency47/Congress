# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4323?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4323
- Title: Ensuring Access to Lower-Cost Medicines for Seniors Act
- Congress: 119
- Bill type: S
- Bill number: 4323
- Origin chamber: Senate
- Introduced date: 2026-04-16
- Update date: 2026-05-18T19:29:17Z
- Update date including text: 2026-05-18T19:29:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-04-16: Introduced in Senate
- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-04-16: Introduced in Senate

## Actions

- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4323",
    "number": "4323",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Ensuring Access to Lower-Cost Medicines for Seniors Act",
    "type": "S",
    "updateDate": "2026-05-18T19:29:17Z",
    "updateDateIncludingText": "2026-05-18T19:29:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
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
        "item": {
          "date": "2026-04-16T18:59:59Z",
          "name": "Referred To"
        }
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4323is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4323\nIN THE SENATE OF THE UNITED STATES\nApril 16 (legislative day, April 14), 2026 Mr. Lankford (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to require PDP sponsors of a prescription drug plan and Medicare Advantage organizations offering an MA\u2013PD plan under part D of the Medicare program that use a formulary to include certain generic drugs and biosimilar biological products on such formulary, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring Access to Lower-Cost Medicines for Seniors Act .\n#### 2. Requirements for PDP sponsors of prescription drug plans and Medicare advantage organizations offering MA\u2013PD plans under part D of the Medicare program that use formularies\n##### (a) In general\nSection 1860D\u20134(b)(3) of the Social Security Act ( 42 U.S.C. 1395w\u2013104(b)(3) ) is amended by adding at the end the following new subparagraphs:\n(J) Required inclusion of certain generic drugs and biosimilar biological products (i) In general Subject to the succeeding provisions of this subparagraph, with respect to a plan year beginning on or after January 1, 2028, the following rules shall apply: (I) If the formulary includes a part D reference drug, the formulary shall include each part D generic drug of such part D reference drug for which the wholesale acquisition cost is less than the wholesale acquisition cost of such part D reference drug. (II) If the formulary includes a part D reference biological product, the formulary shall include at least one part D biosimilar biological of such part D reference biological product for which the wholesale acquisition cost is less than the wholesale acquisition cost of such part D reference biological product (if one or more such part D biosimilar biologicals is available). (ii) Determinations and implementation Determinations of part D generic drugs and part D biosimilar biological products described in subclauses (I) and (II) of clause (i) and implementation of formulary requirements under clause (i) shall be made by PDP sponsors offering prescription drug plans in accordance with uniform requirements established by the Secretary (by program instruction or otherwise), which shall provide for such determinations to be made as of specified dates (in the case of determinations during a plan year, on a quarterly basis), and for any associated formulary changes to be implemented promptly thereafter (in accordance with timeframes specified by the Secretary). Such uniform requirements shall also specify circumstances under which a part D generic drug or part D biosimilar biological product shall be deemed for purposes of subclauses (I) and (II) of clause (i) to have a lower wholesale acquisition cost than its part D reference drug or part D reference biological product (so as to require its inclusion on formularies), including where no wholesale acquisition cost is published for such part D reference drug or part D reference biological product or the part D reference drug or part D reference biological product is not available for purchase by the PDP sponsor (or its network pharmacies) from its manufacturer at the published wholesale acquisition cost. (iii) Prohibition on certain limits on access The PDP sponsor offering the prescription drug plan may not impose limits on access to a part D generic drug required to be included on the formulary under clause (i)(I) or a part D biosimilar biological product required to be included on the formulary under clause (i)(II), including through prior authorization, utilization management, or step therapy, that are more restrictive than any such limits imposed on access to the part D reference drug of such part D generic drug or part D reference biological product of such part D biosimilar biological product, respectively, or that otherwise have the effect of giving preferred status to such part D reference drug or part D reference biological product over such part D generic drug or part D biosimilar biological product, respectively. (iv) Definitions In this subparagraph and subparagraph (K): (I) Part D biosimilar biological product The term part D biosimilar biological product means a covered part D drug that is a biosimilar biological product (as defined in section 1847A(c)(6)(H)). (II) Part D generic drug The term part D generic drug means a covered part D drug that is approved under section 505(j) of the Federal Food, Drug, and Cosmetic Act. (III) Part D reference biological product The term part D reference biological product means a covered part D drug that is a reference biological product (as defined in section 1847A(c)(6)(I)). (IV) Part D reference drug The term part D reference drug means, with respect to a part D generic drug, a covered part D drug that is the listed drug (as described in clause (i) of section 505(j)(2)(A) of the Federal Food, Drug, and Cosmetic Act) that is referred to in the abbreviated application for such part D generic drug under such section. (V) Wholesale acquisition cost The term wholesale acquisition cost has the meaning given such term in section 1847A(c)(6)(B). (K) Cost-Sharing tiering requirements with respect to part D generic drugs and part D biosimilar biological products (i) Generic drug and biosimilar biological product cost-sharing tier With respect to a plan year beginning on or after January 1, 2028, if the PDP sponsor offering the prescription drug plan applies tiered cost-sharing (through copayment or coinsurance tiers) to covered part D drugs on a formulary, the PDP sponsor shall\u2014 (I) have at least one cost-sharing tier on the formulary that only includes part D generic drugs and part D biosimilar biological products; and (II) with respect to each cost-sharing tier described in subclause (I) on the formulary, either apply no cost-sharing requirement or a copayment that is\u2014 (aa) in the case where the lowest branded drug tier of such formulary bases cost-sharing on a copayment amount, an amount at least $20 lower than the copayment for such lowest branded drug tier (but in no case may such copayment amount be less than zero); or (bb) in the case where the lowest branded drug tier of such formulary bases cost-sharing on a coinsurance percentage, an amount at least $20 lower than the actuarially expected average cost-sharing amount payable for the covered part D drugs included on such lowest branded drug tier, determined using processes and methods established under section 1860D\u201311(c) (but in no case may such copayment amount be less than zero). (ii) Specialty generic drug and biosimilar biological product cost-sharing tier With respect to a plan year beginning on or after January 1, 2028, if the PDP sponsor offering the prescription drug plan has a specialty tier, the PDP sponsor shall\u2014 (I) have a second specialty tier on such formulary that only includes part D generic drugs and part D biosimilar biological products\u2014 (aa) for which the cost (as defined by the Secretary) is greater than a cost threshold specified by the Secretary; and (bb) with respect to which the part D reference drug for such a part D generic drug or the part D reference biological product for such a part D biosimilar biological product is either included on a cost-sharing tier on such formulary with a cost-sharing requirement that is greater than the cost-sharing requirement applied under subclause (II), or excluded from such formulary; and (II) apply a coinsurance cost-sharing requirement with respect to the cost-sharing tier required for the formulary under subclause (I) that is at least 5 percentage points lower than the coinsurance percentage applicable to any other specialty tier of the formulary. (iii) Placement of certain generic drugs and biosimilar biological products Each part D generic drug and each part D biosimilar biological product required to be included on the formulary under subparagraph (J)(i) shall be included either on a cost-sharing tier described in clause (i)(I) or, if applicable, the cost-sharing tier required for the formulary under clause (ii)(I). (iv) Application (I) In general The requirements under clauses (i) through (iii) shall, subject to the requirements under section 1860D\u201314, apply after the individual has satisfied any deductible under subsections (a)(2)(A)(i) or (b)(1) of section 1860D\u20132. (II) Limitation The Secretary shall not approve any benefit design for a prescription drug plan or an MA\u2013PD plan to which the requirements of this subparagraph apply if such benefit design has any deductible applicable to any part D generic drug or part D biosimilar biological product unless such deductible, or a greater deductible, also applies to all other covered part D drugs on the formulary of such plan (subject to the requirements under section 1860D\u201314), except for lesser or zero deductibles applicable only to particular types of covered part D drugs which the Secretary determines warrant favorable cost-sharing when such lesser or zero deductibles are also applicable to part D generic drugs and part D biosimilar biological products of the given type. (v) Definitions In this subparagraph: (I) Brand drug The term brand drug means a covered part D drug that is approved under section 505(c) of the Federal Food, Drug, and Cosmetic Act or licensed under section 351(a) of the Public Health Service Act. (II) Lowest branded drug tier The term lowest branded drug tier means the cost-sharing tier of a formulary which includes at least 1 brand drug and provides for the lowest level of cost sharing applicable to any such tier, as determined by the Secretary. (III) Specialty tier The term specialty tier means a cost-sharing tier consisting only of covered part D drugs that have a cost (as defined by the Secretary) which equals or exceeds an applicable cost threshold established by the Secretary for high-cost covered part D drugs to be eligible for inclusion on such cost-sharing tier. .\n##### (b) Conforming amendments\nSection 1860D\u20132 of the Social Security Act ( 42 U.S.C. 1395w\u2013102 ) is amended\u2014\n**(1)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (A), by striking and paragraphs (8) and (9) and inserting , paragraphs (8) and (9), and section 1860D\u20134(b)(3)(K) ; and\n**(B)**\nin subparagraph (B), by inserting before the period the following: and section 1860D\u20134(b)(3)(K) ; and\n**(2)**\nin subsection (c), by adding at the end the following new paragraph:\n(7) Treatment of cost-sharing for part D generic drugs and part D biosimilar biological products The coverage is provided in accordance with section 1860D\u20134(b)(3)(K). .",
      "versionDate": "2026-04-16",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-05-12T20:29:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-16",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s4323",
          "measure-number": "4323",
          "measure-type": "s",
          "orig-publish-date": "2026-04-16",
          "originChamber": "SENATE",
          "update-date": "2026-05-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4323v00",
            "update-date": "2026-05-18"
          },
          "action-date": "2026-04-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Ensuring Access to Lower-Cost Medicines for Seniors Act</strong></p><p>This bill requires prescription drug plans under the Medicare prescription drug benefit to include generic drugs and biosimilars on their formularies.</p><p>Specifically, the bill requires plans that use formularies to include generic drugs and biosimilars on the formularies and without any requirements (e.g., prior authorization requirements) that are more restrictive as compared to those for brand-name drugs and biologics. Plans that use cost-sharing tiers must also have specific tiers for generic drugs and biosimilars, in accordance with certain limitations.</p>"
        },
        "title": "Ensuring Access to Lower-Cost Medicines for Seniors Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4323.xml",
    "summary": {
      "actionDate": "2026-04-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ensuring Access to Lower-Cost Medicines for Seniors Act</strong></p><p>This bill requires prescription drug plans under the Medicare prescription drug benefit to include generic drugs and biosimilars on their formularies.</p><p>Specifically, the bill requires plans that use formularies to include generic drugs and biosimilars on the formularies and without any requirements (e.g., prior authorization requirements) that are more restrictive as compared to those for brand-name drugs and biologics. Plans that use cost-sharing tiers must also have specific tiers for generic drugs and biosimilars, in accordance with certain limitations.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119s4323"
    },
    "title": "Ensuring Access to Lower-Cost Medicines for Seniors Act"
  },
  "summaries": [
    {
      "actionDate": "2026-04-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ensuring Access to Lower-Cost Medicines for Seniors Act</strong></p><p>This bill requires prescription drug plans under the Medicare prescription drug benefit to include generic drugs and biosimilars on their formularies.</p><p>Specifically, the bill requires plans that use formularies to include generic drugs and biosimilars on the formularies and without any requirements (e.g., prior authorization requirements) that are more restrictive as compared to those for brand-name drugs and biologics. Plans that use cost-sharing tiers must also have specific tiers for generic drugs and biosimilars, in accordance with certain limitations.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119s4323"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4323is.xml"
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
      "title": "Ensuring Access to Lower-Cost Medicines for Seniors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Access to Lower-Cost Medicines for Seniors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to require PDP sponsors of a prescription drug plan and Medicare Advantage organizations offering an MA-PD plan under part D of the Medicare program that use a formulary to include certain generic drugs and biosimilar biological products on such formulary, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:40Z"
    }
  ]
}
```
