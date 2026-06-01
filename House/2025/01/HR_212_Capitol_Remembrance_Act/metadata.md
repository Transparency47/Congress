# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/212?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/212
- Title: Capitol Remembrance Act
- Congress: 119
- Bill type: HR
- Bill number: 212
- Origin chamber: House
- Introduced date: 2025-01-06
- Update date: 2025-05-09T08:06:05Z
- Update date including text: 2025-05-09T08:06:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-06: Introduced in House
- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-01-06: Introduced in House

## Actions

- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-06",
    "latestAction": {
      "actionDate": "2025-01-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/212",
    "number": "212",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Capitol Remembrance Act",
    "type": "HR",
    "updateDate": "2025-05-09T08:06:05Z",
    "updateDateIncludingText": "2025-05-09T08:06:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-06",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-06",
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
          "date": "2025-01-06T17:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "WA"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "MS"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "A000371",
      "district": "33",
      "firstName": "Pete",
      "fullName": "Rep. Aguilar, Pete [D-CA-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Aguilar",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "NJ"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "NY"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "MI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "NV"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "NY"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "FL"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "TX"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "GA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
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
      "sponsorshipDate": "2025-01-07",
      "state": "GA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "DC"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "IL"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "CO"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "FL"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "OR"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CT"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
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
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray, Jr. [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "RI"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-18",
      "state": "IL"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr212ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 212\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 6, 2025 Mr. Crow (for himself, Mr. Correa , Ms. Jacobs , Ms. Jayapal , Mrs. Torres of California , Mr. Thompson of Mississippi , Ms. Chu , Mr. Aguilar , Mrs. Watson Coleman , Ms. Barrag\u00e1n , Mr. Gomez , Mr. Panetta , Ms. Meng , Mr. Tonko , Ms. Tlaib , Ms. Titus , Mr. Goldman of New York , Mr. Soto , Mr. Green of Texas , Mr. Bishop , and Mr. Huffman ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo direct the Architect of the Capitol to design and install in the United States Capitol an exhibit that depicts the attack on the Capitol that occurred on January 6, 2021, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Capitol Remembrance Act .\n#### 2. Exhibit depicting the attack on the Capitol\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Architect of the Capitol, in consultation with the Joint Committee on the Library, shall carry out a project to design and install in a prominent location in the United States Capitol a permanent exhibit that depicts the attack on the Capitol that occurred on January 6, 2021.\n##### (b) Exhibit requirements\n**(1) Inclusion of Capitol property**\nThe Architect shall, to the extent practicable, preserve property from the United States Capitol or the United States Capitol Grounds (as described in section 5102 of title 40, United States Code) that was damaged during the attack and include such property in the exhibit described in subsection (a) as the Architect determines appropriate.\n**(2) Photographic records**\nThe Architect shall include existing photographic records relating to the attack on the Capitol in the exhibit described in subsection (a) .\n**(3) Plaque**\nThe Architect shall include in the exhibit described in subsection (a) a plaque for the purpose of honoring\u2014\n**(A)**\nthe United States Capitol Police and other law enforcement agencies that participated in protecting the United States Capitol on January 6, 2021;\n**(B)**\nthe sacrifice of heroes, including United States Capitol Police Officers Brian Sicknick and Howard Liebengood, Metropolitan Police Department Officers Jeffrey Smith, Gunther Hashida, and Kyle DeFreytag, and those who sustained injuries as a result of protecting the United States Capitol on January 6, 2021; and\n**(C)**\nthe Capitol staff that helped restore the Capitol Complex after the attack.\n**(4) Artwork**\nThe Architect may include artwork created to depict the attack on the Capitol in the exhibit described in subsection (a) .\n##### (c) Authorization of appropriations\nThere are authorized to be appropriated such sums as are necessary to carry out this Act. Amounts appropriated pursuant to this subsection shall remain available until expended.",
      "versionDate": "2025-01-06",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Art, artists, authorship",
            "updateDate": "2025-02-05T16:14:11Z"
          },
          {
            "name": "Assault and harassment offenses",
            "updateDate": "2025-02-05T16:14:17Z"
          },
          {
            "name": "Civil disturbances",
            "updateDate": "2025-02-05T16:14:23Z"
          },
          {
            "name": "Congressional agencies",
            "updateDate": "2025-02-05T16:14:30Z"
          },
          {
            "name": "Congressional officers and employees",
            "updateDate": "2025-02-05T16:14:36Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-02-05T16:14:42Z"
          },
          {
            "name": "Crimes against property",
            "updateDate": "2025-02-05T16:14:49Z"
          },
          {
            "name": "District of Columbia",
            "updateDate": "2025-02-05T16:14:55Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-02-05T16:15:06Z"
          },
          {
            "name": "Historical and cultural resources",
            "updateDate": "2025-02-05T16:15:13Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-02-05T16:15:21Z"
          },
          {
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2025-02-05T16:15:27Z"
          },
          {
            "name": "Photography and imaging",
            "updateDate": "2025-02-05T16:15:33Z"
          },
          {
            "name": "Protest and dissent",
            "updateDate": "2025-02-05T16:15:39Z"
          },
          {
            "name": "Subversive activities",
            "updateDate": "2025-02-05T16:15:47Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2025-02-05T16:15:53Z"
          },
          {
            "name": "U.S. Capitol",
            "updateDate": "2025-02-05T16:16:00Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-02-05T16:16:08Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-02-05T16:16:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-31T14:21:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-06",
    "originChamber": "House",
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
          "measure-id": "id119hr212",
          "measure-number": "212",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-06",
          "originChamber": "HOUSE",
          "update-date": "2025-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr212v00",
            "update-date": "2025-02-10"
          },
          "action-date": "2025-01-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Capitol Remembrance Act</strong></p><p>This bill requires the Architect of the Capitol (AOC) to design and install in a prominent location in the U.S. Capitol a permanent exhibit that depicts the January 6, 2021, attack on the Capitol.</p><p>To the extent possible, the AOC must preserve property that was damaged during the attack and include it in the exhibit. The AOC must also include (1) existing photographic records relating to the attack; and (2) a plaque to honor the U.S. Capitol Police and other law enforcement agencies that protected the Capitol, the individuals who died or sustained injuries to protect the Capitol, and the staff who helped restore the Capitol complex after the attack.</p><p>The\u00a0exhibit shall be installed within two years after the bill's enactment.\u00a0</p>"
        },
        "title": "Capitol Remembrance Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr212.xml",
    "summary": {
      "actionDate": "2025-01-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Capitol Remembrance Act</strong></p><p>This bill requires the Architect of the Capitol (AOC) to design and install in a prominent location in the U.S. Capitol a permanent exhibit that depicts the January 6, 2021, attack on the Capitol.</p><p>To the extent possible, the AOC must preserve property that was damaged during the attack and include it in the exhibit. The AOC must also include (1) existing photographic records relating to the attack; and (2) a plaque to honor the U.S. Capitol Police and other law enforcement agencies that protected the Capitol, the individuals who died or sustained injuries to protect the Capitol, and the staff who helped restore the Capitol complex after the attack.</p><p>The\u00a0exhibit shall be installed within two years after the bill's enactment.\u00a0</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr212"
    },
    "title": "Capitol Remembrance Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Capitol Remembrance Act</strong></p><p>This bill requires the Architect of the Capitol (AOC) to design and install in a prominent location in the U.S. Capitol a permanent exhibit that depicts the January 6, 2021, attack on the Capitol.</p><p>To the extent possible, the AOC must preserve property that was damaged during the attack and include it in the exhibit. The AOC must also include (1) existing photographic records relating to the attack; and (2) a plaque to honor the U.S. Capitol Police and other law enforcement agencies that protected the Capitol, the individuals who died or sustained injuries to protect the Capitol, and the staff who helped restore the Capitol complex after the attack.</p><p>The\u00a0exhibit shall be installed within two years after the bill's enactment.\u00a0</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr212"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr212ih.xml"
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
      "title": "Capitol Remembrance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T12:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Capitol Remembrance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-29T12:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Architect of the Capitol to design and install in the United States Capitol an exhibit that depicts the attack on the Capitol that occurred on January 6, 2021, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-29T12:03:26Z"
    }
  ]
}
```
