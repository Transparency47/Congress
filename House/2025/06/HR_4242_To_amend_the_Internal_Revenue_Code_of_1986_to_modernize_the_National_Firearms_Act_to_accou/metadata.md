# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4242?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4242
- Title: Innovate Less Lethal to De-Escalate Tax Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 4242
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2026-04-02T13:01:44Z
- Update date including text: 2026-04-02T13:01:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-12-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-10 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 26 - 15.
- 2026-02-02 - Calendars: Placed on the Union Calendar, Calendar No. 407.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-476.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-476.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-12-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-10 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 26 - 15.
- 2026-02-02 - Calendars: Placed on the Union Calendar, Calendar No. 407.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-476.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-476.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4242",
    "number": "4242",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001183",
        "district": "1",
        "firstName": "David",
        "fullName": "Rep. Schweikert, David [R-AZ-1]",
        "lastName": "Schweikert",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Innovate Less Lethal to De-Escalate Tax Modernization Act",
    "type": "HR",
    "updateDate": "2026-04-02T13:01:44Z",
    "updateDateIncludingText": "2026-04-02T13:01:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-02-02",
      "calendarNumber": {
        "calendar": "U00407"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 407.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-02-02",
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
      "text": "Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-476.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Ways and Means. H. Rept. 119-476.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 26 - 15.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
        "item": [
          {
            "date": "2026-02-02T20:03:32Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-10T15:15:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-27T13:02:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "AZ"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "WI"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "MN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "NY"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "OH"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "TX"
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
      "sponsorshipDate": "2025-06-27",
      "state": "NC"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "WA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "NY"
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
      "sponsorshipDate": "2025-07-15",
      "state": "WV"
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
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "MN"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
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
      "sponsorshipDate": "2025-07-22",
      "state": "TX"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "MN"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "CO"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "AZ"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "IN"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
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
      "sponsorshipDate": "2025-09-18",
      "state": "VA"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "IN"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "OH"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "PA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "CA"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "MS"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "MS"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
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
      "sponsorshipDate": "2025-10-06",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-06",
      "state": "MI"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "IA"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "TX"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "UT"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
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
      "sponsorshipDate": "2025-10-24",
      "state": "LA"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "UT"
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
      "sponsorshipDate": "2025-10-24",
      "state": "CT"
    },
    {
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "OK"
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
      "sponsorshipDate": "2025-10-28",
      "state": "VA"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "PA"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "TN"
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
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "IA"
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
      "sponsorshipDate": "2025-12-09",
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
      "sponsorshipDate": "2025-12-09",
      "state": "OH"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "CO"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CA"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "NC"
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
      "sponsorshipDate": "2026-01-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4242ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4242\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Schweikert (for himself, Mr. Stanton , Mr. Fitzgerald , Mrs. Fischbach , Ms. Tenney , Mr. Carey , Mr. Cuellar , Mr. Davis of North Carolina , Ms. Perez , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to modernize the National Firearms Act to account for advancements in technology and less-than-lethal weapons, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Innovate Less Lethal to De-Escalate Tax Modernization Act .\n#### 2. Exemption of certain less-than-lethal projectile devices from firearms and ammunition tax\n##### (a) In general\nSection 4182 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e), and\n**(2)**\nby inserting after subsection (c) the following new subsection:\n(d) Less-than-Lethal projectile devices (1) In general The tax imposed by section 4181 shall not apply to\u2014 (A) any less-than-lethal projectile device, (B) any device contained on the most recent list made available by the Secretary under paragraph (3)(B), and (C) any shell or cartridge that meets the requirement of paragraph (2)(B) and is designed for use in a device referred to in subparagraph (A) or (B). (2) Less-than-lethal projectile device The term less-than-lethal projectile device means a device that\u2014 (A) is not designed or intended to expel, and may not be readily converted to accept and discharge\u2014 (i) ammunition commonly used in handguns, rifles, or shotguns, or (ii) any other projectile at a velocity exceeding 500 feet per second, (B) is designed and intended to be used in a manner that is not likely to cause death or serious bodily injury, and (C) does not accept, and is not able to be readily modified to accept, ammunition feeding devices\u2014 (i) loaded through the inside of a pistol grip, or (ii) commonly used in semiautomatic firearms. (3) Request for classification Pursuant to a request made by the manufacturer, producer, or importer of a device for a determination as to whether such device satisfies the requirements under paragraph (2), the Secretary shall make such determination not later than 90 days after the date of receipt of such request. (4) Annual review of new and emerging technologies (A) List of less-than-lethal projectile devices The Secretary shall make publicly available a list of devices that the Secretary has determined are described in paragraph (2) and shall update such list annually to take into account new devices. (B) List of non-lethal devices the projectiles of which exceed 500 feet per second (i) In general The Secretary shall\u2014 (I) make publicly available a list of devices that the Secretary has determined are not described in paragraph (2) but would be so described if such paragraph were applied without regard to subparagraph (A)(ii) thereof, and (II) update such list annually to take into account new devices. (ii) Report to Congress The Secretary shall annually submit a written report to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate regarding the annual list of devices described in clause (i), including a copy of such list, a description of the devices that were considered for inclusion on such list, and the reasons for including or excluding such devices from such list. .\n##### (b) Effective date\nThe amendments made by this section shall apply to articles sold by the manufacturer, producer, or importer after the date of the enactment of this Act.\n#### 3. Exemption of certain less-than-lethal projectile devices from National Firearms Act\nSection 5845(a) of the Internal Revenue Code of 1986 is amended by striking an antique firearm or and inserting any antique firearm, any less-than-lethal projectile device (as defined in section 4182(d)(2)), any device referred to in section 4182(d)(1)(B), or .",
      "versionDate": "2025-06-27",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr4242rh.xml",
      "text": "IB\nUnion Calendar No. 407\n119th CONGRESS\n2d Session\nH. R. 4242\n[Report No. 119\u2013476]\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Schweikert (for himself, Mr. Stanton , Mr. Fitzgerald , Mrs. Fischbach , Ms. Tenney , Mr. Carey , Mr. Cuellar , Mr. Davis of North Carolina , Ms. Perez , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Ways and Means\nFebruary 2, 2026 Additional sponsors: Mrs. Miller of West Virginia , Mr. Rutherford , Mr. Stauber , Mr. Nehls , Ms. Johnson of Texas , Mr. Moran , Mr. Finstad , Mr. Evans of Colorado , Mr. Ciscomani , Mr. Yakym , Mr. Gill of Texas , Mr. McGuire , Mr. Vindman , Mr. Stutzman , Mrs. Beatty , Mr. Mackenzie , Mr. Levin , Mr. Ezell , Mr. Thompson of Mississippi , Mr. Veasey , Mr. Correa , Ms. Stevens , Mrs. Hinson , Ms. Van Duyne , Ms. Maloy , Mr. Cline , Mr. Carter of Louisiana , Mr. Kennedy of Utah , Mr. Larson of Connecticut , Mr. Hern of Oklahoma , Mr. Wittman , Mr. Boyle of Pennsylvania , Mr. Kustoff , Mr. Thanedar , Mr. Feenstra , Mr. Steube , Mr. Miller of Ohio , Ms. Boebert , Mr. Gray , Mr. Murphy , and Ms. Clarke of New York\nFebruary 2, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on June 27, 2025\nA BILL\nTo amend the Internal Revenue Code of 1986 to modernize the National Firearms Act to account for advancements in technology and less-than-lethal weapons, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Innovate Less Lethal to De-Escalate Tax Modernization Act .\n#### 2. Exemption of certain less-than-lethal projectile devices from firearms and ammunition tax\n##### (a) In general\nSection 4182 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e), and\n**(2)**\nby inserting after subsection (c) the following new subsection:\n(d) Less-than-Lethal projectile devices (1) In general The tax imposed by section 4181 shall not apply to\u2014 (A) any less-than-lethal projectile device, (B) any device contained on the most recent list made available by the Secretary under paragraph (4)(B), and (C) any shell or cartridge that meets the requirement of paragraph (2)(B) and is designed for use in a device referred to in subparagraph (A) or (B). (2) Less-than-lethal projectile device The term less-than-lethal projectile device means a device that\u2014 (A) is not designed or intended to expel, and may not be readily converted to accept and discharge\u2014 (i) ammunition commonly used in handguns, rifles, or shotguns, or (ii) any other projectile at a velocity exceeding 500 feet per second, (B) is designed and intended to be used in a manner that is not likely to cause death or serious bodily injury, and (C) does not accept, and is not able to be readily modified to accept, ammunition feeding devices\u2014 (i) loaded through the inside of a pistol grip, or (ii) commonly used in semiautomatic firearms. (3) Request for classification Pursuant to a request made by the manufacturer, producer, or importer of a device for a determination as to whether such device satisfies the requirements under paragraph (2), the Secretary shall make such determination not later than 90 days after the date of receipt of such request. (4) Annual review of new and emerging technologies (A) List of less-than-lethal projectile devices The Secretary shall make publicly available a list of devices that the Secretary has determined are described in paragraph (2) and shall update such list annually to take into account new devices. (B) List of non-lethal devices the projectiles of which exceed 500 feet per second (i) In general The Secretary shall\u2014 (I) make publicly available a list of devices that the Secretary has determined are not described in paragraph (2) but would be so described if such paragraph were applied without regard to subparagraph (A)(ii) thereof, and (II) update such list annually to take into account new devices. (ii) Report to Congress The Secretary shall annually submit a written report to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate regarding the annual list of devices described in clause (i), including a copy of such list, a description of the devices that were considered for inclusion on such list, and the reasons for including or excluding such devices from such list. .\n##### (b) Effective date\n**(1) In general**\nExcept as otherwise provided in this subsection, the amendments made by this section shall apply to articles sold by the manufacturer, producer, or importer after the date of the enactment of this Act.\n**(2) Requests for determinations**\nSection 4182(d)(3) of the Internal Revenue Code of 1986 (as added by this section) shall apply to requests received after the date of the enactment of this Act, except that any request under such section which is received during the 180-day period beginning on the date of the enactment of this Act shall be treated for purposes of such section as received as of the close of such period.\n#### 3. Exemption of certain less-than-lethal projectile devices from National Firearms Act\nSection 5845(a) of the Internal Revenue Code of 1986 is amended by striking an antique firearm or and inserting any antique firearm, any less-than-lethal projectile device (as defined in section 4182(d)(2)), any device referred to in section 4182(d)(1)(B), or .",
      "versionDate": "2026-02-02",
      "versionType": "Reported in House"
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
        "actionDate": "2026-02-24",
        "text": "Received in the Senate."
      },
      "number": "2189",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Law-Enforcement Innovate to De-Escalate Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-16",
        "text": "Read twice and referred to the Committee on Finance. (text: CR S8782)"
      },
      "number": "3514",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Less Than Lethal Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Firearms and explosives",
            "updateDate": "2026-01-20T19:45:40Z"
          },
          {
            "name": "Sales and excise taxes",
            "updateDate": "2026-01-20T19:45:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-07-17T19:12:22Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4242ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr4242rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Innovate Less Lethal to De-Escalate Tax Modernization Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-03T06:53:19Z"
    },
    {
      "title": "Innovate Less Lethal to De-Escalate Tax Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:55Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Innovate Less Lethal to De-Escalate Tax Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to modernize the National Firearms Act to account for advancements in technology and less-than-lethal weapons, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T05:33:38Z"
    }
  ]
}
```
