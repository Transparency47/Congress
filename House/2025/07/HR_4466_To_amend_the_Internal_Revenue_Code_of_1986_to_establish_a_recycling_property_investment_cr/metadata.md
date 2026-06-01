# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4466?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4466
- Title: CIRCLE Act
- Congress: 119
- Bill type: HR
- Bill number: 4466
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2026-05-15T08:07:33Z
- Update date including text: 2026-05-15T08:07:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4466",
    "number": "4466",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001201",
        "district": "3",
        "firstName": "Thomas",
        "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
        "lastName": "Suozzi",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "CIRCLE Act",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:33Z",
    "updateDateIncludingText": "2026-05-15T08:07:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:04:35Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "PA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "IN"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4466ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4466\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Suozzi (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a recycling property investment credit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cultivating Investment in Recycling and Circular Local Economies Act of 2025 or the CIRCLE Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe national recycling goal set by the Environmental Protection Agency is 50 percent by 2030.\n**(2)**\nAmerica\u2019s recycling rate hovers around 30 percent.\n**(3)**\nThe establishment of a tax credit for investment in existing and new recycling infrastructure would promote recycling by facilitating modernized and upgraded recycling operations and increasing supply of domestically recycled materials.\n**(4)**\nNew recycling infrastructure would support responsible end markets by helping to meet significant demand for domestically sourced recycled material.\n**(5)**\nDomestic markets face increased competition from international actors who may dump virgin materials or not-verifiably-recycled content in United States markets, undercutting the domestic recycling economy.\n**(6)**\nIt is in the best interests of the United States to fully develop our recycling capacities.\n#### 3. Recycling property investment credit\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. Recycling property investment credit (a) In general For purposes of section 46, the recycling property investment credit for any taxable year is an amount equal to 30 percent of the qualified investment for such taxable year. (b) Qualified investment (1) In general For purposes of subsection (a), the qualified investment for any taxable year is the basis of any eligible property placed in service by the taxpayer during such taxable year. (2) Eligible property For purposes of this section, the term eligible property means property\u2014 (A) which is qualified recycling property, (B) with respect to which depreciation (or amortization in lieu of depreciation) is allowable, and (C) (i) the construction, reconstruction, addition, or erection of which is completed by the taxpayer, or (ii) which is acquired by the taxpayer if the original use of such property commences with the taxpayer. (c) Special rules For purposes of this section\u2014 (1) Certain progress expenditure rules made applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the date of the enactment of the Revenue Reconciliation Act of 1990) shall apply. (2) Special rule for certain subsidized property Rules similar to section 45(b)(3) shall apply. (3) Domestic content bonus credit amount (A) In general In the case of any qualified investment which satisfies the requirement under subparagraph (B), the amount of the credit determined under subsection (a) (determined without regard to this paragraph before the application of subsection (d) and after the application of any other provision of this section) shall be increased by an amount equal to 10 percentage points of the amount so determined. (B) Requirement Rules similar to the rules of section 45(b)(9)(B) shall apply. (4) Phaseout for elective payment In the case of a taxpayer making an election under section 6417 with respect to a credit under this section, rules similar to the rules of section 45(b)(10) shall apply. (d) Credit phase-Out (1) In general The amount of the credit determined under subsection (a) with respect to any qualified investment shall be equal to the product of\u2014 (A) the amount of the credit determined under subsection (a) without regard to this subsection, multiplied by (B) the phase-out percentage under paragraph (2). (2) Phase-out percentage The phase-out percentage under this paragraph is equal to\u2014 (A) in the case of any eligible property with a determination date beginning on or after January 1, 2026, and before December 31, 2032, 100 percent, (B) in the case of any eligible property with a determination date beginning on or after January 1, 2033, and before December 31, 2033, 80 percent, (C) in the case of any eligible property with a determination date beginning on or after January 1, 2034, and before December 31, 2034, 60 percent, (D) in the case of any eligible property with a determination date beginning on or after January 1, 2035, and before December 31, 2035, 40 percent, (E) in the case of any eligible property with a determination date beginning on or after January 1, 2036, and before December 31, 2036, 20 percent, and (F) in the case of any eligible property with a determination date beginning on or after January 1, 2037, 0 percent. (3) Determination date For purposes of paragraph (2), the determination date of an eligible property is\u2014 (A) in the case such property is described in subsection (b)(2)(C)(i), the date on which the construction, reconstruction, addition, or erection of such property begins, and (B) in any other case, the date on which such property is placed in service. (e) Denial of double benefit In the case of any eligible property with respect to which credit is allowed under subsection (a)\u2014 (1) no other credit or deduction shall be allowed for, or by reason of, such property to the extent of the amount of such credit, and (2) the basis of such property shall be reduced by the amount of such credit. (f) Regulations and guidance The Secretary shall issue such regulations or other guidance as the Secretary determines necessary to carry out the purposes of this section, including regulations or other guidance which provides for requirements for recordkeeping or information reporting for purposes of administering the requirements of this section. (g) Definitions For purposes of this section\u2014 (1) Qualified recycling property The term qualified recycling property has the meaning given the term reuse and recycling property in section 168(m)(3)(A). (2) Qualified reuse and recyclable materials The term qualified reuse and recyclable materials has the meaning given such term in section 168(m)(3)(B), except that for purposes of this section such term includes any video display device and any computer device (including computer peripherals, such as keyboards, mice, speakers, cables, printers, and scanners). (3) Recycle The term recycle has the meaning given such term in section 168(m)(3)(C), except that for purposes of this section such term does not include\u2014 (A) any method of sorting, processing, and aggregating materials from solid waste that\u2014 (i) does not preserve the original quality of such materials, and (ii) results in the aggregated material not being usable\u2014 (I) for the initial purpose (or a substantially similar purpose) of such materials, or (II) as feedstock in lieu of virgin feedstock in the production of specification grade commodities, or (B) the primary use of waste or qualified reuse and recyclable materials\u2014 (i) as a fuel or fuel substitute; (ii) for the production or generation of energy (including heat and electricity); (iii) for incineration; (iv) for alternate operating cover; or (v) within the footprint of a landfill. .\n##### (b) Credit made part of investment credit\nSection 46 of such Code is amended by striking and at the end of paragraph (6), by striking the period at the end of paragraph (7) and inserting , and , and by adding at the end the following new paragraph:\n(8) the recycling property investment credit. .\n##### (c) Clerical amendment\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 48E the following new item:\n48F. Recycling property investment credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to\u2014\n**(1)**\nin the case of property described in section 48F(b)(2)(C)(i) of the Internal Revenue Code of 1986 (as added by subsection (a)), property which is constructed, reconstructed, added, or erected after December 31, 2025, and\n**(2)**\nin any other case, property which is placed in service after December 31, 2025.",
      "versionDate": "2025-07-16",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6900",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Affordability Act of 2025",
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
        "updateDate": "2025-07-29T21:31:06Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4466ih.xml"
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
      "title": "CIRCLE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-26T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CIRCLE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-26T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cultivating Investment in Recycling and Circular Local Economies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-26T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a recycling property investment credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-26T03:18:17Z"
    }
  ]
}
```
