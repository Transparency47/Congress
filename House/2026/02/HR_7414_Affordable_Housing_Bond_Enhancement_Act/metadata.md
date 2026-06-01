# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7414?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7414
- Title: Affordable Housing Bond Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 7414
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-05-08T08:05:47Z
- Update date including text: 2026-05-08T08:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7414",
    "number": "7414",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "Y000067",
        "district": "2",
        "firstName": "Rudy",
        "fullName": "Rep. Yakym, Rudy [R-IN-2]",
        "lastName": "Yakym",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Affordable Housing Bond Enhancement Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:05:47Z",
    "updateDateIncludingText": "2026-05-08T08:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
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
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:05:10Z",
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
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "WI"
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
      "sponsorshipDate": "2026-05-07",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7414ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7414\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Yakym (for himself and Ms. Moore of Wisconsin ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand housing investment with mortgage revenue bonds, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Affordable Housing Bond Enhancement Act .\n##### (b) Amendment of 1986 Code\nExcept as otherwise expressly provided, whenever in this Act an amendment or repeal is expressed in terms of an amendment to, or repeal of, a section or other provision, the reference shall be considered to be made to a section or other provision of the Internal Revenue Code of 1986.\n##### (c) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Reporting requirements for bond usage.\nSec. 3. Use of carryforward bond authority.\nSec. 4. Elimination of refinancing limitation for mortgage revenue bonds.\nSec. 5. Increase in financing limit for qualified home improvement loans.\nSec. 6. Revision of recapture tax for mortgage revenue bonds.\nSec. 7. Modifying calculation of credit for interest paid on certified indebtedness.\nSec. 8. Extension of period for mortgage credit certificate to be in effect.\nSec. 9. Extension of period to revoke election to issue mortgage credit certificates.\nSec. 10. Adjustment of public notice requirement.\nSec. 11. Elimination of lender reporting requirement.\n#### 2. Reporting requirements for bond usage\n##### (a) In general\nSection 146 is amended by adding at the end the following:\n(o) Reporting Not later than December 31 of each calendar year, the Secretary shall submit a report to the Committee on Banking, Housing, and Urban Affairs of the Senate, the Committee on Financial Services of the House of Representatives, the Committee on Ways and Means of the House of Representatives, and the Committee on Finance of the Senate, containing information, as provided to the Secretary by State and local issuing authorities, which specifies for each State\u2014 (1) the State ceiling of the State for the preceding calendar year, (2) the aggregate amount of carryforwards available to all issuing authorities in the State available as of the first day of such preceding calendar year, (3) the total bond authority for such State for such preceding calendar year, as represented by the sum of the amounts reported under paragraphs (1) and (2), (4) the aggregate amount of private activity bonds issued by issuing authorities in the State during such preceding calendar year for each purpose described in subsection (f)(5), including\u2014 (A) the amount of such bonds that were subject to the volume cap, and (B) the amount of such bonds that were issued pursuant to a carryforward under subsection (f), (5) the aggregate amount of carryforwards described in paragraph (2) that expired after the last day of the preceding calendar year, and (6) the total amount of any excess amounts described in paragraph (1) of subsection (f) for the preceding calendar year which issuing authorities in the State did not elect to treat as a carryforward under such subsection. .\n##### (b) Electronic reports by issuers\nSection 149(e) is amended by adding at the end the following new paragraph:\n(4) Electronic reporting Any statement required under paragraph (2) shall be submitted electronically. .\n##### (c) Authority To disclose information\nSection 6103(f) is amended by adding at the end the following new paragraph:\n(6) Volume cap reporting The Secretary may disclose to the committees described in section 146(o) the information required under such section. .\n##### (d) Effective date\nThe amendments made by this section shall apply to calendar years beginning after the date of enactment of this Act.\n#### 3. Use of carryforward bond authority\n##### (a) In general\nParagraph (3) of section 146(f) is amended\u2014\n**(1)**\nby striking subparagraph (A) and inserting the following:\n(A) In general If any issuing authority\u2014 (i) elects a carryforward under paragraph (1) with respect to any carryforward purpose, (ii) receives a carryforward under paragraph (4)(B)(i) with respect to any carryforward purpose, or (iii) redesignates a carryforward under paragraph (4)(B)(ii) for any carryforward purpose, any private activity bonds issued by such authority with respect to such purpose at any time during the 3 calendar years following the calendar year in which the carryforward arose shall not be taken into account under subsection (a) to the extent the amount of such bonds issued at or prior to such time does not exceed the amount of the carryforward elected, received, or redesignated for such purpose, as reduced by any amount subsequently transferred to another issuing authority or redesignated for another purpose pursuant to paragraph (4)(B). , and\n**(2)**\nin subparagraph (B), by inserting , or received or redesignated for, after with respect to .\n##### (b) Election\nParagraph (4) of section 146(f) is amended to read as follows:\n(4) Election (A) In general Except as provided in subparagraph (B), any election under this subsection (and any identification or specification contained therein), once made, shall be irrevocable. (B) Exception for housing (i) Transfer In the case of any carryforward elected under paragraph (1) by an issuing authority with respect to any carryforward purpose, during the period described in paragraph (3)(A) with respect to such carryforward, such issuing authority may transfer such carryforward to any issuing authority within the same State that is authorized to issue qualified mortgage bonds or exempt facility bonds described in section 142(a)(7). (ii) Redesignation In the case of any carryforward\u2014 (I) elected under paragraph (1) by an issuing authority with respect to any carryforward purpose which has not been transferred pursuant to clause (i), or (II) received by an issuing authority pursuant to clause (i) with respect to any carryforward purpose, during the period described in paragraph (3)(A) with respect to such carryforward, such issuing authority may redesignate such carryforward to be for the purpose of issuing qualified mortgage bonds or mortgage credit certificates, or for the purpose of issuing exempt facility bonds described in section 142(a)(7). (iii) State direction In the case of a State which has enacted a law described in subsection (e)(1), such State may, by law, prohibit, limit, require, or otherwise direct transfer or redesignation by issuing authorities within such State (except in the case of a constitutional home rule city) pursuant to this subparagraph. .\n##### (c) Effective date\nThe amendments made by this section shall apply to elections made under section 146(f) of the Internal Revenue Code of 1986 after December 31, 2025.\n#### 4. Elimination of refinancing limitation for mortgage revenue bonds\n##### (a) In general\nSection 143(i)(1) is amended by adding at the end the following:\n(D) Exception for refinancing for certain mortgagors (i) In general The refinancing of a mortgage on a residence of a mortgagor who, as of the date of such refinancing, satisfies the principal residence requirements under subsection (c)(1) and the income requirements under subsection (f) shall not be treated as the acquisition or replacement of an existing mortgage for purposes of subparagraph (A). (ii) Special rule In applying clause (i) to any refinancing\u2014 (I) subsection (d) shall not apply, and (II) subsection (e) shall be applied by using the market value of the residence at the time of refinancing in lieu of the acquisition cost. .\n##### (b) Effective date\nThe amendment made by this section shall apply to refinancing loans made on or after the date of enactment of this Act.\n#### 5. Increase in financing limit for qualified home improvement loans\n##### (a) Increase in financing limit\nParagraph (4) of section 143(k) is amended by striking $15,000 and inserting $75,000 .\n##### (b) Inflation adjustment\nParagraph (4) of section 143(k), as amended by subsection (a), is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and by moving such clauses (as so redesignated) 2 ems to the right,\n**(2)**\nby striking The term and inserting the following:\n(A) In general The term , and\n**(3)**\nby adding at the end the following:\n(B) Inflation adjustment (i) In general In the case of any calendar year beginning after 2026, the $75,000 amount in subparagraph (A) shall be increased by an amount equal to\u2014 (I) such dollar amount, multiplied by (II) the cost-of-living adjustment determined under section 1(f)(3) for such calendar year, determined by substituting 2024 for 2016 in subparagraph (A)(ii) thereof. (ii) Rounding If any increase under clause (i) is not a multiple of $100, such increase shall be rounded to the nearest multiple of $100. .\n##### (c) Effective dates\nThe amendments made by this section shall apply to loans made after the last day of the calendar year which includes the date of the enactment of this Act.\n#### 6. Revision of recapture tax for mortgage revenue bonds\n##### (a) In general\nSubparagraph (C) of section 143(m)(4) is amended to read as follows:\n(C) Holding period percentage (i) In general The term holding period percentage means the percentage determined in accordance with the following table: If the disposition occurs during a year after the testing date which is: The holding period percentage is: The 1st such year 20 The 2nd such year 40 The 3rd such year 60 The 4th such year 80 The 5th such year 100 (ii) Retirements of indebtedness If the Federally subsidized indebtedness is completely repaid during any year of the 4-year period beginning on the testing date, the holding period percentage for succeeding years shall be zero. .\n##### (b) Conforming amendments\n**(1)**\nSection 143(m)(2)(B) is amended by striking 9 years and inserting 5 years .\n**(2)**\nSection 143(m)(7)(B)(ii) is amended by striking 9-year period and inserting 5-year period .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 7. Modifying calculation of credit for interest paid on certified indebtedness\n##### (a) In general\nSection 25 is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking subparagraph (B) and inserting the following:\n(B) the certified indebtedness amount on which interest was paid or accrued by the taxpayer during the taxable year. , and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the heading, by striking where credit rate exceeds 20 percent , and\n**(ii)**\nin subparagraph (A), by striking If the certificate credit rate exceeds 20 percent, the and inserting The , and\n**(2)**\nin subsection (d)\u2014\n**(A)**\nby striking paragraph (1) and inserting the following:\n(1) In general (A) Certificate credit rate The certificate credit rate specified in any mortgage credit certificate shall not be less than 1 percent or more than 5 percent. (B) Annual rate With respect to any mortgage credit certificate, the issuing authority may elect to specify a different annual certificate credit rate for each year of the term of the mortgage. , and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the heading, by striking certificate credit rates and inserting amount of credit certificates , and\n**(ii)**\nin subparagraph (A)(ii), by inserting average annual before certificate credit rate .\n##### (b) Effective date\nThe amendments made by this section shall apply to mortgage credit certificates issued on or after the first day of the second calendar year that begins after the date of the enactment of this Act.\n#### 8. Extension of period for mortgage credit certificate to be in effect\n##### (a) In general\nSection 25(e)(3)(B) is amended by striking second and inserting fourth .\n##### (b) Effective date\nThe amendment made by this section shall apply to mortgage credit certificates with respect to which the limitation under section 25(d)(2)(A) of the Internal Revenue Code of 1986 is determined by reference to nonissued bond amounts (a defined in section 25(d)(2)(B) of such Code) relating to calendar years after December 31, 2025.\n#### 9. Extension of period to revoke election to issue mortgage credit certificates\n##### (a) In general\nSection 25(c)(2) is amended by adding at the end the following:\n(C) Revocation of election to issue mortgage credit certificates (i) In general For purposes of any election made by an issuing authority under subparagraph (A)(ii) during any calendar year, such issuing authority may subsequently elect to reduce the nonissued bond amount (as defined in subsection (d)(2)(B)) for such calendar year, provided that such election is made not later than the end of the succeeding calendar year. (ii) Coordination with private activity bond carryforward limitation Under rules established by the Secretary, nothing in clause (i) shall be construed to permit an issuing authority to issue bonds under section 146(f)(3) for a calendar year after the close of the period prescribed for issuing such bonds under such section. .\n##### (b) Effective date\nThe amendment made by this section shall apply to elections made by an issuing authority under section 25(c)(2)(A)(ii) of the Internal Revenue Code of 1986 after December 31, 2025.\n#### 10. Adjustment of public notice requirement\n##### (a) In general\nSection 25(e)(5) is amended by striking 90 days and inserting 30 days .\n##### (b) Effective date\nThe amendment made by this section shall apply to notices provided after December 31, 2025.\n#### 11. Elimination of lender reporting requirement\n##### (a) In general\nSection 25(g) is amended\u2014\n**(1)**\nby striking each person who makes a loan which is a certified indebtedness amount under any mortgage credit certificate and inserting each person who issues a mortgage credit certificate , and\n**(2)**\nby striking the second sentence thereof.\n##### (b) Conforming amendments\nSection 6709(c) is amended by striking In the case of any report required under the second sentence of section 25(g), the and inserting The .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date of enactment of this Act.",
      "versionDate": "2026-02-09",
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
        "actionDate": "2025-10-21",
        "text": "Committee on Banking, Housing, and Urban Affairs. Hearings held."
      },
      "number": "1511",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Affordable Housing Bond Enhancement Act",
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
        "updateDate": "2026-02-17T17:45:52Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7414ih.xml"
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
      "title": "Affordable Housing Bond Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affordable Housing Bond Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to expand housing investment with mortgage revenue bonds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:03:39Z"
    }
  ]
}
```
