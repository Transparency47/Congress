# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4972?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4972
- Title: Create Accountable Respectful Environments (CARE) for Children Act
- Congress: 119
- Bill type: HR
- Bill number: 4972
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2026-05-14T08:08:27Z
- Update date including text: 2026-05-14T08:08:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-08-15: Introduced in House

## Actions

- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4972",
    "number": "4972",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Create Accountable Respectful Environments (CARE) for Children Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:27Z",
    "updateDateIncludingText": "2026-05-14T08:08:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-15",
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
          "date": "2025-08-15T16:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "MS"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "MS"
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
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NC"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "FL"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "FL"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "FL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "FL"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "FL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "MS"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "TN"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "TX"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "GA"
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
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4972ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4972\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Mr. Steube (for himself, Mr. Dunn of Florida , Mrs. Cammack , Ms. Wasserman Schultz , Mr. Soto , Mr. Gimenez , Mr. Scott Franklin of Florida , Mr. Ezell , Mr. Guest , Mr. Bilirakis , Mr. Rutherford , Mr. Edwards , and Mr. Mills ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend part E of title IV of the Social Security Act to address or assist in resolving the shortage of appropriate foster homes for children, to develop resources to keep sibling groups together, and to provide for a system of checks and balances to ensure a child\u2019s ongoing safety and well-being, by providing for the placement of a foster child in cottage family homes and making a child so placed eligible for foster care maintenance payments.\n#### 1. Short title\nThis Act may be cited as the Create Accountable Respectful Environments (CARE) for Children Act .\n#### 2. Placement of foster children in cottage family homes\n##### (a) State plan requirement\nSection 471(a)(37) of the Social Security Act ( 42 U.S.C. 671(a)(37) ) is amended by inserting or a cottage family home before the comma.\n##### (b) Eligibility of cottage family homes for foster care maintenance payments\nSection 472(a)(2)(C) of such Act ( 42 U.S.C. 672(a)(2)(C) ) is amended by inserting a cottage family home, before with a parent .\n##### (c) Definition of cottage family home\nSection 472(c) of such Act ( 42 U.S.C. 672(c) ) is amended by adding at the end the following:\n(3) Cottage family home (A) In general The term cottage family home means a home\u2014 (i) that is operated by a public or private child care agency licensed or approved by the State in which the home is situated as an agency that meets the standards established for the licensing or approval; (ii) that encourages and supports the child and the family of the child in maintaining a strong connection through regular contact and involvement in a plan of care, except to the extent otherwise directed by a court of law; (iii) that is able to serve as a resource to facilitate sibling groups being placed together where daily contact and interaction strengthens family ties; (iv) that provides children access to activities or items that are age or developmentally-appropriate, including the ability to participate in extracurricular, social, or other home and community activities with the same freedom afforded to their peers who are living at home with their families; (v) that has and implements a trauma-informed approach in the care of children; (vi) that prohibits the use of seclusion or mechanical or chemical restraints and permits only short-term physical restraint if approved in the policies of the agency to prevent injury to self or others, and prohibits any prone physical restraint; (vii) that provides a system for a child to alert a staff member if the child has a concern, feels unfairly denied rights, or is subject to a threat of mistreatment; (viii) that has a continuous quality improvement methodology that regularly solicits information from children concerning their perceptions of the quality of care and opinions about the strengths and weaknesses of the program; (ix) that is in a single-family style residence with no more than 2 children per bedroom unless it is in the best interest of the children; and (x) in which the children are under the care of live-in parents that use the reasonable and prudent parent standard and provide 24-hour substitute care of children placed away from their parents or other caretakers. (B) Preservation of State flexibility The Secretary may not prohibit, limit, or penalize, by regulation or order, or bring an action in any court to challenge, any action or determination of a State or political subdivision of a State to\u2014 (i) treat a cottage family home as a foster family home for purposes of this part; or (ii) treat an entity as a cottage family care home for purposes of this part, as the State deems necessary to serve the best interests of children or families. .\n##### (d) No time limit on foster care maintenance payments for children placed in a cottage family home\nSection 472(k)(2) of such Act ( 42 U.S.C. 672(k)(2) ) is amended by adding at the end the following:\n(E) A cottage family home. .\n##### (e) Effective date\n**(1) In general**\nThe amendments made by this section shall take effect on the date of the enactment of this Act, and shall apply to payments under part E of title IV of the Social Security Act for calendar quarters beginning on or after such date.\n**(2) Delay permitted if State legislation required**\nIf the Secretary of Health and Human Services determines that State legislation (other than legislation appropriating funds) is required in order for a State plan under part E of title IV of the Social Security Act to meet the additional requirements imposed by the amendments made by this section, the plan shall not be regarded as failing to meet any of the additional requirements before the date that is 6 months after the date of the enactment of this Act.",
      "versionDate": "2025-08-15",
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
        "name": "Families",
        "updateDate": "2025-09-19T15:26:23Z"
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
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4972ih.xml"
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
      "title": "Create Accountable Respectful Environments (CARE) for Children Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-19T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Create Accountable Respectful Environments (CARE) for Children Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-19T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend part E of title IV of the Social Security Act to address or assist in resolving the shortage of appropriate foster homes for children, to develop resources to keep sibling groups together, and to provide for a system of checks and balances to ensure a child's ongoing safety and well-being, by providing for the placement of a foster child in cottage family homes and making a child so placed eligible for foster care maintenance payments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-19T04:33:19Z"
    }
  ]
}
```
