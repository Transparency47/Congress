# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/833?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/833
- Title: Educational Choice for Children Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 833
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-12-05T21:33:57Z
- Update date including text: 2025-12-05T21:33:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/833",
    "number": "833",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001172",
        "district": "3",
        "firstName": "Adrian",
        "fullName": "Rep. Smith, Adrian [R-NE-3]",
        "lastName": "Smith",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Educational Choice for Children Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:33:57Z",
    "updateDateIncludingText": "2025-12-05T21:33:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-31T15:05:00Z",
          "name": "Referred To"
        }
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
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "UT"
    },
    {
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Walberg",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "PA"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "IN"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "LA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "IA"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "UT"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "IA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "OK"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "OH"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NC"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "SC"
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
      "sponsorshipDate": "2025-01-31",
      "state": "TN"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "GA"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NC"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "VA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "PA"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "SC"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "IA"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "TN"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "MN"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "KS"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "MI"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "WI"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
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
      "sponsorshipDate": "2025-02-14",
      "state": "MN"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "SC"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "PA"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "WA"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
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
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "SC"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "IN"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "GA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "CO"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "IL"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "IL"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "KY"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "OK"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NJ"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NC"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "GA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "OH"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "OH"
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
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
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
      "sponsorshipDate": "2025-04-09",
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
      "sponsorshipDate": "2025-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "MI"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "CO"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "TX"
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
      "sponsorshipDate": "2025-04-29",
      "state": "WI"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "MT"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "AZ"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "TX"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "KY"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "MO"
    },
    {
      "bioguideId": "J000289",
      "district": "4",
      "firstName": "Jim",
      "fullName": "Rep. Jordan, Jim [R-OH-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Jordan",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "OH"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "FL"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MO"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "IN"
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
      "sponsorshipDate": "2025-05-20",
      "state": "AR"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-06-13",
      "state": "FL"
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
      "sponsorshipDate": "2025-07-02",
      "state": "AL"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "MO"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr833ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 833\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Smith of Nebraska (for himself, Mr. Owens , Mr. Walberg , Mr. Kelly of Pennsylvania , Mr. Yakym , Mr. LaHood , Ms. Letlow , Mrs. Miller-Meeks , Mr. Donalds , Ms. Tenney , Mr. Moore of Utah , Mr. Feenstra , Ms. Malliotakis , Mr. Hern of Oklahoma , Mr. Lawler , Mr. Fong , Mr. Carey , Mr. Hudson , Ms. Salazar , Mr. Scott Franklin of Florida , Mr. Crenshaw , Mr. Wilson of South Carolina , Mr. Rose , Mr. Weber of Texas , Mr. Ciscomani , Mr. Moolenaar , Mr. Allen , Mr. Dunn of Florida , Mr. Murphy , Mr. Cline , Mr. Meuser , Mr. Timmons , and Mr. Bergman ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a credit against tax for charitable donations to nonprofit organizations providing education scholarships to qualified elementary and secondary students.\n#### 1. Short title\nThis Act may be cited as the Educational Choice for Children Act of 2025 .\n#### 2. Tax credit for contributions to scholarship granting organizations\n##### (a) Credit for individuals\n**(1) In general**\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25E the following new section:\n25F. Qualified elementary and secondary education scholarships (a) Allowance of credit In the case of an individual who is a citizen or resident of the United States (as defined in section 7701(a)(9)), there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the aggregate amount of qualified contributions made by the taxpayer during the taxable year. (b) Limitations (1) In general The credit allowed under subsection (a) to any taxpayer for any taxable year shall not exceed an amount equal to the greater of\u2014 (A) 10 percent of the adjusted gross income of the taxpayer for the taxable year, or (B) $5,000. (2) Allocation of volume cap The credit allowed under subsection (a) to any taxpayer for any taxable year shall not exceed the amount of the volume cap allocated by the Secretary to such taxpayer under section 3 of the Educational Choice for Children Act of 2025 with respect to qualified contributions made by the taxpayer during the taxable year. (3) Reduction based on State credit The amount allowed as a credit under subsection (a) for a taxable year shall be reduced by the amount allowed as a credit on any State tax return of the taxpayer for qualified contributions made by the taxpayer during the taxable year. (c) Definitions For purposes of this section\u2014 (1) Eligible student The term eligible student means an individual who\u2014 (A) is a member of a household with an income which is not greater than 300 percent of the area median gross income (as such term is used in section 42), and (B) is eligible to enroll in a public elementary or secondary school. (2) Qualified contribution The term qualified contribution means a charitable contribution (as defined by section 170(c)) to a scholarship granting organization in the form of cash or marketable securities. (3) Qualified elementary or secondary education expense The term qualified elementary or secondary education expense means the following expenses in connection with enrollment or attendance at, or for students enrolled at or attending, a public or private elementary or secondary school (including a religious elementary or secondary school): (A) Tuition. (B) Curricula and curricular materials. (C) Books or other instructional materials. (D) Online educational materials. (E) Tuition for tutoring or educational classes outside of the home, including at a tutoring facility, but only if the tutor or instructor is not related to the student and\u2014 (i) is licensed as a teacher in any State, (ii) has taught at\u2014 (I) a public or private elementary or secondary school, or (II) an institution of higher education (as defined in section 101(a) of the Higher Education Act ( 20 U.S.C. 1001(a) ), or (iii) is a subject matter expert in the relevant subject. (F) Fees for a nationally standardized norm-referenced achievement test, an advanced placement examination, or any examinations related to admission to an institution of higher education. (G) Fees for dual enrollment in an institution of higher education. (H) Educational therapies for students with disabilities provided by a licensed or accredited practitioner or provider, including occupational, behavioral, physical, and speech-language therapies. Such term shall include expenses for the purposes described in subparagraphs (A) through (H) in connection with a home school (whether treated as a home school or a private school for purposes of applicable State law). (4) Scholarship granting organization The term scholarship granting organization means any organization\u2014 (A) which\u2014 (i) is described in section 501(c)(3) and exempt from tax under section 501(a), and (ii) is not a private foundation, (B) substantially all of the activities of which are providing scholarships for qualified elementary or secondary education expenses of eligible students, (C) which prevents the co-mingling of qualified contributions with other amounts by maintaining one or more separate accounts exclusively for qualified contributions, and (D) which either\u2014 (i) meets the requirements of subsection (d), or (ii) pursuant to State law, was able (as of the date of the enactment of this section) to receive contributions that are eligible for a State tax credit if such contributions are used by the organization to provide scholarships to individual elementary and secondary students, including scholarships for attending private schools. (d) Requirements for scholarship granting organizations (1) In general An organization meets the requirements of this subsection if\u2014 (A) such organization provides scholarships to 2 or more students, provided that not all such students attend the same school, (B) such organization does not provide scholarships for any expenses other than qualified elementary or secondary education expenses, (C) such organization provides a scholarship to eligible students with a priority for\u2014 (i) students awarded a scholarship the previous school year, and (ii) after application of clause (i), any such students who have a sibling who was awarded a scholarship from such organization, (D) such organization does not earmark or set aside contributions for scholarships on behalf of any particular student, (E) such organization takes appropriate steps to verify the annual household income and family size of eligible students to whom it awards scholarships, and limits them to a member of a household for which the income does not exceed the amount established under subsection (c)(1)(A), (F) such organization\u2014 (i) obtains from an independent certified public accountant annual financial and compliance audits, and (ii) certifies to the Secretary (at such time, and in such form and manner, as the Secretary may prescribe) that the audit described in clause (i) has been completed, and (G) no officer or board member of such organization has been convicted of a felony. (2) Income verification For purposes of paragraph (1)(E), review of all of the following (as applicable) shall be treated as satisfying the requirement to take appropriate steps to verify annual household income: (A) Federal and State income tax returns or tax return transcripts with applicable schedules for the taxable year prior to application. (B) Income reporting statements for tax purposes or wage and income transcripts from the Internal Revenue Service. (C) Notarized income verification letter from employers. (D) Unemployment or workers compensation statements. (E) Budget letters regarding public assistance payments and Supplemental Nutrition Assistance Program (SNAP) payments including a list of household members. (3) Independent certified public accountant For purposes of paragraph (1)(F), the term independent certified public accountant means, with respect to an organization, a certified public accountant who is not a person described in section 465(b)(3)(A) with respect to such organization or any employee of such organization. (4) Prohibition on self-dealing (A) In general A scholarship granting organization may not award a scholarship to any disqualified person. (B) Disqualified person For purposes of this paragraph, a disqualified person shall be determined pursuant to rules similar to the rules of section 4946. (e) Denial of double benefit Any qualified contribution for which a credit is allowed under this section shall not be taken into account as a charitable contribution for purposes of section 170. (f) Carryforward of unused credit (1) In general If the credit allowable under subsection (a) for any taxable year exceeds the limitation imposed by section 26(a) for such taxable year reduced by the sum of the credits allowable under this subpart (other than this section, section 23, and section 25D), such excess shall be carried to the succeeding taxable year and added to the credit allowable under subsection (a) for such taxable year. (2) Limitation No credit may be carried forward under this subsection to any taxable year following the fifth taxable year after the taxable year in which the credit arose. For purposes of the preceding sentence, credits shall be treated as used on a first-in first-out basis. .\n**(2) Conforming amendments**\n**(A)**\nSection 25(e)(1)(C) of such Code is amended by striking and 25D and inserting 25D, and 25F .\n**(B)**\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 25E the following new item:\nSec. 25F. Qualified elementary and secondary education scholarships. .\n##### (b) Credit for corporations\n**(1) In general**\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding after section 45AA the following:\n45BB. Contributions to scholarship granting organizations (a) General rule For purposes of section 38, in the case of a corporation, the education scholarship credit determined under this section for the taxable year is the aggregate amount of qualified contributions for the taxable year. (b) Amount of credit The credit allowed under subsection (a) for any taxable year shall not exceed 5 percent of the taxable income (as defined in section 170(b)(2)(D)) of the corporation for such taxable year. (c) Qualified contributions For purposes of this section, the term qualified contribution has the meaning given such term under section 25F. (d) Denial of double benefit No deduction shall be allowed under any provision of this chapter for any expense for which a credit is allowed under this section. (e) Application of volume cap A qualified contribution shall be taken into account under this section only if such contribution is not in excess of the volume cap established under section 3 of the Educational Choice for Children Act of 2025 . .\n**(2) Conforming amendments**\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period and inserting , plus at the end of paragraph (41), and by adding at the end the following new paragraph:\n(42) the education scholarship credit determined under section 45BB(a). .\n**(3) Clerical amendment**\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Contributions to scholarship granting organizations. .\n##### (c) Failure of scholarship granting organizations To make distributions\n**(1) In general**\nChapter 42 of such Code is amended by adding at the end the following new subchapter:\nI Scholarship Granting Organizations Sec. 4969. Failure to distribute receipts. 4969. Failure to distribute receipts (a) In general In the case of any scholarship granting organization (as defined in section 25F) which has been determined by the Secretary to have failed to satisfy the requirement under subsection (b) for any taxable year, any contribution made to such organization during the first taxable year beginning after the date of such determination shall not be treated as a qualified contribution (as defined in section 25F(c)(2)) for purposes of sections 25F and 45BB. (b) Requirement The requirement described in this subsection is that the amount of receipts of the scholarship granting organization for the taxable year which are distributed before the distribution deadline with respect to such receipts shall not be less than the required distribution amount with respect to such taxable year. (c) Definitions For purposes of this section\u2014 (1) Required distribution amount (A) In general The required distribution amount with respect to a taxable year is the amount equal to 100 percent of the total receipts of the scholarship granting organization for such taxable year\u2014 (i) reduced by the sum of such receipts that are retained for reasonable administrative expenses for the taxable year or are carried to the succeeding taxable year under subparagraph (C), and (ii) increased by the amount of the carryover under subparagraph (C) from the preceding taxable year. (B) Safe harbor for reasonable administrative expenses For purposes of subparagraph (A)(i), if the percentage of total receipts of a scholarship granting organization for a taxable year which are used for administrative purposes is equal to or less than 10 percent, such expenses shall be deemed to be reasonable for purposes of such subparagraph. (C) Carryover With respect to the amount of the total receipts of a scholarship granting organization with respect to any taxable year, an amount not greater than 15 percent of such amount may, at the election of such organization, be carried to the succeeding taxable year. (2) Distributions The term distribution includes amounts which are formally committed but not distributed. A formal commitment described in the preceding sentence may include contributions set aside for eligible students for more than one year. (3) Distribution deadline The distribution deadline with respect to receipts for a taxable year is the first day of the third taxable year following the taxable year in which such receipts are received by the scholarship granting organization. .\n**(2) Clerical amendment**\nThe table of subchapters for chapter 42 of such Code is amended by adding at the end the following new item:\nSubchapter I. Scholarship Granting Organizations .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years ending after December 31, 2025.\n#### 3. Volume cap\n##### (a) In general\nFor purposes of sections 25F(b)(2) and 45BB(e) of the Internal Revenue Code of 1986 (as added by this Act), the volume cap applicable under this section shall be $10,000,000,000 for calendar year 2026 and each subsequent year thereafter. Such amount shall be allocated by the Secretary as provided in subsection (b) to taxpayers with respect to qualified contributions made by such taxpayers, except that 10 percent of such amount shall be divided evenly among the States, and shall be available with respect to\u2014\n**(1)**\nindividuals residing in such States to claim the credit allowed under section 25F of the Internal Revenue Code of 1986, and\n**(2)**\ncorporations created or organized in such State to claim the credit determined under section 45BB of such Code.\n##### (b) First-Come, first-Serve\nFor purposes of applying the volume cap under this section, such volume cap for any calendar year shall be allocated by the Secretary on a first-come, first-serve basis, as determined based on the time (during such calendar year) at which the taxpayer made the qualified contribution with respect to which the allocation is made. The Secretary shall not make any allocation of volume cap for any calendar year after December 31 of such calendar year.\n##### (c) Real-Time information\nFor purposes of this section, the Secretary shall develop a system to track the amount of qualified contributions made during the calendar year for which a credit may be claimed under section 25F or 45BB of the Internal Revenue Code of 1986, with such information to be updated in real time.\n##### (d) Annual increases\n**(1) In general**\nIn the case of the calendar year after a high use calendar year, the dollar amount otherwise in effect under subsection (a) for such calendar year shall be equal to 105 percent of the dollar amount in effect for such high use calendar year.\n**(2) High use calendar year**\nFor purposes of this subsection, the term high use calendar year means any calendar year for which 90 percent or more of the volume cap in effect for such calendar year under subsection (a) is allocated to taxpayers.\n**(3) Prevention of decreases in annual volume cap**\nThe volume cap in effect under subsection (a) for any calendar year shall not be less than the volume cap in effect under such subsection for the preceding calendar year.\n**(4) Publication of annual volume cap**\nThe Secretary shall make publicly available the dollar amount of the volume cap in effect under subsection (a) for each calendar year.\n##### (e) States\nFor purposes of this section, the term State includes the District of Columbia.\n#### 4. Exemption from gross income for scholarships for qualified elementary or secondary education expenses of eligible students\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 140 the following new section:\n139J. Scholarships for qualified elementary or secondary education expenses of eligible students (a) In general In the case of an individual, gross income shall not include any amounts provided to any dependent of such individual pursuant to a scholarship for qualified elementary or secondary education expenses of an eligible student which is provided by a scholarship granting organization. (b) Definitions In this section, the terms qualified elementary or secondary education expense , eligible student , and scholarship granting organization have the same meaning given such terms under section 25F(c). .\n##### (b) Conforming amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before the item relating to section 140 the following new item:\nSec. 139J. Scholarships for qualified elementary or secondary education expenses of eligible students. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts received after December 31, 2025, in taxable years ending after such date.\n#### 5. Organizational and parental autonomy\n##### (a) Prohibition of control over scholarship organizations\n**(1) In general**\n**(A) Treatment**\nA scholarship granting organization shall not, by virtue of participation under any provision of this Act or any amendment made by this Act, be regarded as acting on behalf of any governmental entity.\n**(B) No governmental control**\nNothing in this Act, or any amendment made by this Act, shall be construed to permit, allow, encourage, or authorize any Federal, State, or local government entity, or officer or employee thereof, to mandate, direct, or control any aspect of any scholarship granting organization.\n**(C) Maximum freedom**\nTo the extent permissible by law, this Act, and any amendment made by this Act, shall be construed to allow scholarship granting organizations maximum freedom to provide for the needs of the participants without governmental control.\n**(2) Prohibition of control over non-public schools**\n**(A) No governmental control**\nNothing in this Act, or any amendment made by this Act, shall be construed to permit, allow, encourage, or authorize any Federal, State, or local government entity, or officer or employee thereof, to mandate, direct, or control any aspect of any private or religious elementary or secondary education institution.\n**(B) No exclusion of private or religious schools**\nNo Federal, State, or local government entity, or officer or employee thereof, shall impose or permit the imposition of any conditions or requirements that would exclude or operate to exclude educational expenses at private or religious elementary and secondary education institutions from being considered qualified elementary or secondary education expenses.\n**(C) No exclusion of qualified expenses due to institution's religious character or affiliation**\nNo Federal, State, or local government entity, or officer or employee thereof, shall exclude, discriminate against, or otherwise disadvantage any elementary or secondary education institution with respect to qualified elementary or secondary education expenses at that institution based in whole or in part on the institution\u2019s religious character or affiliation, including religiously based or mission-based policies or practices.\n**(3) Parental rights to use scholarships**\nNo Federal, State, or local government entity, or officer or employee thereof, shall disfavor or discourage the use of scholarships granted by participating scholarship granting organizations for qualified elementary or secondary education expenses at private or nonprofit elementary and secondary education institutions, including faith-based schools.\n**(4) Parental right to intervene**\nIn any action filed in any State or Federal court which challenges the constitutionality (under the constitution of such State or the Constitution of the United States) of any provision of this Act (or any amendment made by this Act), any parent of an eligible student who has received a scholarship from a scholarship granting organization shall have the right to intervene in support of the constitutionality of such provision or amendment. To avoid duplication of efforts and reduce the burdens placed on the parties to the action, the court in any such action may require interveners taking similar positions to file joint papers or to be represented by a single attorney at oral argument, provided that the court does not require such interveners to join any brief filed on behalf of any State which is a defendant in such action.\n##### (b) Definitions\nFor purposes of this section, the terms eligible student , scholarship granting organization , and qualified elementary or secondary education expense shall have the same meanings given such terms under section 25F(c) of the Internal Revenue Code of 1986 (as added by section 2(a) of this Act).",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "817",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to allow a credit against tax for charitable donations to nonprofit organizations providing education scholarships to qualified elementary and secondary students.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-29",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "292",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Educational Choice for Children Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-04-14T19:44:07Z"
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
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr833ih.xml"
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
      "title": "Educational Choice for Children Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Educational Choice for Children Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow a credit against tax for charitable donations to nonprofit organizations providing education scholarships to qualified elementary and secondary students.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T05:18:31Z"
    }
  ]
}
```
