# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2556?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2556
- Title: Protecting Health Care and Lowering Costs Act
- Congress: 119
- Bill type: S
- Bill number: 2556
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2026-05-14T21:23:57Z
- Update date including text: 2026-05-14T21:23:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S4908)
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S4908)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2556",
    "number": "2556",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S000148",
        "district": "",
        "firstName": "Charles",
        "fullName": "Sen. Schumer, Charles E. [D-NY]",
        "lastName": "Schumer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Protecting Health Care and Lowering Costs Act",
    "type": "S",
    "updateDate": "2026-05-14T21:23:57Z",
    "updateDateIncludingText": "2026-05-14T21:23:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S4908)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
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
          "date": "2025-07-30T22:33:00Z",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "OR"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "OR"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NH"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "HI"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "VT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "IL"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CO"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-30",
      "state": "ME"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NM"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-30",
      "state": "VT"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "RI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MD"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "WA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "HI"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "RI"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "VA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NY"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "VA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "WI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "DE"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
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
      "sponsorshipDate": "2025-07-30",
      "state": "IL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "AZ"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NV"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "GA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MN"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "AZ"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NJ"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CO"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NJ"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NV"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "WA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MN"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "DE"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NM"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "PA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "GA"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NH"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2556is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2556\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Schumer (for himself, Mr. Wyden , Mr. Merkley , Mrs. Shaheen , Ms. Hirono , Mr. Welch , Ms. Duckworth , Mr. Hickenlooper , Mr. King , Mr. Luj\u00e1n , Mr. Sanders , Mr. Reed , Mr. Van Hollen , Mr. Peters , Mr. Blumenthal , Mrs. Murray , Mr. Schatz , Mr. Whitehouse , Ms. Warren , Mr. Warner , Mrs. Gillibrand , Mr. Kaine , Mr. Schiff , Ms. Baldwin , Mr. Markey , Mr. Coons , Ms. Alsobrooks , Mr. Durbin , Mr. Padilla , Mr. Gallego , Ms. Rosen , Mr. Warnock , Ms. Smith , Mr. Kelly , Mr. Booker , Ms. Slotkin , Mr. Bennet , Mr. Kim , Ms. Cortez Masto , Ms. Cantwell , Ms. Klobuchar , Ms. Blunt Rochester , Mr. Heinrich , Mr. Fetterman , Mr. Ossoff , Ms. Hassan , and Mr. Murphy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo repeal the changes made by the health subtitle of the One Big Beautiful Bill Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Health Care and Lowering Costs Act .\n#### 2. Repeal of health subtitle changes\nSubtitle B of title VII of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ) is repealed and any law or regulation referred to in such subtitle shall be applied as if such subtitle and the amendments made by such subtitle had not been enacted.\n#### 3. Permanent extension of enhanced tax credit\n##### (a) In general\nSubparagraph (A) of section 36B(c)(1) of the Internal Revenue Code of 1986 is amended by striking but does not exceed 400 percent .\n##### (b) Applicable percentages\n**(1) In general**\nSubparagraph (A) of section 36B(b)(3) of the Internal Revenue Code of 1986 is amended to read as follows:\n(A) Applicable percentage The applicable percentage for any taxable year shall be the percentage such that the applicable percentage for any taxpayer whose household income is within an income tier specified in the following table shall increase, on a sliding scale in a linear manner, from the initial premium percentage to the final premium percentage specified in such table for such income tier: In the case of household income (expressed as a percent of poverty line) within the following income tier: The initial premium percentage is\u2014 The final premium percentage is\u2014 Up to 150 percent 0 0 150 percent up to 200 percent 0 2.0 200 percent up to 250 percent 2.0 4.0 250 percent up to 300 percent 4.0 6.0 300 percent up to 400 percent 6.0 8.5 400 percent and higher 8.5 8.5. .\n**(2) Conforming amendments relating to affordability of coverage**\n**(A)**\nParagraph (1) of section 36B(c) of such Code is amended by striking subparagraph (E).\n**(B)**\nSubparagraph (C) of section 36B(c)(2) of such Code is amended by striking clause (iv).\n**(C)**\nParagraph (4) of section 36B(c) of such Code is amended by striking subparagraph (F).\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-07-30",
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
        "actionDate": "2025-01-09",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "247",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Health Care Affordability Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "46",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Health Care Affordability Act of 2025",
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
        "updateDate": "2025-09-08T16:18:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-30",
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
          "measure-id": "id119s2556",
          "measure-number": "2556",
          "measure-type": "s",
          "orig-publish-date": "2025-07-30",
          "originChamber": "SENATE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2556v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-07-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Health Care and Lowering Costs Act</strong></p><p>This bill makes permanent temporary provisions that generally expand eligibility for and increase the amount of the premium tax credit.\u00a0This bill also repeals multiple Medicaid, Medicare, and health-related tax provisions enacted by the One Big Beautiful Bill Act (OBBBA).</p><p>Currently, eligible taxpayers may claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To qualify, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL) and, after 2025, may not exceed 400% of the FPL (maximum income limit). For 2021-2025, the maximum income limit is eliminated, which generally expands eligibility for the premium tax credit.</p><p>Further, under current law, the amount of the premium tax credit is partially based on the taxpayer\u2019s household income multiplied by the applicable percentage. The applicable percentage varies depending on which of six income ranges (adjusted for inflation after 2025) the taxpayer\u2019s household income falls within. For 2021-2025, the applicable percentages are lowered and the adjustment of the applicable percentages for inflation is eliminated, which generally increases the amount of the premium tax credit.</p><p>The bill permanently eliminates the 400% maximum income limit, lowers the applicable percentages, and eliminates the inflation adjustment for the applicable percentages.</p><p>Finally, the bill repeals multiple Medicaid, Medicare, and health-related tax provisions enacted by the OBBBA, including</p><ul><li>certain Medicare and Medicare eligibility and verification requirements,</li><li>the reduced window for retroactive Medicaid coverage, and</li><li>premium tax credit verification requirements.</li></ul>"
        },
        "title": "Protecting Health Care and Lowering Costs Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2556.xml",
    "summary": {
      "actionDate": "2025-07-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Health Care and Lowering Costs Act</strong></p><p>This bill makes permanent temporary provisions that generally expand eligibility for and increase the amount of the premium tax credit.\u00a0This bill also repeals multiple Medicaid, Medicare, and health-related tax provisions enacted by the One Big Beautiful Bill Act (OBBBA).</p><p>Currently, eligible taxpayers may claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To qualify, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL) and, after 2025, may not exceed 400% of the FPL (maximum income limit). For 2021-2025, the maximum income limit is eliminated, which generally expands eligibility for the premium tax credit.</p><p>Further, under current law, the amount of the premium tax credit is partially based on the taxpayer\u2019s household income multiplied by the applicable percentage. The applicable percentage varies depending on which of six income ranges (adjusted for inflation after 2025) the taxpayer\u2019s household income falls within. For 2021-2025, the applicable percentages are lowered and the adjustment of the applicable percentages for inflation is eliminated, which generally increases the amount of the premium tax credit.</p><p>The bill permanently eliminates the 400% maximum income limit, lowers the applicable percentages, and eliminates the inflation adjustment for the applicable percentages.</p><p>Finally, the bill repeals multiple Medicaid, Medicare, and health-related tax provisions enacted by the OBBBA, including</p><ul><li>certain Medicare and Medicare eligibility and verification requirements,</li><li>the reduced window for retroactive Medicaid coverage, and</li><li>premium tax credit verification requirements.</li></ul>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s2556"
    },
    "title": "Protecting Health Care and Lowering Costs Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Health Care and Lowering Costs Act</strong></p><p>This bill makes permanent temporary provisions that generally expand eligibility for and increase the amount of the premium tax credit.\u00a0This bill also repeals multiple Medicaid, Medicare, and health-related tax provisions enacted by the One Big Beautiful Bill Act (OBBBA).</p><p>Currently, eligible taxpayers may claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To qualify, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL) and, after 2025, may not exceed 400% of the FPL (maximum income limit). For 2021-2025, the maximum income limit is eliminated, which generally expands eligibility for the premium tax credit.</p><p>Further, under current law, the amount of the premium tax credit is partially based on the taxpayer\u2019s household income multiplied by the applicable percentage. The applicable percentage varies depending on which of six income ranges (adjusted for inflation after 2025) the taxpayer\u2019s household income falls within. For 2021-2025, the applicable percentages are lowered and the adjustment of the applicable percentages for inflation is eliminated, which generally increases the amount of the premium tax credit.</p><p>The bill permanently eliminates the 400% maximum income limit, lowers the applicable percentages, and eliminates the inflation adjustment for the applicable percentages.</p><p>Finally, the bill repeals multiple Medicaid, Medicare, and health-related tax provisions enacted by the OBBBA, including</p><ul><li>certain Medicare and Medicare eligibility and verification requirements,</li><li>the reduced window for retroactive Medicaid coverage, and</li><li>premium tax credit verification requirements.</li></ul>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s2556"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2556is.xml"
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
      "title": "Protecting Health Care and Lowering Costs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Health Care and Lowering Costs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal the changes made by the health subtitle of the One Big Beautiful Bill Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:21Z"
    }
  ]
}
```
