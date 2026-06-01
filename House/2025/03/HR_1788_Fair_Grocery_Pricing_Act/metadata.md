# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1788?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1788
- Title: Fair Grocery Pricing Act
- Congress: 119
- Bill type: HR
- Bill number: 1788
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2025-10-29T08:05:57Z
- Update date including text: 2025-10-29T08:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1788",
    "number": "1788",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "F000476",
        "district": "10",
        "firstName": "Maxwell",
        "fullName": "Rep. Frost, Maxwell [D-FL-10]",
        "lastName": "Frost",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Fair Grocery Pricing Act",
    "type": "HR",
    "updateDate": "2025-10-29T08:05:57Z",
    "updateDateIncludingText": "2025-10-29T08:05:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:04:40Z",
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
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "MA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "MI"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "DC"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "LA"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "IL"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "WI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "IN"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "FL"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MA"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MD"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CT"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "TN"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "TX"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1788ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1788\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Frost introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit the use of algorithmic systems by food producers to artificially inflate the price or reduce the supply of their foods.\n#### 1. Short title\nThis Act may be cited as the Fair Grocery Pricing Act .\n#### 2. Definitions\nIn this Act:\n**(1) Chair**\nThe term Chair means the Chair of the Commission.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Consciously parallel pricing coordination**\nThe term consciously parallel pricing coordination means a tacit agreement between 2 or more food producers to raise, lower, change, maintain, or manipulate pricing for the purchase or sale of reasonably interchangeable food products.\n**(4) Coordinating function**\nThe term coordinating function means\u2014\n**(A)**\ncollecting historical or contemporaneous food product prices or supply levels from 2 or more food producers;\n**(B)**\nanalyzing or processing of the information described in subparagraph (A) using a system, software, or process that uses computation, including by using that information to train an algorithm; and\n**(C)**\nrecommending food prices, supply or output, or other commercial term to a food producer.\n**(5) Coordinator**\nThe term coordinator means any person that operates a software or data analytics service that performs a coordinating function for any food producer, including a food producer performing a coordinating function for their own benefit.\n**(6) Food**\nThe term food has the meaning given the term in the 321st section of the Food, Drug and Cosmetic Act ( 21 U.S.C. 321 ).\n**(7) Food producer**\nThe term food producer means any individual, corporation, or entity engaged in the manufacturing, processing, or production of food products for commercial distribution.\n**(8) Person**\nThe term person has the meaning given the term in the 1st section of the Clayton Act ( 15 U.S.C. 12 ).\n**(9) Pre-dispute arbitration agreement**\nThe term pre-dispute arbitration agreement means an agreement between 2 or more parties to arbitrate a dispute between the parties that is made before any dispute has arisen.\n**(10) Pre-dispute joint action waiver**\nThe term pre-dispute joint action waiver means an agreement between 2 or more parties, which may be part of a pre-dispute arbitration agreement, that\u2014\n**(A)**\nwould prohibit or waive the right of a party to participate in a joint, class, or collective action in a judicial, arbitral, administrative, or other forum relating to a dispute between parties; and\n**(B)**\nis made before any dispute has arisen.\n**(11) State**\nThe term State means any of the several States, the District of Columbia, the Commonwealth of Puerto Rico, or any territory or possession of the United States.\n#### 3. Unlawful conduct\n##### (a) In general\n**(1) Contract or conspiracy in restraint of trade**\nIt is unlawful for a food producer, in or affecting commerce, or any agent or subcontractor thereof, to subscribe to, contract with, or otherwise exchange anything of value or use in return for the services of a coordinator, and such action shall be deemed to be a per se violation of the Sherman Act ( 15 U.S.C. 1 et seq. ).\n**(2) Facilitation**\nIt is unlawful for a coordinator, in or affecting commerce, to facilitate an agreement among food producers to not compete with respect to food prices, supply or output, or other commercial term, including by performing a coordinating function.\n#### 4. Enforcement\n##### (a) Enforcement\n**(1) In general**\n**(A) Federal trade commission**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Attorney general**\nThe Attorney General shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms of the Sherman Act ( 15 U.S.C. 1 et seq. ), Clayton Act ( 15 U.S.C. 12 et seq. ), and Antitrust Civil Process Act ( 15 U.S.C. 1311 et seq. ) were incorporated into and made a part of this Act.\n**(C) State attorneys general**\nAny attorney general of a State shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms of the Sherman Act ( 15 U.S.C. 1 et seq. ) and the Clayton Act ( 15 U.S.C. 12 et seq. ) were incorporated into and made a part of this Act.\n**(2) Unfair methods of competition**\nA violation of this Act shall also constitute an unfair method of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ).\n**(3) Independent litigation authority**\nIf the Commission has reason to believe that a person violated this Act, the Commission may commence a civil action, in its own name by any of its attorneys designated by it for such purpose, to recover a civil penalty and seek other appropriate relief in any district court of the United States.\n**(4) Standards of pleading**\nIn a civil action under this subsection, a complaint\u2014\n**(A)**\nplausibly pleads a violation of section 1 or 3(a) of the Sherman Act ( 15 U.S.C. 1 , 3(a)) if the complaint contains factual allegations, including allegations of consciously parallel pricing coordination, demonstrating that the existence of a contract, or conspiracy in restraint of trade or commerce is among the realm of plausible possibilities; and\n**(B)**\nneed not allege facts tending to exclude the possibility of independent action.\n##### (b) Civil actions by injured persons\n**(1) Civil action authorized**\nAny person who is aggrieved by a violation of this Act may bring a civil action in an appropriate district court of the United States, without respect to the amount in controversy, to recover an amount described in paragraph (2).\n**(2) Award amount**\n**(A) In general**\nThe court shall award to the plaintiff threefold the damages sustained by the plaintiff and the reasonable cost of litigation, including a reasonable attorney fee.\n**(B) Interest on damages**\nPursuant to a motion by the plaintiff promptly made, the court may award simple interest on actual damages sustained by the plaintiff for the period beginning on the date of service of the pleading of the plaintiff setting forth a claim under this Act and ending on the date of judgment, or for any shorter period therein.\n**(3) Invalidity of pre-dispute arbitration agreements and pre-dispute joint action waivers**\nAt the election of the plaintiff in an action authorized under paragraph (1), a pre-dispute arbitration agreement or pre-dispute joint action waiver relating to a violation of this Act shall be invalid or unenforceable.\n#### 5. Relationship to Federal antitrust laws\nNothing in this Act, or any amendment made by this Act, shall be construed to modify, impair, or supersede the operation of any of the antitrust laws\n#### 6. Relationship to State and local laws\nNothing in this Act may be construed to preempt any State, Tribal, city, or local law, regulation, or ordinance that supplements this Act.\n#### 7. Severability\nIf any provision of this Act, or the application of such a provision to any person or circumstance, is held to be unconstitutional, the remaining provisions of this Act, and the application of such provisions to any person or circumstance shall not be affected thereby.",
      "versionDate": "2025-03-03",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-05-09T18:16:40Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1788ih.xml"
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
      "title": "Fair Grocery Pricing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Grocery Pricing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of algorithmic systems by food producers to artificially inflate the price or reduce the supply of their foods.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:28Z"
    }
  ]
}
```
