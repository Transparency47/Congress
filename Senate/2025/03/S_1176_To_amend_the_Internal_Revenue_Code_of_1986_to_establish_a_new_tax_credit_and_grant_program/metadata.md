# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1176?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1176
- Title: Healthy Food Access for All Americans Act
- Congress: 119
- Bill type: S
- Bill number: 1176
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2025-12-05T21:47:14Z
- Update date including text: 2025-12-05T21:47:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1176",
    "number": "1176",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Healthy Food Access for All Americans Act",
    "type": "S",
    "updateDate": "2025-12-05T21:47:14Z",
    "updateDateIncludingText": "2025-12-05T21:47:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T16:33:56Z",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "WV"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MD"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1176is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1176\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Mr. Warner (for himself, Mrs. Capito , Mr. Van Hollen , and Mr. Moran ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a new tax credit and grant program to stimulate investment and healthy nutrition options in food deserts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthy Food Access for All Americans Act .\n#### 2. Tax credit and grant program for Special Access Food Providers\n##### (a) In general\n**(1) Allowance of credit**\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Special Access Food Provider Credit and Grant Program (a) Establishment of credit for grocery stores (1) In general For purposes of section 38, the special access food provider credit determined under this section for any taxable year is an amount equal to the lesser of\u2014 (A) the amount of the allocation received by the taxpayer under subsection (d)(1)(A), or (B) the amount equal to\u2014 (i) in the case of a qualified grocery store which is placed in service during such taxable year by a taxpayer which has been certified as a special access food provider, 15 percent of the basis of such grocery store, including any property used in the operation of such grocery store\u2014 (I) which is acquired by the taxpayer if the original use of such property commences with the taxpayer, and (II) with respect to which depreciation (or amortization in lieu of depreciation) is allowable, or (ii) in the case of a qualified renovation area which is placed in service during such taxable year, 10 percent of the renovation expenditures incurred by a taxpayer which has been certified as a special access food provider. (2) Renovation expenditures For purposes of paragraph (1)(B)(ii), the term renovation expenditures means amounts chargeable to capital account and incurred for property (or additions or improvements to property) of a character subject to the allowance for depreciation in connection with the renovation or rehabilitation of a grocery store. (b) Grant program for food banks and temporary access merchants (1) In general The Secretary, in coordination with the Secretary of Agriculture, shall, subject to the requirements of this section, provide a grant to any entity which has been certified as a special access food provider in an amount equal to the lesser of\u2014 (A) the amount of the allocation received by the entity under subsection (d)(1)(B), or (B) the amount equal to\u2014 (i) in the case of a permanent food bank which has been placed in service during the taxable year by such provider, 15 percent of any qualified construction expenses incurred by such provider; and (ii) in the case of any provider which qualifies as a temporary access merchant, 10 percent of any annual operational costs incurred by such provider. (2) Time for payment of grant The Secretary shall make payment of any grant under paragraph (1) during the 60-day period beginning on the later of\u2014 (A) the date of the application for certification as a special access food provider, or (B) the date\u2014 (i) in the case of a permanent food bank, on which the food bank for which the grant is being made is placed in service, or (ii) in the case of a temporary access merchant, the end of the taxable year in which the operational costs were incurred. (3) Grant not considered income for purposes of taxation A grant under this subsection shall not be considered as gross income for purposes of this chapter. (c) Certification as a Special Access Food Provider (1) Application Each applicant for certification as a special access food provider shall submit, for each grocery store, food bank, mobile market, or farmers market, an application with the Secretary, at such time, in such manner, and containing such information as the Secretary may reasonably require. (2) Certification requirements For purposes of certification as a special access food provider, the Secretary, in consultation with the Secretary of Agriculture and the applicable regional community development entity, shall determine whether\u2014 (A) in the case of an applicant seeking to construct, renovate, or rehabilitate a grocery store, whether such store\u2014 (i) following completion of such construction, renovation, or rehabilitation, will qualify as a grocery store (as defined in subsection (h)(3)), (ii) is located in a food desert on the date on which construction, renovation, or rehabilitation begins, (iii) satisfies the eligibility criteria established for projects under the Healthy Food Financing Initiative established under section 243 of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6953 ), and (iv) satisfies such other criteria as is determined appropriate by the Secretary, in consultation with the Secretary of Agriculture, or (B) in the case of an applicant seeking to operate a permanent food bank or as a temporary access merchant, whether such applicant\u2014 (i) is an entity for which no part of the net earnings of such entity inures to the benefit of any private shareholder or individual, (ii) (I) in the case of a permanent food bank, is located in a food desert on the date on which construction of such food bank begins, or (II) in the case of a temporary access merchant\u2014 (aa) sells or provides food in any food desert for an average of\u2014 (AA) in the case of a farmers market, not less than 10 hours (during daylight hours) each week during the calendar year, or (BB) in the case of a temporary access merchant which is not a farmers market, not less than 5 days and 50 hours each week during the calendar year, or (bb) satisfies such requirements as are established by the Secretary of Agriculture to ensure an adequate level of food distribution within food deserts, (iii) satisfies the eligibility criteria described in subparagraph (A)(iii), and (iv) satisfies such other criteria as is determined appropriate by the Secretary. (3) No additional USDA grants for farmers markets A farmers market shall not be eligible for certification as a special access food provider during any period in which such farmers market receives funding pursuant to any other grant program administered by the Department of Agriculture (with the exception of food insecurity nutrition incentive grants provided under section 4405(b) of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 7517(b) )). (d) Allocation of special access food provider credits and grants (1) In general In each calendar year, the Secretary, in coordination with the Secretary of Agriculture, shall provide allocations to entities which have been certified as special access food providers under subsection (c) to receive\u2014 (A) in the case of an entity certified pursuant to subparagraph (A) of subsection (c)(2), a special access food provider credit for expenditures related to a qualified grocery store or qualified renovation area, and (B) in the case of an entity certified pursuant to subparagraph (B) of such subsection, grants for qualified construction expenses or operational costs incurred by such entity. (2) Duration of grants to temporary access merchants In the case of a special access food provider which qualifies as a temporary access merchant, the Secretary shall provide the grant to such provider on an annual basis for a period of not greater than 10 years. (e) Recapture (1) In general Subject to paragraph (3), the Secretary shall provide for recapturing the benefit of any credit allowable or grant provided under this section with respect to any qualified grocery store, qualified renovation area, or permanent food bank which fails to satisfy the requirements under subsection (c)(2) during the 5-year period following the date on which such store, area, or food bank is placed in service. (2) Temporary access merchant Subject to paragraph (3), the Secretary shall provide for recapturing the benefit of any grant provided under this section with respect to any temporary access merchant which fails to satisfy the requirements under subsection (c)(2) for any year during the period described in subsection (d)(2). (3) Application If, during any taxable year, a special access food provider fails to satisfy the requirements under subsection (c)(2), the tax under this chapter for such taxable year shall be increased by an amount equal to the appropriate percentage of the credit or grant amount as is determined appropriate by the Secretary. (f) Basis reduction The basis of any qualified grocery store, any grocery store which includes a qualified renovation area, or any food bank, mobile market, or farmers market shall be reduced by the amount of any credit or grant determined under this section with respect to such property. (g) Regulations The Secretary, in coordination with the Secretary of Agriculture, shall prescribe such regulations as may be appropriate to carry out this section, including regulations which\u2014 (1) prevent the abuse of the purposes of this section, (2) impose appropriate reporting requirements, and (3) ensure that non-metropolitan areas receive a proportional amount of allocations provided under subsection (d). (h) Definitions For purposes of this section: (1) Food desert (A) In general The term food desert means any population census tract in which\u2014 (i) not less than 500 people, or 33 percent of the population of such tract, reside\u2014 (I) in the case of a tract located within a metropolitan area, more than 1 mile from a grocery store, or (II) in the case of a tract not located within a metropolitan area, more than 10 miles from a grocery store, (ii) the poverty rate for such tract is at least 20 percent, or (iii) (I) in the case of a tract not located within a metropolitan area, the median family income for such tract does not exceed 80 percent of statewide median family income, or (II) in the case of a tract located within a metropolitan area, the median family income for such tract does not exceed 80 percent of the greater of statewide median family income or the metropolitan area median family income. (B) Areas not within census tracts In the case of an area which is not tracted for population census tracts, the equivalent county divisions (as defined by the Bureau of the Census) shall be used for purposes of determinations of food deserts under this paragraph. (C) Determination of food deserts For purposes of determining whether a population census tract qualifies as a food desert for purposes of this section, the Secretary shall make such determinations in coordination with the Secretary of Agriculture in such manner as is determined appropriate, including use of the Food Access Research Atlas established by the Department of Agriculture. (2) Groceries The term groceries means\u2014 (A) fresh and frozen produce, (B) fresh and frozen meat and seafood, (C) dairy products, and (D) deli products, including sliced meats, cheeses, and salads. (3) Grocery store The term grocery store means a retail store for which forecasted sales of groceries account for not less than 35 percent of its total annual sales. (4) Metropolitan area The term metropolitan area has the same meaning given the term metropolitan statistical area under section 143(k)(2)(B). (5) Qualified construction expenses The term qualified construction expenses means any costs incurred by the special access food provider before the date on which a permanent food bank is placed in service relating to the planning, design, and construction of such food bank. (6) Qualified grocery store The term qualified grocery store means a grocery store which, on the date on which construction of such store begins, is located in a food desert. (7) Qualified renovation area The term qualified renovation area means any area of a grocery store in which groceries are sold, provided that such grocery store, on the date on which renovation of such area begins, is located in a food desert. (8) Regional community development entity (A) In general The term regional community development entity means any domestic corporation or partnership if\u2014 (i) the primary mission of the entity is serving, or providing investment capital for, low-income communities or low-income persons, (ii) the entity maintains accountability to residents of low-income communities through their representation on any governing board of the entity or on any advisory board to the entity, and (iii) the entity is certified by the Secretary for purposes of this section as being a regional community development entity. (B) Local government In the case of a grocery store for which there is no entity described in subparagraph (A) within a 50-mile radius, the chief executive officer (or the equivalent) of the local jurisdiction in which the grocery store will be located may serve as the regional community development entity for purposes of subsection (c)(2). (9) Secretary of Agriculture The term Secretary of Agriculture means the Secretary of Agriculture or the Secretary's delegate. (10) Temporary access merchant The term temporary access merchant means a mobile market, a farmers market, or a temporary or mobile food bank (as such terms are defined by the Secretary, in coordination with the Secretary of Agriculture)\u2014 (A) which is operated by a special access food provider; and (B) for which the primary purpose is food distribution within food deserts. .\n##### (b) Credit part of general business credit\nSection 38(b) of the Internal Revenue Code of 1986 is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the special access food provider credit determined under section 45BB(a). .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 45BB. Special access food provider credit and grant program. .\n##### (d) Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out the purposes of this section.\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 3. Updates to Food Access Research Atlas\nSection 243 of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6953 ) is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e); and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Food Access Research Atlas Not less frequently than once each year, the Secretary shall update the Food Access Research Atlas of the Secretary to account for food retailers that are placed in service during that year. .",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-04-18",
        "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture."
      },
      "number": "2473",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Healthy Food Access for All Americans Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-08T20:07:38Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1176is.xml"
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
      "title": "Healthy Food Access for All Americans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Healthy Food Access for All Americans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to establish a new tax credit and grant program to stimulate investment and healthy nutrition options in food deserts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:21Z"
    }
  ]
}
```
