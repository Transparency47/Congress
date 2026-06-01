# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2902?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2902
- Title: SOAR Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2902
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-05-27T08:05:37Z
- Update date including text: 2026-05-27T08:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2902",
    "number": "2902",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "V000129",
        "district": "22",
        "firstName": "David",
        "fullName": "Rep. Valadao, David G. [R-CA-22]",
        "lastName": "Valadao",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "SOAR Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:37Z",
    "updateDateIncludingText": "2026-05-27T08:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:11:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-10T13:11:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
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
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NE"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "CO"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "NM"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "FL"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "AZ"
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "HI"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NC"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "NY"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "WA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "PA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "LA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NJ"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "CA"
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
      "sponsorshipDate": "2025-05-29",
      "state": "VA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NC"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MI"
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
      "sponsorshipDate": "2025-09-02",
      "state": "DC"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "IL"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "WA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "OR"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "PA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NY"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "AL"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "MN"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "FL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "OH"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "MD"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "FL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CT"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MO"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "AL"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NC"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "UT"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "OR"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "UT"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "AL"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "SC"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "WA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NH"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "GA"
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
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "IN"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2902ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2902\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Valadao (for himself, Ms. Brownley , Mr. Smith of Nebraska , and Mr. Evans of Colorado ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to improve the payment method for oxygen and oxygen related equipment, supplies, and services, to increase beneficiary access to oxygen and oxygen related equipment, supplies, and services, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Supplemental Oxygen Access Reform Act of 2025 or the SOAR Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Protect beneficiary access to supplemental oxygen therapy in the home and community\nSec. 101. Reform of the medicare supplemental oxygen benefit.\nSec. 102. Establishment of supplemental oxygen responsibilities criteria.\nSec. 103. Technical corrections.\nTITLE II\u2014Protecting beneficiary access to respiratory therapists\nSec. 201. Reimbursement for respiratory therapists.\nTITLE III\u2014Adoption of electronic templates to strengthen fraud and abuse protections and ensure program integrity\nSec. 301. Strengthening program integrity through the use of electronic templates to document medical necessity, and restoring clinical inference for oxygen and oxygen related equipment, supplies, and services.\nSec. 302. Establishing notice requirements for individuals receiving oxygen or oxygen related equipment, supplies, or services.\nTITLE IV\u2014Establishment of beneficiary rights\nSec. 401. Establishing protections for individuals receiving oxygen or oxygen related equipment, supplies, or services.\nI\nProtect beneficiary access to supplemental oxygen therapy in the home and community\n#### 101. Reform of the medicare supplemental oxygen benefit\n##### (a) Removing oxygen and oxygen related equipment, supplies, and services from competitive acquisition program To improve patient access to supplemental oxygen therapy\nSection 1847(a)(3) of the Social Security Act ( 42 U.S.C. 1395w\u20133(a)(3) ) is amended by\u2014\n**(1)**\ninserting and exclusion after exception authority ;\n**(2)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and moving such clauses as so redesignated 2 ems to the right;\n**(3)**\nby striking In carrying out and inserting the following:\n(A) In general In carrying out ; and\n**(4)**\nby adding at the end the following new subparagraph:\n(B) Exclusion of oxygen, and oxygen related equipment, supplies, and services Beginning on or after January 1, 2026, the Secretary shall exclude oxygen and oxygen related equipment, supplies, and services from the competitive acquisition program under this section and payment for oxygen and oxygen related equipment, supplies, and services shall be made as prescribed under subparagraphs (E), (F), and (H) of section 1834(a)(9). .\n##### (b) Establishing adequate payment for oxygen and oxygen related equipment, supplies, and services\nSection 1834(a)(9) of the Social Security Act ( 42 U.S.C. 1395m(a)(9) ) is amended\u2014\n**(1)**\nin the first sentence of the matter preceding subparagraph (A), by inserting the following before the period: (for oxygen and oxygen equipment furnished before January 1, 2026) or the amount determined under subparagraph (E), subject to subparagraphs (F), (G), and (H) (for oxygen and oxygen related equipment, supplies, and services furnished on or after January 1, 2026); ; and\n**(2)**\nby adding at the end the following:\n(E) Payment for oxygen and oxygen related equipment, supplies, and services excluded from competitive acquisition program Subject to subparagraphs (F), (G), and (H) in the case of oxygen and oxygen related equipment, supplies, and services furnished on or after January 1, 2026\u2014 (i) in areas that are competitive bidding areas in which a competitive bidding program is implemented for other covered items, the payment amount is equal to\u2014 (I) for 2026, the fee schedule amounts for the area for items and services in effect on December 31, 2025; and (II) for each subsequent year, the amount determined under this clause for the preceding year, increased by the percentage increase in the consumer price index for all urban consumers (United States city average) for the 12-month period ending on December 31 of the previous year; (ii) in rural areas and non-contiguous areas (Alaska, Hawaii, and United States territories), the payment amount is equal to\u2014 (I) 50 percent of 110 percent of the national average price for the item or service determined under section 414.210(g)(1)(ii) of title 42, Code of Federal Regulations; and (II) 50 percent of\u2014 (aa) for 2026, the fee schedule amount for the area in effect on December 31, 2025; and (bb) for each subsequent year, the amount determined under this subclause for the preceding year, increased by the percentage increase in the consumer price index for all urban consumers (United States city average) for the 12-month period ending on December 31 of the previous year; and (iii) in areas other than those described in clauses (i) and (ii), the payment amount is equal to the sum of 75 percent of the adjusted payment amount established under clause (i) and 25 percent of the unadjusted fee schedule amount otherwise determined without taking into account this subparagraph. (F) Special rule for liquid oxygen (i) Payment (I) In general In lieu of the volume adjustment established under paragraph (5)(C), not later than January 1, 2026, the Secretary in consultation with suppliers, manufacturers, patients and patient advocates, and physicians, and through notice-and-comment rulemaking, shall establish a separate payment amount that meets the requirements of this subparagraph made to a supplier for the provision of liquid oxygen and liquid oxygen related equipment, supplies, and services that meets the requirements described in subparagraph (G). (II) Payment floor The payment amount established under subclause (I) may not be less than an amount equal to 200 percent of the 2015 Durable Medical Equipment, Prosthetics/Orthotics & Supplies Fee Schedule updated by the consumer price index for all urban consumers (United States city average) for years 2016 through 2025. (III) Update mechanism Beginning on January 1, 2027, the payment amount described in subclause (I) shall be increased annually by the projected percentage increase in the consumer price index for all urban consumers (United States city average) for the 12-month period ending December 31 of the previous year. (ii) Considerations In implementing the payment amount under this subparagraph, the Secretary shall take into account the cost of liquid oxygen on a per pound basis, the cost of liquid oxygen equipment, the infrastructure costs associated with providing liquid oxygen equipment and supplies (including labor, storage, transportation, maintenance, and similar costs), the cost of complying with Federal and State regulations specific to the delivery and transportation of liquid oxygen, and any other cost factors the Secretary deems appropriate after consulting with stakeholders such as suppliers, providers, patients and patient advocates, and manufacturers. (iii) Monthly add-on for high-flow patients (I) In general Subject to subclause (II), the Secretary shall establish a non-budget neutral add-on to the payment amount under clause (i) when the prescribing practitioner orders an oxygen flow rate equal to or greater than 6 liters per minute. (II) Add-on amount The add-on amount shall equal the per pound cost of the oxygen exceeding the amount required to provide a liter flow that is equal to or greater than 6 liters per minute. (iv) Periodic assessment of the base rate The Secretary shall assess at least once every 3 years the adequacy of the payment amounts under this subparagraph on a cost-related basis or other economical and equitable basis. (v) Transitional interim payment (I) In general For items and services furnished on or after the date of the enactment of the SOAR Act of 2025 and prior to the implementation of the payment amount established under this subparagraph, the Secretary shall adopt a transitional interim payment amount for liquid oxygen, and liquid oxygen equipment, supplies, and services in an amount equal to 200 percent of the 2015 Durable Medical Equipment, Prosthetics/Orthotics & Supplies Fee Schedule updated by the consumer price index for all urban consumers (United States city average) for years 2016 through 2025. (II) Update This amount shall be updated annually by the projected percentage change in the consumer price index for all urban consumers (United States city average) for the 12-month period ending on December 31 of the previous year, until the Secretary implements the payment amount under this subparagraph. (vi) Coverage criteria (I) In general Not later than January 1, 2026, the Secretary, in consultation with stakeholders, shall establish objective clinical criteria for the coverage of liquid oxygen, and liquid oxygen equipment, supplies, and services under this title. (II) Update of criteria The Secretary shall review and update the coverage standards under this clause every 5 years to ensure the standards take into consideration current medical and clinical guidelines and take into effect modality in order to maximize beneficiary independence. .\n#### 102. Establishment of supplemental oxygen responsibilities criteria\n##### (a) In general\nSection 1834(a)(9) of the Social Security Act ( 42 U.S.C. 1395m(a)(9) ), as amended by section 101(b), is further amended by inserting the following new subparagraph:\n(G) Oxygen and oxygen related equipment, supplies, and services In consultation with stakeholders, the Secretary shall define the scope of services a supplier of oxygen and oxygen related equipment, supplies, and services must provide to receive payment under this part, to include\u2014 (i) conducting an initial evaluation of the beneficiary using the uniform oxygen patient evaluation form described in paragraph (5)(G) to determine the appropriate use of oxygen and oxygen related equipment, supplies, and services by the beneficiary, including the use of portable equipment; (ii) ensuring the beneficiary has appropriate access to portable oxygen, and portable oxygen equipment, supplies, and services based on the mobility needs of the beneficiary, including the needs of the beneficiary outside the home of the beneficiary; (iii) providing written and verbal beneficiary and caregiver education regarding oxygen and oxygen related equipment, supplies, and services, stationary and portable options, and oxygen safety, which includes evaluating the environment of the beneficiary for safety risks or hazards, such as fire and fall hazards; (iv) providing appropriate delivery, set-up, and coordination of oxygen services (including the delivery of any oxygen equipment or supplies to a beneficiary prior to such beneficiary being discharged, delivering such equipment, and setting up the equipment), as needed, in a timely manner as agreed upon by the beneficiary or caregiver, supplier, and prescribing practitioner; (v) evaluating the ability of the beneficiary to operate the equipment safely and effectively; (vi) providing infection control information and instructions about all equipment and supplies; (vii) providing equipment-related services, including checking oxygen system purity levels and flow rates, changing and cleaning filters, and assuring the integrity of alarms and back-up systems, consistent with the manufacturer specifications and in accordance with all Federal, State, and local laws and regulations; (viii) monitoring visits when necessary by appropriate personnel, including a respiratory therapist to evaluate all aspects of the services being provided to the beneficiary by the provider; (ix) documenting exception reporting by the supplier to the prescribing physician when changes occur in the compliance of the beneficiary with the beneficiary's plan of care; (x) providing, as needed, continued education to the beneficiary or caregiver regarding appropriate oxygen equipment maintenance practices and performance; (xi) providing, as prescribed by the plan of care of the prescribing practitioner, appropriate oxygen and oxygen related equipment, supplies, and services (including supplemental supplies and emergency oxygen back-ups as appropriate); (xii) ensuring oxygen and oxygen equipment can be used appropriately outside the home of a beneficiary based on necessity; (xiii) providing 24-hour on-call coverage to respond to beneficiary needs relating to oxygen and oxygen related equipment, supplies, and services; and (xiv) assisting the beneficiary with the coordination of oxygen and oxygen related equipment, supplies, and services, including by assisting the beneficiary find a different supplier if the beneficiary temporarily travels outside of the service area of the supplier. If the beneficiary relocates permanently, the new supplier caring for the beneficiary will assume responsibility for billing the Medicare program directly. .\n##### (b) Effective date\nThe amendment made by this section shall take effect on the date that is 1 year after the date of enactment of this Act.\n#### 103. Technical corrections\nSection 1861(n) is amended by striking iron lungs, oxygen tents and inserting oxygen and oxygen related equipment, supplies, and services .\nII\nProtecting beneficiary access to respiratory therapists\n#### 201. Reimbursement for respiratory therapists\n##### (a) Protecting access to respiratory therapist services\n**(1) Adding respiratory therapist services to the definition of medical and other health services**\nSection 1861(s)(2) of the Social Security Act ( 42 U.S.C. 1395x(s)(2) ) is amended\u2014\n**(A)**\nin subparagraph (JJ), by inserting and after the semicolon; and\n**(B)**\nby adding at the end the following new subparagraph:\n(KK) respiratory therapist services (as defined in subsection (nnn)) furnished on or after January 1, 2026. .\n**(2) Definition of respiratory therapist services**\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended by adding at the end the following new subsection:\n(nnn) Respiratory therapist services The term respiratory therapist services means services performed by a respiratory therapist within the scope of practice of a respiratory therapist as defined by State law, regulations, and applicable accreditation standards for the assessment, treatment, and monitoring of patients requiring oxygen and oxygen related equipment, supplies, or services. .\n##### (b) Add-On payment adjustment\nSection 1834(a)(9) of the Social Security Act ( 42 U.S.C. 1395m(a)(9) ), as amended by sections 101(b) and 102(a), is further amended by adding at the end the following new subparagraph:\n(H) Monthly payment add-on adjustment for respiratory therapist services For respiratory therapist services furnished on or after January 1, 2026, the Secretary shall implement through notice and comment rulemaking and in consultation with stakeholders a non-budget neutral add-on payment adjustment to the payment amount established under this paragraph that reflects the cost of providing respiratory therapist services as clinically appropriate under State law. .\nIII\nAdoption of electronic templates to strengthen fraud and abuse protections and ensure program integrity\n#### 301. Strengthening program integrity through the use of electronic templates to document medical necessity, and restoring clinical inference for oxygen and oxygen related equipment, supplies, and services\n##### (a) Adopting electronic templates for determining medical necessity\nSection 1834(a)(5) of the Social Security Act ( 42 U.S.C. 1395m(a)(5) ) is amended by adding at the end the following:\n(G) Adoption of electronic templates to document medical necessity and strengthen program integrity (i) In general For any oxygen and oxygen related equipment, supplies, or service, including liquid oxygen, furnished on or after January 1, 2026, the Secretary shall adopt a template in an electronic format that meets the requirements of clause (ii) to be completed by the prescribing practitioner (as defined by the Secretary) that shall constitute the complete request for information to determine whether payment for such service, equipment, or supplies is covered by this title and is reasonable and necessary for the diagnosis or treatment of illness or injury (under section 1862(a)(1)(A)). (ii) Template requirements The template shall require the prescribing practitioner to provide each of the following: (I) Documentation that the beneficiary was seen by a prescribing practitioner within the appropriate timeframes for certification of the need for the services, equipment, or supplies. (II) Documentation of the qualifying blood gas or saturation test results. (III) Documentation indicating that the beneficiary needs or is using the appropriate equipment, supplies, and services. (IV) Any other documentation determined appropriate by the Secretary, except the Secretary shall not require the prescribing practitioner to provide medical record notes regarding the beneficiary. (iii) Contractor adjudication The Secretary shall require Medicare administrative contractors to adjudicate claims for payment for oxygen and oxygen related equipment, supplies, and services using electronic transactions. (H) Restoration of clinical inference and judgment For claims submitted on or after the date of enactment of this subparagraph with respect to the conduct of payment audits of suppliers of oxygen and oxygen related equipment, supplies, and services under this part the Secretary shall use clinical inference and clinical judgment in the evaluation of templates, medical records, and orders when conducting such audits in the same manner as the Secretary interpreted and applied such clinical judgment to claim reviews before 2009 pursuant to the Secretary\u2019s instruction to contractors. .\n#### 302. Establishing notice requirements for individuals receiving oxygen or oxygen related equipment, supplies, or services\n##### (a) Annual notice of cost-Sharing obligations for supplemental oxygen\nSection 1804 of the Social Security Act ( 42 U.S.C. 1395b\u20132 ) is amended by adding at the end the following new subsection:\n(e) The notice provided under subsection (a) shall include\u2014 (1) a description of\u2014 (A) the 36-month rental period for supplemental oxygen equipment under section 1834(a)(5)(F); (B) the right of a beneficiary to discuss their prescription for supplemental oxygen equipment with their prescribing physician or practitioner; and (C) any cost sharing requirements for supplemental oxygen equipment, supplies, and services under this title and the termination of such requirements when a beneficiary refuses or discontinues supplemental oxygen therapy; and (2) information on the internal and external grievance processes of suppliers of oxygen and oxygen related equipment, supplies, and services under this title (as well as how to contact Medicare through a hotline or beneficiary ombudsman), including the right of a beneficiary to file, personally or through a representative of the beneficiary's choosing, an internal or external grievance without retaliation or denial of services from a supplier. .\n##### (b) Timely notice of end of cost-Sharing obligations for supplemental oxygen\nSection 1834(a)(5)(F) of the Social Security Act ( 42 U.S.C. 1395m(a)(5)(F) ), is amended by adding at the end the following new clause:\n(iii) Timely notice of end of cost-sharing obligations for supplemental oxygen The Secretary, in consultation with patient advocates, physicians, supplemental oxygen suppliers, respiratory therapists, and other stakeholders, shall distribute a monthly notice to each individual receiving supplemental oxygen equipment, supplies, and services stating the number of months remaining within the rental cap period under this subparagraph during which the beneficiary is responsible for the copayment amount for such equipment. .\nIV\nEstablishment of beneficiary rights\n#### 401. Establishing protections for individuals receiving oxygen or oxygen related equipment, supplies, or services\nSection 1834(a)(5) of the Social Security Act ( 42 U.S.C. 1395m(a)(5) ), as amended by section 301, is further amended by adding at the end the following new subparagraph:\n(H) Establishing protections for individuals receiving oxygen or oxygen related equipment, supplies, or services The Secretary shall establish through regulation protections for any individual receiving oxygen or oxygen related equipment, supplies, or services under this part where such individual shall have the right to\u2014 (i) choose the local supplier of such services from among qualified suppliers and to change such supplier; (ii) receive communications from the supplier in a clear and understandable manner; (iii) ensure privacy and confidentiality in all aspects of treatment and the personal health information of such individual consistent with Federal and State laws; (iv) be informed by the supplier of such services regarding\u2014 (I) all aspects of the services being furnished by such supplier; (II) the right to refuse treatment and to discontinue treatment, including informing the individual's physician and indicating when individual cost-sharing requirements end; and (III) the right to refuse to participate in experimental research; (v) be informed by the supplier of policies and expectations of the supplier regarding patient conduct and responsibilities; (vi) be informed by the supplier about treatment modalities and categories of equipment relating to oxygen services for use by the individual and offered by the supplier; (vii) be informed by the supplier of the policies of such supplier regarding 24-hour on-call coverage; (viii) be informed by the supplier of the financial responsibilities of the individual with regard to such services, including the number of months remaining within the rental cap period under subparagraph (F) during which the patient is responsible for the copayment amount; (ix) be provided with the appropriate gaseous or liquid oxygen equipment, supplies, and services to ensure the mobility of the beneficiary, as well as the clinically appropriate amount of oxygen and oxygen related equipment, supplies, and services as agreed upon by the individual (or the individual\u2019s representative), the supplier, and the prescribing practitioner; (x) receive equipment that is maintained to the guidelines of the manufacturer; (xi) have broken or faulty equipment repaired or replaced in a timely manner; (xii) have oxygen or oxygen related equipment or supplies delivered by the supplier and to be contacted consistent with the requirements of section 410.38 of title 42, Code of Federal Regulations; (xiii) in the case of a supplier involuntary discharging an individual\u2014 (I) receive from such supplier a written notice that is provided to the individual no later than 30 days in advance of the involuntary discharge of the individual; and (II) have such supplier\u2014 (aa) follow established involuntary discharge procedures; or (bb) in the case of an immediate threat to the health and safety of others, follow an abbreviated involuntary discharge procedure; (xiv) be assisted by the supplier in obtaining the oxygen equipment and supplies prescribed by the treating physician of the individual when the individual is traveling; (xv) receive from the supplier oxygen supplies, refills, and emergency back-up equipment, as appropriate; (xvi) be informed of a plan by the supplier in case of a power outage or other natural emergency, so that the individual will continue to receive the necessary oxygen supplies and equipment; and (xvii) be informed by the supplier of\u2014 (I) any potential changes to the equipment, supplies, or services being furnished to the individual and the right to consult with the prescribing physician or practitioner regarding such changes to ensure they are appropriate and necessary and to be informed of the exceptions, as specified by the Secretary, when a supplemental oxygen services supplier may change the oxygen equipment of the individual; and (II) the internal and external grievance processes of the supplier (as well as how to contact Medicare through a hotline or beneficiary ombudsman), which shall include the right of an individual to file, personally or through a representative of the individual's choosing, an internal or external grievance without retaliation or denial of services from such supplier. .",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1406",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SOAR Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-05-09T14:26:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2902",
          "measure-number": "2902",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2025-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2902v00",
            "update-date": "2025-05-21"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supplemental Oxygen Access Reform Act of 2025\u00a0or the SOAR Act of 2025</strong></p><p>This bill establishes certain requirements with respect to the payment and provision of supplemental oxygen and related services under Medicare.</p><p>For example, the bill provides for separate payments, indexed to inflation, of oxygen and related equipment, supplies, and services under Medicare (rather than under the competitive acquisition program). It also specifically covers services that are provided by respiratory therapists under Medicare and provides for an additional payment adjustment for these services.</p><p>Additionally, the bill (1) requires the Centers for Medicare & Medicaid Services to develop an electronic template for providers to use when prescribing oxygen and related equipment, supplies, and services; and (2) establishes certain rights for beneficiaries receiving these items and services, such as the right to choose their suppliers and to receive clear communications and be informed about the services provided.</p>"
        },
        "title": "SOAR Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2902.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supplemental Oxygen Access Reform Act of 2025\u00a0or the SOAR Act of 2025</strong></p><p>This bill establishes certain requirements with respect to the payment and provision of supplemental oxygen and related services under Medicare.</p><p>For example, the bill provides for separate payments, indexed to inflation, of oxygen and related equipment, supplies, and services under Medicare (rather than under the competitive acquisition program). It also specifically covers services that are provided by respiratory therapists under Medicare and provides for an additional payment adjustment for these services.</p><p>Additionally, the bill (1) requires the Centers for Medicare & Medicaid Services to develop an electronic template for providers to use when prescribing oxygen and related equipment, supplies, and services; and (2) establishes certain rights for beneficiaries receiving these items and services, such as the right to choose their suppliers and to receive clear communications and be informed about the services provided.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119hr2902"
    },
    "title": "SOAR Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supplemental Oxygen Access Reform Act of 2025\u00a0or the SOAR Act of 2025</strong></p><p>This bill establishes certain requirements with respect to the payment and provision of supplemental oxygen and related services under Medicare.</p><p>For example, the bill provides for separate payments, indexed to inflation, of oxygen and related equipment, supplies, and services under Medicare (rather than under the competitive acquisition program). It also specifically covers services that are provided by respiratory therapists under Medicare and provides for an additional payment adjustment for these services.</p><p>Additionally, the bill (1) requires the Centers for Medicare & Medicaid Services to develop an electronic template for providers to use when prescribing oxygen and related equipment, supplies, and services; and (2) establishes certain rights for beneficiaries receiving these items and services, such as the right to choose their suppliers and to receive clear communications and be informed about the services provided.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119hr2902"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2902ih.xml"
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
      "title": "SOAR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SOAR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-30T04:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supplemental Oxygen Access Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-30T04:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to improve the payment method for oxygen and oxygen related equipment, supplies, and services, to increase beneficiary access to oxygen and oxygen related equipment, supplies, and services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-30T04:03:27Z"
    }
  ]
}
```
