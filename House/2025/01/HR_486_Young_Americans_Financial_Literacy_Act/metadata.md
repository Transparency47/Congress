# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/486?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/486
- Title: Young Americans Financial Literacy Act
- Congress: 119
- Bill type: HR
- Bill number: 486
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-04-16T08:06:41Z
- Update date including text: 2026-04-16T08:06:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Sponsor introductory remarks on measure. (CR E40)
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Sponsor introductory remarks on measure. (CR E40)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/486",
    "number": "486",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001072",
        "district": "7",
        "firstName": "Andr\u00e9",
        "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
        "lastName": "Carson",
        "party": "D",
        "state": "IN"
      }
    ],
    "title": "Young Americans Financial Literacy Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:41Z",
    "updateDateIncludingText": "2026-04-16T08:06:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E40)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:05:15Z",
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
          "date": "2025-01-16T14:05:10Z",
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
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "RI"
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
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
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
      "sponsorshipDate": "2025-01-16",
      "state": "OH"
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
      "sponsorshipDate": "2025-01-16",
      "state": "LA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
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
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
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
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CT"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "DC"
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
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "RI"
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
      "sponsorshipDate": "2025-01-16",
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
      "sponsorshipDate": "2025-01-16",
      "state": "NJ"
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
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
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
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
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
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NV"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "MN"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NJ"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "OH"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MA"
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
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MD"
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
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MS"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "WA"
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
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NV"
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
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "HI"
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
      "sponsorshipDate": "2025-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MI"
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
      "sponsorshipDate": "2025-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "TX"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "AL"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "NY"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "FL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "DE"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "TX"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "MN"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "OR"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr486ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 486\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Carson (for himself, Mr. Amo , Ms. Barrag\u00e1n , Ms. Brown , Mr. Carter of Louisiana , Mr. Case , Mr. Casten , Mr. Cohen , Ms. Dean of Pennsylvania , Mr. Espaillat , Mr. Evans of Pennsylvania , Mrs. Hayes , Ms. Norton , Mr. Johnson of Georgia , Mr. Magaziner , Mr. McGovern , Mrs. McIver , Mrs. Ramirez , Ms. S\u00e1nchez , Ms. Scholten , Mr. Soto , Mr. Thanedar , Ms. Titus , and Mr. Torres of New York ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a grant program in the Bureau of Consumer Financial Protection to fund the establishment of centers of excellence to support research, development and planning, implementation, and evaluation of effective programs in financial literacy education for young people and families ages 8 through 24 years old, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Young Americans Financial Literacy Act .\n#### 2. Findings\nThe Congress finds as follows:\n**(1)**\nThat 88 percent of Americans believe financial education should be taught in schools and 92 percent of K\u201312 teachers believe that financial education should be taught in school, but only 12 percent of teachers actually teach the subject.\n**(2)**\nAccording to a 2020 survey, less than half of states require high school students to take a course on personal finance, and less than 17 percent of high schoolers were required to take a one semester personal finance course.\n**(3)**\nFor the fourth year in a row, more than one third of surveyed consumers gave themselves a B when grading their own level of basic financial literacy. Less than one-fifth of Americans gave themselves an A . Most adults feel that their financial literacy skills are inadequate, yet they do not rely on anyone else to handle their finances; they feel it is important to know more but have received no financial education.\n**(4)**\nThe sudden disruptions caused by the spread of COVID\u201319 are presenting economic challenges with growing consequences. While some factors affecting financial well-being are beyond individual control, financial literacy can help people better manage their finances through times of hardship.\n**(5)**\nIt is necessary to respond immediately to the pressing needs of individuals faced with the loss of their financial stability; however increased attention must also be paid to financial literacy education reform and long-term solutions to prevent future personal financial disasters.\n**(6)**\nThere is an urgent need to respond to the COVID\u201319 economic recovery with research-based financial literacy education programs to reach individuals at all ages and socioeconomic levels, particularly those facing unique and challenging financial situations, such as high school graduates entering the workforce, soon-to-be and recent college graduates, young families, and the unique needs of military personnel and their families.\n**(7)**\nHigh school and college students who are exposed to cumulative financial education show an increase in financial knowledge, which in turn drives increasingly responsible behavior as they become young adults.\n**(8)**\nThe majority (52 percent) of young adults between the ages of 23\u201328 consider making better choices about managing money , the single most important issue for individual Americans to act on today.\n**(9)**\nAccording to the Government Accountability Office, giving Americans the information they need to make effective financial decisions can be key to their well-being and to the country\u2019s economic health. The current pandemic, in which 88 percent of Americans say is causing stress on their personal finances, underscores the need to improve individuals\u2019 financial literacy and empower all Americans to make informed financial decisions. This is especially true for young people as they are earning their first paychecks, securing student aid, and establishing their financial independence. Therefore, focusing economic education and financial literacy efforts and best practices for young people between the ages of 8\u201324 is of the utmost importance.\n#### 3. Authorization for funding the establishment of centers of excellence in financial literacy education\n##### (a) In general\nThe Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 1037 as section 1038; and\n**(2)**\nby inserting after section 1036 the following:\n1037. Authorization for funding the establishment of centers of excellence in financial literacy education (a) In general The Director of the Bureau, in consultation with the Financial Literacy and Education Commission established under the Financial Literacy and Education Improvement Act, shall make competitive grants to and enter into agreements with eligible institutions to establish centers of excellence to support research, development and planning, implementation, and evaluation of effective programs in financial literacy education for young people and families ages 8 through 24 years old. (b) Authorized activities Activities authorized to be funded by grants made under subsection (a) shall include the following: (1) Developing and implementing comprehensive research based financial literacy education programs for young people\u2014 (A) based on a set of core competencies and concepts established by the Director, including goal setting, planning, budgeting, managing money or transactions, tools and structures, behaviors, consequences, both long- and short-term savings, managing debt and earnings; and (B) which can be incorporated into educational settings through existing academic content areas, including materials that appropriately serve various segments of at-risk populations, particularly minority and disadvantaged individuals. (2) Designing instructional materials using evidence-based content for young families and conducting related outreach activities to address unique life situations and financial pitfalls, including bankruptcy, foreclosure, credit card misuse, and predatory lending. (3) Developing and supporting the delivery of professional development programs in financial literacy education to assure competence and accountability in the delivery system. (4) Improving access to, and dissemination of, financial literacy information for young people and families. (5) Reducing student loan default rates by developing programs to help individuals better understand how to manage educational debt through sustained educational programs for college students. (6) Conducting ongoing research and evaluation of financial literacy education programs to assure learning of defined skills and knowledge, and retention of learning. (7) Developing research-based assessment and accountability of the appropriate applications of learning over short- and long-terms to measure effectiveness of authorized activities. (c) Priority for certain applications The Director shall give a priority to applications that\u2014 (1) provide clear definitions of financial literacy and financially literate to clarify educational outcomes; (2) establish parameters for identifying the types of programs that most effectively reach young people and families in unique life situations and financial pitfalls, including bankruptcy, foreclosure, credit card misuse, and predatory lending; (3) include content that is appropriate to age and socioeconomic levels; (4) develop programs based on educational standards, definitions, and research; (5) include individual goals of financial independence and stability; (6) establish professional development and delivery systems using evidence-based practices; (7) address the needs of one or more at\u2010risk populations; (8) incorporate sensitivities to specific cultural, linguistic, or demographic characteristics; (9) enhance opportunities for asset building, such as increasing savings for lower income households and investments into the stock, bond, and real estate markets; (10) include an evaluation component to ensure the work\u2019s effectiveness in increasing financial literacy or consumer access to appropriate financial products or services, or that the provider has evidence of such effectiveness; (11) promise future replication or can be sustained beyond the program period; and (12) will make effectiveness data (if any) that is generated from the work available to others in the financial education community. (d) Application and evaluation standards and procedures; distribution criteria The Director shall establish application and evaluation standards and procedures, distribution criteria, and such other forms, standards, definitions, and procedures as the Director determines to be appropriate. (e) Content delivery An eligible institution receiving a grant under this section shall\u2014 (1) ensure that content is delivered in an accessible way to young people, through traditional educational methods and digital methods, including over appropriate social media platforms; and (2) to the extent content is delivered through a website, ensure that the website is user friendly, visually appealing, and doesn\u2019t bombard users with dense content that is difficult to comprehend. (f) Grant amounts (1) In general The aggregate amount of grants made under this section during any fiscal year\u2014 (A) shall be at least $27,500,000; and (B) may not exceed $55,000,000. (2) Termination No grants may be made under this section after the end of fiscal year 2029. (g) Report to Congress The Director shall issue an annual report to Congress containing\u2014 (1) a list of grant recipients under this section, including the amount of such grant; and (2) for each grant recipient, a description of the specific populations being served by such grant. (h) Definitions For purposes of this section the following definitions shall apply: (1) Eligible institution The term eligible institution means a partnership of two or more of the following: (A) An institution of higher education. (B) A State or local government agency which specializes in financial education programs. (C) A nonprofit agency, organization, or association. (D) A financial institution. (E) A small organization that is partnering with, but is not itself, a person described under subparagraph (A) through (D). (2) Institution of higher education The term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ). .\n##### (b) Clerical amendment\nThe table of contents under section 1(b) of the Dodd-Frank Wall Street Reform and Consumer Protection Act is amended by striking the item relating to section 1037 and inserting the following:\nSec. 1037. Authorization for funding the establishment of centers of excellence in financial literacy education. Sec. 1038. Effective date. .",
      "versionDate": "2025-01-16",
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
        "updateDate": "2025-03-27T11:31:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr486",
          "measure-number": "486",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr486v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Young Americans Financial Literacy Act</strong></p><p>This bill requires the Consumer Financial Protection Bureau to award competitive grants to eligible\u00a0institutions for the establishment of financial literacy education programs for young people and families.</p><p>An\u00a0<em>eligible institution</em> is a partnership among two or more of the following:</p><ul><li>an institution of higher education;</li><li>a state or local government agency specializing in financial education;</li><li>a nonprofit agency, organization, or association;</li><li>a financial institution; or</li><li>another small organization.</li></ul><p>Authorized grant funded activities shall include</p><ul><li>developing and implementing comprehensive, research based, financial-literacy education programs for young people;</li><li>developing and supporting the delivery of professional development programs in financial literacy education;</li><li>developing educational programs to reduce student loan default rates; and</li><li>conducting ongoing research and evaluation of financial literacy education programs.</li></ul><p>The\u00a0grant program\u00a0shall terminate\u00a0after FY2029.</p>"
        },
        "title": "Young Americans Financial Literacy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr486.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Young Americans Financial Literacy Act</strong></p><p>This bill requires the Consumer Financial Protection Bureau to award competitive grants to eligible\u00a0institutions for the establishment of financial literacy education programs for young people and families.</p><p>An\u00a0<em>eligible institution</em> is a partnership among two or more of the following:</p><ul><li>an institution of higher education;</li><li>a state or local government agency specializing in financial education;</li><li>a nonprofit agency, organization, or association;</li><li>a financial institution; or</li><li>another small organization.</li></ul><p>Authorized grant funded activities shall include</p><ul><li>developing and implementing comprehensive, research based, financial-literacy education programs for young people;</li><li>developing and supporting the delivery of professional development programs in financial literacy education;</li><li>developing educational programs to reduce student loan default rates; and</li><li>conducting ongoing research and evaluation of financial literacy education programs.</li></ul><p>The\u00a0grant program\u00a0shall terminate\u00a0after FY2029.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr486"
    },
    "title": "Young Americans Financial Literacy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Young Americans Financial Literacy Act</strong></p><p>This bill requires the Consumer Financial Protection Bureau to award competitive grants to eligible\u00a0institutions for the establishment of financial literacy education programs for young people and families.</p><p>An\u00a0<em>eligible institution</em> is a partnership among two or more of the following:</p><ul><li>an institution of higher education;</li><li>a state or local government agency specializing in financial education;</li><li>a nonprofit agency, organization, or association;</li><li>a financial institution; or</li><li>another small organization.</li></ul><p>Authorized grant funded activities shall include</p><ul><li>developing and implementing comprehensive, research based, financial-literacy education programs for young people;</li><li>developing and supporting the delivery of professional development programs in financial literacy education;</li><li>developing educational programs to reduce student loan default rates; and</li><li>conducting ongoing research and evaluation of financial literacy education programs.</li></ul><p>The\u00a0grant program\u00a0shall terminate\u00a0after FY2029.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr486"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr486ih.xml"
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
      "title": "Young Americans Financial Literacy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:53Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Young Americans Financial Literacy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program in the Bureau of Consumer Financial Protection to fund the establishment of centers of excellence to support research, development and planning, implementation, and evaluation of effective programs in financial literacy education for young people and families ages 8 through 24 years old, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T05:33:23Z"
    }
  ]
}
```
