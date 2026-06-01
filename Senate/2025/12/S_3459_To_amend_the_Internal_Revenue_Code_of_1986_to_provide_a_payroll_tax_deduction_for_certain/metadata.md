# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3459?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3459
- Title: Support Small Business Growth Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3459
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-01-06T16:14:03Z
- Update date including text: 2026-01-06T16:14:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3459",
    "number": "3459",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "O000174",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Ossoff, Jon [D-GA]",
        "lastName": "Ossoff",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Support Small Business Growth Act of 2025",
    "type": "S",
    "updateDate": "2026-01-06T16:14:03Z",
    "updateDateIncludingText": "2026-01-06T16:14:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T20:16:28Z",
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3459is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3459\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Ossoff (for himself and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a payroll tax deduction for certain small businesses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Support Small Business Growth Act of 2025 .\n#### 2. Payroll tax deduction for small businesses\n##### (a) In general\nPart VI of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 176 the following new section:\n177. Payroll deduction for qualified small businesses (a) In general In the case of a qualified small business, in addition to the deduction allowed by section 162(a)(1), there shall be allowed as a deduction an amount equal to the sum of the applicable amounts determined under subsection (b)(2) with respect to each full-time employee of the employer which has been designated by such employer pursuant to subsection (b)(1). (b) Limitations; applicable amount (1) Designation of employees (A) In general For purposes of subsection (a), with respect to any taxable year, the full-time employees designated by the employer (at such time and in such manner as the Secretary may provide) shall\u2014 (i) not exceed the applicable maximum number of employees, (ii) only include those full-time employees with the lowest wages paid during such taxable year relative to all other full-time employees of such employer, and (iii) not include any highly compensated employee. (B) Applicable maximum number For purposes of subparagraph (A), the applicable maximum number with respect to any qualified small business is\u2014 (i) 10, in the case of a taxable year beginning in 2026, 2027, 2028, 2029, or 2030, (ii) 8, in the case of a taxable year beginning in 2031, (iii) 6, in the case of a taxable year beginning in 2032, (iv) 4, in the case of a taxable year beginning in 2033, and (v) zero thereafter. (2) Applicable amount (A) In general For purposes of subsection (a), with respect to each full-time employee designated pursuant to paragraph (1), the applicable amount shall be an amount equal to the lesser of\u2014 (i) the applicable wage limitation, or (ii) 12 percent of the wages paid to such employee during the taxable year. (B) Applicable wage limitation For purposes of subparagraph (A), the applicable wage limitation is\u2014 (i) $8,000, with respect to the number of full-time employees designated pursuant to paragraph (1) which is equal to\u2014 (I) the applicable maximum number with respect to the qualified small business for the taxable year, reduced by (II) 2, (ii) $6,000, with respect to 1 additional such employee, if applicable, and (iii) $4,000, with respect to 1 additional such employee, if applicable. (c) Qualified small business For purposes of this section, the term qualified small business means, with respect to a taxable year, a small business concern (as defined under section 3 of the Small Business Act) which\u2014 (1) as of the last date of such taxable year\u2014 (A) has not more than 15 full-time employees, and (B) meets the gross receipts test of section 448(c), and (2) certifies to the Secretary, at such time and in such manner as the Secretary shall prescribe, that such concern meets the requirements of this subsection for the taxable year. (d) Definitions For purposes of this section\u2014 (1) Full-time employee The term full-time employee has the meaning given such term by section 4980H(c)(4). (2) Highly compensated employee The term highly compensated employee has the meaning given such term by section 414(q). (e) Termination This section shall not apply to taxable years beginning after December 31, 2033. .\n##### (b) Clerical amendment\nThe table of sections for part VI of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 176 the following new item:\nSec. 177. Payroll deduction for qualified small businesses. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-12-11",
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
        "updateDate": "2026-01-06T16:14:03Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3459is.xml"
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
      "title": "Support Small Business Growth Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:39:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Support Small Business Growth Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:39:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide a payroll tax deduction for certain small businesses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:33:31Z"
    }
  ]
}
```
