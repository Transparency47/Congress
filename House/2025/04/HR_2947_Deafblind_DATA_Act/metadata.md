# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2947?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2947
- Title: Deafblind DATA Act
- Congress: 119
- Bill type: HR
- Bill number: 2947
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2026-05-21T08:08:37Z
- Update date including text: 2026-05-21T08:08:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2947",
    "number": "2947",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001232",
        "district": "6",
        "firstName": "April",
        "fullName": "Rep. McClain Delaney, April [D-MD-6]",
        "lastName": "McClain Delaney",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Deafblind DATA Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:37Z",
    "updateDateIncludingText": "2026-05-21T08:08:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:31:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "FL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
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
      "sponsorshipDate": "2025-04-17",
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
      "sponsorshipDate": "2025-04-17",
      "state": "NC"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
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
      "sponsorshipDate": "2025-04-17",
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
      "sponsorshipDate": "2025-04-17",
      "state": "LA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "NY"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John [D-NY-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "NY"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "KY"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
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
      "sponsorshipDate": "2025-04-17",
      "state": "DC"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "MI"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NJ"
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
      "sponsorshipDate": "2025-05-19",
      "state": "NY"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "FL"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "HI"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "DE"
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
      "sponsorshipDate": "2025-07-22",
      "state": "NY"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "NY"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "KS"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
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
      "sponsorshipDate": "2026-04-16",
      "state": "MO"
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
      "sponsorshipDate": "2026-04-21",
      "state": "VA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "UT"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "VA"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "UT"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2947ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2947\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mrs. McClain Delaney (for herself, Mrs. Cherfilus-McCormick , Mr. Cohen , Ms. Crockett , Mr. Davis of North Carolina , Mr. Doggett , Mr. Fitzpatrick , Mr. Goldman of New York , Mr. Fields , Mr. Lawler , Mr. Mannion , Mr. McGarvey , Mr. Mullin , Ms. Norton , Mr. Takano , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the Bureau of the Census to collect information on deafblind individuals, and for other purposes.\n#### 1. Short title; findings\n##### (a) Short title\nThis Act may be cited as the Deafblind Disabled Americans Table Approximation Act or the Deafblind DATA Act .\n##### (b) Findings\nCongress finds the following:\n**(1)**\nIndividuals who are deafblind experience concomitant hearing and vision loss that may prevent access to information, cause severe communication challenges, and interfere with social and emotional well-being. In children, deafblindness may impact development and educational attainment, while in adults, deafblindness may interfere with employment and other areas. The National Center on Deafblindness estimates 10,000 children and 40,000 adults are deafblind, the National Association of Regulatory Utility Commissioners estimates 70,000\u2013100,000 people are deafblind, and the Helen Keller National Center for Deafblind Youths and Adults estimates 2.47 million Americans have combined hearing and vision loss.\n**(2)**\nIt is difficult to determine the precise number of individuals who experience combined hearing and vision loss, and estimates from various national counts offer radically different estimates.\n**(3)**\nAn accurate, centralized count of all individuals who are deafblind in the United States is necessary to effectively serve the unique needs of this population. Without a comprehensive national picture of this population, individuals who are deafblind may not receive the support necessary to access information, communicate effectively, and better their social and emotional well-being.\n**(4)**\nThe Bureau of the Census currently does not count individuals who experience combined hearing and vision loss. Through the American Community Survey, the Bureau does collect data on those who are deaf or have serious difficulty hearing and those who are blind or have serious difficulty seeing even when wearing glasses . However, this data is not cross referenced to provide information about those who have both limitations.\n**(5)**\nSome people who experience combined hearing and vision loss identify as deafblind or as a part of the deafblind community.\n**(6)**\nBy cross-referencing this existing data to establish a count of all respondents to the American Community Survey who experience concomitant hearing and vision loss, an estimate of the United States deafblind population may be calculated.\n#### 2. Report and publication on deafblind individuals\n##### (a) Report\nNot later than 180 days after the date of the enactment of this Act, the Director of the Bureau of the Census shall submit to Congress a report on the feasibility of publishing the table described in subsection (b) and the feasibility of expanding data collection on individuals who experience combined hearing and vision loss in the American Community Survey (or any successor survey).\n##### (b) Publication of table\n**(1) In general**\nBeginning in 2026 and each year thereafter, the Director of the Bureau of the Census shall publish, on the public website of the Bureau, a table summarizing respondents to the American Community Survey (or any successor survey) who answered Yes in such Survey to being both deaf and blind. The table shall include the following information, sorted by the State in which such respondent resides:\n**(A)**\nThe sex, race, and age of any such respondent.\n**(B)**\nEconomic characteristics of any such respondent, including employment status, educational attainment, earnings, and poverty status.\n**(2) Limitation**\nThe Director shall ensure that no personally identifiable information of any individual is published under paragraph (1).",
      "versionDate": "2025-04-17",
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
        "updateDate": "2025-05-29T14:59:19Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2947ih.xml"
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
      "title": "Deafblind DATA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:14:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deafblind DATA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deafblind Disabled Americans Table Approximation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Bureau of the Census to collect information on deafblind individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:34Z"
    }
  ]
}
```
