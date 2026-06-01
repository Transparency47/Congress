# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/683?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/683
- Title: Combat Veterans Pre-Enrollment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 683
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-04-10T08:06:02Z
- Update date including text: 2026-04-10T08:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-04 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-04 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/683",
    "number": "683",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Combat Veterans Pre-Enrollment Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T08:06:02Z",
    "updateDateIncludingText": "2026-04-10T08:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-04T22:41:26Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AZ"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "HI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NY"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray, Jr. [D-CA-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NV"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "NJ"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr683ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 683\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mrs. Kim (for herself, Mr. Carbajal , Mr. Ciscomani , Ms. Tokuda , Mr. Lawler , and Mr. Cisneros ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to establish a pilot program to permit certain members of the Armed Forces to pre-enroll in the system of annual patient enrollment established and operated under section 1705 of title 38, United States Code.\n#### 1. Short title\nThis Act may be cited as the Combat Veterans Pre-Enrollment Act of 2025 .\n#### 2. Pilot program for pre-enrollment of certain members of the Armed Forces in system of annual patient enrollment of the Department of Veterans Affairs\n##### (a) In general\nNot later than October 1, 2027, the Secretary of Veterans Affairs shall establish a program to carry out, to the maximum extent practicable, all activities necessary to permit a member of the Armed Forces specified in subsection (b) to elect to enroll in the system of annual patient enrollment established and operated under section 1705 of title 38, United States Code, on the date of the separation of such member from active military, naval, air, or space service.\n##### (b) Member of the Armed Forces specified\nA member of the Armed Forces specified in this subsection is a member of the Armed Forces that the Secretary determines\u2014\n**(1)**\nis performing active military, naval, air, or space service;\n**(2)**\nwould be eligible for enrollment in the system of annual patient enrollment established and operated under such section on the date of the separation of such member from such service; and\n**(3)**\nis described in section 1710(e)(1)(D) of title 38, United States Code.\n##### (c) Pre-Enrollment mechanism\n**(1) In general**\nUnder the program required by subsection (a), the Secretary of Veterans Affairs, in conjunction with the Secretary of Defense and the Secretary of Homeland Security, shall establish a mechanism to permit a member of the Armed Forces specified in subsection (b) to elect to pre-enroll in such system of annual patient enrollment, pursuant to the program required by subsection (a), during the 180-day period that precedes the date of the separation of such member from active military, naval, air, or space service.\n**(2) Briefings on mechanism**\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for the duration of the program required by subsection (a), the Department of Veterans Affairs-Department of Defense Joint Executive Committee established under section 320 of title 38, United States Code, shall submit to the appropriate congressional committees a briefing on efforts of the Secretary of Veterans Affairs and the Secretary of Defense with respect to the implementation of the mechanism required by paragraph (1) during the period covered by the briefing.\n##### (d) Report on pre-Enrolled members\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for the duration of such program, the Secretary shall submit to the appropriate congressional committees a report that includes, with respect to the fiscal year that precedes the period covered by the report\u2014\n**(1)**\nthe number of members of the Armed Forces specified in subsection (b) who\u2014\n**(A)**\nelected to participate in such program and who were subsequently\u2014\n**(i)**\nenrolled in the system of annual patient enrollment established and operated under section 1705 of title 38, United States Code; and\n**(ii)**\ndenied enrollment in such system; and\n**(B)**\nelected not to participate in such program; and\n**(2)**\naggregated demographic information on members of the Armed Forces described in paragraph (1), including\u2014\n**(A)**\nage;\n**(B)**\nethnicity;\n**(C)**\nduration of active military, naval, air, or space service;\n**(D)**\ngrade; and\n**(E)**\nArmed Force.\n##### (e) Termination date\nThe authority of the Secretary to carry out the program required by subsection (a) shall terminate on the date that is three years after the date of the enactment of this Act.\n##### (f) GAO report on program\nNot later than the date that is two years after the date of the termination of such authority, the Comptroller General of the United States shall submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\nan analysis of the effectiveness of the program required by subsection (a) with respect to the enrollment of members of the Armed Forces specified in subsection (b) in the system of annual patient enrollment established and operated under section 1705 of title 38, United States Code; and\n**(2)**\nrecommendations of the Comptroller General, if any, with respect to methods to improve to such program.\n##### (g) Definitions\nIn this section:\n**(1)**\nThe term active military, naval, air, or space service has the meaning given such term in section 101 of title 38, United States Code.\n**(2)**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate; and\n**(B)**\nthe Committees on Armed Services of the House of Representatives and the Senate.",
      "versionDate": "2025-01-23",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-19T16:02:12Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-03-19T16:02:06Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-19T16:01:27Z"
          },
          {
            "name": "Military medicine",
            "updateDate": "2025-03-19T16:01:12Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-03-19T16:01:19Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-03-19T16:02:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-05T19:47:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr683",
          "measure-number": "683",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr683v00",
            "update-date": "2025-03-26"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Combat Veterans Pre-Enrollment Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish a program to carry out all activities necessary to permit certain members of the Armed Forces to elect to enroll in the VA health care system on the date of separation of such members from active service. Specifically, the program is for those who served on active duty in a theater of combat operations during a period of war after the Persian Gulf War or in combat against a hostile force during a period of hostilities after November 11, 1998.</p><p>The VA must, in conjunction with the Department of Defense (DOD) and Department of Homeland Security, establish a mechanism to permit a member of the Armed Forces to elect to pre-enroll in the VA health care system during the 180-day period preceding the date of separation of the member from active service.</p><p>The VA-DOD Joint Executive Committee must brief Congress on the efforts to implement such a mechanism under the program.</p><p>The Government Accountability Office must report on the program and include recommendations with respect to methods to improve the program.</p>"
        },
        "title": "Combat Veterans Pre-Enrollment Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr683.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Combat Veterans Pre-Enrollment Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish a program to carry out all activities necessary to permit certain members of the Armed Forces to elect to enroll in the VA health care system on the date of separation of such members from active service. Specifically, the program is for those who served on active duty in a theater of combat operations during a period of war after the Persian Gulf War or in combat against a hostile force during a period of hostilities after November 11, 1998.</p><p>The VA must, in conjunction with the Department of Defense (DOD) and Department of Homeland Security, establish a mechanism to permit a member of the Armed Forces to elect to pre-enroll in the VA health care system during the 180-day period preceding the date of separation of the member from active service.</p><p>The VA-DOD Joint Executive Committee must brief Congress on the efforts to implement such a mechanism under the program.</p><p>The Government Accountability Office must report on the program and include recommendations with respect to methods to improve the program.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr683"
    },
    "title": "Combat Veterans Pre-Enrollment Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Combat Veterans Pre-Enrollment Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish a program to carry out all activities necessary to permit certain members of the Armed Forces to elect to enroll in the VA health care system on the date of separation of such members from active service. Specifically, the program is for those who served on active duty in a theater of combat operations during a period of war after the Persian Gulf War or in combat against a hostile force during a period of hostilities after November 11, 1998.</p><p>The VA must, in conjunction with the Department of Defense (DOD) and Department of Homeland Security, establish a mechanism to permit a member of the Armed Forces to elect to pre-enroll in the VA health care system during the 180-day period preceding the date of separation of the member from active service.</p><p>The VA-DOD Joint Executive Committee must brief Congress on the efforts to implement such a mechanism under the program.</p><p>The Government Accountability Office must report on the program and include recommendations with respect to methods to improve the program.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr683"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr683ih.xml"
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
      "title": "Combat Veterans Pre-Enrollment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Combat Veterans Pre-Enrollment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to establish a pilot program to permit certain members of the Armed Forces to pre-enroll in the system of annual patient enrollment established and operated under section 1705 of title 38, United States Code.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:29Z"
    }
  ]
}
```
