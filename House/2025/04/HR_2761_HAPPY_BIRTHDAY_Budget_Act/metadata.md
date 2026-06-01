# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2761?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2761
- Title: HAPPY BIRTHDAY Budget Act
- Congress: 119
- Bill type: HR
- Bill number: 2761
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2025-07-03T20:04:14Z
- Update date including text: 2025-07-03T20:04:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2761",
    "number": "2761",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "HAPPY BIRTHDAY Budget Act",
    "type": "HR",
    "updateDate": "2025-07-03T20:04:14Z",
    "updateDateIncludingText": "2025-07-03T20:04:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-09T16:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "NY"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "OR"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NJ"
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
      "sponsorshipDate": "2025-06-09",
      "state": "MS"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "MI"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CO"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "IL"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "CA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "NM"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "PA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2761ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2761\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Cohen introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the use of Federal funds for a military parade in the District of Columbia intended for the personal celebration of President Donald J. Trump, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Halting All Parades for Presidents\u2019 Yearly Birthdays, It Risks Taxpayer Harm, Damages, And Your Budget Act or the HAPPY BIRTHDAY Budget Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMilitary parades are traditionally reserved for national celebrations, commemorations of military service, or significant public occasions, not personal milestones such as birthdays.\n**(2)**\nA military parade previously considered in President Donald J. Trump\u2019s first term was canceled due to cost concerns, including costs to the military of $92 million and public safety costs to the District of Columbia of over $21 million.\n**(3)**\nHeavy military vehicles risk causing damage to District of Columbia roads, which are not designed to support such weight, requiring taxpayer-funded repairs.\n**(4)**\nPresident Trump has conducted mass layoffs and firings in the Federal Government through the so-called \u201cDepartment of Government Efficiency (DOGE)\u201d under the guise of \u201csaving taxpayer money\u201d.\n**(5)**\nThe District of Columbia is often not fully reimbursed for expenses incurred during Federal events, placing an undue financial burden on local agencies and taxpayers.\n**(6)**\nThe Washington City Paper reported that President Trump has expressed interest in holding a military parade in the District of Columbia on June 14, 2025, as a personal birthday celebration.\n**(7)**\nWhile June 14, 2025, is the United States Army\u2019s 250th birthday and Flag Day, it is also President Donald J. Trump\u2019s 79th birthday.\n**(8)**\nThe U.S. Army has never held a military parade to celebrate its own birthday, and the Army\u2019s 250th anniversary celebration has been in the planning stages for several years with no plans for a parade in the District of Columbia.\n**(9)**\nIt is unlikely that President Trump will include an air, sea, or terrestrial extravaganza to celebrate the birthdays of the other military branches, further highlighting the personal nature of the proposed celebration.\n#### 3. Sense of Congress\nIt is the sense of Congress that public funds should be used to support the well-being and security of the American people and not expended on displays of military force for personal glorification.\n#### 4. Prohibition on use of funds for military parade in District of Columbia\nNo Federal funds may be obligated or expended for the planning, execution, security, transportation, or infrastructure support of any military parade in the District of Columbia that is primarily intended to celebrate the birthday, personal milestone, or private interest of any individual, including President Donald J. Trump.\n#### 5. Alternative birthday celebrations\n##### (a) Alternative celebrations\nCongress encourages President Trump to consider alternative birthday celebrations that do not involve armored vehicles or fighter jets, such as cake, golf, or bingo night.\n##### (b) Birthday wishes\nIn recognition of his birthday, Congress extends a sincere Happy Birthday to Donald J. Trump, free of charge, and encourages all Americans who wish to send birthday wishes to the President to do so through the United States Postal Service, the only service expressly authorized in the Constitution of the United States for the transmission of personal correspondence, where neither snow nor rain nor heat nor gloom of night stays these couriers from the swift completion of their appointed rounds.",
      "versionDate": "2025-04-09",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-06-13T18:04:18Z"
          },
          {
            "name": "District of Columbia",
            "updateDate": "2025-06-13T18:04:01Z"
          },
          {
            "name": "Military history",
            "updateDate": "2025-06-13T18:04:13Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-06-13T18:04:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-09T18:09:00Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2761ih.xml"
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
      "title": "HAPPY BIRTHDAY Budget Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T13:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HAPPY BIRTHDAY Budget Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T13:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Halting All Parades for Presidents\u2019 Yearly Birthdays, It Risks Taxpayer Harm, Damages, And Your Budget Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T13:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of Federal funds for a military parade in the District of Columbia intended for the personal celebration of President Donald J. Trump, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T13:33:22Z"
    }
  ]
}
```
