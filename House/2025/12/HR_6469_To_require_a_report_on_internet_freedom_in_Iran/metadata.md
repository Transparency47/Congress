# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6469?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6469
- Title: FREEDOM Act
- Congress: 119
- Bill type: HR
- Bill number: 6469
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-03-17T08:05:45Z
- Update date including text: 2026-04-09T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6469",
    "number": "6469",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001241",
        "district": "47",
        "firstName": "Dave",
        "fullName": "Rep. Min, Dave [D-CA-47]",
        "lastName": "Min",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "FREEDOM Act",
    "type": "HR",
    "updateDate": "2026-03-17T08:05:45Z",
    "updateDateIncludingText": "2026-04-09T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "NY"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "AZ"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
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
      "sponsorshipDate": "2025-12-04",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-04",
      "state": "PA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "VA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "FL"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "VA"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "VA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "FL"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "TX"
    },
    {
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "NC"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "IN"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "TN"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "FL"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "IL"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "OK"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "IN"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "MI"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NJ"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "NY"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6469ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6469\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Min (for himself, Ms. Tenney , Ms. Ansari , Ms. Salazar , Mr. Goldman of New York , Mr. Fitzpatrick , Mr. Subramanyam , Mr. Bilirakis , Mr. Walkinshaw , Mr. Wittman , Mr. Swalwell , Mr. Mills , and Mr. Sherman ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require a report on internet freedom in Iran.\n#### 1. Short title\nThis Act may be cited as the Feasibility Review of Emerging Equipment for Digital Open Media Act or the FREEDOM Act .\n#### 2. Report on internet freedom in Iran\n##### (a) In general\nNot later than 120 days after the date of the enactment of the Act, the Secretary of State, in consultation with the Federal Communications Commission and the Department of the Treasury, shall prepare and submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate a report that updates and supplements the report required under section 5124 of the National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ).\n##### (b) Additional matters To be included\nUpdates to the strategy required in section 5124 of the National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ), shall also include the following:\n**(1)**\nAn assessment of the feasibility of using direct-to-cell wireless communications technologies to expand internet access for the people of Iran, including technical, regulatory, and security considerations.\n**(2)**\nAn analysis of how drone-based platforms, signal jamming technologies, and related countermeasures could impact the feasibility, security, economics, and resilience of such direct-to-cell wireless communications.\n**(3)**\nA survey of terrestrial and non-terrestrial telecommunications service providers currently active in Iran, including\u2014\n**(A)**\nwhether such providers are state-owned or state-controlled;\n**(B)**\nthe extent of foreign participation or investment in such providers; and\n**(C)**\nthe implications of such ownership and control for communications freedom and censorship.\n**(4)**\nAny other relevant information to assess the opportunities and risks associated with terrestrial and non-terrestrial communications technologies in Iran.\n##### (c) Form\nThe report required by subsection (a) shall be submitted in unclassified form, but may include a classified annex.",
      "versionDate": "2025-12-04",
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
        "actionDate": "2026-02-10",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 328."
      },
      "number": "3360",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FREEDOM Act",
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
        "name": "International Affairs",
        "updateDate": "2026-01-08T16:41:51Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6469ih.xml"
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
      "title": "FREEDOM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FREEDOM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Feasibility Review of Emerging Equipment for Digital Open Media Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a report on internet freedom in Iran.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:20Z"
    }
  ]
}
```
