# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1552?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1552
- Title: Living Donor Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1552
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-04-18T11:03:24Z
- Update date including text: 2026-04-18T11:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-02-26 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-03-11 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-03-11 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-03-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 352.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-02-26 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-03-11 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-03-11 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2026-03-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 352.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1552",
    "number": "1552",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Living Donor Protection Act of 2025",
    "type": "S",
    "updateDate": "2026-04-18T11:03:24Z",
    "updateDateIncludingText": "2026-04-18T11:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 352.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-26",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
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
        "item": [
          {
            "date": "2026-03-11T20:20:47Z",
            "name": "Reported By"
          },
          {
            "date": "2026-02-26T15:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-01T16:02:05Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-01T16:02:05Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NY"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "MS"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NM"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "WV"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-05-01",
      "state": "ME"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "CT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "VA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "MN"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "OR"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "RI"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "DE"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "TN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NE"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NC"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "IL"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NH"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "MN"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "OR"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "AZ"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NV"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "GA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NJ"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "MI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NJ"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "CT"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "AR"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "AZ"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "WV"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "MT"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "ME"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-10-20",
      "state": "CO"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-27",
      "state": "LA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "MD"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "ND"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "MT"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MI"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "KS"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "IL"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "AL"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "AK"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "IN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "MD"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "IN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "VT"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-04-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1552is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1552\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Cotton (for himself, Mrs. Gillibrand , Mrs. Hyde-Smith , Mr. Luj\u00e1n , Mrs. Capito , Mr. King , Mr. Blumenthal , Mr. Kaine , Ms. Klobuchar , Mr. Merkley , Mr. Whitehouse , Mr. Coons , Mrs. Blackburn , Mr. Ricketts , Mr. Tillis , Mr. Durbin , Mrs. Shaheen , Ms. Smith , Mr. Wyden , Mr. Kelly , Ms. Rosen , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo promote and protect from discrimination living organ donors.\n#### 1. Short title\nThis Act may be cited as the Living Donor Protection Act of 2025 .\n#### 2. Prohibition on denial of coverage or increase in premiums of life or disability insurance for living organ donors\n##### (a) Prohibition\nNotwithstanding any other provision of law, an insurer shall not deny coverage, cancel coverage, refuse to issue, determine the price or premium for, or otherwise vary any term or condition of a life insurance policy, disability insurance policy, or long-term care insurance policy for a person based solely, and without any actual, unique, and material actuarial risks, on the status of such person as a living organ donor.\n##### (b) Enforcement\nA State insurance regulator may take such actions to enforce subsection (a) as are specifically authorized under the laws of such State.\n##### (c) Definitions\nIn this section:\n**(1) Disability insurance policy**\nThe term disability insurance policy means a contract under which an entity promises to pay a person a sum of money in the event that an illness or injury resulting in a disability prevents such person from working.\n**(2) Life insurance policy**\nThe term life insurance policy means a contract under which an entity promises to pay a designated beneficiary a sum of money upon the death of the insured.\n**(3) Living organ donor**\nThe term living organ donor means an individual who has donated all or part of an organ and is not deceased.\n**(4) Long-term care insurance policy**\nThe term long-term care insurance policy means a contract for which the only insurance protection provided under the contract is coverage of qualified long-term care services (as defined in section 7702B(c) of the Internal Revenue Code of 1986).\n#### 3. Clarification of organ donation surgery as qualifying as a serious health condition under FMLA\n##### (a) Private sector employees\nSection 101(11) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611(11) ) is amended, in the matter preceding subparagraph (A), by inserting (including recovery from surgery related to organ donation) after physical or mental condition .\n##### (b) Federal civil service employees\n**(1) Definition**\nSection 6381(5) of title 5, United States Code, is amended, in the matter preceding subparagraph (A), by inserting (including recovery from surgery related to organ donation) after physical or mental condition .\n**(2) Relationship to organ donor leave**\nSection 6382(d)(1) of title 5, United States Code, is amended by adding at the end the following: An employee who takes any part of the 12-week period of leave under subsection (a)(1) to serve as an organ donor (including recovery from surgery related to organ donation) may elect to substitute, for as much of that part as possible, any leave available to the employee under section 6327. .\n#### 4. Updating of educational materials on the benefits and risks of living organ donation\n##### (a) Educational materials\n**(1) Review and updating**\nNot later than 6 months after the date of enactment of this Act, the Secretary of Health and Human Services (in this section referred to as the Secretary ) shall review and update materials related to living organ donation in order to educate the public on\u2014\n**(A)**\nthe benefits and risks of living organ donation; and\n**(B)**\nthe impact of living organ donation on the access of a living organ donor to insurance.\n**(2) Information on statutory changes**\nSuch updating shall include information regarding the requirements under section 2 and the amendments made by section 3.\n##### (b) Methods of updating\nIn carrying out subsection (a), the Secretary shall update, as appropriate\u2014\n**(1)**\npublic service announcements previously provided by the Secretary;\n**(2)**\npublicly accessible websites (such as organdonor.gov, or a successor website) that are maintained by the Secretary and that contain information and resources regarding living organ donation; and\n**(3)**\nother media, as the Secretary determines appropriate.",
      "versionDate": "2025-05-01",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1552rs.xml",
      "text": "II\nCalendar No. 352\n119th CONGRESS\n2d Session\nS. 1552\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Cotton (for himself, Mrs. Gillibrand , Mrs. Hyde-Smith , Mr. Luj\u00e1n , Mrs. Capito , Mr. King , Mr. Blumenthal , Mr. Kaine , Ms. Klobuchar , Mr. Merkley , Mr. Whitehouse , Mr. Coons , Mrs. Blackburn , Mr. Ricketts , Mr. Tillis , Mr. Durbin , Mrs. Shaheen , Ms. Smith , Mr. Wyden , Mr. Kelly , Ms. Rosen , Mr. Warnock , Mr. Kim , Mr. Peters , Mr. Booker , Mr. Murphy , Mr. Boozman , Mr. Gallego , Mr. Justice , Mr. Daines , Ms. Collins , Mr. Bennet , Mr. Kennedy , Ms. Alsobrooks , Mr. Cramer , Mr. Schiff , Mr. Sheehy , Ms. Slotkin , Mr. Marshall , Ms. Duckworth , Mr. Tuberville , Ms. Murkowski , Mr. Young , Mr. Van Hollen , Mr. Banks , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nMarch 11, 2026 Reported by Mr. Cassidy , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo promote and protect from discrimination living organ donors.\n#### 1. Short title\nThis Act may be cited as the Living Donor Protection Act of 2025 .\n#### 2. Prohibition on denial of coverage or increase in premiums of life or disability insurance for living organ donors\n##### (a) Prohibition\nNotwithstanding any other provision of law, an insurer shall not deny coverage, cancel coverage, refuse to issue, determine the price or premium for, or otherwise vary any term or condition of a life insurance policy, disability insurance policy, or long-term care insurance policy for a person based solely, and without any actual, unique, and material actuarial risks, on the status of such person as a living organ donor.\n##### (b) Enforcement\nA State insurance regulator may take such actions to enforce subsection (a) as are specifically authorized under the laws of such State.\n##### (c) Definitions\nIn this section:\n**(1) Disability insurance policy**\nThe term disability insurance policy means a contract under which an entity promises to pay a person a sum of money in the event that an illness or injury resulting in a disability prevents such person from working.\n**(2) Life insurance policy**\nThe term life insurance policy means a contract under which an entity promises to pay a designated beneficiary a sum of money upon the death of the insured.\n**(3) Living organ donor**\nThe term living organ donor means an individual who has donated all or part of an organ and is not deceased.\n**(4) Long-term care insurance policy**\nThe term long-term care insurance policy means a contract for which the only insurance protection provided under the contract is coverage of qualified long-term care services (as defined in section 7702B(c) of the Internal Revenue Code of 1986).\n#### 3. Clarification of organ donation surgery as qualifying as a serious health condition under FMLA\n##### (a) Private sector employees\nSection 101(11) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611(11) ) is amended, in the matter preceding subparagraph (A), by inserting (including recovery from surgery related to organ donation) after physical or mental condition .\n##### (b) Federal civil service employees\n**(1) Definition**\nSection 6381(5) of title 5, United States Code, is amended, in the matter preceding subparagraph (A), by inserting (including recovery from surgery related to organ donation) after physical or mental condition .\n**(2) Relationship to organ donor leave**\nSection 6382(d)(1) of title 5, United States Code, is amended by adding at the end the following: An employee who takes any part of the 12-week period of leave under subsection (a)(1) to serve as an organ donor (including recovery from surgery related to organ donation) may elect to substitute, for as much of that part as possible, any leave available to the employee under section 6327. .\n#### 4. Updating of educational materials on the benefits and risks of living organ donation\n##### (a) Educational materials\n**(1) Review and updating**\nNot later than 6 months after the date of enactment of this Act, the Secretary of Health and Human Services (in this section referred to as the Secretary ) shall review and update materials related to living organ donation in order to educate the public on\u2014\n**(A)**\nthe benefits and risks of living organ donation; and\n**(B)**\nthe impact of living organ donation on the access of a living organ donor to insurance.\n**(2) Information on statutory changes**\nSuch updating shall include information regarding the requirements under section 2 and the amendments made by section 3.\n##### (b) Methods of updating\nIn carrying out subsection (a), the Secretary shall update, as appropriate\u2014\n**(1)**\npublic service announcements previously provided by the Secretary;\n**(2)**\npublicly accessible websites (such as organdonor.gov, or a successor website) that are maintained by the Secretary and that contain information and resources regarding living organ donation; and\n**(3)**\nother media, as the Secretary determines appropriate.",
      "versionDate": "2026-03-11",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-07-22",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on Oversight and Government Reform, and House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4582",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Family and Medical Leave Act of 1993 and title 5, United States Code, to clarify that organ donation surgery qualifies as a serious health condition.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-22",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4583",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Living Donor Protection Act of 2025",
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
            "name": "Disability and health-based discrimination",
            "updateDate": "2026-03-16T16:48:39Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2026-03-16T16:48:39Z"
          },
          {
            "name": "Employee leave",
            "updateDate": "2026-03-16T16:48:39Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-03-16T16:48:39Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-16T16:48:39Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2026-03-16T16:48:39Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-03-16T16:48:39Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2026-03-16T16:48:39Z"
          },
          {
            "name": "Life, casualty, property insurance",
            "updateDate": "2026-03-16T16:48:39Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2026-03-16T16:48:39Z"
          },
          {
            "name": "Organ and tissue donation and transplantation",
            "updateDate": "2026-03-16T16:48:39Z"
          },
          {
            "name": "Surgery and anesthesia",
            "updateDate": "2026-03-16T16:48:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-21T12:04:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-01",
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
          "measure-id": "id119s1552",
          "measure-number": "1552",
          "measure-type": "s",
          "orig-publish-date": "2025-05-01",
          "originChamber": "SENATE",
          "update-date": "2026-02-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1552v00",
            "update-date": "2026-02-26"
          },
          "action-date": "2025-05-01",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Living Donor Protection Act of </strong><strong>2025</strong></p><p>This bill prohibits life insurance, disability insurance, and long-term insurance\u00a0carriers from denying or otherwise restricting coverage for\u00a0living organ donors.</p><p>Specifically, carriers may not deny, cancel, vary premiums, or otherwise impose conditions on policies based on an individual's status as a living organ donor.</p><p>The bill also expressly specifies that recovery from organ-donation surgery constitutes a serious health condition that entitles eligible employees to job-protected medical leave.</p><p>In addition, the Department of Health and Human Services must update educational materials on living organ donation to include information about the benefits and risks of living organ donation and the impact of donation on insurance access, particularly with respect to the bill's changes.</p>"
        },
        "title": "Living Donor Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1552.xml",
    "summary": {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Living Donor Protection Act of </strong><strong>2025</strong></p><p>This bill prohibits life insurance, disability insurance, and long-term insurance\u00a0carriers from denying or otherwise restricting coverage for\u00a0living organ donors.</p><p>Specifically, carriers may not deny, cancel, vary premiums, or otherwise impose conditions on policies based on an individual's status as a living organ donor.</p><p>The bill also expressly specifies that recovery from organ-donation surgery constitutes a serious health condition that entitles eligible employees to job-protected medical leave.</p><p>In addition, the Department of Health and Human Services must update educational materials on living organ donation to include information about the benefits and risks of living organ donation and the impact of donation on insurance access, particularly with respect to the bill's changes.</p>",
      "updateDate": "2026-02-26",
      "versionCode": "id119s1552"
    },
    "title": "Living Donor Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Living Donor Protection Act of </strong><strong>2025</strong></p><p>This bill prohibits life insurance, disability insurance, and long-term insurance\u00a0carriers from denying or otherwise restricting coverage for\u00a0living organ donors.</p><p>Specifically, carriers may not deny, cancel, vary premiums, or otherwise impose conditions on policies based on an individual's status as a living organ donor.</p><p>The bill also expressly specifies that recovery from organ-donation surgery constitutes a serious health condition that entitles eligible employees to job-protected medical leave.</p><p>In addition, the Department of Health and Human Services must update educational materials on living organ donation to include information about the benefits and risks of living organ donation and the impact of donation on insurance access, particularly with respect to the bill's changes.</p>",
      "updateDate": "2026-02-26",
      "versionCode": "id119s1552"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1552is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1552rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Living Donor Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-18T11:03:24Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Living Donor Protection Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-03-13T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Living Donor Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote and protect from discrimination living organ donors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:26Z"
    }
  ]
}
```
