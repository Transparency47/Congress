# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2017?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2017
- Title: Pay Our Military Act
- Congress: 119
- Bill type: HR
- Bill number: 2017
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-10-25T08:05:21Z
- Update date including text: 2025-10-25T08:05:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2017",
    "number": "2017",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001223",
        "district": "13",
        "firstName": "Emilia",
        "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
        "lastName": "Sykes",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Pay Our Military Act",
    "type": "HR",
    "updateDate": "2025-10-25T08:05:21Z",
    "updateDateIncludingText": "2025-10-25T08:05:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NE"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "DE"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2017ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2017\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mrs. Sykes (for herself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo ensure continuity of pay and allowances for members of the Armed Forces in the event of a lapse in appropriations.\n#### 1. Short title\nThis Act may be cited as the Pay Our Military Act .\n#### 2. Continuing appropriations for pay and allowances for members of the Armed Forces\n##### (a) In general\nThere are hereby appropriated for fiscal year 2025, out of any money in the Treasury not otherwise appropriated, for any period during which interim or full-year appropriations for fiscal year 2025 are not in effect, such sums as are necessary to provide pay and allowances to\u2014\n**(1)**\nmembers of the Armed Forces, including the reserve components thereof, who perform active service or inactive-duty training during such period;\n**(2)**\ncivilian employees of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard when the Coast Guard is not operating as a service in the Department of the Navy) whom the Secretary concerned determines are providing support to members of the Armed Forces described in paragraph (1); and\n**(3)**\ncontractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard when the Coast Guard is not operating as a service in the Department of the Navy) whom the Secretary concerned determines are providing support to members of the Armed Forces described in paragraph (1).\n##### (b) Termination\nAppropriations and funds made available and authority granted pursuant to this Act shall be available until the first of the following occurs:\n**(1)**\nThe enactment into law of an appropriation (including a continuing appropriation) for any purpose for which amounts are made available in subsection (a).\n**(2)**\nThe enactment into law of the applicable regular or continuing appropriations resolution or other Act without any appropriation for such purpose.\n**(3)**\nJanuary 1, 2026.\n##### (c) Definitions\nIn this section:\n**(1)**\nThe terms active service , Armed Forces , and inactive-duty training have the meanings given such terms in section 101 of title 10, United States Code.\n**(2)**\nThe term reserve components means the components named in section 10101 of title 10, United States Code.\n**(3)**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of Defense with respect to the Department of Defense; and\n**(B)**\nthe Secretary of Homeland Security with respect to matters concerning the Coast Guard when the Coast Guard is not operating as a service in the Department of the Navy.",
      "versionDate": "2025-03-10",
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
        "updateDate": "2025-05-06T15:43:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119hr2017",
          "measure-number": "2017",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2025-07-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2017v00",
            "update-date": "2025-07-07"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Pay Our Military Act</strong></p><p>This bill provides continuing appropriations for military pay for any period during which interim or full-year appropriations for FY2025 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2025 continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service or inactive-duty training during the period; and (2) civilian employees and contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard when the Coast Guard is not operating as a service in the Department of the Navy) who are providing support to such members of the Armed Forces.</p><p>If a government shutdown occurs, the bill provides the continuing appropriations until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) January 1, 2026.\u00a0</p>"
        },
        "title": "Pay Our Military Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2017.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pay Our Military Act</strong></p><p>This bill provides continuing appropriations for military pay for any period during which interim or full-year appropriations for FY2025 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2025 continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service or inactive-duty training during the period; and (2) civilian employees and contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard when the Coast Guard is not operating as a service in the Department of the Navy) who are providing support to such members of the Armed Forces.</p><p>If a government shutdown occurs, the bill provides the continuing appropriations until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) January 1, 2026.\u00a0</p>",
      "updateDate": "2025-07-07",
      "versionCode": "id119hr2017"
    },
    "title": "Pay Our Military Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pay Our Military Act</strong></p><p>This bill provides continuing appropriations for military pay for any period during which interim or full-year appropriations for FY2025 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides FY2025 continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service or inactive-duty training during the period; and (2) civilian employees and contractors of the Department of Defense (and the Department of Homeland Security in the case of the Coast Guard when the Coast Guard is not operating as a service in the Department of the Navy) who are providing support to such members of the Armed Forces.</p><p>If a government shutdown occurs, the bill provides the continuing appropriations until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) January 1, 2026.\u00a0</p>",
      "updateDate": "2025-07-07",
      "versionCode": "id119hr2017"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2017ih.xml"
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
      "title": "Pay Our Military Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pay Our Military Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure continuity of pay and allowances for members of the Armed Forces in the event of a lapse in appropriations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:52Z"
    }
  ]
}
```
