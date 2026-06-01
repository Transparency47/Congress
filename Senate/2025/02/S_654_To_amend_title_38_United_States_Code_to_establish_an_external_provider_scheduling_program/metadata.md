# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/654?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/654
- Title: A bill to amend title 38, United States Code, to establish an external provider scheduling program to assist the Department of Veterans Affairs in scheduling appointments for care and services under the Veterans Community Care Program, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 654
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-12-03T11:56:36Z
- Update date including text: 2025-12-03T11:56:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-12-02 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.
- 2025-12-02 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.
- 2025-12-02 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 274.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-12-02 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.
- 2025-12-02 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.
- 2025-12-02 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 274.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/654",
    "number": "654",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "A bill to amend title 38, United States Code, to establish an external provider scheduling program to assist the Department of Veterans Affairs in scheduling appointments for care and services under the Veterans Community Care Program, and for other purposes.",
    "type": "S",
    "updateDate": "2025-12-03T11:56:36Z",
    "updateDateIncludingText": "2025-12-03T11:56:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 274.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Veterans' Affairs. Reported by Senator Moran with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
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
            "date": "2025-12-02T19:30:41Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T20:00:08Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-11T14:30:16Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-20T18:15:18Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "NE"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "AR"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s654is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 654\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Moran (for himself, Mrs. Fischer , Mr. Boozman , and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish an external provider scheduling program to assist the Department of Veterans Affairs in scheduling appointments for care and services under the Veterans Community Care Program, and for other purposes.\n#### 1. External provider scheduling program of Department of Veterans Affairs\n##### (a) Establishment\n**(1) In general**\nSubchapter I of chapter 17 of title 38, United States Code, is amended by inserting after section 1703G the following new section:\n1703H. External Provider Scheduling Program (a) In general There is established within the Department a national External Provider Scheduling Program (in this section referred to as the Program ) to assist the Department in scheduling appointments for care and services under the Veterans Community Care Program under section 1703 of this title. (b) Elements of program The Program shall consist of technology that allows schedulers of the Department to view the schedules of health care providers participating in the Veterans Community Care Program under section 1703 of this title and schedule, in real-time, appointments for care and services under such section. (c) Use of contracts The Secretary shall carry out the Program through an existing contract entered into by the Department, if feasible, or a new contract. (d) Reduction in wait times The Secretary shall ensure that the Program\u2014 (1) reduces the time (measured in days) from referral of veterans to health care providers under the Veterans Community Care Program under section 1703 of this title to the actual scheduling of appointments for care or services under such section; and (2) reduces the time (measured in days and hours) for schedulers of the Department to schedule appointments for care or services under such section. (e) Annual report Not later than September 30 of each year through 2028, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the progress of the Secretary in establishing the Program. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 17 of title 38, United States Code, is amended by inserting after the item relating to section 1703G the following new item:\n1703H. External Provider Scheduling Program. .\n##### (b) Availability of program\nThe Secretary of Veterans Affairs shall ensure that the national External Provider Scheduling Program established under section 1703H of title 38, United States Code, as added by subsection (a)(1), is available to all medical centers of the Department of Veterans Affairs by not later than September 30, 2025.\n##### (c) Conforming amendments\nSection 1703 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(2)(A), by inserting , including pursuant to the program under section 1703H of this title, after medical appointments ; and\n**(2)**\nin subsection (h)(2)(B), by inserting , including pursuant to the program under section 1703H of this title before the period at the end.",
      "versionDate": "2025-02-20",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s654rs.xml",
      "text": "II\nCalendar No. 274\n119th CONGRESS\n1st Session\nS. 654\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Moran (for himself, Mrs. Fischer , Mr. Boozman , and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nDecember 2, 2025 Reported by Mr. Moran , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo amend title 38, United States Code, to establish an external provider scheduling program to assist the Department of Veterans Affairs in scheduling appointments for care and services under the Veterans Community Care Program, and for other purposes.\n#### 1. External provider scheduling program of Department of Veterans Affairs\n##### (a) Establishment\n**(1) In general**\nSubchapter I of chapter 17 of title 38, United States Code, is amended by inserting after section 1703G the following new section:\n1703H. External Provider Scheduling Program (a) In general There is established within the Department a national External Provider Scheduling Program (in this section referred to as the Program ) to assist the Department in scheduling appointments for care and services under the Veterans Community Care Program under section 1703 of this title. (b) Elements of program The Program shall consist of technology that allows schedulers of the Department to view the schedules of health care providers participating in the Veterans Community Care Program under section 1703 of this title and schedule, in real-time, appointments for care and services under such section. (c) Use of contracts The Secretary shall carry out the Program through an existing contract entered into by the Department, if feasible, or a new contract. (d) Reduction in wait times The Secretary shall ensure that the Program\u2014 (1) reduces the time (measured in days) from referral of veterans to health care providers under the Veterans Community Care Program under section 1703 of this title to the actual scheduling of appointments for care or services under such section; and (2) reduces the time (measured in days and hours) for schedulers of the Department to schedule appointments for care or services under such section. (e) Annual report Not later than September 30 of each year through 2028, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the progress of the Secretary in establishing the Program. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 17 of title 38, United States Code, is amended by inserting after the item relating to section 1703G the following new item:\n1703H. External Provider Scheduling Program. .\n##### (b) Availability of program\nThe Secretary of Veterans Affairs shall ensure that the national External Provider Scheduling Program established under section 1703H of title 38, United States Code, as added by subsection (a)(1), is available to all medical centers of the Department of Veterans Affairs by not later than September 30, 2025.\n##### (c) Conforming amendments\nSection 1703 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(2)(A), by inserting , including pursuant to the program under section 1703H of this title, after medical appointments ; and\n**(2)**\nin subsection (h)(2)(B), by inserting , including pursuant to the program under section 1703H of this title before the period at the end.",
      "versionDate": "2025-02-20",
      "versionType": "Reported in Senate"
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
            "name": "Computers and information technology",
            "updateDate": "2025-03-21T20:02:17Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-21T20:02:34Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-21T20:02:29Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-03-21T20:01:56Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-03-21T20:02:24Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-21T20:01:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T17:29:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
    "originChamber": "Senate",
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
          "measure-id": "id119s654",
          "measure-number": "654",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2025-05-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s654v00",
            "update-date": "2025-05-09"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill establishes within the Department of Veterans Affairs (VA) a national External Provider Scheduling Program to assist the VA in scheduling appointments for care and services under the Veterans Community Care Program (VCCP). The program must consist of technology that allows VA schedulers to view the schedules of health care providers participating in the VCCP in real time.</p><p>The VA must ensure the program reduces the time (1) from referral to the actual scheduling of appointments for care or services, and (2) for VA schedulers to schedule appointments for care or services.</p><p>The VA must also ensure the program is available to all VA medical centers by September 30, 2025.</p>"
        },
        "title": "A bill to amend title 38, United States Code, to establish an external provider scheduling program to assist the Department of Veterans Affairs in scheduling appointments for care and services under the Veterans Community Care Program, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s654.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill establishes within the Department of Veterans Affairs (VA) a national External Provider Scheduling Program to assist the VA in scheduling appointments for care and services under the Veterans Community Care Program (VCCP). The program must consist of technology that allows VA schedulers to view the schedules of health care providers participating in the VCCP in real time.</p><p>The VA must ensure the program reduces the time (1) from referral to the actual scheduling of appointments for care or services, and (2) for VA schedulers to schedule appointments for care or services.</p><p>The VA must also ensure the program is available to all VA medical centers by September 30, 2025.</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119s654"
    },
    "title": "A bill to amend title 38, United States Code, to establish an external provider scheduling program to assist the Department of Veterans Affairs in scheduling appointments for care and services under the Veterans Community Care Program, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill establishes within the Department of Veterans Affairs (VA) a national External Provider Scheduling Program to assist the VA in scheduling appointments for care and services under the Veterans Community Care Program (VCCP). The program must consist of technology that allows VA schedulers to view the schedules of health care providers participating in the VCCP in real time.</p><p>The VA must ensure the program reduces the time (1) from referral to the actual scheduling of appointments for care or services, and (2) for VA schedulers to schedule appointments for care or services.</p><p>The VA must also ensure the program is available to all VA medical centers by September 30, 2025.</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119s654"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s654is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s654rs.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to establish an external provider scheduling program to assist the Department of Veterans Affairs in scheduling appointments for care and services under the Veterans Community Care Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:36Z"
    },
    {
      "title": "A bill to amend title 38, United States Code, to establish an external provider scheduling program to assist the Department of Veterans Affairs in scheduling appointments for care and services under the Veterans Community Care Program, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T11:56:29Z"
    }
  ]
}
```
