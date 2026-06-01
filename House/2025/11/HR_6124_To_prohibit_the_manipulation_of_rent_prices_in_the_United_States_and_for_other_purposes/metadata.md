# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6124?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6124
- Title: End Rent Fixing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6124
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-03-31T08:05:31Z
- Update date including text: 2026-03-31T08:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6124",
    "number": "6124",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001318",
        "district": "",
        "firstName": "Becca",
        "fullName": "Rep. Balint, Becca [D-VT-At Large]",
        "lastName": "Balint",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "End Rent Fixing Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-31T08:05:31Z",
    "updateDateIncludingText": "2026-03-31T08:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-11-19T15:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "IL"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "OR"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "TX"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MN"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "PA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NH"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "GA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "WA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "DC"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MN"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "IL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "OR"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MI"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "FL"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CT"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "OR"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "PA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "PA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-01-23",
      "state": "NJ"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "OR"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-02-17",
      "state": "MA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MI"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-03-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6124ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6124\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Ms. Balint (for herself, Mr. Garc\u00eda of Illinois , Ms. Bonamici , Mr. Casar , Ms. Craig , Mr. Deluzio , Mr. Gomez , Ms. Goodlander , Mr. Johnson of Georgia , Ms. Jayapal , Ms. Norton , Ms. Omar , Mrs. Ramirez , Ms. Salinas , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit the manipulation of rent prices in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Rent Fixing Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Coordinating function**\nThe term coordinating function means\u2014\n**(A)**\ncollecting historical or contemporaneous prices, supply levels, or lease or rental contract termination and renewal dates of residential dwelling units, either directly or indirectly, from 2 or more rental property owners;\n**(B)**\nanalyzing or processing the information described in subparagraph (A) using a system, software, or process that uses the same or a similar formula or methodology, including by using that information to train an algorithm to predict rental prices, lease renewal terms, or ideal occupancy levels; and\n**(C)**\nrecommending rental prices, lease renewal terms, or occupancy levels to 2 or more rental property owners.\n**(3) Coordinator**\nThe term coordinator means any person that performs a coordinating function for any rental property owner, including a rental property owner performing a coordinating function for their own benefit.\n**(4) Person**\nThe term person has the meaning given the term in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ).\n**(5) Residential dwelling unit**\nThe term residential dwelling unit \u2014\n**(A)**\nmeans any house, apartment, accessory unit, manufactured home, manufactured housing community lot, or other unit used as a residence; and\n**(B)**\ndoes not include inpatient medical care, licensed long-term care, and detention or correctional facilities.\n**(6) Rental property owner**\nThe term rental property owner means any individual, corporation, partnership, association, joint-stock company, trust, or unincorporated organization, including an organization not organized to carry on business for its own profit or that of its members, that owns real property and leases or rents such property or any portion thereof.\n**(7) State**\nThe term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, and any territory or possession of the United States.\n#### 3. Unlawful conduct\n##### (a) Conspiracy\nIt shall be unlawful for a rental property owner, in or affecting commerce, or any agent or subcontractor thereof, to knowingly subscribe to, contract with, or otherwise exchange anything of value in return for the services of a coordinator, and such action shall be deemed to be an unlawful method of competition in violation of section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) and a per se violation of section 1 of the Sherman Act ( 15 U.S.C. 1 ).\n##### (b) Coordination\nIt shall be unlawful for any person, in or affecting commerce, to perform a coordinating function, and such action shall be deemed to be an unlawful method of competition in violation of section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) and a per se violation of section 1 of the Sherman Act ( 15 U.S.C. 1 ).\n#### 4. Enforcement\n##### (a) In general\n**(1) Federal Trade Commission**\nA violation of this Act shall also constitute an unfair method of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), and if the Commission has reason to believe that a person violated this Act, the Commission\u2014\n**(A)**\nmay commence a civil action, in its own name by any of its attorneys designated by it for such purpose, to recover a civil penalty and seek other appropriate relief; and\n**(B)**\nshall have jurisdiction to enforce this Act against an organization not organized to carry on business for its own profit or that of its members.\n**(2) Attorney General**\nThe Attorney General shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers and duties as though all applicable terms of the Sherman Act ( 15 U.S.C. 1 et seq. ), Clayton Act ( 15 U.S.C. 12 et seq. ), and Antitrust Civil Process Act ( 15 U.S.C. 1311 et seq. ) were incorporated into and made a part of this Act.\n**(3) State attorneys general**\nAny attorney general of a State shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers and duties as though all applicable terms of the Sherman Act ( 15 U.S.C. 1 et seq. ) and the Clayton Act ( 15 U.S.C. 12 et seq. ) were incorporated into and made a part of this Act.\n##### (b) Civil actions by injured persons\n**(1) Civil action authorized**\nAny person who is aggrieved by a violation of this Act may bring a civil action in an appropriate district court of the United States, without respect to the amount in controversy, to recover an amount described in paragraph (2).\n**(2) Award amount**\n**(A) In general**\nThe court shall award the plaintiff threefold the damages sustained by the plaintiff and the reasonable cost of litigation, including a reasonable attorney fee.\n**(B) Interest on damages**\nPursuant to a motion by plaintiff promptly made, the court may award simple interest on actual damages sustained by the plaintiff for the period beginning on the date of service of the pleading of the plaintiff setting forth a claim under this Act and ending on the date of judgment, or for any shorter period therein.\n**(3) Invalidity of pre-dispute arbitration agreements and pre-dispute joint action waivers**\nAt the election of the plaintiff in an action authorized under paragraph (1), a pre-dispute arbitration agreement or pre-dispute joint action waiver relating to a violation of this Act shall be invalid or unenforceable.\n#### 5. Standards of pleading\nIn a civil action alleging a violation of sections 1 or 3(a) of the Sherman Act ( 15 U.S.C. 1 , 3(a)), including an action brought by the United States, a State attorney general, or the Federal Trade Commission under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), a complaint need not allege facts tending to exclude the possibility of independent action and shall not be dismissed for failure to state a claim unless it appears beyond doubt that the claimant can prove no set of facts in support of their claim which would entitle them to relief.\n#### 6. Relationship to other laws\n##### (a) Antitrust laws\nNothing in this Act, or any amendment made by this Act, shall be construed to impair or supersede the operation of any of the antitrust laws, and the unlawful conduct set forth in this Act is in addition to and not instead of conduct prohibited by the antitrust laws.\n##### (b) State laws\nNothing in this Act may be construed to preempt, annul, alter, or affect, or exempt any person subject to the provisions of this Act from complying with the laws of any State, except to the extent that those laws are inconsistent with any provision of this Act, and then only to the extent of the inconsistency. For purposes of this section, a State law is not inconsistent with this Act if the protection such law affords any person greater than the protection provided by this Act.\n#### 7. Severability\nIf any provision of this Act, or the application of such a provision to any person or circumstance, is held to be unconstitutional, the remaining provisions of this Act, and the application of such provisions to any person or circumstance shall not be affected thereby.",
      "versionDate": "2025-11-19",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-11-19",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3207",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "End Rent Fixing Act of 2025",
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
        "name": "Commerce",
        "updateDate": "2025-12-01T19:40:56Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6124ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "End Rent Fixing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End Rent Fixing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the manipulation of rent prices in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:48:36Z"
    }
  ]
}
```
