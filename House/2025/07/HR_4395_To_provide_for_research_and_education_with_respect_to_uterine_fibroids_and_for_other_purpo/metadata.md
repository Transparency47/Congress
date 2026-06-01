# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4395?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4395
- Title: Stephanie Tubbs Jones Uterine Fibroid Research and Education Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4395
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2026-05-13T08:06:06Z
- Update date including text: 2026-05-13T08:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4395",
    "number": "4395",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001067",
        "district": "9",
        "firstName": "Yvette",
        "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
        "lastName": "Clarke",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Stephanie Tubbs Jones Uterine Fibroid Research and Education Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:06Z",
    "updateDateIncludingText": "2026-05-13T08:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:03:30Z",
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
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "OH"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "IL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NJ"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "GA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "AL"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NC"
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
      "sponsorshipDate": "2025-07-15",
      "state": "DC"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "VA"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NY"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "LA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MI"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MA"
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
      "sponsorshipDate": "2025-07-15",
      "state": "GA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "FL"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "AZ"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MI"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "FL"
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
      "sponsorshipDate": "2025-07-15",
      "state": "MS"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
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
      "sponsorshipDate": "2025-07-15",
      "state": "OR"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NJ"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "LA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NY"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "FL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "PA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "FL"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MN"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "AL"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NC"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NY"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "IL"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "TX"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "HI"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NY"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NY"
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
      "sponsorshipDate": "2025-07-16",
      "state": "NC"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "WA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "TN"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NV"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CA"
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
      "sponsorshipDate": "2025-08-08",
      "state": "IL"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "CA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "WI"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MA"
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
      "sponsorshipDate": "2026-05-12",
      "state": "GA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4395ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4395\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Ms. Clarke of New York (for herself, Ms. Brown , Ms. Kelly of Illinois , Mrs. Watson Coleman , Mr. David Scott of Georgia , Ms. Sewell , Mrs. Foushee , Ms. Norton , Ms. McClellan , Ms. Vel\u00e1zquez , Mr. Fields , Mrs. Dingell , Ms. Tlaib , Mrs. Trahan , Mr. Johnson of Georgia , Mr. Peters , Mr. Frost , Ms. Ansari , Mr. Thanedar , Ms. Castor of Florida , Mr. Thompson of Mississippi , Mr. Krishnamoorthi , Ms. Salinas , Mrs. McIver , Mr. Carter of Louisiana , Ms. Meng , Ms. Wilson of Florida , Ms. Lee of Pennsylvania , Ms. Simon , Ms. Wasserman Schultz , Mr. Takano , Ms. Craig , Mr. Figures , Ms. Adams , Mr. Khanna , Mr. Meeks , Ms. Underwood , Mr. Green of Texas , Ms. Tokuda , Ms. Rivas , and Mr. Mannion ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide for research and education with respect to uterine fibroids, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stephanie Tubbs Jones Uterine Fibroid Research and Education Act of 2025 .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nIt is estimated that 20 percent to 50 percent of women of reproductive age currently have uterine fibroids, and up to 77 percent of women will develop fibroids before menopause.\n**(2)**\nIn the United States, an estimated 26,000,000 women between the ages of 15 and 50 have uterine fibroids, and approximately 15,000,000 of these individuals experience symptoms. Uterine fibroids may cause significant morbidity through their presence in the uterus and pelvic cavity, and symptoms can include pelvic pain, severe menstrual bleeding, iron-deficiency anemia, fatigue, bladder or bowel dysfunction, infertility, and pregnancy complications and loss.\n**(3)**\nThe pain, discomfort, stress, and other physical and emotional symptoms of living with fibroids may significantly interfere with a woman\u2019s quality of life, compromising her ability to function normally or work or care for her family, and may lead to more severe health and wellness issues.\n**(4)**\nMost women will experience uterine fibroids by the age of 50, yet few data exist describing the overall patient experience with fibroids.\n**(5)**\nMany people with fibroids are likely undiagnosed. Patients wait on average 3.6 years before seeking treatment, and over 40 percent of patients see two or more health care providers prior to receiving a diagnosis, underscoring the need for improved awareness and education.\n**(6)**\nPeople of color are more likely to develop uterine fibroids. It is estimated that more than 80 percent of Black women and about 70 percent of White women develop fibroids by the time they reach menopause. Black individuals with fibroids have also been shown to have more severe symptoms and develop early-onset uterine fibroids that develop into larger tumors.\n**(7)**\nCurrent research and available data do not provide adequate information on the prevalence and incidence of fibroids in Asian, Hispanic, and Black individuals.\n**(8)**\nSymptomatic uterine fibroids can cause reproductive problems, including infertility. People with uterine fibroids are much more likely to miscarry during early pregnancy than people without them.\n**(9)**\nAccording to the Evidence Report Summary on the Management of Uterine Fibroids, as compiled by the Agency for Healthcare Research and Quality of the Department of Health and Human Services, there is a remarkable lack of high-quality evidence supporting the effectiveness of most interventions for symptomatic fibroids .\n**(10)**\nMost medical options for managing fibroid symptoms regulate or suppress menstruation and prevent pregnancy. There is a great need for minimally invasive, fertility-friendly therapies, as well as biomarkers, imaging assessments, or risk-based algorithms that can help predict patient response to therapy.\n**(11)**\nThe presence of symptomatic uterine fibroids is the most common reason for hysterectomies, accounting for 39 percent of hysterectomies annually in the United States. Approximately 42 per 1,000 women are hospitalized annually because of uterine fibroids, but Black patients have higher rates of hospitalization, hysterectomies, and myomectomies compared to White women. Uterine fibroids are also the leading cause of hospitalization related to a gynecological disorder.\n**(12)**\nThe personal and societal costs of uterine fibroids in the United States are significant. Uterine fibroid tumors have been estimated to cost the United States $5,900,000,000 to $34,400,000,000 annually. The annual direct costs, including surgery, hospital admissions, outpatient visits, and medications, were estimated at $4,100,000,000 to $9,400,000,000 annually. Estimated lost work-hour costs ranged from $1,550,000,000 to $17,200,000,000 annually. Obstetric outcomes that were attributed to fibroid tumors resulted in costs of $238,000,000 to $7,760,000,000 annually.\n**(13)**\nAt the Federal level, uterine fibroid research remains drastically underfunded as compared to patient disease burden. In 2019, fibroid research received about $17,000,000 in funding from the National Institutes of Health, putting it in the bottom 50 of 292 funded conditions.\n#### 3. Research with respect to uterine fibroids\n##### (a) Research\nThe Secretary of Health and Human Services (referred to in this Act as the Secretary ) shall expand, intensify, and coordinate programs for the conduct and support of research with respect to uterine fibroids.\n##### (b) Administration and coordination\nThe Secretary shall carry out the conduct and support of research pursuant to subsection (a), in coordination with the appropriate institutes, offices, and centers of the National Institutes of Health and any other relevant Federal agency, as determined by the Director of the National Institutes of Health.\n##### (c) Authorization of appropriations\nFor the purpose of carrying out this section, there are authorized to be appropriated $30,000,000 for each of fiscal years 2026 through 2030.\n#### 4. Research with respect to Medicaid coverage of uterine fibroids treatment\n##### (a) Research\nThe Secretary (or the Secretary\u2019s designee) shall establish a research database, or expand an existing research database, to collect data on services furnished to individuals diagnosed with uterine fibroids under a State plan (or a waiver of such a plan) under the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) or under a State child health plan (or a waiver of such a plan) under the Children\u2019s Health Insurance Program under title XXI of such Act ( 42 U.S.C. 1397aa et seq. ) for the treatment of such fibroids for purposes of assessing the frequency at which such individuals are furnished such services.\n##### (b) Report\n**(1) In general**\nNot later than the date that is two years after the date of the enactment of this Act, the Secretary shall submit to Congress a report on the amount of Federal and State expenditures with respect to services furnished for the treatment of uterine fibroids under State plans (or waivers of such plans) under the Medicaid program under such title XIX and State child health plans (or waivers of such plans) under the Children\u2019s Health Insurance Program under such title XXI.\n**(2) Coordination**\nThe Secretary shall coordinate the development and submission of the report required under paragraph (1) with any other relevant Federal agency, as determined by the Secretary.\n#### 5. Education and dissemination of information with respect to uterine fibroids\n##### (a) Uterine fibroids public education program\nThe Secretary shall develop and disseminate to the public information regarding uterine fibroids, including information on\u2014\n**(1)**\nthe awareness, incidence, and prevalence of uterine fibroids among individuals, including all minority individuals;\n**(2)**\nthe elevated risk for minority individuals to develop uterine fibroids; and\n**(3)**\nthe availability, as medically appropriate, of the range of treatment options for symptomatic uterine fibroids, including non-hysterectomy treatments and procedures.\n##### (b) Dissemination of information\nThe Secretary may disseminate information under subsection (a) directly or through arrangements with intra-agency initiatives, nonprofit organizations, consumer groups, institutions of higher education (as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )), or Federal, State, or local public private partnerships.\n##### (c) Authorization of appropriations\nFor the purpose of carrying out this section, there are authorized to be appropriated such sums as may be necessary for each of fiscal years 2026 through 2030.\n#### 6. Information to health care providers with respect to uterine fibroids\n##### (a) Dissemination of information\nThe Secretary shall, in consultation and in accordance with guidelines from relevant medical societies, work with health care-related specialty societies and health systems to promote evidence-based care for individuals with fibroids. Such efforts shall include minority individuals who have an elevated risk to develop uterine fibroids and the range of available options for the treatment of symptomatic uterine fibroids, including non-hysterectomy drugs and devices approved under the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ).\n##### (b) Authorization of appropriations\nFor the purpose of carrying out this section, there are authorized to be appropriated such sums as may be necessary for each of the fiscal years 2026 through 2030.\n#### 7. Definition\nIn this Act, the term minority individuals means individuals who are members of a racial and ethnic minority group, as defined in section 1707(g) of the Public Health Service Act ( 42 U.S.C. 300u\u20136(g) ).",
      "versionDate": "2025-07-15",
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
        "actionDate": "2025-07-15",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2275",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stephanie Tubbs Jones Uterine Fibroid Research and Education Act of 2025",
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
        "updateDate": "2025-07-31T11:57:18Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4395ih.xml"
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
      "title": "Stephanie Tubbs Jones Uterine Fibroid Research and Education Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T10:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stephanie Tubbs Jones Uterine Fibroid Research and Education Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T10:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for research and education with respect to uterine fibroids, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T10:18:22Z"
    }
  ]
}
```
