# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2563?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2563
- Title: Aviation Education Remaining Operational Act
- Congress: 119
- Bill type: HR
- Bill number: 2563
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2025-10-01T08:06:04Z
- Update date including text: 2025-10-01T08:06:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-01 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-01 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2563",
    "number": "2563",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000491",
        "district": "3",
        "firstName": "Frank",
        "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
        "lastName": "Lucas",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Aviation Education Remaining Operational Act",
    "type": "HR",
    "updateDate": "2025-10-01T08:06:04Z",
    "updateDateIncludingText": "2025-10-01T08:06:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-01T20:48:08Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
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
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2563ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2563\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Lucas introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo ensure the continuity of air traffic controller training activities of the Federal Aviation Administration in the event of a lapse in appropriation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Aviation Education Remaining Operational Act or the AERO Act .\n#### 2. FAA Academy\n##### (a) Activities\nThe Administrator of the Federal Aviation Administration shall continue any activities and support services required to continue the operation of the Federal Aviation Administration Academy in Oklahoma City, Oklahoma, including air traffic controller training, during a lapse in appropriations to the Federal Aviation Administration that results in a Government shutdown or emergency furlough to ensure the Academy remains open for the duration of such lapse in appropriations to the Federal Aviation Administration.\n##### (b) Employees\nDuring a lapse in appropriations to the Federal Aviation Administration that results in a Government shutdown or emergency furlough, all Administration employees providing services at the Academy and students completing training at the Academy who are employed by the Administration are excepted from furlough.",
      "versionDate": "2025-04-01",
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
        "updateDate": "2025-04-06T14:23:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119hr2563",
          "measure-number": "2563",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-01",
          "originChamber": "HOUSE",
          "update-date": "2025-09-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2563v00",
            "update-date": "2025-09-22"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Aviation Education Remaining Operational Act or the AERO Act</strong></p><p>This bill directs the Federal Aviation Administration (FAA) to continue FAA Academy operations in Oklahoma City, Oklahoma, including air traffic controller training, during a lapse in FAA appropriations that results in a government shutdown or an emergency furlough.</p><p>If such a lapse in FAA appropriations occurs, the bill also exempts from furlough (1) all FAA employees providing services at the academy, and (2) students who are completing training at the academy and are FAA employees. This exemption requires the employees to continue working during a government shutdown.\u00a0</p>"
        },
        "title": "Aviation Education Remaining Operational Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2563.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Aviation Education Remaining Operational Act or the AERO Act</strong></p><p>This bill directs the Federal Aviation Administration (FAA) to continue FAA Academy operations in Oklahoma City, Oklahoma, including air traffic controller training, during a lapse in FAA appropriations that results in a government shutdown or an emergency furlough.</p><p>If such a lapse in FAA appropriations occurs, the bill also exempts from furlough (1) all FAA employees providing services at the academy, and (2) students who are completing training at the academy and are FAA employees. This exemption requires the employees to continue working during a government shutdown.\u00a0</p>",
      "updateDate": "2025-09-22",
      "versionCode": "id119hr2563"
    },
    "title": "Aviation Education Remaining Operational Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Aviation Education Remaining Operational Act or the AERO Act</strong></p><p>This bill directs the Federal Aviation Administration (FAA) to continue FAA Academy operations in Oklahoma City, Oklahoma, including air traffic controller training, during a lapse in FAA appropriations that results in a government shutdown or an emergency furlough.</p><p>If such a lapse in FAA appropriations occurs, the bill also exempts from furlough (1) all FAA employees providing services at the academy, and (2) students who are completing training at the academy and are FAA employees. This exemption requires the employees to continue working during a government shutdown.\u00a0</p>",
      "updateDate": "2025-09-22",
      "versionCode": "id119hr2563"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2563ih.xml"
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
      "title": "Aviation Education Remaining Operational Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Aviation Education Remaining Operational Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure the continuity of air traffic controller training activities of the Federal Aviation Administration in the event of a lapse in appropriation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:23Z"
    }
  ]
}
```
