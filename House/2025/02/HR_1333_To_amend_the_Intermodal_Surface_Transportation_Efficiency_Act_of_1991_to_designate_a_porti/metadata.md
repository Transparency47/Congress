# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1333?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1333
- Title: To amend the Intermodal Surface Transportation Efficiency Act of 1991 to designate a portion of United States Route 74 in North Carolina as a future interstate, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 1333
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-03-27T08:07:36Z
- Update date including text: 2025-03-27T08:07:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-13 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-13 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1333",
    "number": "1333",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001236",
        "district": "14",
        "firstName": "Tim",
        "fullName": "Rep. Moore, Tim [R-NC-14]",
        "lastName": "Moore",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "To amend the Intermodal Surface Transportation Efficiency Act of 1991 to designate a portion of United States Route 74 in North Carolina as a future interstate, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-03-27T08:07:36Z",
    "updateDateIncludingText": "2025-03-27T08:07:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:08:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-13T22:19:05Z",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1333ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1333\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Moore of North Carolina (for himself and Mr. Edwards ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Intermodal Surface Transportation Efficiency Act of 1991 to designate a portion of United States Route 74 in North Carolina as a future interstate, and for other purposes.\n#### 1. Designation of future interstate\n##### (a) Designation as high priority corridor\nSection 1105(c) of the Intermodal Surface Transportation Efficiency Act of 1991 ( Public Law 102\u2013240 ) is amended by adding at the end the following:\n(103) United States Route 74 from Columbus, North Carolina to Kings Mountain, North Carolina. .\n##### (b) Designation as future interstate\nSection 1105(e)(5)(A) of the Intermodal Surface Transportation Efficiency Act of 1991 is amended by striking and subsection (c)(102) and inserting subsection (c)(102), and subsection (c)(103) .",
      "versionDate": "2025-02-13",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-14T16:43:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1333",
          "measure-number": "1333",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1333v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill designates U.S. Route 74 from Columbus, North Carolina, to Kings Mountain, North Carolina, as (1) a high priority corridor on the National Highway System, and (2) a future part of the Interstate System.</p>"
        },
        "title": "To amend the Intermodal Surface Transportation Efficiency Act of 1991 to designate a portion of United States Route 74 in North Carolina as a future interstate, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1333.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill designates U.S. Route 74 from Columbus, North Carolina, to Kings Mountain, North Carolina, as (1) a high priority corridor on the National Highway System, and (2) a future part of the Interstate System.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr1333"
    },
    "title": "To amend the Intermodal Surface Transportation Efficiency Act of 1991 to designate a portion of United States Route 74 in North Carolina as a future interstate, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill designates U.S. Route 74 from Columbus, North Carolina, to Kings Mountain, North Carolina, as (1) a high priority corridor on the National Highway System, and (2) a future part of the Interstate System.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr1333"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1333ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Intermodal Surface Transportation Efficiency Act of 1991 to designate a portion of United States Route 74 in North Carolina as a future interstate, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:21:00Z"
    },
    {
      "title": "To amend the Intermodal Surface Transportation Efficiency Act of 1991 to designate a portion of United States Route 74 in North Carolina as a future interstate, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T09:07:02Z"
    }
  ]
}
```
