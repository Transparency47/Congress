# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8137?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8137
- Title: To amend the Internal Revenue Code of 1986 to establish tax credits for the production of, and investment in, certain renewable materials.
- Congress: 119
- Bill type: HR
- Bill number: 8137
- Origin chamber: House
- Introduced date: 2026-03-27
- Update date: 2026-05-21T08:08:32Z
- Update date including text: 2026-05-21T08:08:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-27: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-27: Introduced in House

## Actions

- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8137",
    "number": "8137",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000470",
        "district": "7",
        "firstName": "Michelle",
        "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
        "lastName": "Fischbach",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to establish tax credits for the production of, and investment in, certain renewable materials.",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:32Z",
    "updateDateIncludingText": "2026-05-21T08:08:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
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
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-27",
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
          "date": "2026-03-28T01:32:40Z",
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "IN"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "IA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8137ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8137\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2026 Mrs. Fischbach (for herself and Ms. Budzinski ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish tax credits for the production of, and investment in, certain renewable materials.\n#### 1. Credit for renewable materials production\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Renewable materials production credit (a) Allowance of credit For purposes of section 38, the renewable materials production credit for any taxable year is an amount equal to the product of\u2014 (1) 10 cents, multiplied by (2) the number of pounds of qualified renewable material which is\u2014 (A) produced by the taxpayer during such taxable year at a renewable material production facility, and (B) either\u2014 (i) sold by the taxpayer to an unrelated person, or (ii) used by the taxpayer producing such qualified renewable material, only if such sale or use is in a trade or business of the taxpayer during the taxable year. (b) Definitions For purposes of this section\u2014 (1) Qualified renewable material (A) In general The term qualified renewable material means the biobased carbon content portion of any product, including a chemical, produced using biological conversion, thermal conversion, catalytic conversion, chemical conversion, or a combination thereof, from biomass. (B) Exclusions The term qualified renewable material shall not include any product\u2014 (i) which is suitable for use as a fuel in any vehicle (whether or not the vehicle is manufactured primarily for use on public streets, roads, and highways), marine vessel, watercraft, or aircraft, (ii) used to generate heat or electricity, (iii) which is suitable for use as food or feed, (iv) produced from biomass which was not manufactured, produced, grown, or extracted in whole or in significant part within\u2014 (I) the United States (within the meaning of section 638(1)), or (II) a possession of the United States (within the meaning of section 638(2)), or (v) which is derived from coprocessing biomass with a feedstock which is not biomass. (C) First sale or use to qualify In the case where multiple points in a supply chain may be eligible under this section, the qualified renewable material that first meets the requirements of this section will be the only qualified renewable material eligible. (2) Biobased carbon content portion The term biobased carbon content portion means the biobased carbon content as determined pursuant to ASTM D6866. (3) Biomass The term biomass has the same meaning given such term in section 45K(c)(3), except biomass does not include any qualified renewable material. (4) Renewable material production facility The term renewable material production facility means any facility\u2014 (A) that produces qualified renewable material during a qualifying credit period, and (B) located in the United States or a possession of the United States (within the meaning of section 638(2)). (5) Qualifying credit period (A) In general The term qualifying credit period means the 10-year period beginning on the later of\u2014 (i) the date the renewable material production facility was originally placed in service, (ii) the date the modifications described in subparagraph (B) were placed in service, or (iii) the date of enactment of this section. (B) Modifications The modifications described in this subparagraph are substantial modifications to an existing facility which allow such facility to produce qualified renewable material. (c) Special rules (1) Credit attributable to taxpayer (A) In general Except as otherwise provided in subparagraph (B) or in any regulations prescribed by the Secretary, any credit under this section shall be attributable to the person that sells or uses the qualified renewable material. (B) Election If the person described in subparagraph (A) makes an election under this subparagraph in such time and manner as the Secretary may prescribe by regulations, the credit under this section\u2014 (i) shall be allowable to the person to whom the qualified renewable material is sold, and (ii) shall not be allowable to the person described in subparagraph (A). (2) Coordination with investment credit The term renewable material production facility shall not include any facility for which a renewable materials investment credit determined under section 48F is allowed under section 38 for the taxable year or any prior taxable year. (3) Credit reduced for tax-exempt bonds Rules similar to the rules of section 45(b)(3) shall apply. (4) Limitation The amount of the credit determined under subsection (a) with respect to any facility for any taxable year (determined after the application of paragraph (3)) shall not exceed $10,000,000. .\n##### (b) Coordination with clean fuel production credit\nSection 45Z(d)(4)(B) is amended by adding at the end the following:\n(iv) The renewable materials production credit under section 45BB. .\n##### (c) Credit made transferable\nSection 6418(f)(1) is amended\u2014\n**(1)**\nin subparagraph (A) by adding at the end the following:\n(xii) The renewable materials production credit determined under section 45BB. , and\n**(2)**\nin subparagraph (B), by striking or (vii) and inserting (vii), or (xii) .\n##### (d) Credit made part of general business credit\nSubsection (b) of section 38 of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the renewable materials production credit determined under section 45BB. .\n##### (e) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following:\nSec. 45BB. Renewable materials production credit. .\n##### (f) Regulations\nThe Secretary, in consultation with the Secretary of Agriculture, shall establish regulations or other guidance for implementing the credit established under this section within 180 days of the date of enactment.\n##### (g) Effective date\nThe amendments made by this section shall apply to qualified renewable material produced on or after the date of enactment.\n#### 2. Credit for renewable materials investment\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n48F. Renewable materials investment credit (a) Allowance of credit For purposes of section 46, the renewable materials investment credit for any taxable year is an amount equal to 30 percent of the qualified investment for the taxable year with respect to any qualified facility. (b) Qualified investment (1) In general For purposes of subsection (a), the qualified investment for any taxable year with respect to any qualified facility is the basis of any qualified property placed in service by the taxpayer during such taxable year which\u2014 (A) is used in the production of qualified renewable material, and (B) is part of a qualified facility. (2) Qualified property For purposes of this section, the term qualified property means property\u2014 (A) which is\u2014 (i) tangible personal property, or (ii) other tangible property (not including a building or its structural components), but only if such property is used as an integral part of the qualified facility, (B) with respect to which depreciation (or amortization in lieu of depreciation) is allowable, (C) which is constructed, reconstructed, erected, or acquired by the taxpayer, and (D) the original use of which commences with the taxpayer. (3) Qualified facility (A) In general The term qualified facility means a renewable material production facility within the meaning of section 45BB(b)(3). (B) Exclusion The term qualified facility shall not include any facility for which a renewable materials production credit determined under section 45BB is allowed under section 38 for the taxable year or any prior taxable year. (4) Coordination with rehabilitation credit The qualified investment with respect to any qualified facility for any taxable year shall not include that portion of the basis of any property which is attributable to qualified rehabilitation expenditures (as defined in section 47(c)(2)). (c) Special rules (1) Certain progress expenditure rules made applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the date of the enactment of the Revenue Reconciliation Act of 1990) shall apply for purposes of subsection (a). (2) Credit reduced for tax-exempt bonds Rules similar to the rules of section 45(b)(3) shall apply. .\n##### (b) Coordination with clean fuel production credit\nSection 45Z(d)(4)(B), as amended by section 1, is amended by adding at the end the following:\n(v) The credit determined under section 46 to the extent that such credit is attributable to the renewable materials investment credit. .\n##### (c) Credit made transferable\nSection 6418, as amended by section 1, is amended\u2014\n**(1)**\nin subsection (f)(1)(A) by adding at the end the following:\n(xiii) The renewable materials investment credit determined under section 48F. , and\n**(2)**\nin paragraph (g)(3) by striking (xi) and inserting (xi), or (xiii), .\n##### (d) Conforming amendments\n**(1)**\nSection 46 of such Code is amended\u2014\n**(A)**\nin paragraph (6) by striking and at the end,\n**(B)**\nin paragraph (7) by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(8) the renewable materials investment credit. .\n**(2)**\nSection 49(a)(1)(C) of such Code is amended\u2014\n**(A)**\nby striking and at the end of clause (vii),\n**(B)**\nby striking the period at the end of clause (viii) and inserting , and , and\n**(C)**\nby adding at the end the following new clause:\n(ix) the basis of any qualified property which is part of a qualified facility under section 48F. .\n**(3)**\nSection 50(a)(2)(E) of such Code is amended by striking or 48E(e) and inserting 48E(e), or 48F(c)(1) .\n**(4)**\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 48E the following new item:\nSec. 48F. Renewable materials investment credit. .\n##### (e) Regulations\nThe Secretary, in consultation with the Secretary of Agriculture, shall establish regulations or other guidance for implementing the credit established under this section within 180 days of the date of enactment.\n##### (f) Effective date\nThe amendments made by this section shall apply to property placed in service after the date of enactment.",
      "versionDate": "2026-03-27",
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
        "updateDate": "2026-04-14T01:31:50Z"
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
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8137ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish tax credits for the production of, and investment in, certain renewable materials.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:35Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to establish tax credits for the production of, and investment in, certain renewable materials.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T08:06:23Z"
    }
  ]
}
```
