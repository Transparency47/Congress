# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6011?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6011
- Title: VA Work-Study Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 6011
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2026-04-24T08:07:19Z
- Update date including text: 2026-04-24T08:07:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6011",
    "number": "6011",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "VA Work-Study Improvement Act",
    "type": "HR",
    "updateDate": "2026-04-24T08:07:19Z",
    "updateDateIncludingText": "2026-04-24T08:07:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T17:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-17T18:30:26Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
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
      "sponsorshipDate": "2025-11-10",
      "state": "IN"
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
      "sponsorshipDate": "2025-11-10",
      "state": "NY"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "MN"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "TN"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "LA"
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
      "sponsorshipDate": "2025-11-10",
      "state": "PA"
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
      "sponsorshipDate": "2025-11-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "NJ"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "NV"
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
      "sponsorshipDate": "2025-11-10",
      "state": "GA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "IL"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "WA"
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
      "sponsorshipDate": "2025-11-10",
      "state": "VA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "KY"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "NJ"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
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
      "sponsorshipDate": "2025-11-10",
      "state": "DC"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "MD"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
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
      "sponsorshipDate": "2025-11-10",
      "state": "NV"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "NJ"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "GA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MI"
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
      "sponsorshipDate": "2025-11-18",
      "state": "MA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "TX"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
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
      "sponsorshipDate": "2025-12-09",
      "state": "AZ"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6011ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6011\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Mrs. McClain Delaney (for herself, Ms. Budzinski , Mr. Carson , Ms. Clarke of New York , Ms. Craig , Mr. Cohen , Mr. Fields , Mr. Fitzpatrick , Ms. Garcia of Texas , Mr. Gottheimer , Mr. Horsford , Mr. Johnson of Georgia , Mr. Krishnamoorthi , Mr. Larsen of Washington , Ms. McClellan , Mr. McGarvey , Mrs. McIver , Mr. Moulton , Ms. Norton , Mr. Olszewski , Ms. Simon , Ms. Titus , Mrs. Watson Coleman , and Mr. Whitesides ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the VA Work-Study program.\n#### 1. Short title\nThis Act may be cited as the VA Work-Study Improvement Act .\n#### 2. Improvements to VA Work-Study program\n##### (a) Authorized activities\nSubsection (a)(5) of section 3485 of title 38, United States Code, is amended by adding at the end the following new subparagraph:\n(L) Any other activity at an agency of a State or local government or a nonprofit organization that would benefit, directly or indirectly, veterans or members of the Armed Forces. .\n##### (b) Applicable hourly minimum wage\nParagraph (7) of subsection (a) of such section is amended to read as follows:\n(7) In this subsection and subsection (e): (A) The term applicable hourly minimum wages means the higher of the following wages: (i) The minimum rate of basic pay for any Federal employee under the General Schedule or the Federal Wage System pursuant to parts 530 and 532 of title 5, Code of Federal Regulations. (ii) The hourly minimum wage under comparable law of the State in which the services are to be performed. (iii) The hourly minimum wage under comparable law of the local government with jurisdiction over the area in which the services are to be performed. (B) The term rate of basic pay has the meaning given such term in section 8331 of title 5. .\n##### (c) Electronic timesheets\nSuch section is amended by adding at the end the following new subsection:\n(g) The Secretary shall ensure that\u2014 (1) an individual participating in a qualifying work-study activity may electronically record the hours worked under such activity; and (2) the supervisor of such individual may electronically approve such records. .\n##### (d) Publication of data\nSuch section, as amended by subsection (c), is further amended by adding at the end the following new subsection:\n(h) On an annual basis, the Secretary shall publish the following information regarding qualifying work-study activities carried out during the covered year: (1) The number of individuals who participated in a qualifying work-study activity. (2) The demographics of such individuals. (3) A description of such activities. (4) The wages paid to such individuals. (5) The number of hours worked by such individuals. (6) A list of the participating educational institutions. .\n##### (e) Applicability\nThe amendments made by this Act shall apply with respect to a payment of work-study allowance made under section 3485 of title 38, United States Code, on or after January 1, 2028.",
      "versionDate": "2025-11-10",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-18T16:16:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-10",
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
          "measure-id": "id119hr6011",
          "measure-number": "6011",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6011v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-11-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>VA Work-Study Improvement Act</b></p> <p>This bill modifies certain pay and eligibility requirements under the Department of Veterans Affairs (VA) work-study program, including minimum wage and timesheet requirements.</p> <p>The bill expands the list of qualifying work-study activities to include state government, local government, or nonprofit organization activities that would benefit veterans or members of the Armed Forces.</p> <p>The bill also modifies minimum wage requirements under the work-study program. Under the bill, the hourly minimum wage paid under the work-study program must be the higher of (1) the minimum rate of basic pay for any federal employee (under the general schedule or federal wage system pursuant to specified regulations), (2) the hourly minimum wage in the state where the services are to be performed, or (3) the hourly minimum wage of the local government with jurisdiction over the area in which the services are to be performed.</p> <p>Additionally, the VA must ensure that (1) an individual participating in a qualifying work-study activity may electronically record such hours, and (2) the supervisor may electronically approve such records.</p> <p>Finally, the VA must annually publish specified information regarding qualifying work-study activities carried out during the year, including the demographics of individuals participating in the program.</p>"
        },
        "title": "VA Work-Study Improvement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6011.xml",
    "summary": {
      "actionDate": "2025-11-10",
      "actionDesc": "Introduced in House",
      "text": "<p><b>VA Work-Study Improvement Act</b></p> <p>This bill modifies certain pay and eligibility requirements under the Department of Veterans Affairs (VA) work-study program, including minimum wage and timesheet requirements.</p> <p>The bill expands the list of qualifying work-study activities to include state government, local government, or nonprofit organization activities that would benefit veterans or members of the Armed Forces.</p> <p>The bill also modifies minimum wage requirements under the work-study program. Under the bill, the hourly minimum wage paid under the work-study program must be the higher of (1) the minimum rate of basic pay for any federal employee (under the general schedule or federal wage system pursuant to specified regulations), (2) the hourly minimum wage in the state where the services are to be performed, or (3) the hourly minimum wage of the local government with jurisdiction over the area in which the services are to be performed.</p> <p>Additionally, the VA must ensure that (1) an individual participating in a qualifying work-study activity may electronically record such hours, and (2) the supervisor may electronically approve such records.</p> <p>Finally, the VA must annually publish specified information regarding qualifying work-study activities carried out during the year, including the demographics of individuals participating in the program.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr6011"
    },
    "title": "VA Work-Study Improvement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-10",
      "actionDesc": "Introduced in House",
      "text": "<p><b>VA Work-Study Improvement Act</b></p> <p>This bill modifies certain pay and eligibility requirements under the Department of Veterans Affairs (VA) work-study program, including minimum wage and timesheet requirements.</p> <p>The bill expands the list of qualifying work-study activities to include state government, local government, or nonprofit organization activities that would benefit veterans or members of the Armed Forces.</p> <p>The bill also modifies minimum wage requirements under the work-study program. Under the bill, the hourly minimum wage paid under the work-study program must be the higher of (1) the minimum rate of basic pay for any federal employee (under the general schedule or federal wage system pursuant to specified regulations), (2) the hourly minimum wage in the state where the services are to be performed, or (3) the hourly minimum wage of the local government with jurisdiction over the area in which the services are to be performed.</p> <p>Additionally, the VA must ensure that (1) an individual participating in a qualifying work-study activity may electronically record such hours, and (2) the supervisor may electronically approve such records.</p> <p>Finally, the VA must annually publish specified information regarding qualifying work-study activities carried out during the year, including the demographics of individuals participating in the program.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr6011"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6011ih.xml"
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
      "title": "VA Work-Study Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Work-Study Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve the VA Work-Study program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:14Z"
    }
  ]
}
```
