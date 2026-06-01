# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2398?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2398
- Title: Kay Hagan Tick Reauthorization Act
- Congress: 119
- Bill type: S
- Bill number: 2398
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2026-05-20T11:03:28Z
- Update date including text: 2026-05-20T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-07-30 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2025-09-08 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 154.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-07-30 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2025-09-08 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 154.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2398",
    "number": "2398",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001035",
        "district": "",
        "firstName": "Susan",
        "fullName": "Sen. Collins, Susan M. [R-ME]",
        "lastName": "Collins",
        "party": "R",
        "state": "ME"
      }
    ],
    "title": "Kay Hagan Tick Reauthorization Act",
    "type": "S",
    "updateDate": "2026-05-20T11:03:28Z",
    "updateDateIncludingText": "2026-05-20T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 154.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-09-08T21:23:03Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T14:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-23T16:33:09Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MN"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-23",
      "state": "ME"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MN"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MO"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NY"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NH"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "KS"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "NH"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "PA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "WV"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "IN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "VT"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CO"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "PA"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "AR"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "OR"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-07",
      "state": "FL"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-03",
      "state": "NJ"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "RI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NJ"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2398is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2398\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Ms. Collins (for herself, Ms. Smith , Mr. King , Mrs. Gillibrand , Ms. Klobuchar , and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo reauthorize the Kay Hagan Tick Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Kay Hagan Tick Reauthorization Act .\n#### 2. Reauthorization of programs\n##### (a) National strategy and regional centers of excellence in vector-Borne disease\nSection 317U of the Public Health Service Act ( 42 U.S.C. 247b\u201323 ) is amended\u2014\n**(1)**\nin subsection (b), in the matter preceding paragraph (1), by striking the Tick-Borne Disease Working Group established under section 2062 of the 21st Century Cures Act ( 42 U.S.C. 284s ) and other individuals, as appropriate and inserting appropriate individuals ; and\n**(2)**\nin subsection (f), by striking 2021 through 2025 and inserting 2026 through 2030 .\n##### (b) Enhanced support To assist health departments in addressing vector-Borne diseases\nSection 2822(c) of the Public Health Service Act ( 42 U.S.C. 300hh\u201332(c) ) is amended by striking 2021 through 2025 and inserting 2026 through 2030 .",
      "versionDate": "2025-07-23",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2398rs.xml",
      "text": "II\nCalendar No. 154\n119th CONGRESS\n1st Session\nS. 2398\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Ms. Collins (for herself, Ms. Smith , Mr. King , Mrs. Gillibrand , Ms. Klobuchar , Mr. Hawley , Mr. Schumer , Mrs. Shaheen , Mr. Marshall , Ms. Hassan , Mr. McCormick , Mrs. Capito , Mr. Banks , Mr. Welch , Mr. Blumenthal , Mr. Hickenlooper , and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nSeptember 8, 2025 Reported by Mr. Cassidy , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo reauthorize the Kay Hagan Tick Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Kay Hagan Tick Reauthorization Act .\n#### 2. Reauthorization of programs\n##### (a) National strategy and regional centers of excellence in vector-Borne disease\nSection 317U of the Public Health Service Act ( 42 U.S.C. 247b\u201323 ) is amended\u2014\n**(1)**\nin subsection (b), in the matter preceding paragraph (1), by striking the Tick-Borne Disease Working Group established under section 2062 of the 21st Century Cures Act ( 42 U.S.C. 284s ) and other individuals, as appropriate and inserting appropriate individuals ; and\n**(2)**\nin subsection (f), by striking 2021 through 2025 and inserting 2026 through 2030 .\n##### (b) Enhanced support To assist health departments in addressing vector-Borne diseases\nSection 2822(c) of the Public Health Service Act ( 42 U.S.C. 300hh\u201332(c) ) is amended by striking 2021 through 2025 and inserting 2026 through 2030 .",
      "versionDate": "2025-09-08",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-07-15",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S4370-4371)"
      },
      "number": "2294",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Kay Hagan Tick Reauthorization Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-13",
        "text": "Forwarded by Subcommittee to Full Committee by Voice Vote."
      },
      "number": "4348",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To reauthorize the Kay Hagan Tick Act, and for other purposes.",
      "type": "HR"
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
            "name": "Health programs administration and funding",
            "updateDate": "2025-09-16T14:17:04Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-09-16T14:17:10Z"
          },
          {
            "name": "Insects",
            "updateDate": "2025-09-16T14:17:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-05T17:06:26Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2398is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2398rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Kay Hagan Tick Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:28Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Kay Hagan Tick Reauthorization Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-09-10T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Kay Hagan Tick Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T12:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Kay Hagan Tick Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-29T12:33:19Z"
    }
  ]
}
```
