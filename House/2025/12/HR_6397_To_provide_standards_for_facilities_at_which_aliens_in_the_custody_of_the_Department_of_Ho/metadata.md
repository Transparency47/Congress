# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6397?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6397
- Title: Dignity for Detained Immigrants Act
- Congress: 119
- Bill type: HR
- Bill number: 6397
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-05-16T08:07:50Z
- Update date including text: 2026-05-16T08:07:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-04 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2025-12-04 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-04 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2025-12-04 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6397",
    "number": "6397",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "J000298",
        "district": "7",
        "firstName": "Pramila",
        "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
        "lastName": "Jayapal",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Dignity for Detained Immigrants Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:50Z",
    "updateDateIncludingText": "2026-05-16T08:07:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Oversight, Investigations, and Accountability Subcommittee",
          "systemCode": "hshm09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight, Investigations, and Accountability.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-12-04T05:00:00Z",
                "name": "Referred to"
              }
            },
            "name": "Border Security and Enforcement Subcommittee",
            "systemCode": "hshm11"
          },
          {
            "activities": {
              "item": {
                "date": "2025-12-04T05:00:00Z",
                "name": "Referred to"
              }
            },
            "name": "Oversight, Investigations, and Accountability Subcommittee",
            "systemCode": "hshm09"
          }
        ]
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-03T15:02:10Z",
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
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "WA"
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "RI"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-03",
      "state": "VA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "TX"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "TX"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "FL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "TN"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "CO"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "MI"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "TX"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "PA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "TX"
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
      "sponsorshipDate": "2025-12-03",
      "state": "NC"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "TX"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "NM"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "MA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "WI"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "NJ"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "MA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
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
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "WA"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MD"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "NM"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "WA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "FL"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "FL"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "PR"
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
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-04",
      "state": "WA"
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
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "WA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MD"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MO"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CO"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MD"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NJ"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "N000015",
      "district": "1",
      "firstName": "Richard",
      "fullName": "Rep. Neal, Richard E. [D-MA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Neal",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6397ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6397\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Ms. Jayapal (for herself, Mr. Smith of Washington , Ms. Adams , Mr. Amo , Ms. Ansari , Ms. Balint , Ms. Barrag\u00e1n , Mr. Beyer , Ms. Bonamici , Mr. Boyle of Pennsylvania , Ms. Brown , Ms. Brownley , Mr. Carson , Mr. Carter of Louisiana , Mr. Casar , Mr. Casten , Mr. Castro of Texas , Mrs. Cherfilus-McCormick , Ms. Chu , Ms. Clarke of New York , Mr. Cleaver , Mr. Cohen , Mr. Correa , Ms. Crockett , Mr. Crow , Mr. Davis of Illinois , Ms. Dean of Pennsylvania , Ms. DeGette , Mr. DeSaulnier , Ms. Dexter , Mrs. Dingell , Mr. Doggett , Ms. Escobar , Mr. Espaillat , Mr. Evans of Pennsylvania , Mrs. Fletcher , Mrs. Foushee , Ms. Friedman , Mr. Frost , Mr. Garamendi , Mr. Garc\u00eda of Illinois , Mr. Garcia of California , Ms. Garcia of Texas , Mr. Goldman of New York , Mr. Gomez , Mr. Green of Texas , Mrs. Grijalva , Mrs. Hayes , Mr. Horsford , Ms. Hoyle of Oregon , Mr. Huffman , Mr. Ivey , Mr. Jackson of Illinois , Ms. Jacobs , Mr. Johnson of Georgia , Ms. Johnson of Texas , Ms. Kamlager-Dove , Ms. Kelly of Illinois , Mr. Khanna , Mr. Krishnamoorthi , Ms. Lee of Pennsylvania , Ms. Leger Fernandez , Mr. Levin , Mr. Lieu , Ms. Lofgren , Ms. Matsui , Ms. McClellan , Ms. McCollum , Mr. McGarvey , Mr. McGovern , Mrs. McIver , Mr. Meeks , Mr. Menendez , Ms. Meng , Ms. Moore of Wisconsin , Mr. Moulton , Mr. Mullin , Mr. Nadler , Mr. Norcross , Ms. Norton , Ms. Ocasio-Cortez , Ms. Omar , Mr. Pallone , Mr. Panetta , Ms. Pingree , Mr. Pocan , Ms. Pressley , Mr. Quigley , Mrs. Ramirez , Ms. Randall , Mr. Raskin , Ms. Rivas , Ms. Ross , Mr. Ruiz , Ms. Salinas , Ms. S\u00e1nchez , Ms. Scanlon , Ms. Schakowsky , Ms. Simon , Mr. Soto , Ms. Stansbury , Ms. Strickland , Mr. Swalwell , Mr. Takano , Mr. Thanedar , Mr. Thompson of Mississippi , Mr. Thompson of California , Ms. Titus , Ms. Tlaib , Ms. Tokuda , Mr. Tonko , Mr. Torres of New York , Mrs. Trahan , Mr. Vargas , Mr. Veasey , Ms. Vel\u00e1zquez , Ms. Wasserman Schultz , Ms. Waters , Mrs. Watson Coleman , Ms. Williams of Georgia , Ms. Wilson of Florida , Ms. Lois Frankel of Florida , Mr. Hern\u00e1ndez , and Mrs. Sykes ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide standards for facilities at which aliens in the custody of the Department of Homeland Security are detained, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dignity for Detained Immigrants Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that detention, even for a short period of time, inflicts severe, irreparable harm on children and should be avoided.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate committees of congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on the Judiciary of the Senate;\n**(B)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate;\n**(C)**\nthe Committee on the Judiciary of the House of Representatives; and\n**(D)**\nthe Committee on Homeland Security of the House of Representatives.\n**(2) Department**\nThe term Department means the Department of Homeland Security.\n**(3) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n#### 4. Standards for department of homeland security detention facilities\n##### (a) Rulemaking\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall, by regulation, establish detention standards for each facility at which aliens in the custody of the Department are detained.\n##### (b) Minimum protection\nThe standards established under subsection (a) shall provide, at a minimum, the level of protections for detainees described in the American Bar Association\u2019s Civil Immigration Detention Standards (adopted in August 2012, and as modified in August 2014).\n##### (c) Biennial updates\nNot less frequently than biennially, the Secretary shall review and update such standards, as appropriate.\n#### 5. Oversight and transparency\n##### (a) Periodic inspections\n**(1) In general**\nOn a periodic basis, not less frequently than annually, the Inspector General of the Department (referred to in this section as the Inspector General ) shall conduct an unannounced, in-person inspection of each facility at which aliens in the custody of the Department are detained to ensure that each such facility is in compliance with the standards established under section 4.\n**(2) Report**\nNot later than 60 days after conducting an inspection under paragraph (1), the Inspector General shall\u2014\n**(A)**\nsubmit a report to the Secretary containing the results of such inspection; and\n**(B)**\nmake the report available to the public on the internet website of the Department.\n**(3) Failure to comply with standards**\n**(A) Initial failure**\n**(i) In general**\nIf the Inspector General determines that a facility has failed to comply with the standards established under section 4 for the first time during any 2-year period, and such noncompliance constitutes a deficiency that threatens the health, safety, or the due process rights of detainees\u2014\n**(I)**\nthe Inspector General shall notify the Secretary of such determination; and\n**(II)**\nthe Secretary shall\u2014\n**(aa)**\nin the case of a facility not owned by the Department, impose a meaningful fine of not less than 10 percent of the value of the contract with the facility; and\n**(bb)**\nin the case of a facility owned by the Department\u2014\n(AA)\nissue a written warning to the facility not later than 30 days after receiving such notification from the Inspector General, which shall include remedial measures to be carried out not later than 60 days after the issuance of the warning; and\n(BB)\nnot later than 60 days after the issuance of a warning under subitem (AA), certify to the Inspector General that the remedial measures have been carried out.\n**(ii) Follow-up inspection**\nNot later than 180 days after the date on which the Inspector General makes a notification under clause (i)(I), the Inspector General shall conduct an in-person inspection of the facility to determine whether the facility has achieved compliance with the standards established under section 4.\n**(B) Subsequent failures**\nIf the Inspector General determines that a facility has failed to comply with the standards established under section 4 in 2 or more inspections under paragraph (1) during any 2-year period, and such noncompliance constitutes a deficiency that threatens the health, safety, or the rights of detainees\u2014\n**(i)**\nthe Inspector General shall notify the Secretary of such determination; and\n**(ii)**\nthe Secretary shall\u2014\n**(I)**\nin the case of a facility not owned by the Department\u2014\n**(aa)**\nnot later than 30 days after receiving such notification, transfer each detainee to a facility that does so comply;\n**(bb)**\nterminate the contract with the owner or operator of the facility; and\n**(cc)**\nensure that no funds made available to the Department be used to continue such contract; and\n**(II)**\nin the case of a facility owned by the Department\u2014\n**(aa)**\nnot later than 60 days after receiving such notification, transfer each detainee to a facility that does so comply; and\n**(bb)**\nsuspend the use of such facility until such time as the Inspector General\u2014\n(AA)\ncertifies to the Secretary that the facility is in compliance with such standards; and\n(BB)\nmakes available to the public on the internet website of the Department information relating to the remedial measures taken.\n##### (b) Deaths in custody\n**(1) Notification**\nNot later than 24 hours after the death of an alien in the custody of the Department, the Secretary shall notify the appropriate committees of Congress of such death.\n**(2) Investigations**\n**(A) In general**\nNot later than 30 days after the death of an alien in the custody of the Department, the Secretary shall conduct an investigation into such death, which shall include a root cause analysis that identifies any changes to policies, practices, training curricula, staffing, or potential system-wide errors that may reduce the probability of such an event in the future.\n**(B) Root cause analysis**\nEach root cause analysis required by subparagraph (A) shall be carried out\u2014\n**(i)**\nby appropriately qualified personnel, including 1 or more medical professionals qualified in a field relevant to the death; and\n**(ii)**\nin accordance with professional medical standards for investigating sentinel events in medical care facilities, including the Sentinel Event Policy promulgated by The Joint Commission.\n**(C) Public report**\nNot later than 60 days after such a death, the Secretary shall\u2014\n**(i)**\nissue a full report describing the results of the investigation required by subparagraph (A); and\n**(ii)**\nmake the report available to the public on the internet website of the Department.\n**(D) Review by inspector general**\nNot later than 90 days after the death of an alien in the custody of the Department, the Inspector General shall conduct a review of the report issued under subparagraph (C) with respect to such death.\n**(3) Definition of death of an alien in the custody of the department**\nThe term death of an alien in the custody of the Department means the death of an alien occurring while the alien is under the supervision of the Department, regardless of\u2014\n**(A)**\nthe location of the death; or\n**(B)**\nwhether the death may have resulted from a health problem that existed before or during, or was exacerbated by, the detention of the alien.\n##### (c) Report to congress\n**(1) In general**\nNot less frequently than annually, the Secretary shall submit to the appropriate committees of Congress a report on the inspections and oversight of facilities at which aliens in the custody of the Department are detained.\n**(2) Elements**\nEach report required by paragraph (1) shall include, for the preceding year\u2014\n**(A)**\na list of each detention facility found by the Inspector General to be in noncompliance with the standards established under section 4;\n**(B)**\nfor each such facility, a description of the remedial actions taken, or planned to be taken, by the Secretary so as to achieve compliance with such standards; and\n**(C)**\na determination as to whether such remedial actions have succeeded in bringing the facility into compliance with such standards.\n##### (d) Classification of documents for purposes of FOIA\nThe reports required by subsections (a)(2) and (b)(2)(C), and any contract between the Department and a private or public entity that provides for the use of a facility not owned by the Department to detain aliens in the custody of the Department, are considered records for purposes of section 552 of title 5, United States Code, and do not qualify for the exception under subsection (b)(4) of such section.\n##### (e) Facilities matrix\n**(1) In general**\nOn the first day of each month, the Secretary shall ensure that a publicly accessible internet website of the Department contains the information described in paragraph (2) for each facility at which aliens in the custody of the Department are detained.\n**(2) Elements**\nThe information referred to in paragraph (1) is, for each such facility, the following:\n**(A)**\nThe name and location of the facility.\n**(B)**\nWhether the facility houses adults, children, or both.\n**(C)**\nThe number of beds available in the facility on the last day of the preceding month, disaggregated by gender.\n**(D)**\nThe total number of aliens detained in the facility on the last day of the preceding month, disaggregated by gender and classification as a child or as an adult.\n**(E)**\nWhether the facility is used to detain aliens for longer than 72 hours.\n**(F)**\nWhether the facility is used to detain aliens for longer than 7 days.\n**(G)**\nThe average number of aliens detained in the facility during the current year and during the preceding month, disaggregated by gender and classification as a child or as an adult.\n**(H)**\nWhether the facility is in compliance with the standards established under section 4.\n**(I)**\nIn the case of a facility not owned by the Department, a description of the nature of the contract providing for the detention of aliens at the facility.\n**(J)**\nThe average, median, 25th quartile, and 50th quartile number of days that an alien has been detained at the facility during the preceding month.\n##### (f) Online detainee locator system\nThe Secretary shall ensure that the online detainee locator system maintained by the Department, or any successor system, is updated not later than 12 hours after an alien is\u2014\n**(1)**\ntaken into, or released from, custody by the Department;\n**(2)**\ntransferred to, or detained in, a detention facility; or\n**(3)**\nremoved from the United States.\n##### (g) Information collected and maintained for aliens in DHS custody\nThe Secretary shall collect and maintain, for each alien in the custody of the Department, the following information:\n**(1)**\nThe gender and age of the alien.\n**(2)**\nThe date on which the alien was taken into such custody.\n**(3)**\nThe country of nationality of the alien.\n**(4)**\nWhether the alien is considered a vulnerable person (as such term is defined in section 236(c)(5) of the Immigration and Nationality Act, as amended by section 9) or a primary caregiver.\n**(5)**\nThe provision of law pursuant to which the Secretary is authorized to detain the alien.\n**(6)**\nThe name of the facility in which the alien is detained.\n**(7)**\nWith respect to any transfer of the alien to another detention facility\u2014\n**(A)**\na description of the transfer of the alien to the other detention facility;\n**(B)**\nthe reason for the transfer; and\n**(C)**\nin the case of a transfer effectuated despite presence of the alien\u2019s legal counsel or immediate relative in the jurisdiction of the original detention facility, a justification for such transfer.\n**(8)**\nThe status and basis of any removal proceedings of which the alien is the subject.\n**(9)**\nThe initial custody determination made by U.S. Immigration and Customs Enforcement, including any review of such determination.\n**(10)**\nThe date of the alien\u2019s release or removal, and the reason for such release or removal, as applicable.\n**(11)**\nWhether the alien is subject to a final order of removal.\n**(12)**\nWhether the alien was apprehended as part of a family unit.\n**(13)**\nWhether the alien was separated from a family unit at the border or in the interior of the United States.\n#### 6. Civil actions\n##### (a) Civil action for violation of standards\n**(1) In general**\nAn individual detained in a facility required to comply with the standards established under section 4 who is injured as a result of a violation of such standards may file a claim in the appropriate district court of the United States.\n**(2) Recovery**\nIn a civil action under this subsection, the court may order injunctive relief and compensatory damages, and may award the prevailing party reasonable attorney fees, and costs.\n#### 7. Detention facility construction and maintenance\n##### (a) Restriction on construction\n**(1) In general**\nNot later than 180 days before initiating, or entering into a contract for, the construction of a new facility or the expansion of an existing facility for the detention of aliens in the custody of the Department, the Secretary shall submit to the appropriate committees of Congress a notification of the plan to construct or expand such facility, including\u2014\n**(A)**\nthe location, size, and capacity of such facility;\n**(B)**\nthe anticipated timeline and cost of constructing or expanding such facility; and\n**(C)**\nthe intended population to be detained at such facility, including the gender and ages of such population.\n**(2) Public availability**\nThe Secretary shall make the information described in paragraph (1) available to the public on the internet website of the Department.\n##### (b) Phase-Out of private detention facilities and use of jails\n**(1) Secure detention facilities**\n**(A) In general**\nThe Secretary\u2014\n**(i)**\nmay not enter into or extend any contract or agreement with any public or private for-profit entity that owns or operates a detention facility for use of such facility to detain aliens in the custody of the Department; and\n**(ii)**\nshall terminate any contract or agreement described in clause (i) not later than the date that is 3 years after the date of the enactment of this Act.\n**(B) Ownership requirement**\nBeginning on the date that is 3 years after the date of the enactment of this Act, any facility at which aliens in the custody of the Department are detained shall be owned and operated by the Department.\n**(2) Alternatives to detention programs**\n**(A) In general**\nThe Secretary\u2014\n**(i)**\nmay not enter into or extend any contract or agreement with any public or private for-profit entity for the operation of a program or the use of a facility for nonresidential, detention-related activities for aliens who are subject to monitoring by the Department; and\n**(ii)**\nshall terminate any contract or agreement described in clause (i) not later than the date that is 3 years after the date of the enactment of this Act.\n**(B) Ownership and operation requirement**\nBeginning on the date that is 3 years after the date of the enactment of this Act, any program or facility used for the activities described in subparagraph (A)(i) shall be owned and operated by a nonprofit organization or the Department.\n**(3) Implementation plan**\nNot later than 60 days after the date of the enactment of this Act, the Secretary shall develop, and make publicly available, a plan and timeline for the implementation of this subsection.\n##### (c) Facility requirement\nThe Secretary shall ensure that each facility for the detention of aliens has a visitor waiting and security screening area that is indoor and climate-controlled.\n#### 8. Appearance of detained aliens for other legal matters\nThe Secretary shall establish rules to ensure that any alien detained in the custody of the Department who is required to appear in Federal or State court (including family court) for another matter is transported by an officer or employee of the Department to such court proceeding.\n#### 9. Procedures for detaining aliens\n##### (a) Probable cause and custody determination hearings\nSection 236 of the Immigration and Nationality Act ( 8 U.S.C. 1226 ) is amended to read as follows:\n236. Apprehension and detention of aliens (a) Arrest, detention, and release (1) In general On a warrant issued by an immigration judge, or pursuant to section 287(a)(2), the Secretary of Homeland Security may arrest an alien, and in accordance with this section, detain the alien or release the alien on bond, subject to conditions, or recognizance, pending a decision on whether the alien is to be removed from the United States. (2) Exemption for unaccompanied alien children (A) In general This section shall not apply to unaccompanied alien children (as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) )). (B) Transfer of custody Any unaccompanied alien child in the custody of the Secretary of Homeland Security shall be transferred to the custody of the Secretary of Health and Human Services pursuant to section 235(b)(3) of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( 8 U.S.C. 1232(b)(3) ). (b) Bond determination (1) In general An immigration judge who releases an alien on bond under this section shall\u2014 (A) consider, for purposes of setting the amount of the bond, the alien\u2019s financial position and ability to pay the bond without imposing financial hardship on the alien; and (B) set bond at an amount no greater than necessary to ensure the alien\u2019s appearance for removal proceedings. (2) Inability to pay bond The Secretary of Homeland Security may not continue to detain an alien solely based on the alien\u2019s inability to pay bond. (c) Custody determination (1) Initial determination (A) In general Not later than 48 hours after taking an alien into custody pursuant to this section or section 235, or with respect to an alien subject to a reinstated order of removal pursuant to section 241(a)(5) who has been found to have a credible or reasonable fear of return, the Secretary of Homeland Security shall make an initial custody determination with regard to the alien, and provide such determination in writing to the alien. (B) Least restrictive conditions With respect to a custody determination under subparagraph (A), if the Secretary determines that the release of an alien will not reasonably ensure the appearance of the alien as required or will endanger the safety of any other person or the community, the Secretary shall impose the least restrictive conditions, as described in paragraph (4). (2) Timing (A) In general An alien who seeks to challenge the initial custody determination under paragraph (1) shall be provided with the opportunity for a hearing before an immigration judge not later than 72 hours after the initial custody determination to determine whether the alien should be detained. (B) Access to counsel On request by an alien, or the legal counsel of an alien, an immigration judge may grant a reasonable continuance of a hearing under subparagraph (A) to provide the alien or such legal counsel additional time to prepare for the hearing. (3) Presumption of release (A) In general In a hearing under this subsection, there shall be a presumption that the alien should be released. (B) Rebuttal (i) In general The Secretary of Homeland Security has the duty of rebutting this presumption, which may only be shown based on clear and convincing evidence, including credible and individualized information, that the use of alternatives to detention will not reasonably ensure the appearance of the alien at removal proceedings, or that the alien is a threat to another person or the community. (ii) Consideration The Attorney General\u2014 (I) shall consider the totality of each case; and (II) may not rely on an alien\u2019s criminal conviction, arrest, pending criminal charge, or combination thereof as the sole factor to justify the continued detention of the alien. (4) Least restrictive conditions required (A) In general If an immigration judge determines, pursuant to a hearing under this section, that the release of an alien will not reasonably ensure the appearance of the alien as required or will endanger the safety of any other person or the community, the immigration judge shall order the least restrictive conditions, or combination of conditions, that the judge determines will reasonably ensure the appearance of the alien as required and the safety of any other person and the community, which may include\u2014 (i) release on recognizance; (ii) secured or unsecured release on bond; or (iii) participation in a program described in subsection (f). (B) Monthly review Not less frequently than monthly, the immigration judge shall review any condition assigned to an alien pursuant to subparagraph (A). (C) Modification of conditions of supervision An immigration judge may modify or rescind conditions of supervision imposed on an alien by the Secretary of Homeland Security. (5) Special rule for vulnerable persons and primary caregivers (A) In general In the case of an alien subject to a custody determination under this subsection who is a vulnerable person or a primary caregiver, the alien may not be detained unless the Secretary of Homeland Security demonstrates, in addition to the requirements under paragraph (3), that it is unreasonable or not practicable to place the alien in a community-based supervision program. (B) Definitions In this paragraph: (i) Material witness The term material witness means an individual who presents a declaration to an attorney investigating, prosecuting, or defending the workplace claim or from the presiding officer overseeing the workplace claim attesting that, to the best of the declarant\u2019s knowledge and belief, reasonable cause exists to believe that the testimony of the individual will be relevant to the outcome of the workplace claim. (ii) Primary caregiver The term primary caregiver means an individual who is established to be a caregiver, parent, or close relative caring for or traveling with a child. (iii) Vulnerable person The term vulnerable person means an individual who\u2014 (I) is under 21 years of age or over 60 years of age; (II) is pregnant; (III) identifies as lesbian, gay, bisexual, transgender, queer, or intersex; (IV) is a victim or witness of a crime; (V) has filed a nonfrivolous civil rights claim in Federal or State court; (VI) has filed, or is a material witness to, a bonafide workplace claim; (VII) has a serious mental or physical illness or disability; (VIII) has been determined by an asylum officer in an interview conducted under section 235(b)(1)(B) to have a credible fear of persecution or torture; (IX) has limited English language proficiency and is not provided access to appropriate and meaningful language services in a timely fashion; or (X) has been determined by an immigration judge or by the Secretary of Homeland Security to have experienced or to be experiencing severe trauma or to be a survivor of torture or gender-based violence, based on information obtained during intake, from the alien\u2019s attorney or legal service provider, or through credible self-reporting. (iv) Workplace claim The term workplace claim means any written or oral claim, charge, complaint, or grievance filed with, communicated to, or submitted to the employer, a Federal, State, or local agency or court, or an employee representative related to the violation of applicable Federal, State, and local labor laws, including laws concerning wages and hours, labor relations, family and medical leave, occupational health and safety, civil rights, or nondiscrimination. (6) Subsequent determinations An alien detained under this section shall be provided with a de novo custody determination hearing under this subsection\u2014 (A) not later than 30 days after the date of the enactment of this Act; (B) every 60 days; and (C) upon showing of a change in circumstances or good cause for such a hearing. (d) Release upon an order granting relief from removal The Secretary of Homeland Security\u2014 (1) shall immediately release an alien with respect to whom an immigration judge has entered an order providing relief from removal (including an order granting asylum or withholding, deferral, or cancellation of removal) or an order terminating removal proceedings, which order is pending appeal, upon entry of the order; and (2) may impose only reasonable conditions on the alien\u2019s release from custody. (e) Prohibition on detention of children Notwithstanding any other provision of this Act, the Secretary of Homeland Security may not detain in a facility operated or contracted by U.S. Immigration and Customs Enforcement any individual who is under the age of 18 years. (f) Community-Based case management program (1) In general The Secretary of Homeland Security shall establish, outside of the purview of U.S. Immigration and Customs Enforcement, a community-based case management program that\u2014 (A) provides alternatives to detaining aliens; (B) offers a continuum of community-based support options and services, including\u2014 (i) case management; and (ii) access to\u2014 (I) social services; (II) medical and mental health services; (III) housing; (IV) transportation; and (V) legal services; and (C) provides services in the appropriate language. (2) Prohibition on electronic surveillance The program under paragraph (1) may not include, as an alternative to detention, the provision of ankle monitors or other forms of electronic surveillance. (3) Within 180 days, the Secretary shall undertake a study to examine best practices of government-funded case management and related services, including exploring the possibility of funding case management services out of the Department. (4) Contracts (A) In general The Secretary may enter into 1 or more contracts to operate the case management program described in paragraph (1). (B) Prioritization In entering into a contract under subparagraph (A), the Secretary shall give priority to direct contracts with qualified nongovernmental community-based organizations that have experience providing services to immigrant, refugee, and asylum-seeking populations. (5) Individualized determination required (A) In general In determining whether to order an alien to participate in a program under this subsection, the Secretary or the immigration judge, as appropriate, shall make an individualized determination to determine the appropriate level of supervision for the alien. (B) Exemption Participation in a program under this subsection may not be ordered for an alien for whom it is determined that release on reasonable bond or recognizance will reasonably ensure the appearance of the alien as required and the safety of any other person and the community. (6) Prohibition on fees for alternatives to detention An alien who is required to participate in a specific alternatives to detention program or service may not be charged a fee for such participation. (7) Case management review Not later than 180 days after the date of the enactment of the Dignity for Detained Immigrants Act, the Secretary shall conduct a review of\u2014 (A) best practices in federally funded case management programs; and (B) the feasibility of transferring alternatives to detention case management programs out of the purview of the Department of Homeland Security. .\n##### (b) Probable cause hearing\nSection 287(a) of the Immigration and Nationality Act ( 8 U.S.C. 1357(a)(2) ) is amended by striking the subsection designation and all that follows through United States; in paragraph (2) and inserting the following:\n(a) In general Any officer or employee of the Department of Homeland Security authorized under regulations prescribed by the Secretary of Homeland Security shall have power without warrant\u2014 (1) to interrogate any alien or person believed to be an alien as to the person\u2019s right to be or to remain in the United States, provided that such interrogation is not based on the person\u2019s race, ethnicity, national origin, religion, sexual orientation, color, spoken language, or English language proficiency; and (2) to arrest any alien who, in the presence or view of the officer or employee, is entering or attempting to enter the United States in violation of any law or regulation made pursuant to law regulating the admission, exclusion, expulsion, or removal of aliens, or to arrest any alien in the United States, if\u2014 (A) the officer or employee has probable cause to believe that\u2014 (i) the alien is in the United States in violation of any such law or regulation; and (ii) is likely to escape before a warrant can be obtained for the arrest of the alien; (B) the officer or employee has reason to believe that the alien would knowingly and willfully fail to appear in immigration court in response to a properly served notice to appear; and (C) not later than 48 hours after being taken into custody, the alien is provided with a hearing before an immigration judge to determine whether there was probable cause for such arrest, including probable cause to believe that the alien would have knowingly and willfully failed to appear as required under subparagraph (B) if the alien had not been arrested, which burden to establish probable cause shall be on the Department of Homeland Security; .\n##### (c) Mandatory detention repealed\n**(1) In general**\nThe Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) is amended\u2014\n**(A)**\nin section 235(b) ( 8 U.S.C. 1225(b) )\u2014\n**(i)**\nin paragraph (1)(B)\u2014\n**(I)**\nin clause (ii), by striking detained and inserting referred ; and\n**(II)**\nin clause (iii), by striking subclause (IV); and\n**(ii)**\nin paragraph (2)(A), by striking detained and inserting referred ;\n**(B)**\nby striking section 236A ( 8 U.S.C. 1226 );\n**(C)**\nin section 238(a)(2) ( 8 U.S.C. 1228(a)(2) ), by striking pursuant to section 236(c), ; and\n**(D)**\nin section 506(a)(2) ( 8 U.S.C. 1536(a)(2) )\u2014\n**(i)**\nby amending the heading to read as follows: Release hearing for aliens detained ; and\n**(ii)**\nin subparagraph (A)\u2014\n**(I)**\nby amending the heading to read as follows: In general ;\n**(II)**\nin the matter preceding clause (i), by striking lawfully admitted for permanent residence ;\n**(III)**\nby striking clause (i); and\n**(IV)**\nby redesignating clauses (ii) and (iii) as clauses (i) and (ii), respectively.\n**(2) Conforming amendments**\n**(A)**\nThe table of sections for the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) is amended by striking the item relating to section 236A.\n**(B)**\nSection 241(c)(3)(A)(ii) of the Immigration and Nationality Act ( 8 U.S.C. 1231(c)(3)(A)(ii) ) is amended\u2014\n**(i)**\nin subclause (I), by striking the comma at the end and inserting ; or ;\n**(ii)**\nin subclause (II), by striking , or and inserting a period; and\n**(iii)**\nby striking subclause (III).\n##### (d) Aliens ordered removed\n**(1) In general**\nSection 241(a) of the Immigration and Nationality Act ( 8 U.S.C. 1231(a) ) is amended\u2014\n**(A)**\nin paragraph (1), by striking 90 days each place it appears and inserting 60 days ;\n**(B)**\nby amending paragraph (2) to read as follows:\n(2) Initial custody redetermination hearing (A) In general Not later than 72 hours after the entry of a final administrative order of removal, the alien ordered removed shall be provided with a custody redetermination hearing before an immigration judge. (B) Presumption of detention For purposes of the hearing under subparagraph (A), the alien shall be detained during the removal period unless the alien demonstrates by the preponderance of the evidence that\u2014 (i) the alien\u2019s removal is not reasonably foreseeable; and (ii) the alien does not pose a risk to the safety of any individual or to the community. ;\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nin the paragraph heading, by striking 90-day and inserting 60-day ; and\n**(ii)**\nin the matter preceding subparagraph (A), by striking the alien, pending removal, shall be subject to supervision under and inserting the following: except as provided in paragraph (6), any alien who has been detained during the removal period shall be released from custody, pending removal, subject to individualized supervision requirements in accordance with ;\n**(D)**\nby amending paragraph (6) to read as follows:\n(6) Subsequent custody redetermination hearings (A) In general The Secretary of Homeland Security may request a subsequent redetermination hearing before an immigration judge seeking continued detention for an alien ordered to be detained pursuant to paragraph (2) who has not been removed within the removal period. (B) Standard An alien may only be detained after the removal period upon a showing by the Secretary of Homeland Security that\u2014 (i) the alien\u2019s removal is reasonably foreseeable; or (ii) the alien poses a risk to the safety of an individual or the community, which may only be established based on credible and individualized information and may not be established based only on the fact that the alien has been charged with or is suspected of a crime. (C) Period of detention (i) In general An alien may not be detained pursuant to an order under this paragraph for longer than a 60-day period. (ii) Subsequent redetermination hearing The Secretary of Homeland Security may seek subsequent redetermination hearings under this paragraph in order to continue detaining an alien beyond each such 60-day period. ; and\n**(E)**\nby striking paragraph (7).\n**(2) Technical and conforming amendments**\nThe Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) is amended\u2014\n**(A)**\nin section 238 ( 8 U.S.C. 1228 )\u2014\n**(i)**\nin subsection (a)(1)\u2014\n**(I)**\nby moving the paragraph 2 ems to the right;\n**(II)**\nby amending the paragraph heading to read as follows: In general ; and\n**(III)**\nin the first sentence\u2014\n**(aa)**\nby striking section 241(a)(2)(A)(iii) and inserting section 237(a)(2)(A)(iii) ;\n**(bb)**\nby striking section 241(a)(2)(A)(ii) and inserting section 237(a)(2)(A)(ii) ; and\n**(cc)**\nby striking section 241(a)(2)(A)(i) and inserting 237(a)(2)(A)(i) ;\n**(ii)**\nin the second subsection (c)\u2014\n**(I)**\nin paragraph (2)(B), by striking section 241(a)(2)(A) and inserting section 237(a)(2)(A) ; and\n**(II)**\nin paragraph (4), by striking section 241(a) and inserting section 237(a) ; and\n**(iii)**\nby redesignating the second subsection (c) as subsection (d);\n**(B)**\nin section 276(b)(4) ( 8 U.S.C. 1326(b)(4) ), by striking section 241(a)(4)(B) and inserting section 237(a)(4)(B) ; and\n**(C)**\nin section 501(1) ( 8 U.S.C. 1531(1) ), by striking section 241(a)(4)(B) and inserting section 237(a)(4)(B) .\n#### 10. Prohibition on solitary confinement\n##### (a) In general\nAn individual in the custody of the Department may not be placed in solitary confinement.\n##### (b) Definition of solitary confinement\nIn this section, the term solitary confinement \u2014\n**(1)**\nmeans the confinement of an individual to the individual\u2019s cell, alone or with a cellmate, whether pursuant to disciplinary, administrative, or classification action; and\n**(2)**\ndoes not include the confinement of an individual to an individual\u2019s cell during designated sleeping time.\n#### 11. Legal orientation\n##### (a) Program\nThe Secretary of Homeland Security shall ensure that each facility used to detain aliens provides access to the Legal Orientation Program (or any successor program), to be operated by a nonprofit nongovernmental organization with demonstrated immigration law expertise, for each alien detained at such facility, whether or not such facility is owned by the Department.\n##### (b) Orientation\nThe Secretary of Homeland Security shall ensure that each alien described in subsection (a) receives a legal orientation under such subsection, which may be provided in a group setting, as soon as practicable after entering the detention facility, but in no case after the initial hearing before an immigration judge.\n#### 12. Access to counsel\nThe Secretary of Homeland Security shall permit an alien who has counsel in accordance with section 292 of the Immigration and Nationality Act ( 8 U.S.C. 1362 ) to access such counsel, in a private, confidential setting, including through confidential contact with counsel through in person, telephonic, or televideo meetings.\n#### 13. Congressional oversight\n##### (a) Oversight\nThe Secretary of Homeland Security shall permit a covered person to enter, for the purpose of conducting oversight, any facility operated by or for the Department used to detain or otherwise house aliens for any period of time, and may not make any temporary modification at any such facility that in any way alters what is observed by a visiting covered person, compared to what would be observed in the absence of such modification.\n##### (b) No prior notice for Members\nA covered person described in subsection (b)(1) may not be required to provide prior notice of the intent to enter a facility described in subsection (a) for the purpose of conducting oversight.\n##### (c) Notice for employees\n**(1) Employees not accompanying a Member**\nExcept as provided in paragraph (2), the Secretary of Homeland Security may require a covered person described in subsection (b)(2) to provide notice to a facility described in subsection (a) at least 24 hours in advance of entry into such facility.\n**(2) Employees accompanying a Member**\nThe notice described in paragraph (1) shall not be required for a covered person described in subsection (b)(2) who is accompanying a covered person described in subsection (b)(1).\n##### (d) Covered person defined\nIn this section, the term covered person means\u2014\n**(1)**\na Member of Congress; and\n**(2)**\nan employee of the House of Representatives or the Senate designated by such a Member for the purpose of this section.",
      "versionDate": "2025-12-03",
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
        "actionDate": "2026-01-27",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3702",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Dignity for Detained Immigrants Act",
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
        "name": "Immigration",
        "updateDate": "2026-01-05T16:23:30Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6397ih.xml"
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
      "title": "Dignity for Detained Immigrants Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dignity for Detained Immigrants Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T06:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide standards for facilities at which aliens in the custody of the Department of Homeland Security are detained, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T06:18:21Z"
    }
  ]
}
```
