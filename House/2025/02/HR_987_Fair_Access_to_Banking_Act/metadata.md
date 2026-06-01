# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/987?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/987
- Title: Fair Access to Banking Act
- Congress: 119
- Bill type: HR
- Bill number: 987
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2026-05-21T08:07:53Z
- Update date including text: 2026-05-21T08:07:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/987",
    "number": "987",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Fair Access to Banking Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:53Z",
    "updateDateIncludingText": "2026-05-21T08:07:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "GA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "TX"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "WI"
    },
    {
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NC"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "LA"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "AL"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
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
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "KS"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "GA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "MN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "NY"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "AL"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "IN"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "MO"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TN"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NV"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NE"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "AL"
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
      "sponsorshipDate": "2025-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MT"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "CO"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "GA"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "MO"
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
      "sponsorshipDate": "2025-02-24",
      "state": "FL"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "MI"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "TX"
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
      "sponsorshipDate": "2025-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "KS"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
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
      "sponsorshipDate": "2025-02-24",
      "state": "GA"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MD"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "IL"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NC"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IN"
    },
    {
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "KY"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "TN"
    },
    {
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Walberg",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "MI"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "FL"
    },
    {
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "OK"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "VA"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MI"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "WA"
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
      "sponsorshipDate": "2025-04-10",
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
      "sponsorshipDate": "2025-04-10",
      "state": "TX"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "WI"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "UT"
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
      "sponsorshipDate": "2025-05-05",
      "state": "FL"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "SC"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "FL"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "SC"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "MO"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "FL"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "IA"
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
      "sponsorshipDate": "2025-06-05",
      "state": "WV"
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
      "sponsorshipDate": "2025-06-05",
      "state": "MI"
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
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
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
      "sponsorshipDate": "2025-06-05",
      "state": "UT"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TN"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "TX"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "ID"
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
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "IA"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "FL"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "SC"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "CO"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "NC"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "TN"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "SC"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "WI"
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
      "sponsorshipDate": "2025-09-15",
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
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "MN"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "False",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "CA"
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
      "sponsorshipDate": "2025-11-20",
      "state": "AZ"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "ID"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "GA"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "GA"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "OH"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "LA"
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
      "sponsorshipDate": "2026-04-30",
      "state": "OH"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr987ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 987\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Barr (for himself, Mr. Meuser , Mr. Scott Franklin of Florida , Mr. Clyde , and Mr. Harrigan ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend certain banking laws to prohibit certain financial service providers who deny fair access to financial services from using taxpayer funded discount window lending programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Access to Banking Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\narticle I of the Constitution of the United States guarantees the people of the United States the right to enact public policy through the free and fair election of representatives and through the actions of State legislatures and Congress;\n**(2)**\nfinancial institutions rightly objected to the Operation Choke Point initiative through which certain government agencies pressured financial institutions to cut off access to financial services to lawful sectors of the economy;\n**(3)**\nin response to pressure from advocates whose policy objectives are served when financial institutions deny certain customers access to financial services, financial institutions are now, however, increasingly employing subjective, category-based evaluations to deny certain persons access to financial services;\n**(4)**\nthis privatization of the discriminatory practices underlying Operation Choke Point by financial institutions represents as great a threat to the national economy, national security, and the soundness of banking and financial markets in the United States as Operation Choke Point itself;\n**(5)**\nfinancial institutions are supported by the United States taxpayers and enjoy significant privileges in the financial system of the United States and should not be permitted to act as de facto regulators or unelected legislators by withholding financial services to otherwise credit worthy businesses based on subjective political reasons, bias or prejudices;\n**(6)**\nfinancial institutions are not well-equipped to balance risks unrelated to financial exposures and the operations required to deliver financial services;\n**(7)**\nthe United States taxpayers came to the aid for large financial institutions during the great recession of 2008 because they were deemed too important to the national economy to be permitted to fail;\n**(8)**\nwhen a financial institution predicates the access to financial services of a person on factors or information (such as the lawful products a customer manufactures or sells or the services the customer provides) other than quantitative, impartial risk-based standards, the financial institution has failed to act consistent with basic principles of sound risk management and failed to provide fair access to financial services;\n**(9)**\nfinancial institutions have a responsibility to make decisions about whether to provide a person with financial services on the basis of impartial criteria free from prejudice or favoritism;\n**(10)**\nwhile fair access to financial services does not obligate a financial institution to offer any particular financial service to the public, or to operate in any particular geographic area, or to provide a service the financial institution offers to any particular person, it is necessary that\u2014\n**(A)**\nthe financial services a financial institution chooses to offer in the geographic areas in which the financial institution operates be made available to all customers based on the quantitative, impartial risk-based standards of the financial institution, and not based on whether the customer is in a particular category of customers;\n**(B)**\nfinancial institutions assess the risks posed by individual customers on a case-by-case basis, rather than category-based assessment; and\n**(C)**\nfinancial institutions implement controls to manage relationships commensurate with these risks associated with each customer, not a strategy of total avoidance of particular industries or categories of customers;\n**(11)**\nfinancial institutions are free to provide or deny financial services to any individual customer, but first, the financial institutions must rely on empirical data that are evaluated consistent with the established, impartial risk-management standards of the financial institution; and\n**(12)**\nanything less is not prudent risk management and may result in unsafe or unsound practices, denial of fair access to financial services, cancelling, or eliminating certain businesses in society, and have a deleterious effect on national security and the national economy.\n#### 3. Purpose\nThe purposes of this Act are to\u2014\n**(1)**\nensure fair access to financial services and fair treatment of customers by financial service providers, including national and State banks, Federal savings associations, and State and Federal credit unions;\n**(2)**\nensure financial institutions conduct themselves in a safe and sound manner, comply with laws and regulations, treat their customers fairly, and provide fair access to financial services;\n**(3)**\nprotect against financial institutions being able to impede otherwise lawful commerce and thereby achieve certain public policy goals;\n**(4)**\nensure that persons involved in politically unpopular businesses but that are lawful under Federal law receive fair access to financial services under the law; and\n**(5)**\nensure financial institutions operate in a safe and sound manner by making judgments and decisions about whether to provide a customer with financial services on an impartial, individualized risk-based analysis using empirical data evaluated under quantifiable standards.\n#### 4. Advances to individual member banks\n##### (a) Member banks\nSection 10B of the Federal Reserve Act ( 12 U.S.C. 347b ) is amended by adding at the end the following:\n(c) Prohibition on use of discount window lending programs No member bank with more than $50,000,000,000 in total consolidated assets, or subsidiary of the member bank, may use a discount window lending program if the member bank or subsidiary refuses to do business with any person who is in compliance with the law, including section 8 of the Fair Access to Banking Act . .\n##### (b) Insured depository institutions\nSection 8(a)(2)(A) of the Federal Deposit Insurance Act ( 12 U.S.C. 1818(a)(2)(A) ) is amended\u2014\n**(1)**\nin clause (ii), by striking or at the end;\n**(2)**\nin clause (iii), by striking the comma at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(iv) an insured depository institution with more than $500,000,000,000 in total consolidated assets, or subsidiary of the insured depository institution, that refuses to do business with any person who is in compliance with the law, including section 8 of the Fair Access to Banking Act . .\n##### (c) Nonmember banks, trust companies, and other depository institutions\nSection 13 of the Federal Reserve Act ( 12 U.S.C. 342 ) is amended by inserting Provided further , That no such nonmember bank or trust company or other depository institution with more than $50,000,000,000 in total consolidated assets, or subsidiary of such nonmember bank or trust company or other depository institution, may refuse to do business with any person who is in compliance with the law, including, including section 8 of the Fair Access to Banking Act : after appropriate: .\n#### 5. Payment card networks\n##### (a) Definition\nIn this section, the term payment card network has the meaning given the term in section 921(c) of the Electronic Fund Transfer Act ( 15 U.S.C. 1693o\u20132(c) ).\n##### (b) Prohibition\nNo payment card network, including a subsidiary of a payment card network, may, directly or through any agent, processor, or licensed member of the network, by contract, requirement, condition, penalty, or otherwise, prohibit or inhibit the ability of any person who is in compliance with the law, including section 8 of this Act, to obtain access to services or products of the payment card network because of political or reputational risk considerations.\n##### (c) Civil penalty\nAny payment card network that violates subsection (b) shall be assessed a civil penalty by the Comptroller of the Currency of not more than 10 percent of the value of the services or products described in that subsection, not to exceed $10,000 per violation.\n#### 6. Credit unions\nSection 206(b)(1) of the Federal Credit Union Act ( 12 U.S.C. 1786 ) is amended by inserting or is refusing or has refused, or has a subsidiary that is refusing or has refused, to do business with any person who is in compliance with the law, including section 8 of the Fair Access to Banking Act , after as an insured credit union, .\n#### 7. Use of automated clearing house network\n##### (a) Definitions\nIn this section:\n**(1) Covered credit union**\nThe term covered credit union means\u2014\n**(A)**\nany insured credit union, as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ); or\n**(B)**\nany credit union that is eligible to make application to become an insured credit union under section 201 of the Federal Credit Union Act ( 12 U.S.C. 1781 ).\n**(2) Member bank**\nThe term member bank has the meaning given the term in the third undesignated paragraph of the first section of the Federal Reserve Act ( 12 U.S.C. 221 ).\n##### (b) Prohibition\nNo covered credit union, member bank, or State-chartered non-member bank with more than $50,000,000,000 in total consolidated assets, or a subsidiary of the covered credit union, member bank, or State-chartered non-member bank, may use the Automated Clearing House Network if that member bank, credit union, or subsidiary of the member bank or credit union, refuses to do business with any person who is in compliance with the law, including section 8 of this Act.\n#### 8. Fair access to financial services\n##### (a) Definitions\nIn this section:\n**(1) Bank**\nThe term bank \u2014\n**(A)**\nmeans an entity for which the Office of the Comptroller of the Currency is the appropriate Federal banking agency, as defined in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nincludes\u2014\n**(i)**\nmember banks;\n**(ii)**\nnon-member banks;\n**(iii)**\ncovered credit unions;\n**(iv)**\nState-chartered non-member banks; and\n**(v)**\ntrust companies.\n**(2) Covered bank**\n**(A) In general**\nThe term covered bank means a bank that has the ability to\u2014\n**(i)**\nraise the price a person has to pay to obtain an offered financial service from the bank or from a competitor; or\n**(ii)**\nsignificantly impede a person, or the business activities of a person, in favor of or to the advantage of another person.\n**(B) Presumption**\n**(i) In general**\nA bank shall not be presumed to be a covered bank if the bank has less than $50,000,000,000 in total assets.\n**(ii) Rebuttable presumption**\n**(I) In general**\nA bank is presumed to be a covered bank if the bank has $50,000,000,000 or more in total assets.\n**(II) Rebuttal**\nA bank that meets the criteria under subclause (I) can seek to rebut this presumption by submitting to the Office of the Comptroller of the Currency written materials that, in the judgement of the agency, demonstrate the bank does not meet the definition of covered bank.\n**(3) Covered credit union**\nThe term covered credit union means\u2014\n**(A)**\nany insured credit union, as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ); or\n**(B)**\nany credit union that is eligible to make application to become an insured credit union under section 201 of the Federal Credit Union Act ( 12 U.S.C. 1781 ).\n**(4) Deny**\nThe term deny means to deny or refuse to enter into or terminate an existing financial services relationship with a person.\n**(5) Fair access to financial services**\nThe term fair access to financial services means persons engaged in activities lawful under Federal law are able to obtain financial services at banks without impediments caused by a prejudice against or dislike for a person or the business of the customer, products or services sold by the person, or favoritism for market alternatives to the business of the person. Refusing to provide or continue to provide financial services to a person because the person engaged in rude or harassing conduct toward an employee of a bank is not a violation of this section.\n**(6) Financial service**\nThe term financial service means a financial product or service, including\u2014\n**(A)**\ncommercial and merchant banking;\n**(B)**\nlending;\n**(C)**\nfinancing;\n**(D)**\nleasing;\n**(E)**\ncash, asset and investment management and advisory services;\n**(F)**\ncredit card services;\n**(G)**\npayment processing;\n**(H)**\nsecurity and foreign exchange trading and brokerage services; and\n**(I)**\ninsurance products.\n**(7) Member bank**\nThe term member bank has the meaning given the term in the third undesignated paragraph of the first section of the Federal Reserve Act ( 12 U.S.C. 221 ).\n##### (b) Requirements\n**(1) In general**\nTo provide fair access to financial services, a covered bank (including a subsidiary of a covered bank), except as necessary to comply with another provision of law\u2014\n**(A)**\nshall make each financial service it offers available to all persons in the geographic market served by the covered bank on proportionally equal terms;\n**(B)**\nmay not deny any person a financial service the covered bank offers unless the denial is justified by such quantified and documented failure of the person to meet quantitative, impartial risk-based standards established in advance by the covered bank;\n**(C)**\nmay not deny, in coordination with or at the request of others, any person a financial service the covered bank offers; and\n**(D)**\nshall, when denying any person financial services the covered bank offers, provide written justification to the person explaining the basis for the denial, including any specific laws or regulations the covered bank believes are being violated by the person or customer, if any.\n**(2) Justification requirement**\nA justification described in paragraph (1)(D) may not be based solely on the reputational risk to the covered bank.\n##### (c) Cause of action for violations of this section\n**(1) In general**\nNotwithstanding any other provision of law, a person may commence a civil action in the appropriate district court of the United States against any covered bank that violates or fails to comply with the requirements under this Act, for harm that person suffered as a result of such violation.\n**(2) No exhaustion**\nIt shall not be necessary for a person to exhaust its administrative remedies before commencing a civil action under this Act.\n**(3) Damages**\nIf a person prevails in a civil action under this Act, a court shall award the person\u2014\n**(A)**\nreasonable attorney\u2019s fees and costs; and\n**(B)**\ntreble damages.",
      "versionDate": "2025-02-05",
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
        "actionDate": "2025-02-04",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "401",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fair Access to Banking Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-07T16:06:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119hr987",
          "measure-number": "987",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-05",
          "originChamber": "HOUSE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr987v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fair Access to Banking Act </strong></p><p>This bill places restrictions on certain banks, credit unions, and payment card networks if they refuse to do business with a person who complies with the law. Restrictions include prohibiting the use of electronic funds transfer systems and lending programs, termination of an institution's depository insurance, and specified civil penalties.</p><p>Banks and other specified financial institutions are allowed to deny financial services to a person only if the denial is justified by a documented failure of that person to meet quantitative, impartial, risk-based standards established in advance by the institution. This justification may not be based upon reputational risks to the institution.</p><p>The bill establishes the right for a person to bring a civil action for a violation of this bill.</p>"
        },
        "title": "Fair Access to Banking Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr987.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Access to Banking Act </strong></p><p>This bill places restrictions on certain banks, credit unions, and payment card networks if they refuse to do business with a person who complies with the law. Restrictions include prohibiting the use of electronic funds transfer systems and lending programs, termination of an institution's depository insurance, and specified civil penalties.</p><p>Banks and other specified financial institutions are allowed to deny financial services to a person only if the denial is justified by a documented failure of that person to meet quantitative, impartial, risk-based standards established in advance by the institution. This justification may not be based upon reputational risks to the institution.</p><p>The bill establishes the right for a person to bring a civil action for a violation of this bill.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr987"
    },
    "title": "Fair Access to Banking Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Access to Banking Act </strong></p><p>This bill places restrictions on certain banks, credit unions, and payment card networks if they refuse to do business with a person who complies with the law. Restrictions include prohibiting the use of electronic funds transfer systems and lending programs, termination of an institution's depository insurance, and specified civil penalties.</p><p>Banks and other specified financial institutions are allowed to deny financial services to a person only if the denial is justified by a documented failure of that person to meet quantitative, impartial, risk-based standards established in advance by the institution. This justification may not be based upon reputational risks to the institution.</p><p>The bill establishes the right for a person to bring a civil action for a violation of this bill.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr987"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr987ih.xml"
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
      "title": "Fair Access to Banking Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Access to Banking Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend certain banking laws to prohibit certain financial service providers who deny fair access to financial services from using taxpayer funded discount window lending programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:18:33Z"
    }
  ]
}
```
