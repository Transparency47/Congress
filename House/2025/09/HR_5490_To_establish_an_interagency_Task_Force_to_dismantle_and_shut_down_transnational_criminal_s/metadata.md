# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5490?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5490
- Title: Dismantle Foreign Scam Syndicates Act
- Congress: 119
- Bill type: HR
- Bill number: 5490
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-05-20T08:08:39Z
- Update date including text: 2026-05-20T08:08:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-18 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 48 - 0.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-18 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 48 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5490",
    "number": "5490",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001229",
        "district": "6",
        "firstName": "Jefferson",
        "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
        "lastName": "Shreve",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Dismantle Foreign Scam Syndicates Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:39Z",
    "updateDateIncludingText": "2026-05-20T08:08:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 48 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
            "date": "2025-12-03T16:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-18T14:08:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-18T14:08:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MI"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "OH"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "IN"
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
      "sponsorshipDate": "2025-11-18",
      "state": "NC"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "GU"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "NJ"
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
      "sponsorshipDate": "2025-12-02",
      "state": "VA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-03",
      "state": "NJ"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "RI"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "DE"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "IN"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "OH"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "SC"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "WA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MD"
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
      "sponsorshipDate": "2025-12-15",
      "state": "NJ"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "CA"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "MO"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "MT"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "MN"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NV"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
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
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "FL"
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
      "sponsorshipDate": "2026-02-24",
      "state": "NV"
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
      "sponsorshipDate": "2026-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "IL"
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
      "sponsorshipDate": "2026-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "OK"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "IL"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MA"
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
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
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
      "sponsorshipDate": "2026-03-25",
      "state": "FL"
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
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
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
      "sponsorshipDate": "2026-04-06",
      "state": "IL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
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
      "sponsorshipDate": "2026-04-14",
      "state": "MI"
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
      "sponsorshipDate": "2026-04-21",
      "state": "VA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MA"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "TN"
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
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
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
      "sponsorshipDate": "2026-05-12",
      "state": "MA"
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
      "sponsorshipDate": "2026-05-12",
      "state": "DC"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5490ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5490\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Shreve (for himself, Mr. Moolenaar , and Mr. Rulli ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish an interagency Task Force to dismantle and shut down transnational criminal syndicates perpetuating mass online scam operations against Americans.\n#### 1. Short title\nThis Act may be cited as the Dismantle Foreign Scam Syndicates Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nDuring the COVID\u201319 pandemic, Chinese criminal organizations active in Southeast Asia pivoted to a new and potent form of financial scam involving elaborate fraudulent online cryptocurrency investment schemes.\n**(2)**\nThe most common form of such financial scam is known as pig butchering , Chinese criminal slang that describes how scammers develop a virtual relationship inducing them to invest ever larger sums into phony platforms, serving to \u2018fatten\u2019 their victims for the slaughter.\n**(3)**\nCrime syndicates use the forced labor of hundreds of thousands of victims of human trafficking to perpetrate such scams.\n**(4)**\nThese victims themselves fall prey to false job advertisements before they are taken to a compound and forced to meet aggressive scam quotas under pain of violent punishment if they refuse.\n**(5)**\nThese so-called scam centers are most prevalent across Burma, Laos, and Cambodia, corrupt and repressive countries where transparency is absent, rule of law is anemic and checks and balances are non-existent, and often operate as joint ventures between the Chinese criminal groups organizations and the autocratic governments.\n**(6)**\nSince 2021, these scams have increasingly targeted Americans, robbing thousands of their life savings and enriching and entrenching transnational criminal syndicates and corrupt leaders in Cambodia, Laos and Burma.\n**(7)**\nAmerican losses to these scams grew by 33 percent year-on-year in 2024.\n**(8)**\nAccording to the Department of Treasury, Americans lost at least $10,000,000,000 from these operations in 2024 alone.\n**(9)**\nGlobal losses are estimated to be higher than $60,000,000,000 annually.\n**(10)**\nThe true dollar amount of losses to these scams is estimated to be much higher as many instances go unreported.\n**(11)**\nTroubling links exist between the People\u2019s Republic of China, Chinese criminal scam syndicates, and the corrupt local politicians enabling their rise.\n#### 3. Statement of policy\nIt shall be the policy of the United States to comprehensively combat the transnational organized criminals operating human trafficking compounds primarily in Southeast Asia to perpetrate large-scale online scams against the American people.\n#### 4. Task Force\n##### (a) Establishment\nNot later than 30 days after the date of the enactment of this Act, the President shall establish an interagency Task Force responsible for leading a whole-of-government effort to dismantle and shut down transnational criminal syndicates perpetuating mass online scam operations against Americans through the operation of large-scale scam compounds fueled by the forced labor of victims of trafficking in persons.\n##### (b) Duties\nThe Task Force shall\u2014\n**(1)**\nnot later than 180 days after the date of the enactment of this Act, develop and submit to the appropriate congressional committees a comprehensive United States Government strategy to shut down online scam centers, prevent their further proliferation, disrupt and dismantle transnational criminal entities and human traffickers involved in operating such centers, and hold accountable corrupt officials, state, and non-state actors enabling such entities and traffickers for the purpose of incentivizing cooperation; and\n**(2)**\ncoordinate and oversee implementation of such strategy.\n##### (c) Leadership and composition\nThe Task Force shall\u2014\n**(1)**\nbe chaired by the Secretary of State (or the Secretary\u2019s designee);\n**(2)**\nmeet on a regular basis at the call of the Chair; and\n**(3)**\nbe comprised of the heads (or the heads\u2019 designees) of\u2014\n**(A)**\nthe Department of State, including the Bureau of International Narcotics and Law Enforcement Affairs, the Bureau of East Asian and Pacific Affairs, and the Office to Monitor and Combat Trafficking in Persons;\n**(B)**\nthe Department of Justice, including the Federal Bureau of Investigation;\n**(C)**\nthe Department of Homeland Security, including the U.S. Secret Service and Homeland Security Investigations; and\n**(D)**\nthe Department of the Treasury, including the Office of Terrorism and Financial Intelligence, the Office of Foreign Assets Control, and Financial Crimes Enforcement Network.\n##### (d) Further composition\nThe heads (or the heads\u2019 designees) of the following entities are authorized to be members of the Task Force:\n**(1)**\nThe U.S. Securities and Exchange Commission.\n**(2)**\nThe Federal Trade Commission.\n**(3)**\nThe Federal Communications Commission.\n**(4)**\nAny other department, agency, or entity the President determines to be relevant.\n##### (e) Intelligence community\nThe intelligence community is authorized to provide support to the Task Force.\n##### (f) Information sharing\nTo ensure proper coordination and effective interagency action, each Federal department or agency represented on the Task Force shall fully share\u2014\n**(1)**\nall relevant data with the Task Force; and\n**(2)**\nall information regarding the department or agency\u2019s plans, before and after final agency decisions are made, on all matters relating to actions regarding combating online scams.\n##### (g) Consultation\nThe Task Force or representatives thereof shall\u2014\n**(1)**\nconsult quarterly with United States State and local law enforcement entities and stakeholder organizations with firsthand expertise in reporting and combatting online scam operations, cyberscams known as pig butchering scams , and other kinds of cyberscams, and recovering stolen crypto assets, and incorporate their feedback and recommendations to the maximum extent feasible;\n**(2)**\nconsult regularly with U.S. non-governmental organizations with expertise in countering trafficking in persons or anti-corruption, as appropriate; and\n**(3)**\ndevelop partnerships with relevant private sector actors, including banks, social media platforms, online dating applications, telecommunication carriers, cryptocurrency exchanges, internet service providers, applications stores, search engines, and search optimization companies, for the purpose of better disrupting the enabling infrastructure of scam compounds, operations, and syndicates.\n##### (h) Sunset\nThe Task Force shall terminate on the date that is seven years after the date of the enactment of this Act.\n#### 5. Elements of comprehensive strategy\n##### (a) In general\nThe strategy required by section 1(b)(1) shall incorporate the following objectives:\n**(1)**\nBringing pressure to bear on foreign governments, in coordination with allies and partners to the greatest extent possible, that are complicit in, tolerant of, or uncooperative in combatting online scam operations.\n**(2)**\nInvestigating the People\u2019s Republic of China\u2019s (PRC) involvement in the origin and perpetuation of online scam operations, including through links between Chinese Communist Party officials and criminal organizations, deepening regional security influence, and selective crackdowns that incentivize the targeting of Americans.\n**(3)**\nInvestigating the Burmese military\u2019s involvement in allowing, neglecting, and profiting from online scam operations in Burma, and the importance of resolving the instability and violence in Burma to stop the unfettered operation of scam centers in Burma.\n**(4)**\nResponding comprehensively to PRC complicity in and instrumentalization of online scam operations.\n**(5)**\nReducing the power, influence, and scope of transnational criminal organizations and operations in Southeast Asia and wherever else they may propagate.\n**(6)**\nBuilding the capacity of trusted foreign law enforcement partners to degrade, disrupt, and shut down online scam centers and prevent their proliferation, including through training in digital forensics, anti-money laundering, and border patrol.\n**(7)**\nBuilding the capacity of trusted foreign law enforcement partners to screen for and protect victims of trafficking in persons in a trauma-informed manner, prosecute traffickers, and prevent trafficking into online scam centers, including through public awareness campaigns.\n**(8)**\nImposing sanctions or other relevant designations, comprehensively and in coordination with allies and partners to the greatest extent possible, on the perpetrators and enablers of online scams, using relevant transnational organized crime, corruption, human rights, and trafficking in persons authorities.\n**(9)**\nAdvocating for the greylisting or blacklisting, as appropriate, of countries involved in state-sponsored scam operations, including Cambodia, at the Financial Action Task Force.\n**(10)**\nHarnessing offensive cyber capabilities to degrade online scam centers\u2019 operations.\n**(11)**\nRecovering and returning stolen assets of defrauded United States persons.\n**(12)**\nIntegrating data collection, analysis, and response mechanisms across Federal, State, and local agencies, including by assessing if any existing relevant Fusion Centers could be leveraged to combat online scam centers.\n**(13)**\nConvening a coalition of like-minded foreign allies and partners to combat online scam centers, including through the establishment of similar task forces or working groups, the compilation and sharing of data, and collaboration regarding the indictment of key actors and enablers.\n##### (b) Measurable indicators\nThe Task Force shall develop measurable indicators of the success of the strategy required by section 1731(b)(1), which may include persons sanctioned, arrest warrants or indictments issued, arrests made, U.S. losses mitigated, and the number of victims of trafficking in persons rescued, and known scam centers reduced, in comparison to the previous year.\n#### 6. Annual report to Congress\n##### (a) In general\nNot later than 360 days after the date of the submission of the strategy required by section 1(b)(1), and annually thereafter for five years, the Task Force shall submit to the appropriate congressional committees a report that includes, for the previous year the following:\n**(1)**\nA list of all foreign persons sanctioned by the United States for being responsible for, complicit in, or responsible for ordering, controlling, or otherwise directing, online financial scams against United States nationals.\n**(2)**\nFor the foreign persons listed in paragraph (1), an assessment and review of their ongoing involvement in the operation of scam centers, including an identification of entities in particular from within the People\u2019s Republic of China that aid or abet such foreign persons.\n**(3)**\nAn estimate of how much money was stolen from United States nationals through scams emanating from online scam centers, including as a percentage of the estimated total amount stolen through such scams globally.\n**(4)**\nAn estimate of how many stolen funds were intercepted, seized, or returned.\n**(5)**\nAn estimate of how many victims of trafficking in persons were employed in online scam centers.\n**(6)**\nAn estimate of the total number of people involved in operating or supporting the operation of scam centers.\n**(7)**\nA list of known online scam centers.\n**(8)**\nA description of if, where, and how online scam centers and operations have proliferated globally.\n**(9)**\nRecommendations on the kinds of programs the Department of State should support in order to effectively implement the strategy described in subsection (c), including the level of appropriations such programs would require.\n**(10)**\nAny other measures the Task Force determines appropriate to include.\n##### (b) Form\nEach report submitted pursuant to subsection (a) shall be unclassified but may include a classified annex.\n##### (c) Consultation\nThe Task Force shall consult regularly with the appropriate congressional committees on its efforts to implement the strategy required by section 1(b)(1), including potential updates. Such consultations should include descriptions of the Task Force\u2019s periodic consultations with local law enforcement agencies and civil society organizations and any incorporated recommendations, as well as recommendations for strengthening the Task Force\u2019s capability to effectively shut down online scam centers, dismantle criminal scam organizations, and recoup stolen U.S. assets. Such consultations may take the form of briefings.\n#### 7. Imposition of sanctions\n##### (a) Determination, Imposition, and Report Required\nNot later than 180 days after the date of the enactment of this Act, the President shall, in accordance with the strategy required by section 1(b)(1)\u2014\n**(1)**\ndetermine whether each foreign person listed in subsection (d) meets the statutory criteria for the imposition of sanctions under one or more of the sanctions programs and authorities listed in subsection (c);\n**(2)**\npursuant to paragraph (1), impose applicable sanctions against such foreign persons determined to meet such criteria for imposition of sanctions; and\n**(3)**\nsubmit to the appropriate congressional committees a report containing\u2014\n**(A)**\na list of all foreign persons determined to meet such criteria; and\n**(B)**\nfor any foreign person listed in subsection (d) that is not determined to meet the criteria for the imposition of sanctions under one or more of the sanctions programs and authorities listed in subsection (c), a complete justification of such a non-determination or decision to otherwise not apply the sanctions authorized by such sanctions programs and authorities.\n##### (b) Waiver\nThe President may waive the imposition of sanctions with respect to a foreign person listed in subsection (d) on or after the date that is 15 days after the President\u2014\n**(1)**\ndetermines that such a waiver is vital to the national security interests of the United States; and\n**(2)**\nsubmits to the appropriate congressional committees the reasons for that determination.\n##### (c) Applicable Sanctions\nThe sanctions listed in this subsection are the sanctions described in the following:\n**(1)**\nSections 1262 through 1264 of the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 10101 et seq. ).\n**(2)**\nSection 111 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7108 ).\n**(3)**\nExecutive Order 13581, relating to Transnational Criminal Organization Sanctions.\n##### (d) Foreign persons\n**(1) In general**\nThe foreign persons listed in this subsection are the following:\n**(A)**\nAik Paung.\n**(B)**\nBenjamin Mauerberger.\n**(C)**\nChen Xiuling.\n**(D)**\nD. Chen Zhi.\n**(E)**\nChou Bun Eng.\n**(F)**\nDy Vichea.\n**(G)**\nEdward Lee.\n**(H)**\nGabriel Tan.\n**(I)**\nHonn Sorachna.\n**(J)**\nHun To.\n**(K)**\nIng Dara.\n**(L)**\nKok An.\n**(M)**\nKuoch Chamrouen.\n**(N)**\nLi Xiong.\n**(O)**\nLong Dimanche.\n**(P)**\nMa Dongli.\n**(Q)**\nMichael Chiam.\n**(R)**\nMote Thun.\n**(S)**\nNeth Savoeun.\n**(T)**\nRithy Raksmei.\n**(U)**\nSai Aung Lin.\n**(V)**\nSai Kyaw Hla.\n**(W)**\nSar Sokha.\n**(X)**\nSaw Min Min Oo.\n**(Y)**\nSu Zhongkian.\n**(Z)**\nYan Borith.\n**(AA)**\nYan Narong.\n**(BB)**\nYan Sathya.\n**(CC)**\nYim Leak.\n**(DD)**\nYu Jianjun.\n**(EE)**\nYu Lingxiong.\n**(FF)**\nZhong Baojia (also known as Wang Qiang).\n**(GG)**\n9 Dynasty.\n**(HH)**\nDongmei Group.\n**(II)**\nFully Light Group of Companies, LTD.\n**(JJ)**\nHongmen World Cultural and Historical Association.\n**(KK)**\nHuione Group.\n**(LL)**\nK99 Group.\n**(MM)**\nPrince Group Holding Company.\n**(NN)**\nTrans-Asia International Holding Group.\n**(OO)**\nUnion Development Group.\n**(PP)**\nWhite Sands Palace Casino.\n**(QQ)**\nXinwang International.\n**(RR)**\nAny person, organization, or entity determined by the President, based on credible evidence, to be responsible for, complicit in, or responsible for ordering, controlling, or otherwise directing, online financial scams against United States nationals, including those scams originating from compounds in Southeast Asia in which victims of severe forms of trafficking in persons are forced to engage in illegal scam activity.\n**(2) Exception**\nIn accordance with section 102(b)(19) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7101(b)(19) ), no person determined by the President to be a victim of trafficking in persons shall be considered to be a foreign person listed in this subsection for purposes of imposition of sanctions under this section.\n#### 8. Programs to support victims of forced criminality\n##### (a) In general\nThe Secretary of State is authorized to carry out programs, out of the funds authorized to be appropriated by section 6 and in accordance with section 106(a) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7105(a) ), to provide trauma-informed care, shelter, reintegration, and support services for victims of trafficking in persons within online scam centers.\n##### (b) Design and implementation\nThe Task Force shall ensure programs authorized by subsection (a) are designed and implemented in a manner that prevents revictimization and gains information and evidence critical to understanding online scam centers\u2019 operations and prosecuting scammers.\n#### 9. Authorization of appropriations\nThere is authorized to be appropriated $30,000,000 for the Department of State for each of the fiscal years 2026 and 2027 to develop, coordinate, and implement the strategy required by section 1(b)(1).\n#### 10. Definitions\nIn this Act\u2014\n**(1)**\nthe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations of the Senate; and\n**(2)**\nthe term intelligence community has the meaning given that term in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 ).",
      "versionDate": "2025-09-18",
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
        "name": "International Affairs",
        "updateDate": "2026-04-01T19:24:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-18",
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
          "measure-id": "id119hr5490",
          "measure-number": "5490",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-18",
          "originChamber": "HOUSE",
          "update-date": "2026-05-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5490v00",
            "update-date": "2026-05-05"
          },
          "action-date": "2025-09-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Dismantle Foreign Scam Syndicates Act</strong></p><p>This bill requires the President to (1) impose applicable sanctions on foreign persons (individuals or entities) responsible for online financial scams against U.S. nationals, and (2) establish an interagency task\u00a0force to shut down\u00a0the criminal syndicates perpetuating such scams.</p><p>Under the bill, the President must determine whether 43 specified foreign persons, and any other foreign persons the President determines are responsible for or complicit in online financial scams against U.S. nationals, are subject to sanctions under specified laws and <a href=\"https://obamawhitehouse.archives.gov/the-press-office/2011/07/25/executive-order-13581-blocking-property-transnational-criminal-organizat\">Executive Order 13581</a>. Upon such determination, the President must impose applicable sanctions (for\u00a0example, blocking the sanctioned person's property transactions within the United States).</p><p>The President must also establish an interagency task force to shut down transnational criminal syndicates that use large scam centers and forced labor of trafficked persons to perpetuate mass online scams against Americans. The task force must (1) submit a comprehensive strategy to Congress to combat these scam centers and dismantle the criminal elements involved with them, and (2) coordinate and oversee implementation of the strategy. Within 360 days of submitting the strategy to Congress and annually thereafter for five years the task force must submit to Congress a report addressing various topics related to such scam centers including a list of all foreign persons sanctioned by the United States for their scam center involvement.</p><p>The Department of State is authorized to provide trauma-informed care, shelter, reintegration, and support services for victims of trafficking in persons within online scam centers.</p>"
        },
        "title": "Dismantle Foreign Scam Syndicates Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5490.xml",
    "summary": {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dismantle Foreign Scam Syndicates Act</strong></p><p>This bill requires the President to (1) impose applicable sanctions on foreign persons (individuals or entities) responsible for online financial scams against U.S. nationals, and (2) establish an interagency task\u00a0force to shut down\u00a0the criminal syndicates perpetuating such scams.</p><p>Under the bill, the President must determine whether 43 specified foreign persons, and any other foreign persons the President determines are responsible for or complicit in online financial scams against U.S. nationals, are subject to sanctions under specified laws and <a href=\"https://obamawhitehouse.archives.gov/the-press-office/2011/07/25/executive-order-13581-blocking-property-transnational-criminal-organizat\">Executive Order 13581</a>. Upon such determination, the President must impose applicable sanctions (for\u00a0example, blocking the sanctioned person's property transactions within the United States).</p><p>The President must also establish an interagency task force to shut down transnational criminal syndicates that use large scam centers and forced labor of trafficked persons to perpetuate mass online scams against Americans. The task force must (1) submit a comprehensive strategy to Congress to combat these scam centers and dismantle the criminal elements involved with them, and (2) coordinate and oversee implementation of the strategy. Within 360 days of submitting the strategy to Congress and annually thereafter for five years the task force must submit to Congress a report addressing various topics related to such scam centers including a list of all foreign persons sanctioned by the United States for their scam center involvement.</p><p>The Department of State is authorized to provide trauma-informed care, shelter, reintegration, and support services for victims of trafficking in persons within online scam centers.</p>",
      "updateDate": "2026-05-05",
      "versionCode": "id119hr5490"
    },
    "title": "Dismantle Foreign Scam Syndicates Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dismantle Foreign Scam Syndicates Act</strong></p><p>This bill requires the President to (1) impose applicable sanctions on foreign persons (individuals or entities) responsible for online financial scams against U.S. nationals, and (2) establish an interagency task\u00a0force to shut down\u00a0the criminal syndicates perpetuating such scams.</p><p>Under the bill, the President must determine whether 43 specified foreign persons, and any other foreign persons the President determines are responsible for or complicit in online financial scams against U.S. nationals, are subject to sanctions under specified laws and <a href=\"https://obamawhitehouse.archives.gov/the-press-office/2011/07/25/executive-order-13581-blocking-property-transnational-criminal-organizat\">Executive Order 13581</a>. Upon such determination, the President must impose applicable sanctions (for\u00a0example, blocking the sanctioned person's property transactions within the United States).</p><p>The President must also establish an interagency task force to shut down transnational criminal syndicates that use large scam centers and forced labor of trafficked persons to perpetuate mass online scams against Americans. The task force must (1) submit a comprehensive strategy to Congress to combat these scam centers and dismantle the criminal elements involved with them, and (2) coordinate and oversee implementation of the strategy. Within 360 days of submitting the strategy to Congress and annually thereafter for five years the task force must submit to Congress a report addressing various topics related to such scam centers including a list of all foreign persons sanctioned by the United States for their scam center involvement.</p><p>The Department of State is authorized to provide trauma-informed care, shelter, reintegration, and support services for victims of trafficking in persons within online scam centers.</p>",
      "updateDate": "2026-05-05",
      "versionCode": "id119hr5490"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5490ih.xml"
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
      "title": "Dismantle Foreign Scam Syndicates Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T08:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dismantle Foreign Scam Syndicates Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T08:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish an interagency Task Force to dismantle and shut down transnational criminal syndicates perpetuating mass online scam operations against Americans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T08:48:37Z"
    }
  ]
}
```
