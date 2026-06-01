# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5645?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5645
- Title: Pray Safe Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5645
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-05-27T08:05:51Z
- Update date including text: 2026-05-27T08:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-01 - Committee: Referred to the Subcommittee on Emergency Management and Technology.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-01 - Committee: Referred to the Subcommittee on Emergency Management and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5645",
    "number": "5645",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "M001188",
        "district": "6",
        "firstName": "Grace",
        "fullName": "Rep. Meng, Grace [D-NY-6]",
        "lastName": "Meng",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Pray Safe Act of 2025",
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
      "actionDate": "2025-10-01",
      "committees": {
        "item": {
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Emergency Management and Technology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-10-01T20:16:23Z",
              "name": "Referred to"
            }
          },
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-30T16:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
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
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "OH"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "IL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NE"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "IN"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "RI"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "AZ"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "NY"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "OH"
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
      "sponsorshipDate": "2025-10-31",
      "state": "PA"
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
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NJ"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
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
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
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
      "sponsorshipDate": "2025-12-09",
      "state": "GA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "MI"
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
      "sponsorshipDate": "2025-12-11",
      "state": "NY"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "NJ"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MI"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "NE"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "MI"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "FL"
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "KS"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "AZ"
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
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "CA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "AZ"
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
      "sponsorshipDate": "2026-05-26",
      "state": "NY"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5645ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5645\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Ms. Meng (for herself, Ms. Salazar , Mr. Goldman of New York , Mr. Miller of Ohio , Mr. Min , Mr. Lawler , Mr. Schneider , Mr. Bacon , Mr. Correa , Mr. Mackenzie , Mr. Carson , and Mr. Bilirakis ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a Federal Clearinghouse on Safety and Best Practices for Nonprofit Organizations, Faith-based Organizations, and Houses of Worship within the Department of Homeland Security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pray Safe Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Clearinghouse**\nThe term Clearinghouse means the Federal Clearinghouse on Safety and Security Best Practices for Nonprofit Organizations, Faith-based Organizations, and Houses of Worship established under section 3(a).\n**(2) Department**\nThe term Department means the Department of Homeland Security.\n**(3) Faith-based organization**\nThe term faith-based organization means a group, center, or nongovernmental organization with a religious, ideological, or spiritual motivation, character, affiliation, or purpose that meets the definition of nonprofit organization.\n**(4) House of worship**\nThe term house of worship means a place or building, including a synagogue, mosque, temple, and church, in which congregants practice their religious or spiritual beliefs.\n**(5) Nonprofit organization**\nThe term nonprofit organization means an organization\u2014\n**(A)**\nof the type described in subsection (c)(3) of section 501 of the Internal Revenue Code of 1986 and exempt from taxation under subsection (a) of such section; and\n**(B)**\ndetermined to be at risk of a terrorist attack or other threat by the Secretary.\n**(6) Safety and security**\nThe term safety and security means prevention of, protection against, or recovery from threats and incidents, including natural disasters, manmade disasters, or terrorist attacks.\n**(7) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n#### 3. Federal Clearinghouse on Safety and Security Best Practices for Nonprofit Organizations, Faith-based Organizations, and Houses of Worship\n##### (a) Federal Clearinghouse\n**(1) Establishment**\n**(A) In general**\nNot later than 270 days after the date of enactment of this Act, the Secretary, in consultation with the Attorney General, the Executive Director of the White House Office of Faith-Based and Neighborhood Partnerships, and the head of any other agency the Secretary determines appropriate, shall establish within the Department a Federal Clearinghouse on Safety and Security Best Practices for Nonprofit Organizations, Faith-based Organizations, and Houses of Worship.\n**(B) Purpose**\nThe Clearinghouse shall be the primary resource of the Federal Government to\u2014\n**(i)**\neducate and publish online best practices and recommendations for safety and security for nonprofit organizations, including faith-based organizations, and houses of worship; and\n**(ii)**\nprovide information relating to Federal grant programs available to nonprofit organizations, including faith-based organizations, and houses of worship.\n**(C) Personnel**\n**(i) Assignments**\nThe Clearinghouse shall be assigned such personnel and resources as the Secretary considers appropriate to carry out this subsection.\n**(ii) Detailees**\nThe Secretary may coordinate detailees on a reimbursable or a nonreimbursable basis as required for the Clearinghouse.\n**(iii) Designated point of contact**\n**(I) In general**\nThere shall be not fewer than 1 employee assigned or detailed to the Clearinghouse who shall be the designated point of contact to provide information and assistance to nonprofit organizations, including faith-based organizations, and houses of worship, including assistance relating to the grant program established under subsection (c).\n**(II) Contact information**\nThe contact information of the designated point of contact under subclause (I) shall be made available on the website of the Clearinghouse.\n**(iv) Qualification**\nTo the maximum extent possible, any personnel assigned or detailed to the Clearinghouse under this subparagraph should be familiar with nonprofit organizations, including faith-based organizations, and houses of worship and with physical and online security measures to identify and prevent safety and security risks.\n**(2) Clearinghouse contents**\n**(A) Evidence-based tiers**\n**(i) In general**\nThe Secretary, in consultation with the Attorney General, the Executive Director of the White House Office of Faith-Based and Neighborhood Partnerships, and the head of any other agency the Secretary determines appropriate, shall develop tiers for determining evidence-based best practices and recommendations that demonstrate a significant effect on improving safety and security of nonprofit organizations, including faith-based organizations, and houses of worship.\n**(ii) Requirements**\nThe tiers required to be developed under clause (i) shall\u2014\n**(I)**\nprioritize\u2014\n**(aa)**\nstrong evidence from not fewer than 1 well-designed and well-implemented experimental study; and\n**(bb)**\nmoderate evidence from not fewer than 1 well-designed and well-implemented quasi-experimental study; and\n**(II)**\nconsider promising evidence that demonstrates a rationale based on high-quality research findings or positive evaluations that the activity, strategy, or intervention is likely to improve and promote safety and security of nonprofit organizations, including faith-based organizations, and houses of worship.\n**(B) Criteria for best practices and recommendations**\nThe best practices and recommendations referred to in paragraph (1)(B)(i) of the Clearinghouse shall, at a minimum\u2014\n**(i)**\nidentify areas of concern for nonprofit organizations, including faith-based organizations, and houses of worship, including event planning recommendations, checklists, facility hardening, tabletop exercise resources, and other resilience measures;\n**(ii)**\ninvolve comprehensive safety and security measures, including threat prevention, preparedness, protection, mitigation, incident response, and recovery to improve the safety and security posture of nonprofit organizations, including faith-based organizations, and houses of worship upon implementation;\n**(iii)**\ninvolve comprehensive safety and security measures, including preparedness, protection, mitigation, incident response, and recovery to improve the resiliency of nonprofit organizations, including faith-based organizations, and houses of worship from threats and incidents, including natural disasters, manmade disasters, or terrorist attacks or other threats;\n**(iv)**\ninclude any evidence or research rationale supporting the determination of the Clearinghouse that the comprehensive safety and security measures under clauses (ii) and (iii) have been shown to have a significant effect on improving the safety and security of individuals who, at the time of any such threat or incident, are physically located in the place or building of a nonprofit organization, including a faith-based organization, or a house of worship, including\u2014\n**(I)**\nfindings and data from previous Federal, State, local, Tribal, territorial, private sector, and nongovernmental organization research centers relating to the safety and security of nonprofit organizations, including faith-based organizations, and houses of worship, including from targeted violence; and\n**(II)**\nother supportive evidence or findings relied upon by the Clearinghouse in determining best practices and recommendations to improve the safety and security posture of nonprofit organizations, including faith-based organizations, and houses of worship upon implementation; and\n**(v)**\ninclude an overview of the available resources the Clearinghouse can provide to nonprofit organizations and houses of worship.\n**(C) Additional information**\nThe Clearinghouse shall maintain and make available a comprehensive index of all Federal grant programs for which nonprofit organizations, including faith-based organizations, and houses of worship are eligible, which shall include the performance metrics the recipient will be required to provide for each grant.\n**(D) Past recommendations**\nTo the greatest extent practicable, the Clearinghouse shall identify and present, as appropriate, best practices and recommendations issued by Federal, State, local, Tribal, territorial, private sector, and nongovernmental organizations relevant to the safety and security of nonprofit organizations, including faith-based organizations, and houses of worship.\n**(E) Existing platform**\nThe Secretary may establish and maintain the Clearinghouse on an online platform or a website that is in existence as of the date of enactment of this Act.\n**(3) Assistance and training**\nThe Secretary may produce and publish materials on the Clearinghouse to assist and train nonprofit organizations, including faith-based organizations, and houses of worship regarding the implementation of the best practices and recommendations under this subsection.\n**(4) Continuous improvement**\n**(A) In general**\nThe Secretary shall\u2014\n**(i)**\ncollect for the purpose of continuous improvement of the Clearinghouse\u2014\n**(I)**\nClearinghouse data analytics;\n**(II)**\nuser feedback on the implementation of resources, best practices, and recommendations identified by the Clearinghouse; and\n**(III)**\nany evaluations conducted regarding implementation of such best practices and recommendations;\n**(ii)**\nin coordination with the Faith-Based Security Advisory Council of the Department, the Department of Justice, the Executive Director of the White House Office of Faith-Based and Neighborhood Partnerships, and any other agency the Secretary determines appropriate\u2014\n**(I)**\nassess and identify Clearinghouse best practices and recommendations for which there are no resources available through Federal Government programs for implementation;\n**(II)**\nprovide feedback on the implementation of such best practices and recommendations; and\n**(III)**\npropose additional best practices and recommendations for inclusion in the Clearinghouse; and\n**(iii)**\nnot less frequently than annually, examine and update the Clearinghouse in accordance with\u2014\n**(I)**\nthe information collected under clause (i); and\n**(II)**\nthe best practices and recommendations proposed under clause (ii)(III).\n**(B) Report to Congress**\nNot later than 3 years after the date of enactment of this Act, and every 3 years thereafter during the period in which the Clearinghouse is in existence, the Secretary shall submit to Congress a report on the updates under subparagraph (A)(iii) made to the Clearinghouse during the preceding 3-year period, which shall include a description of any changes made pursuant thereto to the Clearinghouse.\n##### (b) Notification of the Clearinghouse\n**(1) In general**\nThe Secretary shall provide to the individuals, Federal agencies, and committees specified in paragraph (2) written notification of the establishment of the Clearinghouse, including updates pertaining to grant programs identified under subsection (a)(2)(C).\n**(2) Individuals, Federal agencies, and committees specified**\nThe individuals, Federal entities, and committees specified in this paragraph are the following:\n**(A)**\nEvery State homeland security advisor.\n**(B)**\nEvery State department of homeland security.\n**(C)**\nOther Federal agencies with grant programs or initiatives that aid in the safety and security of nonprofit organizations, including faith-based organizations, and houses of worship, as determined appropriate by the Secretary.\n**(D)**\nEvery Cyber Security Advisor.\n**(E)**\nEvery Protective Security Advisor.\n**(F)**\nEvery Federal Bureau of Investigation Joint Terrorism Task Force.\n**(G)**\nEvery Homeland Security Fusion Center.\n**(H)**\nEvery State or territorial Governor or other chief executive.\n**(I)**\nThe Committee on Homeland Security and Governmental Affairs and the Committee on the Judiciary of the Senate.\n**(J)**\nThe Committee on Homeland Security and the Committee on the Judiciary of the House of Representatives.\n##### (c) Federal grants and resources overview\n**(1) In general**\nTo the extent practicable, the Secretary, when carrying out subsection (a)(2)(C), shall include a grants program overview on the website of the Clearinghouse that shall\u2014\n**(A)**\nbe a location for all information regarding Federal grant programs that are open to nonprofit organizations, including faith-based organizations, and houses of worship for the purposes of safety and security;\n**(B)**\ndirectly link to each grant application and any applicable user guides;\n**(C)**\nidentify all safety and security homeland security assistance programs managed by the Department that may be used to implement best practices and recommendations of the Clearinghouse;\n**(D)**\nconcurrent with the application period for any grant identified under subsection (a)(2)(C), provide information related to the required elements of grant applications to aid nonprofit organizations, including faith-based organizations, and houses of worship in meeting the eligibility criteria for Federal grants; and\n**(E)**\nprovide answers to frequently asked questions regarding the implementation of best practices and recommendations of the Clearinghouse and best practices for applying for a grant identified under subsection (a)(2)(C).\n**(2) Provision of information relating to Federal grants and resources**\nEach Federal agency notified under subsection (b) shall provide to the Secretary or other appropriate point of contact for the Clearinghouse for inclusion in the Clearinghouse necessary information regarding any Federal grant programs or resources of the Federal agency that are available for nonprofit organizations, including faith-based organizations, and houses of worship.\n**(3) State grants and resources**\n**(A) In general**\nAny State notified under subsection (b) may provide to the Secretary or other appropriate point of contact for the Clearinghouse for inclusion in the Clearinghouse necessary information regarding any grant programs or resources of the State available for nonprofit organizations, including faith-based organizations, and houses of worship for the purposes of safety and security.\n**(B) Identification of resources**\nThe Clearinghouse shall, to the extent practicable, identify for each State the following:\n**(i)**\nEach State agency responsible for safety and security of nonprofit organizations, including faith-based organizations, and houses of worship in the State, or any State that does not have such an agency designated.\n**(ii)**\nAny grant program that may be used for the purposes of implementing best practices and recommendations of the Clearinghouse.\n**(iii)**\nAny resources or programs, including community prevention or intervention efforts, that may be used to assist in targeted violence and terrorism prevention.\n##### (d) Other resources\nThe Secretary shall, on the website of the Clearinghouse, include a separate section for other resources that shall provide a centralized list of all available points of contact from which a nonprofit organization, including a faith-based organization, or a house of worship may seek assistance in grant applications and in carrying out the best practices and recommendations of the Clearinghouse, including the following:\n**(1)**\nA list of contact information to reach Department personnel to assist with grant-related questions.\n**(2)**\nThe applicable Agency contact information to connect houses of worship with Protective Security Advisors.\n**(3)**\nContact information for all Department Fusion Centers, listed by State.\n**(4)**\nInformation on the If you See Something Say Something Campaign of the Department.\n**(5)**\nAny other appropriate contacts.\n##### (e) Rule of construction\nNothing in this section may be construed to create, satisfy, or waive any requirement under Federal civil rights laws, including\u2014\n**(1)**\ntitle II of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12131 et seq. ); or\n**(2)**\ntitle VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ).\n##### (f) Sunset\nThis Act shall cease to be effective on the date that is 4 years after the date of enactment of this Act.\n#### 4. GAO report\nThe Comptroller General of the United States shall submit to Congress a report on the state of Federal grants devoted to safety and security for nonprofit organizations, including faith-based organizations, and houses of worship, and an evaluation of the relevant programs and resources devoted to the safety and security of nonprofit organizations, including faith-based organizations, and houses of worship as of the date of the report.",
      "versionDate": "2025-09-30",
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
        "actionDate": "2025-09-30",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2947",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Pray Safe Act of 2025",
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
        "name": "Emergency Management",
        "updateDate": "2025-12-05T21:47:00Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5645ih.xml"
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
      "title": "Pray Safe Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-26T05:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pray Safe Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-26T05:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a Federal Clearinghouse on Safety and Best Practices for Nonprofit Organizations, Faith-based Organizations, and Houses of Worship within the Department of Homeland Security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-26T05:33:23Z"
    }
  ]
}
```
