# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/581?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/581
- Title: Providing for consideration of the bill (H.R. 185) to advance responsible policies.
- Congress: 119
- Bill type: HRES
- Bill number: 581
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2026-04-03T18:18:38Z
- Update date including text: 2026-04-03T18:18:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Rules.
- 2025-07-15 - IntroReferral: Submitted in House
- 2025-07-15 - IntroReferral: Submitted in House
- 2025-09-02 - Discharge: Motion to Discharge Committee filed by Mr. Massie. Petition No: 119-9. (<a href="https://clerk.house.gov/DischargePetition/2025090209">Discharge petition</a> text with signatures.)
- 2025-11-12 - Discharge: Motion to discharge the Committee on Rules filed by Mr. Massie. Assigned to the Discharge Calendar, Calendar No. 2. (consideration: CR H4665)
- 2025-11-19 12:03:10 - Floor: Pursuant to the provisions of H. Res. 879, H. Res. 581 is laid on the table.
- Latest action: 2025-07-15: Submitted in House

## Actions

- 2025-07-15 - IntroReferral: Referred to the House Committee on Rules.
- 2025-07-15 - IntroReferral: Submitted in House
- 2025-07-15 - IntroReferral: Submitted in House
- 2025-09-02 - Discharge: Motion to Discharge Committee filed by Mr. Massie. Petition No: 119-9. (<a href="https://clerk.house.gov/DischargePetition/2025090209">Discharge petition</a> text with signatures.)
- 2025-11-12 - Discharge: Motion to discharge the Committee on Rules filed by Mr. Massie. Assigned to the Discharge Calendar, Calendar No. 2. (consideration: CR H4665)
- 2025-11-19 12:03:10 - Floor: Pursuant to the provisions of H. Res. 879, H. Res. 581 is laid on the table.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/581",
    "number": "581",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies.",
    "type": "HRES",
    "updateDate": "2026-04-03T18:18:38Z",
    "updateDateIncludingText": "2026-04-03T18:18:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H1B000",
      "actionDate": "2025-11-19",
      "actionTime": "12:03:10",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Pursuant to the provisions of H. Res. 879, H. Res. 581 is laid on the table.",
      "type": "Floor"
    },
    {
      "actionCode": "H12450",
      "actionDate": "2025-11-12",
      "calendarNumber": {
        "calendar": "D00002"
      },
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to discharge the Committee on Rules filed by Mr. Massie. Assigned to the Discharge Calendar, Calendar No. 2. (consideration: CR H4665)",
      "type": "Discharge"
    },
    {
      "actionCode": "H17000",
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to Discharge Committee filed by Mr. Massie. Petition No: 119-9. (<a href=\"https://clerk.house.gov/DischargePetition/2025090209\">Discharge petition</a> text with signatures.)",
      "type": "Discharge"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
            "date": "2025-11-12T21:57:46Z",
            "name": "Unknown"
          },
          {
            "date": "2025-07-15T14:05:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "GA"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "TN"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "MO"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "CO"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "NJ"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "AZ"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "FL"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MI"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "OH"
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
      "sponsorshipDate": "2025-07-17",
      "state": "MA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "SC"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "MD"
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
      "sponsorshipDate": "2025-07-21",
      "state": "WA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NY"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "TX"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "MI"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "FL"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CO"
    },
    {
      "bioguideId": "P000197",
      "district": "11",
      "firstName": "Nancy",
      "fullName": "Rep. Pelosi, Nancy [D-CA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pelosi",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CA"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NV"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
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
      "sponsorshipDate": "2025-07-23",
      "state": "DC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NH"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CO"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MD"
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "AZ"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "PA"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CO"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NY"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "OH"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NY"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "OR"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "MO"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
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
      "sponsorshipDate": "2025-09-03",
      "state": "MO"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres581ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 581\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Mr. Massie (for himself and Mr. Khanna ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 185) to advance responsible policies.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 185) to advance responsible policies. All points of order against consideration of the bill are waived. The amendment in the nature of a substitute specified in section 4 of this resolution shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on the Judiciary or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.R. 185.\n#### 3.\nThe Clerk shall transmit to the Senate a message that the House has passed H.R. 185 no later than one week after passage.\n#### 4.\nThe amendment in the nature of a substitute referred to in the first section of this resolution is as follows:\nStrike all after the enacting clause and insert the following:\n1. Short title This Act may be cited as the Epstein Files Transparency Act . 2. Release of documents relating to Jeffrey Epstein (a) In general Not later than 30 days after the date of enactment of this Act, the Attorney General shall, subject to subsection (b), make publicly available in a searchable and downloadable format all unclassified records, documents, communications, and investigative materials in the possession of the Department of Justice, including the Federal Bureau of Investigation and United States Attorneys\u2019 Offices, that relate to: (1) Jeffrey Epstein including all investigations, prosecutions, or custodial matters. (2) Ghislaine Maxwell. (3) Flight logs or travel records, including but not limited to manifests, itineraries, pilot records, and customs or immigration documentation, for any aircraft, vessel, or vehicle owned, operated, or used by Jeffrey Epstein or any related entity. (4) Individuals, including government officials, named or referenced in connection with Epstein\u2019s criminal activities, civil settlements, immunity or plea agreements, or investigatory proceedings. (5) Entities (corporate, nonprofit, academic, or governmental) with known or alleged ties to Epstein\u2019s trafficking or financial networks. (6) Any immunity deals, non-prosecution agreements, plea bargains, or sealed settlements involving Epstein or his associates. (7) Internal DOJ communications, including emails, memos, meeting notes, concerning decisions to charge, not charge, investigate, or decline to investigate Epstein or his associates. (8) All communications, memoranda, directives, logs, or metadata concerning the destruction, deletion, alteration, misplacement, or concealment of documents, recordings, or electronic data related to Epstein, his associates, his detention and death, or any investigative files. (9) Documentation of Epstein\u2019s detention or death, including incident reports, witness interviews, medical examiner files, autopsy reports, and written records detailing the circumstances and cause of death. (b) Prohibited grounds for withholding No record shall be withheld, delayed, or redacted on the basis of any of the following: (1) Embarrassment, reputational harm, or political sensitivity, including to any government official, public figure, or foreign dignitary. (c) Permitted withholdings (1) The Attorney General may withhold or redact the segregable portions of records that\u2014 (A) contain personally identifiable information of victims or victims\u2019 personal and medical files and similar files the disclosure of which would constitute a clearly unwarranted invasion of personal privacy; (B) depicts or contains child sexual abuse materials (CSAM) as defined under 18 U.S.C. 2256 and prohibited under 18 U.S.C. 2252\u20132252A; (C) would jeopardize an active federal investigation or ongoing prosecution, provided that such withholding is narrowly tailored and temporary; (D) depicts or contains images of death, physical abuse, or injury of any person; or (E) contain information specifically authorized under criteria established by an Executive order to be kept secret in the interest of national defense or foreign policy and are in fact properly classified pursuant to such Executive order. (2) All redactions must be accompanied by a written justification published in the Federal Register and submitted to Congress. (3) To the extent that any covered information would otherwise be redacted or withheld as classified information under this section, the Attorney General shall declassify that classified information to the maximum extent possible. (A). If the Attorney General makes a determination that covered information may not be declassified and made available in a manner that protects the national security of the United States, including methods or sources related to national security, the Attorney General shall release an unclassified summary for each of the redacted or withheld classified information. (4) All decisions to classify any covered information after July 1, 2025 shall be published in the Federal Register and submitted to Congress, including the date of classification, the identity of the classifying authority, and an unclassified summary of the justification. 3. Report to Congress Within 15 days of completion of the release required under Section 2, the Attorney General shall submit to the House and Senate Committees on the Judiciary a report listing: (1) All categories of records released and withheld. (2) A summary of redactions made, including legal basis. (3) A list of all government officials and politically exposed persons named or referenced in the released materials, with no redactions permitted under subsection (b)(1). .",
      "versionDate": "2025-07-15",
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
        "actionDate": "2025-11-19",
        "text": "Became Public Law No: 119-38."
      },
      "number": "4405",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Epstein Files Transparency Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-18",
        "actionTime": "15:05:03",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "879",
      "relationshipDetails": {
        "item": [
          {
            "identifiedBy": "House",
            "type": "Procedurally related"
          },
          {
            "identifiedBy": "House",
            "type": "Procedurally related"
          }
        ]
      },
      "title": "Providing for consideration of the joint resolution (S.J. Res. 80) providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to ''National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision''; providing for consideration of the joint resolution (H.J. Res. 130) providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to ''Buffalo Field Office Record of Decision and Approved Resource Management Plan Amendment''; providing for consideration of the joint resolution (H.J. Res. 131) providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to ''Coastal Plain Oil and Gas Leasing Program Record of Decision''; providing for consideration of the concurrent resolution (H. Con. Res. 58) denouncing the horrors of socialism; providing for consideration of the bill (H.R. 1949) to repeal restrictions on the export and import of natural gas; providing for consideration of the bill (H.R. 3109) to require the Secretary of Energy to direct the National Petroleum Council to issue a report with respect to petrochemical refineries in the United States, and for other purposes; providing for consideration of the bill (H.R. 5107) to repeal the Comprehensive Policing and Justice Reform Amendment Act of 2022 enacted by the District of Columbia Council; providing for consideration of the bill (H.R. 5214) to require mandatory pretrial and post conviction detention for crimes of violence and dangerous crimes and require mandatory cash bail for certain offenses that pose a threat to public safety or order in the District of Columbia, and for other purposes; and for other purposes.",
      "type": "HRES"
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
            "name": "House of Representatives",
            "updateDate": "2025-12-02T19:37:35Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-12-02T19:37:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-09-08T13:18:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-15",
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
          "measure-id": "id119hres581",
          "measure-number": "581",
          "measure-type": "hres",
          "orig-publish-date": "2025-07-15",
          "originChamber": "HOUSE",
          "update-date": "2025-09-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres581v00",
            "update-date": "2025-09-09"
          },
          "action-date": "2025-07-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution provides a special\u00a0rule\u00a0for consideration of\u00a0H.R. 185 and amends that bill to direct the Department of Justice (DOJ) to make publicly available certain records related to Jeffrey Epstein or Ghislaine Maxwell.</p><p>Under H.R. 185, as amended by the resolution,\u00a0DOJ\u00a0must publicly disclose all unclassified records, documents, communications, and investigative materials in its possession that relate to Epstein or Maxwell. The records include unclassified records referring or relating to\u00a0Epstein's detention and death; flight logs of aircraft owned or used by Epstein; individuals named in connection with Epstein\u2019s criminal activities, civil settlements, or immunity or plea agreements; immunity deals, sealed settlements, or plea bargains of Epstein or his associates; entities with ties to Epstein\u2019s trafficking or financial networks; and internal Department of Justice communications concerning decisions to investigate or charge Epstein or his associates.\u00a0</p><p>However, under the amended bill, DOJ may withhold or redact portions of records with written justification that such portions contain (1) victims' personally identifiable information; (2) child sexual abuse materials; (3) images of death, physical abuse, or injury; (4) information which would jeopardize an active federal investigation or prosecution; or (5) classified information. DOJ may not withhold or redact records on the basis of embarrassment,\u00a0reputational harm, or political sensitivity.</p><p>Further, within 15 days of completing the required disclosures, DOJ must provide Congress with a report listing all categories of records released and withheld, all redactions\u00a0made and their legal basis, and all government officials and politically exposed persons named or referenced in the released materials.</p>"
        },
        "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres581.xml",
    "summary": {
      "actionDate": "2025-07-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides a special\u00a0rule\u00a0for consideration of\u00a0H.R. 185 and amends that bill to direct the Department of Justice (DOJ) to make publicly available certain records related to Jeffrey Epstein or Ghislaine Maxwell.</p><p>Under H.R. 185, as amended by the resolution,\u00a0DOJ\u00a0must publicly disclose all unclassified records, documents, communications, and investigative materials in its possession that relate to Epstein or Maxwell. The records include unclassified records referring or relating to\u00a0Epstein's detention and death; flight logs of aircraft owned or used by Epstein; individuals named in connection with Epstein\u2019s criminal activities, civil settlements, or immunity or plea agreements; immunity deals, sealed settlements, or plea bargains of Epstein or his associates; entities with ties to Epstein\u2019s trafficking or financial networks; and internal Department of Justice communications concerning decisions to investigate or charge Epstein or his associates.\u00a0</p><p>However, under the amended bill, DOJ may withhold or redact portions of records with written justification that such portions contain (1) victims' personally identifiable information; (2) child sexual abuse materials; (3) images of death, physical abuse, or injury; (4) information which would jeopardize an active federal investigation or prosecution; or (5) classified information. DOJ may not withhold or redact records on the basis of embarrassment,\u00a0reputational harm, or political sensitivity.</p><p>Further, within 15 days of completing the required disclosures, DOJ must provide Congress with a report listing all categories of records released and withheld, all redactions\u00a0made and their legal basis, and all government officials and politically exposed persons named or referenced in the released materials.</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119hres581"
    },
    "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies."
  },
  "summaries": [
    {
      "actionDate": "2025-07-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides a special\u00a0rule\u00a0for consideration of\u00a0H.R. 185 and amends that bill to direct the Department of Justice (DOJ) to make publicly available certain records related to Jeffrey Epstein or Ghislaine Maxwell.</p><p>Under H.R. 185, as amended by the resolution,\u00a0DOJ\u00a0must publicly disclose all unclassified records, documents, communications, and investigative materials in its possession that relate to Epstein or Maxwell. The records include unclassified records referring or relating to\u00a0Epstein's detention and death; flight logs of aircraft owned or used by Epstein; individuals named in connection with Epstein\u2019s criminal activities, civil settlements, or immunity or plea agreements; immunity deals, sealed settlements, or plea bargains of Epstein or his associates; entities with ties to Epstein\u2019s trafficking or financial networks; and internal Department of Justice communications concerning decisions to investigate or charge Epstein or his associates.\u00a0</p><p>However, under the amended bill, DOJ may withhold or redact portions of records with written justification that such portions contain (1) victims' personally identifiable information; (2) child sexual abuse materials; (3) images of death, physical abuse, or injury; (4) information which would jeopardize an active federal investigation or prosecution; or (5) classified information. DOJ may not withhold or redact records on the basis of embarrassment,\u00a0reputational harm, or political sensitivity.</p><p>Further, within 15 days of completing the required disclosures, DOJ must provide Congress with a report listing all categories of records released and withheld, all redactions\u00a0made and their legal basis, and all government officials and politically exposed persons named or referenced in the released materials.</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119hres581"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres581ih.xml"
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
      "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:48Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for consideration of the bill (H.R. 185) to advance responsible policies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T11:31:55Z"
    }
  ]
}
```
