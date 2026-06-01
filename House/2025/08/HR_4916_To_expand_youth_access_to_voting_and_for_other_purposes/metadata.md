# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4916?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4916
- Title: Youth Voting Rights Act
- Congress: 119
- Bill type: HR
- Bill number: 4916
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2026-02-20T20:30:29Z
- Update date including text: 2026-02-20T20:30:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-05 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-05 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4916",
    "number": "4916",
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
    "title": "Youth Voting Rights Act",
    "type": "HR",
    "updateDate": "2026-02-20T20:30:29Z",
    "updateDateIncludingText": "2026-02-20T20:30:29Z"
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
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-08-05T14:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-05T14:03:25Z",
          "name": "Referred To"
        }
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
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "NY"
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
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4916ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4916\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Ms. Williams of Georgia (for herself, Ms. Ansari , Ms. Brown , Mr. Carson , Mrs. Cherfilus-McCormick , Ms. Clarke of New York , Ms. Crockett , Ms. DelBene , Mr. Deluzio , Mr. Doggett , Ms. Elfreth , Mr. Evans of Pennsylvania , Mr. Fields , Mr. Figures , Mr. Garc\u00eda of Illinois , Mr. Green of Texas , Mr. Jackson of Illinois , Mr. Johnson of Georgia , Ms. Kamlager-Dove , Ms. Kelly of Illinois , Mr. Krishnamoorthi , Ms. Lee of Pennsylvania , Mr. Lynch , Ms. McClellan , Mrs. McIver , Mr. Mfume , Mr. Moulton , Mr. Mullin , Ms. Norton , Ms. Pressley , Mrs. Ramirez , Ms. Salinas , Ms. Schakowsky , Mr. Scott of Virginia , Ms. Sewell , Ms. Simon , Ms. Strickland , Mr. Thanedar , Mr. Thompson of Mississippi , Ms. Titus , Ms. Tlaib , and Mr. Tonko ) introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo expand youth access to voting, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Youth Voting Rights Act .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Sense of Congress.\nSec. 3. Findings.\nSec. 4. Enforcement of the 26th Amendment.\nSec. 5. Treatment of public institutions of higher education as voter registration agencies under National Voter Registration Act of 1993.\nSec. 6. Pre-registration of minors for voting in Federal elections.\nSec. 7. On-campus polling locations.\nSec. 8. Prohibition of residency requirements.\nSec. 9. Requirements for voter identification.\nSec. 10. Grants to States for activities to encourage involvement of youth in election activities.\nSec. 11. Absentee voting.\nSec. 12. Studies and data collection.\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\n50 years ago, our Nation came together unanimously to expand the franchise to those 18 years of age and older and to outlaw age-based discrimination in accessing the franchise;\n**(2)**\n50 years later, the promises of the 26th Amendment to the Constitution of the United States (referred to in this Act as the 26th Amendment ) remain unfulfilled although the reasons that motivated its ratification endure; and\n**(3)**\npursuant to section 2 of the 26th Amendment, Congress is empowered to enforce the article by appropriate legislation and acts accordingly in this Act.\n#### 3. Findings\nCongress finds the following:\n**(1)**\nOver 50 years ago, on July 1, 1971, this Nation ratified into the Constitution of the United States the 26th Amendment, lowering the voting age from 21 to 18 years of age and outlawing the denial or abridgement of the right to vote on account of age.\n**(2)**\nSupport for the 26th Amendment was nearly unanimous. The proposed constitutional amendment passed with bipartisan supermajorities, passing in the Senate with a vote of 94\u20130, and passing in the House of Representatives with a vote of 401\u201319. The 26th Amendment was approved by the requisite 38 States in less than 100 days, making it the quickest constitutional amendment to be ratified in United States history.\n**(3)**\nSupport for lowering the voting age to 18 was championed across the aisle. President Dwight Eisenhower, former Commander of the Allied Forces, included the issue in his 1954 State of the Union Address. Moreover, President Richard Nixon emphasized his support for the 26th Amendment during its certification ceremony, describing that young people serve a critical role by infusing the practice of democracy with some idealism, some courage, some stamina, some high moral purpose that this Nation always needs, because a country, throughout history, we find, goes through ebbs and flows of idealism. . Similarly, Senate majority leader Michael Mansfield and Senator Ted Kennedy were key advocates of the measure, having first proposed a statutory route for lowering the voting age in the Voting Rights Act Amendments of 1970 ( Public Law 91\u2013285 ), in addition to supporting a path through constitutional ratification.\n**(4)**\nThe Voting Rights Act Amendments of 1970 ( Public Law 91\u2013285 ) marked the first Federal law to enfranchise youth and outlaw age discrimination in accessing the franchise. In title III of that Act, Congress declared, with strong bipartisan support, that the 21-year age requirement\u2014\n**(A)**\ndenies and abridges the inherent constitutional rights of citizens eighteen years of age but not yet twenty-one years of age to vote ;\n**(B)**\nhas the effect of denying those disenfranchised the due process and equal protection of the laws that are guaranteed to them under the Fourteenth Amendment ; and\n**(C)**\ndoes not bear a reasonable relationship to any compelling State interest. .\n**(5)**\nThe age-based expansion of the franchise via the Voting Rights Act Amendments of 1970 was ultimately found by a strongly divided Supreme Court to be unconstitutional as applied to State and local races and constitutional as applied to Federal races. Thus, to ensure uniform election administration in Federal and State races, a constitutional solution was required.\n**(6)**\nA variety of reasons were advanced to support ratification of the 26th Amendment. The emerging themes included\u2014\n**(A)**\nthe value of idealism, courage, and moral purpose that youth provide in reenergizing the practice of democracy;\n**(B)**\nthe increased political competence of young people compared to prior generations, due to greater access to information through standardized education and technology such as then-widely available television sets;\n**(C)**\nthe increased responsibilities assumed by the group as they fought in war, assumed debt, and lived independently;\n**(D)**\na general recognition of the Nation\u2019s expansion toward a more inclusive suffrage; and\n**(E)**\nthe stemming of unrest by encouraging institutionalized mechanisms to advance change.\n**(7)**\nIn referring the 26th Amendment to the States for ratification, Congress invoked the Voting Rights Act and the principles protected by the 14th Amendment to the Constitution of the United States, explaining that [F]orcing young voters to undertake special burdens-obtaining absentee ballots, or traveling to one centralized location in each city, for example-in order to exercise their right to vote might well serve to dissuade them from participating in the election. This result, and the election procedures that create it, are at least inconsistent with the purpose of the Voting Rights [A]ct, which sought to encourage greater political participation on the part of the young; such segregation might even amount to a denial of their 14th Amendment right to equal protection of the laws in the exercise of the franchise. .\n**(8)**\nAccording to the Center for Information & Research on Civic Learning and Engagement (referred to in this Act as CIRCLE ) of Tufts University, a record-high 28 percent of young people voted in the 2018 midterm elections, more than doubling the record-low 13 percent youth turnout in 2014. Still, young people vote at lower levels than older adults.\n**(9)**\nLower youth voting rates are not a sign of generational apathy but of systemic barriers and issues with the culture of political engagement that have plagued young people of various generations for decades. Individuals that were part of older generations voted at similar rates as individuals in the Millennial and Gen Z generations when those older generations were youth. For the first presidential election in which a generation\u2019s entire 18\u201324 age cohort was eligible to vote (1972 for Boomers, 1992 for Gen X, and 2008 for Millennials), each participated at about 50 percent.\n**(10)**\nThe outsized reliance by young voters on provisional ballots in recent years demonstrates the structural obstacles young voters face due to voter restrictions. A 2016 survey found that 1 in 4 Millennials voted provisionally in the 2016 race, compared to 6 percent of Baby Boomers, and 2 percent of the Greatest Generation.\n**(11)**\nIn addition to voting provisionally at disproportionate rates, young voters\u2019 provisional ballots are also disproportionally rejected. As determined by a recent Federal court, voters aged 18 to 21 in Florida had their provisional ballots rejected at a rate more than 4 times higher than the rejection rate for provisional ballots cast by voters between the ages of 45 to 64.\n**(12)**\nSimilarly, young voters experience a higher rejection rate of vote-by-mail ballots compared to older voters. One study found that voters aged 18 to 21 had their vote-by-mail ballots rejected at a rate of over 5 times that of voters between the ages of 45 to 64 and over 8 times those over the age of 65. These rejection rates trend with those of voters of color. For example, the study found that the rate of rejection of vote-by-mail ballots for Hispanic and African American voters is over 2 times that of White voters.\n**(13)**\nMoreover, when special burdens are removed, young people vote more frequently. Once polling places were finally situated on campuses during the early voting period, pursuant to successful 26th Amendment litigation, one study found that on 12 campuses alone, nearly 60,000 registered voters participated in the 2018 general election through early in-person voting. Young voters, people of color, and those who did not cast a ballot in 2016 disproportionately voted at the on-campus voting locations. Voter turnout is bolstered by on-campus voting locations because those locations lower the opportunity costs for voting for all registered voters, particularly for young registered voters.\n**(14)**\nYoung people are passionate about political issues and often want to engage in the political process, but they face barriers to participation. For example, they may face structural obstacles such as proof requirements that obscure a young person's right to vote, barriers to voter registration, inaccessible or poorly equipped polling places, campus gerrymanders, over-reliance on provisional ballots, unequal access to vote-by-mail, and unfair treatment of provisional and vote-by-mail ballots. Some of these barriers are acute for the youngest voters who are particularly transient and move every year, thereby struggling to update their voter registration, or who are less likely to have a driver\u2019s license to use as voter identification. Youth voters are similarly vulnerable to confusion about their right to vote from their campus residences. Although the Supreme Court summarily affirmed the right of college students to vote from their campus residences in 1979, pursuant to the 26th Amendment, misinformation, disinformation, and legal challenges persist about this right. Congress finds that students indeed have a right to vote from their campus residences. Relatedly, many young people have not been taught about elections and voting, including the practicalities of registering and casting a ballot and the reasons why their voices and votes matter in democracy.\n**(15)**\nSeven States restrict access to vote-by-mail on account of age, allowing voters above a certain age to vote with no excuse, and requiring that voters below 60 or 65 meet a narrow list of excuses to vote-by-mail. In those States, voters 65 and older comprise nearly 65 percent of all at-home ballots, whereas the use of at-home ballots is more evenly distributed across age cohorts in States without the age-restriction. In age-discriminatory vote-at-home States, 21 percent of adults over 65 voted at home in 2018, but less than 6 percent of voters 18\u201334 did so. Congress further finds that eligible voters, including youth, have the right to vote by mail in Federal elections free of prima facie age restrictions.\n**(16)**\nStudies reinforce the habit-forming nature of voting, making it all the more important that voting becomes normalized at an early age through unobstructed access to the ballot. For example, a recent study found that on average, voting in 1 election increases the probability of voting in a future election by 10 percentage points.\n**(17)**\nAccording to CIRCLE, youth without college experience also tend to vote at lower rates than young people in college. For example, in 2018, 28 percent of youth (ages 18\u201329) voted, while the Institute for Democracy & Higher Education of Tufts University estimated that 40 percent of college students cast a ballot. There are disparities by age, and even among youth; the youngest group (ages 18 and 19) vote at lower rates. There are also disparities by urbanicity, with young people in rural areas and other civic deserts having lower voter turnout.\n**(18)**\nAccording to CIRCLE, low-income youth are acutely impacted, since their economic struggles translate into multiple logistical barriers to voting. A recent survey of low-income youth found that young voters reported barriers to voting, including\u2014\n**(A)**\nconfusion with voter identification rules (88 percent);\n**(B)**\nconfusion about the impact of voter disenfranchisement (42 percent reported lack of clarity about whether someone who paid a fine for driving under the influence could vote or if someone with a suspended driver\u2019s license could vote);\n**(C)**\nconfusion about the location of polling places (39 percent did not know where to vote); and\n**(D)**\na high lack of confidence that they would be fully prepared to vote if an election happened next week (only half of surveyed youth reported confidence).\n**(19)**\nMoreover, youth reported negative voting experiences due to failure to see young people working at the polls (87 percent), failure to see poll workers that look like them (74 percent), and not believing that election officials make an effort to ensure that people like them can vote (59 percent).\n**(20)**\nPresidential election years are particularly consequential for youth voter engagement. For example, 61 percent of 18- to 29-year-olds were registered to vote in 2008, compared to 49 percent in 2010. Moreover, youth who registered to vote are considerably more likely to vote. Among youth registered in 2008, 84 percent cast a ballot.\n**(21)**\nWhile direct youth voter registration, outreach, and engagement is typically heightened in the Summer and Fall months leading up to presidential elections, unprecedented obstacles presented themselves amid the COVID\u201319 pandemic as the economy slowed, the Nation shut down, and institutions of higher education, technical and vocational schools, and high schools, along with county election offices, changed their normal operations.\n**(22)**\nThe 2020 primary cycle shed light on the unique obstacles faced by young voters in uncertain times as they were displaced from the college domiciles where they would eventually return. Confused and misinformed about their right to vote from campus despite the temporary relocation, these voters had to adjust for the first time to obtaining, printing, properly filling out and submitting along with required proofs, and mailing postage-required official forms and paperwork, such as voter registration forms, absentee ballot requests, and absentee ballots.\n**(23)**\nThe 2020 election resulted in unprecedented voter turnout overall, boasting the highest turnout in United States history, with 17,000,000 more voters compared to the last presidential cycle. The unprecedented trend tracked for youth voters as well. 2020 was the first election in which the majority of voters under the age of 30 voted. States with the highest youth voter rates were those with more robust registration and vote by mail laws, such as those with pre-registration, same day registration, election day registration, early voting, and accessible no-excuse vote by mail opportunities.\n**(24)**\nThe response to increased voter turnout has been an unprecedented number of State legislative proposals to make it harder to cast a valid ballot, such as the imposition of limitations on the availability of drop-boxes, limitations on the counting of out-of-precinct ballots, and the removal of student identification as valid voter identification where required. Pressures have also mounted on the local level, with continued efforts to prevent or remove on-campus polling locations, which are key to youth engagement since they allow students to vote where they study, work, eat, and sleep.\n**(25)**\nState and local election administration impacts youth at large, including high school youth in their ability to pre-register in advance of turning 18, college students matriculating in traditional public and private 2- or 4-year institutions of higher education or vocational and technical programs, and the most vulnerable or overlooked youth populations, such as those in less stable housing and those who do not pursue college education.\n**(26)**\nThe 14th and 26th Amendments, and the Elections Clause of section 4 of article I and Guarantee Clause of section 4 of article IV, of the Constitution empower Congress to protect the right to vote in Federal elections.\n**(27)**\nThe Voting Rights Act of 1965 was always understood to be privately enforceable, and to contain a private right of action by which all voters of the United States could guarantee the rights guaranteed therein. Recently, in light of the continued development of the law concerning privately enforceable statutes, academic discussion and jurisprudential dicta have incorrectly questioned the Voting Rights Act of 1965\u2019s private right of action. This Act and the amendments made by this Act recognize the hundreds of cases brought by private plaintiffs to enforce the Voting Rights Act of 1965 and re-affirms that such a private right of action has always existed for the Voting Rights Act of 1965.\n#### 4. Enforcement of the 26th Amendment\nTitle III of the Voting Rights Act of 1965 ( 52 U.S.C. 10701 et seq. ) is amended by adding at the end the following:\n303. Private right of action; standard of review; fees (a) Private right of action Any person eighteen years of age and older who is aggrieved by a denial or abridgment of the right of a citizen of the United States to vote on account of age may commence a civil action in any appropriate district court of the United States for relief. (b) Standard of review A denial or abridgment of the right of a citizen of the United States to vote on account of age shall be established in a private right of action under subsection (a) if a qualification or prerequisite to voting or standard, practice, or procedure\u2014 (1) has the effect of denying or abridging to citizens eighteen years of age and older the due process or equal protection of the laws that are guaranteed to them under the 14th and 26th Amendments of the Constitution of the United States; and (2) is not necessary to advance any compelling interest of a State or political subdivision. (c) Fees and costs The court, in an action under this section, shall allow the plaintiff, if the prevailing party, to recover from the defendant reasonable attorneys\u2019 and expert witness fees, and other costs of the action. .\n#### 5. Treatment of public institutions of higher education as voter registration agencies under National Voter Registration Act of 1993\n##### (a) In general\nSection 7(a)(2) of the National Voter Registration Act of 1993 ( 52 U.S.C. 20506(a)(2) ) is amended\u2014\n**(1)**\nby striking and at the end of subparagraph (A);\n**(2)**\nby striking the period at the end of subparagraph (B) and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(C) all offices within public institutions of higher education, as defined in section 101 and section 102(c) of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ; 20 U.S.C. 1002(c) ), that provide assistance to students. .\n##### (b) Application\nSection 4(b) of the National Voter Registration Act of 1993 ( 52 U.S.C. 20503(b) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively, and indenting appropriately;\n**(2)**\nby striking States .\u2014This Act and inserting States .\u2014 ;\n(1) In general Except as provided in paragraph (2), this Act ;\n**(3)**\nin paragraph (1), as added by paragraph (2) of this subsection, by striking paragraphs and inserting subparagraphs ; and\n**(4)**\nby adding at the end the following new paragraph:\n(2) Application of certain requirements Notwithstanding paragraph (1), in the case of a State described in paragraph (1)(B), subsection (a)(3)(B), section 7, and paragraphs (1)(C), (5), and (6) of section 8(a) shall apply, but only with respect to institutions described in section 7(a)(2)(C). .\n#### 6. Pre-registration of minors for voting in Federal elections\n##### (a) Pre-Registration of minors for voting in Federal elections\nThe National Voter Registration Act of 1993 ( 52 U.S.C. 20501 et seq. ) is amended by inserting after section 8 the following new section:\n8A. Pre-registration process for minors (a) Requiring Implementation of Pre-Registration Process Each State shall implement a process under which\u2014 (1) an individual who is a resident of the State may apply to register to vote in elections for Federal office in the State at any time on or after the date on which the individual turns 16 years of age; (2) if the individual is not 18 years of age or older at the time the individual applies under paragraph (1) but would be eligible to vote in such primary or general elections if the individual were 18 years of age, the State shall ensure that the individual is registered to vote in elections for Federal office in the State that are held on or after the date on which the individual turns 18 years of age; and (3) the activities the State implements in order to comply with sections 5 and 7 shall include pre-registration services (to the same extent as registration services) for qualifying individuals, as described in this subsection. (b) Permitting Availability of Process for Younger Individuals A State may, at its option, make the process implemented under subsection (a) available to individuals who are younger than 16 years of age. .\n##### (b) Application\nSection 4(b)(2) of the National Voter Registration Act of 1993 ( 52 U.S.C. 20503(b)(2) ), as added by section 5(b), is amended\u2014\n**(1)**\nby striking paragraph (1)(B), subsection (a)(3)(B) and inserting \u201cparagraph (1)(B)\u2014\n(A) subsection (a)(3)(B) ;\n**(2)**\nin subparagraph (A), as added by paragraph (1), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(B) section 8A shall apply. .\n##### (c) Effective Date\nThe amendments made by this section shall take effect upon the expiration of the 90-day period that begins on the date of the enactment of this Act.\n#### 7. On-campus polling locations\n##### (a) Definitions\nIn this section:\n**(1) Campus**\nThe term campus \u2014\n**(A)**\nmeans a geographic site of an institution of higher education that is permanent in nature and offers courses in educational or training programs which are available for students to attend in person; and\n**(B)**\nincludes main campuses, branch campuses, and additional locations in the United States.\n**(2) Institution of higher education**\nThe term institution of higher education has the meaning given that term in subsections (a) and (b) of section 101 and subsections (b) and (c) of section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) , 1001(b), 1002(b), 1002(c)).\n**(3) State**\nThe term State means each of the several States and the District of Columbia.\n##### (b) In general\nEach State shall ensure that polling places for each election for Federal office (referred to in this section as a Federal election ) are made available, on the date of a Federal election, on\u2014\n**(1)**\neach campus of any State public institution of higher education in the State, except any such campus for which the State has received a waiver under subsection (e); and\n**(2)**\neach campus of any other institution of higher education in the State for which the State has received the institution\u2019s written permission to have a polling place on campus.\n##### (c) Non-State institutions\nNot less than 90 days before the State's deadline for certifying polling place locations in advance of each Federal election, the State shall request in writing permission to place a polling place for a Federal election, to be available on the date of that election, on the campus of each institution of higher education that is not a State public institution of higher education\u2014\n**(1)**\nfor the next Federal election; or\n**(2)**\nfor a longer period of time, as agreed to by the State and the institution of higher education.\n##### (d) Alternative polling places\nFor each institution of higher education that is not a State public institution of higher education and that does not give written permission as described in subsection (c) for placement of a polling place on the institution's campus, the State shall implement alternative procedures to ensure voting is accessible to youth on that campus who are age 18 and over. Such procedures may include\u2014\n**(1)**\noffering free shuttles for such youth to other nearby polling locations;\n**(2)**\nmaking available on the campus absentee voting drop boxes for such youth; or\n**(3)**\noffering an on-campus early voting option or a mobile unit on the campus for early voting or election day voting for such youth.\n##### (e) Waivers\n**(1) In general**\nThe Attorney General may, upon the request of a State, waive the requirement under subsection (b)(1) with respect to a Federal election for a campus described in such paragraph for which the State, in accordance with the guidance under paragraph (3)\u2014\n**(A)**\ndetermines is an unsuitable polling location in the State for that Federal election; and\n**(B)**\nagrees to require alternative procedures at such campus to ensure voting in Federal elections is accessible to youth who are age 18 and over for that Federal election.\n**(2) Applications to include alternative procedures**\nTo request a waiver under paragraph (1) with respect to a Federal election and for a campus described in subsection (b)(1), a State shall submit an application to the Attorney General that includes information on the alternative procedures the State will require the State public institution of higher education to implement with respect to that Federal election for that campus to ensure voting is accessible to youth who are age 18 and over. Such procedures may include\u2014\n**(A)**\noffering free shuttles for such youth to other polling locations;\n**(B)**\nmaking available on the campus absentee voting drop boxes for such youth; or\n**(C)**\noffering an on-campus early voting option or a mobile unit on the campus for early voting or election day voting for such youth.\n**(3) Guidance**\nNot later than 180 days after the date of enactment of this Act, the Attorney General shall issue guidance on the administration of this section, including guidance on the coverage under this section of campuses and institutions of higher education, as defined in subsection (a), acceptable reasons for allowing a waiver under this subsection, and alternative procedures described in paragraph (2), with respect to a campus described in subsection (b)(1). Such guidance shall include considerations of issues relating to the accessibility of the campus, including\u2014\n**(A)**\nthe inability to modify the physical attributes of the campus to make the campus accessible for voting;\n**(B)**\nthe proximity of the campus to local population centers;\n**(C)**\nthe ability of youth age 18 and over who are from historically disadvantaged communities to access the campus;\n**(D)**\nthe ability of the institution of higher education to comply with other Federal or State laws relating to Federal elections at that campus location; and\n**(E)**\nthe number of students enrolled at the institution of higher education in the year of the relevant Federal election.\n##### (f) Enforcement\n**(1) Attorney General**\nThe Attorney General may bring a civil action in an appropriate district court for such declaratory or injunctive relief as is necessary to carry out this section.\n**(2) Private right of action**\n**(A)**\nA person who is aggrieved by a violation of this section may provide written notice of the violation to the chief election official of the State involved.\n**(B)**\nIf the violation is not corrected within 90 days after receipt of a notice under subparagraph (A), or within 20 days after receipt of the notice if the violation occurred within 120 days before the date of a Federal election, the aggrieved person may bring a civil action in an appropriate district court for declaratory or injunctive relief with respect to the violation.\n**(C)**\nIf the violation occurred within 30 days before the date of a Federal election, the aggrieved person need not provide notice to the chief election official of the State under subparagraph (A) before bringing a civil action under subparagraph (B).\n**(D)**\nThe court, in an action under this section, shall allow the plaintiff, if the prevailing party, to recover from the defendant reasonable attorneys\u2019 and expert witness fees and other costs of the action.\n#### 8. Prohibition of residency requirements\n##### (a) Applicability to all elections for Federal office\nSection 202 of the Voting Rights Act of 1965 ( 52 U.S.C. 10502 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1)\u2014\n**(i)**\nby striking the offices of President and Vice President and inserting Federal office ; and\n**(ii)**\nby striking presidential elections and inserting elections for Federal office ;\n**(B)**\nin paragraph (1), by striking their President and Vice President and inserting Federal office ;\n**(C)**\nin paragraph (5), by striking ; and and inserting , and in some cases, the twenty-sixth amendment, including the right to vote from a college domicile; and ; and\n**(D)**\nin paragraph (6), by striking presidential elections and inserting elections for Federal office ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking voting for President and Vice President and inserting voting in elections for Federal office ; and\n**(B)**\nby striking presidential elections and inserting elections for Federal office ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby striking election for President and Vice President and inserting election for Federal office ; and\n**(B)**\nby striking electors for President and Vice President, or for President and Vice President, and inserting Federal office, each place the term appears;\n**(4)**\nin subsection (d), by striking the choice of electors for President and Vice President or for President and Vice President and inserting Federal office ;\n**(5)**\nin subsection (e)\u2014\n**(A)**\nby striking election for President and Vice President and inserting election for Federal office ; and\n**(B)**\nby striking the choice of electors for President and Vice President, or for President and Vice President, and inserting Federal office ; and\n**(6)**\nin subsection (f)\u2014\n**(A)**\nby striking election for President and Vice President and inserting election for Federal office ; and\n**(B)**\nby striking for the choice of electors for President and Vice President, or for President and Vice President, and inserting for Federal office .\n##### (b) Private right of action relating to residence requirements for voting\nSection 202 of the Voting Rights Act of 1965 ( 52 U.S.C. 10502 ) is further amended by adding at the end the following:\n(j) Private right of action Any person who is aggrieved by a violation of this section may commence a civil action in any appropriate district court of the United States for relief. The court, in an action under this section, shall allow the plaintiff, if the prevailing party, to recover from the defendant reasonable attorneys\u2019 and expert witness fees and other costs of the action. .\n#### 9. Requirements for voter identification\n##### (a) In general\nTitle III of the Help America Vote Act of 2002 ( 52 U.S.C. 21081 et seq. ) is amended\u2014\n**(1)**\nby redesignating sections 305 and 306 as sections 306 and 307, respectively; and\n**(2)**\nby inserting after section 304 the following new section:\n305. Treatment of student identification cards as voter identification (a) In general To the extent that a State or local jurisdiction has a voter identification requirement, the State or local jurisdiction shall treat a student identification card issued by an institution of higher education that contains the minimum identifying information required for any other eligible form of voter identification as meeting such voter identification requirement. (b) Institution of higher education For purposes of this section, the term institution of higher education has the meaning given that term in subsections (a) and (b) of section 101 and subsections (b) and (c) of section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) , 1001(b), 1002(b), 1002(c)). .\n##### (b) Conforming amendment relating to enforcement\nSection 401 of such Act ( 52 U.S.C. 21111 ) is amended by striking and 304 and inserting , 304, and 305 .\n##### (c) Clerical amendments\nThe table of contents of such Act is amended\u2014\n**(1)**\nby redesignating the items relating to sections 305 and 306 as relating to sections 306 and 307, respectively; and\n**(2)**\nby inserting after the item relating to section 304 the following new item:\nSec. 305. Treatment of student identification cards as voter identification. .\n#### 10. Grants to States for activities to encourage involvement of youth in election activities\n##### (a) In general\nSubtitle D of title II of the Help America Vote Act of 2002 (52 U.S.C. et seq.) is amended by adding at the end the following:\n7 Grants to encourage youth involvement in election activities 297. Grants to encourage youth involvement in election activities (a) In general The Commission shall make grants to eligible States to increase the involvement of youth, including those under 18 years of age, in public election activities in the State. (b) Eligibility (1) Application A State is eligible to receive a grant under this section if the State submits to the Commission, at such time and in such form as the Commission may require, an application containing\u2014 (A) a description of the State\u2019s plan; (B) a description of the performance measures and targets the State will use to determine its success in carrying out the plan; and (C) such other information and assurances as the Commission may require. (2) Contents of plan A State\u2019s plan under this subsection shall include\u2014 (A) methods to promote the use of the pre-registration process implemented under section 8A of the National Voter Registration Act of 1993; (B) modifications to the curriculum of secondary schools in the State to promote civic engagement; (C) a description of how the State will provide funding to secondary schools and institutions of higher education to enable those schools and institutions to support activities (including activities carried out by student organizations) to increase voter registration and voter turnout, including pre-registration where allowable; (D) the creation of a paid fellowship program for youth to work with State and local election officials to support youth civic and political engagement; (E) a description of how the grant funding will reduce disparities in access to the electoral process among youth who are members of protected classes, as defined by the Commission, under Federal law; and (F) such other activities to encourage the involvement of youth in the electoral process as the State considers appropriate, including encouraging youth to serve as poll workers, deputy voter registrars, or election workers where allowable, and outreach activities to engage secondary schools, postsecondary educational institutions, and the most vulnerable or overlooked youth populations, such as those in less stable housing and those who do not pursue college education. (c) Period of Grant; Report (1) Period of grant A State receiving a grant under this section shall use the funds provided by the grant over a 2-year period agreed to between the State and the Commission. (2) Report Not later than 6 months after the end of the 2-year period agreed to under paragraph (1), the State shall submit to the Commission a report on the activities the State carried out with the funds provided by the grant, and shall include in the report an analysis of the extent to which the State met the performance measures and targets included in its application under subsection (b)(2). (d) State Defined In this section, the term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands. (e) Youth Engagement Fund (1) In general The Commission shall establish a Youth Engagement Fund for the purpose of making grants under this section. (2) Authorization of appropriation There is authorized to be appropriated to the Youth Engagement Fund to carry out this section\u2014 (A) for fiscal year 2026, $26,000,000; and (B) for each subsequent fiscal year, the difference between $26,000,000 and the amount of unobligated funds in the Youth Engagement Fund as of the close of the preceding fiscal year. (3) Availability Funds appropriated pursuant to the authorization of appropriations in paragraph (2) shall remain available for a period of 10 years from the fiscal year in which appropriated. .\n##### (b) Clerical amendment\nThe table of contents of such Act is amended by adding at the end of the items relating to subtitle D of title II the following:\nPART 7\u2014Grants To encourage youth involvement in election activities Sec. 297. Grants to encourage youth involvement in election activities. .\n#### 11. Absentee voting\n##### (a) Enforcement of 26th amendment\nSection 301(a)(1) of the Voting Rights Act of 1965 ( 52 U.S.C. 10701(a)(1) ) is amended by inserting before the period at the end the following: , including denials or abridgements of the rights of citizens of the United States to vote on account of age as a result of age-based restrictions for individuals of legal voting age to voting by mail .\n##### (b) Sense of Congress\nIt is the sense of Congress that age-based restrictions for individuals of legal voting age to vote by mail constitute a violation of the 26th Amendment to the Constitution of the United States.\n#### 12. Studies and data collection\n##### (a) GAO Study\n**(1) In General**\nNot later than 180 days after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report on voter registration trends, absentee voting trends, and provisional voting trends, disaggregated by age and (where information on race is available) race in accordance with paragraph (2), including\u2014\n**(A)**\nan examination of the reliance on absentee and provisional ballots by age;\n**(B)**\nan examination of the availability of polling places on the campuses of institutions of higher education as defined in section 7 of this Act, including consideration of the characteristics of those institutions and the populations they serve;\n**(C)**\nthe rejection rates for voter registration applications and absentee ballot applications;\n**(D)**\nthe rejection rates for absentee ballots and provisional ballots; and\n**(E)**\nthe reasons for those rejections.\n**(2) Disaggregation**\nThe information described in paragraph (1) shall be disaggregated according to (where information on race is available) race and according to the following age cohorts:\n**(A)**\n16 to 17.\n**(B)**\n18 to 21.\n**(C)**\n22 to 24.\n**(D)**\n25 to 29.\n**(E)**\n30 to 34.\n**(F)**\n35 to 39.\n**(G)**\n40 to 44.\n**(H)**\n45 to 49.\n**(I)**\n50 to 54.\n**(J)**\n55 to 59.\n**(K)**\n60 to 64.\n**(L)**\n65 to 69.\n**(M)**\n70 to 74.\n**(N)**\n75 to 79.\n**(O)**\n80 to 84.\n**(P)**\n85 and over.\n##### (b) Election Assistance Commission data collection\n**(1) In general**\nThe Election Assistance Commission shall collect, as a part of the Election Administration and Voting Survey effort, and make publicly available, data from States on\u2014\n**(A)**\napplication and rejection rates of voter registration applications and absentee ballot applications for elections for Federal office based on age and (where information on race is available) race;\n**(B)**\napplication and rejection rates of absentee ballots and the issuance and rejection rates of provisional ballots cast for elections for Federal office based on age and (where information on race is available) race;\n**(C)**\nthe reasons provided by the State for the rejection of such ballots; and\n**(D)**\ninformation on the availability of polling places on the campuses of institutions of higher education as defined in section 7 of this Act, including consideration of the characteristics of those institutions and the populations they serve.\n**(2) Disaggregation**\nThe information described in paragraph (1) shall be disaggregated according to each age cohort described in subparagraphs (A) through (P) of subsection (a)(2).\n**(3) Requiring State submission of information regarding rejected ballots**\n**(A) Requirement**\nTitle III of the Help America Vote Act of 2002 ( 52 U.S.C. 21081 et seq. ) is amended by inserting after section 303 the following new section:\n303A. Required submission of information regarding rejected applications and ballots (a) Requirement Each State shall furnish to the Election Assistance Commission such information as the Commission may request for purposes of carrying out section 12(b) of the Youth Voting Rights Act. (b) Effective date This section shall apply with respect to the elections for Federal office held on or after the date of enactment of this section. .\n**(B) Enforcement**\nSection 401 of such Act ( 52 U.S.C. 21111 ) is amended by striking and 303 and inserting 303, and 303A .\n**(C) Clerical amendment**\nThe table of contents of such Act is amended by inserting after the item relating to section 303 the following new item:\nSec. 303A. Required submission of information regarding rejected applications and ballots. .",
      "versionDate": "2025-08-05",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-15T18:15:20Z"
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
          "measure-id": "id119hr4916",
          "measure-number": "4916",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-05",
          "originChamber": "HOUSE",
          "update-date": "2026-02-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4916v00",
            "update-date": "2026-02-20"
          },
          "action-date": "2025-08-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Youth Voting Rights Act</strong></p><p>This bill expands voting access for youth.</p><p>Specifically, the bill establishes a private right of action to enforce the Twenty-Sixth Amendment, which prohibits denying or abridging the right to vote based on age. Further, the bill authorizes the Department of Justice to enforce the Twenty-Sixth Amendment against age-based restrictions for voting by mail.</p><p>Additionally, the bill directs each state to</p><ul><li>designate as voter registration agencies all offices within public institutions of higher education (IHEs) that provide assistance to students,</li><li>implement a preregistration process to allow minors\u00a0who are 16 years\u00a0or older\u00a0to register to vote in federal elections that take place\u00a0when or after\u00a0the preregistered individual turns age 18, and</li><li>ensure the availability of polling places on campuses of IHEs (with the availability of waivers).</li></ul><p>The bill prohibits durational residency requirements for voting in all federal elections. Currently, this prohibition applies only to voting for the offices of President and Vice President.</p><p>States and local jurisdictions with voter identification requirements must treat IHE-issued student identification cards as voter identification.</p><p>The Election Assistance Commission (EAC) must make grants to states to increase the involvement of individuals under age 18 in public election activities.</p><p>The Government Accountability Office must report to Congress on trends related to voter registration, absentee voting, and provisional voting. The EAC must also collect and make publicly available certain data from states.</p>"
        },
        "title": "Youth Voting Rights Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4916.xml",
    "summary": {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Youth Voting Rights Act</strong></p><p>This bill expands voting access for youth.</p><p>Specifically, the bill establishes a private right of action to enforce the Twenty-Sixth Amendment, which prohibits denying or abridging the right to vote based on age. Further, the bill authorizes the Department of Justice to enforce the Twenty-Sixth Amendment against age-based restrictions for voting by mail.</p><p>Additionally, the bill directs each state to</p><ul><li>designate as voter registration agencies all offices within public institutions of higher education (IHEs) that provide assistance to students,</li><li>implement a preregistration process to allow minors\u00a0who are 16 years\u00a0or older\u00a0to register to vote in federal elections that take place\u00a0when or after\u00a0the preregistered individual turns age 18, and</li><li>ensure the availability of polling places on campuses of IHEs (with the availability of waivers).</li></ul><p>The bill prohibits durational residency requirements for voting in all federal elections. Currently, this prohibition applies only to voting for the offices of President and Vice President.</p><p>States and local jurisdictions with voter identification requirements must treat IHE-issued student identification cards as voter identification.</p><p>The Election Assistance Commission (EAC) must make grants to states to increase the involvement of individuals under age 18 in public election activities.</p><p>The Government Accountability Office must report to Congress on trends related to voter registration, absentee voting, and provisional voting. The EAC must also collect and make publicly available certain data from states.</p>",
      "updateDate": "2026-02-20",
      "versionCode": "id119hr4916"
    },
    "title": "Youth Voting Rights Act"
  },
  "summaries": [
    {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Youth Voting Rights Act</strong></p><p>This bill expands voting access for youth.</p><p>Specifically, the bill establishes a private right of action to enforce the Twenty-Sixth Amendment, which prohibits denying or abridging the right to vote based on age. Further, the bill authorizes the Department of Justice to enforce the Twenty-Sixth Amendment against age-based restrictions for voting by mail.</p><p>Additionally, the bill directs each state to</p><ul><li>designate as voter registration agencies all offices within public institutions of higher education (IHEs) that provide assistance to students,</li><li>implement a preregistration process to allow minors\u00a0who are 16 years\u00a0or older\u00a0to register to vote in federal elections that take place\u00a0when or after\u00a0the preregistered individual turns age 18, and</li><li>ensure the availability of polling places on campuses of IHEs (with the availability of waivers).</li></ul><p>The bill prohibits durational residency requirements for voting in all federal elections. Currently, this prohibition applies only to voting for the offices of President and Vice President.</p><p>States and local jurisdictions with voter identification requirements must treat IHE-issued student identification cards as voter identification.</p><p>The Election Assistance Commission (EAC) must make grants to states to increase the involvement of individuals under age 18 in public election activities.</p><p>The Government Accountability Office must report to Congress on trends related to voter registration, absentee voting, and provisional voting. The EAC must also collect and make publicly available certain data from states.</p>",
      "updateDate": "2026-02-20",
      "versionCode": "id119hr4916"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4916ih.xml"
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
      "title": "Youth Voting Rights Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T06:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Youth Voting Rights Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T06:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand youth access to voting, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T06:48:35Z"
    }
  ]
}
```
