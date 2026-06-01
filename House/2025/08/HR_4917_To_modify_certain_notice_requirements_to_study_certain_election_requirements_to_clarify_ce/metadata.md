# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4917?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4917
- Title: Expanding the VOTE Act
- Congress: 119
- Bill type: HR
- Bill number: 4917
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2026-03-26T08:06:32Z
- Update date including text: 2026-03-26T08:06:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-05 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-05 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4917",
    "number": "4917",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Expanding the VOTE Act",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:32Z",
    "updateDateIncludingText": "2026-03-26T08:06:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-05T14:02:10Z",
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
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MD"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "NY"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "NY"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "KS"
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
      "sponsorshipDate": "2025-08-05",
      "state": "AL"
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
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
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
      "sponsorshipDate": "2025-08-05",
      "state": "VA"
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "AZ"
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
      "sponsorshipDate": "2025-08-05",
      "state": "OH"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "IN"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "HI"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "FL"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MO"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
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
      "sponsorshipDate": "2025-08-05",
      "state": "NC"
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "PA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MD"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "PA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "AL"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
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
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NV"
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "GA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "MA"
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "MD"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "VI"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "OR"
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "AZ"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "WA"
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-26",
      "state": "GA"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "CO"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "RI"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MO"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "NJ"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4917ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4917\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Ms. Williams of Georgia (for herself, Mr. Raskin , Mr. Morelle , Ms. Clarke of New York , Mr. Espaillat , Ms. Meng , Ms. Davids of Kansas , Ms. Sewell , Mr. Veasey , Mr. Scott of Virginia , Ms. Adams , Mr. Amo , Ms. Ansari , Ms. Brown , Ms. Budzinski , Mr. Carson , Mr. Case , Mr. Casten , Mrs. Cherfilus-McCormick , Mr. Cleaver , Mr. Costa , Ms. Crockett , Mr. Davis of North Carolina , Ms. DelBene , Mr. Deluzio , Mr. Doggett , Ms. Elfreth , Mr. Evans of Pennsylvania , Mr. Fields , Mr. Figures , Mrs. Fletcher , Mr. Garc\u00eda of Illinois , Mr. Green of Texas , Mr. Horsford , Mr. Jackson of Illinois , Mr. Johnson of Georgia , Ms. Kamlager-Dove , Ms. Kelly of Illinois , Mr. Krishnamoorthi , Mr. Larson of Connecticut , Ms. Lee of Pennsylvania , Mr. Lynch , Ms. McClellan , Mrs. McIver , Mr. Meeks , Mr. Mfume , Mr. Min , Ms. Moore of Wisconsin , Mr. Moulton , Mr. Mullin , Ms. Norton , Ms. Plaskett , Mr. Pocan , Ms. Pressley , Mrs. Ramirez , Ms. Salinas , Ms. Schakowsky , Ms. Simon , Mr. Stanton , Ms. Strickland , Mrs. Sykes , Mr. Thanedar , Mr. Thompson of Mississippi , Ms. Titus , Ms. Tlaib , and Mr. Tonko ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo modify certain notice requirements, to study certain election requirements, to clarify certain election requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding the Voluntary Opportunities for Translations in Elections Act or the Expanding the VOTE Act .\n#### 2. Language minority notice requirements\nSection 203 of the Voting Rights Act of 1965 ( 52 U.S.C. 10503 ) is amended\u2014\n**(1)**\nby amending subsection (b)(3)(A) to read as follows:\n(A) the term voting materials \u2014 (i) means registration or voting notices, forms, instructions, assistance, or other materials or information relating to the electoral process, including ballots; and (ii) includes digital and printed material or information produced relating to the electoral process; ;\n**(2)**\nby redesignating subsection (e) as subsection (g); and\n**(3)**\nby inserting after subsection (d) the following new subsections:\n(e) Responsibility of States providing voting materials in covered political subdivisions The prohibition under subsection (b) shall apply to any State that provides voting materials to a political subdivision subject to such prohibition. (f) Notice The Attorney General shall submit a notice of the prohibition of subsection (b), and the threshold at which such prohibition applies, to each State or political subdivision that is\u2014 (1) below the threshold requirement under subclause (II) of subsection (b)(2)(A)(i) by not more than 1,000; or (2) below the threshold requirement under subclause (I) or (III) of subsection (b)(2)(A)(i) by not more than 0.5 percent. .\n#### 3. Provisions related to American Indian and Alaska Native languages\nSection 203 of the Voting Rights Act of 1965 ( 52 U.S.C. 10503 ), as amended by section 2, is further amended\u2014\n**(1)**\nin subsection (b)(3)(C), by striking 1990 and inserting most recent ; and\n**(2)**\nby striking subsection (c) and inserting the following:\n(c) Provision of voting materials in the language of a minority group (1) In general Subject to paragraph (2), whenever any State or political subdivision subject to the prohibition of subsection (b) provides any registration or voting notices, forms, instructions, assistance, or other materials or information relating to the electoral process, including ballots, it shall provide them in the language of the applicable minority group as well as in the English language. (2) Exceptions (A) When written American Indian and Alaska Native translations for voters are not required In the case of a minority group that is American Indian or Alaska Native, if the Tribal government of that minority group has notified the Attorney General that the language is unwritten or the Tribal government does not want a written translation, a State or political subdivision subject to the prohibition of subsection (b) shall only be required to furnish that minority group, in the covered language, oral instructions, assistance, translation of voting materials, and other information relating to registration and voting. (B) Other minority groups with unwritten language In the case of a minority group that is not American Indian or Alaska Native, if the language of that minority group is unwritten, a State or political subdivision subject to the prohibition of subsection (b) shall only be required to furnish that minority group, in the covered language, oral instructions, assistance, translation of voting materials, and other information relating to registration and voting. (3) Written translations for election workers Notwithstanding paragraph (2), a State or political division subject to the prohibition of subsection (b) shall provide written translations of all voting materials, with the consent of any applicable Tribal government, to election workers to ensure that the translations from English to the language of a minority group are complete, accurate, and uniform. (4) Tribal government defined In this subsection, the term Tribal government means the recognized governing body of any Indian or Alaska Native Tribe, band, nation, pueblo, village, community, component band, or component reservation, individually identified (including parenthetically) in the list published most recently as of the date of enactment of the Expanding the VOTE Act pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ). .\n#### 4. Grants to jurisdictions to incentivize the provision of voting materials in languages not triggering Section 203 coverage in applying jurisdiction\n##### (a) Availability of grants\n**(1) In general**\nThe Election Assistance Commission (in this section, referred to as the Commission ) shall make incentive grants under subsection (b) to States and political subdivisions to assist the States and political subdivisions in providing voting materials during an election cycle in the language of a covered language minority group.\n**(2) Application required**\nIn order to receive a grant under this section, a State or political subdivision shall submit to the Commission, at such time and in such form as the Commission may require, an application containing such information and assurances as the Commission may require, such as a plan for the State or political subdivision to engage stakeholders with a demonstrated experience of serving the relevant covered language minority group.\n##### (b) Incentive grants\n**(1) Use of funds**\nThe Commission shall make an incentive grant under this subsection to a State or political subdivision to cover the reasonable costs incurred by the State or political subdivision in providing voting materials in the language of a covered language minority group for an election cycle.\n**(2) Continuation of provision of materials for groups in succeeding election cycles**\nIf a State or political subdivision receives an incentive grant with respect to a covered language minority group for an election cycle, the State or political subdivision will certify to the Commission that the State or political subdivision will continue to provide voting materials in the language of that covered language minority group for each succeeding election cycle unless the population of the group during the succeeding cycle has dropped by 0.5 percent or more from the population of the group during the first election cycle for which the State or political subdivision received an incentive grant with respect to the group.\n**(3) Prohibiting multiple grants for same language minority group**\nIf a State or political subdivision receives an incentive grant with respect to a covered language minority group, the State or subdivision may not receive another incentive grant with respect to that same covered language minority group.\n##### (c) Definitions\nIn this section\u2014\n**(1)**\nthe term covered language minority group \u2014\n**(A)**\nmeans, with respect to a State or political subdivision, the members of a single language minority who do not meet the requirements of clause (i) or (ii) of section 203(b)(2)(A) of the Voting Rights Act of 1965 ( 52 U.S.C. 10503(b)(2)(A) ); and\n**(B)**\nincludes the language minorities described in section 203(g) of such Act ( 52 U.S.C. 10503(g) ) and any other language minority;\n**(2)**\nthe term election cycle means the period which begins on the day after the date of a regularly scheduled general election for Federal office and which ends on the date of the next regularly scheduled general election for Federal office;\n**(3)**\nthe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, American Samoa, Guam, and the Commonwealth of the Northern Mariana Islands; and\n**(4)**\nthe term voting materials has the meaning given under section 203(b)(3)(A) of the Voting Rights Act of 1065 ( 52 U.S.C. 10503(b)(3)(A) ).\n##### (d) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $15,000,000, to remain available until expended.\n#### 5. Study on certain language minority notice requirements\n##### (a) In general\nThe Comptroller General of the United States, in consultation with the Director of the Census, the Attorney General, and the Election Assistance Commission, shall conduct a study on the impact of\u2014\n**(1)**\nreducing the threshold requirement\u2014\n**(A)**\nunder subclause (II) of section 203(b)(2)(A)(i) of the Voting Rights Act of 1965 ( 52 U.S.C. 10503(b)(2)(A)(i) ) to 7,500 and 5,000, respectively; and\n**(B)**\nunder subclause (I) or (III) of section 203(b)(2)(A)(i) of the Voting Rights Act of 1965 ( 52 U.S.C. 10503(b)(2)(A)(i) ) to 4 percent, 3 percent, 2.5 percent, and 2 percent, respectively; and\n**(2)**\nexpanding the definition of the term language minorities to include native speakers of Arabic, French and Haitian Creole, and any other language that the Comptroller General determines to be appropriate.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report on the findings of the study conducted under subsection (a).",
      "versionDate": "2025-08-05",
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
        "actionDate": "2025-07-31",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "2589",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expanding the VOTE Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-15T18:16:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-05",
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
          "measure-id": "id119hr4917",
          "measure-number": "4917",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-05",
          "originChamber": "HOUSE",
          "update-date": "2026-02-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4917v00",
            "update-date": "2026-02-20"
          },
          "action-date": "2025-08-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Expanding the Voluntary Opportunities for Translations in Elections Act or the Expanding the VOTE Act</strong></p><p>This bill expands access to voting materials for individuals with limited proficiency in the English language.</p><p>Section 203 of the Voting Rights Act of 1965 (VRA) requires covered states and political subdivisions to provide voting materials and other language assistance to\u00a0persons who are American Indian, Asian American, Alaskan Natives, or of Spanish heritage and\u00a0whose ability to speak or understand English limits electoral participation. A state or political subdivision that is subject to Section 203 is prohibited from providing English-only voting materials in an election. Among other requirements, this bill (1) requires the Department of Justice to issue a notice of prohibition, including the trigger threshold at which the prohibition applies, to certain states and political subdivisions; and (2) requires covered states and political subdivisions to provide written translations of all voting materials, with the consent of any applicable tribal government, to election workers.</p><p>Additionally, the bill requires the Election Assistance Commission to make incentive grants for states and political subdivisions to provide translated voting materials.</p><p>The bill also directs the Government Accountability Office to study and report on the impact of (1) reducing the threshold requirement under Section 203 of the VRA, and (2) expanding the definition of\u00a0<em>language minorities</em> to include native speakers of additional languages.</p>"
        },
        "title": "Expanding the VOTE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4917.xml",
    "summary": {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanding the Voluntary Opportunities for Translations in Elections Act or the Expanding the VOTE Act</strong></p><p>This bill expands access to voting materials for individuals with limited proficiency in the English language.</p><p>Section 203 of the Voting Rights Act of 1965 (VRA) requires covered states and political subdivisions to provide voting materials and other language assistance to\u00a0persons who are American Indian, Asian American, Alaskan Natives, or of Spanish heritage and\u00a0whose ability to speak or understand English limits electoral participation. A state or political subdivision that is subject to Section 203 is prohibited from providing English-only voting materials in an election. Among other requirements, this bill (1) requires the Department of Justice to issue a notice of prohibition, including the trigger threshold at which the prohibition applies, to certain states and political subdivisions; and (2) requires covered states and political subdivisions to provide written translations of all voting materials, with the consent of any applicable tribal government, to election workers.</p><p>Additionally, the bill requires the Election Assistance Commission to make incentive grants for states and political subdivisions to provide translated voting materials.</p><p>The bill also directs the Government Accountability Office to study and report on the impact of (1) reducing the threshold requirement under Section 203 of the VRA, and (2) expanding the definition of\u00a0<em>language minorities</em> to include native speakers of additional languages.</p>",
      "updateDate": "2026-02-20",
      "versionCode": "id119hr4917"
    },
    "title": "Expanding the VOTE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanding the Voluntary Opportunities for Translations in Elections Act or the Expanding the VOTE Act</strong></p><p>This bill expands access to voting materials for individuals with limited proficiency in the English language.</p><p>Section 203 of the Voting Rights Act of 1965 (VRA) requires covered states and political subdivisions to provide voting materials and other language assistance to\u00a0persons who are American Indian, Asian American, Alaskan Natives, or of Spanish heritage and\u00a0whose ability to speak or understand English limits electoral participation. A state or political subdivision that is subject to Section 203 is prohibited from providing English-only voting materials in an election. Among other requirements, this bill (1) requires the Department of Justice to issue a notice of prohibition, including the trigger threshold at which the prohibition applies, to certain states and political subdivisions; and (2) requires covered states and political subdivisions to provide written translations of all voting materials, with the consent of any applicable tribal government, to election workers.</p><p>Additionally, the bill requires the Election Assistance Commission to make incentive grants for states and political subdivisions to provide translated voting materials.</p><p>The bill also directs the Government Accountability Office to study and report on the impact of (1) reducing the threshold requirement under Section 203 of the VRA, and (2) expanding the definition of\u00a0<em>language minorities</em> to include native speakers of additional languages.</p>",
      "updateDate": "2026-02-20",
      "versionCode": "id119hr4917"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4917ih.xml"
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
      "title": "Expanding the VOTE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding the VOTE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding the Voluntary Opportunities for Translations in Elections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modify certain notice requirements, to study certain election requirements, to clarify certain election requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:34Z"
    }
  ]
}
```
