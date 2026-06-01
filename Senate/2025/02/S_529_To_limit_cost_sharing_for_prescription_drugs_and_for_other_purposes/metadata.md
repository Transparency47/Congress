# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/529?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/529
- Title: Capping Prescription Costs Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 529
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2026-02-04T05:06:14Z
- Update date including text: 2026-02-04T05:06:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/529",
    "number": "529",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Capping Prescription Costs Act of 2025",
    "type": "S",
    "updateDate": "2026-02-04T05:06:14Z",
    "updateDateIncludingText": "2026-02-04T05:06:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T21:40:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "WI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NJ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "CT"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NM"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "MN"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "WA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "VT"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MD"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NM"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s529is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 529\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Warnock (for himself, Ms. Baldwin , Mr. Booker , Mr. Blumenthal , Mr. Fetterman , Mrs. Gillibrand , Mr. Heinrich , Mr. Kim , Ms. Klobuchar , Mrs. Murray , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo limit cost-sharing for prescription drugs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Capping Prescription Costs Act of 2025 .\n#### 2. Cap on prescription drug cost-sharing\n##### (a) Qualified health plans\nSection 1302(c) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18022(c) ) is amended\u2014\n**(1)**\nin paragraph (3)(A)(i), by inserting , including cost-sharing with respect to prescription drugs covered by the plan after charges ; and\n**(2)**\nby adding at the end the following:\n(5) Prescription drug cost-sharing (A) 2026 For plan years beginning in 2026, the cost-sharing incurred under a health plan with respect to prescription drugs covered by the plan shall not exceed $2,000 per year for each enrolled individual, or $4,000 per year for each family. (B) 2027 and later (i) In general In the case of any plan year beginning in a calendar year after 2026, the limitation under this paragraph shall be equal to the applicable dollar amount under subparagraph (A) for plan years beginning in 2026, increased by an amount equal to the product of that amount and the medical care component of the consumer price index for all urban consumers (as published by the Bureau of Labor Statistics) for that year. (ii) Adjustment to amount If the amount of any increase under clause (i) is not a multiple of $5, such increase shall be rounded to the next lowest multiple of $5. .\n##### (b) Group health plans\n**(1) Public Health Service Act**\nPart D of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111 et seq. ) is amended by inserting after section 2799A\u20135 ( 42 U.S.C. 300gg\u2013115 ) the following:\n2799A\u20136. Cap on prescription drug cost-sharing for group health plans A group health plan and health insurance issuer offering group health insurance coverage shall ensure that any cost-sharing imposed under the plan or coverage with respect to prescription drugs covered by the plan or coverage does not exceed the limitations provided for under paragraph (5) of section 1302(c) of the Patient Protection and Affordable Care Act. .\n**(2) Employee Retirement Income Security Act**\n**(A) In general**\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act ( 29 U.S.C. 1185 et seq. ) is amended by inserting after section 720 ( 29 U.S.C. 1185i ) the following:\n721. Cap on prescription drug cost-sharing A group health plan and health insurance issuer offering group health insurance coverage shall ensure that any cost-sharing imposed under the plan or coverage with respect to prescription drugs covered by the plan or coverage does not exceed the limitations provided for under paragraph (5) of section 1302(c) of the Patient Protection and Affordable Care Act. .\n**(B) Clerical amendment**\nThe table of contents in section 1 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 note) is amended by inserting after the item relating to section 720 the following:\nSec. 721. Cap on prescription drug cost-sharing .\n**(3) Internal Revenue Code of 1986**\n**(A) In general**\nSubchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by inserting after section 9820 the following:\n9821. Cap on prescription drug cost-sharing A group health plan shall ensure that any cost-sharing imposed under the plan with respect to prescription drugs covered by the plan does not exceed the limitations provided for under paragraph (5) of section 1302(c) of the Patient Protection and Affordable Care Act. .\n**(B) Clerical amendment**\nThe table of sections for subchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 9820 the following:\nSec. 9821. Cap on prescription drug cost-sharing .\n##### (c) Effective date\nThe amendments made by subsections (a) and (b) shall take effect with respect to plan years beginning on or after January 1, 2026.",
      "versionDate": "2025-02-11",
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
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Education and Workforce, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2553",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Capping Prescription Costs Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-05-02T14:57:01Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-05-02T14:56:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T16:20:00Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s529is.xml"
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
      "title": "Capping Prescription Costs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to limit cost-sharing for prescription drugs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Capping Prescription Costs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:25Z"
    }
  ]
}
```
