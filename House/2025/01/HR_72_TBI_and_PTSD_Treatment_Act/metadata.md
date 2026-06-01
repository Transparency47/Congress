# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/72?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/72
- Title: TBI and PTSD Treatment Act
- Congress: 119
- Bill type: HR
- Bill number: 72
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-12T20:34:38Z
- Update date including text: 2025-02-12T20:34:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-06 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-06 - Committee: Referred to the Subcommittee on Health.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/72",
    "number": "72",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "TBI and PTSD Treatment Act",
    "type": "HR",
    "updateDate": "2025-02-12T20:34:38Z",
    "updateDateIncludingText": "2025-02-12T20:34:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-06T17:43:06Z",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr72ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 72\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself, Mr. Crane , and Mr. Gosar ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to furnish hyperbaric oxygen therapy to veterans with traumatic brain injury or post-traumatic stress disorder.\n#### 1. Short title\nThis Act may be cited as the TBI and PTSD Treatment Act .\n#### 2. Hyperbaric oxygen therapy for veterans with traumatic brain injury or post-traumatic stress disorder\n##### (a) In general\nChapter 17 of title 38, United States Code, is amended by inserting after section 1710E the following new section:\n1710F. Traumatic brain injury and post-traumatic stress disorder: hyperbaric oxygen therapy (a) Authority The Secretary shall furnish hyperbaric oxygen therapy to a veteran who has a condition specified in subsection (b) through a health care provider described in section 1703(c)(5) of this title. (b) Covered conditions The conditions specified in this subsection are the following: (1) Traumatic brain injury. (2) Post-traumatic stress disorder. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1710E the following new item:\n1710F. Traumatic brain injury and post-traumatic stress disorder: hyperbaric oxygen therapy. .",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-12T15:40:37Z"
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
          "measure-id": "id119hr72",
          "measure-number": "72",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr72v00",
            "update-date": "2025-02-12"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>TBI and PTSD Treatment Act</b></p> <p>This bill requires the Department of Veterans Affairs to furnish hyperbaric oxygen therapy through a provider authorized by the Veterans Community Care Program to veterans who have a traumatic brain injury or post-traumatic stress disorder.</p>"
        },
        "title": "TBI and PTSD Treatment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr72.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>TBI and PTSD Treatment Act</b></p> <p>This bill requires the Department of Veterans Affairs to furnish hyperbaric oxygen therapy through a provider authorized by the Veterans Community Care Program to veterans who have a traumatic brain injury or post-traumatic stress disorder.</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr72"
    },
    "title": "TBI and PTSD Treatment Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>TBI and PTSD Treatment Act</b></p> <p>This bill requires the Department of Veterans Affairs to furnish hyperbaric oxygen therapy through a provider authorized by the Veterans Community Care Program to veterans who have a traumatic brain injury or post-traumatic stress disorder.</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr72"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr72ih.xml"
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
      "title": "TBI and PTSD Treatment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TBI and PTSD Treatment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to furnish hyperbaric oxygen therapy to veterans with traumatic brain injury or post-traumatic stress disorder.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T06:49:43Z"
    }
  ]
}
```
