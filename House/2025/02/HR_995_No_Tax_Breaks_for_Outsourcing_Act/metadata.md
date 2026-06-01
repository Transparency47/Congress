# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/995?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/995
- Title: No Tax Breaks for Outsourcing Act
- Congress: 119
- Bill type: HR
- Bill number: 995
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2026-03-02T16:11:34Z
- Update date including text: 2026-03-02T16:11:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/995",
    "number": "995",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000399",
        "district": "37",
        "firstName": "Lloyd",
        "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
        "lastName": "Doggett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "No Tax Breaks for Outsourcing Act",
    "type": "HR",
    "updateDate": "2026-03-02T16:11:34Z",
    "updateDateIncludingText": "2026-03-02T16:11:34Z"
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
          "date": "2025-02-05T15:03:30Z",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "AZ"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "VT"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "OH"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "GA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "OR"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "OH"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IN"
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
      "sponsorshipDate": "2025-02-05",
      "state": "LA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "TX"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "HI"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MO"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "TN"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert [D-NJ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NJ"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "TX"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CO"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MD"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CT"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "WA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "OR"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MI"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "TX"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NM"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "TX"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "ME"
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
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "TX"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "AZ"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CT"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NV"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "OR"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MD"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "WA"
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
      "sponsorshipDate": "2025-02-05",
      "state": "GA"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
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
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "OH"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CT"
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
      "sponsorshipDate": "2025-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "RI"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "GA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "DE"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MN"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "KY"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MA"
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
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NJ"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MD"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IN"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CO"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NJ"
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
      "sponsorshipDate": "2025-02-05",
      "state": "DC"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MN"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NJ"
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
      "sponsorshipDate": "2025-02-05",
      "state": "WA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "ME"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "WI"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MD"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "OR"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "WA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NM"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MI"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "OH"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MI"
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
      "sponsorshipDate": "2025-02-05",
      "state": "MS"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NV"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MI"
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
      "sponsorshipDate": "2025-02-05",
      "state": "HI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MA"
    },
    {
      "bioguideId": "T000489",
      "district": "18",
      "firstName": "Sylvester",
      "fullName": "Rep. Turner, Sylvester [D-TX-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "TX"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NJ"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "GA"
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
      "sponsorshipDate": "2025-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NY"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "WA"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "CT"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray, Jr. [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "GA"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MI"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "IL"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MO"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
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
      "sponsorshipDate": "2026-02-03",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr995ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 995\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Doggett (for himself, Ms. Adams , Ms. Ansari , Ms. Balint , Ms. Barrag\u00e1n , Mrs. Beatty , Mr. Bishop , Ms. Bonamici , Mr. Boyle of Pennsylvania , Ms. Brown , Ms. Brownley , Ms. Budzinski , Mr. Carson , Mr. Carter of Louisiana , Mr. Casar , Mr. Case , Ms. Chu , Ms. Clarke of New York , Mr. Cleaver , Mr. Cohen , Mr. Conaway , Ms. Crockett , Mr. Crow , Mr. Davis of Illinois , Mr. Davis of North Carolina , Ms. Dean of Pennsylvania , Mrs. McClain Delaney , Ms. DeLauro , Ms. DelBene , Mr. Deluzio , Mr. DeSaulnier , Ms. Dexter , Mrs. Dingell , Ms. Escobar , Mr. Espaillat , Mr. Evans of Pennsylvania , Ms. Leger Fernandez , Mr. Foster , Mrs. Foushee , Ms. Lois Frankel of Florida , Mr. Frost , Mr. Garamendi , Mr. Garc\u00eda of Illinois , Mr. Garcia of California , Ms. Garcia of Texas , Mr. Golden of Maine , Mr. Goldman of New York , Mr. Gomez , Mr. Green of Texas , Mr. Grijalva , Mrs. Hayes , Mr. Horsford , Ms. Hoyle of Oregon , Mr. Huffman , Mr. Ivey , Mr. Jackson of Illinois , Ms. Jayapal , Mr. Johnson of Georgia , Ms. Kaptur , Ms. Kelly of Illinois , Mr. Kennedy of New York , Mr. Khanna , Mr. Landsman , Mr. Larson of Connecticut , Ms. Lee of Pennsylvania , Mr. Lieu , Mr. Lynch , Mr. Magaziner , Mrs. McBath , Ms. McBride , Ms. McCollum , Mr. McGarvey , Mr. McGovern , Mr. Meeks , Mr. Menendez , Ms. Meng , Mr. Mfume , Mr. Moulton , Mr. Mrvan , Mr. Nadler , Mr. Neguse , Mr. Norcross , Ms. Norton , Ms. Ocasio-Cortez , Ms. Omar , Mr. Pallone , Ms. Perez , Ms. Pingree , Mr. Pocan , Ms. Pressley , Mrs. Ramirez , Mr. Raskin , Mr. Riley of New York , Ms. Ross , Mr. Ryan , Ms. Salinas , Ms. Scanlon , Ms. Schakowsky , Mr. Sherman , Mr. Smith of Washington , Mr. Soto , Ms. Stansbury , Ms. Stevens , Mrs. Sykes , Mr. Takano , Mr. Thanedar , Mr. Thompson of Mississippi , Ms. Titus , Ms. Tlaib , Ms. Tokuda , Mr. Tonko , Mrs. Torres of California , Mrs. Trahan , Mr. Turner of Texas , Mr. Vargas , Ms. Vel\u00e1zquez , Ms. Wasserman Schultz , Ms. Waters , Mrs. Watson Coleman , Ms. Williams of Georgia , and Ms. Wilson of Florida ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for current year inclusion of net CFC tested income, and for other purposes.\n#### 1. Short title, etc\n##### (a) Short title\nThis Act may be cited as the No Tax Breaks for Outsourcing Act .\n##### (b) Amendment of 1986 code\nExcept as otherwise expressly provided, whenever in this Act an amendment or repeal is expressed in terms of an amendment to, or repeal of, a section or other provision, the reference shall be considered to be made to a section or other provision of the Internal Revenue Code of 1986.\n##### (c) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title, etc.\nSec. 2. Current year inclusion of net CFC tested income.\nSec. 3. Country-by-country application of limitation on foreign tax credit based on taxable units.\nSec. 4. Limitation on deduction of interest by domestic corporations which are members of an international financial reporting group.\nSec. 5. Modifications to rules relating to inverted corporations.\nSec. 6. Treatment of foreign corporations managed and controlled in the United States as domestic corporations.\n#### 2. Current year inclusion of net CFC tested income\n##### (a) Repeal of tax-Free deemed return on investments\n**(1) In general**\nSection 951A(a) is amended by striking global intangible low-taxed income and inserting net CFC tested income .\n**(2) Conforming amendments**\n**(A)**\nSection 951A is amended by striking subsections (b) and (d).\n**(B)**\nSection 951A(e)(1) is amended by striking subsections (b), (c)(1)(A), and and inserting subsections (c)(1)(A) and .\n**(C)**\nSection 951A(f) is amended by striking global intangible low-taxed income each place it appears and inserting net CFC tested income .\n**(D)**\nSection 960(d)(2)(A) is amended by striking global intangible low-taxed income (as defined in section 951A(b)) and inserting net CFC tested income (as defined in section 951A(c)) .\n##### (b) Country-by-Country application of section based on CFC taxable units\nSection 951A is amended by adding at the end the following new subsection:\n(g) Country-by-Country application of section based on CFC taxable units (1) In general If any CFC taxable unit of a United States shareholder is a tax resident of (or, in the case of a branch, is located in) a country which is different from the country with respect to which any other CFC taxable unit of such United States shareholder is a tax resident (or, in the case of a branch, is located in)\u2014 (A) such shareholder\u2019s net CFC tested income for purposes of subsection (a) shall be the sum of the amounts of net CFC tested income determined separately with respect to each such country, and (B) for purposes of determining such separate amounts of net CFC tested income\u2014 (i) except as otherwise provided by the Secretary, any reference in subsection (c) to a controlled foreign corporation of such shareholder shall be treated as reference to a CFC taxable unit of such shareholder, and (ii) net CFC tested income and such other items and amounts as the Secretary may provide, shall be determined separately with respect to each such country by determining such amounts with respect to the CFC taxable units of such shareholder which are a tax resident of such country. (2) Definitions For purposes of this subsection\u2014 (A) CFC taxable unit The term CFC taxable unit means any taxable unit described in clause (ii), (iii), or (iv) of section 904(e)(2)(B), determined\u2014 (i) by substituting controlled foreign corporation for foreign corporation each place it appears in such clauses, and (ii) without regard to the references to the taxpayer in clauses (iii) and (iv) of such section. (B) Application of other definitions Terms used in this subsection which are also used in section 904(e) shall have the same meaning as when used in section 904(e). (3) Special rules For purposes of this subsection\u2014 (A) Application of certain rules Except as otherwise provided by the Secretary, rules similar to the rules of section 904(e) shall apply. (B) Allocation of net CFC tested income to controlled foreign corporations Except as otherwise provided by the Secretary, subsection (f)(2) shall be applied separately with respect to each CFC taxable unit. .\n##### (c) Regulatory authority\nSection 951A , as amended by subsection (b), is amended by adding at the end the following new subsection:\n(h) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out, or prevent the avoidance of, the purposes of this section, including regulations or guidance which provide for\u2014 (1) the treatment of property if such property is transferred, or held, temporarily, (2) the treatment of property if the avoidance of the purposes of this section is a factor in the transfer or holding of such property, (3) appropriate adjustments to the basis of stock and other ownership interests, and to earnings and profits, to reflect tested losses (whether or not taken into account in determining net CFC tested income), (4) rules similar to the rules provided under the regulations or guidance issued under section 904(e)(4), (5) other appropriate basis adjustments, (6) appropriate adjustments to be made, and appropriate tax attributes and records to be maintained, separately with respect to CFC taxable units, and (7) appropriate adjustments in determining tested income or tested loss if property is transferred between related parties or amounts are paid or accrued between related parties. .\n##### (d) Coordination with other provisions\nSection 951A(f)(1) is amended by adding at the end the following new subparagraph:\n(C) Treatment of certain references Except as otherwise provided by the Secretary, references to section 951 or section 951(a) in sections 959, 961, 962, and such other provisions as the Secretary may identify shall include references to section 951A or section 951A(a), respectively. .\n##### (e) Repeal of reduced rate of tax on net CFC tested income and foreign-Derived intangible income\n**(1) In general**\nPart VIII of subchapter B of chapter 1 is amended by striking section 250 (and by striking the item relating to such section in the table of sections of such part).\n**(2) Conforming amendments**\n**(A)**\nSection 59A(c)(4)(B)(i) is amended by striking section 172, 245A, or 250 and inserting section 172 or 245A .\n**(B)**\nSection 172(d) is amended by striking paragraph (9).\n**(C)**\nSection 246(b)(1) is amended\u2014\n**(i)**\nby striking subsection (a) and (b) of section 245, and section 250 and inserting and subsection (a) and (b) of section 245 ; and\n**(ii)**\nby striking subsection (a) and (b) of section 245, and 250 and inserting and subsection (a) and (b) of section 245 .\n**(D)**\nSection 469(i)(3)(E)(iii) is amended by striking , 221, and 250 and inserting and 221 .\n##### (f) Repeal of certain exclusions from the determination of tested income\nSection 951A(c)(2)(A)(i) is amended\u2014\n**(1)**\nby striking subclauses (III) and (V),\n**(2)**\nby redesignating subclause (IV) as subclause (III),\n**(3)**\nby adding and at the end of subclause (II), and\n**(4)**\nby striking and at the end of subclause (III) (as so redesignated) and inserting over .\n##### (g) Increase in deemed paid credit for taxes properly attributable to tested income\n**(1) In general**\nSection 960(d) is amended by striking 80 percent of .\n**(2) Conforming amendment**\nSection 78 is amended by striking (determined without regard to the phrase \u201c80 percent of\u201d in subsection (d)(1) thereof) .\n##### (h) Repeal of high tax exclusion for foreign base company income and insurance income\n**(1) In general**\nSection 954(b) is amended by striking paragraph (4).\n**(2) Conforming amendment**\nSection 904(d)(3)(E) is amended by striking the last sentence.\n##### (i) Elimination of carryback of foreign tax credit\n**(1) In general**\nSection 904(c) is amended\u2014\n**(A)**\nby striking in the first preceding taxable year and in any of the first 10 succeeding taxable years, in that order and inserting in any of the first 10 succeeding taxable years, in order ,\n**(B)**\nby striking preceding or each place it appears, and\n**(C)**\nby striking Carryback and in the heading thereof.\n**(2) Application to limitation on foreign oil and gas taxes**\nSection 907(f) is amended\u2014\n**(A)**\nin paragraph (1), by striking in the first preceding taxable year and ,\n**(B)**\nin paragraph (2), by striking preceding or in the matter preceding subparagraph (A),\n**(C)**\nin paragraph (3)(B)\u2014\n**(i)**\nby striking in a preceding or succeeding and inserting in a succeeding , and\n**(ii)**\nby striking in such preceding or succeeding both places it appears and inserting in such succeeding , and\n**(D)**\nin the heading, by striking Carryback and .\n##### (j) Treatment of foreign base company oil related income as subpart F income\n**(1) In general**\nSection 954(a) is amended by striking and at the end of paragraph (2), by striking the period at the end of paragraph (3) and inserting , and , and by adding at the end the following new paragraph:\n(4) the foreign base company oil related income for the taxable year (determined under subsection (f) and reduced as provided in subsection (b)(5)). .\n**(2) Foreign base company oil related income**\nSection 954 is amended by inserting after subsection (e) the following new subsection:\n(f) Foreign base company oil related income For purposes of this section, the term foreign base company oil related income means foreign oil related income (within the meaning of paragraphs (2) and (3) of section 907(c)) other than income derived from a source within a foreign country in connection with\u2014 (1) oil or gas which was extracted from an oil or gas well located in such foreign country, or (2) oil, gas, or a primary product of oil or gas which is sold by the foreign corporation or a related person for use or consumption within such country or is loaded in such country on a vessel or aircraft as fuel for such vessel or aircraft. Such term shall not include any foreign personal holding company income (as defined in subsection (c)). .\n**(3) Conforming amendments**\n**(A)**\nSection 952(c)(1)(B)(iii) is amended by redesignating subclauses (III) and (IV) as subclauses (IV) and (V), respectively, and by inserting after subclause (II) the following new subclause:\n(III) foreign base company oil related income. .\n**(B)**\nSection 954(b) is amended\u2014\n**(i)**\nby striking and the foreign base company services income in paragraph (5) and inserting the foreign base company services income, and the foreign base company oil related income , and\n**(ii)**\nby adding at the end the following new paragraph:\n(6) Foreign base company oil related income not treated as another kind of foreign base company income Income of a corporation which is foreign base company oil related income shall not be considered foreign base company income of such corporation under paragraph (2) or (3) of subsection (a). .\n##### (k) Effective dates\n**(1) In general**\nExcept as otherwise provided in this subsection, the amendments made by this section shall apply to taxable years of foreign corporations beginning after December 31, 2024, and to taxable years of United States shareholders in which or with which such taxable years of foreign corporations end.\n**(2) Regulatory authority and coordination with other provisions**\nThe amendments made by subsections (c) and (d) shall apply to taxable years of foreign corporations beginning after the date of the enactment of this Act, and to taxable years of United States shareholders in which or with which such taxable years of foreign corporations end.\n**(3) Repeal of reduced rate of tax; increase in deemed paid credit**\nThe amendments made by subsections (e) and (g) shall apply to taxable years beginning after December 31, 2024.\n**(4) Elimination of carryback of foreign tax credit**\nThe amendment made by subsection (i) shall apply to credits arising in taxable years beginning after December 31, 2024.\n##### (l) No inference regarding certain modifications\nThe amendments made by subsections (c) and (d) shall not be construed to create any inference with respect to the proper application of any provision of the Internal Revenue Code of 1986 with respect to any taxable year beginning before the taxable years to which such amendments apply.\n#### 3. Country-by-country application of limitation on foreign tax credit based on taxable units\n##### (a) In general\nSection 904 is amended by inserting after subsection (d) the following new subsection:\n(e) Country-by-Country application based on taxable units (1) In general Subsection (d) (and the provisions of this title referred to in paragraph (1) of such subsection) shall be applied separately with respect to each country by taking into account the aggregate income properly attributable or otherwise allocable to a taxable unit of the taxpayer which is a tax resident of (or, in the case of a branch, is located in) such country. (2) Taxable units (A) In general Except as otherwise provided by the Secretary, each item shall be attributable or otherwise allocable to exactly one taxable unit of the taxpayer. (B) Determination of taxable units Except as otherwise provided by the Secretary, the taxable units of a taxpayer are as follows: (i) General taxable unit The person that is the taxpayer and that is not otherwise described in a separate clause of this subparagraph. (ii) Certain foreign corporations Each foreign corporation with respect to which the taxpayer is a United States shareholder. (iii) Interests in pass-through entities Each interest held (directly or indirectly) by the taxpayer or any foreign corporation referred to in clause (ii) in a pass-through entity if such pass-through entity is a tax resident of a country other than the country with respect to which such taxpayer or foreign corporation (as the case may be) is a tax resident. (iv) Branches Each branch (or portion thereof) the activities of which are directly or indirectly carried on by the taxpayer or any foreign corporation referred to in clause (ii) and which give rise to a taxable presence in a country other than the country with respect to which such taxpayer or foreign corporation (as the case may be) is a tax resident. (3) Definitions and special rules For purposes of this subsection\u2014 (A) Tax resident Except as otherwise provided by the Secretary, the term tax resident means a person or entity subject to tax under the tax law of a country as a resident. If an entity is organized under the law of a country, or resident in a country, that does not impose an income tax with respect to such entities, such entity shall, except as provided by the Secretary, be treated as subject to tax under the tax law of such country for the purposes of the preceding sentence. (B) Pass-through entity Except as otherwise provided by the Secretary, the term pass-through entity includes any partnership or other entity to the extent that income, gain, deduction, or loss of the entity is taken into account in determining the income or loss of a person that owns (directly or indirectly) an interest in such entity. (C) Branch Except as otherwise provided by the Secretary, the term branch means a taxable presence of a tax resident in a country other than its country of residence as determined under such other country\u2019s tax law. The Secretary shall provide regulations or other guidance applying such term to activities in a country that do not give rise to a taxable presence. (D) Treatment of fiscally autonomous jurisdictions Any fiscally autonomous jurisdiction shall be treated as a separate country. Any possession of the United States shall also be treated as a separate country. (E) Possession of the United States The term possession of the United States means each of American Samoa, the Commonwealth of the Northern Mariana Islands, the Commonwealth of Puerto Rico, Guam, and the Virgin Islands. (4) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out, or prevent avoidance of, the purposes of this subsection, including regulations or other guidance\u2014 (A) providing for the application of this subsection to an entity or arrangement that is considered a tax resident of more than one country or of no country, (B) providing for the application of this subsection to hybrid entities or hybrid transactions (as such terms are used for purposes of section 267A), pass-through entities, passive foreign investment companies, trusts, and other entities or arrangements not otherwise described in this subsection, and (C) providing for the assignment of any item (including foreign taxes and deductions) to taxable units, including in the case of amounts not otherwise taken into account in determining taxable income under this chapter. .\n##### (b) Treatment of inadequate substantiation\nSection 904(d)(4)(C)(ii) is amended by striking paragraph (1)(A) and inserting paragraph (1)(C) .\n##### (c) Application of foreign tax credit limitation with respect to foreign branches\nSection 904(d)(2)(J)(i) is amended\u2014\n**(1)**\nby striking qualified business units (as defined in section 989(a)) in 1 or more foreign countries and inserting foreign branches described in section 904(e)(2)(B)(iv) , and\n**(2)**\nby striking a qualified business unit and inserting a foreign branch .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n#### 4. Limitation on deduction of interest by domestic corporations which are members of an international financial reporting group\n##### (a) In general\nSection 163 is amended by redesignating subsection (n) as subsection (p) and by inserting after subsection (m) the following new subsection:\n(n) Limitation on deduction of interest by domestic corporations in international financial reporting groups (1) In general In the case of any domestic corporation which is a member of any international financial reporting group, the deduction under this chapter for interest paid or accrued during the taxable year shall not exceed the sum of\u2014 (A) the allowable percentage of 110 percent of the excess (if any) of\u2014 (i) the amount of such interest so paid or accrued, over (ii) the amount described in subparagraph (B), plus (B) the amount of interest includible in gross income of such corporation for such taxable year. (2) International financial reporting group (A) For purposes of this subsection, the term international financial reporting group means, with respect to any reporting year, any group of entities which\u2014 (i) includes\u2014 (I) at least one foreign corporation engaged in a trade or business within the United States, or (II) at least one domestic corporation and one foreign corporation, (ii) prepares consolidated financial statements with respect to such year, and (iii) reports in such statements average annual gross receipts (determined in the aggregate with respect to all entities which are part of such group) for the 3-reporting-year period ending with such reporting year in excess of $100,000,000. (B) Rules relating to determination of average gross receipts For purposes of subparagraph (A)(iii), rules similar to the rules of section 448(c)(3) shall apply. (3) Allowable percentage For purposes of this subsection\u2014 (A) In general The term allowable percentage means, with respect to any domestic corporation for any taxable year, the ratio (expressed as a percentage and not greater than 100 percent) of\u2014 (i) such corporation\u2019s allocable share of the international financial reporting group\u2019s reported net interest expense for the reporting year of such group which ends in or with such taxable year of such corporation, over (ii) such corporation\u2019s reported net interest expense for such reporting year of such group. (B) Reported net interest expense The term reported net interest expense means\u2014 (i) with respect to any international financial reporting group for any reporting year, the excess of\u2014 (I) the aggregate amount of interest expense reported in such group\u2019s consolidated financial statements for such taxable year, over (II) the aggregate amount of interest income reported in such group\u2019s consolidated financial statements for such taxable year, and (ii) with respect to any domestic corporation for any reporting year, the excess of\u2014 (I) the amount of interest expense of such corporation reported in the books and records of the international financial reporting group which are used in preparing such group\u2019s consolidated financial statements for such taxable year, over (II) the amount of interest income of such corporation reported in such books and records. (C) Allocable share of reported net interest expense With respect to any domestic corporation which is a member of any international financial reporting group, such corporation\u2019s allocable share of such group\u2019s reported net interest expense for any reporting year is the portion of such expense which bears the same ratio to such expense as\u2014 (i) the EBITDA of such corporation for such reporting year, bears to (ii) the EBITDA of such group for such reporting year. (D) EBITDA (i) In general The term EBITDA means, with respect to any reporting year, earnings before interest, taxes, depreciation, and amortization\u2014 (I) as determined in the international financial reporting group\u2019s consolidated financial statements for such year, or (II) for purposes of subparagraph (A)(i), as determined in the books and records of the international financial reporting group which are used in preparing such statements if not determined in such statements. (ii) Treatment of disregarded entities The EBITDA of any domestic corporation shall not fail to include the EBITDA of any entity which is disregarded for purposes of this chapter. (iii) Treatment of intra-group distributions The EBITDA of any domestic corporation shall be determined without regard to any distribution received by such corporation from any other member of the international financial reporting group. (E) Special rules for non-positive EBITDA (i) Non-positive group EBITDA In the case of any international financial reporting group the EBITDA of which is zero or less, paragraph (1) shall not apply to any member of such group the EBITDA of which is above zero. (ii) Non-positive entity EBITDA In the case of any group member the EBITDA of which is zero or less, paragraph (1) shall be applied without regard to subparagraph (A) thereof. (4) Consolidated financial statement For purposes of this subsection, the term consolidated financial statement means any consolidated financial statement described in paragraph (2)(A)(ii) if such statement is\u2014 (A) a financial statement which is certified as being prepared in accordance with generally accepted accounting principles, international financial reporting standards, or any other comparable method of accounting identified by the Secretary, and which is\u2014 (i) a 10\u2013K (or successor form), or annual statement to shareholders, required to be filed with the United States Securities and Exchange Commission, (ii) an audited financial statement which is used for\u2014 (I) credit purposes, (II) reporting to shareholders, partners, or other proprietors, or to beneficiaries, or (III) any other substantial nontax purpose, but only if there is no statement described in clause (i), or (iii) filed with any other Federal or State agency for nontax purposes, but only if there is no statement described in clause (i) or (ii), or (B) a financial statement which\u2014 (i) is used for a purpose described in subclause (I), (II), or (III) of subparagraph (A)(ii), or (ii) filed with any regulatory or governmental body (whether domestic or foreign) specified by the Secretary, but only if there is no statement described in subparagraph (A). (5) Reporting year For purposes of this subsection, the term reporting year means, with respect to any international financial reporting group, the year with respect to which the consolidated financial statements are prepared. (6) Application to certain entities (A) Partnerships Except as otherwise provided by the Secretary in paragraph (7), this subsection and subsection (o) shall apply to any partnership which is a member of any international financial reporting group under rules similar to the rules of section 163(j)(4). (B) Foreign corporations engaged in trade or business within the United States Except as otherwise provided by the Secretary in paragraph (7), any deduction for interest paid or accrued by a foreign corporation engaged in a trade or business within the United States shall be limited in a manner consistent with the principles of this subsection. (C) Consolidated groups For purposes of this subsection, the members of any group that file (or are required to file) a consolidated return with respect to the tax imposed by chapter 1 for a taxable year shall be treated as a single corporation. (7) Regulations The Secretary may issue such regulations or other guidance as are necessary or appropriate to carry out the purposes of this subsection. .\n##### (b) Carryforward of disallowed interest\n**(1) In general**\nSection 163 is amended by inserting after subsection (n), as added by subsection (a), the following new subsection:\n(o) Carryforward of certain disallowed interest The amount of any interest not allowed as a deduction for any taxable year by reason of subsection (j)(1) or (n)(1) (whichever imposes the lower limitation with respect to such taxable year) shall be treated as interest (and as business interest for purposes of subsection (j)(1)) paid or accrued (and as interest expense reported as described in clause (i)(I) or (ii)(I) of subsection (n)(3)(B), as the case may be) in the succeeding taxable year. Interest paid or accrued in any taxable year (determined without regard to the preceding sentence) shall not be carried past the fifth taxable year following such taxable year, determined by treating interest as allowed as a deduction on a first-in, first-out basis. .\n**(2) Conforming amendments**\n**(A)**\nSection 163(j)(2) is amended to read as follows:\n(2) Carryforward cross-reference For carryforward treatment, see subsection (o). .\n**(B)**\nSection 163(j)(4)(B)(i)(I) is amended by striking paragraph (2) and inserting subsection (o) .\n**(C)**\nSection 381(c)(20) is amended to read as follows:\n(20) Carryforward of disallowed interest The carryover of disallowed interest described in section 163(o) to taxable years ending after the date of distribution or transfer. .\n**(D)**\nSection 382(d)(3) is amended to read as follows:\n(3) Application to carryforward of disallowed interest The term pre-change loss shall include any carryover of disallowed interest described in section 163(o) under rules similar to the rules of paragraph (1). .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n#### 5. Modifications to rules relating to inverted corporations\n##### (a) In general\nSubsection (b) of section 7874 is amended to read as follows:\n(b) Inverted corporations treated as domestic corporations (1) In general Notwithstanding section 7701(a)(4), a foreign corporation shall be treated for purposes of this title as a domestic corporation if\u2014 (A) such corporation would be a surrogate foreign corporation if subsection (a)(2) were applied by substituting 80 percent for 60 percent , or (B) such corporation is an inverted domestic corporation. (2) Inverted domestic corporation For purposes of this subsection, a foreign corporation shall be treated as an inverted domestic corporation if, pursuant to a plan (or a series of related transactions)\u2014 (A) the entity completes after December 22, 2017, the direct or indirect acquisition of\u2014 (i) substantially all of the properties held directly or indirectly by a domestic corporation, or (ii) substantially all of the assets of, or substantially all of the properties constituting a trade or business of, a domestic partnership, and (B) after the acquisition, either\u2014 (i) more than 50 percent of the stock (by vote or value) of the entity is held\u2014 (I) in the case of an acquisition with respect to a domestic corporation, by former shareholders of the domestic corporation by reason of holding stock in the domestic corporation, or (II) in the case of an acquisition with respect to a domestic partnership, by former partners of the domestic partnership by reason of holding a capital or profits interest in the domestic partnership, or (ii) the management and control of the expanded affiliated group which includes the entity occurs, directly or indirectly, primarily within the United States, and such expanded affiliated group has significant domestic business activities. (3) Exception for corporations with substantial business activities in foreign country of organization A foreign corporation described in paragraph (2) shall not be treated as an inverted domestic corporation if after the acquisition the expanded affiliated group which includes the entity has substantial business activities in the foreign country in which or under the law of which the entity is created or organized when compared to the total business activities of such expanded affiliated group. For purposes of subsection (a)(2)(B)(iii) and the preceding sentence, the term substantial business activities shall have the meaning given such term under regulations in effect on December 22, 2017, except that the Secretary may issue regulations increasing the threshold percent in any of the tests under such regulations for determining if business activities constitute substantial business activities for purposes of this paragraph. (4) Management and control For purposes of paragraph (2)(B)(ii)\u2014 (A) In general The Secretary shall prescribe regulations for purposes of determining cases in which the management and control of an expanded affiliated group is to be treated as occurring, directly or indirectly, primarily within the United States. The regulations prescribed under the preceding sentence shall apply to periods after December 22, 2017. (B) Executive officers and senior management Such regulations shall provide that the management and control of an expanded affiliated group shall be treated as occurring, directly or indirectly, primarily within the United States if substantially all of the executive officers and senior management of the expanded affiliated group who exercise day-to-day responsibility for making decisions involving strategic, financial, and operational policies of the expanded affiliated group are based or primarily located within the United States. Individuals who in fact exercise such day-to-day responsibilities shall be treated as executive officers and senior management regardless of their title. (5) Significant domestic business activities For purposes of paragraph (2)(B)(ii), an expanded affiliated group has significant domestic business activities if at least 25 percent of\u2014 (A) the employees of the group are based in the United States, (B) the employee compensation incurred by the group is incurred with respect to employees based in the United States, (C) the assets of the group are located in the United States, or (D) the income of the group is derived in the United States, determined in the same manner as such determinations are made for purposes of determining substantial business activities under regulations referred to in paragraph (3) as in effect on December 22, 2017, but applied by treating all references in such regulations to foreign country and relevant foreign country as references to the United States . The Secretary may issue regulations decreasing the threshold percent in any of the tests under such regulations for determining if business activities constitute significant domestic business activities for purposes of this paragraph. .\n##### (b) Conforming amendments\n**(1)**\nClause (i) of section 7874(a)(2)(B) is amended by striking after March 4, 2003, and inserting after March 4, 2003, and before December 23, 2017, .\n**(2)**\nSubsection (c) of section 7874 is amended\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nby striking subsection (a)(2)(B)(ii) and inserting subsections (a)(2)(B)(ii) and (b)(2)(B)(i) ; and\n**(ii)**\nby inserting or (b)(2)(A) after (a)(2)(B)(i) in subparagraph (B);\n**(B)**\nin paragraph (3), by inserting or (b)(2)(B)(i), as the case may be, after (a)(2)(B)(ii) ;\n**(C)**\nin paragraph (5), by striking subsection (a)(2)(B)(ii) and inserting subsections (a)(2)(B)(ii) and (b)(2)(B)(i) ; and\n**(D)**\nin paragraph (6), by inserting or inverted domestic corporation, as the case may be, after surrogate foreign corporation .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years ending after December 22, 2017.\n##### (d) Extension of limitation on assessment\nIf the period of limitation on assessment of tax resulting from the amendments made by subsection (a) expires before the end of the 3-year period beginning on the date of the enactment of this Act, such assessment (to the extent attributable to such amendments) may, nevertheless, be made before the close of such 3-year period.\n#### 6. Treatment of foreign corporations managed and controlled in the United States as domestic corporations\n##### (a) In general\nSection 7701 is amended by redesignating subsection (p) as subsection (q) and by inserting after subsection (o) the following new subsection:\n(p) Certain corporations managed and controlled in the United States treated as domestic for income tax (1) In general Notwithstanding subsection (a)(4), in the case of a corporation described in paragraph (2) if\u2014 (A) the corporation would not otherwise be treated as a domestic corporation for purposes of this title, but (B) the management and control of the corporation occurs, directly or indirectly, primarily within the United States, then, solely for purposes of chapter 1 (and any other provision of this title relating to chapter 1), the corporation shall be treated as a domestic corporation. (2) Corporation described (A) In general A corporation is described in this paragraph if\u2014 (i) the stock of such corporation is regularly traded on an established securities market, or (ii) the aggregate gross assets of such corporation (or any predecessor thereof), including assets under management for investors, whether held directly or indirectly, at any time during the taxable year or any preceding taxable year is $50,000,000 or more. (B) General exception A corporation shall not be treated as described in this paragraph if\u2014 (i) such corporation was treated as a corporation described in this paragraph in a preceding taxable year, (ii) such corporation\u2014 (I) is not regularly traded on an established securities market, and (II) has, and is reasonably expected to continue to have, aggregate gross assets (including assets under management for investors, whether held directly or indirectly) of less than $50,000,000, and (iii) the Secretary grants a waiver to such corporation under this subparagraph. (3) Management and control (A) In general The Secretary shall prescribe regulations for purposes of determining cases in which the management and control of a corporation is to be treated as occurring primarily within the United States. (B) Executive officers and senior management Such regulations shall provide that\u2014 (i) the management and control of a corporation shall be treated as occurring primarily within the United States if substantially all of the executive officers and senior management of the corporation who exercise day-to-day responsibility for making decisions involving strategic, financial, and operational policies of the corporation are located primarily within the United States, and (ii) individuals who are not executive officers and senior management of the corporation (including individuals who are officers or employees of other corporations in the same chain of corporations as the corporation) shall be treated as executive officers and senior management if such individuals exercise the day-to-day responsibilities of the corporation described in clause (i). (C) Corporations primarily holding investment assets Such regulations shall also provide that the management and control of a corporation shall be treated as occurring primarily within the United States if\u2014 (i) the assets of such corporation (directly or indirectly) consist primarily of assets being managed on behalf of investors, and (ii) decisions about how to invest the assets are made in the United States. .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning on or after the date which is 2 years after the date of the enactment of this Act, whether or not regulations are issued under section 7701(p)(3) of the Internal Revenue Code of 1986, as added by this section.",
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
        "actionDate": "2026-02-11",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7493",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Corporate Inversions Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-11",
        "text": "Read twice and referred to the Committee on Finance. (text: CR S579-580)"
      },
      "number": "3847",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Corporate Inversions Act of 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-05",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "409",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Tax Breaks for Outsourcing Act",
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
        "updateDate": "2025-05-05T15:02:52Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr995ih.xml"
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
      "title": "No Tax Breaks for Outsourcing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Tax Breaks for Outsourcing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide for current year inclusion of net CFC tested income, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:44Z"
    }
  ]
}
```
