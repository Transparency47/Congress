# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1638?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1638
- Title: CROWN Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1638
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2025-12-05T21:40:07Z
- Update date including text: 2025-12-05T21:40:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1638",
    "number": "1638",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "CROWN Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:40:07Z",
    "updateDateIncludingText": "2025-12-05T21:40:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:05:50Z",
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
          "date": "2025-02-26T15:05:45Z",
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
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
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
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MO"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NC"
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
      "sponsorshipDate": "2025-02-26",
      "state": "OH"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
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
      "sponsorshipDate": "2025-02-26",
      "state": "AL"
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
      "sponsorshipDate": "2025-02-26",
      "state": "DC"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "LA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "KY"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OH"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WI"
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
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
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
      "sponsorshipDate": "2025-02-26",
      "state": "OH"
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
      "sponsorshipDate": "2025-02-26",
      "state": "MS"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WA"
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
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-26",
      "state": "AZ"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IN"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
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
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NV"
    },
    {
      "bioguideId": "T000489",
      "district": "18",
      "firstName": "Sylvester",
      "fullName": "Rep. Turner, Sylvester [D-TX-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
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
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-26",
      "state": "NC"
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
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
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
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "RI"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-26",
      "state": "VI"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CT"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WA"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
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
      "sponsorshipDate": "2025-02-26",
      "state": "LA"
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
      "sponsorshipDate": "2025-02-26",
      "state": "OR"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MO"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MD"
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
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WI"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MN"
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
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "J000294",
      "district": "8",
      "firstName": "Hakeem",
      "fullName": "Rep. Jeffries, Hakeem S. [D-NY-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Jeffries",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
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
      "sponsorshipDate": "2025-02-27",
      "state": "MA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "OR"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "AZ"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "IL"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OH"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "WA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1638ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1638\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mrs. Watson Coleman (for herself, Ms. Williams of Georgia , Ms. McClellan , Mr. Smith of Washington , Mr. Johnson of Georgia , Mrs. Ramirez , Mr. Cleaver , Mr. Doggett , Ms. Adams , Ms. Brown , Mr. Cohen , Ms. Tlaib , Ms. Sewell , Ms. Norton , Mr. Green of Texas , Ms. Jacobs , Ms. Underwood , Mr. Kennedy of New York , Mr. Fields , Mr. Mullin , Ms. Wilson of Florida , Ms. Kamlager-Dove , Mrs. Cherfilus-McCormick , Mr. Krishnamoorthi , Mr. McGarvey , Mrs. McIver , Mrs. Beatty , Mr. Pocan , Ms. Kelly of Illinois , Ms. Sherrill , Mrs. Sykes , Mr. Thompson of Mississippi , Ms. Strickland , Mr. Meeks , Mr. Foster , Mr. Grijalva , Mr. Carson , Mr. Espaillat , Ms. Clarke of New York , Mr. Evans of Pennsylvania , Mr. Quigley , Mr. Horsford , Mr. Turner of Texas , Ms. Brownley , Ms. Stevens , Mr. Tonko , Mr. Takano , Mr. Torres of New York , Mr. Davis of Illinois , Mr. Vargas , Mrs. Foushee , Mr. Conaway , Mr. Davis of North Carolina , Mr. Amo , Mr. Ivey , Mr. Jackson of Illinois , Ms. Plaskett , Mrs. Hayes , Ms. Jayapal , Mr. Menendez , Mr. Carter of Louisiana , Ms. Bynum , Ms. Ocasio-Cortez , Mrs. McBath , Mr. Bell , Ms. Waters , Mr. Veasey , Mr. Mfume , Ms. Vel\u00e1zquez , Ms. Pressley , Ms. Moore of Wisconsin , Ms. Omar , Ms. Lee of Pennsylvania , Mr. Frost , and Mr. Jeffries ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit discrimination based on an individual\u2019s texture or style of hair.\n#### 1. Short title\nThis Act may be cited as the Creating a Respectful and Open World for Natural Hair Act of 2025 or the CROWN Act of 2025 .\n#### 2. Findings; sense of Congress; purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThroughout United States history, society has used (in conjunction with skin color) hair texture and hairstyle to classify individuals on the basis of race.\n**(2)**\nLike one\u2019s skin color, one\u2019s hair has served as a basis of race and national origin discrimination.\n**(3)**\nRacial and national origin discrimination can and do occur because of longstanding racial and national origin biases and stereotypes associated with hair texture and style.\n**(4)**\nFor example, people of African descent have been deprived of educational and employment opportunities because they are adorned with natural or protective hairstyles in which hair is tightly coiled or tightly curled, or worn in locs, cornrows, twists, braids, Bantu knots, or Afros.\n**(5)**\nRacial and national origin discrimination is reflected in school and workplace policies and practices that bar natural or protective hairstyles commonly worn by people of African descent.\n**(6)**\nFor example, as recently as 2018, the United States Armed Forces had grooming policies that barred natural or protective hairstyles that servicewomen of African descent commonly wear and that described these hairstyles as unkempt .\n**(7)**\nIn 2018, the United States Armed Forces rescinded these policies and recognized that this description perpetuated derogatory racial stereotypes.\n**(8)**\nThe United States Armed Forces also recognized that prohibitions against natural or protective hairstyles that African-American servicewomen are commonly adorned with are racially discriminatory and bear no relationship to African-American servicewomen\u2019s occupational qualifications and their ability to serve and protect the Nation.\n**(9)**\nSome Federal courts have narrowly interpreted the protections against discrimination on the basis of race or national origin found in existing Federal civil rights laws, including provisions of the Civil Rights Act of 1964 ( 42 U.S.C. 2000a et seq. ), section 1977 of the Revised Statutes ( 42 U.S.C. 1981 ), and the Fair Housing Act ( 42 U.S.C. 3601 et seq. ), thereby permitting, for example, employers to discriminate against people of African descent who wear natural or protective hairstyles, even though the employment policies involved are not related to workers\u2019 ability to perform their jobs.\n**(10)**\nApplying these narrow interpretations has resulted in a lack of Federal civil rights protection for individuals who are discriminated against on the basis of characteristics that are commonly associated with race and national origin.\n**(11)**\nStarting in 2019, State legislatures and municipal bodies throughout the United States have introduced and passed legislation that rejects certain Federal courts\u2019 restrictive interpretation of race and national origin, and expressly classifies race and national origin discrimination as inclusive of discrimination on the basis of natural or protective hairstyles commonly associated with race and national origin.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Federal Government should acknowledge that individuals who have hair texture or wear a hairstyle that is historically and contemporarily associated with African Americans or persons of African descent have suffered harmful discrimination in schools, workplaces, and other contexts based upon longstanding race and national origin stereotypes and biases;\n**(2)**\na clear and comprehensive law should address the deprivation of educational, employment, and other opportunities on the basis of hair texture and hairstyle that are commonly associated with race or national origin;\n**(3)**\nclear, consistent, and enforceable legal standards must be provided to redress the widespread incidences of race and national origin discrimination based upon hair texture and hairstyle in schools, workplaces, housing, federally funded institutions, and other contexts;\n**(4)**\nit is necessary to prevent educational, employment, and other decisions, practices, and policies generated by or reflecting negative biases and stereotypes related to race or national origin;\n**(5)**\nthe Federal Government must play a key role in enforcing Federal civil rights laws in a way that secures equal educational, employment, and other opportunities for all individuals regardless of their race or national origin;\n**(6)**\nthe Federal Government must play a central role in enforcing the standards established under this Act on behalf of individuals who suffer race or national origin discrimination based upon hair texture and hairstyle;\n**(7)**\nit is necessary to prohibit and provide remedies for the harms suffered as a result of race or national origin discrimination on the basis of hair texture and hairstyle; and\n**(8)**\nit is necessary to mandate that school, workplace, and other applicable standards be applied in a nondiscriminatory manner and to explicitly prohibit the adoption or implementation of grooming requirements that disproportionately impact people of African descent.\n##### (c) Purpose\nThe purpose of this Act is to institute definitions of race and national origin for Federal civil rights laws that effectuate the comprehensive scope of protection Congress intended to be afforded by such laws and Congress\u2019 objective to eliminate race and national origin discrimination in the United States.\n#### 3. Federally assisted programs\n##### (a) In general\nNo individual in the United States shall be excluded from participation in, be denied the benefits of, or be subjected to discrimination under, any program or activity receiving Federal financial assistance, based on the individual\u2019s hair texture or hairstyle, if that hair texture or that hairstyle is commonly associated with a particular race or national origin (including a hairstyle in which hair is tightly coiled or tightly curled, locs, cornrows, twists, braids, Bantu knots, and Afros).\n##### (b) Enforcement\nSubsection (a) shall be enforced in the same manner and by the same means, including with the same jurisdiction, as if such subsection was incorporated in title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ), and as if a violation of subsection (a) was treated as if it was a violation of section 601 of such Act ( 42 U.S.C. 2000d ).\n##### (c) Definitions\nIn this section\u2014\n**(1)**\nthe term program or activity has the meaning given the term in section 606 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d\u20134a ); and\n**(2)**\nthe terms race and national origin mean, respectively, race within the meaning of the term in section 601 of that Act ( 42 U.S.C. 2000d ) and national origin within the meaning of the term in that section 601.\n#### 4. Housing programs\n##### (a) In general\nNo person in the United States shall be subjected to a discriminatory housing practice based on the person\u2019s hair texture or hairstyle, if that hair texture or that hairstyle is commonly associated with a particular race or national origin (including a hairstyle in which hair is tightly coiled or tightly curled, locs, cornrows, twists, braids, Bantu knots, and Afros).\n##### (b) Enforcement\nSubsection (a) shall be enforced in the same manner and by the same means, including with the same jurisdiction, as if such subsection was incorporated in the Fair Housing Act ( 42 U.S.C. 3601 et seq. ), and as if a violation of subsection (a) was treated as if it was a discriminatory housing practice.\n##### (c) Definition\nIn this section\u2014\n**(1)**\nthe terms discriminatory housing practice and person have the meanings given the terms in section 802 of the Fair Housing Act ( 42 U.S.C. 3602 ); and\n**(2)**\nthe terms race and national origin mean, respectively, race within the meaning of the term in section 804 of that Act ( 42 U.S.C. 3604 ) and national origin within the meaning of the term in that section 804.\n#### 5. Public accommodations\n##### (a) In general\nNo person in the United States shall be subjected to a practice prohibited under section 201, 202, or 203 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000a et seq. ), based on the person\u2019s hair texture or hairstyle, if that hair texture or that hairstyle is commonly associated with a particular race or national origin (including a hairstyle in which hair is tightly coiled or tightly curled, locs, cornrows, twists, braids, Bantu knots, and Afros).\n##### (b) Enforcement\nSubsection (a) shall be enforced in the same manner and by the same means, including with the same jurisdiction, as if such subsection was incorporated in title II of the Civil Rights Act of 1964, and as if a violation of subsection (a) was treated as if it was a violation of section 201, 202, or 203, as appropriate, of such Act.\n##### (c) Definition\nIn this section, the terms race and national origin mean, respectively, race within the meaning of the term in section 201 of that Act ( 42 U.S.C. 2000a ) and national origin within the meaning of the term in that section 201.\n#### 6. Employment\n##### (a) Prohibition\nIt shall be an unlawful employment practice for an employer, employment agency, labor organization, or joint labor-management committee controlling apprenticeship or other training or retraining (including on-the-job training programs) to fail or refuse to hire or to discharge any individual, or otherwise to discriminate against an individual, based on the individual\u2019s hair texture or hairstyle, if that hair texture or that hairstyle is commonly associated with a particular race or national origin (including a hairstyle in which hair is tightly coiled or tightly curled, locs, cornrows, twists, braids, Bantu knots, and Afros).\n##### (b) Enforcement\nSubsection (a) shall be enforced in the same manner and by the same means, including with the same jurisdiction, as if such subsection was incorporated in title VII of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e et seq. ), and as if a violation of subsection (a) was treated as if it was a violation of section 703 or 704, as appropriate, of such Act ( 42 U.S.C. 2000e\u20132 , 2000e\u20133).\n##### (c) Definitions\nIn this section the terms person , race , and national origin have the meanings given the terms in section 701 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e ).\n#### 7. Equal rights under the law\n##### (a) In general\nNo person in the United States shall be subjected to a practice prohibited under section 1977 of the Revised Statutes ( 42 U.S.C. 1981 ), based on the person\u2019s hair texture or hairstyle, if that hair texture or that hairstyle is commonly associated with a particular race or national origin (including a hairstyle in which hair is tightly coiled or tightly curled, locs, cornrows, twists, braids, Bantu knots, and Afros).\n##### (b) Enforcement\nSubsection (a) shall be enforced in the same manner and by the same means, including with the same jurisdiction, as if such subsection was incorporated in section 1977 of the Revised Statutes, and as if a violation of subsection (a) was treated as if it was a violation of that section 1977.\n#### 8. Rule of construction\nNothing in this Act shall be construed to limit definitions of race or national origin under the Civil Rights Act of 1964 ( 42 U.S.C. 2000a et seq. ), the Fair Housing Act ( 42 U.S.C. 3601 et seq. ), or section 1977 of the Revised Statutes ( 42 U.S.C. 1981 ).",
      "versionDate": "2025-02-26",
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
        "actionDate": "2025-02-26",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "751",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CROWN Act of 2025",
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
            "name": "Cosmetics and personal care",
            "updateDate": "2025-07-24T14:43:20Z"
          },
          {
            "name": "Due process and equal protection",
            "updateDate": "2025-07-24T14:43:20Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-07-24T14:43:20Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-07-24T14:43:20Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-07-24T14:43:20Z"
          },
          {
            "name": "Housing discrimination",
            "updateDate": "2025-07-24T14:43:20Z"
          },
          {
            "name": "Poverty and welfare assistance",
            "updateDate": "2025-07-24T14:43:20Z"
          },
          {
            "name": "Public housing",
            "updateDate": "2025-07-24T14:43:20Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-07-24T14:43:20Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-24T14:43:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-03-21T14:39:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119hr1638",
          "measure-number": "1638",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-09-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1638v00",
            "update-date": "2025-09-19"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Creating a Respectful and Open World for Natural Hair Act of 2025 or the CROWN Act of 2025</strong></p><p>This bill prohibits discrimination based on a person's hair texture or hairstyle if that style or texture is commonly associated with a particular race or national origin. Specifically, the bill prohibits this type of discrimination against those participating in federally assisted programs, housing programs, public accommodations, and employment.</p><p>Persons shall not be deprived of equal rights under the law and shall not be subjected to prohibited practices based on their hair texture or style.</p><p>The bill provides for enforcement procedures under the applicable laws (e.g., the Civil Rights Act\u00a0of 1964).</p>"
        },
        "title": "CROWN Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1638.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Creating a Respectful and Open World for Natural Hair Act of 2025 or the CROWN Act of 2025</strong></p><p>This bill prohibits discrimination based on a person's hair texture or hairstyle if that style or texture is commonly associated with a particular race or national origin. Specifically, the bill prohibits this type of discrimination against those participating in federally assisted programs, housing programs, public accommodations, and employment.</p><p>Persons shall not be deprived of equal rights under the law and shall not be subjected to prohibited practices based on their hair texture or style.</p><p>The bill provides for enforcement procedures under the applicable laws (e.g., the Civil Rights Act\u00a0of 1964).</p>",
      "updateDate": "2025-09-19",
      "versionCode": "id119hr1638"
    },
    "title": "CROWN Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Creating a Respectful and Open World for Natural Hair Act of 2025 or the CROWN Act of 2025</strong></p><p>This bill prohibits discrimination based on a person's hair texture or hairstyle if that style or texture is commonly associated with a particular race or national origin. Specifically, the bill prohibits this type of discrimination against those participating in federally assisted programs, housing programs, public accommodations, and employment.</p><p>Persons shall not be deprived of equal rights under the law and shall not be subjected to prohibited practices based on their hair texture or style.</p><p>The bill provides for enforcement procedures under the applicable laws (e.g., the Civil Rights Act\u00a0of 1964).</p>",
      "updateDate": "2025-09-19",
      "versionCode": "id119hr1638"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1638ih.xml"
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
      "title": "CROWN Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T07:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CROWN Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Creating a Respectful and Open World for Natural Hair Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit discrimination based on an individual's texture or style of hair.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T07:18:30Z"
    }
  ]
}
```
