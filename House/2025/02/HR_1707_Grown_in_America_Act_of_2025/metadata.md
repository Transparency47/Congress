# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1707?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1707
- Title: Grown in America Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1707
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-05-13T08:06:30Z
- Update date including text: 2026-05-13T08:06:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1707",
    "number": "1707",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000392",
        "district": "8",
        "firstName": "David",
        "fullName": "Rep. Kustoff, David [R-TN-8]",
        "lastName": "Kustoff",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Grown in America Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:30Z",
    "updateDateIncludingText": "2026-05-13T08:06:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:09:25Z",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MO"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "OH"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IA"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "WA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "MN"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "TX"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-12-23",
      "state": "MN"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "AR"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "GA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "GA"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "AZ"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NY"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "MO"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "PA"
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
      "sponsorshipDate": "2026-04-27",
      "state": "NC"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1707ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1707\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Kustoff (for himself, Mr. Costa , Mr. Alford , Mr. Rouzer , and Mr. Carey ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a tax credit to incentivize the purchase of American agricultural commodities.\n#### 1. Short title\nThis Act may be cited as the Grown in America Act of 2025 .\n#### 2. Domestically produced agriculture credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Domestically produced agriculture credit (a) In general For purposes of section 38, the domestically produced agriculture credit determined under this section for any taxable year is an amount equal to the lesser of\u2014 (1) (A) the product of\u2014 (B) 25 percent of the total agricultural input costs of such taxpayer with respect to such taxable year, multiplied by (C) the applicable percentage of the taxpayer for the taxable year, or (2) $100,000,000. (b) Definitions For purposes of this section\u2014 (1) Applicable percentage For purposes of this section, the applicable percentage for a taxpayer for any taxable year is an amount (expressed as a percentage) equal to the quotient of\u2014 (A) the domestic agricultural input costs of such taxpayer for such taxable year, divided by (B) the total agricultural input costs of such taxpayer for such taxable year. (2) Agricultural commodity (A) In general The term agricultural commodity means a commodity specified in subparagraph (B) that\u2014 (i) is marketed for human consumption, or (ii) is used in the production or manufacture of a product marketed for human consumption. (B) Commodities specified The commodities described in this subparagraph are\u2014 (i) The commodities described in subparagraphs (A), (B) excluding live animals, (C), and (E) of section 513 of the Federal Agriculture Improvement and Reform Act of 1996, and (ii) the products of farm-raised fish (as defined in section 1501 of the Agricultural Act of 2014). (3) Domestic agricultural input costs The term domestic agricultural input costs means any expenses paid or incurred by the taxpayer during any taxable year to purchase agricultural commodities\u2014 (A) which are produced in the United States, and (B) which the taxpayer uses in the course of the trade or business of the taxpayer to produce products\u2014 (i) in the United States, and (ii) sold for human consumption without further processing. (4) Foreign agricultural input costs The term foreign agricultural input costs means any expenses paid or incurred by the taxpayer during any taxable year to purchase agricultural commodities\u2014 (A) which are produced outside the United States, and (B) which the taxpayer uses in the course of the trade or business of the taxpayer to produce products\u2014 (i) in the United States, and (ii) sold for human consumption without further processing. (5) Total agricultural input costs (A) In general Subject to subparagraph (B), the term total agricultural input costs means an amount equal to the sum of domestic agricultural input costs and foreign agricultural input costs of the taxpayer for any taxable year. (B) Exception The term total agricultural input costs shall not include any expenses paid or incurred by the taxpayer during the taxable year to purchase any agricultural commodity identified and listed by the Secretary of Agriculture under section 2(c) of the Grown in America Act of 2025 . (c) Ineligibility for credit (1) In general In the case of any taxpayer for which the 3-year average applicable percentage for any taxable year does not exceed the applicable threshold, the amount of the credit allowed under subsection (a) shall be reduced to zero for such taxable year. (2) Applicable threshold For purposes of this subsection, the term applicable threshold means\u2014 (A) in the case of taxable years beginning in 2026, 50 percent, (B) in the case of taxable years beginning in 2027, 55 percent, (C) in the case of taxable years beginning in 2028, 60 percent, (D) in the case of taxable years beginning in 2029, 65 percent, (E) in the case of taxable years beginning in 2030, 70 percent. (F) in the case of taxable years beginning in 2031, 75 percent, (G) in the case of taxable years beginning in 2032, 80 percent, and (H) in the case of taxable years beginning after December 31, 2033, 85 percent. (3) 3-year average applicable percentage For purposes of this subsection, the term 3-year average applicable percentage means, with respect to a taxpayer and any taxable year, the amount (expressed as a percentage) equal that is equal to the quotient of\u2014 (A) the domestic agricultural input costs of such taxpayer for the 3-year period ending on the last day of such taxable year, divided by (B) the total agricultural input costs of such taxpayer for such 3-year period. (d) Cooperative organizations (1) Apportionment of credit In the case of an eligible cooperative organization described in paragraph (4), any portion of the credit determined under subsection (a) for the taxable year may, at the election of the organization, be apportioned among patrons eligible to share in patronage dividends on the basis of the quantity or value of business done with or for such patrons for the taxable year. (2) Form and effect of election An election under subparagraph (A) for any taxable year shall be made on a timely filed return for such year. (3) Election irrevocable An election under subparagraph (A) shall be irrevocable for the taxable year. (4) Treatment of organizations and patrons (A) Organizations The amount of the credit not apportioned to patrons pursuant to paragraph (1) shall be included in the amount determined under subsection (a) for the taxable year of the eligible cooperative organization. (B) Patrons The amount of the credit apportioned to patrons pursuant to paragraph (1) shall be included in the amount determined under subsection (a) for the first taxable year of each patron ending on or after the last day of the payment period (as defined in section 1382(d)) for the taxable year of the eligible cooperative organization or, if earlier, for the taxable year of each patron ending on or after the date on which the patron receives notice from such cooperative of the apportionment. (5) Special rule If the amount of the credit of an eligible cooperative organization determined under subsection (a) for a taxable year is less than the amount of such credit shown on the return of the cooperative organization for such year, an amount equal to the excess of\u2014 (A) such reduction, over (B) the amount not apportioned to such patrons under subparagraph (A) for the taxable year, shall be treated as an increase in tax imposed by this chapter on such organization. Such increase shall not be treated as a tax imposed by this chapter for purposes of determining the amount of any credit under this chapter. (6) Eligible cooperative organization For purposes of this subsection, the term eligible cooperative organization has the meaning given to the term specified agricultural or horticultural cooperative in section 199A(g)(4). (e) Aggregation rule All persons which are treated as a single employer under subsections (a) and (b) of section 52 shall be treated as a single taxpayer for purposes of this section. (f) Regulations The Secretary may prescribe such regulations and other guidance as may be necessary or appropriate to carry out this section. .\n##### (b) Credit allowed as part of general business credit\n**(1) In general**\nSection 38(b) of such Code is amended by adding at the end the following new paragraph:\n(42) the domestically produced agriculture credit determined under section 45U(a). .\n**(2) Limitations**\nSection 38(c) of such Code is amended by adding at the end the following new paragraph:\n(7) Special rules for domestically produced agriculture credit In the case of the portion of the credit determined under subsection (a) which is attributable to the domestically produced agriculture credit determined under section 45BB\u2014 (A) this section and section 39 shall be applied separately with respect to such credit, (B) in applying paragraph (1) to such credit\u2014 (i) for purposes of subparagraph (A) thereof, the tentative minimum tax shall be treated as being zero, (ii) for purposes of subparagraph (B) thereof, such subparagraph shall be applied\u2014 (I) by substituting 50 percent for 25 percent , and (II) by substituting $0 for $25,000 , and (iii) the limitation under paragraph (1) (as modified by clause (ii)) shall be reduced by the credit allowed under subsection (a) for the taxable year (other than the domestically produced agriculture credit), and (C) with respect to the application of section 39, subsection (a) of such section shall be applied\u2014 (i) in paragraphs (1)(B) and (2)(B) thereof, by substituting 10 taxable years for 20 taxable years each place it appears, and (ii) in paragraph (2)(A), by substituting 11 taxable years for 21 taxable years . .\n##### (c) Domestically unavailable agricultural commodities\nFor purposes of section 45BB of such Code, the Secretary of Agriculture shall establish and maintain a list that identifies, with respect to each calendar year beginning after the date of enactment of this Act, the agricultural commodities (as defined in subsection (b)(2) of such section) that cannot feasibly be produced, grown, or raised domestically during such calendar year.\n##### (d) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Domestically produced agriculture credit. .\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-02-27",
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
        "updateDate": "2025-05-07T19:59:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
    "originChamber": "House",
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
          "measure-id": "id119hr1707",
          "measure-number": "1707",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2026-05-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1707v00",
            "update-date": "2026-05-04"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Grown in America Act of 2025</strong></p><p>This bill establishes a new tax credit (as part of the general business tax credit) for domestically produced agriculture.</p><p>Specifically, the bill allows a tax credit for the lesser of (1) 25% of domestically produced agricultural commodity expenses multiplied by the ratio of such expenses to total agricultural commodity expenses (excluding expenses for agricultural commodities that cannot feasibly be produced domestically), or (1) $100 million. (Conditions apply).</p><p>To qualify for the tax credit, a business\u2019s average expenses (over three years) for domestically produced agricultural commodities must exceed a certain percentage\u00a0of total agricultural commodity expenses (excluding expenses for agricultural commodities that cannot feasibly be produced domestically). The required percentage is 50% for 2026 and increases by 5% each year until it reaches 85% for tax years beginning after 2033.</p><p>Under the bill, agricultural commodities include</p><ul><li>horticultural, viticultural, and dairy products;</li><li>livestock and livestock products (excluding live animals);</li><li>poultry and bee raising products; and</li><li>farm-raised fish products.</li></ul><p>In addition, the general business tax credit limit based on a business\u2019s tax liability is calculated separately for the domestically produced agriculture tax credit, and the credit is generally limited to 50% of a business\u2019s net regular tax liability.</p><p>Finally, domestically produced agriculture tax credit amounts in excess of such limitation may be\u00a0carried forward for 10 years (rather than the 20 years allowed for other business tax credits).</p>"
        },
        "title": "Grown in America Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1707.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Grown in America Act of 2025</strong></p><p>This bill establishes a new tax credit (as part of the general business tax credit) for domestically produced agriculture.</p><p>Specifically, the bill allows a tax credit for the lesser of (1) 25% of domestically produced agricultural commodity expenses multiplied by the ratio of such expenses to total agricultural commodity expenses (excluding expenses for agricultural commodities that cannot feasibly be produced domestically), or (1) $100 million. (Conditions apply).</p><p>To qualify for the tax credit, a business\u2019s average expenses (over three years) for domestically produced agricultural commodities must exceed a certain percentage\u00a0of total agricultural commodity expenses (excluding expenses for agricultural commodities that cannot feasibly be produced domestically). The required percentage is 50% for 2026 and increases by 5% each year until it reaches 85% for tax years beginning after 2033.</p><p>Under the bill, agricultural commodities include</p><ul><li>horticultural, viticultural, and dairy products;</li><li>livestock and livestock products (excluding live animals);</li><li>poultry and bee raising products; and</li><li>farm-raised fish products.</li></ul><p>In addition, the general business tax credit limit based on a business\u2019s tax liability is calculated separately for the domestically produced agriculture tax credit, and the credit is generally limited to 50% of a business\u2019s net regular tax liability.</p><p>Finally, domestically produced agriculture tax credit amounts in excess of such limitation may be\u00a0carried forward for 10 years (rather than the 20 years allowed for other business tax credits).</p>",
      "updateDate": "2026-05-04",
      "versionCode": "id119hr1707"
    },
    "title": "Grown in America Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Grown in America Act of 2025</strong></p><p>This bill establishes a new tax credit (as part of the general business tax credit) for domestically produced agriculture.</p><p>Specifically, the bill allows a tax credit for the lesser of (1) 25% of domestically produced agricultural commodity expenses multiplied by the ratio of such expenses to total agricultural commodity expenses (excluding expenses for agricultural commodities that cannot feasibly be produced domestically), or (1) $100 million. (Conditions apply).</p><p>To qualify for the tax credit, a business\u2019s average expenses (over three years) for domestically produced agricultural commodities must exceed a certain percentage\u00a0of total agricultural commodity expenses (excluding expenses for agricultural commodities that cannot feasibly be produced domestically). The required percentage is 50% for 2026 and increases by 5% each year until it reaches 85% for tax years beginning after 2033.</p><p>Under the bill, agricultural commodities include</p><ul><li>horticultural, viticultural, and dairy products;</li><li>livestock and livestock products (excluding live animals);</li><li>poultry and bee raising products; and</li><li>farm-raised fish products.</li></ul><p>In addition, the general business tax credit limit based on a business\u2019s tax liability is calculated separately for the domestically produced agriculture tax credit, and the credit is generally limited to 50% of a business\u2019s net regular tax liability.</p><p>Finally, domestically produced agriculture tax credit amounts in excess of such limitation may be\u00a0carried forward for 10 years (rather than the 20 years allowed for other business tax credits).</p>",
      "updateDate": "2026-05-04",
      "versionCode": "id119hr1707"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1707ih.xml"
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
      "title": "Grown in America Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Grown in America Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a tax credit to incentivize the purchase of American agricultural commodities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:34:02Z"
    }
  ]
}
```
