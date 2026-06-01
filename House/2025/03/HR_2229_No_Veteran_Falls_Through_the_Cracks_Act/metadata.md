# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2229?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2229
- Title: No Veteran Falls Through the Cracks Act
- Congress: 119
- Bill type: HR
- Bill number: 2229
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-06-24T16:25:03Z
- Update date including text: 2025-06-24T16:25:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-04 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-04 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2229",
    "number": "2229",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001213",
        "district": "1",
        "firstName": "Bryan",
        "fullName": "Rep. Steil, Bryan [R-WI-1]",
        "lastName": "Steil",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "No Veteran Falls Through the Cracks Act",
    "type": "HR",
    "updateDate": "2025-06-24T16:25:03Z",
    "updateDateIncludingText": "2025-06-24T16:25:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-04",
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
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:07:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T18:09:12Z",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2229ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2229\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Steil introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to improve the ability of veterans to make appointments for mental health care furnished by the Secretary.\n#### 1. Short title\nThis Act may be cited as the No Veteran Falls Through the Cracks Act .\n#### 2. Improvements to scheduling by veterans of mental health appointments at Department of Veterans Affairs\n##### (a) Rescheduling cancelled appointments\nIf a covered veteran cancels an appointment for mental health care furnished by the Secretary of Veterans Affairs, the Secretary shall seek to reschedule the appointment, regardless of the method by which the veteran cancelled the appointment. In seeking to reschedule such appointment, the Secretary shall contact the veteran by telephone. If the veteran does not reschedule the appointment during the first telephone call, the Secretary shall contact the veteran at least once more by telephone to reschedule the appointment.\n##### (b) Covered veteran defined\nIn this section, the term covered veteran means a veteran who is enrolled in the system of patient enrollment established under section 1705(a) of title 38, United States Code.",
      "versionDate": "2025-03-18",
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
        "updateDate": "2025-05-12T15:29:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-18",
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
          "measure-id": "id119hr2229",
          "measure-number": "2229",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-18",
          "originChamber": "HOUSE",
          "update-date": "2025-06-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2229v00",
            "update-date": "2025-06-24"
          },
          "action-date": "2025-03-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Veteran Falls Through the Cracks Act</strong></p> <p>This bill requires the Department of Veterans Affairs to attempt to reschedule a veteran's mental health care appointment if the veteran has canceled such an appointment.<br/> </p>"
        },
        "title": "No Veteran Falls Through the Cracks Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2229.xml",
    "summary": {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Veteran Falls Through the Cracks Act</strong></p> <p>This bill requires the Department of Veterans Affairs to attempt to reschedule a veteran's mental health care appointment if the veteran has canceled such an appointment.<br/> </p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119hr2229"
    },
    "title": "No Veteran Falls Through the Cracks Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Veteran Falls Through the Cracks Act</strong></p> <p>This bill requires the Department of Veterans Affairs to attempt to reschedule a veteran's mental health care appointment if the veteran has canceled such an appointment.<br/> </p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119hr2229"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2229ih.xml"
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
      "title": "No Veteran Falls Through the Cracks Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T12:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Veteran Falls Through the Cracks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T12:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to improve the ability of veterans to make appointments for mental health care furnished by the Secretary.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T12:03:23Z"
    }
  ]
}
```
