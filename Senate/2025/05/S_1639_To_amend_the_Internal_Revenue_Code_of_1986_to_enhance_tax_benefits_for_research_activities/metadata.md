# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1639?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1639
- Title: American Innovation and Jobs Act
- Congress: 119
- Bill type: S
- Bill number: 1639
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-06-06T18:13:36Z
- Update date including text: 2025-06-06T18:13:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1639",
    "number": "1639",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "American Innovation and Jobs Act",
    "type": "S",
    "updateDate": "2025-06-06T18:13:36Z",
    "updateDateIncludingText": "2025-06-06T18:13:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T19:31:35Z",
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
      "sponsorshipDate": "2025-05-07",
      "state": "NH"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "OK"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NH"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "MT"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "VA"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "WY"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NV"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "NC"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MI"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "KS"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "AL"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "WA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "LA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "NE"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "AZ"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "AL"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "VA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "WV"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NV"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "NE"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "WI"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "KS"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NM"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "TN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "DE"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "OK"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MI"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "MS"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-05-07",
      "state": "ME"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "NC"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "GA"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "OH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1639is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1639\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Young (for himself, Ms. Hassan , Mr. Lankford , Mrs. Shaheen , Mr. Daines , Mr. Warner , Mr. Barrasso , Ms. Rosen , Mr. Tillis , Mr. Peters , Mr. Marshall , Mr. Padilla , Mr. Tuberville , Mrs. Murray , Mr. Kennedy , Ms. Klobuchar , Mr. Ricketts , Mr. Kelly , Mrs. Britt , Mr. Kaine , Mrs. Capito , Ms. Cortez Masto , Mrs. Fischer , Ms. Baldwin , Mr. Moran , Mr. Luj\u00e1n , Mr. Hagerty , Mr. Coons , Mr. Mullin , Ms. Slotkin , Mr. Wicker , Mr. King , Mr. Budd , Mr. Ossoff , Mr. Husted , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to enhance tax benefits for research activities.\n#### 1. Short title\nThis Act may be cited as the American Innovation and Jobs Act .\n#### 2. Restoring immediate expensing for research and development investments\n##### (a) In general\nSection 174 of the Internal Revenue Code of 1986 is amended to read as follows:\n174. Research and experimental expenditures (a) Treatment as Expenses (1) In general A taxpayer may treat research or experimental expenditures which are paid or incurred by him during the taxable year in connection with his trade or business as expenses which are not chargeable to capital account. The expenditures so treated shall be allowed as a deduction. (2) When method may be adopted (A) Without consent A taxpayer may, without the consent of the Secretary, adopt the method provided in this subsection for his first taxable year for which expenditures described in paragraph (1) are paid or incurred. (B) With consent A taxpayer may, with the consent of the Secretary, adopt at any time the method provided in this subsection. (3) Scope The method adopted under this subsection shall apply to all expenditures described in paragraph (1). The method adopted shall be adhered to in computing taxable income for the taxable year and for all subsequent taxable years unless, with the approval of the Secretary, a change to a different method is authorized with respect to part or all of such expenditures. (b) Amortization of Certain Research and Experimental Expenditures (1) In general At the election of the taxpayer, made in accordance with regulations prescribed by the Secretary, research or experimental expenditures which are\u2014 (A) paid or incurred by the taxpayer in connection with his trade or business, (B) not treated as expenses under subsection (a), and (C) chargeable to capital account but not chargeable to property of a character which is subject to the allowance under section 167 (relating to allowance for depreciation, etc.) or section 611 (relating to allowance for depletion), may be treated as deferred expenses. In computing taxable income, such deferred expenses shall be allowed as a deduction ratably over such period of not less than 60 months as may be selected by the taxpayer (beginning with the month in which the taxpayer first realizes benefits from such expenditures). Such deferred expenses are expenditures properly chargeable to capital account for purposes of section 1016(a)(1) (relating to adjustments to basis of property). (2) Time for and scope of election The election provided by paragraph (1) may be made for any taxable year, but only if made not later than the time prescribed by law for filing the return for such taxable year (including extensions thereof). The method so elected, and the period selected by the taxpayer, shall be adhered to in computing taxable income for the taxable year for which the election is made and for all subsequent taxable years unless, with the approval of the Secretary, a change to a different method (or to a different period) is authorized with respect to part or all of such expenditures. The election shall not apply to any expenditure paid or incurred during any taxable year before the taxable year for which the taxpayer makes the election. (c) Land and Other Property This section shall not apply to any expenditure for the acquisition or improvement of land, or for the acquisition or improvement of property to be used in connection with the research or experimentation and of a character which is subject to the allowance under section 167 (relating to allowance for depreciation, etc.) or section 611 (relating to allowance for depletion); but for purposes of this section allowances under section 167, and allowances under section 611, shall be considered as expenditures. (d) Exploration Expenditures This section shall not apply to any expenditure paid or incurred for the purpose of ascertaining the existence, location, extent, or quality of any deposit of ore or other mineral (including oil and gas). (e) Only Reasonable Research Expenditures Eligible This section shall apply to a research or experimental expenditure only to the extent that the amount thereof is reasonable under the circumstances. (f) Cross References (1) For adjustments to basis of property for amounts allowed as deductions as deferred expenses under subsection (b), see section 1016(a)(14). (2) For election of 10-year amortization of expenditures allowable as a deduction under subsection (a), see section 59(e). .\n##### (b) Clerical Amendment\nThe table of sections for part VI of subchapter B of chapter 1 is amended by striking the item relating to section 174 and inserting the following new item:\nSec. 174. Research and experimental expenditures .\n##### (c) Conforming Amendments\n**(1)**\nSection 41(d)(1)(A) is amended by striking specified research or experimental expenditures under section 174 and inserting expenses under section 174 .\n**(2)**\nSection 280C(c) is amended to read as follows:\n(c) Credit for Increasing Research Activities (1) In general No deduction shall be allowed for that portion of the qualified research expenses (as defined in section 41(b)) or basic research expenses (as defined in section 41(e)(2)) otherwise allowable as a deduction for the taxable year which is equal to the amount of the credit determined for such taxable year under section 41(a). (2) Similar rule where taxpayer capitalizes rather than deducts expenses If\u2014 (A) the amount of the credit determined for the taxable year under section 41(a)(1), exceeds (B) the amount allowable as a deduction for such taxable year for qualified research expenses or basic research expenses (determined without regard to paragraph (1)), the amount chargeable to capital account for the taxable year for such expenses shall be reduced by the amount of such excess. (3) Election of reduced credit (A) In general In the case of any taxable year for which an election is made under this paragraph\u2014 (i) paragraphs (1) and (2) shall not apply, and (ii) the amount of the credit under section 41(a) shall be the amount determined under subparagraph (B). (B) Amount of reduced credit The amount of credit determined under this subparagraph for any taxable year shall be the amount equal to the excess of\u2014 (i) the amount of credit determined under section 41(a) without regard to this paragraph, over (ii) the product of\u2014 (I) the amount described in clause (i), and (II) the rate of tax under section 11(b). (C) Election An election under this paragraph for any taxable year shall be made not later than the time for filing the return of tax for such year (including extensions), shall be made on such return, and shall be made in such manner as the Secretary may prescribe. Such an election, once made, shall be irrevocable. (4) Controlled groups Paragraph (3) of subsection (b) shall apply for purposes of this subsection. .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred in taxable years beginning after December 31, 2021.\n#### 3. Expanding refundable research credit for new and small businesses\n##### (a) Increasing cap on refundable credit\n**(1) In general**\nSubclause (I) of section 41(h)(4)(B)(i) of the Internal Revenue Code of 1986 is amended by striking $250,000 and inserting the applicable amount .\n**(2) Applicable amount**\nSubclause (II) of section 41(h)(4)(B)(i) of such Code is amended to read as follows:\n(II) Applicable amount For purposes of subclause (I), the applicable amount is\u2014 (aa) in the case of any taxable year beginning after December 31, 2024, and before January 1, 2026, $500,000, (bb) in the case of any taxable year beginning after December 31, 2025, and before January 1, 2027, $525,000, (cc) in the case of any taxable year beginning after December 31, 2026, and before January 1, 2028, $550,000, (dd) in the case of any taxable year beginning after December 31, 2027, and before January 1, 2029, $575,000, (ee) in the case of any taxable year beginning after December 31, 2028, and before January 1, 2030, $600,000, (ff) in the case of any taxable year beginning after December 31, 2029, and before January 1, 2031, $625,000, (gg) in the case of any taxable year beginning after December 31, 2030, and before January 1, 2032, $650,000, (hh) in the case of any taxable year beginning after December 31, 2031, and before January 1, 2033, $675,000, (ii) in the case of any taxable year beginning after December 31, 2032, and before January 1, 2034, $700,000, (jj) in the case of any taxable year beginning after December 31, 2033, and before January 1, 2035, $725,000, and (kk) in the case of any taxable year beginning after December 31, 2034, $750,000. .\n**(3) Conforming amendments**\n**(A)**\nClause (ii) of section 41(h)(5)(B) of such Code is amended by striking each of the $250,000 amounts and inserting the applicable amount .\n**(B)**\nSection 3111(f) of such Code is amended\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nby striking (applied without regard to subclause (II) thereof), and and inserting a period,\n**(II)**\nby striking subparagraph (B), and\n**(III)**\nby striking for a taxable year and all that follows through allowed as a credit and inserting for a taxable year, there shall be allowed as a credit ,\n**(ii)**\nin paragraph (2)\u2014\n**(I)**\nby striking paragraph (1)(A) and inserting paragraph (1) , and\n**(II)**\nby striking , and the credit allowed by paragraph (1)(B) shall not exceed the tax imposed by subsection (b) for any calendar quarter, , and\n**(iii)**\nin paragraph (4)\u2014\n**(I)**\nby striking credits and inserting credit , and\n**(II)**\nby striking or (b) .\n##### (b) Extension of eligibility and applicability of election\n**(1) Startup date**\nSubclause (II) of section 41(h)(3)(A)(i) of the Internal Revenue Code of 1986 is amended by striking 5-taxable-year period and inserting 8-taxable-year period .\n**(2) Extension of limitation on election**\nClause (ii) of section 41(h)(4)(B) of such Code is amended by striking 5 or more and inserting 8 or more .\n##### (c) Gross receipts test\nClause (i) of section 41(h)(3)(A) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking $5,000,000 in subclause (I) and inserting $15,000,000 , and\n**(2)**\nby striking gross receipts in subclause (II) and inserting gross receipts in excess of $25,000 .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n#### 4. Increasing access to the research credit for startups\n##### (a) In general\nParagraph (4) of section 41(c) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(D) Special rules for qualified small businesses In the case of a qualified small business (as defined in subsection (h)(3))\u2014 (i) subparagraph (A) shall be applied by substituting 20 percent for 14 percent , and (ii) if subparagraph (B) applies to such taxpayer, at the election of the taxpayer\u2014 (I) subparagraph (B)(ii) shall be applied by substituting 10 percent for 6 percent , or (II) in lieu of applying subparagraph (B), the average under subparagraph (A) shall be determined by disregarding any taxable year in the 3-year period described in such subparagraph in which there were no qualified research expenses. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-05-07",
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
        "actionDate": "2025-03-10",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1990",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Innovation and R&D Competitiveness Act of 2025",
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
        "updateDate": "2025-06-06T18:13:36Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1639is.xml"
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
      "title": "American Innovation and Jobs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Innovation and Jobs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to enhance tax benefits for research activities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:27Z"
    }
  ]
}
```
