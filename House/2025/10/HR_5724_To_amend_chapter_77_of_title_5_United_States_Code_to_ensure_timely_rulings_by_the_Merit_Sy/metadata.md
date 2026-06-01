# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5724?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5724
- Title: FAST Justice Act
- Congress: 119
- Bill type: HR
- Bill number: 5724
- Origin chamber: House
- Introduced date: 2025-10-08
- Update date: 2026-04-24T08:06:59Z
- Update date including text: 2026-04-24T08:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-08: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-08 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-08: Introduced in House

## Actions

- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-08 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-08",
    "latestAction": {
      "actionDate": "2025-10-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5724",
    "number": "5724",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000831",
        "district": "11",
        "firstName": "James",
        "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
        "lastName": "Walkinshaw",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "FAST Justice Act",
    "type": "HR",
    "updateDate": "2026-04-24T08:06:59Z",
    "updateDateIncludingText": "2026-04-24T08:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-08",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-08",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-08",
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
          "date": "2025-10-08T19:01:45Z",
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
          "date": "2025-10-08T19:01:40Z",
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
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MA"
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
      "sponsorshipDate": "2025-10-08",
      "state": "DC"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
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
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MD"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MI"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MD"
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
      "sponsorshipDate": "2025-10-08",
      "state": "GA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "OH"
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
      "sponsorshipDate": "2025-10-08",
      "state": "NM"
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
      "sponsorshipDate": "2025-10-08",
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
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
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
      "sponsorshipDate": "2025-10-08",
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
      "sponsorshipDate": "2025-10-08",
      "state": "NV"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NV"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NJ"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5724ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5724\nIN THE HOUSE OF REPRESENTATIVES\nOctober 8, 2025 Mr. Walkinshaw (for himself, Mr. Lynch , Ms. Norton , Mrs. Cherfilus-McCormick , Mr. Vindman , Mr. Subramanyam , Ms. McClellan , Ms. Elfreth , Mr. Thanedar , Mr. Hoyer , Mr. Johnson of Georgia , Mr. Landsman , Ms. Stansbury , Mr. Kennedy of New York , Ms. Wasserman Schultz , Ms. Stevens , and Ms. Titus ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend chapter 77 of title 5, United States Code, to ensure timely rulings by the Merit Systems Protection Board on appeals by Federal employees and applicants for employment.\n#### 1. Short title\nThis Act may be cited as the Fair Access to Swift and Timely Justice Act or the FAST Justice Act .\n#### 2. Timeliness of MSPB appeals\n##### (a) In general\nSection 7701 of title 5, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (k) as subsection (l); and\n**(2)**\nby inserting after subsection (j) the following:\n(k) Untimely action by MSPB (1) In general On and after the date that is 120 days after the date on which an employee or applicant for employment files an appeal under this section, other than an appeal of a case that is subject to section 7702, if the Merit Systems Protection Board has not taken an action with respect to the appeal that is subject to judicial review, the employee or applicant shall be entitled to file a civil action with respect to the personnel action that is the subject of the appeal. (2) Filing (A) In general An employee or applicant may bring a civil action under paragraph (1) in a district court of the United States for\u2014 (i) any judicial district in which a personnel action that is a subject of the civil action is alleged to have occurred; or (ii) the judicial district in which the employee or applicant would have been employed, but for a personnel action that is a subject of the civil action. (B) Where principal office is located If the respondent for a civil action under paragraph (1) is not subject to personal jurisdiction in any judicial district described in subparagraph (A), the civil action may be brought in a district court of the United States for the judicial district in which the principal office of the respondent is located. (3) Standards for judicial review In a civil action under paragraph (1), the court\u2014 (A) shall apply the standard of review under section 7703(c) only with respect to an order or decision of the Merit Systems Protection Board; and (B) in making any other determination, shall apply the same standard of review that would have applied to the review of the personnel action at issue by the Merit Systems Protection Board. (4) Appeal of district court determination An appeal from an order or decision of the district court in a civil action under paragraph (1) shall, in accordance with section 1291 of title 28, be filed with the court of appeals of the United States for the judicial district in which the district court is located. (5) Stay If an employee or applicant for employment brings a civil action in accordance with paragraph (1) with respect to a personnel action, the Merit Systems Protection Board\u2014 (A) shall stay the appeal relating to the personnel action upon the filing of the civil action; and (B) if the civil action is dismissed for lack of jurisdiction, shall resume processing the appeal. .\n##### (b) Rule of construction\nNothing in the amendments made by subsection (a) shall be construed to limit the ability of an employee or applicant for employment to obtain judicial review of an order or decision of the Merit Systems Protection Board in accordance with section 7703 of title 5, United States Code.",
      "versionDate": "2025-10-08",
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
        "actionDate": "2025-10-07",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2977",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FAST Justice Act",
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
        "updateDate": "2025-12-08T21:50:08Z"
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
      "date": "2025-10-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5724ih.xml"
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
      "title": "FAST Justice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-21T11:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAST Justice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Access to Swift and Timely Justice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 77 of title 5, United States Code, to ensure timely rulings by the Merit Systems Protection Board on appeals by Federal employees and applicants for employment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-21T11:18:13Z"
    }
  ]
}
```
