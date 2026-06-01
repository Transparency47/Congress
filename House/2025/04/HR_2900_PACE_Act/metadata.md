# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2900?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2900
- Title: PACE Act
- Congress: 119
- Bill type: HR
- Bill number: 2900
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-03-13T13:30:09Z
- Update date including text: 2026-03-13T13:30:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2900",
    "number": "2900",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "PACE Act",
    "type": "HR",
    "updateDate": "2026-03-13T13:30:09Z",
    "updateDateIncludingText": "2026-03-13T13:30:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:01:10Z",
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
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "IL"
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
      "sponsorshipDate": "2025-12-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2900ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2900\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Ms. Tenney (for herself and Mr. Schneider ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase and make fully refundable the Child and Dependent Care Tax Credit, to increase the maximum amount excludable from gross income for employer-provided dependent care assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Affordable Childcare for Everyone Act or the PACE Act .\n#### 2. Refundability of Child and Dependent Care Tax Credit\n##### (a) In general\nThe Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby redesignating section 21 as section 36C; and\n**(2)**\nby moving section 36C, as so redesignated, from subpart A of part IV of subchapter A of chapter 1 to the location immediately before section 37 in subpart C of part IV of subchapter A of chapter 1.\n##### (b) Technical amendments\n**(1)**\nParagraph (1) of section 23(f) of the Internal Revenue Code of 1986 is amended by striking 21(e) and inserting 36C(e) .\n**(2)**\nParagraph (6) of section 35(g) of such Code is amended by striking 21(e) and inserting 36C(e) .\n**(3)**\nParagraph (1) of section 36C(a) of such Code (as redesignated by subsection (a)) is amended by striking this chapter and inserting this subtitle .\n**(4)**\nSubparagraph (C) of section 129(a)(2) of such Code is amended by striking section 21(e) and inserting section 36C(e) .\n**(5)**\nParagraph (2) of section 129(b) of such Code is amended by striking section 21(d)(2) and inserting section 36C(d)(2) .\n**(6)**\nParagraph (1) of section 129(e) of such Code is amended by striking section 21(b)(2) and inserting section 36C(b)(2) .\n**(7)**\nSubsection (e) of section 213 of such Code is amended by striking section 21 and inserting section 36C .\n**(8)**\nSubparagraph (H) of section 6213(g)(2) of such Code is amended by striking section 21 and inserting section 36C .\n**(9)**\nSubparagraph (L) of section 6213(g)(2) of such Code is amended by inserting 36C, after 32, .\n**(10)**\nParagraph (2) of section 1324(b) of title 31, United States Code, is amended by inserting 36C, after 36B, .\n**(11)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following:\nSec. 36C. Expenses for household and dependent care services necessary for gainful employment. .\n**(12)**\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by striking the item relating to section 21.\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Enhancement of the Child and Dependent Care Tax Credit\n##### (a) In general\nSection 36C of the Internal Revenue Code of 1986, as redesignated by section 2 of this Act, is amended\u2014\n**(1)**\nin paragraph (2) of subsection (a), by striking 35 percent reduced (but not below 20 percent) and inserting 50 percent reduced (but not below 35 percent) ;\n**(2)**\nby striking subsection (g) and redesignating subsection (f) as subsection (g); and\n**(3)**\nby inserting after subsection (e) the following new subsection:\n(f) Inflation adjustment (1) In general In the case of any taxable year beginning after 2025, each of the dollar amounts in subsections (a)(2) and (c) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (2) Rounding If any increase determined under paragraph (1) is not a multiple of $50, such increase shall be rounded to the nearest multiple of $50. .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 4. Increase in exclusion for employer-provided dependent care assistance\n##### (a) In general\nSubparagraph (A) of section 129(a)(2) of the Internal Revenue Code of 1986 (relating to dependent care assistance programs) is amended by striking $5,000 ($2,500 and inserting $7,500 (half such dollar amount .\n##### (b) Inflation adjustment\nParagraph (2) of section 129(a) of such Code is amended by striking subparagraph (D) and inserting the following new subparagraph:\n(D) Inflation adjustment In the case of any taxable year beginning in a calendar year after 2026, the $7,500 amount in subparagraph (A) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. Any increase determined under the preceding sentence shall be rounded to the nearest multiple of $100. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-04-10",
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
        "updateDate": "2025-05-12T20:17:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2900",
          "measure-number": "2900",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2900v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Promoting Affordable Childcare for Everyone Act or the PACE Act </strong></p><p>This bill increases and makes refundable the tax credit for qualified child and dependent care expenses. The bill also increases the exclusion from gross income for employer-provided child and dependent care benefits.</p><p>Under current law, a nonrefundable tax credit is allowed for up to 35% (maximum tax credit percentage) of qualified child and dependent care expenses incurred by an individual to work or look for work, up to a maximum amount. The percentage of such expenses allowed as a tax credit may be reduced, but not below 20% (minimum tax credit percentage), based on an individual\u2019s adjusted gross income.</p><p>The bill generally increases the tax credit for qualified child and dependent care expenses by</p><ul><li>increasing the maximum tax credit percentage to 50%,</li><li>increasing the minimum tax credit percentage to 35%, and</li><li>adjusting the maximum credit amounts\u00a0annually for inflation.</li></ul><p>The bill also makes the tax credit for qualified child and dependent care expenses refundable.</p><p>Finally, the bill increases and adjusts for inflation the amount that may be excluded from gross income for employer-sponsored child and dependent care benefits (e.g., dependent care flexible spending arrangements) to $7,500 (from $5,000).</p>"
        },
        "title": "PACE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2900.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Promoting Affordable Childcare for Everyone Act or the PACE Act </strong></p><p>This bill increases and makes refundable the tax credit for qualified child and dependent care expenses. The bill also increases the exclusion from gross income for employer-provided child and dependent care benefits.</p><p>Under current law, a nonrefundable tax credit is allowed for up to 35% (maximum tax credit percentage) of qualified child and dependent care expenses incurred by an individual to work or look for work, up to a maximum amount. The percentage of such expenses allowed as a tax credit may be reduced, but not below 20% (minimum tax credit percentage), based on an individual\u2019s adjusted gross income.</p><p>The bill generally increases the tax credit for qualified child and dependent care expenses by</p><ul><li>increasing the maximum tax credit percentage to 50%,</li><li>increasing the minimum tax credit percentage to 35%, and</li><li>adjusting the maximum credit amounts\u00a0annually for inflation.</li></ul><p>The bill also makes the tax credit for qualified child and dependent care expenses refundable.</p><p>Finally, the bill increases and adjusts for inflation the amount that may be excluded from gross income for employer-sponsored child and dependent care benefits (e.g., dependent care flexible spending arrangements) to $7,500 (from $5,000).</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119hr2900"
    },
    "title": "PACE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Promoting Affordable Childcare for Everyone Act or the PACE Act </strong></p><p>This bill increases and makes refundable the tax credit for qualified child and dependent care expenses. The bill also increases the exclusion from gross income for employer-provided child and dependent care benefits.</p><p>Under current law, a nonrefundable tax credit is allowed for up to 35% (maximum tax credit percentage) of qualified child and dependent care expenses incurred by an individual to work or look for work, up to a maximum amount. The percentage of such expenses allowed as a tax credit may be reduced, but not below 20% (minimum tax credit percentage), based on an individual\u2019s adjusted gross income.</p><p>The bill generally increases the tax credit for qualified child and dependent care expenses by</p><ul><li>increasing the maximum tax credit percentage to 50%,</li><li>increasing the minimum tax credit percentage to 35%, and</li><li>adjusting the maximum credit amounts\u00a0annually for inflation.</li></ul><p>The bill also makes the tax credit for qualified child and dependent care expenses refundable.</p><p>Finally, the bill increases and adjusts for inflation the amount that may be excluded from gross income for employer-sponsored child and dependent care benefits (e.g., dependent care flexible spending arrangements) to $7,500 (from $5,000).</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119hr2900"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2900ih.xml"
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
      "title": "PACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-30T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-30T03:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Affordable Childcare for Everyone Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-30T03:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to increase and make fully refundable the Child and Dependent Care Tax Credit, to increase the maximum amount excludable from gross income for employer-provided dependent care assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-30T03:48:23Z"
    }
  ]
}
```
