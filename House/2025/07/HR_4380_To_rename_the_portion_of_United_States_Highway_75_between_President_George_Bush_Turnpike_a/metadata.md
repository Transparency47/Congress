# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4380?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4380
- Title: To rename the portion of United States Highway 75 between President George Bush Turnpike and United States Highway 380 as the "U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway".
- Congress: 119
- Bill type: HR
- Bill number: 4380
- Origin chamber: House
- Introduced date: 2025-07-14
- Update date: 2025-09-11T08:06:07Z
- Update date including text: 2025-09-11T08:06:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-14: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-15 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-14: Introduced in House

## Actions

- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-15 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4380",
    "number": "4380",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To rename the portion of United States Highway 75 between President George Bush Turnpike and United States Highway 380 as the \"U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway\".",
    "type": "HR",
    "updateDate": "2025-09-11T08:06:07Z",
    "updateDateIncludingText": "2025-09-11T08:06:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-14",
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
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-14",
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
          "date": "2025-07-14T16:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-15T17:00:44Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4380ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4380\nIN THE HOUSE OF REPRESENTATIVES\nJuly 14, 2025 Mr. Self introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo rename the portion of United States Highway 75 between President George Bush Turnpike and United States Highway 380 as the U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway .\n#### 1. Designation of U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway\n##### (a) Designation\nThe portion of United States Highway 75 between President George Bush Turnpike and United States Highway 380 currently designated as Sam Johnson Highway , shall, after the date of enactment of this Act, be known and designated as the U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway .\n##### (b) Reference\nAny reference in any law, regulation, map, document, paper, or other record of the United States to the portion of the highway referred to in subsection (a) shall be considered to be a reference to the U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway.",
      "versionDate": "2025-07-14",
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
        "updateDate": "2025-09-10T16:44:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-14",
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
          "measure-id": "id119hr4380",
          "measure-number": "4380",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-14",
          "originChamber": "HOUSE",
          "update-date": "2025-09-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4380v00",
            "update-date": "2025-09-10"
          },
          "action-date": "2025-07-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill renames the portion of U.S. Highway 75 between President George Bush Turnpike and U.S. Highway 380 as the U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway. Currently, this portion of the highway is designated as the\u00a0Sam Johnson Highway.</p>"
        },
        "title": "To rename the portion of United States Highway 75 between President George Bush Turnpike and United States Highway 380 as the \"U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4380.xml",
    "summary": {
      "actionDate": "2025-07-14",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill renames the portion of U.S. Highway 75 between President George Bush Turnpike and U.S. Highway 380 as the U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway. Currently, this portion of the highway is designated as the\u00a0Sam Johnson Highway.</p>",
      "updateDate": "2025-09-10",
      "versionCode": "id119hr4380"
    },
    "title": "To rename the portion of United States Highway 75 between President George Bush Turnpike and United States Highway 380 as the \"U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway\"."
  },
  "summaries": [
    {
      "actionDate": "2025-07-14",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill renames the portion of U.S. Highway 75 between President George Bush Turnpike and U.S. Highway 380 as the U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway. Currently, this portion of the highway is designated as the\u00a0Sam Johnson Highway.</p>",
      "updateDate": "2025-09-10",
      "versionCode": "id119hr4380"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4380ih.xml"
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
      "title": "To rename the portion of United States Highway 75 between President George Bush Turnpike and United States Highway 380 as the \"U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T08:33:22Z"
    },
    {
      "title": "To rename the portion of United States Highway 75 between President George Bush Turnpike and United States Highway 380 as the \"U.S. Congressman and Prisoner of War Sam Johnson Memorial Highway\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-15T08:05:32Z"
    }
  ]
}
```
