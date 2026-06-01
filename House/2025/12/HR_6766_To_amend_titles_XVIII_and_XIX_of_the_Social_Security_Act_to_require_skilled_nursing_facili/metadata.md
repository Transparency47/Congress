# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6766?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6766
- Title: Essential Caregivers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6766
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-05-30T08:05:49Z
- Update date including text: 2026-05-30T08:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6766",
    "number": "6766",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Essential Caregivers Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:49Z",
    "updateDateIncludingText": "2026-05-30T08:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:04:20Z",
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
          "date": "2025-12-16T15:04:15Z",
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
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CT"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "PA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "KS"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "AZ"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "FL"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MI"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NV"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-12-23",
      "state": "NY"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-12-23",
      "state": "FL"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-23",
      "state": "WI"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-12-23",
      "state": "FL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "FL"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "OR"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "CO"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "CA"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CT"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "MI"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "WI"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CA"
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
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
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
      "sponsorshipDate": "2026-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "DE"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CT"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CT"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CT"
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
      "sponsorshipDate": "2026-01-15",
      "state": "AL"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "KS"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "MA"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "AL"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "FL"
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
      "sponsorshipDate": "2026-01-22",
      "state": "NC"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "NE"
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
      "sponsorshipDate": "2026-01-22",
      "state": "WA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "PA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "PA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "WV"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "CA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NM"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "MI"
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
      "sponsorshipDate": "2026-02-03",
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
      "sponsorshipDate": "2026-02-03",
      "state": "NM"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "NE"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "AL"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NY"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NH"
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
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "NY"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "CA"
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
      "sponsorshipDate": "2026-02-20",
      "state": "HI"
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
      "sponsorshipDate": "2026-02-23",
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
      "sponsorshipDate": "2026-02-23",
      "state": "RI"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CO"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "FL"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "AR"
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
      "sponsorshipDate": "2026-02-24",
      "state": "FL"
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
      "sponsorshipDate": "2026-02-24",
      "state": "PA"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "IA"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "MI"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "SC"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "PA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "IA"
    },
    {
      "bioguideId": "R000395",
      "district": "5",
      "firstName": "Harold",
      "fullName": "Rep. Rogers, Harold [R-KY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "KY"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2026-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
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
      "sponsorshipDate": "2026-03-18",
      "state": "ME"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "VA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "WI"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CO"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "ND"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MI"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "FL"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "AR"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "MN"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MI"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "MI"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "VA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "FL"
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
      "sponsorshipDate": "2026-04-09",
      "state": "AR"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NM"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "MO"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "AL"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MO"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "VT"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "AZ"
    },
    {
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Walberg",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "MI"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "FL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "IN"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NY"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "VA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "RI"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "NC"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "PA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "IL"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "WI"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "CA"
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
      "sponsorshipDate": "2026-04-23",
      "state": "MA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "WA"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "AL"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
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
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "SC"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "ME"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "OH"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "VA"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "SC"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "OH"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MI"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "GA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "ID"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "MI"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "NC"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "OH"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6766ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6766\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Ms. Tenney (for herself, Mr. Larson of Connecticut , Mr. Fitzpatrick , Mr. Mann , Mr. Ciscomani , and Mr. Mills ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to require skilled nursing facilities, nursing facilities, intermediate care facilities for the intellectually disabled, and inpatient rehabilitation facilities to permit essential caregivers access during any period in which regular visitation is restricted.\n#### 1. Short title\nThis Act may be cited as the Essential Caregivers Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAccording to the National Center for Health Statistics of the Centers for Disease Control and Prevention, an estimated 1,300,000 individuals resided in nursing homes in 2020 at the onset of the COVID\u201319 pandemic, and nearly half of all nursing home residents were living with a diagnosis of Alzheimer\u2019s or other related dementia.\n**(2)**\nRegulations issued pursuant to subtitle C of title IV of the Omnibus Budget Reconciliation Act of 1987 (commonly known as the Nursing Home Reform Act of 1987 ) ( Public Law 100\u2013203 ) established basic rights and services for residents of nursing homes, including the right to a dignified existence, self-determination, and communication with and access to persons and services inside and outside the facility .\n**(3)**\nIn March of 2020, the Centers for Medicare & Medicaid Services instructed nursing facilities to restrict visitation for all visitors and non-essential healthcare personnel and cancel communal dining and group activities. Long-term care ombudsman program representatives and State surveyors were among those whose access to long-term care facilities was prohibited or extremely restricted despite reopening guidance released by the Centers for Medicare & Medicaid Services in May of 2020.\n**(4)**\nMany long-term care residents declined dramatically or died prematurely from failure to thrive in isolation.\n**(5)**\nAccording to the National Consumer Voice for Quality Long-Term Care, in the first year of the COVID\u201319 pandemic, 1 in 5 healthcare workers resigned, retired, or were fired. This exacerbated the longstanding problem of staff shortages that already existed. Lack of staff, combined with the forced absence of families, many of whom provided informal care and support to residents, resulted in a significant decline in residents\u2019 health and well-being. During the pandemic, pressure ulcers in nursing home residents rose by 31 percent, the number of residents experiencing significant weight loss rose by 49 percent, the number of residents reporting feeling down, depressed, or hopeless rose by 40 percent, and the number of residents prescribed antipsychotic medications rose by 77.5 percent.\n**(6)**\nAccording to the Department of Health and Human Services, loneliness and isolation, such as that experienced by long-term care residents during the COVID\u201319 pandemic, represent profound threats to an individual\u2019s health and well-being.\n**(7)**\nEssential caregivers provide supplemental care for their loved one, regardless of staff shortages, staff turnover, or emergencies. Essential caregivers support residents and advocate on their behalf.\n#### 3. Right to essential caregivers; access to essential caregivers during periods when visitation is otherwise restricted\n##### (a) Medicare skilled nursing facilities\nSection 1819(c)(3) of the Social Security Act ( 42 U.S.C. 1395i\u20133(c)(3) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) through (E) as clauses (i) through (v), respectively;\n**(2)**\nby striking A skilled nursing facility must\u2014 and inserting the following:\n(A) In general A skilled nursing facility must\u2014 ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(B) Access to essential caregivers during emergency periods when visitation is otherwise restricted (i) Designation of essential caregiver Each skilled nursing facility must recognize the right of each resident of such facility to\u2014 (I) designate and have access to essential caregivers for such resident at all times, including during any period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law; and (II) amend such designation at any time. (ii) Presumption of designation For purposes of clause (i), in the case of a resident who is unable, by reason of cognitive or mental disability, to make an election described in such clause, the resident representative (as defined in section 483.5 of title 42, Code of Federal Regulations) of such resident may make such designation for such resident. (iii) Access to essential caregivers during emergency periods when visitation is otherwise restricted During a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law, including any period in which a waiver or modification of requirements pursuant to section 1135 is in effect, a skilled nursing facility must\u2014 (I) not deny in-person access to a resident by an essential caregiver of the resident except as provided in this subparagraph; (II) allow at least 1 essential caregiver to have access to and provide assistance to such resident at such facility every day and at any time; (III) enforce the agreement described in clause (vii)(II) with respect to an essential caregiver; and (IV) provide reasonable accommodations to protect the rights of a roommate co-living with a resident who has an essential caregiver. (iv) Restrictions on access (I) In general During a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law, including any period in which a waiver or modification of requirements pursuant to section 1135 is in effect, a skilled nursing facility\u2014 (aa) may, subject to item (bb), deny access to a resident by an essential caregiver of the resident for\u2014 (AA) an initial period of not longer than 7 days; and (BB) one additional period of not longer than 7 days (in addition to the initial period described in subitem (AA)) if the department of health or other applicable agency of the State in which the facility is located approves the denial of access for such additional period; and (bb) must allow access to a resident who is in end-of-life care or a resident in decline or distress, as defined by the Secretary. (II) Rule of application For purposes of subclause (I), a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law shall begin on the date that such order or other operation of law takes effect and shall end on the date that such order or other operation of law expires or is otherwise terminated. During any such period, the maximum number of days for which a skilled nursing facility may deny access to a resident by an essential caregiver of the resident is 7 total days (or, subject to the approval of the department of health or other applicable agency of the State in which the facility is located, 14 total days). (v) Compliance and notification (I) Authority No essential caregiver who upholds the agreement described in clause (vii)(II) shall be denied access to the skilled nursing facility of the resident involved. (II) Notification If an essential caregiver fails to comply with an agreement with a skilled nursing facility described in clause (vii)(II), the facility must first provide a warning to the essential caregiver and resident in writing citing specific issues of non-compliance and providing clear guidance for corrective measures. (III) Enforcement If an essential caregiver or resident, after receiving a notification of noncompliance described in subclause (II), fails to take corrective action, the essential caregiver may subsequently be denied access to the resident. In such cases, the facility shall provide to such caregiver and such resident (or health care proxy of such resident), not later than 24 hours after such denial of access occurs, a written explanation as to why such caregiver was denied access to such resident. Such explanation must include the resident\u2019s and caregiver's options for appeal under the processes established under clause (vi). (vi) Options for residents and caregivers to appeal denials of access (I) In general Not later than 2 years after the date of enactment of this subparagraph, the Secretary shall issue a final rule establishing a process for residents and caregivers to appeal denials of access to the State survey agency. (II) Appeals process The State survey agency shall\u2014 (aa) receive appeals from residents and essential caregivers challenging a decision by a skilled nursing facility to deny access under clause (v); and (bb) begin investigating such appeals not later than 2 business days after receiving such appeals. (III) Burden of proof During an appeal received under the appeals process established under subclause (I), if a skilled nursing facility defends a decision to deny access to an essential caregiver under clause (v) on the basis that the essential caregiver violated the agreement described in clause (vii)(II), the skilled nursing facility shall have the burden of proof in demonstrating that the essential caregiver violated such agreement. (IV) Resolution of appeals (aa) Determination With respect to an appeal received under the appeals process established under subclause (I), the State survey agency shall make a determination as to whether a skilled nursing facility violated a requirement or prohibition of this subparagraph within 48 hours of commencing its investigation. (bb) Violations If the agency determines that a facility has violated such a requirement or prohibition, the agency shall\u2014 (AA) require the facility to allow immediate access to the essential caregiver in question; (BB) require the facility to establish a corrective action plan to prevent the recurrence of such violation within a 7-day period of receiving notice from the agency; and (CC) impose a civil money penalty in an amount to be determined by the agency (not to exceed $5,000) if such facility fails to implement the corrective action plan within the 7-day period specified in subitem (BB). (vii) Definition of essential caregiver For purposes of this subparagraph, the term essential caregiver means, with respect to a resident of a skilled nursing facility, an individual who\u2014 (I) is designated by or on behalf of the resident pursuant to clause (i) or clause (ii); and (II) agrees to follow all safety protocols established by such facility, which shall be clearly specified in writing and may be no more restrictive than the safety protocols (including safety standards and entry requirements) applicable to staff of such facility. .\n##### (b) Medicaid nursing facilities\nSection 1919(c)(3) of the Social Security Act ( 42 U.S.C. 1396r(c)(3) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) through (E) as clauses (i) through (v), respectively;\n**(2)**\nby striking A nursing facility must\u2014 and inserting the following:\n(A) In general A nursing facility must\u2014 ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(B) Access to essential caregivers during emergency periods when visitation is otherwise restricted (i) Designation of essential caregiver Each nursing facility must recognize the right of each resident of such facility to\u2014 (I) designate and have access to essential caregivers for such resident at all times, including during any period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law; and (II) amend such designation at any time. (ii) Presumption of designation For purposes of clause (i), in the case of a resident who is unable, by reason of cognitive or mental disability, to make an election described in such clause, the resident representative (as defined in section 483.5 of title 42, Code of Federal Regulations) of such resident may be permitted to make such designation for such resident. (iii) Access to essential caregivers during emergency periods when visitation is otherwise restricted During a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law, including any period in which a waiver or modification of requirements pursuant to section 1135 is in effect, a nursing facility must\u2014 (I) not deny in-person access to a resident by an essential caregiver of the resident except as provided in this subparagraph; (II) allow at least 1 essential caregiver to have access to and provide assistance to such resident at such facility every day and at any time; (III) enforce the agreement described in clause (vii)(II) with respect to an essential caregiver; and (IV) provide reasonable accommodations to protect the rights of a roommate co-living with a resident who has an essential caregiver. (iv) Restrictions on access (I) In general During a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law, including any period in which a waiver or modification of requirements pursuant to section 1135 is in effect, a nursing facility\u2014 (aa) may, subject to item (bb), deny access to a resident by an essential caregiver of the resident for\u2014 (AA) an initial period of not longer than 7 days; and (BB) one additional period of not longer than 7 days (in addition to the initial period described in subitem (AA)) if the department of health or other applicable agency of the State in which the facility is located approves the denial of access for such additional period; and (bb) must allow access to a resident who is in end-of-life care or a resident in decline or distress, as defined by the Secretary. (II) Rule of application For purposes of subclause (I), a period of emergency in which regular visitation is restricted by order of a Federal, State, or local authority or by other operation of law shall begin on the date that such order or other operation of law takes effect and shall end on the date that such order or other operation of law expires or is otherwise terminated. During any such period, the maximum number of days for which a nursing facility may deny access to a resident by an essential caregiver of the resident is 7 total days (or, subject to the approval of the department of health or other applicable agency of the State in which the facility is located, 14 total days). (v) Compliance and notification (I) Authority No essential caregiver who upholds the agreement described in clause (vii)(II) shall be denied access to the nursing facility of the resident involved. (II) Notification If an essential caregiver fails to comply with an agreement with a nursing facility described in clause (vii)(II), the facility must first provide a warning to the essential caregiver and resident in writing citing specific issues of non-compliance and providing clear guidance for corrective measures. (III) Enforcement If an essential caregiver or resident, after receiving a notification of noncompliance described in subclause (II), fails to take corrective action, the essential caregiver may subsequently be denied access to the resident. In such cases, the facility shall provide to such caregiver and such resident (or health care proxy of such resident), not later than 24 hours after such denial of access occurs, a written explanation as to why such caregiver was denied access to such resident. Such explanation must include the resident\u2019s and caregiver's options for appeal under the processes established under clause (vi). (vi) Options for residents and caregivers to appeal denials of access (I) In general Not later than 2 years after the date of enactment of this subparagraph, the Secretary shall issue a final rule establishing a process for residents and caregivers to appeal denials of access to the State survey agency. (II) Appeals process The State survey agency shall\u2014 (aa) receive appeals from residents and essential caregivers challenging a decision by a nursing facility to deny access under clause (v); and (bb) begin investigating such appeals not later than 2 business days after receiving such appeals. (III) Burden of proof During an appeal received under the appeals process established under subclause (I), if a nursing facility defends a decision to deny access to an essential caregiver under clause (v) on the basis that the essential caregiver violated the agreement described in clause (vii)(II), the nursing facility shall have the burden of proof in demonstrating that the essential caregiver violated such agreement. (IV) Resolution of appeals (aa) Determination With respect to an appeal received under the appeals process established under subclause (I), the State survey agency shall make a determination as to whether a nursing facility violated a requirement or prohibition of this subparagraph within 48 hours of commencing its investigation. (bb) Violations If the agency determines that a facility has violated such a requirement or prohibition, the agency shall\u2014 (AA) require the facility to allow immediate access to the essential caregiver in question; (BB) require the facility to establish a corrective action plan to prevent the recurrence of such violation within a 7-day period of receiving notice from the agency; and (CC) impose a civil money penalty in an amount to be determined by the agency (not to exceed $5,000) if such facility fails to implement the corrective action plan within the 7-day period specified in subitem (BB). (vii) Definition of essential caregiver For purposes of this subparagraph, the term essential caregiver means, with respect to a resident of a nursing facility, an individual who\u2014 (I) is designated by or on behalf of the resident pursuant to clause (i) or clause (ii); and (II) agrees to follow all safety protocols established by such facility, which shall be clearly specified in writing and may be no more restrictive than the safety protocols (including safety standards and entry requirements) applicable to staff of such facility. .\n##### (c) Intermediate care facilities for the intellectually disabled\nSection 1905(d) of the Social Security Act ( 42 U.S.C. 1396d(d) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking and at the end;\n**(2)**\nin paragraph (3), by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following new paragraph:\n(4) the institution complies with the requirements relating to the designation of, and access to residents by, essential caregivers described in section 1919(c)(3)(B) in the same manner as if such institution were a nursing facility. .\n##### (d) Inpatient rehabilitation facilities\nSection 1866(a)(1) of the Social Security Act ( 42 U.S.C. 1395cc(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (X), by striking and at the end;\n**(2)**\nin subparagraph (Y), by striking the period at the end and inserting , and ; and\n**(3)**\nby inserting after subparagraph (Y) the following new subparagraph:\n(Z) in the case of an inpatient rehabilitation facility that is located on the same campus (as defined by the Secretary) as a skilled nursing facility, nursing facility (as defined in section 1919(a)), or intermediate care facility for the intellectually disabled (as described in section 1905(d)), to comply with the requirements relating to the designation of, and access to residents by, essential caregivers described in section 1819(c)(3)(B) in the same manner as if such institution were a skilled nursing facility. .\n##### (e) Regulations\nThe Secretary of Health and Human Services shall, after consultation with stakeholders (including residents, family members, long-term care ombudsmen, other advocates of nursing home residents, and nursing home providers), promulgate regulations to carry out this Act and the amendments made by this Act.\n##### (f) Rules of construction\n**(1) No new authority for State and local officials to restrict visitation at nursing facilities**\nNothing in this section or the amendments made by this section shall be construed as creating any new authority for State or local officials to restrict visitation at nursing facilities.\n**(2) No new authority for nursing facilities to unilaterally restrict visitation**\nNothing in this section or the amendments made by this section shall be construed as creating any new authority for a skilled nursing facility or nursing facility (as such terms are defined in sections 1819 and 1919 of the Social Security Act, respectively ( 42 U.S.C. 1395i\u20133 , 1396r)) to restrict visitation.\n##### (g) Effective date\nThe amendments made by this Act shall take effect on the date that is 2 years after the date of enactment of this Act, and shall apply with respect to periods beginning on or after such date in which regular visitation at nursing facilities is restricted by order of a Federal, State, or local authority or by other operation of law.",
      "versionDate": "2025-12-16",
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
        "actionDate": "2025-12-16",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3492",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Essential Caregivers Act of 2025",
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
        "updateDate": "2026-03-20T18:49:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-16",
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
          "measure-id": "id119hr6766",
          "measure-number": "6766",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-16",
          "originChamber": "HOUSE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6766v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-12-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Essential Caregivers Act of 2025</strong>\u00a0</p><p>This bill prohibits certain health care facilities from limiting the access of essential caregivers to residents of those facilities, including during designated emergency periods. <em></em>\u00a0</p><p>Specifically, the bill generally prohibits Medicare skilled nursing facilities, Medicaid nursing facilities, Medicaid intermediate care facilities, and associated inpatient rehabilitation facilities from restricting the access of essential caregivers to residents of the facilities, including during emergency periods in which visitation rights are otherwise restricted. During emergency periods, facilities may restrict access for an initial period of up to seven days and for one additional maximum seven-day period (if the additional period is approved by the state health department). Facilities may restrict access for a total of 7 days (or 14 days with the approval of the state health department) during an emergency period.</p><p>Essential caregivers must agree to comply with any safety protocols set by the facility, which may be no more stringent for caregivers compared to those for staff. Caregivers who fail to comply with these requirements may be denied access, subject to an appeals process.</p>"
        },
        "title": "Essential Caregivers Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6766.xml",
    "summary": {
      "actionDate": "2025-12-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Essential Caregivers Act of 2025</strong>\u00a0</p><p>This bill prohibits certain health care facilities from limiting the access of essential caregivers to residents of those facilities, including during designated emergency periods. <em></em>\u00a0</p><p>Specifically, the bill generally prohibits Medicare skilled nursing facilities, Medicaid nursing facilities, Medicaid intermediate care facilities, and associated inpatient rehabilitation facilities from restricting the access of essential caregivers to residents of the facilities, including during emergency periods in which visitation rights are otherwise restricted. During emergency periods, facilities may restrict access for an initial period of up to seven days and for one additional maximum seven-day period (if the additional period is approved by the state health department). Facilities may restrict access for a total of 7 days (or 14 days with the approval of the state health department) during an emergency period.</p><p>Essential caregivers must agree to comply with any safety protocols set by the facility, which may be no more stringent for caregivers compared to those for staff. Caregivers who fail to comply with these requirements may be denied access, subject to an appeals process.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr6766"
    },
    "title": "Essential Caregivers Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-12-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Essential Caregivers Act of 2025</strong>\u00a0</p><p>This bill prohibits certain health care facilities from limiting the access of essential caregivers to residents of those facilities, including during designated emergency periods. <em></em>\u00a0</p><p>Specifically, the bill generally prohibits Medicare skilled nursing facilities, Medicaid nursing facilities, Medicaid intermediate care facilities, and associated inpatient rehabilitation facilities from restricting the access of essential caregivers to residents of the facilities, including during emergency periods in which visitation rights are otherwise restricted. During emergency periods, facilities may restrict access for an initial period of up to seven days and for one additional maximum seven-day period (if the additional period is approved by the state health department). Facilities may restrict access for a total of 7 days (or 14 days with the approval of the state health department) during an emergency period.</p><p>Essential caregivers must agree to comply with any safety protocols set by the facility, which may be no more stringent for caregivers compared to those for staff. Caregivers who fail to comply with these requirements may be denied access, subject to an appeals process.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr6766"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6766ih.xml"
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
      "title": "Essential Caregivers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Essential Caregivers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T03:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles XVIII and XIX of the Social Security Act to require skilled nursing facilities, nursing facilities, intermediate care facilities for the intellectually disabled, and inpatient rehabilitation facilities to permit essential caregivers access during any period in which regular visitation is restricted.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T03:03:20Z"
    }
  ]
}
```
