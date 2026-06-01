# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4083?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4083
- Title: Working Americans’ Tax Cut Act
- Congress: 119
- Bill type: S
- Bill number: 4083
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-05-01T11:03:33Z
- Update date including text: 2026-05-01T11:03:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4083",
    "number": "4083",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Working Americans\u2019 Tax Cut Act",
    "type": "S",
    "updateDate": "2026-05-01T11:03:33Z",
    "updateDateIncludingText": "2026-05-01T11:03:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T17:13:00Z",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "AZ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NY"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NJ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NJ"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "IL"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-03-12",
      "state": "VT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "OR"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "DE"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "HI"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "WI"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "HI"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NM"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-12",
      "state": "ME"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "DE"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "AZ"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4083is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4083\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Mr. Van Hollen (for himself, Mr. Kelly , Mrs. Gillibrand , Mr. Booker , Mr. Kim , Mr. Durbin , Mr. Sanders , Mr. Merkley , Mr. Coons , Mr. Blumenthal , Mr. Schatz , Ms. Baldwin , Ms. Hirono , Mr. Heinrich , Mr. King , Mr. Markey , Mr. Welch , Mr. Schiff , and Ms. Blunt Rochester ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to make certain modifications in relation to the taxation of income required to fund basic living expenses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Working Americans\u2019 Tax Cut Act .\n#### 2. Alternative maximum tax for low-income individuals\n##### (a) In general\nPart I of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 1 the following new section:\n1A. Alternative maximum tax for low- and middle-income individuals (a) In general In the case of a qualified individual, the tax imposed under section 1 for any taxable year shall not exceed 25.5 percent of the excess of\u2014 (1) the taxpayer\u2019s modified adjusted gross income for such taxable year, over (2) the cost-of-living exemption for such taxable year. (b) Qualified individual (1) In general For purposes of this section, the term qualified individual means, with respect to any taxable year, any individual if the taxpayer's modified adjusted gross income for such taxable year is less than 175 percent of the cost-of-living exemption for such taxable year. (2) Exception The term qualified individual shall not include any person described in section 63(c)(6). (c) Cost-of-Living exemption For purposes of this section\u2014 (1) In general The term cost-of-living exemption means, with respect to any taxable year\u2014 (A) in the case of a taxpayer not described in subparagraph (B) or (C), 100 percent of the annualized cost-of-living wage, (B) in the case of a joint return, 200 percent of the annualized cost-of-living wage, and (C) in the case of a head of household, 140 percent of the annualized cost-of-living wage. (2) Annualized cost of living wage (A) In general The term annualized cost-of-living wage means, with respect to any taxable year, an amount equal to $46,000, multiplied by the ratio of\u2014 (i) the CPI\u2013U for the calendar year preceding the calendar year in which such taxable year begins, to (ii) the CPI\u2013U for the calendar year preceding the calendar year of the date of enactment of the Working Americans\u2019 Tax Cut Act . (B) CPI\u2013U For purposes of this paragraph, the term CPI\u2013U means, when used with respect to a calendar year, the Consumer Price Index for all urban consumers, as published by the Bureau of Labor Statistics, for September of such year. (d) Modified adjusted gross income For purposes of this section, the term modified adjusted gross income means adjusted gross income increased by\u2014 (1) any amount excluded from gross income under section 911, 931, or 933, and (2) an amount equal to the portion of the taxpayer's social security benefits (as defined in section 86(d)) which is not included in gross income under section 86 for the taxable year. .\n##### (b) Clerical amendment\nThe table of sections for part I of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 1 the following new item:\nSec. 1A. Alternative maximum tax for low- and middle-income individuals. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Surcharge on high income individuals\n##### (a) In general\nSubchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new part:\nVIII Surcharge on high income individuals Sec. 59B. Surcharge on high income individuals. 59B. Surcharge on high income individuals (a) General rule In the case of a taxpayer other than a corporation, there is hereby imposed (in addition to any other tax imposed by this subtitle) a tax equal to the sum of\u2014 (1) 5 percent of so much of the modified adjusted gross income of the taxpayer as exceeds $1,000,000, but does not exceed $2,000,000, (2) 10 percent of so much of the modified adjusted gross income of the taxpayer as exceeds $2,000,000, but does not exceed $5,000,000, plus (3) 12 percent of so much of the modified adjusted gross income of the taxpayer as exceeds $5,000,000. (b) Inflation adjustment (1) In general In the case of any taxable year beginning after 2026, subsection (a) shall be applied by substituting each dollar amount in such subsection with an amount equal to the product of\u2014 (A) such dollar amount (as determined without regard to this subsection), multiplied by (B) an amount equal to the ratio of\u2014 (i) the CPI\u2013U for the calendar year preceding the calendar year in which such taxable year begins, to (ii) the CPI\u2013U for the calendar year preceding the calendar year of the date of enactment of the Working Americans\u2019 Tax Cut Act . (2) CPI\u2013U For purposes of this subsection, the term CPI\u2013U means, when used with respect to a calendar year, the Consumer Price Index for all urban consumers, as published by the Bureau of Labor Statistics, for September of such year. (c) Taxpayers making a joint return In the case of any taxpayer filing a joint return under section 6013, subsection (a) shall be applied (after the application of subsection (b)) by increasing each of the dollar amounts by an amount equal to 50 percent of such dollar amount. (d) Modified adjusted gross income For purposes of this section, the term modified adjusted gross income means adjusted gross income reduced by any deduction (not taken into account in determining adjusted gross income) allowed for investment interest (as defined in section 163(d)). In the case of an estate or trust, adjusted gross income shall be determined as provided in section 67(e). (e) Special rules (1) Citizens and residents living abroad The dollar amount in effect under subsection (a) (after the application of subsections (b) and (c)) shall be decreased by the excess of\u2014 (A) the amounts excluded from the taxpayer\u2019s gross income under section 911, over (B) the amounts of any deductions or exclusions disallowed under section 911(d)(6) with respect to the amounts described in subparagraph (A). (2) Charitable trusts Subsection (a) shall not apply to a trust all the unexpired interests in which are devoted to one or more of the purposes described in section 170(c)(2)(B). (3) Not treated as tax imposed by this chapter for certain purposes The tax imposed under this section shall not be treated as tax imposed by this chapter for purposes of determining the amount of any credit under this chapter or for purposes of section 55. .\n##### (b) Clerical amendment\nThe table of parts for subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nPart VIII\u2014Surcharge on high income individuals .\n##### (c) Section 15 not To apply\nThe amendment made by subsection (a) shall not be treated as a change in a rate of tax for purposes of section 15 of the Internal Revenue Code of 1986.\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-03-12",
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
        "actionDate": "2026-03-16",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7937",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Working Americans\u2019 Tax Cut Act",
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
        "updateDate": "2026-03-31T21:34:49Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4083is.xml"
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
      "title": "Working Americans\u2019 Tax Cut Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T11:03:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to make certain modifications in relation to the taxation of income required to fund basic living expenses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Working Americans\u2019 Tax Cut Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:18Z"
    }
  ]
}
```
