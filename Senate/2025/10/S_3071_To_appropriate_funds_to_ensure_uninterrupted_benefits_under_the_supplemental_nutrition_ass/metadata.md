# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3071?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3071
- Title: Keep SNAP and WIC Funded Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3071
- Origin chamber: Senate
- Introduced date: 2025-10-29
- Update date: 2025-12-05T21:59:58Z
- Update date including text: 2025-12-05T21:59:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-29: Introduced in Senate
- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Read twice and referred to the Committee on Appropriations.
- Latest action: 2025-10-29: Introduced in Senate

## Actions

- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Read twice and referred to the Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-29",
    "latestAction": {
      "actionDate": "2025-10-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3071",
    "number": "3071",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Keep SNAP and WIC Funded Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:59:58Z",
    "updateDateIncludingText": "2025-12-05T21:59:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-29",
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
          "date": "2025-10-29T19:44:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "MN"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "NY"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "MD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "WA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
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
      "sponsorshipDate": "2025-10-29",
      "state": "NY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "NH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "CO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "NJ"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-10-29",
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
      "sponsorshipDate": "2025-10-29",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "WA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "GA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "CA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "MI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-10-29",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "HI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "CA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "NH"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "MI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "VA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "GA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "OR"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3071is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3071\nIN THE SENATE OF THE UNITED STATES\nOctober 29, 2025 Mr. Luj\u00e1n (for himself, Ms. Klobuchar , Mr. Schumer , Ms. Alsobrooks , Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Booker , Ms. Cantwell , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mr. Gallego , Mrs. Gillibrand , Ms. Hassan , Mr. Heinrich , Mr. Hickenlooper , Ms. Hirono , Mr. Kaine , Mr. Kelly , Mr. Kim , Mr. King , Mr. Markey , Mr. Merkley , Mr. Murphy , Mrs. Murray , Mr. Ossoff , Mr. Padilla , Mr. Peters , Mr. Reed , Ms. Rosen , Mr. Sanders , Mr. Schatz , Mr. Schiff , Mrs. Shaheen , Ms. Slotkin , Ms. Smith , Mr. Van Hollen , Mr. Warner , Mr. Warnock , Ms. Warren , Mr. Welch , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nTo appropriate funds to ensure uninterrupted benefits under the supplemental nutrition assistance program and the special supplemental nutrition program for women, infants, and children.\n#### 1. Short title\nThis Act may be cited as the Keep SNAP and WIC Funded Act of 2025 .\n#### 2. Uninterrupted benefits under supplemental nutrition assistance program and special supplemental nutrition program for women, infants, and children\n##### (a) In general\nIn fiscal year 2026, for any period during which interim continuing appropriations or full-year appropriations for that fiscal year have not been enacted for the Department of Agriculture, there are appropriated to the Secretary of Agriculture, out of any money in the Treasury not otherwise appropriated, such sums as are necessary\u2014\n**(1)**\nto provide uninterrupted benefits under the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. );\n**(2)**\nto provide consolidated block grants under section 19 of that Act ( 7 U.S.C. 2028 ); and\n**(3)**\nto carry out without interruption the special supplemental nutrition program for women, infants, and children established by section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ).\n##### (b) Retroactivity\nThe appropriations under subsection (a) shall include any amounts necessary for payment of any missed benefits described in that subsection during the period beginning on September 30, 2025, and ending on the date of enactment of this Act.\n##### (c) Termination\nAppropriations shall be made available pursuant to subsection (a) until the earlier of\u2014\n**(1)**\nthe date of enactment into law of appropriations (including a continuing appropriation) for the Department of Agriculture for fiscal year 2026; and\n**(2)**\nSeptember 30, 2026.\n##### (d) Reimbursements to States\nThe Secretary of Agriculture shall use the amounts made available pursuant to subsection (a) to reimburse State agencies for costs incurred in carrying out the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ), including consolidated block grants under section 19 of that Act ( 7 U.S.C. 2028 ), and the special supplemental nutrition program for women, infants, and children established by section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ), including the cost of benefits issued under those programs, during a lapse in appropriations for those programs, to the extent that the State agency carried out those programs in accordance with Federal law (including regulations) during that lapse.\n##### (e) Charge to future appropriations\nExpenditures made pursuant to this Act shall be charged to the applicable appropriation, fund, or authorization whenever a bill in which such applicable appropriation, fund, or authorization is contained is enacted into law.",
      "versionDate": "2025-10-29",
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
        "actionDate": "2025-10-24",
        "text": "Referred to the House Committee on Appropriations."
      },
      "number": "5822",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keep SNAP Funded Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-21",
        "text": "Read twice and referred to the Committee on Appropriations."
      },
      "number": "3024",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keep SNAP Funded Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-07",
        "text": "Referred to the House Committee on Appropriations."
      },
      "number": "5950",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Keep SNAP and WIC Funded Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-05T15:47:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-29",
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
          "measure-id": "id119s3071",
          "measure-number": "3071",
          "measure-type": "s",
          "orig-publish-date": "2025-10-29",
          "originChamber": "SENATE",
          "update-date": "2025-11-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3071v00",
            "update-date": "2025-11-06"
          },
          "action-date": "2025-10-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Keep SNAP and WIC Funded Act of 2025</strong></p><p>This bill provides FY2026 appropriations for the Department of Agriculture (USDA) to continue operating the Supplemental Nutrition Assistance Program (SNAP); the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC); and a related block grant program if there is a lapse in FY2026 appropriations for USDA.</p><p>Specifically, the bill provides appropriations to USDA for any period in which legislation to provide FY2026 interim continuing appropriations or full-year appropriations for USDA has not been enacted. If such a lapse in appropriations occurs, the bill provides the appropriations that are necessary to continue</p><ul><li>providing uninterrupted SNAP benefits,</li><li>providing consolidated block grants to Puerto Rico and American Samoa for nutrition assistance programs, and</li><li>carrying out\u00a0WIC without interruption.</li></ul><p>In addition, the bill provides appropriations to pay any benefits under these programs that were missed on or after September 30, 2025, and before this bill is enacted.</p><p>The appropriations for these purposes are available until the earlier of (1) the\u00a0enactment into law of legislation to provide FY2026 appropriations for USDA (including continuing appropriations), or (2) September 30, 2026.\u00a0</p><p>The bill also requires USDA to use the funds provided by this bill to reimburse state agencies for costs that were incurred to carry out these programs during a lapse in appropriations, to the extent that the programs were carried out in accordance with federal law (including regulations) during the lapse.\u00a0</p>"
        },
        "title": "Keep SNAP and WIC Funded Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3071.xml",
    "summary": {
      "actionDate": "2025-10-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Keep SNAP and WIC Funded Act of 2025</strong></p><p>This bill provides FY2026 appropriations for the Department of Agriculture (USDA) to continue operating the Supplemental Nutrition Assistance Program (SNAP); the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC); and a related block grant program if there is a lapse in FY2026 appropriations for USDA.</p><p>Specifically, the bill provides appropriations to USDA for any period in which legislation to provide FY2026 interim continuing appropriations or full-year appropriations for USDA has not been enacted. If such a lapse in appropriations occurs, the bill provides the appropriations that are necessary to continue</p><ul><li>providing uninterrupted SNAP benefits,</li><li>providing consolidated block grants to Puerto Rico and American Samoa for nutrition assistance programs, and</li><li>carrying out\u00a0WIC without interruption.</li></ul><p>In addition, the bill provides appropriations to pay any benefits under these programs that were missed on or after September 30, 2025, and before this bill is enacted.</p><p>The appropriations for these purposes are available until the earlier of (1) the\u00a0enactment into law of legislation to provide FY2026 appropriations for USDA (including continuing appropriations), or (2) September 30, 2026.\u00a0</p><p>The bill also requires USDA to use the funds provided by this bill to reimburse state agencies for costs that were incurred to carry out these programs during a lapse in appropriations, to the extent that the programs were carried out in accordance with federal law (including regulations) during the lapse.\u00a0</p>",
      "updateDate": "2025-11-06",
      "versionCode": "id119s3071"
    },
    "title": "Keep SNAP and WIC Funded Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Keep SNAP and WIC Funded Act of 2025</strong></p><p>This bill provides FY2026 appropriations for the Department of Agriculture (USDA) to continue operating the Supplemental Nutrition Assistance Program (SNAP); the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC); and a related block grant program if there is a lapse in FY2026 appropriations for USDA.</p><p>Specifically, the bill provides appropriations to USDA for any period in which legislation to provide FY2026 interim continuing appropriations or full-year appropriations for USDA has not been enacted. If such a lapse in appropriations occurs, the bill provides the appropriations that are necessary to continue</p><ul><li>providing uninterrupted SNAP benefits,</li><li>providing consolidated block grants to Puerto Rico and American Samoa for nutrition assistance programs, and</li><li>carrying out\u00a0WIC without interruption.</li></ul><p>In addition, the bill provides appropriations to pay any benefits under these programs that were missed on or after September 30, 2025, and before this bill is enacted.</p><p>The appropriations for these purposes are available until the earlier of (1) the\u00a0enactment into law of legislation to provide FY2026 appropriations for USDA (including continuing appropriations), or (2) September 30, 2026.\u00a0</p><p>The bill also requires USDA to use the funds provided by this bill to reimburse state agencies for costs that were incurred to carry out these programs during a lapse in appropriations, to the extent that the programs were carried out in accordance with federal law (including regulations) during the lapse.\u00a0</p>",
      "updateDate": "2025-11-06",
      "versionCode": "id119s3071"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3071is.xml"
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
      "title": "Keep SNAP and WIC Funded Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-08T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keep SNAP and WIC Funded Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T03:53:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to appropriate funds to ensure uninterrupted benefits under the supplemental nutrition assistance program and the special supplemental nutrition program for women, infants, and children.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T03:48:14Z"
    }
  ]
}
```
