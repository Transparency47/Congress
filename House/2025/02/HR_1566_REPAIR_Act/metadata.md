# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1566?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1566
- Title: REPAIR Act
- Congress: 119
- Bill type: HR
- Bill number: 1566
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2026-05-27T08:05:51Z
- Update date including text: 2026-05-27T08:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-25 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-25 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1566",
    "number": "1566",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "D000628",
        "district": "2",
        "firstName": "Neal",
        "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
        "lastName": "Dunn",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "REPAIR Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:51Z",
    "updateDateIncludingText": "2026-05-27T08:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-10T20:43:30Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-10T20:42:08Z",
                "name": "Markup by"
              },
              {
                "date": "2025-02-25T20:41:24Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "WA"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "OH"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TN"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "IA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "OH"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NV"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CO"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-25",
      "state": "DC"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TN"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "WI"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "OR"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "PA"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "WA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "NY"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "VA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "TX"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "IL"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "WA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NV"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "MT"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "VA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "MI"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "sponsorshipWithdrawnDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "NC"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "CO"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NV"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "AR"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "ME"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "TX"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Walberg",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "MI"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "AZ"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "WI"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NH"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "AZ"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1566ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1566\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mr. Dunn of Florida (for himself, Ms. Perez , Mr. Davidson , Mr. Boyle of Pennsylvania , Mrs. Harshbarger , Mr. Tonko , Mr. Nunn of Iowa , Mr. Mullin , Mr. Thompson of Pennsylvania , Mr. Landsman , Mr. Amodei of Nevada , Ms. Pettersen , Mr. Bost , Ms. Norton , Mr. Rose , and Mr. Khanna ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo ensure consumers have access to data relating to motor vehicles of the consumers and critical repair information and tools for such motor vehicles, to provide such consumers with choices for the maintenance, service, and repair of such vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Right to Equitable and Professional Auto Industry Repair Act or the REPAIR Act .\n#### 2. Maintaining competition and data privacy after consumers purchase motor vehicles\n##### (a) In general\n**(1) Prohibition on motor vehicle manufacturers withholding vehicle-generated data, critical repair information, and tools**\nA motor vehicle manufacturer may not employ any technological barrier or specified legal barrier that impairs the ability of\u2014\n**(A)**\na motor vehicle owner (or a designee of a motor vehicle owner) to access vehicle-generated data pursuant to paragraph (2);\n**(B)**\na motor vehicle owner (or a designee of a motor vehicle owner), an aftermarket parts manufacturer, a diagnostic tool manufacturer, a manufacturer of motor vehicle equipment, an aftermarket parts remanufacturer, or a motor vehicle repair facility (or a distributor or service provider of a motor vehicle repair facility) to access critical repair information and tools;\n**(C)**\na motor vehicle owner (or a designee of a motor vehicle owner) to use a motor vehicle towing or service provider chosen by such owner (or such designee);\n**(D)**\nan aftermarket parts manufacturer, a motor vehicle equipment manufacturer, an aftermarket parts remanufacturer, or a motor vehicle repair facility (or a distributor or service provider of a motor vehicle repair facility) to produce or offer compatible aftermarket parts; or\n**(E)**\na motor vehicle owner (or a designee of a motor vehicle owner) to diagnose, repair, and maintain a motor vehicle in the same manner as any motor vehicle manufacturer or motor vehicle dealer.\n**(2) Requirement to provide vehicle-generated data to motor vehicle owners**\nA motor vehicle manufacturer shall\u2014\n**(A)**\nprovide for a motor vehicle owner (or a designee of a motor vehicle owner), without restriction or limitation, in or at the same manner, time, method, cost (less discounts and rebates), data content set, and subject to the same cryptographic or technological protections as any motor vehicle manufacturer, motor vehicle dealer, authorized motor vehicle service provider, or any other third party to whom such manufacturer provides vehicle-generated data, to have access to vehicle-generated data\u2014\n**(i)**\nthrough and including the interface ports of the motor vehicle (including OBD port and J\u20131939); and\n**(ii)**\nto the extent such vehicle is equipped for wireless transmission of such data, over wireless technology via any telematics system; and\n**(B)**\nmake available to motor vehicle owners (or designees of motor vehicle owners), aftermarket parts manufacturers, aftermarket parts remanufacturers, diagnostic tool manufacturers, and motor vehicle repair facilities (and the distributors and service providers of such facilities) without restriction or limitation, in or at the same manner, time, method, cost (less discounts and rebates), data content set, and subject to the same cryptographic or technological protections, as any motor vehicle manufacturer, motor vehicle dealer, authorized motor vehicle service provider, or any other third party to whom such manufacturer provides vehicle-generated data, any critical repair information and tools related to the motor vehicles such manufacturer manufactures.\n**(3) Prohibition on certain mandates related to repairs**\nExcept for recall and warranty repairs, repair or maintenance service procedures, recommendations, service bulletins, repair manuals, position statements, or other similar repair or maintenance guides that are distributed to consumers or to professional repairers, a motor vehicle manufacturer may not\u2014\n**(A)**\nmandate or imply a mandate to use any particular brand or manufacturer of parts, tools, or motor vehicle equipment; or\n**(B)**\nrecommend the use of any particular brand or manufacturer of parts, tools, or motor vehicle equipment without a prominent notice immediately following the recommendation, in the same font as the recommendation and in a font size no smaller than the font size used in the recommendation, stating that: Vehicle owners can choose which repair parts, tools, and motor vehicle equipment to purchase and should carefully consider their options. .\n**(4) Prohibition on certain limitations**\nMotor vehicle manufacturers may not limit the number or types of persons who a motor vehicle owner may designate as simultaneous designees under this subsection.\n**(5) Limitation**\nA motor vehicle manufacturer, including any affiliate of such manufacturer and any person working on behalf of such manufacturer, may not be considered or treated in the same way as the motor vehicle owner (or a designee of the motor vehicle owner) for any purpose, except for inclusion in notifications of persistent access to vehicle-generated data.\n**(6) Rules of construction**\nNothing in this Act may be construed to\u2014\n**(A)**\nlimit or expand any law or right relating to intellectual property;\n**(B)**\nrequire a motor vehicle manufacturer to divulge any trade secret (as defined in section 1839 of title 18, United States Code) that is not made available to motor vehicle owners (or designees of motor vehicle owners), aftermarket parts manufacturers, aftermarket parts remanufacturers, diagnostic tool manufacturers, and motor vehicle repair facilities (and the distributors and service providers of such facilities) pursuant to paragraph (2)(B); or\n**(C)**\npreclude a motor vehicle manufacturer from employing cryptographic or technological protections necessary to secure vehicle-generated data, safety critical vehicle systems, and motor vehicles.\n**(7) Requirements for persons receiving vehicle-generated data**\n**(A) Revocation of designation**\nA motor vehicle owner may revoke the designation of a designee of such owner in the same manner that such designee is designated and without any unreasonable or deceptive burden or barrier on such owner.\n**(B) Request to delete data**\nExcept as provided in subparagraph (D), a person who accesses vehicle-generated data shall delete such data not later than 72 hours after the relevant motor vehicle owner requests (digitally or in writing) the person to do so, with the exception of such data that is necessary to retain for motor vehicle maintenance record-keeping, accounting, and safety purposes.\n**(C) Use of data**\nExcept as provided in subparagraph (D), a person who accesses or stores vehicle-generated data\u2014\n**(i)**\nmay not use such data for any purpose unrelated to the diagnostics, repair, service, wear, and calibration or recalibration of parts and systems of the motor vehicle as such services are requested by the motor vehicle owner; and\n**(ii)**\nmay not sell, license, or transfer such data to any other person, except as requested or consented to by the motor vehicle owner for the purpose of diagnostics, repair, service, wear, and calibration or recalibration of parts and systems of the motor vehicle.\n**(D) Research and development exception**\n**(i) Research and development**\nNotwithstanding subparagraphs (B) and (C), a manufacturer of motor vehicles, parts, or tools may use and retain vehicle-generated data in a de-identified form for purposes of research and development related to the manufacture or service of such motor vehicles, parts, or tools.\n**(ii) Data in a de-identified form defined**\nIn this paragraph, the term data in a de-identified form means information that does not identify and is not linked or reasonably linkable to a distinct individual or motor vehicle, regardless of whether the information is aggregated, and with respect to which the manufacturer of the motor vehicle, parts, or tools\u2014\n**(I)**\ntakes reasonable technical measures to ensure that the information cannot, at any point, be used to re-identify an individual or device that identifies or is linked or reasonably linkable to an individual;\n**(II)**\npublicly commits in a clear and conspicuous manner\u2014\n**(aa)**\nto process and transfer the information solely in a de-identified form without any reasonable means for re-identification; and\n**(bb)**\nto not attempt to re-identify the information with any individual or any device that identifies or is linked or reasonably linkable to an individual; and\n**(III)**\ncontractually obligates any person or entity who receives the information from such manufacturer\u2014\n**(aa)**\nto comply with each provision of this clause with respect to the information; and\n**(bb)**\nto require that such obligation is included contractually in any subsequent instance in which the information may be received by such person or entity.\n##### (b) Nullification of attempts To restrict competition and consumer rights\nAny provision in a contract executed on or after the date of the enactment of this Act by or on behalf of a motor vehicle manufacturer that purports to violate subsection (a) shall be null and void to the extent that such provision would allow the motor vehicle manufacturer to avoid the prohibitions and requirements described in subsection (a).\n#### 3. Fair Competition After Vehicles Are Sold Advisory Committee\n##### (a) Establishment\nNot later than 90 days after the date of the enactment of this Act, the Commission shall establish an advisory committee to be known as the Fair Competition After Vehicles Are Sold Advisory Committee (in this section referred to as the Advisory Committee ).\n##### (b) Chair\nThe Chair of the Commission (or a designee of the Chair) shall serve as the head of the Advisory Committee.\n##### (c) Membership\nThe Advisory Committee shall be composed of the following members:\n**(1)**\nThe Director of the Bureau of Competition (or a designee of the Director).\n**(2)**\nThe Administrator of the National Highway Traffic Safety Administration (or a designee of the Administrator).\n**(3)**\n11 individuals, appointed by the Chair of the Commission, to be comprised of 1 individual from each of the following:\n**(A)**\nIndependent motor vehicle repair facilities.\n**(B)**\nMotor vehicle parts retailers.\n**(C)**\nMotor vehicle parts distributors.\n**(D)**\nOriginal motor vehicle equipment parts manufacturers.\n**(E)**\nAftermarket parts manufacturers.\n**(F)**\nAftermarket tools manufacturers.\n**(G)**\nMotor vehicle manufacturers.\n**(H)**\nMotor vehicle dealership service centers.\n**(I)**\nConsumer rights organizations.\n**(J)**\nAutomobile insurers.\n**(K)**\nTrucking companies.\n##### (d) Function\nThe Advisory Committee shall provide recommendations to the Commission on\u2014\n**(1)**\nthe implementation of this Act;\n**(2)**\ncompetition issues after motor vehicles are sold, including such issues facing the motor vehicle repair industry (especially existing and emerging barriers related to motor vehicle repair); and\n**(3)**\nhow to ensure motor vehicle owners maintain control over the vehicle-generated data of the motor vehicles of such owners.\n##### (e) Duties\nIn carrying out the function described in subsection (c), the Advisory Committee shall\u2014\n**(1)**\nfoster industry collaboration in a clear and transparent manner;\n**(2)**\ncoordinate with and include participation by the private sector, including representatives of\u2014\n**(A)**\nindependent motor vehicle repair facilities;\n**(B)**\nmotor vehicle parts retailers;\n**(C)**\nmotor vehicle parts distributors;\n**(D)**\noriginal motor vehicle equipment parts manufacturers;\n**(E)**\naftermarket parts manufacturers;\n**(F)**\naftermarket tools manufacturers;\n**(G)**\nmotor vehicle manufacturers;\n**(H)**\nmotor vehicle dealership service centers;\n**(I)**\nconsumer rights organizations;\n**(J)**\nautomobile insurers;\n**(K)**\ntrucking companies;\n**(L)**\nmembers of the public; and\n**(M)**\nother interested parties; and\n**(3)**\nassess existing and emerging barriers to competitive motor vehicle repair.\n##### (f) Meetings\nThe Advisory Committee shall meet not fewer than 3 times per year at the call of the head.\n##### (g) Reports\n**(1) Contents**\nOn at least an annual basis, the Advisory Committee shall issue a report to the Commission that includes\u2014\n**(A)**\na description of efforts by the industries represented within the Advisory Committee to comply with this Act; and\n**(B)**\nan assessment of existing and emerging barriers to motor vehicle repair and control of motor vehicle owners over the vehicle-generated data of the motor vehicles of such owners, including whether additional types of data should be included in the definition of vehicle-generated data.\n**(2) Submission**\nNot later than 30 days after the date on which the Commission receives a report issued pursuant to paragraph (1), the Commission shall submit a copy of the report to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate.\n##### (h) Termination\n**(1) Process**\nThe Advisory Committee shall terminate upon an agreement of a majority of the membership.\n**(2) Notice**\nNot later than 30 days prior to the date on which the Advisory Committee terminates, the Advisory Committee shall provide notice of and a basis for the termination to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate.\n#### 4. Rulemaking\nNot later than 180 days after the date of the enactment of this Act, the National Highway Traffic Safety Administration, in consultation with the Commission, shall promulgate, under section 553 of title 5, United States Code, regulations to require motor vehicle manufacturers and motor vehicle dealers to inform motor vehicle owners about the rights of such owners under this Act at the point of purchase of a motor vehicle.\n#### 5. Enforcement by Federal Trade Commission\n##### (a) Unfair or deceptive acts or practices\nA violation of this Act or a regulation promulgated under this Act shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n##### (b) Powers of Commission\nThe Commission shall enforce this Act and any regulation promulgated under this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act, and any person who violates this Act or a regulation promulgated under this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (c) Complaint process\n**(1) Filing by complainant**\nAny person alleging any action taken or refused to be taken by any party subject to this Act in violation of this Act may file a complaint with the Commission briefly stating the facts of such allegation.\n**(2) Notification and response**\nUpon receiving a complaint filed pursuant to paragraph (1), the Commission shall forward the complaint to the party named in the complaint and request that such party answer such complaint in writing within a reasonable time determined by the Commission.\n**(3) Further action**\n**(A) Relief of liability**\nIf the party named in the complaint ceases the conduct alleged in such complaint and otherwise makes reparation for any harm or injury alleged to have been caused within the time determined pursuant to paragraph (2), the party shall be relieved of liability to the complainant only for such allegation.\n**(B) Additional investigation**\nIf the party named in the complaint does not satisfy the complaint as described in subparagraph (A) within the time determined pursuant to paragraph (2) or if there is any reasonable ground for continuing to investigate such complaint, the Commission shall investigate the allegation described in such complaint in such manner and by such means as the Commission determines proper.\n**(C) Clarification**\nA complaint may not be dismissed because of the absence of direct damage to the complainant.\n**(4) Orders by Commission**\n**(A) Deadline**\nThe Commission, with respect to any investigation of a complaint filed pursuant to paragraph (1), shall issue an order concluding such investigation not later 5 months after the date on which the complaint was filed.\n**(B) Appellate process**\nAny order concluding an investigation pursuant to subparagraph (A) shall be a final order and may be appealed to the United States District Court for the District Court of Columbia.\n#### 6. Definitions\nIn this Act:\n**(1) Aftermarket part**\n**(A) In general**\nThe term aftermarket part means any part offered for sale or for installation in or on a motor vehicle after such vehicle has left the production line of the motor vehicle manufacturer.\n**(B) Exclusions**\nSuch term does not include any original motor vehicle equipment or part manufactured for a motor vehicle manufacturer.\n**(2) Agency**\nThe term agency has the meaning given that term in section 551 of title 5, United States Code.\n**(3) Authorized motor vehicle service provider**\nThe term authorized motor vehicle service provider means a person who\u2014\n**(A)**\nhas an arrangement with a motor vehicle manufacturer under which the motor vehicle manufacturer grants to the individual or business a license to use a trade name, service mark, or other proprietary identifier for the purpose of offering the service of diagnosis, maintenance, or repair of a motor vehicle under the name of the motor vehicle manufacturer; or\n**(B)**\nhas another arrangement with the motor vehicle manufacturer to offer such services on behalf of the motor vehicle manufacturer.\n**(4) Automated driving system**\n**(A) In general**\nThe term automated driving system means the hardware and software that collectively are capable of performing the entire dynamic driving task on a sustained basis, regardless of whether such hardware and software are limited to a specific operational design domain.\n**(B) Inclusions**\nSuch term includes motor vehicles designed to be operated exclusively by a Level 4 or 5 automated driving system (as defined by the SAE International standard J3016, published on April 30, 2021, or subsequently adopted by the Secretary) for all trips.\n**(C) Exclusions**\nSuch term does not include motor vehicle components not specifically and solely related to a dynamic driving task.\n**(5) Barrier**\nThe term barrier means a restriction that prohibits, makes more difficult, or tends to make more difficult the ability of a person to exercise rights under this Act.\n**(6) Chair**\nThe term Chair means the Chair of the Commission.\n**(7) Commission**\nThe term Commission means the Federal Trade Commission.\n**(8) Critical repair information and tools**\nThe term critical repair information and tools means all of the technical and compatibility information, tools, equipment, wiring diagrams, parts nomenclature and descriptions, parts catalogs, repair procedures, training materials, software, and technology, including information related to diagnostics, repair, service, and calibration or recalibration of parts and systems, necessary to return a motor vehicle to operational specifications.\n**(9) Dynamic driving task**\n**(A) In general**\nThe term dynamic driving task means all of the real-time operational and tactical functions required to operate a motor vehicle in on-road traffic.\n**(B) Exclusions**\nSuch term does not include strategic functions, such as the scheduling of trips and the selection of destinations and waypoints.\n**(10) Insurer**\nThe term insurer has the meaning given that term in section 313(r) of title 31, United States Code.\n**(11) Motor vehicle**\n**(A) In general**\nThe term motor vehicle has the meaning\u2014\n**(i)**\ngiven that term in section 30102(a) of title 49, United States Code; and\n**(ii)**\ngiven the term trailer in section 390 of title 49, Code of Federal Regulations.\n**(B) Exclusion**\nSuch term does not include a vehicle equipped with an automated driving system.\n**(12) Motor vehicle dealer**\nThe term motor vehicle dealer means a dealer (as defined in section 30102(a) of title 49, United States Code) who has an agreement with a motor vehicle manufacturer related to the diagnostics, repair, or service of a motor vehicle.\n**(13) Motor vehicle equipment**\nThe term motor vehicle equipment has the meaning given that term in section 30102(a) of title 49, United States Code.\n**(14) Motor vehicle manufacturer**\nThe term motor vehicle manufacturer means an entity that manufactures a motor vehicle (as defined in section 30102(a) of title 49, United States Code).\n**(15) Motor vehicle owner**\n**(A) In general**\nThe term motor vehicle owner means a person with a present possessive ownership right in a motor vehicle.\n**(B) Exclusions**\nSuch term does not include\u2014\n**(i)**\na motor vehicle manufacturer; or\n**(ii)**\na person operating on behalf of\u2014\n**(I)**\na motor vehicle manufacturer;\n**(II)**\na motor vehicle financing company;\n**(III)**\na motor vehicle dealer; or\n**(IV)**\na motor vehicle lessor.\n**(16) Motor vehicle repair facility**\nThe term motor vehicle repair facility means any person who, in the ordinary course of business, is engaged in the business of diagnosis, service, maintenance, repair, or calibration or recalibration of motor vehicles or motor vehicle equipment.\n**(17) Person**\nThe term person means an individual, trust, estate, partnership, association, company, or corporation.\n**(18) Remanufacturer**\nThe term remanufacturer means a person who uses a standardized industrial process by which previously sold, worn, or non-functional products are returned to same-as-new (or better) condition and performance in a process that is in line with specific technical specifications (including engineering, quality, and testing standards) and yields fully warranted products.\n**(19) Service provider**\nThe term service provider means any designee of a motor vehicle owner or motor vehicle repair facility employed by such motor vehicle owner or motor vehicle repair facility to assist with the diagnosis and repair of a motor vehicle, including the diagnosis and repair of wireless and remote technologies or any other wireless and remote services comparable to such provided by a motor vehicle manufacturer.\n**(20) Specified legal barrier**\nThe term specified legal barrier means\u2014\n**(A)**\na request for a waiver of the right of a motor vehicle owner under this Act to use a motor vehicle repair facility of the choosing of such owner;\n**(B)**\na requirement for such a waiver as a condition for purchasing, leasing, operating, or obtaining warranty repairs for a motor vehicle; or\n**(C)**\nan offer for such owner to receive any compensation or other incentive for such a waiver.\n**(21) Technological barrier**\nThe term technological barrier means any technological restriction that prohibits, makes more difficult, or tends to make more difficult the ability of a person to exercise rights under this Act.\n**(22) Telematics system**\nThe term telematics system means any system in a motor vehicle that collects vehicle-generated data and transmits such data using wireless communications to a remote receiving point where such data is stored.\n**(23) Vehicle-generated data**\n**(A) In general**\nThe term vehicle-generated data means any direct, real-time, in-vehicle data generated, or generated and retained, by the operation of a motor vehicle related to diagnostics, repair, service, wear, and calibration or recalibration of parts and systems required to return such vehicle to operational specifications in compliance with Federal motor vehicle safety and emissions laws, regulations, and standards.\n**(B) Exclusions**\nThe term vehicle-generated data does not include\u2014\n**(i)**\ndiagnostics, repair, service, wear, and calibration or recalibration of parts and systems required to return an automated driving system to operational specifications; or\n**(ii)**\nany personally identifiable information.\n#### 7. Report to Congress\nNot later than 2 years after the date of the enactment of this Act, and every 2 years thereafter, the Commission shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report that includes\u2014\n**(1)**\na summary of investigations conducted and orders issued pursuant to section 5(c), including descriptions of unfair practices relating to repair and data access restrictions and a summary of best practices from stakeholders;\n**(2)**\nactions by the Commission to adapt to changes and advances in motor vehicle technology to maintain competition in the motor vehicle aftermarket and to ensure motor vehicle owners maintain control over the vehicle-generated data of the motor vehicles of such owners; and\n**(3)**\nany recommendations by the Commission for legislation that would improve the ability of the Commission and other relevant agencies to further protect consumers from unfair acts limiting competition in motor vehicle repair and strengthen consumer control over vehicle-generated data.\n#### 8. Relationship to State laws\nA State, or political subdivision of a State, may not maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of a law of the State, or political subdivision of the State, that is covered by any provision of this Act or any regulation promulgated pursuant to this Act.\n#### 9. Severability\nIf any provision of this Act, or the application thereof to any person or circumstance, is held invalid, the remainder of this Act, and the application of such provision to other persons not similarly situated or to other circumstances, shall not be affected by the invalidation.",
      "versionDate": "2025-02-25",
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
            "name": "Business records",
            "updateDate": "2026-02-23T16:19:58Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-02-23T16:19:44Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-02-23T16:19:37Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-02-23T16:21:05Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-02-23T16:20:07Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-02-23T16:22:04Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-02-23T16:22:10Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-02-23T16:17:26Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2026-02-23T16:20:40Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2026-02-23T16:20:22Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2026-02-23T16:17:33Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-02-23T16:19:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-03-25T18:46:29Z"
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1566ih.xml"
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
      "title": "REPAIR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T07:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REPAIR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T07:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Right to Equitable and Professional Auto Industry Repair Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T07:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure consumers have access to data relating to motor vehicles of the consumers and critical repair information and tools for such motor vehicles, to provide such consumers with choices for the maintenance, service, and repair of such vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T07:03:35Z"
    }
  ]
}
```
