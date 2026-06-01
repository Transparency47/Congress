# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/111?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/111
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the United States Fish and Wildlife Service relating to "Barred Owl Management Strategy".
- Congress: 119
- Bill type: HJRES
- Bill number: 111
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-04-03T20:47:40Z
- Update date including text: 2026-04-03T20:47:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/111",
    "number": "111",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the United States Fish and Wildlife Service relating to \"Barred Owl Management Strategy\".",
    "type": "HJRES",
    "updateDate": "2026-04-03T20:47:40Z",
    "updateDateIncludingText": "2026-04-03T20:47:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TN"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "SC"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TN"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
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
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NJ"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TN"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NJ"
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
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
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
      "sponsorshipDate": "2025-07-23",
      "state": "NC"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
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
      "sponsorshipDate": "2025-07-23",
      "sponsorshipWithdrawnDate": "2025-09-10",
      "state": "PA"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "FL"
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
      "sponsorshipDate": "2025-08-22",
      "state": "NY"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "TX"
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
      "sponsorshipDate": "2025-09-02",
      "state": "TX"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-10",
      "state": "GA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "IN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "NY"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "LA"
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
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "TN"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
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
      "sponsorshipDate": "2025-10-10",
      "state": "IN"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "NC"
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
      "sponsorshipDate": "2025-10-14",
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
      "sponsorshipDate": "2025-10-21",
      "state": "NY"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "TN"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "UT"
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
      "sponsorshipDate": "2025-11-18",
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
      "sponsorshipDate": "2026-02-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres111ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 111\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Nehls (for himself, Mr. Harder of California , Mr. Perry , Mr. Gray , Mr. Ogles , Mr. Carter of Georgia , Ms. Mace , Mr. Gooden , Ms. Kamlager-Dove , Mr. Burchett , Mr. Buchanan , Mr. Bilirakis , Mr. Van Drew , Mrs. Harshbarger , Mr. Gottheimer , Mr. Fitzpatrick , Mrs. Cherfilus-McCormick , Mr. Thanedar , Mr. Davis of North Carolina , Mrs. Luna , and Ms. Lee of Pennsylvania ) submitted the following joint resolution; which was referred to the Committee on Natural Resources\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the United States Fish and Wildlife Service relating to Barred Owl Management Strategy .\nThat Congress disapproves the rule submitted by the United States Fish and Wildlife Service relating to \u201cBarred Owl Management Strategy\u201d (issued September 6, 2024, as a record of decision, and a letter of opinion from the Government Accountability Office dated May 28, 2025, printed in the Congressional Record on July 10, 2025, on pages S4311\u2013S4313, concluding that such record of decision is a rule under the Congressional Review Act), and such rule shall have no force or effect.",
      "versionDate": "2025-07-23",
      "versionType": "IH"
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
        "actionDate": "2025-10-29",
        "text": "Motion to proceed to consideration of measure rejected in Senate by Yea-Nay Vote. 25 - 72. Record Vote Number: 597."
      },
      "number": "69",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the United States Fish and Wildlife Service relating to \"Record of Decision for the Barred Owl Management Strategy; Washington, Oregon, and California\".",
      "type": "SJRES"
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-11-19T19:42:42Z"
          },
          {
            "name": "Birds",
            "updateDate": "2025-11-19T19:42:42Z"
          },
          {
            "name": "California",
            "updateDate": "2025-11-19T19:42:42Z"
          },
          {
            "name": "Department of the Interior",
            "updateDate": "2025-11-19T19:42:42Z"
          },
          {
            "name": "Oregon",
            "updateDate": "2025-11-19T19:42:42Z"
          },
          {
            "name": "Pest management",
            "updateDate": "2025-11-19T19:42:42Z"
          },
          {
            "name": "Washington State",
            "updateDate": "2025-11-19T19:42:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Animals",
        "updateDate": "2026-04-03T20:28:00Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres111ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the United States Fish and Wildlife Service relating to \"Barred Owl Management Strategy\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T04:48:33Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the United States Fish and Wildlife Service relating to \"Barred Owl Management Strategy\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T08:07:21Z"
    }
  ]
}
```
