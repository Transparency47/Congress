# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/171?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/171
- Title: Make Transportation Authorities Accountable and Transparent Act
- Congress: 119
- Bill type: HR
- Bill number: 171
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-28T21:32:51Z
- Update date including text: 2025-02-28T21:32:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-04 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-04 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/171",
    "number": "171",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Make Transportation Authorities Accountable and Transparent Act",
    "type": "HR",
    "updateDate": "2025-02-28T21:32:51Z",
    "updateDateIncludingText": "2025-02-28T21:32:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-04",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:25:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-04T14:13:59Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-01-03",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr171ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 171\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Ms. Malliotakis (for herself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the inspector general of the Department of Transportation to conduct an audit on the use of Federal funds by certain entities providing public transportation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Make Transportation Authorities Accountable and Transparent Act .\n#### 2. Inspector General audit on public transportation coronavirus relief spending\n##### (a) Inspector general audit\n**(1) Audit required**\nThe inspector general of the Department of Transportation shall conduct an audit of funds provided to each specified transit agency under the applicable laws during the 5 fiscal years ending before the date of enactment of this Act.\n**(2) Contents of audit**\nThe audit conducted under paragraph (1) shall include the amount of funds received under each of the applicable laws and a description of how such funds were spent.\n**(3) Report to Congress**\nNot later than 180 days after the date of enactment of this Act, the inspector general shall submit to Congress a report containing the results of the audit.\n##### (b) Definitions\nIn this Act:\n**(1) Applicable laws**\nThe term applicable laws means the following:\n**(A)**\nChapter 53 of title 49, United States Code.\n**(B)**\nThe Coronavirus Preparedness and Response Supplemental Appropriations Act, 2020.\n**(C)**\nThe Coronavirus Aid, Relief, and Economic Security Act.\n**(D)**\nThe Consolidated Appropriations Act, 2021.\n**(E)**\nThe American Rescue Plan Act of 2021.\n**(2) Public transportation**\nThe term public transportation has the meaning given the term in section 5302 of title 49, United States Code.\n**(3) Specified transit agency**\nThe term specified transit agency means the 5 entities providing public transportation with the most unlinked passenger trips for calendar year 2019, as reported to the National Transit Database, that received Federal funds under any of the applicable laws.",
      "versionDate": "2025-01-03",
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
            "name": "Accounting and auditing",
            "updateDate": "2025-02-24T16:54:30Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-24T16:54:50Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-02-24T16:54:38Z"
          },
          {
            "name": "Public transit",
            "updateDate": "2025-02-24T16:54:44Z"
          },
          {
            "name": "Transportation programs funding",
            "updateDate": "2025-02-24T16:54:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-19T15:50:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr171",
          "measure-number": "171",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr171v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Make Transportation Authorities Accountable and Transparent Act</strong></p><p>This bill directs the Office of Inspector General of the Department of Transportation to conduct an audit of public transportation spending under certain laws (including specified coronavirus relief laws) and report to Congress.</p>"
        },
        "title": "Make Transportation Authorities Accountable and Transparent Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr171.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Make Transportation Authorities Accountable and Transparent Act</strong></p><p>This bill directs the Office of Inspector General of the Department of Transportation to conduct an audit of public transportation spending under certain laws (including specified coronavirus relief laws) and report to Congress.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr171"
    },
    "title": "Make Transportation Authorities Accountable and Transparent Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Make Transportation Authorities Accountable and Transparent Act</strong></p><p>This bill directs the Office of Inspector General of the Department of Transportation to conduct an audit of public transportation spending under certain laws (including specified coronavirus relief laws) and report to Congress.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr171"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr171ih.xml"
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
      "title": "Make Transportation Authorities Accountable and Transparent Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Make Transportation Authorities Accountable and Transparent Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the inspector general of the Department of Transportation to conduct an audit on the use of Federal funds by certain entities providing public transportation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T05:33:19Z"
    }
  ]
}
```
