# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/965?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/965
- Title: Housing Unhoused Disabled Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 965
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-04-13T16:08:41Z
- Update date including text: 2026-04-13T16:08:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-02-10 17:25:00 - Floor: Mr. Hill (AR) moved to suspend the rules and pass the bill.
- 2025-02-10 17:25:01 - Floor: Considered under suspension of the rules. (consideration: CR H603-605)
- 2025-02-10 17:25:02 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 965.
- 2025-02-10 17:41:03 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H603)
- 2025-02-10 17:41:03 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H603)
- 2025-02-10 17:41:05 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-02-11 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-02-10 17:25:00 - Floor: Mr. Hill (AR) moved to suspend the rules and pass the bill.
- 2025-02-10 17:25:01 - Floor: Considered under suspension of the rules. (consideration: CR H603-605)
- 2025-02-10 17:25:02 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 965.
- 2025-02-10 17:41:03 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H603)
- 2025-02-10 17:41:03 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H603)
- 2025-02-10 17:41:05 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-02-11 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/965",
    "number": "965",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "S000344",
        "district": "32",
        "firstName": "Brad",
        "fullName": "Rep. Sherman, Brad [D-CA-32]",
        "lastName": "Sherman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Housing Unhoused Disabled Veterans Act",
    "type": "HR",
    "updateDate": "2026-04-13T16:08:41Z",
    "updateDateIncludingText": "2026-04-13T16:08:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2025-02-10",
      "actionTime": "17:41:05",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37300",
      "actionDate": "2025-02-10",
      "actionTime": "17:41:03",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H603)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-02-10",
      "actionTime": "17:41:03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H603)",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-02-10",
      "actionTime": "17:25:02",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "DEBATE - The House proceeded with forty minutes of debate on H.R. 965.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-02-10",
      "actionTime": "17:25:01",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered under suspension of the rules. (consideration: CR H603-605)",
      "type": "Floor"
    },
    {
      "actionCode": "H30300",
      "actionDate": "2025-02-10",
      "actionTime": "17:25:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Mr. Hill (AR) moved to suspend the rules and pass the bill.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-11T15:40:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-04T17:09:45Z",
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
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "True",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NE"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "AZ"
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
      "sponsorshipDate": "2025-02-07",
      "state": "NY"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IL"
    },
    {
      "bioguideId": "A000371",
      "district": "33",
      "firstName": "Pete",
      "fullName": "Rep. Aguilar, Pete [D-CA-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Aguilar",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-07",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-07",
      "state": "LA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "RI"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "OR"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "RI"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-07",
      "state": "DC"
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
      "sponsorshipDate": "2025-02-07",
      "state": "NC"
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
      "sponsorshipDate": "2025-02-07",
      "state": "PA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "CA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "WA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "MI"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "OH"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "NY"
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
      "sponsorshipDate": "2025-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "NM"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
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
      "sponsorshipDate": "2025-02-10",
      "state": "NC"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "OR"
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
      "sponsorshipDate": "2025-02-10",
      "state": "NY"
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
      "sponsorshipDate": "2025-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
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
      "sponsorshipDate": "2025-02-10",
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
      "sponsorshipDate": "2025-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "NY"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr965ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 965\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Sherman (for himself, Ms. De La Cruz , Mr. Lieu , Mr. Levin , Mr. Carbajal , Mr. Gottheimer , Ms. Brownley , Mrs. Cherfilus-McCormick , Ms. Budzinski , Mr. Foster , Mr. Sessions , Mr. Meuser , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend section 3(b)(4) of the United States Housing Act of 1937 to exclude certain disability benefits from income for the purposes of determining eligibility for the supported housing program under section 8(o)(19), and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Unhoused Disabled Veterans Act .\n#### 2. Exclusion of certain disability benefits\nSection 3(b)(4)(B) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(4)(B) ) is amended\u2014\n**(1)**\nby redesignating clauses (iv) and (v) as clauses (vi) and (vii), respectively; and\n**(2)**\nby inserting after clause (iii) the following:\n(iv) with respect to the supported housing program under section 8(o)(19), any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code, received by a veteran, except that this exclusion may not apply to the definition of adjusted income; (v) with respect to any household receiving rental assistance under the supported housing program under section 8(o)(19) as it relates to eligibility for other types of housing assistance, any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code, received by a veteran, except that this exclusion may not apply to the definition of adjusted income; .\n#### 3. Treatment of certain disability benefits\n##### (a) In general\nWhen determining the eligibility of a veteran to rent a residential dwelling unit constructed on Department property on or after the date of the enactment of this Act, for which assistance is provided as part of a housing assistance program administered by the Secretary of Housing and Urban Development and not yet in existence at the time of the enactment of this section, the Secretary shall exclude from income any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code by such person.\n##### (b) Definitions\nIn this section:\n**(1) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(2) Department property**\nThe term Department property has the meaning given the term in section 901 of title 38, United States Code.",
      "versionDate": "2025-02-04",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr965rfs.xml",
      "text": "IIB\n119th CONGRESS\n1st Session\nH. R. 965\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Received; read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nAN ACT\nTo amend section 3(b)(4) of the United States Housing Act of 1937 to exclude certain disability benefits from income for the purposes of determining eligibility for the supported housing program under section 8(o)(19), and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Unhoused Disabled Veterans Act .\n#### 2. Exclusion of certain disability benefits\nSection 3(b)(4)(B) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(4)(B) ) is amended\u2014\n**(1)**\nby redesignating clauses (iv) and (v) as clauses (vi) and (vii), respectively; and\n**(2)**\nby inserting after clause (iii) the following:\n(iv) with respect to the supported housing program under section 8(o)(19), any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code, received by a veteran, except that this exclusion may not apply to the definition of adjusted income; (v) with respect to any household receiving rental assistance under the supported housing program under section 8(o)(19) as it relates to eligibility for other types of housing assistance, any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code, received by a veteran, except that this exclusion may not apply to the definition of adjusted income; .\n#### 3. Treatment of certain disability benefits\n##### (a) In general\nWhen determining the eligibility of a veteran to rent a residential dwelling unit constructed on Department property on or after the date of the enactment of this Act, for which assistance is provided as part of a housing assistance program administered by the Secretary of Housing and Urban Development and not yet in existence at the time of the enactment of this section, the Secretary shall exclude from income any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code by such person.\n##### (b) Definitions\nIn this section:\n**(1) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(2) Department property**\nThe term Department property has the meaning given the term in section 901 of title 38, United States Code.",
      "versionDate": "2025-02-11",
      "versionType": "Referred in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr965eh.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 965\nIN THE HOUSE OF REPRESENTATIVES\nAN ACT\nTo amend section 3(b)(4) of the United States Housing Act of 1937 to exclude certain disability benefits from income for the purposes of determining eligibility for the supported housing program under section 8(o)(19), and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Unhoused Disabled Veterans Act .\n#### 2. Exclusion of certain disability benefits\nSection 3(b)(4)(B) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(4)(B) ) is amended\u2014\n**(1)**\nby redesignating clauses (iv) and (v) as clauses (vi) and (vii), respectively; and\n**(2)**\nby inserting after clause (iii) the following:\n(iv) with respect to the supported housing program under section 8(o)(19), any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code, received by a veteran, except that this exclusion may not apply to the definition of adjusted income; (v) with respect to any household receiving rental assistance under the supported housing program under section 8(o)(19) as it relates to eligibility for other types of housing assistance, any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code, received by a veteran, except that this exclusion may not apply to the definition of adjusted income; .\n#### 3. Treatment of certain disability benefits\n##### (a) In general\nWhen determining the eligibility of a veteran to rent a residential dwelling unit constructed on Department property on or after the date of the enactment of this Act, for which assistance is provided as part of a housing assistance program administered by the Secretary of Housing and Urban Development and not yet in existence at the time of the enactment of this section, the Secretary shall exclude from income any disability benefits received under chapter 11 or chapter 15 of title 38, United States Code by such person.\n##### (b) Definitions\nIn this section:\n**(1) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(2) Department property**\nThe term Department property has the meaning given the term in section 901 of title 38, United States Code.",
      "versionDate": "",
      "versionType": "Engrossed in House"
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
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1415",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Housing Unhoused Disabled Veterans Act",
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
            "name": "Disability assistance",
            "updateDate": "2025-02-10T16:07:20Z"
          },
          {
            "name": "Low- and moderate-income housing",
            "updateDate": "2025-02-10T16:07:20Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2025-02-10T16:07:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-02-10T12:59:18Z"
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
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr965ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr965rfs.xml"
        }
      ],
      "type": "Referred in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr965eh.xml"
        }
      ],
      "type": "Engrossed in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RFS",
      "billTextVersionName": "Referred in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Housing Unhoused Disabled Veterans Act",
      "titleType": "Short Titles from RFS (Referred to Senate) bill text",
      "titleTypeCode": "255",
      "updateDate": "2025-02-13T03:08:15Z"
    },
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Housing Unhoused Disabled Veterans Act",
      "titleType": "Short Title(s) as Passed House",
      "titleTypeCode": "104",
      "updateDate": "2025-02-12T02:53:16Z"
    },
    {
      "title": "Housing Unhoused Disabled Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T06:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Unhoused Disabled Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T06:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 3(b)(4) of the United States Housing Act of 1937 to exclude certain disability benefits from income for the purposes of determining eligibility for the supported housing program under section 8(o)(19), and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T06:03:40Z"
    }
  ]
}
```
