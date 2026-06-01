# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1227?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1227
- Title: ABC Act
- Congress: 119
- Bill type: S
- Bill number: 1227
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2026-04-28T11:03:21Z
- Update date including text: 2026-04-28T11:03:21Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1227",
    "number": "1227",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "ABC Act",
    "type": "S",
    "updateDate": "2026-04-28T11:03:21Z",
    "updateDateIncludingText": "2026-04-28T11:03:21Z"
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
        "item": [
          {
            "date": "2025-04-01T20:03:24Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-01T20:03:24Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WV"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CO"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MS"
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "NC"
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "FL"
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WY"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "AZ"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "AL"
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "SD"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "RI"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "LA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "DE"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MO"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "IL"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NM"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "AR"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "NE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "NV"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "ME"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "NJ"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1227is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1227\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Markey (for himself, Mrs. Capito , Mr. Hickenlooper , Mrs. Hyde-Smith , Mr. Blumenthal , Mr. Tillis , Ms. Klobuchar , Mr. Scott of Florida , Ms. Baldwin , Ms. Lummis , Mr. Kelly , Mrs. Britt , Ms. Hirono , Mr. Rounds , Mr. Whitehouse , Mr. Cassidy , Mr. Coons , and Mr. Schmitt ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require the Administrator of the Centers for Medicare & Medicaid Services and the Commissioner of Social Security to review and simplify the processes, procedures, forms, and communications for family caregivers to assist individuals in establishing eligibility for, enrolling in, and maintaining and utilizing coverage and benefits under the Medicare, Medicaid, CHIP, and Social Security programs respectively, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Alleviating Barriers for Caregivers Act or the ABC Act .\n#### 2. Review of Medicare, Medicaid, CHIP, and Social Security to simplify processes. procedures, forms, and communications\n##### (a) Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Centers for Medicare & Medicaid Services.\n**(2) CHIP**\nThe term CHIP means the Children\u2019s Health Insurance Program established under title XXI of the Social Security Act ( 42 U.S.C. 1397aa et seq. ).\n**(3) Commissioner**\nThe term Commissioner means the Commissioner of Social Security.\n**(4) Covered agencies**\nThe term covered agencies means the Centers for Medicare & Medicaid Services and the Social Security Administration.\n**(5) Covered officials**\nThe term covered officials means the Administrator and Commissioner.\n**(6) Covered programs**\nThe term covered programs means Medicare, Medicaid, CHIP, and the Social Security programs.\n**(7) Disability**\nThe term disability has the meaning given such term in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 ).\n**(8) Family caregiver**\nThe term family caregiver has the meaning given the term in section 2 of the RAISE Family Caregivers Act ( 42 U.S.C. 3030s note).\n**(9) Medicaid**\nThe term Medicaid means the Medicaid program established under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ).\n**(10) Medicare**\nThe term Medicare means the Medicare program established under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ).\n**(11) State**\nThe term State means any of the 50 States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, Guam, American Samoa, or the Commonwealth of the Northern Mariana Islands.\n**(12) Social Security programs**\nThe term Social Security programs means each of the following:\n**(A)**\nThe programs for old-age and survivors insurance benefits and disability insurance benefits established under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ).\n**(B)**\nThe program for supplemental security income benefits established under title XVI of such Act ( 42 U.S.C. 1381 et seq. ).\n##### (b) Review of programs\n**(1) In general**\nThe Administrator and the Commissioner shall jointly conduct a review of the eligibility determination and application processes, procedures, forms, and communications of Medicare, Medicaid, CHIP, and the Social Security programs.\n**(2) Goals of the review**\nIn conducting the reviews under paragraph (1), the covered officials shall seek ways to\u2014\n**(A)**\nsimplify and streamline policies and procedures for determining eligibility for, enrolling in, maintaining coverage in, and utilizing the full benefits available under the covered programs;\n**(B)**\nreduce the frequency of family caregivers having to\u2014\n**(i)**\nprovide the same information to covered agencies more than once;\n**(ii)**\ncomplete\u2014\n**(I)**\nmultiple documents for each covered agency; or\n**(II)**\ndocuments requesting the same or similar information for multiple covered agencies; or\n**(iii)**\nprovide information to the covered agencies that\u2014\n**(I)**\nthe covered agencies already have; or\n**(II)**\nthe covered agencies can easily receive from other Federal agencies; and\n**(C)**\nmake it easier for family caregivers to work with the covered agencies and the State agencies responsible for administering State Medicaid and CHIP plans by\u2014\n**(i)**\nproviding information on eligibility for, enrollment in, maintaining coverage in, and utilizing the full benefits available under the covered programs to family caregivers;\n**(ii)**\nimproving communications between family caregivers and employees of covered agencies by\u2014\n**(I)**\ndecreasing call wait times;\n**(II)**\nensuring that employees of covered agencies and the State agencies responsible for administering State Medicaid and CHIP plans provide timely answers to the questions of family caregivers;\n**(III)**\nimproving the websites of the covered programs\u2014\n**(aa)**\nby making it easier for family caregivers to find information regarding benefit availability, eligibility, and how to maintain coverage; and\n**(bb)**\nby designing such websites to align with the requirements of the Americans with Disabilities Act ( 42 U.S.C. 12101 et seq. ) regarding web design;\n**(IV)**\nimproving the timely access to in-person appointments or meetings between employees of covered agencies and family caregivers;\n**(V)**\nproviding translation or interpretation services for family caregivers for whom English is not their primary language; and\n**(VI)**\nproviding information to family caregivers in accessible formats, including formats compatible with American Sign Language and multiple languages;\n**(iii)**\nensuring that employees of covered agencies and the State agencies responsible for administering State Medicaid and CHIP plans understand how the covered programs can help family caregivers;\n**(iv)**\nimproving the relationship between family caregivers and the covered agencies and the State agencies responsible for administering State Medicaid and CHIP plans, which may include regularly meeting with family caregivers, individuals entitled to, receiving services from, or filing for, 1 or more of the covered programs, and other stakeholders of the covered programs;\n**(v)**\nensuring that employees of covered agencies and the State agencies responsible for administering State Medicaid and CHIP plans who are responsible for resolving disputes, appeals, and grievances within the covered programs receive education, training, and guidance on specific issues faced by family caregivers who participate in the covered programs; and\n**(vi)**\ntaking other actions the covered officials may identify.\n**(3) Input from family caregivers, organizations, and State entities**\nIn conducting the reviews under paragraph (1), the covered officials shall seek input from\u2014\n**(A)**\nfamily caregivers, including family caregivers with a disability, that have interacted with the covered programs;\n**(B)**\nState, regional, national, and Tribal organizations representing or working with family caregivers or individuals receiving care from family caregivers; and\n**(C)**\nState Medicaid and CHIP programs.\n##### (c) Action\nAfter the reviews under subsection (b) have been completed, the covered officials shall take actions that will simplify and streamline policies and procedures that improve customer service for individuals entitled to, receiving services from, or filing for, any of the covered programs, and family caregivers.\n##### (d) Report to Congress\n**(1) In general**\nNo later than 2 years after the date of enactment of this Act, the covered officials shall each submit a report to the Committee on Finance of the Senate, the Committee on Ways and Means of the House of Representatives, and the Committee on Energy and Commerce of the House of Representatives that details the results of the respective reviews each covered official conducted under subsection (b).\n**(2) Contents of the report**\nThe reports required under paragraph (1) shall contain\u2014\n**(A)**\nissues that the covered officials identified in the reviews and their findings;\n**(B)**\nthe actions that the covered officials are taking to address the issues in subparagraph (A);\n**(C)**\nan estimate on when the actions in subparagraph (B) will be completed;\n**(D)**\nprojected annual costs to implement the actions identified in subparagraph (B); and\n**(E)**\nany recommended change in Federal law to address any issue identified in subparagraph (A).\n**(3) Updated reports**\nThe covered officials shall each submit a report 2 years after submitting the report required under paragraph (1) providing an update to the contents identified in paragraph (2).\n**(4) Publication of the reports**\nThe covered officials shall make the reports required under paragraphs (1) and (3) publicly accessible on the websites of covered agencies.\n##### (e) Reducing red tape for State Medicaid and CHIP programs\nNot later than 1 year after the date of enactment of this Act, the Administrator shall issue a letter to each State Medicaid and CHIP Director to\u2014\n**(1)**\nencourage State Medicaid agencies to conduct reviews of State Medicaid programs and State CHIP programs similar to the reviews conducted at the Federal level under subsection (b);\n**(2)**\nprovide suggestions, informed by the results of such Federal reviews, for promising practices that States could take to reduce administrative burdens on family caregivers in supporting individuals entitled to, receiving service from, or filing for, 1 or more of the covered programs in applying for and receiving assistance under State Medicaid programs and State CHIP programs; and\n**(3)**\nidentify best practices to support family caregivers.",
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
        "actionDate": "2025-03-31",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2491",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ABC Act",
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
        "name": "Health",
        "updateDate": "2025-05-01T13:24:41Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1227is.xml"
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
      "title": "ABC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ABC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Alleviating Barriers for Caregivers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the Centers for Medicare & Medicaid Services and the Commissioner of Social Security to review and simplify the processes, procedures, forms, and communications for family caregivers to assist individuals in establishing eligibility for, enrolling in, and maintaining and utilizing coverage and benefits under the Medicare, Medicaid, CHIP, and Social Security programs respectively, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:22Z"
    }
  ]
}
```
