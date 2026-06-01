# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2486?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2486
- Title: Heating and Cooling Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 2486
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-01-10T07:12:57Z
- Update date including text: 2026-01-10T07:12:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2486",
    "number": "2486",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "A000381",
        "district": "3",
        "firstName": "Yassamin",
        "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
        "lastName": "Ansari",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Heating and Cooling Relief Act",
    "type": "HR",
    "updateDate": "2026-01-10T07:12:57Z",
    "updateDateIncludingText": "2026-01-10T07:12:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:01:05Z",
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
          "date": "2025-03-31T16:01:00Z",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MO"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
      "state": "LA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "FL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
      "state": "TN"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
      "state": "IL"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CO"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "TX"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "PA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "LA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
      "state": "GA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-31",
      "state": "PA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
      "state": "WI"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
      "state": "MN"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CO"
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
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-31",
      "state": "IL"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
      "state": "MI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-04-07",
      "state": "VT"
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
      "sponsorshipDate": "2025-04-08",
      "state": "NC"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "FL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
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
      "sponsorshipDate": "2025-05-05",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CT"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "WA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "IN"
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
      "sponsorshipDate": "2025-12-17",
      "state": "AZ"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "MD"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2486ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2486\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Ms. Ansari (for herself, Ms. Barrag\u00e1n , Mr. Bell , Mr. Carson , Mr. Carter of Louisiana , Ms. Castor of Florida , Mrs. Cherfilus-McCormick , Mr. Cleaver , Mr. Cohen , Ms. Crockett , Mr. Davis of Illinois , Ms. DeGette , Mr. Doggett , Mr. Evans of Pennsylvania , Mr. Fields , Mr. Huffman , Mr. Johnson of Georgia , Mr. Khanna , Ms. Lee of Pennsylvania , Mrs. McIver , Ms. Meng , Ms. Moore of Wisconsin , Mr. Mullin , Ms. Norton , Ms. Ocasio-Cortez , Ms. Omar , Ms. Pettersen , Mrs. Ramirez , Ms. S\u00e1nchez , Ms. Schakowsky , Mr. Smith of Washington , Mr. Thanedar , Mr. Thompson of Mississippi , Ms. Titus , Ms. Tlaib , and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Low-Income Home Energy Assistance Act of 1981 to increase the availability of heating and cooling assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Heating and Cooling Relief Act .\n#### 2. Findings\nCongress finds that:\n**(1)**\nEnergy remains unaffordable for low-income households. Nationally, low-income households spend a larger portion of their income on home energy costs than other households. While the average energy burden for non-low-income households is approximately 3 percent, low-income households experience energy burdens that are 3 times higher, with 1 in 4 low-income households spending more than 15 percent of their income on energy bills. The report for the Household Pulse Survey of the Bureau of the Census, issued on October 3, 2024, noted that, for families with incomes of less than $35,000 a year, about 54 percent said that they reduced or went without basic household necessities, such as medicine or food, in order to pay an energy bill, for at least one month in the last year.\n**(2)**\nThe Low-Income Housing Energy Assistance Program was authorized by Congress to reduce home energy burdens with heating and cooling assistance. In 2023, only 18 percent of income-eligible households received a subsidy under the program.\n**(3)**\nClimate change is fueling increasingly intense winter storms, frequent hurricanes and wildfires, and extreme temperatures. Over the past 2 decades, the United States has seen a 135 percent increase in billion-dollar winter disasters, fueled by climate change, rising from 31 of those disasters from 1985 through 2004, to 73 of those disasters from 2005 through 2024.\n**(4)**\nHeat waves are increasingly common as climate change accelerates, and now occur more often in major cities across the United States. According to reports from the National Aeronautics and Space Administration, 2024 was the hottest year on record in Earth\u2019s history. The average heat wave season across 50 cities is approximately 46 days longer now than it was in the 1960s, and the American Medical Association found that heat-related deaths have increased by over 16 percent per year since 2016. However, in fiscal year 2023, less than 3 percent of income-eligible households received cooling assistance under the Low-Income Home Energy Assistance Program, with only 7 percent of funding from the Low-Income Home Energy Assistance Program going toward cooling needs. As a result, the Federal Government should provide further cooling assistance for communities in need.\n**(5)**\nAs a result of rising home energy bills and insufficient Federal funding for the Low-Income Home Energy Assistance Program, residential utility arrears, or the amount of funds owed by households to their utilities, has climbed to an all-time high of over $21,000,000,000 as of September 2024, with over 21,000,000 households in debt to electric utilities and over 15,000,000 households in debt to natural gas companies. Nearly 1 out of every 7 households is behind on their electric or gas bill.\n**(6)**\nWhile most States have shutoff protections that prevent utility companies from disconnecting a customer\u2019s energy service during the coldest winter months, 10 States have no winter shutoff protections, and 29 States have no summer shutoff protections. Even in certain States with winter or summer shutoff protections, shutoffs continue to increase as the period around the hottest and coldest months lengthens.\n**(7)**\nThe loss of home energy service due to high energy burdens is one of the primary reasons for homelessness, especially for families with children. In some housing contexts, loss of home energy service is a grounds for eviction.\n**(8)**\nThe Federal Government should expand and update the Low-Income Home Energy Assistance Program, as part of a robust Federal social safety net, to\u2014\n**(A)**\nprotect families against unaffordable home energy bills and home energy shutoffs, by providing sufficient funding and imposing regulations where necessary;\n**(B)**\nensure all low- and moderate-income families have access to affordable home cooling powered by renewable energy, which will enable households to adapt to rising temperatures due to climate change and promote climate and energy resiliency;\n**(C)**\nenhance timely and meaningful public participation and outreach\u2014\n**(i)**\nby including nontraditional partners, including home energy suppliers, local educational agencies, and entities carrying out other programs for low-income people, to assist with signups; and\n**(ii)**\nby adding stronger provisions for presumed eligibility and waiving documentation requirements for eligibility; and\n**(D)**\nfurther Federal efforts to weatherize housing for low- and moderate-income households, to help families struggling to pay their home energy bills and to meet national clean energy goals.\n#### 3. Funding\nSection 2602 of the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8621 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby striking section 2607A) and inserting section 2604(e), 2605(u), 2607A, 2607B, or 2607C) ; and\n**(B)**\nby striking $2,000,000,000 and all that follows and inserting such sums as may be necessary, including such sums as may be necessary to enable the States to assist all households that meet the eligibility requirements established under this title and to enable States to implement home energy affordability measures described in section 2605(b)(3). ;\n**(2)**\nin subsection (e), in the first sentence\u2014\n**(A)**\nby striking in each fiscal year ;\n**(B)**\nby striking $600,000,000 and inserting $2,000,000,000 for fiscal year 2026, and $2,000,000,000 plus such additional sums as may be necessary for each fiscal year thereafter, ; and\n**(C)**\nby inserting , or arising from a major disaster, as defined in section 2604(e)(1) before the period at the end; and\n**(3)**\nby adding at the end the following:\n(f) There is authorized to be appropriated to carry out section 2607C, including making grants under that section, $1,000,000,000 for fiscal year 2026, and $1,000,000,000 plus such additional sums as may be necessary for each fiscal year thereafter. .\n#### 4. Definitions\nSection 2603 of the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8622 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (4) through (6), (7) through (10), and (11), as paragraphs (6) through (8), (10) through (13), and (15), respectively;\n**(2)**\nby inserting after paragraph (3) the following:\n(4) The terms extreme heat and extreme cold , used with respect to a period, means a period in which there is an increased risk of\u2014 (A) heat-related or cold-related, respectively, illness, hospitalization, or death; or (B) failures or energy shutoffs of home cooling or heating, respectively. (5) The term HEAP coordinator means an employee\u2014 (A) who administers a program funded under section 2602(b); and (B) whose salary is paid, partly or wholly, with funds made available under that section. ;\n**(3)**\nby inserting after paragraph (8), as so redesignated, the following:\n(9) The term local coordinating agency means any local organization or local office that receives funds under section 2602(b) to perform customer intake, or approval of benefits, on behalf of the State agency. ; and\n**(4)**\nby inserting after paragraph (13), as so redesignated, the following:\n(14) The term State agency means any State agency that administers the program funded under section 2602(b). .\n#### 5. Assistance for emergencies and major disasters, including extreme heat and cold\nSection 2604 of the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8623 ) is amended\u2014\n**(1)**\nin subsection (a)(1)(B), by striking section 2605(b)(9)(B) and inserting section 2605(b)(10)(B) ; and\n**(2)**\nin subsection (e)\u2014\n**(A)**\nby striking (e) and inserting the following:\n(e) (1) In this subsection: (2) ;\n**(B)**\nin paragraph (1), by adding at the end the following:\n(A) The term covered household means an eligible household in an area where the President, or the Secretary, as the case may be, has declared or determined the occurrence of a natural disaster, emergency, or major disaster. (B) The term major disaster means\u2014 (i) a major disaster or emergency declared under section 401 or 501, respectively, of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 , 5191); (ii) a public health emergency determined under section 319 of the Public Health Service Act ( 42 U.S.C. 247d ); or (iii) a period of extreme heat or extreme cold, as determined by the Secretary. ;\n**(C)**\nin paragraph (2), as so designated, by striking natural disaster or other emergency involved and inserting natural disaster, emergency, or major disaster involved ; and\n**(D)**\nby adding at the end the following:\n(3) Upon a declaration or a determination of a natural disaster, emergency, or major disaster, for an area, the Secretary and the Administrator of the Federal Emergency Management Agency shall, to the extent practicable, provide heating or cooling assistance through such an allotment to a State for covered households in that area. (4) To receive assistance under this subsection, the State that has jurisdiction over the covered households shall provide assurances to the Secretary that the State\u2014 (A) will not preclude a household that receives heating assistance or cooling assistance under this title during a calendar year, on the basis of obtaining that assistance, from receiving cooling assistance or heating assistance, respectively, under this title during that year; (B) will not require a household to indicate that a household member has a medical need for assistance under this title, to be eligible for that assistance; and (C) will allow use of such assistance for purposes for which heating or cooling assistance is available under the program funded under section 2602(b), including for providing energy-efficient air conditioners, and other equipment needed for home cooling, to eligible households. .\n#### 6. Eligible households\nSection 2605 of the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8624 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)(A), by striking paragraph (5) and inserting paragraph (6) ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting , subject to subsection (c)(1)(A), after only ;\n**(ii)**\nin subparagraph (B), by striking (B) and all that follows through clause (ii) and inserting the following:\n(B) households with incomes which do not exceed the greater of\u2014 (i) an amount equal to 250 percent of the poverty level; or (ii) an amount equal to 80 percent of the State median income, ; and\n**(iii)**\nin the matter following subparagraph (B)\u2014\n**(I)**\nby striking may give and inserting shall give ; and\n**(II)**\nby inserting before the semicolon the following: , and the State may not exclude a household from eligibility on the basis of citizenship of 1 or more of the household members ;\n**(C)**\nby redesignating paragraphs (3) through (16) as paragraphs (4) through (17), respectively;\n**(D)**\nby inserting after paragraph (2) the following:\n(3) Energy burden limits To the extent practicable, the Secretary shall work with States using funding under section 2602(b) (supplemented by funding available through State-level energy programs, utility affordability initiatives, or other mechanisms as determined by the State in consultation with the Secretary) to implement home energy affordability measures\u2014 (A) to ensure that no household eligible under paragraph (2) experiences an energy burden for which the expenditures of the household for home energy exceed 3 percent of household income; and (B) to prioritize the further reduction of energy burdens for such eligible households with the lowest incomes. ; and\n**(E)**\nin subparagraph (B) of paragraph (10), as so redesignated, by striking paragraph (16) and inserting paragraph (17) ;\n**(2)**\nin subsection (c)(1)\u2014\n**(A)**\nin subparagraph (A), by striking assistance to be provided under this title, including criteria and inserting\nassistance to be provided under this title, including\u2014 (i) certifying that the State and local coordinating agencies in the State\u2014 (I) shall, to the greatest extent possible, use data sharing agreements with Federal and State low-income assistance programs, including the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ), the Medicaid program established under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), and the supplemental security income program established under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ), to verify eligibility; (II) shall implement simplified re-enrollment procedures for households with fixed incomes or households already determined to be eligible under other Federal and State low-income assistance programs, to reduce administrative burdens on applicants and agencies; (III) shall not require applicants to submit proof of citizenship to establish status as an eligible household; and (IV) if neither the verification process described in subclause (I) nor the re-enrollment process described in subclause (II) apply to a household, shall allow applicants to self-attest that the applicants meet the criteria established under this title for an eligible household, to the extent necessary to facilitate access to assistance and prevent undue hardship for applicants; and (ii) describing criteria. ;\n**(B)**\nin subparagraph (E), by striking paragraph (5) and inserting paragraph (6) ; and\n**(C)**\nin subparagraph (F), by striking clauses (3), (4), (5), (6), (7), (8), (10), (12), (13), and (15) of subsection (b) and inserting paragraphs (4), (5), (6), (7), (8), (9), (11), (13), (14), and (16) of subsection (b) ;\n**(3)**\nin subsection (e), by striking subsection (b)(10) and inserting subsection (b)(11) ;\n**(4)**\nin subsection (f), by adding at the end the following:\n(3) For purposes of section 401(c), and the remainder of title IV, of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1611(a) , 1601 et seq.), assistance under this title shall not be considered to be a Federal public benefit. ; and\n**(5)**\nin subsection (j), by striking the State may apply and inserting the State may, subject to subsection (c)(1)(A)(i), apply .\n#### 7. Conditions for funding\nSection 2605 of the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8624 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)(C), by inserting before the semicolon the following: , using toxics-free materials that do not contain asthmagens or respiratory sensitizers, giving priority in the use of those funds under this subparagraph, to the greatest extent practicable, to supporting emergency home repairs that foster energy efficiency, decarbonization, and climate resilience, including through beneficial electrification of heating and cooling ;\n**(B)**\nin paragraph (8), as so redesignated\u2014\n**(i)**\nin subparagraph (C), by striking and at the end; and\n**(ii)**\nby adding at the end the following:\n(E) ensure that\u2014 (i) the home energy supplier will not charge late fees for any payment, by a household receiving assistance through the program funded under section 2602(b), during the period beginning 6 months before and ending 6 months after a date on which the supplier receives funds through the program for the household; and (ii) if the supplier receives funds through the program for such a household and charged such late fees during that period, the supplier shall refund the fees to the household not later than 7 days after the date the supplier receives the funds; (F) ensure that the home energy supplier will not shut off home energy from a household that received assistance through the program funded under section 2602(b), within the 2-year period beginning on the date the household received the assistance; (G) ensure that the home energy supplier, in return for receiving funds through the program funded under section 2602(b)\u2014 (i) will provide to the State data on households that have not paid their home energy bills, to enable the State and the supplier to carry out coordinated outreach concerning assistance available through the program funded under section 2602(b); and (ii) will, when sending a notice of late payments to such households, include information on such assistance, on how to access such assistance through the program, and on eligibility criteria for the program; and (H) ensure that the home energy supplier will, not later than 2 years after the date of enactment of the Heating and Cooling Relief Act, in return for receiving assistance under the program funded under section 2602(b) and through a partnership with the State, offer a low-income energy affordability payment program; ; and\n**(C)**\nin paragraph (10), as so redesignated\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking 10 percent and inserting 15 percent ; and\n**(II)**\nby striking and at the end; and\n**(ii)**\nby adding at the end the following:\n(C) in planning and administering that program, the State shall use the portion of the amount described in subparagraph (A), that exceeds 10 percent of the funds described in subparagraph (A), to expand the State program funded under section 2602(b) so that the State operates the program on a year-round basis; and (D) in planning and administering that program, the State\u2014 (i) shall make technological changes to allow, not later than 5 years after the date of enactment of the Heating and Cooling Relief Act, for online submission of applications for assistance through that program; and (ii) shall, to the extent practicable\u2014 (I) conduct outreach activities, including activities to increase enrollment as described in subsection (p); (II) ensure that all HEAP coordinators in the State receive wages, for administration funded under section 2602(b), at not less than the greater of $15 per hour or the applicable Federal, State, or local minimum wage rate; (III) conduct training for HEAP coordinators, State agency staff, and community partners on best practices for outreach, application processing, and assisting eligible households; (IV) as needed, conduct outreach relating to the program funded under section 2602(b) to rural electric cooperatives, home energy suppliers owned by a political subdivision of a State, such as a municipally owned electric utility, and home energy suppliers owned by any agency, authority, corporation, or instrumentality of a political subdivision of a State; and (V) ensure autoenrollment of eligible households into the program funded under section 2602(b), and in the process document any potential barriers to autoenrollment that need to be clarified or otherwise addressed at the Federal level; ;\n**(2)**\nin subsection (c)(1)\u2014\n**(A)**\nin subparagraph (G), by striking and at the end;\n**(B)**\nby redesignating subparagraph (H) as subparagraph (I); and\n**(C)**\nby inserting after subparagraph (G) the following:\n(H) describes how the State will expand the State program funded under section 2602(b) so that the State operates the program on a year-round basis in accordance with subsection (b)(10)(C) and the measures the State has taken so far to carry out that expansion; and ; and\n**(3)**\nby adding at the end the following:\n(m) The Secretary shall allow, to the greatest extent possible, eligible households to obtain assistance with minimal administrative burden, by carrying out subsection (c)(1)(A)(i). (n) The Secretary shall, by grant or contract, provide for a study that examines the rates of home energy shutoffs and assessments of late fees among eligible households, relative to those rates for households that are not eligible households, over a period of several years. (o) The Secretary shall provide technical assistance to States to support partnerships described in subsection (b)(8)(H). (p) (1) The Secretary, in consultation with the Secretary of Education, shall issue guidance for use of funds for administrative activities described in subsection (b)(10) to increase, through partnerships with elementary schools, secondary schools, and local educational agencies, enrollment in the program funded under section 2602(b) among eligible households that include children and that have high energy burdens. (2) The Secretary shall issue guidance for use by States on outreach relating to assistance through the program funded under section 2602(b) to high-risk individuals, with relevant medical conditions, that benefit from the use of medical equipment that requires electricity, including a ventilator, an oxygen concentrator, or another medical device that requires electricity. (3) The Secretary shall issue guidance for use by States on how to ensure that eligible households are aware of additional grants, tax credits, and rebates, made available under Public Law 117\u2013169 , or an amendment made by such law. (q) Not later than 1 year after the date of enactment of the Heating and Cooling Relief Act, the Secretary shall require each State receiving funds under this title, including allotments under subsection (a) or (e) of section 2604, to develop and update as necessary, an action plan for a period of extreme heat, which shall describe how the State will use its allotments under this title to assist eligible households in covering cooling costs and mitigating heat-related health risks. (r) Not later than 1 year after the date of enactment of the Heating and Cooling Relief Act , the Secretary shall conduct a review of eligibility criteria for assistance under this title and identify additional vulnerable populations to include under such criteria, such as pregnant women and individuals with medical conditions exacerbated by a period of extreme heat. (s) The Secretary, in consultation with the Secretary of Energy, shall require State energy offices receiving Federal funds under this title to develop plans\u2014 (1) to retrofit low-income housing stock to adapt to rising temperatures and address environmental hazards, including\u2014 (A) deploying highly efficient cooling systems, including heat pumps; (B) expanding weatherization and passive cooling strategies; (C) addressing structural and health hazards, including mold, lead, asbestos, and pest infections; and (D) ensuring that necessary electrical panel and wiring upgrades are completed to support the installation of cooling systems and energy efficiency improvements; and (2) to assess and adapt existing (as of the date of development of the plan) shutoff policies to protect all households while considering the impact on energy affordability and energy grid reliability. (t) (1) Not later than 1 year after the date of enactment of the Heating and Cooling Relief Act , the Secretary, in consultation with the Secretary of Housing and Urban Development, shall submit a report to Congress that\u2014 (A) identifies safe residential temperature standards for federally assisted dwelling units, considering risks of periods of extreme heat and extreme cold and regional climate variations; and (B) proposes strategies to ensure compliance with the standards, including permitting covered utility allowances to be used for cooling assistance where feasible, taking into account regional climate variations and housing stock differences. (2) In this subsection, the term covered utility allowance means a utility allowance\u2014 (A) applicable to public housing dwelling units under section 3 of the United States Housing Act of 1937 ( 42 U.S.C. 1437a ); or (B) under the housing choice voucher program under section 8(o)(2)(D) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(2)(D) ). .\n#### 8. Weatherization\nSection 2605(k) of the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8624(k) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking 15 percent and inserting 25 percent ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A), in the matter preceding clause (i)\u2014\n**(i)**\nby striking subparagraph (B) and inserting subparagraph (C) ; and\n**(ii)**\nby striking the greater of 25 percent and inserting a portion equal to the greater of 35 percent ;\n**(B)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(C)**\nby inserting after subparagraph (A) the following:\n(B) The State\u2014 (i) shall, to the extent practicable\u2014 (I) use the portion described in subparagraph (A) for energy-related home repair that reduces dependence on fossil fuel energy sources; and (II) use the portion to facilitate the use of funds made available under section 2602(b) to increase the participation of eligible households in community solar programs, or to otherwise increase access to and ownership of distributed renewable energy infrastructure among eligible households; and (ii) shall if possible give the highest priority to using the portion for home repair that replaces appliances that rely on fossil fuels with appliances that use electric heating or cooling technology, powered by renewable energy. .\n#### 9. Home energy payment arrears data collection\nSection 2605 of the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8624 ), as amended by section 7, is further amended by adding at the end the following:\n(u) (1) (A) The Secretary, in consultation with the Secretary of Energy, shall develop a standardized template for States and home energy suppliers to use to track and report data on eligible households in arrears in home energy payments, including data on the related fees and disconnections for such households. (B) The template developed under subparagraph (A) shall\u2014 (i) include a definition of an eligible household in arrears, with respect to home energy payments, as an eligible household that has not made payment on a home energy bill for more than 60 to 90 days, as determined by the State agency or local coordinating agency, unless otherwise specified by State law; (ii) include metrics on related disconnections, late fees, reconnections, and arrearage balances for eligible households; and (iii) align with existing (as of the date of the development) Federal and State reporting mechanisms where applicable. (2) Not later than 1 year after the date of enactment of the Heating and Cooling Relief Act, the Secretary shall, in consultation with the Secretary of Energy, issue guidance on best practices for States (including through partnerships with home energy suppliers) to pay for home energy payment arrearages with assistance provided through the program funded under section 2602(b), including by paying for such arrearages at the time of dissemination of assistance through that program. Such guidance shall prohibit any home energy supplier receiving funds through the program from recovering arrearage assistance costs through rate increases or other charges to customers, including cost recovery mechanisms that disproportionately impact low-income households. (3) To the extent practicable, the Secretary and the Secretary of Energy shall jointly\u2014 (A) implement a data tracking system, aligned with the standardized reporting template developed under paragraph (1), to collect aggregate data regarding the number of eligible households in arrears and their respective energy burdens and develop recommendations to HEAP coordinators on how to minimize energy burdens for the households; and (B) issue guidance to home energy suppliers with recommendations for working with State agencies to address home energy payment arrearages of eligible households. (4) The Secretary, in consultation with the Secretary of Energy, may make grants to States to assist the States in implementing data tracking and reporting requirements under this subsection. (5) There are authorized to be appropriated to carry out this subsection such sums as may be necessary. .\n#### 10. Program name change\n##### (a) LIHEAP\nThe Low-Income Home Energy Assistance Act of 1981 is amended\u2014\n**(1)**\nin section 2607A(b) ( 42 U.S.C. 8626a(b) ), in the matter preceding paragraph (1), by striking low-income the first place it appears; and\n**(2)**\nin section 2607B(e)(2)(B)(ii) ( 42 U.S.C. 8626b(e)(2)(B)(ii) ), by striking Low-Income .\n##### (b) Other law\nA reference in any other Federal law (other than that Act), Executive order, rule, regulation, or delegation of authority, or any document, of or relating to the Low-Income Home Energy Assistance Program, shall be deemed to refer to the Home Energy Assistance Program.\n#### 11. Just transition grants\nThe Low-Income Home Energy Assistance Act of 1981 is amended by inserting after section 2607B ( 42 U.S.C. 8626b ) the following:\n2607C. HEAP just transition grants (a) Grant program The Secretary and the Secretary of Energy shall jointly carry out a grant program under this section. In carrying out the program, the Secretaries shall make grants for a period of 3 years to States and local governments to support the development and implementation of interagency plans to reduce energy burdens for eligible households with high home energy use. The plans shall promote the reduction of those burdens in a manner that supports a just transition away from fossil fuel energy and protects eligible households from the threats of climate change. The Secretaries shall make the grants for a period of 3 years. (b) Preferences In making the grants, the Secretary shall give a preference to States, and local governments, who set up coordination systems\u2014 (1) to identify eligible households, that are recipients of assistance through the program funded under section 2602(b), with high home energy use; (2) to prioritize eligible households with the highest energy burdens and lowest incomes, in alignment with the priority provisions in paragraphs (2) and (3) of section 2605(b), to receive emergency repair, weatherization, and retrofit assistance that results in decarbonization and reductions in energy use; and (3) to partner with entities carrying out workforce development initiatives, unions, or minority or women-owned business enterprises to provide emergency repairs, weatherization, and retrofit assistance. (c) Report to Congress At the conclusion of the 3-year grant period, the Secretaries shall\u2014 (1) conduct an evaluation of the program\u2019s outcomes; and (2) prepare and submit to Congress a report containing the results of the evaluation and policy recommendations. .\n#### 12. Conforming amendments\nThe Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8621 et seq. ) is amended\u2014\n**(1)**\nin section 2607B(e)(2)(K) ( 42 U.S.C. 8626b(e)(2)(K) ) by striking paragraphs (2), (3), (4), (5), (7), (9), (10), (11), (12), (13), and (14) of section 2605(b) and inserting paragraphs (2), (4), (5), (6), (8), (10), (11), (12), (13), (14), and (15) of section 2605(b) ; and\n**(2)**\nin section 2610(b)(1) ( 42 U.S.C. 8629 ) by striking clauses (2), (5), (8), and (15) of section 2605(b) and inserting paragraphs (2), (6), (9), and (16) of section 2605(b) .",
      "versionDate": "2025-03-31",
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
        "actionDate": "2025-03-31",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1214",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Heating and Cooling Relief Act",
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
        "name": "Energy",
        "updateDate": "2025-04-07T13:10:17Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2486ih.xml"
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
      "title": "Heating and Cooling Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Heating and Cooling Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Low-Income Home Energy Assistance Act of 1981 to increase the availability of heating and cooling assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:16Z"
    }
  ]
}
```
