# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8193?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8193
- Title: To designate the facility of the United States Postal Service located at 189 East Main Street in Xenia, Ohio, as the "Gilman 'Gil' Whitney Post Office Building".
- Congress: 119
- Bill type: HR
- Bill number: 8193
- Origin chamber: House
- Introduced date: 2026-04-02
- Update date: 2026-05-14T19:20:19Z
- Update date including text: 2026-05-14T19:20:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-04-02: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- Latest action: 2026-04-02: Introduced in House

## Actions

- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-02",
    "latestAction": {
      "actionDate": "2026-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8193",
    "number": "8193",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000463",
        "district": "10",
        "firstName": "Michael",
        "fullName": "Rep. Turner, Michael R. [R-OH-10]",
        "lastName": "Turner",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 189 East Main Street in Xenia, Ohio, as the \"Gilman 'Gil' Whitney Post Office Building\".",
    "type": "HR",
    "updateDate": "2026-05-14T19:20:19Z",
    "updateDateIncludingText": "2026-05-14T19:20:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-02",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-02",
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
        "item": [
          {
            "date": "2026-04-29T13:09:22Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-02T12:31:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "J000289",
      "district": "4",
      "firstName": "Jim",
      "fullName": "Rep. Jordan, Jim [R-OH-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Jordan",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8193ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8193\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2026 Mr. Turner of Ohio (for himself, Mrs. Beatty , Mr. Balderson , Ms. Brown , Mr. Carey , Mr. Davidson , Mr. Jordan , Mr. Joyce of Ohio , Ms. Kaptur , Mr. Landsman , Mr. Latta , Mr. Miller of Ohio , Mr. Rulli , Mrs. Sykes , and Mr. Taylor ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 189 East Main Street in Xenia, Ohio, as the Gilman Gil Whitney Post Office Building .\n#### 1. Gilman Gil Whitney Post Office Building\n##### (a) Designation\nThe facility of the United States Postal Service located at 189 East Main Street in Xenia, Ohio, shall be known and designated as the Gilman Gil Whitney Post Office Building .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Gilman Gil Whitney Post Office Building .",
      "versionDate": "2026-04-02",
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
            "name": "Congressional tributes",
            "updateDate": "2026-05-08T17:22:40Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2026-05-08T17:22:40Z"
          },
          {
            "name": "Ohio",
            "updateDate": "2026-05-08T17:22:44Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2026-05-08T17:22:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-09T16:48:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-02",
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
          "measure-id": "id119hr8193",
          "measure-number": "8193",
          "measure-type": "hr",
          "orig-publish-date": "2026-04-02",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr8193v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2026-04-02",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 189 East Main Street in Xenia, Ohio, as the \"Gilman 'Gil' Whitney Post Office Building\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 189 East Main Street in Xenia, Ohio, as the \"Gilman 'Gil' Whitney Post Office Building\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr8193.xml",
    "summary": {
      "actionDate": "2026-04-02",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 189 East Main Street in Xenia, Ohio, as the \"Gilman 'Gil' Whitney Post Office Building\".",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr8193"
    },
    "title": "To designate the facility of the United States Postal Service located at 189 East Main Street in Xenia, Ohio, as the \"Gilman 'Gil' Whitney Post Office Building\"."
  },
  "summaries": [
    {
      "actionDate": "2026-04-02",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 189 East Main Street in Xenia, Ohio, as the \"Gilman 'Gil' Whitney Post Office Building\".",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr8193"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8193ih.xml"
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
      "title": "To designate the facility of the United States Postal Service located at 189 East Main Street in Xenia, Ohio, as the \"Gilman 'Gil' Whitney Post Office Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:25Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 189 East Main Street in Xenia, Ohio, as the \"Gilman 'Gil' Whitney Post Office Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T08:05:36Z"
    }
  ]
}
```
