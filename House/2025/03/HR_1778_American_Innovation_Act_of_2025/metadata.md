# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1778?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1778
- Title: American Innovation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1778
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-04-15T01:36:32Z
- Update date including text: 2026-04-15T01:36:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1778",
    "number": "1778",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "American Innovation Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-15T01:36:32Z",
    "updateDateIncludingText": "2026-04-15T01:36:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:02:30Z",
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
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "NE"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "KS"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "WV"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "TN"
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
      "sponsorshipDate": "2026-02-20",
      "state": "UT"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "TN"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "GA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NY"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NE"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "VA"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "TX"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1778ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1778\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Buchanan (for himself, Mr. Kelly of Pennsylvania , Mr. Smith of Nebraska , Mr. Estes , Mrs. Miller of West Virginia , and Mr. Miller of Ohio ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to promote new business innovation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Innovation Act of 2025 .\n#### 2. Simplification and expansion of deduction for start-up and organizational expenditures\n##### (a) In general\nSection 195 of the Internal Revenue Code of 1986 is amended by redesignating subsections (c) and (d) as subsections (d) and (e), respectively, and by striking all that precedes subsection (d) (as so redesignated) and inserting the following:\n195. Start-up and organizational expenditures (a) Capitalization of expenditures Except as otherwise provided in this section, no deduction shall be allowed for start-up or organizational expenditures. (b) Election To deduct (1) In general If a taxpayer elects the application of this subsection with respect to any active trade or business\u2014 (A) the taxpayer shall be allowed a deduction for the taxable year in which such active trade or business begins in an amount equal to the lesser of\u2014 (i) the aggregate amount of start-up and organizational expenditures paid or incurred in connection with such active trade or business, or (ii) $20,000, reduced (but not below zero) by the amount by which such aggregate amount exceeds $120,000, and (B) the remainder of such start-up and organizational expenditures shall be charged to capital account and allowed as an amortization deduction determined by amortizing such expenditures ratably over the 180-month period beginning with the month in which the active trade or business begins. (2) Application to organizational expenditures In the case of organizational expenditures with respect to any corporation or partnership, the active trade or business referred to in paragraph (1) means the first active trade or business carried on by such corporation or partnership. (3) Inflation adjustment In the case of any taxable year beginning after December 31, 2026, the $20,000 and $120,000 amounts in paragraph (1)(A)(ii) shall each be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. If any amount as increased under the preceding sentence is not a multiple of $1,000, such amount shall be rounded to the nearest multiple of $1,000. (c) Allowance of deduction upon liquidation or disposition (1) Liquidation of partnership or corporation If any partnership or corporation is completely liquidated by the taxpayer, any start-up or organizational expenditures paid or incurred in connection with such partnership or corporation which were not allowed as a deduction by reason of this section may be deducted to the extent allowable under section 165. (2) Disposition of trade or business If any trade or business is completely disposed of or discontinued by the taxpayer, any start-up expenditures paid or incurred in connection with such trade or business which were not allowed as a deduction by reason of this section (and not taken into account in connection with a liquidation to which paragraph (1) applies) may be deducted to the extent allowable under section 165. For purposes of this paragraph, in the case of any deduction allowed under subsection (b)(1) with respect to both start-up and organizational expenditures, the amount treated as so allowed with respect to start-up expenditures shall bear the same ratio to such deduction as the start-up expenditures taken into account in determining such deduction bears to the aggregate of the start-up and organizational expenditures so taken into account. .\n##### (b) Organizational expenditures\nSection 195(d) of such Code, as redesignated by subsection (a), is amended by adding at the end the following new paragraphs:\n(3) Organizational expenditures The term organizational expenditures means any expenditure which\u2014 (A) is incident to the creation of a corporation or a partnership, (B) is chargeable to capital account, and (C) is of a character which, if expended incident to the creation of a corporation or a partnership having an ascertainable life, would be amortizable over such life. (4) Application to certain disregarded entities In the case of any entity with a single owner that is disregarded as an entity separate from its owner, this section shall be applied in the same manner as if such entity were a corporation. .\n##### (c) Election\nSection 195(e)(2) of such Code, as redesignated by subsection (a), is amended to read as follows:\n(2) Partnerships and S corporations In the case of any partnership or S corporation, the election under subsection (b) shall be made (and this section shall be applied) at the entity level. .\n##### (d) Conforming amendments\n**(1)**\n**(A)**\nPart VIII of subchapter B of chapter 1 is amended by striking section 248 of such Code (and by striking the item relating to such section in the table of sections of such part).\n**(B)**\nSection 170(b)(2)(D)(ii) of such Code is amended by striking (except section 248) .\n**(C)**\nSection 312(n)(3) of such Code is amended by striking Sections 173 and 248 and inserting Sections 173 and 195 .\n**(D)**\nSection 535(b)(3) of such Code is amended by striking (except section 248) .\n**(E)**\nSection 545(b)(3) of such Code is amended by striking (except section 248) .\n**(F)**\nSection 545(b)(4) of such Code is amended by striking (except section 248) .\n**(G)**\nSection 834(c)(7) of such Code is amended by striking (except section 248) .\n**(H)**\nSection 852(b)(2)(C) of such Code is amended by striking (except section 248) .\n**(I)**\nSection 857(b)(2)(A) of such Code is amended by striking (except section 248) .\n**(J)**\nSection 1363(b) of such Code is amended by adding and at the end of paragraph (2), by striking paragraph (3), and by redesignating paragraph (4) as paragraph (3).\n**(K)**\nSection 1375(b)(1)(B)(i) of such Code is amended by striking (other than the deduction allowed by section 248, relating to organization expenditures) .\n**(2)**\n**(A)**\nSection 709 of such Code is amended to read as follows:\n709. Treatment of syndication fees No deduction shall be allowed under this chapter to a partnership or to any partner of the partnership for any amounts paid or incurred to promote the sale of (or to sell) an interest in the partnership. .\n**(B)**\nThe item relating to section 709 in the table of sections for part I of subchapter K of chapter 1 of such Code is amended to read as follows:\nSec. 709. Treatment of syndication fees. .\n**(3)**\nSection 1202(e)(2)(A) of such Code is amended by striking section 195(c)(1)(A) and inserting section 195(d)(1)(A) .\n**(4)**\nThe item relating to section 195 in the table of contents of part VI of subchapter B of chapter 1 of such Code is amended to read as follows:\nSec. 195. Start-up and organizational expenditures. .\n##### (e) Effective date\nThe amendments made by this section shall apply to expenditures paid or incurred in connection with active trades or businesses which begin in taxable years beginning after December 31, 2025.\n#### 3. Preservation of start-up net operating losses and tax credits after ownership change\n##### (a) Application to net operating losses\nSection 382(d) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(4) Exception for start-up losses (A) In general In the case of any net operating loss carryforward described in paragraph (1)(A) which arose in a start-up period taxable year, the amount of such net operating loss carryforward otherwise taken into account under such paragraph shall be reduced by the net start-up loss determined with respect to the trade or business referred to in subparagraph (B)(i) for such start-up period taxable year. (B) Start-up period taxable year The term start-up period taxable year means any taxable year of the old loss corporation which\u2014 (i) begins before the close of the 3-year period beginning on the date on which any trade or business of such corporation begins as an active trade or business (as determined under section 195(d)(2) without regard to subparagraph (B) thereof), and (ii) ends after January 31, 2026. (C) Net start-up loss (i) In general The term net start-up loss means, with respect to any trade or business referred to in subparagraph (B)(i) for any start-up period taxable year, the amount which bears the same ratio (but not greater than 1) to the net operating loss carryforward which arose in such start-up period taxable year as\u2014 (I) the net operating loss (if any) which would have been determined for such start-up period taxable year if only items of income, gain, deduction, and loss properly allocable to such trade or business were taken into account, bears to (II) the amount of the net operating loss determined for such start-up period taxable year. (ii) Special rule for last taxable year in start-up period In the case of any start-up period taxable year which ends after the close of the 3-year period described in subparagraph (B)(i) with respect to any trade or business, the net start-up loss with respect to such trade or business for such start-up period taxable year shall be the same proportion of such loss (determined without regard to this clause) as the proportion of such start-up period taxable year which is on or before the last day of such period. (D) Application to net operating loss arising in year of ownership change Subparagraph (A) shall apply to any net operating loss described in paragraph (1)(B) in the same manner as such subparagraph applies to net operating loss carryforwards described in paragraph (1)(A), but by only taking into account the amount of such net operating loss (and the amount of the net start-up loss) which is allocable under paragraph (1)(B) to the period described in such paragraph. Proper adjustment in the allocation of the net start-up loss under the preceding sentence shall be made in the case of a taxable year to which subparagraph (C)(ii) applies. (E) Application to taxable years which are start-up period taxable years with respect to more than 1 trade or business In the case of any net operating loss carryforward which arose in a taxable year which is a start-up period taxable year with respect to more than 1 trade or business\u2014 (i) this paragraph shall be applied separately with respect to each such trade or business, and (ii) the aggregate reductions under subparagraph (A) shall not exceed such net operating loss carryforward. (F) Continuity of business requirement If the new loss corporation does not continue the trade or business referred to in subparagraph (B)(i) at all times during the 2-year period beginning on the change date, this paragraph shall not apply with respect to such trade or business. (G) Certain title 11 or similar cases (i) Multiple ownership changes In the case of a 2nd ownership change to which subsection (l)(5)(D) applies, this paragraph shall not apply for purposes of determining the pre-change loss with respect to such 2nd ownership change. (ii) Certain insolvency transactions If subsection (l)(6) applies for purposes of determining the value of the old loss corporation under subsection (e), this paragraph shall not apply. (H) Not applicable to disallowed interest This paragraph shall not apply for purposes of applying the rules of paragraph (1) to the carryover of disallowed interest under paragraph (3). (I) Transition rule This paragraph shall not apply with respect to any trade or business if the date on which such trade or business begins as an active trade or business (as determined under section 195(d)(2) without regard to subparagraph (B) thereof) is on or before January 31, 2026. .\n##### (b) Application To excess credits\nSection 383 of such Code is amended by redesignating subsection (e) as subsection (f) and by inserting after subsection (d) the following new subsection:\n(e) Exception for start-Up excess credits (1) In general In the case of any unused general business credit of the corporation under section 39 which arose in a start-up period taxable year, the amount of such unused general business credit otherwise taken into account under subsection (a)(2)(A) shall be reduced by the start-up excess credit determined with respect to any trade or business referred to in section 382(d)(4)(B)(i) for such start-up period taxable year. (2) Start-up period taxable year For purposes of this subsection, the term start-up period taxable year has the meaning given such term in section 382(d)(4)(B). (3) Start-up excess credit For purposes of this subsection, the term start-up excess credit means, with respect to any trade or business referred to in section 382(d)(4)(B)(i) for any start-up period taxable year, the amount which bears the same ratio to the unused general business credit which arose in such start-up period taxable year as\u2014 (A) the amount of the general business credit which would have been determined for such start-up period taxable year if only credits properly allocable to such trade or business were taken into account, bears to (B) the amount of the general business credit determined for such start-up period taxable year. (4) Application of certain rules Rules similar to the rules of subparagraphs (C)(ii), (D), (E), and (F) of section 382(d)(4) shall apply for purposes of this subsection. (5) Transition rule This subsection shall not apply with respect to any trade or business if the date on which such trade or business begins as an active trade or business (as determined under section 195(d)(2) without regard to subparagraph (B) thereof) is on or before January 31, 2026. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years ending after January 31, 2025.",
      "versionDate": "2025-03-03",
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
        "actionDate": "2026-03-25",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4207",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Innovation Act of 2026",
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
        "name": "Taxation",
        "updateDate": "2025-05-07T15:50:05Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1778ih.xml"
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
      "title": "American Innovation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Innovation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T02:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to promote new business innovation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T02:48:20Z"
    }
  ]
}
```
