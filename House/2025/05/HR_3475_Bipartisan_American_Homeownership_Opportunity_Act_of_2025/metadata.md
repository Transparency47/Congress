# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3475?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3475
- Title: Bipartisan American Homeownership Opportunity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3475
- Origin chamber: House
- Introduced date: 2025-05-17
- Update date: 2025-11-01T08:05:53Z
- Update date including text: 2025-11-01T08:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-17: Introduced in House
- 2025-05-17 - IntroReferral: Introduced in House
- 2025-05-17 - IntroReferral: Introduced in House
- 2025-05-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-05-17: Introduced in House

## Actions

- 2025-05-17 - IntroReferral: Introduced in House
- 2025-05-17 - IntroReferral: Introduced in House
- 2025-05-17 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-17",
    "latestAction": {
      "actionDate": "2025-05-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3475",
    "number": "3475",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Bipartisan American Homeownership Opportunity Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-01T08:05:53Z",
    "updateDateIncludingText": "2025-11-01T08:05:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-17",
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
      "actionDate": "2025-05-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-17",
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
          "date": "2025-05-17T14:00:40Z",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-17",
      "state": "ME"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NM"
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
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3475ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3475\nIN THE HOUSE OF REPRESENTATIVES\nMay 17, 2025 Mr. Fitzpatrick (for himself and Mr. Golden of Maine ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a new first-time homebuyer credit and to establish the starter home construction credit.\n#### 1. Short title\nThis Act may be cited as the Bipartisan American Homeownership Opportunity Act of 2025 .\n#### 2. First-time homebuyer credit\n##### (a) In general\nSection 36 of the Internal Revenue Code of 1986 is amended to read as follows:\n36. First-time homebuyer credit (a) In general ln the case of an individual who is a first-time homebuyer of a principal residence in the United States during a taxable year, there shall be allowed as a credit against the tax imposed by this subtitle for such taxable year an amount equal to so much of the amount of the down payment paid by such taxpayer to purchase such principal residence as does not exceed $50,000. (b) Limitation (1) In general The amount allowable as a credit under subsection (a) (determined without regard to this paragraph) for the taxable year shall be reduced (but not below zero) by the amount which bears the same ratio to the amount which is so allowable as\u2014 (A) the excess (if any) of\u2014 (i) the taxpayer\u2019s modified adjusted gross income for the preceding taxable year, over (ii) the applicable threshold amount, bears to\u2014 (B) $100,000 (2) Threshold amount For purposes of this subsection, the term threshold amount means\u2014 (A) $300,000 in the case of a joint return or surviving spouse, (B) $225,000 in the case of a head of household, or (C) $150,000 in the case of any other individual. (3) Modified adjusted gross income For purposes of paragraph (1), the term modified adjusted gross income means the adjusted gross income of the taxpayer for the taxable year increased by any amount excluded from gross income under section 911, 931, or 933. (c) Exceptions No credit under subsection (a) shall be allowed to any taxpayer for any taxable year with respect to the purchase of a residence if\u2014 (1) the taxpayer is a nonresident alien, (2) the taxpayer disposes of such residence (or such residence ceases to be the principal residence of the taxpayer (and, if married, the taxpayer\u2019s spouse)) before the close of such taxable year, (3) a deduction under section 151 with respect to such taxpayer is allowable to another taxpayer for such taxable year, or (4) the taxpayer fails to attach to the return of tax for such taxable year a properly executed copy of the settlement statement used to complete such purchase. (d) Election for advanced payment (1) In general At the election of the first-time homebuyer, the Secretary shall transfer to a qualifying escrow account an amount equal to the amount that is allowable to such first-time homebuyer under subsection (a) in the present taxable year. (2) Treatment of transfer The amount of the credit allowed under subsection (a) to any taxpayer for any taxable year shall be reduced (but not below zero) by the aggregate amount of payments made under this subsection at the election of such taxpayer during such taxable year. Any failure to so reduce the credit shall be treated as arising out of a mathematical or clerical error and assessed according to section 6213(b)(1). (3) Qualifying escrow account For purposes of this subsection, the term qualifying escrow account means an escrow account established for the purchase of a principal residence by a qualified first-time homebuyer that meets the following requirements: (A) Amounts in such account may only be used for a down payment on a purchase with respect to which a credit is allowed under subsection (a). (B) Such account is administered by a bank (as defined in section 408A (n)). (C) The administrator of the account shall transfer to the Secretary any amount in such account not used under subparagraph (A) on the earlier of\u2014 (i) the date that is 180 days after the date on which such amount was transferred to such account under paragraph (1), or (ii) as soon as practicable upon request of the qualified first-time homebuyer. (e) Recapture of credit (1) In general lf, during any taxable year, there is a recapture event with respect to any property with respect to which a credit was allowed under subsection (a), then the tax of the taxpayer to whom such credit was allowed under this chapter for such taxable year shall be increased by an amount equal to the amount of the credit that was allowed with respect to such property. (2) Recapture event For purposes of this section, the term recapture event means, during the 5-year period beginning on the date of the purchase with respect to which a credit was allowed under subsection (a)\u2014 (A) the sale, lease to a third party, or disposition of any part of the property with respect to which such credit was allowed, or (B) such property ceases to be the principal residence of the taxpayer (or, in the case of a joint return, of the taxpayer\u2019s spouse). (3) Exceptions Paragraph (1) shall not apply to any of the following: (A) Purchase of new primary residence (i) In general A sale of a property with respect to which a credit was allowed under subsection (a) which is incident to the purchase by a taxpayer of a new primary residence if the proceeds of such sale are used to carry out the purchase of such new primary residence. (ii) Treatment of new primary residence ln the case of a purchase of a primary residence described in clause (i), for purposes of paragraph (1), such primary residence shall be treated as a property with respect to which a credit was allowed under subsection (a), except that the period described in paragraph (2) shall begin on the date on which the original purchase with respect to which the credit was allowed under subsection (a) occurred. (B) Death Any taxable year ending after the death of the taxpayer (or, in the case of a joint return, of the spouse of the taxpayer). (C) Divorce A transfer of a residence to which section 1041(a) applies. (D) Government orders A recapture event relating to a principal residence occurring in connection with Government orders received by such individual, or such individual\u2019s spouse, for qualified official extended duty service. (E) Qualified official extended duty service For purposes of this paragraph, the term qualified official extended duty service means service on qualified official extended duty as\u2014 (i) a member of the uniformed services, (ii) a member of the Foreign Service of the United States, or (iii) an employee of the intelligence community. (f) Definitions For purposes of this section\u2014 (1) First-time homebuyer The term first-time homebuyer means any individual if such individual (and if married, such individual\u2019s spouse)\u2014 (A) had no present ownership interest in a principal residence during the 10-year period ending on the date of the purchase of the principal residence to which this section applies, (B) has not been allowed a credit under subsection (a) for any preceding taxable year, and (C) attests that such individual (and if married, such individual\u2019s spouse) has never had a majority interest in a residential property. (2) Principal residence The term principal residence has the same meaning as when used in section 121. (3) Purchase (A) In general The term purchase means any acquisition, but only if\u2014 (i) the property is purchased using a mortgage loan from a commercial lender, (ii) the property is not acquired from a person related to the person acquiring such property (or, if married, such individual\u2019s spouse), and (iii) the basis of the property in the hands of the person acquiring such property is not determined\u2014 (I) in whole or in part by reference to the adjusted basis of such property in the hands of the person from whom acquired, or (II) under section 1014(a). (B) Construction A residence which is constructed by the taxpayer shall be treated as purchased by the taxpayer on the date the taxpayer first occupies such residence. (4) Related persons A person shall be treated as related to another person if the relationship between such persons would result in the disallowance of losses under section 267 or 707(b) (but, in applying section 267(b) and (c) for purposes of this section, paragraph (4) of section 267(c)(4) shall be treated as providing that the family of an individual shall include only his spouse, ancestors, and lineal descendants). (g) Basis adjustment For purposes of this subtitle, if a credit is allowed under this section in connection with any expenditure for any property, the increase in the basis of such property which would (but for this subsection) result from such expenditure shall be reduced by the amount of the credit so determined. (h) Inflation adjustment (1) In general In the case of any taxable year beginning after 2025, the dollar amounts in this section shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting \u201ccalendar year 2023\u201d for calendar year 2016 in subparagraph (A)(ii). (2) Rounding lf any increase under paragraph (1) is not a multiple of $100, such increase shall be rounded to the nearest multiple of $100. (i) Reporting (1) In general lf the Secretary requires information reporting under section 6045 by a person described in subsection (d)(2) thereof to verify the eligibility of taxpayers for the credit allowable by this section, the exception provided by section 6045(e) shall not apply. (2) Information from lender The Secretary may require any lender issuing a loan for the purchase of a property with respect to which a credit is allowed under subsection (a) or with respect to which a first-time homebuyer has made a request for a transfer under subsection (d)(1) to provide such information relating to the related purchase as the Secretary determines appropriate. (j) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section. .\n##### (b) Effective date\nThe amendment made by this section shall apply to residences purchased in taxable years beginning after the date of the enactment of this Act.\n#### 3. Starter home construction credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45U. Starter home construction credit (a) In general For the purposes of section 38, the starter home construction credit determined under this section for any taxable year is an amount equal to 15 percent of the qualified home construction costs of the taxpayer for the taxable year. (b) Limitation The amount allowable as a credit under subsection (a) to any taxpayer for any taxable year shall not exceed the amount allocated to such taxpayer for the calendar year in which such taxable year ends under subsection (d). (c) Increase for first-Time homebuyer ln the case of a unit of housing sold to a first-time homebuyer (as defined in section 36(g)(1)), subsection (a) shall be applied by substituting 30 percent for 15 percent . (d) Qualified home construction costs For purposes of this section, the term qualified home construction costs means, with respect to a taxable year, amounts paid or incurred by the taxpayer for labor and material costs to construct a unit of housing placed in service during such taxable year\u2014 (1) the total square footage of which does not exceed 1200 feet, and (2) the sale price of which does not exceed 80 percent of the area median home price. (e) Allocation.\u2014 (1) In general The aggregate starter home construction credit dollar amount which a housing credit agency may allocate for any calendar year is the portion of the State starter home construction credit ceiling allocated under this paragraph for such calendar year to such agency. (2) State ceiling initially allocated to state housing credit agencies The State starter home construction credit ceiling for each calendar year shall be allocated to the housing credit agency of such State. If there is more than 1 housing credit agency of a State, all such agencies shall be treated as a single agency. (3) State starter home credit ceiling The State starter home credit ceiling applicable to any State for any calendar year shall be an amount equal to the sum of\u2014 (A) the unused State housing credit ceiling (if any) of such State for the preceding calendar year, plus (B) $30 multiplied by the population of the State (determined in accordance with section 146(j)). (4) Housing credit agency For purposes of this subsection, the term housing credit agency has the meaning given in section 42(h)(8)(A). (5) Inflation adjustment (A) In general ln the case of any taxable year beginning after 2025, the dollar amount in paragraph (3)(B) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2023 for calendar year 2016 in subparagraph (A)(ii) thereof. (B) Rounding lf any increase under subparagraph (A) is not a multiple of $5, such increase shall be rounded to the nearest multiple of $5. (f) Basis adjustment For purposes of this subtitle, if a credit is allowed under this section in connection with any expenditure for any property, the increase in the basis of such property which would (but for this subsection) result from such expenditure shall be reduced by the amount of the credit so determined. (g) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section. .\n##### (b) Credit To be part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (32), by striking the period at the end of paragraph (33) and inserting , plus , and by adding at the end the following new paragraph:\n(34) the starter home construction credit determined under section 45U(a). .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 45T the following new item:\nSec. 45U. Starter home construction credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this section.",
      "versionDate": "2025-05-17",
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
        "updateDate": "2025-06-06T20:30:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-17",
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
          "measure-id": "id119hr3475",
          "measure-number": "3475",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-17",
          "originChamber": "HOUSE",
          "update-date": "2025-07-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3475v00",
            "update-date": "2025-07-02"
          },
          "action-date": "2025-05-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bipartisan American Homeownership Opportunity Act of 2025</strong></p><p>This bill provides a new refundable tax credit for first-time homebuyers and a new tax credit to home builders for the construction of starter homes, both subject to limitations.</p><p>First-time homebuyers may claim a tax credit equal to the amount of the down payment up to $50,000, subject to income limitations. The tax credit begins to\u00a0phase out when a homebuyer\u2019s income exceeds $300,000 for joint filers or surviving spouses, $225,000 for head of household filers, and $150,000 for single filers. The amounts are adjusted annually for inflation after 2025.\u00a0\u00a0</p><p>The bill requires homebuyers to add the amount received as a tax credit to taxable income if, within five years from the purchase, the house is sold, leased, or is no longer used as the principal place of residence. (Some exceptions apply.)</p><p>The bill also provides a tax credit for home builders of up to 15% of construction costs (materials and labor) incurred to build a home that is no larger than 1,200 square feet and is sold for an amount that does not exceed 80% of the median home prices for the area. The amount of the tax credit increases to 30% if the home is sold to a first-time home buyer.</p><p>Finally, under the bill, each state receives an annual allocation for the tax credit for the construction of starter homes, for allocation by the state\u2019s housing finance agency to builders (similar to the administration of the low-income housing tax credit).\u00a0</p>"
        },
        "title": "Bipartisan American Homeownership Opportunity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3475.xml",
    "summary": {
      "actionDate": "2025-05-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bipartisan American Homeownership Opportunity Act of 2025</strong></p><p>This bill provides a new refundable tax credit for first-time homebuyers and a new tax credit to home builders for the construction of starter homes, both subject to limitations.</p><p>First-time homebuyers may claim a tax credit equal to the amount of the down payment up to $50,000, subject to income limitations. The tax credit begins to\u00a0phase out when a homebuyer\u2019s income exceeds $300,000 for joint filers or surviving spouses, $225,000 for head of household filers, and $150,000 for single filers. The amounts are adjusted annually for inflation after 2025.\u00a0\u00a0</p><p>The bill requires homebuyers to add the amount received as a tax credit to taxable income if, within five years from the purchase, the house is sold, leased, or is no longer used as the principal place of residence. (Some exceptions apply.)</p><p>The bill also provides a tax credit for home builders of up to 15% of construction costs (materials and labor) incurred to build a home that is no larger than 1,200 square feet and is sold for an amount that does not exceed 80% of the median home prices for the area. The amount of the tax credit increases to 30% if the home is sold to a first-time home buyer.</p><p>Finally, under the bill, each state receives an annual allocation for the tax credit for the construction of starter homes, for allocation by the state\u2019s housing finance agency to builders (similar to the administration of the low-income housing tax credit).\u00a0</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119hr3475"
    },
    "title": "Bipartisan American Homeownership Opportunity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bipartisan American Homeownership Opportunity Act of 2025</strong></p><p>This bill provides a new refundable tax credit for first-time homebuyers and a new tax credit to home builders for the construction of starter homes, both subject to limitations.</p><p>First-time homebuyers may claim a tax credit equal to the amount of the down payment up to $50,000, subject to income limitations. The tax credit begins to\u00a0phase out when a homebuyer\u2019s income exceeds $300,000 for joint filers or surviving spouses, $225,000 for head of household filers, and $150,000 for single filers. The amounts are adjusted annually for inflation after 2025.\u00a0\u00a0</p><p>The bill requires homebuyers to add the amount received as a tax credit to taxable income if, within five years from the purchase, the house is sold, leased, or is no longer used as the principal place of residence. (Some exceptions apply.)</p><p>The bill also provides a tax credit for home builders of up to 15% of construction costs (materials and labor) incurred to build a home that is no larger than 1,200 square feet and is sold for an amount that does not exceed 80% of the median home prices for the area. The amount of the tax credit increases to 30% if the home is sold to a first-time home buyer.</p><p>Finally, under the bill, each state receives an annual allocation for the tax credit for the construction of starter homes, for allocation by the state\u2019s housing finance agency to builders (similar to the administration of the low-income housing tax credit).\u00a0</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119hr3475"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3475ih.xml"
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
      "title": "Bipartisan American Homeownership Opportunity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-02T13:58:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bipartisan American Homeownership Opportunity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-02T13:58:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a new first-time homebuyer credit and to establish the starter home construction credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:34Z"
    }
  ]
}
```
