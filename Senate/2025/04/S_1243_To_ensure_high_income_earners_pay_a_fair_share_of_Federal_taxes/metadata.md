# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1243?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1243
- Title: Paying a Fair Share Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1243
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2026-02-04T19:53:57Z
- Update date including text: 2026-02-04T19:53:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1243",
    "number": "1243",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Paying a Fair Share Act of 2025",
    "type": "S",
    "updateDate": "2026-02-04T19:53:57Z",
    "updateDateIncludingText": "2026-02-04T19:53:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T21:55:16Z",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MD"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "IL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MN"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "RI"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "HI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-04-01",
      "state": "VT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "WI"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NJ"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "VT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1243is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1243\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Whitehouse (for himself, Mr. Merkley , Mr. Blumenthal , Mr. Van Hollen , Mr. Durbin , Ms. Klobuchar , Mr. Reed , Ms. Hirono , Mr. Sanders , Ms. Baldwin , Ms. Warren , Mr. Booker , Mr. Welch , Ms. Smith , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo ensure high-income earners pay a fair share of Federal taxes.\n#### 1. Short title\nThis Act may be cited as the Paying a Fair Share Act of 2025 .\n#### 2. Fair share tax on high-income taxpayers\n##### (a) In general\nSubchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new part:\nVIII Fair Share Tax on High-Income Taxpayers Sec. 59B. Fair share tax. 59B. Fair share tax (a) General rule (1) Phase-in of tax In the case of any high-income taxpayer, there is hereby imposed for a taxable year (in addition to any other tax imposed by this subtitle) a tax equal to the product of\u2014 (A) the amount determined under paragraph (2), and (B) a fraction (not to exceed 1)\u2014 (i) the numerator of which is the excess of\u2014 (I) the taxpayer's adjusted gross income, over (II) the dollar amount in effect under subsection (c)(1), and (ii) the denominator of which is the dollar amount in effect under subsection (c)(1). (2) Amount of tax The amount of tax determined under this paragraph is an amount equal to the excess (if any) of\u2014 (A) the tentative fair share tax for the taxable year, over (B) the excess of\u2014 (i) the sum of\u2014 (I) the regular tax liability (as defined in section 26(b)) for the taxable year, determined without regard to any tax liability determined under this section, (II) the tax imposed by section 55 for the taxable year, plus (III) the payroll tax for the taxable year, over (ii) the credits allowable under part IV of subchapter A (other than sections 27(a), 31, and 34). (b) Tentative fair share tax For purposes of this section\u2014 (1) In general The tentative fair share tax for the taxable year is 30 percent of the excess of\u2014 (A) the adjusted gross income of the taxpayer, over (B) the modified charitable contribution deduction for the taxable year. (2) Modified charitable contribution deduction For purposes of paragraph (1)\u2014 (A) In general The modified charitable contribution deduction for any taxable year is an amount equal to the amount which bears the same ratio to the deduction allowable under section 170 (section 642(c) in the case of a trust or estate) for such taxable year as\u2014 (i) the amount of itemized deductions allowable under the regular tax (as defined in section 55) for such taxable year, determined after the application of section 68, bears to (ii) such amount, determined before the application of section 68. (B) Taxpayer must itemize In the case of any individual who does not elect to itemize deductions for the taxable year, the modified charitable contribution deduction shall be zero. (c) High-Income taxpayer For purposes of this section\u2014 (1) In general The term high-income taxpayer means, with respect to any taxable year, any taxpayer (other than a corporation) with an adjusted gross income for such taxable year in excess of $1,000,000 (50 percent of such amount in the case of a married individual who files a separate return). (2) Inflation adjustment (A) In general In the case of a taxable year beginning after 2025, the $1,000,000 amount under paragraph (1) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (B) Rounding If any amount as adjusted under subparagraph (A) is not a multiple of $10,000, such amount shall be rounded to the next lowest multiple of $10,000. (d) Payroll tax For purposes of this section, the payroll tax for any taxable year is an amount equal to the excess of\u2014 (1) the taxes imposed on the taxpayer under sections 1401, 1411, 3101, 3201, and 3211(a) (to the extent such tax is attributable to the rate of tax in effect under section 3101) with respect to such taxable year or wages or compensation received during such taxable year, over (2) the deduction allowable under section 164(f) for such taxable year. (e) Special rule for estates and trusts For purposes of this section, in the case of an estate or trust, adjusted gross income shall be computed in the manner described in section 67(e). (f) Not treated as tax imposed by this chapter for certain purposes The tax imposed under this section shall not be treated as tax imposed by this chapter for purposes of determining the amount of any credit under this chapter (other than the credit allowed under section 27(a)) or for purposes of section 55. .\n##### (b) Clerical amendment\nThe table of parts for subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nPart VIII\u2014Fair Share Tax on High-Income Taxpayers .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n#### 3. Sense of the Senate regarding tax reform\nIt is the sense of the Senate that\u2014\n**(1)**\nCongress should enact tax reform that repeals unfair and unnecessary tax loopholes and expenditures, simplifies the system for millions of taxpayers and businesses, and makes sure that the wealthiest taxpayers pay a fair share; and\n**(2)**\nthis Act is an interim step that can be done quickly and serve as a floor on taxes for the highest-income taxpayers, cut the deficit by billions of dollars a year, and help encourage more fundamental reform of the tax system.",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-04-01",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2534",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Paying a Fair Share Act of 2025",
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
        "updateDate": "2025-05-09T13:40:39Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1243is.xml"
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
      "title": "Paying a Fair Share Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Paying a Fair Share Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure high-income earners pay a fair share of Federal taxes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:35Z"
    }
  ]
}
```
