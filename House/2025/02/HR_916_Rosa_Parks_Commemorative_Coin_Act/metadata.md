# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/916?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/916
- Title: Rosa Parks Commemorative Coin Act
- Congress: 119
- Bill type: HR
- Bill number: 916
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-02-10T09:05:22Z
- Update date including text: 2026-02-10T09:05:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H452)
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H452)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/916",
    "number": "916",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001281",
        "district": "3",
        "firstName": "Joyce",
        "fullName": "Rep. Beatty, Joyce [D-OH-3]",
        "lastName": "Beatty",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Rosa Parks Commemorative Coin Act",
    "type": "HR",
    "updateDate": "2026-02-10T09:05:22Z",
    "updateDateIncludingText": "2026-02-10T09:05:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
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
      "actionCode": "B00100",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H452)",
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
          "date": "2025-02-04T17:06:05Z",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "RI"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MO"
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
      "sponsorshipDate": "2025-02-04",
      "state": "GA"
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
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "OR"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IN"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-04",
      "state": "LA"
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
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "MO"
    },
    {
      "bioguideId": "C000537",
      "district": "6",
      "firstName": "James",
      "fullName": "Rep. Clyburn, James E. [D-SC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyburn",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "SC"
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
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "LA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "AL"
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
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
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
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
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
      "sponsorshipDate": "2025-02-04",
      "state": "MA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "GA"
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
      "sponsorshipDate": "2025-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
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
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "WI"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CO"
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
      "sponsorshipDate": "2025-02-04",
      "state": "DC"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VI"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VA"
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
      "sponsorshipDate": "2025-02-04",
      "state": "AL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "WA"
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
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "MS"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "T000489",
      "district": "18",
      "firstName": "Sylvester",
      "fullName": "Rep. Turner, Sylvester [D-TX-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-02-04",
      "state": "GA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "IL"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "MD"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr916ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 916\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mrs. Beatty (for herself, Ms. Adams , Mr. Amo , Mr. Bell , Mr. Bishop , Ms. Brown , Ms. Brownley , Ms. Bynum , Mr. Carson , Mr. Casten , Mr. Carter of Louisiana , Mrs. Cherfilus-McCormick , Ms. Clarke of New York , Mr. Cleaver , Mr. Clyburn , Mr. Conaway , Ms. Crockett , Mr. Davis of Illinois , Mr. Davis of North Carolina , Mr. Fields , Mr. Figures , Mrs. Foushee , Mr. Frost , Mr. Goldman of New York , Mr. Green of Texas , Mr. Grijalva , Mrs. Hayes , Mr. Horsford , Mr. Ivey , Mr. Jackson of Illinois , Mr. Johnson of Georgia , Ms. Johnson of Texas , Ms. Kamlager-Dove , Ms. Kelly of Illinois , Mr. Kennedy of New York , Ms. Lee of Pennsylvania , Mr. Lynch , Mrs. McBath , Ms. McClellan , Mrs. McIver , Mr. Meeks , Ms. Moore of Wisconsin , Mr. Neguse , Ms. Norton , Ms. Plaskett , Mr. Scott of Virginia , Ms. Sewell , Ms. Simon , Ms. Strickland , Ms. Stevens , Mrs. Sykes , Mr. Thanedar , Mr. Thompson of Mississippi , Ms. Tlaib , Mr. Turner of Texas , Ms. Underwood , Mr. Vargas , Mr. Veasey , Ms. Waters , Mrs. Watson Coleman , Ms. Williams of Georgia , and Ms. Pressley ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Secretary of the Treasury to mint commemorative coins in recognition of the life and legacy of Rosa Parks.\n#### 1. Short title\nThis Act may be cited as the Rosa Parks Commemorative Coin Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nRosa Parks, widely celebrated as the Mother of the Civil Rights Movement , became an iconic figure when she refused to give up her seat on a segregated bus in Montgomery, Alabama, on December 1, 1955, igniting a pivotal movement that challenged racial segregation and forever altered the course of American history.\n**(2)**\nBorn on February 4, 1913, in Tuskegee, Alabama, to Leona McCauley, a teacher, and James McCauley, a carpenter, Parks grew up in the segregated South, experiencing firsthand the harsh realities of racial injustice.\n**(3)**\nDespite the profound challenges of racial inequality, Parks attended segregated schools in Alabama, graduating high school in 1933, where her education and experiences fueled her lifelong commitment to activism.\n**(4)**\nIn 1943, Parks became deeply involved with the National Association for the Advancement of Colored People, where she served as Secretary and Youth Leader, investigating cases of racial violence such as the rape of Recy Taylor and the lynching of Emmett Till.\n**(5)**\nOn December 1, 1955, Parks was arrested for refusing to give up her seat to a White man on a segregated bus in Montgomery, Alabama, an act that led to the historic 381-day Montgomery Bus Boycott by more than 40,000 riders.\n**(6)**\nThe boycott sparked a legal challenge to Montgomery\u2019s bus segregation laws, which culminated in the Supreme Court\u2019s landmark decision in Browder v. Gayle declaring bus segregation unconstitutional on November 13, 1956.\n**(7)**\nFollowing the boycott, Parks faced significant personal and economic hardships, including the loss of her job and ongoing threats to her life, yet her determination to fight for justice remained steadfast.\n**(8)**\nIn 1957, Parks moved to Detroit, Michigan, where she continued her work as an advocate for racial equality, focusing on economic justice, political participation, and racial integration.\n**(9)**\nParks became a global symbol of resistance to racial segregation and injustice, and her act of defiance inspired civil rights movements around the world.\n**(10)**\nThroughout her life, Parks remained committed to civil rights activism, participating in marches and speaking engagements, as well as mentoring younger generations of activists, furthering her legacy of leadership in the struggle for racial equality.\n**(11)**\nParks passed away on October 24, 2005, at the age of 92, leaving an enduring legacy of courage, resilience, and leadership that continues to inspire social justice and equality advocates across the globe.\n**(12)**\nIn recognition of her profound impact, Parks became the first woman and second African American to lie in honor in the United States Capitol Rotunda.\n**(13)**\nIn 1996, President Bill Clinton awarded Parks the Presidential Medal of Freedom, the highest civilian honor bestowed by the President of the United States.\n**(14)**\nIn 1999, Parks received the Congressional Gold Medal, the highest expression of national appreciation for distinguished achievements and contributions bestowed by the United States Congress.\n**(15)**\nParks\u2019 legacy is commemorated through numerous schools, streets, transit stations, and monuments named in her honor, ensuring that her contributions to American history are remembered and celebrated.\n**(16)**\nIn 2006, Ohio became the first state to designate December 1, the day of Parks\u2019 arrest, as Rosa Parks Day, garnering unanimous support from the state legislature and being signed into law by Governor Bob Taft.\n**(17)**\nRosa Parks Day is also celebrated in the states of California, Massachusetts, Michigan, Missouri, and New York on her birthday, February 4, and in Alabama, Oregon, Tennessee, and Texas on December 1.\n**(18)**\nIt is fitting and proper to recognize and preserve the achievements and impact of Rosa Parks, whose personal sacrifice, unwavering resistance, and inspirational advocacy were essential to the success of the Civil Rights Movement, and whose legacy continues to serve as a beacon of hope and inspiration for future generations.\n#### 3. Coin specifications\n##### (a) Denominations\nIn recognition and celebration of Rosa Parks, the Secretary of the Treasury (hereafter in this Act referred to as the Secretary ) shall mint and issue the following coins:\n**(1) $5 gold coins**\nNot more than 50,000 $5 coins, which shall\u2014\n**(A)**\nweigh 8.359 grams;\n**(B)**\nhave a diameter of 0.850 inches; and\n**(C)**\ncontain at least 90 percent gold.\n**(2) $1 silver coins**\nNot more than 400,000 $1 coins, which shall\u2014\n**(A)**\nweigh 26.73 grams;\n**(B)**\nhave a diameter of 1.500 inches; and\n**(C)**\ncontain at least 90 percent silver.\n**(3) Half-dollar clad coins**\nNot more than 750,000 half-dollar coins which shall\u2014\n**(A)**\nweigh 11.34 grams;\n**(B)**\nhave a diameter of 1.205 inches; and\n**(C)**\nbe minted to the specifications for half-dollar coins contained in section 5112(b) of title 31, United States Code.\n##### (b) Legal tender\nThe coins minted under this Act shall be legal tender, as provided in section 5103 of title 31, United States Code.\n##### (c) Numismatic items\nFor purposes of sections 5134 and 5136 of title 31, United States Code, all coins minted under this Act shall be considered to be numismatic items.\n#### 4. Designs of coins\n##### (a) Design requirements\n**(1) In general**\nThe designs of the coins minted under this Act shall be emblematic of the legacy of Rosa Parks as a leader of the Civil Rights Movement. At least one obverse design shall bear the name and likeness of Rosa Parks.\n**(2) Designation and inscriptions**\nOn each coin minted under this Act, there shall be\u2014\n**(A)**\na designation of the value of the coin;\n**(B)**\nan inscription of the year 2029 ; and\n**(C)**\ninscriptions of the words Liberty , In God We Trust , United States of America , and E Pluribus Unum .\n##### (b) Selection\nThe designs for the coins minted under this Act shall be\u2014\n**(1)**\nselected by the Secretary, after consultation with\u2014\n**(A)**\nthe Rosa and Raymond Parks Institute for Self Development; and\n**(B)**\nthe Commission of Fine Arts; and\n**(2)**\nreviewed by the Citizens Coinage Advisory Committee.\n#### 5. Issuance of coins\n##### (a) Quality of coins\nCoins minted under this Act shall be issued in uncirculated and proof qualities.\n##### (b) Period for issuance\nThe Secretary may issue coins minted under this Act only during the calendar year beginning on January 1, 2029.\n#### 6. Sale of coins\n##### (a) Sale price\nThe coins issued under this Act shall be sold by the Secretary at a price equal to the sum of\u2014\n**(1)**\nthe face value of the coins;\n**(2)**\nthe surcharge provided in section 7(a) with respect to such coins; and\n**(3)**\nthe cost of designing and issuing the coins (including labor, materials, dies, use of machinery, overhead expenses, marketing, and shipping).\n##### (b) Bulk sales\nThe Secretary shall make bulk sales of the coins issued under this Act at a reasonable discount.\n##### (c) Prepaid orders\n**(1) In general**\nThe Secretary shall accept prepaid orders for the coins minted under this Act before the issuance of the coins.\n**(2) Discount**\nSale prices with respect to prepaid orders under paragraph (1) shall be at a reasonable discount.\n#### 7. Surcharges\n##### (a) In general\nAll sales of coins minted under this Act shall include a surcharge as follows:\n**(1)**\nA surcharge of $35 per coin for the $5 coins.\n**(2)**\nA surcharge of $10 per coin for the $1 coins.\n**(3)**\nA surcharge of $5 per coin for the half-dollar coins.\n##### (b) Distribution\nSubject to section 5134(f)(1) of title 31, United States Code, all surcharges received by the Secretary from the sale of coins issued under this Act shall be promptly paid by the Secretary to the Rosa and Raymond Parks Institute for Self Development, for the purpose of accomplishing and advancing its mission to carry on the work of Rosa Parks in youth development and civil rights education and advocacy.\n##### (c) Audits\nThe Rosa and Raymond Parks Institute for Self Development shall be subject to the audit requirements of section 5134(f)(2) of title 31, United States Code, with regard to the amounts received under subsection (b).\n##### (d) Limitation\nNotwithstanding subsection (a), no surcharge may be included with respect to the issuance under this Act of any coin during a calendar year if, as of the time of such issuance, the issuance of such coin would result in the number of commemorative coin programs issued during such year to exceed the annual 2 commemorative coin program issuance limitation under section 5112(m)(1) of title 31, United States Code. The Secretary may issue guidance to carry out this subsection.\n#### 8. Financial assurances\nThe Secretary shall take such actions as may be necessary to ensure that\u2014\n**(1)**\nminting and issuing coins under this Act will not result in any net cost to the United States Government; and\n**(2)**\nno funds, including applicable surcharges, are disbursed to any recipient designated in section 7(b) until the total cost of designing and issuing all of the coins authorized by this Act (including labor, materials, dies, use of machinery, winning design compensation, overhead expenses, marketing, and shipping) is recovered by the United States Treasury, consistent with sections 5112(m) and 5134(f) of title 31, United States Code.",
      "versionDate": "2025-02-04",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-07T13:42:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr916",
          "measure-number": "916",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-06-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr916v00",
            "update-date": "2025-06-03"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rosa Parks Commemorative Coin Act</strong></p><p>This bill directs the Department of the Treasury to mint and issue coins in recognition and celebration of Rosa Parks. All sales of coins issued under this bill must include a surcharge to be paid to the Rosa and Raymond Parks Institute for Self Development.</p>"
        },
        "title": "Rosa Parks Commemorative Coin Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr916.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rosa Parks Commemorative Coin Act</strong></p><p>This bill directs the Department of the Treasury to mint and issue coins in recognition and celebration of Rosa Parks. All sales of coins issued under this bill must include a surcharge to be paid to the Rosa and Raymond Parks Institute for Self Development.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119hr916"
    },
    "title": "Rosa Parks Commemorative Coin Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rosa Parks Commemorative Coin Act</strong></p><p>This bill directs the Department of the Treasury to mint and issue coins in recognition and celebration of Rosa Parks. All sales of coins issued under this bill must include a surcharge to be paid to the Rosa and Raymond Parks Institute for Self Development.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119hr916"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr916ih.xml"
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
      "title": "Rosa Parks Commemorative Coin Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rosa Parks Commemorative Coin Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Treasury to mint commemorative coins in recognition of the life and legacy of Rosa Parks.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:52Z"
    }
  ]
}
```
