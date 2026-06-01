# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/46?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/46
- Title: Health Care Affordability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 46
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2026-05-14T21:23:29Z
- Update date including text: 2026-05-14T21:23:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/46",
    "number": "46",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Health Care Affordability Act of 2025",
    "type": "S",
    "updateDate": "2026-05-14T21:23:29Z",
    "updateDateIncludingText": "2026-05-14T21:23:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T19:58:29Z",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "WI"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-01-09",
      "state": "ME"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NH"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "VT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "VA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "DE"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "WA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "GA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "RI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MD"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NV"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "HI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MN"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NV"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "AZ"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NJ"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "RI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "OR"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "VA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NM"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "HI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CO"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CO"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MI"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NM"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NJ"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MI"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "DE"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "AZ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MD"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s46is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 46\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mrs. Shaheen (for herself, Ms. Baldwin , Mr. Schumer , Mr. Wyden , Mr. Blumenthal , Mr. King , Ms. Hassan , Mr. Welch , Mr. Kaine , Mr. Coons , Ms. Warren , Mr. Durbin , Mrs. Murray , Mr. Warnock , Mrs. Gillibrand , Mr. Reed , Ms. Duckworth , Mr. Van Hollen , Ms. Cortez Masto , Mr. Schatz , Mr. Padilla , Ms. Smith , Ms. Klobuchar , Ms. Rosen , Mr. Kelly , Mr. Booker , Mr. Whitehouse , Mr. Merkley , Mr. Schiff , Mr. Warner , Mr. Markey , Mr. Luj\u00e1n , Ms. Hirono , Mr. Bennet , Mr. Hickenlooper , Mr. Peters , Mr. Fetterman , Mr. Heinrich , Mr. Kim , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand eligibility for the refundable credit for coverage under a qualified health plan.\n#### 1. Short title\nThis Act may be cited as the Health Care Affordability Act of 2025 .\n#### 2. Increase in eligibility for credit\n##### (a) In general\nSubparagraph (A) of section 36B(c)(1) of the Internal Revenue Code of 1986 is amended by striking but does not exceed 400 percent .\n##### (b) Applicable percentages\n**(1) In general**\nSubparagraph (A) of section 36B(b)(3) of the Internal Revenue Code of 1986 is amended to read as follows:\n(A) Applicable percentage The applicable percentage for any taxable year shall be the percentage such that the applicable percentage for any taxpayer whose household income is within an income tier specified in the following table shall increase, on a sliding scale in a linear manner, from the initial premium percentage to the final premium percentage specified in such table for such income tier: In the case of household income (expressed as a percent of poverty line) within the following income tier: The initial premium percentage is\u2014 The final premium percentage is\u2014 Up to 150 percent 0 0 150 percent up to 200 percent 0 2.0 200 percent up to 250 percent 2.0 4.0 250 percent up to 300 percent 4.0 6.0 300 percent up to 400 percent 6.0 8.5 400 percent and higher 8.5 8.5. .\n**(2) Conforming amendments relating to affordability of coverage**\n**(A)**\nParagraph (1) of section 36B(c) of such Code is amended by striking subparagraph (E).\n**(B)**\nSubparagraph (C) of section 36B(c)(2) of such Code is amended by striking clause (iv).\n**(C)**\nParagraph (4) of section 36B(c) of such Code is amended by striking subparagraph (F).\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-01-09",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6900",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Affordability Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-03",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Energy and Commerce, Financial Services, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7767",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Make Billionaires Pay Their Fair Share Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-02",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3956",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Make Billionaires Pay Their Fair Share Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-01",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4849",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Health Care and Lowering Costs Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-30",
        "text": "Read twice and referred to the Committee on Finance. (text: CR S4908)"
      },
      "number": "2556",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Health Care and Lowering Costs Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-09",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "247",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Health Care Affordability Act of 2025",
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
            "updateDate": "2025-03-04T18:44:36Z"
          },
          {
            "name": "Income tax credits",
            "updateDate": "2025-03-04T18:44:36Z"
          },
          {
            "name": "Tax administration and collection, taxpayers",
            "updateDate": "2025-03-04T18:44:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-14T18:56:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
    "originChamber": "Senate",
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
          "measure-id": "id119s46",
          "measure-number": "46",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-09-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s46v00",
            "update-date": "2025-09-19"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Health Care Affordability Act of 2025</strong></p><p>This bill makes permanent temporary changes enacted by the American Rescue Plan Act of 2021 (ARPA) and the Inflation Reduction Act of 2022 (IRA) that generally expand eligibility for and increase the amount of the premium tax credit.</p><p>Currently, eligible taxpayers may be able to claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To be eligible for the premium tax credit, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL) and, after 2025, may not exceed 400% of the FPL (maximum income limit). For 2021-2025, the ARPA and IRA eliminated the maximum income limit, which generally expands eligibility for the premium tax credit.</p><p>Further, under current law, the amount of the premium tax credit is (1) generally the plan premium (conditions apply), minus (2) the taxpayer\u2019s household income multiplied by the applicable percentage. The applicable percentage is a specific percentage that varies depending on which of six income ranges (adjusted for inflation after 2025) the taxpayer\u2019s household income falls within. For 2021-2025, the ARPA and IRA lowered the applicable percentages and eliminated the adjustment of the applicable percentages for inflation, which generally increases the amount of the premium tax credit.</p><p>The bill makes permanent the elimination of the 400% maximum income limit, the lower applicable percentages, and the elimination of the inflation adjustment for the applicable percentages.</p>"
        },
        "title": "Health Care Affordability Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s46.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Health Care Affordability Act of 2025</strong></p><p>This bill makes permanent temporary changes enacted by the American Rescue Plan Act of 2021 (ARPA) and the Inflation Reduction Act of 2022 (IRA) that generally expand eligibility for and increase the amount of the premium tax credit.</p><p>Currently, eligible taxpayers may be able to claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To be eligible for the premium tax credit, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL) and, after 2025, may not exceed 400% of the FPL (maximum income limit). For 2021-2025, the ARPA and IRA eliminated the maximum income limit, which generally expands eligibility for the premium tax credit.</p><p>Further, under current law, the amount of the premium tax credit is (1) generally the plan premium (conditions apply), minus (2) the taxpayer\u2019s household income multiplied by the applicable percentage. The applicable percentage is a specific percentage that varies depending on which of six income ranges (adjusted for inflation after 2025) the taxpayer\u2019s household income falls within. For 2021-2025, the ARPA and IRA lowered the applicable percentages and eliminated the adjustment of the applicable percentages for inflation, which generally increases the amount of the premium tax credit.</p><p>The bill makes permanent the elimination of the 400% maximum income limit, the lower applicable percentages, and the elimination of the inflation adjustment for the applicable percentages.</p>",
      "updateDate": "2025-09-19",
      "versionCode": "id119s46"
    },
    "title": "Health Care Affordability Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Health Care Affordability Act of 2025</strong></p><p>This bill makes permanent temporary changes enacted by the American Rescue Plan Act of 2021 (ARPA) and the Inflation Reduction Act of 2022 (IRA) that generally expand eligibility for and increase the amount of the premium tax credit.</p><p>Currently, eligible taxpayers may be able to claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To be eligible for the premium tax credit, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL) and, after 2025, may not exceed 400% of the FPL (maximum income limit). For 2021-2025, the ARPA and IRA eliminated the maximum income limit, which generally expands eligibility for the premium tax credit.</p><p>Further, under current law, the amount of the premium tax credit is (1) generally the plan premium (conditions apply), minus (2) the taxpayer\u2019s household income multiplied by the applicable percentage. The applicable percentage is a specific percentage that varies depending on which of six income ranges (adjusted for inflation after 2025) the taxpayer\u2019s household income falls within. For 2021-2025, the ARPA and IRA lowered the applicable percentages and eliminated the adjustment of the applicable percentages for inflation, which generally increases the amount of the premium tax credit.</p><p>The bill makes permanent the elimination of the 400% maximum income limit, the lower applicable percentages, and the elimination of the inflation adjustment for the applicable percentages.</p>",
      "updateDate": "2025-09-19",
      "versionCode": "id119s46"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s46is.xml"
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
      "title": "Health Care Affordability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Health Care Affordability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to expand eligibility for the refundable credit for coverage under a qualified health plan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:32Z"
    }
  ]
}
```
