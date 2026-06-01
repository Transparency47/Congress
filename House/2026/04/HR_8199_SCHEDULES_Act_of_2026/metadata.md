# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8199?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8199
- Title: SCHEDULES Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8199
- Origin chamber: House
- Introduced date: 2026-04-06
- Update date: 2026-05-23T08:07:31Z
- Update date including text: 2026-05-23T08:07:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-04-06: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-04-27 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- Latest action: 2026-04-06: Introduced in House

## Actions

- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-04-27 - Committee: Referred to the Subcommittee on Oversight and Investigations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-06",
    "latestAction": {
      "actionDate": "2026-04-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8199",
    "number": "8199",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000472",
        "district": "18",
        "firstName": "Scott",
        "fullName": "Rep. Franklin, Scott [R-FL-18]",
        "lastName": "Franklin",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "SCHEDULES Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:31Z",
    "updateDateIncludingText": "2026-05-23T08:07:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-27",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-06",
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
      "actionDate": "2026-04-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-06",
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
          "date": "2026-04-06T14:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-04-27T13:10:59Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "CA"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "FL"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "GU"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "FL"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "KY"
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
      "sponsorshipDate": "2026-04-15",
      "state": "FL"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8199ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8199\nIN THE HOUSE OF REPRESENTATIVES\nApril 6, 2026 Mr. Scott Franklin of Florida (for himself, Mr. Panetta , Mr. Patronis , and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to establish a comprehensive standard for timing between referrals and appointments for care from the Department of Veterans Affairs and to submit a report with respect to that standard, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Scheduling for Community Health and Easy Data to Understand for Legislators to Evaluate Services Act of 2026 or the SCHEDULES Act of 2026 .\n#### 2. Establishment of comprehensive standard for timing between referral and appointment for care from Department of Veterans Affairs\n##### (a) Establishment of standard\n**(1) In general**\nThe Secretary of Veterans Affairs shall establish a comprehensive standard for timing between the date on which a referral for care for a veteran under the laws administered by the Secretary is entered into the care coordination system of the Department of Veterans Affairs and the date on which an appointment for care for the veteran occurs, whether at a facility of the Department or through care in the community.\n**(2) Modification**\nThe Secretary may modify the standard established under paragraph (1) as the appointment scheduling processes of the Department for care at a facility of the Department or through care in the community are updated.\n**(3) Publication**\nNot later than 30 days before establishing under paragraph (1) or modifying under paragraph (2) the comprehensive standard required under this subsection, the Secretary shall publish such standard in the Federal Register and on a publicly available internet website of the Department.\n##### (b) Report\n**(1) In general**\nNot less frequently than quarterly, the Secretary shall submit to Congress a report on the number and percentage of referrals from the Department to facilities of the Department or providers in the community that meet the standard under subsection (a).\n**(2) Elements**\nEach report submitted under paragraph (1) shall include the following:\n**(A)**\nThe number and percentage of total referrals from each facility of the Department that meet, for the quarter covered by the report\u2014\n**(i)**\nthe standard under subsection (a);\n**(ii)**\nwith respect to referrals to a facility of the Department, the three-business-day standard for scheduling an appointment at a facility of the Department; and\n**(iii)**\nwith respect to referrals for care in the community, the seven-calendar-day standard for scheduling an appointment for care in the community.\n**(B)**\nThe number and percentage of referrals from each facility of the Department that meet each of the standards specified in subparagraph (A), disaggregated by each of the five, or more, most in-demand categories of care provided at such facility (such as mental health, cardiology, neurology, oncology, etc.).\n**(C)**\nA list of all medical centers of the Department ranked from best to worst in meeting the standard under subsection (a), including a disaggregated list by State.\n**(3) Annually included information**\nNot less frequently than annually, the Secretary shall include in the report required under paragraph (1)\u2014\n**(A)**\naggregated data for the four-quarter period preceding the date of the report; and\n**(B)**\na description of steps taken by the Department to improve the timeliness of the provision of care by the Department and an estimate of when the Department will be fully compliant with the standard under subsection (a).\n**(4) Public availability**\nThe Secretary shall make each report required under paragraph (1) publicly available on a website of the Veterans Health Administration.",
      "versionDate": "2026-04-06",
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
        "actionDate": "2026-03-26",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "4229",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SCHEDULES Act of 2026",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-21T01:27:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-06",
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
          "measure-id": "id119hr8199",
          "measure-number": "8199",
          "measure-type": "hr",
          "orig-publish-date": "2026-04-06",
          "originChamber": "HOUSE",
          "update-date": "2026-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr8199v00",
            "update-date": "2026-05-06"
          },
          "action-date": "2026-04-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Scheduling for Community Health and Easy Data to Understand for Legislators to Evaluate Services Act of 2026 or the SCHEDULES Act of 2026</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish a standard for timing between the date on which a referral for VA care is entered into the VA's system and the date on which an appointment for care occurs, whether at a VA facility or through care in the community.</p><p>The VA must publish the standard in the Federal Register and on a publicly accessible VA website. Additionally, the VA must submit a report at least quarterly on the number and percentage of referrals that meet the new timing standard.</p>"
        },
        "title": "SCHEDULES Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr8199.xml",
    "summary": {
      "actionDate": "2026-04-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Scheduling for Community Health and Easy Data to Understand for Legislators to Evaluate Services Act of 2026 or the SCHEDULES Act of 2026</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish a standard for timing between the date on which a referral for VA care is entered into the VA's system and the date on which an appointment for care occurs, whether at a VA facility or through care in the community.</p><p>The VA must publish the standard in the Federal Register and on a publicly accessible VA website. Additionally, the VA must submit a report at least quarterly on the number and percentage of referrals that meet the new timing standard.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr8199"
    },
    "title": "SCHEDULES Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-04-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Scheduling for Community Health and Easy Data to Understand for Legislators to Evaluate Services Act of 2026 or the SCHEDULES Act of 2026</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish a standard for timing between the date on which a referral for VA care is entered into the VA's system and the date on which an appointment for care occurs, whether at a VA facility or through care in the community.</p><p>The VA must publish the standard in the Federal Register and on a publicly accessible VA website. Additionally, the VA must submit a report at least quarterly on the number and percentage of referrals that meet the new timing standard.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr8199"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8199ih.xml"
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
      "title": "SCHEDULES Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SCHEDULES Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Scheduling for Community Health and Easy Data to Understand for Legislators to Evaluate Services Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Veterans Affairs to establish a comprehensive standard for timing between referrals and appointments for care from the Department of Veterans Affairs and to submit a report with respect to that standard, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T05:18:35Z"
    }
  ]
}
```
