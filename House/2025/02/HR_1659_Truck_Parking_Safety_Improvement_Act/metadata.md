# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1659?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1659
- Title: Truck Parking Safety Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 1659
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-04-07T08:05:47Z
- Update date including text: 2026-04-07T08:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-27 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-27 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1659",
    "number": "1659",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001295",
        "district": "12",
        "firstName": "Mike",
        "fullName": "Rep. Bost, Mike [R-IL-12]",
        "lastName": "Bost",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Truck Parking Safety Improvement Act",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:47Z",
    "updateDateIncludingText": "2026-04-07T08:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-27T23:03:14Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IN"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "WI"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MO"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "PA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MI"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "KS"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MS"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NV"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NH"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IN"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "WI"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "RI"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CO"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IN"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "TN"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "WI"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "AL"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "LA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "FL"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NC"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "MS"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "UT"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "OH"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "VA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "IL"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MI"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "SD"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "FL"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "OH"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NJ"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CO"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "VA"
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
      "sponsorshipDate": "2025-09-08",
      "state": "AR"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NM"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "TX"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "MO"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NY"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "PA"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1659ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1659\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Bost (for himself, Ms. Craig , Mr. Stauber , Mr. Carbajal , Mr. Mrvan , Mrs. Kim , Mr. Steil , Mr. Nehls , Mr. Cleaver , Mr. Meuser , Ms. Scholten , Mr. Swalwell , Ms. Brownley , Mr. LaHood , Mr. Mann , Mr. Guest , Ms. Titus , Mr. Pappas , Mr. Davis of North Carolina , Mr. Yakym , Mr. Van Orden , Mr. Finstad , Mr. Magaziner , Mr. Hurd of Colorado , Mrs. Houchin , Ms. Ross , and Mr. Cuellar ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to establish a competitive grant program for projects for commercial motor vehicle parking, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Truck Parking Safety Improvement Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that it should be a national priority to address the shortage of parking for commercial motor vehicles on the Federal-aid highway system to improve highway safety.\n#### 3. Parking for commercial motor vehicles\n##### (a) In general\nChapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Parking for commercial motor vehicles (a) Definitions In this section: (1) Commercial motor vehicle The term commercial motor vehicle has the meaning given the term in section 31132 of title 49. (2) Safety rest area The term safety rest area has the meaning given the term in section 120(c)(1). (b) Grant authority Subject to the availability of funds, the Secretary shall make grants, on a competitive basis, to eligible entities for projects to provide public parking for commercial motor vehicles and improve the safety of commercial motor vehicle drivers. (c) Eligible entities (1) In general An entity eligible to receive a grant under this section is any of the following: (A) A State. (B) A metropolitan planning organization. (C) A unit of local government. (D) A political subdivision of a State or local government carrying out responsibilities relating to commercial motor vehicle parking. (E) A Tribal government or a consortium of Tribal governments. (F) A multistate or multijurisdictional group of entities described in subparagraphs (A) through (E). (2) Private sector participation An eligible entity that receives a grant under this section may partner with a private entity to carry out an eligible project under this section. (d) Eligible projects (1) In general An entity may use a grant provided under this section for a project described in paragraph (2) that is on\u2014 (A) a Federal-aid highway; or (B) a facility with reasonable access (as described in section 658.19 of title 23, Code of Federal Regulations (or a successor regulation)) to\u2014 (i) a Federal-aid highway; or (ii) a freight facility. (2) Projects described A project referred to in paragraph (1) is a project\u2014 (A) to construct a safety rest area that includes parking for commercial motor vehicles; (B) to construct additional commercial motor vehicle parking capacity\u2014 (i) adjacent to a private commercial truck stop or travel plaza; (ii) within the boundaries of, or adjacent to, a publicly owned freight facility, including a port terminal operated by a public authority; (iii) at an existing facility, including an inspection or weigh station and a park-and-ride location; or (iv) at another suitable facility, as determined by the eligible entity, in concurrence with the Secretary; (C) to reopen an existing weigh station, safety rest area, park-and-ride facility, or other government-owned facility, that is not in use, for commercial motor vehicle parking; (D) to construct or make capital improvements to an existing public commercial motor vehicle parking facility to expand parking use and availability, including at a seasonal facility; (E) to identify, promote, and manage the availability of publicly and privately provided commercial motor vehicle parking, such as through the use of intelligent transportation systems; (F) to improve the personal safety of commercial motor vehicle drivers at a parking facility as part of a project described in subparagraphs (A) through (D); or (G) to improve a parking facility, including through truck stop electrification systems, as part of a project described in subparagraphs (A) through (D). (e) Application To be eligible to receive a grant under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including\u2014 (1) a description of the proposed project; and (2) any other information that the Secretary determines to be necessary. (f) Selection criteria The Secretary may select a project to receive a grant under this section only if the Secretary determines that\u2014 (1) there is a shortage of commercial motor vehicle parking capacity in the corridor in which the project is located; (2) the eligible entity has consulted with motor carriers, commercial motor vehicle drivers, public safety officials, and private providers of commercial motor vehicle parking regarding the project; (3) the project will likely\u2014 (A) increase the availability or utilization of commercial motor vehicle parking; (B) facilitate the efficient movement of freight; or (C) improve highway safety, traffic congestion, and air quality; and (4) the eligible entity demonstrates the ability to provide for the maintenance and operation of the facility. (g) Additional consideration To the maximum extent practicable, the Secretary shall select projects to receive grants under the program in a manner that maximizes the geographic dispersion of new commercial motor vehicle parking capacity across the United States. (h) Use of funds (1) In general An eligible entity may use a grant under this section for\u2014 (A) development phase activities, including planning, feasibility analysis, benefit-cost analysis, environmental review, preliminary engineering and design work, and other preconstruction activities necessary to advance a project under this section; and (B) construction and operational improvements. (2) Limitations (A) In general An eligible entity may use not more than 25 percent of the amount of a grant under this section for activities described in paragraph (1)(A). (B) Existing facilities (i) In general Except as provided in clause (ii), not more than 10 percent of the amounts made available for each fiscal year for grants under this section may be used for projects described in subsection (d)(2)(E) that solely identify, promote, and manage the availability of existing commercial motor vehicle parking. (ii) Exception Clause (i) shall not apply to a project described in subsection (d)(2)(E) that is part of a project to expand commercial motor vehicle parking capacity. (3) Prohibition (A) In general Amounts made available to carry out this section shall not be used for the construction, or development phase activities that would enable the construction, of charging or fueling infrastructure for the propulsion of a vehicle, including a commercial motor vehicle. (B) Savings provision Nothing in this paragraph limits the use of funds other than funds made available to carry out this section. (i) Requirements (1) Publicly accessible parking Commercial motor vehicle parking constructed, opened, or improved with funds from a grant under this section shall be open and accessible to all commercial motor vehicle drivers. (2) Prohibition on charging fees (A) In general No fee may be charged by an eligible entity to a commercial motor vehicle driver to gain access to parking constructed, opened, maintained, or improved with a grant under this section. (j) Treatment of projects Notwithstanding any other provision of law, a project carried out under this section shall be treated as a project on a Federal-aid highway under this chapter. (k) Period of availability of funds Amounts made available for projects under this section shall remain available for a period of 3 years after the last day of the fiscal year in which the amounts are made available. .\n##### (b) Clerical amendment\nThe analysis for chapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Parking for commercial motor vehicles. .\n#### 4. Survey and comparative assessment\n##### (a) In general\nNot later than 4 years after the date of enactment of this Act, and every 2 years thereafter, the Secretary of Transportation, in consultation with appropriate State motor carrier safety personnel, motor carriers, State departments of transportation, and private providers of commercial motor vehicle parking, shall submit to the Committee on Environment and Public Works of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report that\u2014\n**(1)**\nevaluates the availability of adequate parking and rest facilities, taking into account both private and public facilities, for commercial motor vehicles engaged in interstate transportation;\n**(2)**\nevaluates the effectiveness of the projects funded under section 180 of title 23, United States Code, in improving access to commercial motor vehicle parking;\n**(3)**\nevaluates the ability of eligible entities that received a grant under section 180 of title 23, United States Code, to sustain the operation of parking facilities constructed with funds provided under that section; and\n**(4)**\nreports on the progress being made to provide adequate commercial motor vehicle parking facilities.\n##### (b) Results\nThe Secretary of Transportation shall make the reports under subsection (a) available to the public on the website of the Department of Transportation.\n##### (c) Alignment of reports\nIn carrying out this section, the Secretary of Transportation shall\u2014\n**(1)**\nconsider the results of the commercial motor vehicle parking facilities assessments of States under subsection (f) of section 70202 of title 49, United States Code; and\n**(2)**\nseek to align the contents of the reports under subsection (a) and the submission and publication of those reports with the State freight plans developed and updated under that section.\n#### 5. Authorization of appropriations\nThere are authorized to be appropriated to the Secretary of Transportation for projects for commercial motor vehicle parking under section 180 of title 23, United States Code, $151,000,000 for each of fiscal years 2025 through 2029.",
      "versionDate": "2025-02-27",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-18T16:20:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1659",
          "measure-number": "1659",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-04-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1659v00",
            "update-date": "2025-04-22"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Truck Parking Safety Improvement Act</strong></p><p>This bill directs the Department of Transportation (DOT) to provide competitive grants for projects that provide public parking for commercial motor vehicles and improve the safety of commercial motor vehicle drivers. States, metropolitan planning organizations, tribal governments, and local governments are eligible for these grants.</p><p>The grants must be used for projects on federal-aid highways or a facility with reasonable access to such a highway or a freight facility.</p><p>A grant recipient may not charge a fee to a commercial motor vehicle driver to access a public parking facility that is constructed, opened, maintained, or improved with a grant under this program.</p><p>In providing grants, DOT must determine that</p><ul><li>there is a shortage of commercial motor vehicle parking capacity in the project's corridor;</li><li>the eligible entity has consulted motor carriers, commercial motor vehicle drivers, public safety officials, and private providers of commercial motor vehicle parking regarding the project;</li><li>the project will likely increase the availability or utilization of commercial motor vehicle parking, facilitate the efficient movement of freight, or improve highway safety, traffic congestion, and air quality; and</li><li>the eligible entity has demonstrated the ability to provide for the facility's maintenance and operation.</li></ul><p>To the maximum extent practicable, DOT must select grant projects that maximize the geographic dispersion of new commercial motor vehicle parking capacity across the United States.</p>"
        },
        "title": "Truck Parking Safety Improvement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1659.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Truck Parking Safety Improvement Act</strong></p><p>This bill directs the Department of Transportation (DOT) to provide competitive grants for projects that provide public parking for commercial motor vehicles and improve the safety of commercial motor vehicle drivers. States, metropolitan planning organizations, tribal governments, and local governments are eligible for these grants.</p><p>The grants must be used for projects on federal-aid highways or a facility with reasonable access to such a highway or a freight facility.</p><p>A grant recipient may not charge a fee to a commercial motor vehicle driver to access a public parking facility that is constructed, opened, maintained, or improved with a grant under this program.</p><p>In providing grants, DOT must determine that</p><ul><li>there is a shortage of commercial motor vehicle parking capacity in the project's corridor;</li><li>the eligible entity has consulted motor carriers, commercial motor vehicle drivers, public safety officials, and private providers of commercial motor vehicle parking regarding the project;</li><li>the project will likely increase the availability or utilization of commercial motor vehicle parking, facilitate the efficient movement of freight, or improve highway safety, traffic congestion, and air quality; and</li><li>the eligible entity has demonstrated the ability to provide for the facility's maintenance and operation.</li></ul><p>To the maximum extent practicable, DOT must select grant projects that maximize the geographic dispersion of new commercial motor vehicle parking capacity across the United States.</p>",
      "updateDate": "2025-04-22",
      "versionCode": "id119hr1659"
    },
    "title": "Truck Parking Safety Improvement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Truck Parking Safety Improvement Act</strong></p><p>This bill directs the Department of Transportation (DOT) to provide competitive grants for projects that provide public parking for commercial motor vehicles and improve the safety of commercial motor vehicle drivers. States, metropolitan planning organizations, tribal governments, and local governments are eligible for these grants.</p><p>The grants must be used for projects on federal-aid highways or a facility with reasonable access to such a highway or a freight facility.</p><p>A grant recipient may not charge a fee to a commercial motor vehicle driver to access a public parking facility that is constructed, opened, maintained, or improved with a grant under this program.</p><p>In providing grants, DOT must determine that</p><ul><li>there is a shortage of commercial motor vehicle parking capacity in the project's corridor;</li><li>the eligible entity has consulted motor carriers, commercial motor vehicle drivers, public safety officials, and private providers of commercial motor vehicle parking regarding the project;</li><li>the project will likely increase the availability or utilization of commercial motor vehicle parking, facilitate the efficient movement of freight, or improve highway safety, traffic congestion, and air quality; and</li><li>the eligible entity has demonstrated the ability to provide for the facility's maintenance and operation.</li></ul><p>To the maximum extent practicable, DOT must select grant projects that maximize the geographic dispersion of new commercial motor vehicle parking capacity across the United States.</p>",
      "updateDate": "2025-04-22",
      "versionCode": "id119hr1659"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1659ih.xml"
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
      "title": "Truck Parking Safety Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:14:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Truck Parking Safety Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to establish a competitive grant program for projects for commercial motor vehicle parking, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T04:33:30Z"
    }
  ]
}
```
