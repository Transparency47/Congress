# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4639?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4639
- Title: Infertility Treatment Affordability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4639
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-11-01T08:05:32Z
- Update date including text: 2025-11-01T08:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4639",
    "number": "4639",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Infertility Treatment Affordability Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-01T08:05:32Z",
    "updateDateIncludingText": "2025-11-01T08:05:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:03:25Z",
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "OH"
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
      "sponsorshipDate": "2025-07-23",
      "state": "OH"
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
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4639ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4639\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Carey (for himself, Mr. Landsman , and Mr. Miller of Ohio ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide an income tax credit for the costs of infertility treatments.\n#### 1. Short title\nThis Act may be cited as the Infertility Treatment Affordability Act of 2025 .\n#### 2. Credit for infertility treatments\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 24 the following new section:\n23A. Credit for infertility treatments (a) Allowance of credit In the case of an eligible individual, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to 50 percent of the qualified infertility treatment expenses paid or incurred during the taxable year. (b) Limitations (1) Dollar limitation The amount of the credit under subsection (a) for any taxable year shall not exceed the excess (if any) of\u2014 (A) the dollar amount in effect under section 23(b)(1) for the taxable year, over (B) the aggregate amount of the credits allowed under subsection (a) for all preceding taxable years. (2) Income limitation (A) In general The amount otherwise allowable as a credit under subsection (a) for any taxable year (determined after the application of paragraph (1) and without regard to this paragraph and subsection (c)) shall be reduced (but not below zero) by an amount which bears the same ratio to the amount so allowable as\u2014 (i) the amount (if any) by which the taxpayer\u2019s adjusted gross income exceeds the dollar amount in effect under clause (i) of section 23(b)(2)(A), bears to (ii) $40,000. (B) Determination of adjusted gross income For purposes of subparagraph (A), adjusted gross income shall be determined without regard to sections 911, 931, and 933. (3) Portion of credit refundable (A) In general So much of the credit allowed under subsection (a) for any taxable year (determined after the applications of paragraphs (1) and (2)) as does not exceed $5,000 shall be treated as a credit allowed under subpart C and not as a credit allowed under this subpart. (B) Adjustments for inflation (i) In general In the case of a taxable year beginning after December 31, 2025, the $5,000 amount in subparagraph (A) shall be increased by an amount equal to\u2014 (I) such dollar amount, multiplied by (II) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (ii) Rounding If any amount as increased under clause (i) is not a multiple of $10, such amount shall be rounded to the nearest multiple of $10. (4) Denial of double benefit (A) In general Any qualified infertility treatment expense taken into account for purposes of any deduction (or any credit other than the credit allowed under this section) shall be reduced by the amount of the credit allowed under subsection (a) with respect to such expense. (B) Grants No credit shall be allowed under subsection (a) for any expense to the extent that reimbursement or other funds in compensation for such expense are received under any Federal, State, or local program. (C) Insurance reimbursement No credit shall be allowed under subsection (a) for any expense to the extent that payment for such expense is made, or reimbursement for such expense is received, under any insurance policy. (c) Carryforwards of unused credit (1) In general If the portion of the credit allowable under subsection (a) which is allowed under this subpart exceeds the limitation imposed by section 26(a) for such taxable year reduced by the sum of the credits allowable under this subpart (other than this section and section 25D), such excess shall be carried to the succeeding taxable year and added to the credit allowable under subsection (a) for such succeeding taxable year. (2) Limitation No credit may be carried forward under this subsection to any taxable year after the 5th taxable year after the taxable year in which the credit arose. For purposes of the preceding sentence, credits shall be treated as used on a first-in, first-out basis. (d) Qualified infertility treatment expenses For purposes of this section\u2014 (1) In general The term qualified infertility treatment expenses means amounts paid or incurred for the treatment of infertility if such treatment is provided\u2014 (A) by a physician, or other medical practitioner, licensed in the United States, and (B) pursuant to a diagnosis of infertility by a physician licensed in the United States. (2) Treatments in advance of infertility arising from medical treatments For purposes of this section: (A) In general In the case of expenses incurred in advance of a diagnosis of infertility for fertility preservation procedures which are conducted prior to medical procedures that, as determined by a physician licensed in the United States, may cause involuntary infertility or sterilization, such expenses shall be treated as qualified infertility treatment expenses\u2014 (i) notwithstanding paragraph (1)(B), and (ii) without regard to whether a diagnosis of infertility subsequently results. (B) Exception for procedures designed to result in infertility Expenses for fertility preservation procedures in advance of a procedure designed to result in infertility or sterilization shall not be treated as qualified infertility treatment expenses. (3) Infertility The term infertility \u2014 (A) means the inability to conceive or to carry a pregnancy to live birth, (B) includes iatrogenic infertility resulting from medical treatments such as chemotherapy, radiation, or surgery, and (C) does not include infertility or sterilization resulting from a procedure designed for such purpose. (e) Eligible individual For purposes of this section, the term eligible individual means an individual\u2014 (1) who has been diagnosed with infertility by a physician licensed in the United States, or (2) with respect to whom a physician licensed in the United States has made the determination described in subsection (d)(2)(A). (f) Married couples must file joint returns Rules similar to the rules of paragraphs (2), (3), and (4) of section 21(e) shall apply for purposes of this section. .\n##### (b) Conforming amendments\n**(1)**\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before the item relating to section 24 the following new item:\nSec. 23A. Credit for infertility treatments. .\n**(2)**\nSection 23(c)(1) of such Code is amended by striking section 25D and inserting sections 23A and 25D .\n**(3)**\nSection 25(e)(1)(C) of such Code is amended by inserting , 23A, after 23 .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-07-23",
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
        "updateDate": "2025-08-07T15:41:28Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4639ih.xml"
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
      "title": "Infertility Treatment Affordability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Infertility Treatment Affordability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide an income tax credit for the costs of infertility treatments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:29Z"
    }
  ]
}
```
