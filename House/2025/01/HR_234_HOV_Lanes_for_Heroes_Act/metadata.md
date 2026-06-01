# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/234?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/234
- Title: HOV Lanes for Heroes Act
- Congress: 119
- Bill type: HR
- Bill number: 234
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-10-18T08:05:42Z
- Update date including text: 2025-10-18T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-08 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-08 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/234",
    "number": "234",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "HOV Lanes for Heroes Act",
    "type": "HR",
    "updateDate": "2025-10-18T08:05:42Z",
    "updateDateIncludingText": "2025-10-18T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-08",
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
      "actionDate": "2025-01-07",
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
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-08T14:34:55Z",
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
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "IN"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MN"
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
      "sponsorshipDate": "2025-10-17",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr234ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 234\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Ms. Malliotakis introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo allow certain veterans to use high occupancy vehicle lanes, including toll lanes.\n#### 1. Short title\nThis Act may be cited as the HOV Lanes for Heroes Act .\n#### 2. HOV facilities\n##### (a) In general\nSection 166(b) of title 23, United States Code, is amended by inserting at the end the following:\n(7) Disabled veterans (A) In general The public authority may allow a disabled veteran to use the HOV facility if such veteran has a license plate that clearly identifies the vehicle, a registered transponder, or other method of identification the public authority considers necessary for qualification. (B) Definition of disabled veteran For purposes of this paragraph, the term disabled veteran means a veteran (as such term is defined in section 101 of title 38) who the Secretary of Veterans Affairs has determined has a service-connected (as such term is defined in such section) disability rated at or above a percentage determined to be qualifying by the public authority. (C) Occupancy exception Notwithstanding the occupancy requirement of subsection (a)(2), 1 occupant described in subparagraph (B) of this paragraph may be permitted to use a HOV facility. (D) No charge for tolls Under this paragraph, a public authority may charge no toll. .\n##### (b) Conforming amendments\nSection 166 of such title is further amended\u2014\n**(1)**\nin subsection (b)(1) by striking through (5) and inserting through (7) ; and\n**(2)**\nin subsection (d)(1) by striking paragraph (4) or (5) and inserting paragraph (4), (5), (6), or (7) .",
      "versionDate": "2025-01-07",
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
            "name": "Commuting",
            "updateDate": "2025-09-10T20:19:30Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-09-10T20:19:30Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-09-10T20:19:30Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2025-09-10T20:19:30Z"
          },
          {
            "name": "Transportation costs",
            "updateDate": "2025-09-10T20:19:30Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-09-10T20:19:30Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-09-10T20:19:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-06T17:36:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr234",
          "measure-number": "234",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr234v00",
            "update-date": "2025-02-10"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>HOV Lanes for Heroes Act</b></p> <p>This bill provides authority for a public authority to allow a disabled veteran to use a high occupancy vehicle (HOV) facility if such veteran has a license plate that clearly identifies the vehicle, a registered transponder, or other method of qualifying identification.</p> <p>The public authority may not charge a toll to the veteran for use of the HOV facility.</p>"
        },
        "title": "HOV Lanes for Heroes Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr234.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><b>HOV Lanes for Heroes Act</b></p> <p>This bill provides authority for a public authority to allow a disabled veteran to use a high occupancy vehicle (HOV) facility if such veteran has a license plate that clearly identifies the vehicle, a registered transponder, or other method of qualifying identification.</p> <p>The public authority may not charge a toll to the veteran for use of the HOV facility.</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr234"
    },
    "title": "HOV Lanes for Heroes Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><b>HOV Lanes for Heroes Act</b></p> <p>This bill provides authority for a public authority to allow a disabled veteran to use a high occupancy vehicle (HOV) facility if such veteran has a license plate that clearly identifies the vehicle, a registered transponder, or other method of qualifying identification.</p> <p>The public authority may not charge a toll to the veteran for use of the HOV facility.</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr234"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr234ih.xml"
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
      "title": "HOV Lanes for Heroes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HOV Lanes for Heroes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow certain veterans to use high occupancy vehicle lanes, including toll lanes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:18:29Z"
    }
  ]
}
```
