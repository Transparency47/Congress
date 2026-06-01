# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2045?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2045
- Title: Medicare Dental, Vision, and Hearing Benefit Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2045
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2026-04-23T08:07:14Z
- Update date including text: 2026-04-23T08:07:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2045",
    "number": "2045",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
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
    "title": "Medicare Dental, Vision, and Hearing Benefit Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-23T08:07:14Z",
    "updateDateIncludingText": "2026-04-23T08:07:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:02:10Z",
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
          "date": "2025-03-11T14:02:05Z",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "OH"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "VA"
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "TN"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "VA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
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
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CO"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "CT"
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "NM"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "LA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
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
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NJ"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "CT"
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "GA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OH"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OH"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "WA"
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NV"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "DE"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "VA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MN"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "FL"
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "MD"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "WI"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "MN"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "WI"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NJ"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "MD"
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
      "sponsorshipDate": "2025-03-11",
      "state": "NC"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OR"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "GA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "AL"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NJ"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "NM"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "MS"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "FL"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "KY"
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
      "sponsorshipDate": "2025-03-11",
      "state": "NC"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NJ"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "FL"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-24",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
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
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MO"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "NV"
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
      "sponsorshipDate": "2025-06-03",
      "state": "NY"
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
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-30",
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
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
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
      "sponsorshipDate": "2026-04-22",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2045ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2045\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Doggett (for himself, Ms. Adams , Ms. Ansari , Ms. Balint , Ms. Barrag\u00e1n , Mrs. Beatty , Mr. Beyer , Mr. Bishop , Ms. Bonamici , Mr. Boyle of Pennsylvania , Mr. Carson , Mr. Carter of Louisiana , Mr. Casar , Mr. Castro of Texas , Ms. Chu , Mr. Cleaver , Mr. Cohen , Mr. Connolly , Ms. Crockett , Mr. Cuellar , Mr. Davis of Illinois , Ms. Dean of Pennsylvania , Ms. DeGette , Mrs. McClain Delaney , Ms. DeLauro , Mr. Deluzio , Mr. DeSaulnier , Ms. Dexter , Mrs. Dingell , Ms. Escobar , Mr. Espaillat , Mr. Evans of Pennsylvania , Ms. Leger Fernandez , Mr. Fields , Ms. Friedman , Mr. Frost , Mr. Garamendi , Mr. Garc\u00eda of Illinois , Mr. Garcia of California , Ms. Garcia of Texas , Mr. Goldman of New York , Mr. Gottheimer , Mr. Green of Texas , Mr. Grijalva , Mrs. Hayes , Ms. Hoyle of Oregon , Mr. Huffman , Mr. Jackson of Illinois , Ms. Jacobs , Ms. Jayapal , Mr. Johnson of Georgia , Ms. Johnson of Texas , Ms. Kaptur , Mr. Khanna , Mr. Krishnamoorthi , Mr. Landsman , Mr. Larsen of Washington , Mr. Larson of Connecticut , Ms. Lee of Pennsylvania , Ms. Lee of Nevada , Mr. Lieu , Ms. McBride , Ms. McClellan , Ms. McCollum , Mrs. Cherfilus-McCormick , Mr. McGovern , Mr. Meeks , Ms. Meng , Mr. Mfume , Ms. Moore of Wisconsin , Mr. Nadler , Mr. Norcross , Ms. Norton , Ms. Ocasio-Cortez , Ms. Omar , Ms. Pingree , Mr. Pocan , Ms. Pou , Ms. Pressley , Mrs. Ramirez , Mr. Raskin , Ms. Ross , Mr. Ruiz , Ms. Salinas , Ms. S\u00e1nchez , Ms. Scanlon , Ms. Schakowsky , Mr. David Scott of Georgia , Ms. Sewell , Mr. Sherman , Ms. Sherrill , Mr. Smith of Washington , Mr. Soto , Ms. Stansbury , Mr. Swalwell , Mr. Takano , Mr. Thanedar , Mr. Thompson of Mississippi , Mr. Thompson of California , Ms. Titus , Ms. Tlaib , Ms. Tokuda , Mr. Tonko , Mr. Torres of New York , Mrs. Trahan , Mr. Vargas , Mr. Veasey , Ms. Vel\u00e1zquez , Ms. Wasserman Schultz , Ms. Waters , Mrs. Watson Coleman , Ms. Williams of Georgia , Ms. Wilson of Florida , Mr. McGarvey , Mrs. Foushee , Mrs. McIver , Ms. Lois Frankel of Florida , and Mr. Gomez ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide for coverage of dental, vision, and hearing care under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Medicare Dental, Vision, and Hearing Benefit Act of 2025 .\n#### 2. Dental and oral health care\n##### (a) Coverage\nSection 1861(s)(2) of the Social Security Act ( 42 U.S.C. 1395x(s)(2) ) is amended\u2014\n**(1)**\nin subparagraph (II), by striking and after the semicolon at the end;\n**(2)**\nin subparagraph (JJ), by adding and after the semicolon at the end; and\n**(3)**\nby adding at the end the following new subparagraph:\n(KK) dental and oral health services (as defined in subsection (nnn)); .\n##### (b) Dental and oral health services defined\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended by adding at the end the following new subsection:\n(nnn) Dental and oral health services The term dental and oral health services means\u2014 (1) preventative and screening services, such as oral exams, dental cleanings, dental x-rays, and fluoride treatments; (2) basic dental services, such as tooth restorations, basic periodontics services, tooth extractions, and oral disease management services; (3) major dental services, such as major tooth restorations, major periodontics services, bridges, crowns, root canals, and extractions; (4) emergency dental care; and (5) other necessary services related to dental or oral health (as defined by the Secretary). .\n##### (c) Payment; coinsurance; and limitations\n**(1) In general**\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a)(1) ) is amended\u2014\n**(A)**\nby striking and before (GG) ; and\n**(B)**\nby inserting before the semicolon at the end the following: , and (HH) with respect to dental and oral health services (as defined in section 1861(lll)), the amount paid shall be the payment amount specified under section 1834(aa) .\n**(2) Payment and limits specified**\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395m ) is amended by adding at the end the following new subsection:\n(aa) Payment and limits for dental and oral health services (1) In general The payment amount under this part for dental and oral health services (as defined in section 1861(nnn)) shall be, subject to paragraph (3), the applicable percent (specified in paragraph (2)) of the lesser of the actual charge for the services or the amount determined under the payment basis determined under section 1848. (2) Applicable percent (A) In general For purposes of paragraph (1), except as provided in subparagraph (B), the applicable percent specified in this paragraph is\u2014 (i) with respect to services described in section 1861(nnn)(1) furnished during 2026 or a subsequent year, 100 percent; and (ii) with respect to services not described in clause (i)\u2014 (I) for a year before 2027, 0 percent; (II) for 2027, 30 percent; (III) for 2028, 60 percent; and (IV) for 2029 and each subsequent year, 80 percent. (B) Special rule for certain low-income individuals For purposes of paragraph (1), the applicable percent specified in this paragraph is, with respect to services furnished to an individual who is a subsidy eligible individual (as defined in section 1860D\u201314(a)(3)), or who would be a subsidy eligible individual if the individual were enrolled in a prescription drug plan or MA\u2013PD plan\u2014 (i) with respect to services described in section 1861(nnn)(1), for 2026 and each subsequent year, 100 percent; and (ii) with respect to services not described in clause (i), for 2027 and each subsequent year, 80 percent. (3) Limitations and Secretarial authority (A) Frequency With respect to dental and oral health services that are\u2014 (i) routine dental cleanings, payment may be made under this part for only two such cleanings during a 12-month period; and (ii) routine exams, payment may be made under this part for only two such exams during a 12-month period. (B) Secretarial authority (i) Authority to apply additional limitations The Secretary may apply such other reasonable limitations on the extent to which dental and oral services are covered under this part, including through application of a prior authorization requirement. (ii) Authority to modify coverage Notwithstanding any other provision of this title, if the Secretary determines appropriate, the Secretary may modify the coverage under this part of dental and oral health services to the extent that such modification is consistent with the recommendations of the United States Preventive Services Task Force. (iii) Authority to waive frequency limitations Notwithstanding subparagraph (A), the Secretary may waive any frequency limitation under such subparagraph for an individual (or category of individuals) if determined appropriate by the Secretary. .\n##### (d) Payment under physician fee schedule\nSection 1848(j)(3) of the Social Security Act ( 42 U.S.C. 1395w\u20134(j)(3) ) is amended by inserting (2)(KK), before (3) .\n##### (e) Dentures\n**(1) In general**\nSection 1861(s)(8) of the Social Security Act ( 42 U.S.C. 1395x(s)(8) ) is amended\u2014\n**(A)**\nby striking (other than dental) and inserting (including dentures) ; and\n**(B)**\nby striking internal body .\n**(2) Special payment rules**\nSection 1834(a) of the Social Security Act ( 42 U.S.C. 1395m(a) ) is amended by adding at the end the following new paragraph:\n(23) Payment and limits for dentures (A) In general The payment amount under this part for dentures shall be, subject to subparagraph (C), the applicable percent (specified in subparagraph (B)) of the amount otherwise payable for such dentures under this section. (B) Applicable percent For purposes of subparagraph (A), the applicable percent specified in this subparagraph is\u2014 (i) for a year before 2027, 0 percent; and (ii) for 2027 and each subsequent year, 80 percent. (C) Limitations and Secretarial authority (i) In general Payment may be made under this part for an individual for\u2014 (I) not more than one full upper and one full lower denture once every five years; and (II) not more than one partial upper denture and one partial lower denture once every five years. (ii) Secretarial authority (I) Authority to apply additional limitations The Secretary may apply such other reasonable limitations on the extent to which dentures are covered under this part, including through application of a prior authorization requirement. (II) Authority to modify coverage Notwithstanding any other provision of this title, if the Secretary determines appropriate, the Secretary may modify the coverage under this part of dentures to the extent that such modification is consistent with the recommendations of the United States Preventive Services Task Force. (III) Authority to waive frequency limitations Notwithstanding clause (i), the Secretary may waive any frequency limitation under such clause for an individual (or category of individuals) if determined appropriate by the Secretary. .\n##### (f) Repeal of ground for exclusion\nSection 1862(a) of the Social Security Act ( 42 U.S.C. 1395y ) is amended by striking paragraph (12).\n##### (g) Effective date\nThe amendments made by this section shall apply to services furnished on or after January 1, 2026.\n#### 3. Vision care\n##### (a) Coverage\nSection 1861(s)(2) of the Social Security Act ( 42 U.S.C. 1395x(s)(2) ), as amended by section 2, is further amended\u2014\n**(1)**\nin subparagraph (JJ), by striking and after the semicolon at the end;\n**(2)**\nin subparagraph (KK), by adding and after the semicolon at the end; and\n**(3)**\nby adding at the end the following new subparagraph:\n(LL) vision services (as defined in subsection (ooo)); .\n##### (b) Vision services defined\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ), as amended by section 2, is further amended by adding at the end the following new subsection:\n(ooo) Vision services The term vision services means\u2014 (1) routine eye examinations and procedures performed (during the course of any eye examination) to determine the refractive state of the eyes; and (2) other necessary services related to eye and vision health (as defined by the Secretary). .\n##### (c) Payment; coinsurance; and limitations\n**(1) In general**\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a)(1) ), as amended by section 2, is further amended\u2014\n**(A)**\nby striking and before (HH) ; and\n**(B)**\nby inserting before the semicolon at the end the following: , and (II) with respect to vision services (as defined in section 1861(mmm)), the amount paid shall be the payment amount specified under section 1834(bb) .\n**(2) Payment and limits specified**\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395m ), as amended by section 2, is further amended by adding at the end the following new subsection:\n(bb) Payment and limits for vision services (1) In general The payment amount under this part for vision services (as defined in section 1861(ooo)) shall be, subject to paragraph (2), 80 percent of the lesser of the actual charge for the services or the amount determined under the payment basis determined under section 1848. (2) Limitations and Secretarial authority (A) Frequency With respect to routine eye exams, payment may be made under this part for only one such exam during a 12-month period. (B) Secretarial authority (i) Authority to apply additional limitations The Secretary may apply other reasonable limitations on the extent to which vision services are covered under this part, including through application of a prior authorization requirement. (ii) Authority to modify coverage Notwithstanding any other provision of this title, if the Secretary determines appropriate, the Secretary may modify the coverage under this part of vision services to the extent that such modification is consistent with the recommendations of the United States Preventive Services Task Force. (iii) Authority to waive frequency limitations Notwithstanding subparagraph (A), the Secretary may waive any frequency limitation under such subparagraph for an individual (or category of individuals) if determined appropriate by the Secretary. .\n##### (d) Payment under physician fee schedule\nSection 1848(j)(3) of the Social Security Act ( 42 U.S.C. 1395w\u20134(j)(3) ) is amended by inserting (2)(LL), after (2)(KK), (as added by section 2).\n##### (e) Special payment rules for eyeglasses, contact lenses, and low vision devices\nSection 1834(a) of the Social Security Act ( 42 U.S.C. 1395m(a) ), as amended by section 2, is further amended by adding at the end the following:\n(24) Payment and limits for eyeglasses and contact lenses (A) In general The payment amount under this part for eyeglass lenses, eyeglass frames, and contact lenses shall be, subject to subparagraph (B), 80 percent of the amount otherwise payable for such eyeglass lenses, eyeglass frames, and contact lenses, respectively, under this section. (B) Limitations and Secretarial authority (i) In general Subject to clause (iii), payment may be made under this part (other than for eyewear described in section 1861(s)(8)) for an individual for\u2014 (I) not more than one pair of eyeglass lenses during any 12-month period in an amount not exceeding $100; (II) not more than one set of eyeglass frames during any 24-month period in an amount not exceeding $100; and (III) contact lenses, only to the extent that the sum of such payments for contact lenses does not exceed a limitation of $200 during any 24-month period beginning during the first year beginning at least six months after the date of the enactment of this paragraph (or, beginning during a subsequent year, such limitation for a 24-month period beginning in the previous year increase by an appropriate inflation adjustment specified by the Secretary). (ii) Secretarial authority (I) Authority to apply additional limitations The Secretary may apply such other reasonable limitations on the extent to which eyeglass lenses, eyeglass frames, and contact lenses are covered under this part, including through application of a prior authorization requirement. (II) Authority to modify coverage Notwithstanding any other provision of this title, if the Secretary determines appropriate, the Secretary may modify the coverage under this part of eyeglass lenses, eyeglass frames, and contact lenses to the extent that such modification is consistent with the recommendations of the United States Preventive Services Task Force. (III) Authority to waive frequency limitations Notwithstanding clause (i), the Secretary may waive any frequency limitation under such clause for an individual (or category of individuals) if determined appropriate by the Secretary. (iii) Update of payment limits to account for inflation With respect to eyeglass lenses and contact lenses furnished during 2027 or a subsequent year, the Secretary shall increase the dollar amounts in effect under this subparagraph for such year by the percentage change in the consumer price index for all urban consumers (United States city average) for the 12-month period ending with June of the previous year. (25) Payment and limits for low vision devices (A) In general The payment amount under this part for low vision devices shall be 80 percent of the amount otherwise payable for low vision devices under this section. (B) Secretarial authority (i) Authority to apply limitations The Secretary may apply reasonable limitations on the extent to which low vision devices are covered under this part, including through application of a prior authorization requirement. (ii) Authority to modify coverage Notwithstanding any other provision of this title, if the Secretary determines appropriate, the Secretary may modify the coverage under this part of low vision devices to the extent that such modification is consistent with the recommendations of the United States Preventive Services Task Force. (C) Low vision device defined In this paragraph, the term low vision device means a device, prescribed by a physician, that magnifies, enhances, or otherwise augments or interprets visual images irrespective of the size, form, or technological features of such device and does not include ordinary eyeglasses or contact lenses. In the previous sentence, the term ordinary eyeglasses or contact lenses means lenses that are intended to fully correct visual acuity or fully eliminate refractive error. .\n##### (f) Definition of durable medical equipment To include eyeglasses, contact lenses, and low vision devices\nSection 1861(n) of the Social Security Act ( 42 U.S.C. 1395x(n) ) is amended\u2014\n**(1)**\nby striking and before eye tracking and inserting a comma; and\n**(2)**\nby inserting , and eyeglass lenses, low vision devices (as defined in section 1834(a)(25)), eyeglass frames, and contact lenses before ; except .\n##### (g) Repeal of ground for exclusion\nSection 1862(a)(7) of the Social Security Act ( 42 U.S.C. 1395y(a)(7) ) is amended by striking , eyeglasses (other than eyewear described in section 1861(s)(8)) or eye examinations for the purpose of prescribing, fitting, or changing eyeglasses, procedures performed (during the course of any eye examination) to determine the refractive state of the eyes .\n##### (h) Effective date\nThe amendments made by this section shall apply to services furnished on or after January 1, 2026.\n#### 4. Hearing care\n##### (a) Coverage\n**(1) In general**\nSection 1861(s)(2) of the Social Security Act ( 42 U.S.C. 1395x(s)(2) ), as amended by sections 2 and 3, is further amended\u2014\n**(A)**\nin subparagraph (KK), by striking and at the end;\n**(B)**\nin subparagraph (LL), by inserting and at the end; and\n**(C)**\nby adding at the end the following new subparagraph:\n(MM) audiology services (as defined in subsection (ll)(3)) and hearing services (as defined in subsection (ll)(5)); .\n**(2) Hearing services defined**\nSection 1861(ll) of the Social Security Act ( 42 U.S.C. 1395x(ll) ) is amended\u2014\n**(A)**\nin the subsection heading, by inserting ; Hearing Services after Audiology Services ; and\n**(B)**\nby adding at the end the following new paragraph:\n(5) The term hearing services means\u2014 (A) routine hearing exams and exams for hearing aids; and (B) other necessary services related to hearing health (as defined by the Secretary). .\n##### (b) Payment; coinsurance; and limitations\n**(1) In general**\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a)(1) ), as amended by sections 2 and 3, is further amended\u2014\n**(A)**\nby striking and before (II) ; and\n**(B)**\nby inserting before the semicolon at the end the following: , and (JJ) with respect to audiology services (as defined in section 1861(ll)(3)) and hearing services (as defined in section 1861(ll)(5)), the amount paid shall be the payment amount specified under section 1834(cc) .\n**(2) Payment and limits specified**\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395m ), as amended by sections 2 and 3, is further amended by adding at the end the following new subsection:\n(cc) Payment and limits for hearing services (1) In general The payment amount under this part for audiology services (as defined in section 1861(ll)(3)) and hearing services (as defined in section 1861(ll)(5)), shall be, subject to paragraph (2), 80 percent of the lesser of the actual charge for the services or the amount determined under the payment basis determined under section 1848. (2) Secretarial authority (A) Authority to apply limitations The Secretary may apply reasonable limitations on the extent to which audiology services and hearing services are covered under this part, including through application of a prior authorization requirement. (B) Authority to modify coverage Notwithstanding any other provision of this title, if the Secretary determines appropriate, the Secretary may modify the coverage under this part of audiology services and hearing services to the extent that such modification is consistent with the recommendations of the United States Preventive Services Task Force. .\n##### (c) Payment under the physician fee schedule\nSection 1848(j)(3) of the Social Security Act ( 42 U.S.C. 1395w\u20134(j)(3) ), as amended by section 2(d), is further amended by inserting (2)(MM), before (3) .\n##### (d) Hearing aids\n**(1) Repeal of ground for exclusion**\nSection 1862(a)(7) of the Social Security Act ( 42 U.S.C. 1395y(a)(7) ), as amended by section 3(g), is further amended by striking , hearing aids or examinations therefor, .\n**(2) Definition of durable medical equipment to include hearing aids**\nSection 1861(n) of the Social Security Act ( 42 U.S.C. 1395x(n) ), as amended by section 3, is further amended by inserting hearing aids, before and eyeglass lenses .\n**(3) Special payment rules for hearing aids**\nSection 1834(a) of the Social Security Act ( 42 U.S.C. 1395m(a) ), as amended by sections 2 and 3, is further amended by adding at the end the following new paragraph:\n(26) Payment and limits for hearing aids (A) In general The payment amount under this part for hearing aids shall be, subject to subparagraph (B), 80 percent of the amount otherwise payable for hearing aids under this section. (B) Limitations and Secretarial authority (i) In general Payment may be made under this part for an individual for not more than one hearing aid per ear during a 48-month period. (ii) Secretarial authority (I) Authority to apply additional limitations The Secretary may apply additional limitations on the extent to which hearing aids are covered under this part, including through application of a prior authorization requirement and through application of criteria for a minimum level of hearing loss for coverage of an initial or replacement hearing aid. (II) Authority to modify coverage Notwithstanding any other provision of this title, if the Secretary determines appropriate, the Secretary may modify the coverage under this part of hearing aids to the extent that such modification is consistent with the recommendations of the United States Preventive Services Task Force. (iii) Authority to waive frequency limitations Notwithstanding clause (i), the Secretary may waive any frequency limitation under such clause for an individual (or category of individuals) if determined appropriate by the Secretary. .\n##### (e) Effective date\nThe amendments made by this section shall apply to services furnished on or after January 1, 2026.\n#### 5. Nonapplication of competitive acquisition to certain items\nSection 1847(a)(2) of the Social Security Act ( 42 U.S.C. 1395w\u20133(a)(2) ) is amended\u2014\n**(1)**\nby striking and excluding and inserting excluding ; and\n**(2)**\nby inserting , and excluding dentures, eyeglass lenses, contact lenses, and hearing aids before the period at the end.\n#### 6. Inclusion of an oral health professional on the United States Preventive Services Task Force\n##### (a) In general\nThe first sentence of section 915(a)(1) of the Public Health Service Act ( 42 U.S.C. 299b\u20134(a)(1) ) is amended by inserting , including at least 1 oral health professional before the period at the end.\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply beginning on January 1 of the first year beginning at least 6 months after the date of the enactment of this Act.",
      "versionDate": "2025-03-11",
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
        "name": "Health",
        "updateDate": "2025-03-27T14:35:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119hr2045",
          "measure-number": "2045",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2045v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Medicare Dental, Vision, and Hearing Benefit Act of 2025</strong></p><p>This bill provides for Medicare coverage of dental, vision, and hearing care. Coverage includes (1) routine dental cleanings and exams, basic and major dental services, emergency dental care, and dentures; (2) routine eye exams, eyeglasses, and contact lenses; and (3) routine hearing exams, hearing aids, and exams for hearing aids. With respect to such care, the bill establishes special payment rules, limitations, and coinsurance requirements.</p>"
        },
        "title": "Medicare Dental, Vision, and Hearing Benefit Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2045.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicare Dental, Vision, and Hearing Benefit Act of 2025</strong></p><p>This bill provides for Medicare coverage of dental, vision, and hearing care. Coverage includes (1) routine dental cleanings and exams, basic and major dental services, emergency dental care, and dentures; (2) routine eye exams, eyeglasses, and contact lenses; and (3) routine hearing exams, hearing aids, and exams for hearing aids. With respect to such care, the bill establishes special payment rules, limitations, and coinsurance requirements.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr2045"
    },
    "title": "Medicare Dental, Vision, and Hearing Benefit Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicare Dental, Vision, and Hearing Benefit Act of 2025</strong></p><p>This bill provides for Medicare coverage of dental, vision, and hearing care. Coverage includes (1) routine dental cleanings and exams, basic and major dental services, emergency dental care, and dentures; (2) routine eye exams, eyeglasses, and contact lenses; and (3) routine hearing exams, hearing aids, and exams for hearing aids. With respect to such care, the bill establishes special payment rules, limitations, and coinsurance requirements.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr2045"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2045ih.xml"
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
      "title": "Medicare Dental, Vision, and Hearing Benefit Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T17:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicare Dental, Vision, and Hearing Benefit Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T17:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide for coverage of dental, vision, and hearing care under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T17:18:23Z"
    }
  ]
}
```
