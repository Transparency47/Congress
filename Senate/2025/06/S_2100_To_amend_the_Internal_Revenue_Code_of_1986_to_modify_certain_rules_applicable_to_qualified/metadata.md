# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2100?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2100
- Title: Modernizing Agricultural and Manufacturing Bonds Act
- Congress: 119
- Bill type: S
- Bill number: 2100
- Origin chamber: Senate
- Introduced date: 2025-06-17
- Update date: 2026-01-15T12:03:40Z
- Update date including text: 2026-01-15T12:03:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in Senate
- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Read twice and referred to the Committee on Finance.
- 2026-01-14 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- Latest action: 2025-06-17: Introduced in Senate

## Actions

- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Read twice and referred to the Committee on Finance.
- 2026-01-14 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2100",
    "number": "2100",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Modernizing Agricultural and Manufacturing Bonds Act",
    "type": "S",
    "updateDate": "2026-01-15T12:03:40Z",
    "updateDateIncludingText": "2026-01-15T12:03:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-17",
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
      "actionDate": "2025-06-17",
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
          "date": "2026-01-14T19:30:02Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-17T20:30:28Z",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "VA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2100is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2100\nIN THE SENATE OF THE UNITED STATES\nJune 17, 2025 Ms. Ernst (for herself, Mr. Warner , and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify certain rules applicable to qualified small issue manufacturing bonds, to expand certain exceptions to the private activity bond rules for first-time farmers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modernizing Agricultural and Manufacturing Bonds Act .\n#### 2. Modifications to qualified small issue bonds\n##### (a) Manufacturing Facilities To Include Production of Intangible Property and Functionally Related Facilities\nSubparagraph (C) of section 144(a)(12) of the Internal Revenue Code of 1986 is amended to read as follows:\n(C) Manufacturing facility For purposes of this paragraph\u2014 (i) In general The term manufacturing facility means any facility which\u2014 (I) is used in the manufacturing or production of tangible personal property (including the processing resulting in a change in the condition of such property), (II) is used in the creation or production of intangible property which is described in section 197(d)(1)(C)(iii), or (III) is functionally related and subordinate to a facility described in subclause (I) or (II) if such facility is located on the same site as the facility described in subclause (I) or (II). (ii) Certain facilities included The term manufacturing facility includes facilities that are directly related and ancillary to a manufacturing facility (determined without regard to this clause) if\u2014 (I) those facilities are located on the same site as the manufacturing facility, and (II) not more than 25 percent of the net proceeds of the issue are used to provide those facilities. (iii) Limitation on office space A rule similar to the rule of section 142(b)(2) shall apply for purposes of clause (i). (iv) Limitation on refundings for certain property Subclauses (II) and (III) of clause (i) shall not apply to any bond issued on or before the date of the enactment of the Modernizing Agricultural and Manufacturing Bonds Act , or to any bond issued to refund a bond issued on or before such date (other than a bond to which clause (iii) of this subparagraph (as in effect before the date of the enactment of the Modernizing Agricultural and Manufacturing Bonds Act applies)), either directly or in a series of refundings. .\n##### (b) Increase in limitations\n**(1) In general**\nSection 144(a)(4) of such Code is amended\u2014\n**(A)**\nin subparagraph (A)(i), by striking $10,000,000 and inserting $30,000,000 , and\n**(B)**\nin the heading, by striking $10,000,000 and inserting $30,000,000 .\n**(2) Increase in additional capital expenditures not taken into account**\nSection 144(a)(4)(G) of such Code is amended by inserting $30,000,000, in the case of bonds issued after the date of the enactment of the Modernizing Agricultural and Manufacturing Bonds Act .\n**(3) Increase in aggregate limit per taxpayer**\nSection 144(a)(10)(A) of such Code is amended by striking $40,000,000 and inserting $120,000,000 .\n**(4) Adjustment for inflation**\nSection 144(a) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(13) Adjustment for inflation In the case of any calendar year after 2025, the $30,000,000 amounts in paragraph (4)(A), the $30,000,000 amount in paragraph (4)(G), and the $120,000,000 amount in paragraph (10)(A) shall each be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. If any amount as increased under the preceding sentence is not a multiple of $100,000, such amount shall be rounded to the nearest multiple of $100,000. .\n##### (c) Effective date\nThe amendments made by this section shall apply to obligations issued after the date of the enactment of this Act.\n#### 3. Expansion of certain exceptions to the private activity bond rules for first-time farmers\n##### (a) Increase in dollar limitation\n**(1) In general**\nSection 147(c)(2)(A) of the Internal Revenue Code of 1986 is amended by striking $450,000 and inserting $1,000,000 .\n**(2) Repeal of separate lower dollar limitation on used farm equipment**\nSection 147(c)(2) of such Code is amended by striking subparagraph (F) and by redesignating subparagraphs (G) and (H) as subparagraphs (F) and (G), respectively.\n**(3) Qualified small issue bond limitation conformed to increased dollar limitation**\nSection 144(a)(11)(A) of such Code is amended by striking $250,000 and inserting $1,000,000 .\n**(4) Inflation adjustment**\n**(A) In general**\nSection 147(c)(2)(G) of such Code, as redesignated by paragraph (2), is amended\u2014\n**(i)**\nby striking after 2008, the dollar amount in subparagraph (A) shall be increased and inserting after 2026, the dollar amounts in subparagraph (A) and section 144(a)(11)(A) shall each be increased ,\n**(ii)**\nin clause (ii), by striking 2007 and inserting 2025 , and\n**(iii)**\nin the last sentence, by striking $100 each place it appears and inserting $10,000 .\n**(B) Cross-reference**\nSection 144(a)(11) of such Code is amended by adding at the end the following new subparagraph:\n(D) Inflation adjustment For inflation adjustment of dollar amount contained in subparagraph (A), see section 147(c)(2)(G). .\n##### (b) Substantial farmland determined on basis of average rather than median farm size\nSection 147(c)(2)(E) of such Code is amended by striking median and inserting average .\n##### (c) Effective date\nThe amendments made by this section shall apply to bonds issued after December 31, 2025.",
      "versionDate": "2025-06-17",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-06-30T18:08:41Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2100is.xml"
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
      "title": "Modernizing Agricultural and Manufacturing Bonds Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-15T12:03:40Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Modernizing Agricultural and Manufacturing Bonds Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-28T02:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to modify certain rules applicable to qualified small issue manufacturing bonds, to expand certain exceptions to the private activity bond rules for first-time farmers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-28T02:33:29Z"
    }
  ]
}
```
