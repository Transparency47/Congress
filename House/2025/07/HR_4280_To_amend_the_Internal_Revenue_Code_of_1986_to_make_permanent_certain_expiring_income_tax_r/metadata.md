# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4280?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4280
- Title: Bipartisan Tax Fairness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4280
- Origin chamber: House
- Introduced date: 2025-07-02
- Update date: 2025-07-29T21:26:56Z
- Update date including text: 2025-07-29T21:26:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-02: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-02: Introduced in House

## Actions

- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-02",
    "latestAction": {
      "actionDate": "2025-07-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4280",
    "number": "4280",
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
    "title": "Bipartisan Tax Fairness Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-29T21:26:56Z",
    "updateDateIncludingText": "2025-07-29T21:26:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-02",
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
      "actionDate": "2025-07-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-02",
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
          "date": "2025-07-02T13:01:15Z",
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
      "sponsorshipDate": "2025-07-02",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4280ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4280\nIN THE HOUSE OF REPRESENTATIVES\nJuly 2, 2025 Mr. Fitzpatrick (for himself and Mr. Golden of Maine ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to make permanent certain expiring income tax rates and to establish a new top income tax rate.\n#### 1. Short title\nThis Act may be cited as the Bipartisan Tax Fairness Act of 2025 .\n#### 2. Modification of income tax rates\n##### (a) Married individuals filing joint returns and surviving spouses\nSection 1(a) of the Internal Revenue Code of 1986 is amended by striking the table contained therein and inserting the following:\nIf taxable income is: The tax is: Not over $19,050 10% of taxable income. Over $19,050 but not over $77,400 $1,905, plus 12% of the excess over $19,050. Over $77,400 but not over $165,000 $8,907, plus 22% of the excess over $77,400. Over $165,000 but not over $315,000 $28,179, plus 24% of the excess over $165,000. Over $315,000 but not over $400,000 $64,179, plus 32% of the excess over $315,000. Over $400,000 but not over $600,000 $91,379, plus 35% of the excess over $400,000. Over $600,000 but not over $2,000,000 $161,379, plus 37% of the excess over $600,000. Over $2,000,000 $679,379, plus 39.6% of the excess over $2,000,000 .\n##### (b) Heads of households\nSection 1(b) of such Code is amended by striking the table contained therein and inserting the following:\nIf taxable income is: The tax is: Not over $13,600 10% of taxable income. Over $13,600 but not over $51,800 $1,360, plus 12% of the excess over $13,600. Over $51,800 but not over $82,500 $5,944, plus 22% of the excess over $51,800. Over $82,500 but not over $157,500 $12,698, plus 24% of the excess over $82,500. Over $157,500 but not over $200,000 $30,698, plus 32% of the excess over $157,500. Over $200,000 but not over $500,000 $44,298, plus 35% of the excess over $200,000. Over $500,000 but not over $1,000,000 $149,298, plus 37% of the excess over $500,000. Over $1,000,000 $334,298, plus 39.6% of the excess over $1,000,000 .\n##### (c) Unmarried individuals other than surviving spouses and heads of households\nSection 1(c) of such Code is amended by striking the table contained therein and inserting the following:\nIf taxable income is: The tax is: Not over $9,525 10% of taxable income. Over $9,525 but not over $38,700 $952.50, plus 12% of the excess over $9,525. Over $38,700 but not over $82,500 $4,453.50, plus 22% of the excess over $38,700. Over $82,500 but not over $157,500 $14,089.50, plus 24% of the excess over $82,500. Over $157,500 but not over $200,000 $32,089.50, plus 32% of the excess over $157,500. Over $200,000 but not over $500,000 $45,689.50, plus 35% of the excess over $200,000. Over $500,000 but not over $1,000,000 $150,689.50, plus 37% of the excess over $500,000. Over $1,000,000 $335,698.50, plus 39.6% of the excess over $1,000,000 .\n##### (d) Married individuals filing separate returns\nSection 1(d) of such Code is amended by striking the table contained therein and inserting the following:\nIf taxable income is: The tax is: Not over $9,525 10% of taxable income. Over $9,525 but not over $38,700 $952.50, plus 12% of the excess over $9,525. Over $38,700 but not over $82,500 $4,453.50, plus 22% of the excess over $38,700. Over $82,500 but not over $157,500 $14,089.50, plus 24% of the excess over $82,500. Over $157,500 but not over $200,000 $32,089.50, plus 32% of the excess over $157,500. Over $200,000 but not over $300,000 $45,689.50, plus 35% of the excess over $200,000. Over $300,000 but not over $1,000,000 $80,689.50, plus 37% of the excess over $300,000. Over $1,000,000 $339,689.50, plus 39.6% of the excess over $1,000,000 .\n##### (e) Estates and trusts\nSection 1(e) of such Code is amended by striking the table contained therein and inserting the following:\nIf taxable income is: The tax is: Not over $2,550 10% of taxable income. Over $2,550 but not over $9,150 $255, plus 24% of the excess over $2,550. Over $9,150 but not over $12,500 $1,839, plus 35% of the excess over $9,150. Over $12,500 $3,011.50, plus 37% of the excess over $12,500. .\n##### (f) Inflation adjustments\nSection 1(f) of such Code is amended\u2014\n**(1)**\nby amending paragraph (2)(A) to read as follows:\n(A) by increasing the minimum and maximum dollar amounts for each bracket for which a tax is imposed under such table by the cost-of-living adjustment for such calendar year, determined under this subsection for such calendar year by substituting \u20182017\u2019 for \u20182016\u2019 in paragraph (3)(A)(ii), ,\n**(2)**\nby amending paragraph (7) to read as follows:\n(7) Rounding (A) In general Except as provided in subparagraph (B), if any increase determined under paragraph (2)(A) is not a multiple of $25, such increase shall be rounded to the next lowest multiple of $25. (B) Joint returns, etc In the case of a table prescribed under subsection (a), subparagraph (A) shall be applied by substituting $50 for $25 both places it appears. ,\n**(3)**\nby striking paragraph (8), and\n**(4)**\nin the heading, by striking Phaseout of marriage penalty in 15-percent bracket; adjustments and inserting Adjustments .\n##### (g) Conforming amendments\n**(1)**\nSection 1 of such Code is amended by striking subsections (i) and (j).\n**(2)**\nSection 3402(q)(1) of such Code is amended by striking third lowest and inserting fourth lowest .\n##### (h) Effective date\n**(1) In general**\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n**(2) Application of section 15**\nSection 15 of such Code shall not apply to any change in a rate of tax by reason of\u2014\n**(A)**\nsection 1(j) of such Code (as in effect before its repeal by this section), or\n**(B)**\nany amendment made by this section.",
      "versionDate": "2025-07-02",
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
        "updateDate": "2025-07-29T21:26:56Z"
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
      "date": "2025-07-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4280ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to make permanent certain expiring income tax rates and to establish a new top income tax rate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T04:31:27Z"
    },
    {
      "title": "Bipartisan Tax Fairness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bipartisan Tax Fairness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T04:23:24Z"
    }
  ]
}
```
