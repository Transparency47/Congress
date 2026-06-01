# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4756?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4756
- Title: Freights First Act
- Congress: 119
- Bill type: HR
- Bill number: 4756
- Origin chamber: House
- Introduced date: 2025-07-25
- Update date: 2025-10-07T08:05:43Z
- Update date including text: 2025-10-07T08:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-25: Introduced in House
- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-26 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-07-25: Introduced in House

## Actions

- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-26 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-25",
    "latestAction": {
      "actionDate": "2025-07-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4756",
    "number": "4756",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001316",
        "district": "7",
        "firstName": "Eric",
        "fullName": "Rep. Burlison, Eric [R-MO-7]",
        "lastName": "Burlison",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Freights First Act",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:43Z",
    "updateDateIncludingText": "2025-10-07T08:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-26",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-25",
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
      "actionDate": "2025-07-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-25",
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
          "date": "2025-07-25T15:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-26T21:31:15Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
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
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "PA"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4756ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4756\nIN THE HOUSE OF REPRESENTATIVES\nJuly 25, 2025 Mr. Burlison (for himself, Mr. Perry , and Ms. Hageman ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to limit the preference for Amtrak using rail lines, junctions, and crossings near ports and rail yards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freights First Act .\n#### 2. Limitation of preference for Amtrak\nSection 24308(c) of title 49, United States Code, is amended\u2014\n**(1)**\nby striking Except in an emergency and inserting the following:\n(1) In general Except as provided in paragraph (2) or in an emergency ; and\n**(2)**\nby adding at the end the following:\n(2) Limitation of preference Intercity and commuter rail passenger transportation provided by or for Amtrak shall not have preference over freight transportation in using a rail line, junction, or crossing if such rail line, junction, or crossing is located within 50 miles of a port or rail yard. .",
      "versionDate": "2025-07-25",
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
        "updateDate": "2025-09-12T18:23:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-25",
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
          "measure-id": "id119hr4756",
          "measure-number": "4756",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-25",
          "originChamber": "HOUSE",
          "update-date": "2025-09-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4756v00",
            "update-date": "2025-09-15"
          },
          "action-date": "2025-07-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Freights First Act</strong></p><p>This bill eliminates Amtrak's preference over freight transportation in using a rail line, junction, or crossing if such rail line, junction, or crossing is located within 50 miles of a port or rail yard. Currently, Amtrak's priority status does not apply if there is\u00a0an emergency.</p>"
        },
        "title": "Freights First Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4756.xml",
    "summary": {
      "actionDate": "2025-07-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freights First Act</strong></p><p>This bill eliminates Amtrak's preference over freight transportation in using a rail line, junction, or crossing if such rail line, junction, or crossing is located within 50 miles of a port or rail yard. Currently, Amtrak's priority status does not apply if there is\u00a0an emergency.</p>",
      "updateDate": "2025-09-15",
      "versionCode": "id119hr4756"
    },
    "title": "Freights First Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freights First Act</strong></p><p>This bill eliminates Amtrak's preference over freight transportation in using a rail line, junction, or crossing if such rail line, junction, or crossing is located within 50 miles of a port or rail yard. Currently, Amtrak's priority status does not apply if there is\u00a0an emergency.</p>",
      "updateDate": "2025-09-15",
      "versionCode": "id119hr4756"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4756ih.xml"
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
      "title": "Freights First Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T03:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freights First Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to limit the preference for Amtrak using rail lines, junctions, and crossings near ports and rail yards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:20Z"
    }
  ]
}
```
