# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/553?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/553
- Title: BRAVE Act
- Congress: 119
- Bill type: HR
- Bill number: 553
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-01-31T09:05:25Z
- Update date including text: 2026-01-31T09:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-20 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-20 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/553",
    "number": "553",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000804",
        "district": "1",
        "firstName": "Robert",
        "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
        "lastName": "Wittman",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "BRAVE Act",
    "type": "HR",
    "updateDate": "2026-01-31T09:05:25Z",
    "updateDateIncludingText": "2026-01-31T09:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-20T22:38:56Z",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "HI"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MD"
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
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CO"
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
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
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
      "sponsorshipDate": "2025-12-18",
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
      "sponsorshipDate": "2026-01-30",
      "state": "NJ"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr553ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 553\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Wittman (for himself and Mr. Case ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to establish a patient outreach system relating to mental health care, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Be Ready to Assist Veterans in Extremis Act or the BRAVE Act .\n#### 2. Establishment of Department of Veterans Affairs system for patient outreach relating to mental health care\n##### (a) Establishment of system\nChapter 17 of title 38, United States Code, is amended by inserting after section 1720J the following new section (and conforming the table of sections at the beginning of such chapter accordingly):\n1720K. Mental health care: patient outreach system The Secretary of Veterans Affairs shall establish a patient outreach system under which the Secretary shall ensure that veterans who are enrolled in the system of annual patient enrollment established and operated under section 1705 of this title and have experienced a traumatic or other highly stressful event, may elect to receive from the Secretary information relating to mental health and resources relating to the mental health care services available to the veteran. .\n##### (b) Administration of system\nIn administering the patient outreach system established under section 1720K of title 38, United States Code (as added by subsection (a)), the Secretary of Veterans Affairs shall seek to coordinate such system with the Transition Assistance Program of the Department of Defense.\n##### (c) Deadline for establishment\nThe Secretary shall establish the patient outreach system under such section 1720K by not later than two years after the date of the enactment of this Act.",
      "versionDate": "2025-01-16",
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
            "name": "Health promotion and preventive care",
            "updateDate": "2025-03-13T16:02:08Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-03-13T16:02:02Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-13T16:01:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T15:32:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr553",
          "measure-number": "553",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr553v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Be Ready to Assist Veterans in Extremis Act or the BRAVE Act</strong></p> <p>This bill requires the Department of Veterans Affairs (VA) to establish a patient outreach system under which it must ensure that veterans who are enrolled in the VA health care system and have experienced a traumatic or highly stressful event may elect to receive information and resources relating to mental health and available mental health care services.</p> <p>The VA must coordinate the system with the Transition Assistance Program of the Department of Defense. </p>"
        },
        "title": "BRAVE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr553.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Be Ready to Assist Veterans in Extremis Act or the BRAVE Act</strong></p> <p>This bill requires the Department of Veterans Affairs (VA) to establish a patient outreach system under which it must ensure that veterans who are enrolled in the VA health care system and have experienced a traumatic or highly stressful event may elect to receive information and resources relating to mental health and available mental health care services.</p> <p>The VA must coordinate the system with the Transition Assistance Program of the Department of Defense. </p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr553"
    },
    "title": "BRAVE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Be Ready to Assist Veterans in Extremis Act or the BRAVE Act</strong></p> <p>This bill requires the Department of Veterans Affairs (VA) to establish a patient outreach system under which it must ensure that veterans who are enrolled in the VA health care system and have experienced a traumatic or highly stressful event may elect to receive information and resources relating to mental health and available mental health care services.</p> <p>The VA must coordinate the system with the Transition Assistance Program of the Department of Defense. </p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr553"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr553ih.xml"
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
      "title": "BRAVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T11:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BRAVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Be Ready to Assist Veterans in Extremis Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to establish a patient outreach system relating to mental health care, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T11:03:20Z"
    }
  ]
}
```
