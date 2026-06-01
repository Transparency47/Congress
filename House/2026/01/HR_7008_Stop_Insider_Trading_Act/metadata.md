# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7008?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7008
- Title: Stop Insider Trading Act
- Congress: 119
- Bill type: HR
- Bill number: 7008
- Origin chamber: House
- Introduced date: 2026-01-12
- Update date: 2026-04-23T12:55:52Z
- Update date including text: 2026-04-23T12:55:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-12: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-01-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-14 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 7 - 4.
- 2026-02-03 - Calendars: Placed on the Union Calendar, Calendar No. 409.
- 2026-02-03 - Committee: Reported (Amended) by the Committee on House Administration. H. Rept. 119-479.
- 2026-02-03 - Committee: Reported (Amended) by the Committee on House Administration. H. Rept. 119-479.
- Latest action: 2026-01-12: Introduced in House

## Actions

- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-01-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-14 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 7 - 4.
- 2026-02-03 - Calendars: Placed on the Union Calendar, Calendar No. 409.
- 2026-02-03 - Committee: Reported (Amended) by the Committee on House Administration. H. Rept. 119-479.
- 2026-02-03 - Committee: Reported (Amended) by the Committee on House Administration. H. Rept. 119-479.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-12",
    "latestAction": {
      "actionDate": "2026-01-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7008",
    "number": "7008",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001213",
        "district": "1",
        "firstName": "Bryan",
        "fullName": "Rep. Steil, Bryan [R-WI-1]",
        "lastName": "Steil",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Stop Insider Trading Act",
    "type": "HR",
    "updateDate": "2026-04-23T12:55:52Z",
    "updateDateIncludingText": "2026-04-23T12:55:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-02-03",
      "calendarNumber": {
        "calendar": "U00409"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 409.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on House Administration. H. Rept. 119-479.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on House Administration. H. Rept. 119-479.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 7 - 4.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
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
      "actionDate": "2026-01-12",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-12",
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
            "date": "2026-02-03T18:47:34Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-14T17:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-12T17:02:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NC"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "VA"
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
      "sponsorshipDate": "2026-01-12",
      "state": "NC"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "OK"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "OH"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "IL"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "FL"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "AZ"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "TN"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "FL"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "TX"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "OH"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "WI"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NE"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "SD"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "CO"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "PA"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "GA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NY"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "WA"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "TX"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "IA"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "FL"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "KS"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "FL"
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
      "sponsorshipDate": "2026-01-12",
      "state": "SC"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "IA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "VA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "TX"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "MD"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "TX"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "MO"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "IN"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "UT"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "IA"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "True",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "MI"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "FL"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "FL"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "MI"
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
      "sponsorshipDate": "2026-01-12",
      "state": "GA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NY"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "PA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "KS"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "ND"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "VA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "IA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "FL"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NJ"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "AZ"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "FL"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "IN"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NY"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NC"
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
      "sponsorshipDate": "2026-01-12",
      "state": "MI"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "PA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "FL"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NE"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "TX"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "PA"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "MI"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "MI"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "IN"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "WI"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "WI"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "WI"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "PA"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "AL"
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
      "sponsorshipDate": "2026-01-12",
      "state": "OH"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NC"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "MO"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "AK"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "IL"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "AL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
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
      "sponsorshipDate": "2026-01-13",
      "state": "FL"
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
      "sponsorshipDate": "2026-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
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
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "MT"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "CO"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "OR"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "GA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "FL"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "MS"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "HI"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "TN"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7008ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7008\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 12, 2026 Mr. Steil (for himself, Mr. Hudson , Mr. Griffith , Mr. Murphy , Mrs. Bice , Mr. Carey , Mrs. Miller of Illinois , Ms. Lee of Florida , Mr. Biggs of Arizona , Mr. Ogles , Mrs. Luna , Mr. Roy , Mr. Taylor , Mr. Van Orden , Mr. Bacon , Mr. Johnson of South Dakota , Mr. Hurd of Colorado , Mr. Joyce of Pennsylvania , Mr. Collins , Mr. Lawler , Mr. Baumgartner , Mr. Cloud , Mr. Feenstra , Mr. Scott Franklin of Florida , Mr. Mann , Mr. Buchanan , Mr. Timmons , Mrs. Kim , Mr. Nunn of Iowa , Mr. Cline , Mr. Crenshaw , Mr. Harris of Maryland , Mr. Arrington , Mr. Alford , Mr. Yakym , Mr. Kennedy of Utah , Mrs. Miller-Meeks , Mr. James , Mr. Mills , Mrs. Cammack , Mr. Barrett , Mr. Carter of Georgia , Mr. LaLota , Mr. Mackenzie , Mr. Schmidt , Mrs. Fedorchak , Mrs. Kiggans of Virginia , Mrs. Hinson , Mr. Rutherford , Mr. Smith of New Jersey , Mr. Ciscomani , Mr. Kiley of California , Mr. Patronis , Mrs. Houchin , Mr. Riley of New York , Mr. Harrigan , Mr. Moolenaar , Mr. Perry , Mr. Bean of Florida , Mr. Flood , Mr. Self , Mr. Bresnahan , Mr. Huizenga , Mr. Bergman , Mr. Messmer , Mr. Tiffany , Mr. Grothman , Mr. Fitzgerald , Mr. Smucker , Mr. Strong , Mr. Miller of Ohio , Mr. McDowell , and Mrs. Wagner ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend chapter 131 of title 5 to require certain restrictions on stocks for Members of Congress and their spouses and dependents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Insider Trading Act .\n#### 2. Restrictions on covered investments\n##### (a) Table of contents\nThe table of contents for chapter 131 of title 5, United States Code, is amended by adding at the end the following:\nSubchapter IV. Restrictions on covered investments\n13151. Definitions.\n13152. Restrictions on covered investments.\n13153. Penalties.\n##### (b) Restrictions\nChapter 131 of title 5, United States Code, is amended by adding at the end a new subchapter:\nIV Restrictions on covered investments 13151. Definitions In this subchapter: (1) Covered individual The term covered individual means any of the following: (A) A Member of Congress, as defined in section 13101. (B) A dependent child (as defined in section 13101) or a spouse of a Member of Congress. (2) Covered investment (A) In general The term covered investment \u2014 (i) means a security issued by a publicly traded company or any comparable economic interest acquired through synthetic means, such as the use of a derivative, including an option, warrant, or other similar means; and (B) Exclusion The term covered investment does not include\u2014 (i) an excepted investment fund (as described in section 13104(f)(8)); (ii) any other fund that would be an excepted investment fund but for the fact that the fund does not meet the diversification requirement solely because the fund is concentrated in\u2014 (I) the United States; or (II) the State, territory, or District of residence of the covered individual who owns the fund; (iii) an interest in a small business concern as defined under section 3 of the Small Business Act ( 15 U.S.C. 632 ); or (iv) investments held in a trust if no covered individual has any authority over a trustee of the trust, including the authority to appoint, replace, or direct the actions of such a trustee, and the trustee is not the spouse, child, parent, or sibling of a Member of Congress. (3) Publicly traded company The term publicly traded company means an issuer that has a class of securities registered under section 12 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78l ). (4) Security The term security has the meaning given the term in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) ). (5) Supervising ethics office The term supervising ethics office has the meaning given the term in section 13101. 13152. Restrictions on covered investments (a) Conduct during federal service Except as described in subsection (c), no covered individual may purchase a covered investment. (b) Advanced notice requirement (1) In general No covered individual shall sell a covered investment, unless a notice of intent to sell the covered investment is made by the Member of Congress and publicly disclosed at least 7 calendar days, and no more than 14 calendar days, prior to the sale in accordance with the requirements of this subsection. (2) Contents of notice The notice under paragraph (1) shall include the following: (A) The projected date of sale of a covered investment. (B) A description of such sale. (C) The number of shares in such sale. (3) Withdrawal The notice under paragraph (1) shall be withdrawn by the Member of Congress who filed it, prior to the close of the expiration of the notice, if the covered individual determines not to sell the covered asset. (4) Filing A Member of Congress shall file the notice under paragraph (1) for each intended sale by the Member, or the spouse or dependent child of the Member, with\u2014 (A) the Clerk of the House of Representatives, in the case of a Representative in Congress, a Delegate to Congress, or the Resident Commissioner from Puerto Rico; or (B) the Secretary of the Senate, in the case of a Senator. (5) Publication The notice under paragraph (1) and the withdrawal under paragraph (3) shall, upon receipt, be made publicly available on a website controlled by the by the Clerk of the House of Representatives or the Secretary of the Senate, as applicable. (c) Exceptions (1) Occupation The requirements of subsections (a) and (b) shall not apply to a spouse or dependent child of a Member of Congress with respect to a transaction in a covered investment which is\u2014 (A) on behalf, or for the benefit, of any person other than a covered individual; or (B) made as a part of compensation from an employer of such individual or in furtherance of any fiduciary or occupational obligations of such individual. (2) Other The requirements of subsection (a) shall not apply to a covered individual with respect to a transaction in a covered investment made for the purpose of reinvesting dividends received from such covered investment. 13153. Enforcement (a) In general Any covered individual who violates the restrictions in section 13152 with respect to a covered investment, shall, at the direction of the supervising ethics office\u2014 (1) incur a fee, as calculated in subsection (b), to be paid by the Member of Congress who\u2014 (A) caused the violation; or (B) is the spouse or parent of a covered individual who caused the violation; and (2) in the case of a purchase of a covered investment, be required to sell a covered investment purchased in violation of section 13152(a). (b) Calculation of fees The fee required under subsection (a) shall be equal to the sum of\u2014 (1) $2,000 or ten percent of the value of the transaction in the covered investment which violates section 13152, whichever is greater; and (2) the net gain realized, if any, from the covered investment during the period beginning on the most recent date on which the individual became a covered individual and ending on the date of disposition of the covered investment, as determined by the supervising ethics office. (c) Payment restrictions A Member of Congress may not pay any of the fees under this section by using amounts from the following sources: (1) The Members\u2019 Representational Allowance. (2) The Senators\u2019 Official Personnel and Office Expense Account. (3) Any contribution (as defined in section 301(8) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101(8) )) accepted as a candidate, and any other donation received as support for activities of the individual as a holder of Federal office. (d) Miscellaneous receipts Any amounts collected in fees authorized by this section shall be deposited in the general fund of the Treasury as miscellaneous receipts in accordance with section 3302(b) of title 31. (e) Referral Upon the assessment of a fee under this section, the supervising ethics office has the authority to refer a Member of Congress to the Department of Justice in the same manner and to the same extent as a violation under section 13106 if such Member of Congress resigns or retires before paying such assessed fee. (f) Interpretative guidance Each supervising ethics office may issue interpretative guidance on this subchapter and in issuing such guidance, may consider mitigating or aggravating circumstances. .\n##### (c) Effective date\nThe amendments made by this Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2026-01-12",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7008rh.xml",
      "text": "IB\nUnion Calendar No. 409\n119th CONGRESS\n2d Session\nH. R. 7008\n[Report No. 119\u2013479]\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 12, 2026 Mr. Steil (for himself, Mr. Hudson , Mr. Griffith , Mr. Murphy , Mrs. Bice , Mr. Carey , Mrs. Miller of Illinois , Ms. Lee of Florida , Mr. Biggs of Arizona , Mr. Ogles , Mrs. Luna , Mr. Roy , Mr. Taylor , Mr. Van Orden , Mr. Bacon , Mr. Johnson of South Dakota , Mr. Hurd of Colorado , Mr. Joyce of Pennsylvania , Mr. Collins , Mr. Lawler , Mr. Baumgartner , Mr. Cloud , Mr. Feenstra , Mr. Scott Franklin of Florida , Mr. Mann , Mr. Buchanan , Mr. Timmons , Mrs. Kim , Mr. Nunn of Iowa , Mr. Cline , Mr. Crenshaw , Mr. Harris of Maryland , Mr. Arrington , Mr. Alford , Mr. Yakym , Mr. Kennedy of Utah , Mrs. Miller-Meeks , Mr. James , Mr. Mills , Mrs. Cammack , Mr. Barrett , Mr. Carter of Georgia , Mr. LaLota , Mr. Mackenzie , Mr. Schmidt , Ms. Fedorchak , Mrs. Kiggans of Virginia , Mrs. Hinson , Mr. Rutherford , Mr. Smith of New Jersey , Mr. Ciscomani , Mr. Kiley of California , Mr. Patronis , Mrs. Houchin , Mr. Riley of New York , Mr. Harrigan , Mr. Moolenaar , Mr. Perry , Mr. Bean of Florida , Mr. Flood , Mr. Self , Mr. Bresnahan , Mr. Huizenga , Mr. Bergman , Mr. Messmer , Mr. Tiffany , Mr. Grothman , Mr. Fitzgerald , Mr. Smucker , Mr. Strong , Mr. Miller of Ohio , Mr. McDowell , and Mrs. Wagner ) introduced the following bill; which was referred to the Committee on House Administration\nFebruary 3, 2026 Additional sponsors: Mr. Begich , Mr. Crane , Mr. LaHood , Mr. Rogers of Alabama , Ms. Tenney , Mr. Mast , Mr. Gosar , Mr. Ellzey , Mr. Fallon , Mr. Langworthy , Mr. Downing , Mr. Webster of Florida , Mr. Fong , Mr. Crank , Mr. Bentz , Mr. McCormick , Mr. Haridopolos , Mr. Guest , Mr. Case , Mr. Van Epps , and Mr. Evans of Colorado\nFebruary 3, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on January 12, 2026\nA BILL\nTo amend chapter 131 of title 5 to require certain restrictions on stocks for Members of Congress and their spouses and dependents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Insider Trading Act .\n#### 2. Restrictions on covered investments\n##### (a) Table of contents\nThe table of contents for chapter 131 of title 5, United States Code, is amended by adding at the end the following:\nSubchapter IV\u2014Restrictions on covered investments 13151. Definitions. 13152. Restrictions on covered investments. 13153. Enforcement. .\n##### (b) Restrictions\nChapter 131 of title 5, United States Code, is amended by adding at the end a new subchapter:\nIV Restrictions on covered investments 13151. Definitions In this subchapter: (1) Covered individual The term covered individual means any of the following: (A) A Member of Congress, as defined in section 13101. (B) A dependent child (as defined in section 13101) or a spouse of a Member of Congress. (2) Covered investment (A) In general The term covered investment means a security issued by a publicly traded company or any comparable economic interest acquired through synthetic means, such as the use of a derivative, including an option, warrant, or other similar means. (B) Exclusion The term covered investment does not include\u2014 (i) an excepted investment fund (as described in section 13104(f)(8)); (ii) any other fund that would be an excepted investment fund but for the fact that the fund does not meet the diversification requirement solely because the fund is concentrated in\u2014 (I) the United States; or (II) the State, territory, or District of residence of the covered individual who owns the fund; (iii) an interest in a small business concern as defined under section 3 of the Small Business Act ( 15 U.S.C. 632 ); or (iv) investments held in a trust if no covered individual has any authority over a trustee of the trust, including the authority to appoint, replace, or direct the actions of such a trustee, and the trustee is not the spouse, child, parent, or sibling of a Member of Congress. (3) Publicly traded company The term publicly traded company means an issuer that has a class of securities registered under section 12 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78l ). (4) Security The term security has the meaning given the term in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) ). (5) Supervising ethics office The term supervising ethics office has the meaning given the term in section 13101. 13152. Restrictions on covered investments (a) Conduct during federal service Except as described in subsection (c), no covered individual may purchase a covered investment. (b) Advanced notice requirement (1) In general No covered individual shall sell a covered investment, unless a notice of intent to sell the covered investment is made by the Member of Congress and publicly disclosed at least 7 calendar days, and no more than 14 calendar days, prior to the sale in accordance with the requirements of this subsection. (2) Contents of notice The notice under paragraph (1) shall include the following: (A) The projected date of sale of a covered investment. (B) A description of such sale. (C) The number of shares in such sale. (3) Withdrawal The notice under paragraph (1) shall be withdrawn by the Member of Congress who filed it, prior to the close of the expiration of the notice, if the covered individual determines not to sell the covered asset. (4) Filing A Member of Congress shall file the notice under paragraph (1) for each intended sale by the Member, or the spouse or dependent child of the Member, with\u2014 (A) the Clerk of the House of Representatives, in the case of a Representative in Congress, a Delegate to Congress, or the Resident Commissioner from Puerto Rico; or (B) the Secretary of the Senate, in the case of a Senator. (5) Publication The notice under paragraph (1) and the withdrawal under paragraph (3) shall, upon receipt, be made publicly available on a website controlled by the by the Clerk of the House of Representatives or the Secretary of the Senate, as applicable. (c) Exceptions (1) Occupation The requirements of subsections (a) and (b) shall not apply to a spouse or dependent child of a Member of Congress with respect to a transaction in a covered investment which is\u2014 (A) on behalf, or for the benefit, of any person other than a covered individual; or (B) made as a part of compensation from an employer of such individual or in furtherance of any fiduciary or occupational obligations of such individual. (2) Other The requirements of subsection (a) shall not apply to a covered individual with respect to a transaction in a covered investment made for the purpose of reinvesting dividends received from such covered investment. 13153. Enforcement (a) In general Any covered individual who violates the restrictions in section 13152 with respect to a covered investment, shall, at the direction of the supervising ethics office\u2014 (1) incur a fee, as calculated in subsection (b), to be paid by the Member of Congress who\u2014 (A) caused the violation; or (B) is the spouse or parent of a covered individual who caused the violation; and (2) in the case of a purchase of a covered investment, be required to sell a covered investment purchased in violation of section 13152(a). (b) Calculation of fees The fee required under subsection (a) shall be equal to the sum of\u2014 (1) $2,000 or ten percent of the value of the transaction in the covered investment which violates section 13152, whichever is greater; and (2) the net gain realized, if any, from the covered investment during the period beginning on the most recent date on which the individual became a covered individual and ending on the date of disposition of the covered investment, as determined by the supervising ethics office. (c) Payment restrictions A Member of Congress may not pay any of the fees under this section by using amounts from the following sources: (1) The Members\u2019 Representational Allowance. (2) The Senators\u2019 Official Personnel and Office Expense Account. (3) Any contribution (as defined in section 301(8) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101(8) )) accepted as a candidate, and any other donation received as support for activities of the individual as a holder of Federal office. (d) Miscellaneous receipts Any amounts collected in fees authorized by this section shall be deposited in the general fund of the Treasury as miscellaneous receipts in accordance with section 3302(b) of title 31. (e) Referral Upon the assessment of a fee under this section, the supervising ethics office has the authority to refer a Member of Congress to the Department of Justice in the same manner and to the same extent as a violation under section 13106 if such Member of Congress resigns or retires before paying such assessed fee. (f) Interpretative guidance Each supervising ethics office may issue interpretative guidance on this subchapter and in issuing such guidance, may consider mitigating or aggravating circumstances. .\n##### (c) Effective date\nThe amendments made by this Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2026-02-03",
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
        "actionDate": "2026-03-18",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "4134",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Insider Trading Act",
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
        "name": "Congress",
        "updateDate": "2026-04-23T12:55:52Z"
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
      "date": "2026-01-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7008ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7008rh.xml"
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
      "title": "Stop Insider Trading Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-04T04:23:15Z"
    },
    {
      "title": "Stop Insider Trading Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T09:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Insider Trading Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T09:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 131 of title 5 to require certain restrictions on stocks for Members of Congress and their spouses and dependents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T09:18:34Z"
    }
  ]
}
```
