# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1384?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1384
- Title: Veterans Equal Access Act
- Congress: 119
- Bill type: HR
- Bill number: 1384
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2026-05-20T08:08:10Z
- Update date including text: 2026-05-20T08:08:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-14 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-14 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1384",
    "number": "1384",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Veterans Equal Access Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:10Z",
    "updateDateIncludingText": "2026-05-20T08:08:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-02-14",
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
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:31:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T17:52:45Z",
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
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "OH"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "NV"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "LA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1384ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1384\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Mast introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo authorize Department of Veterans Affairs health care providers to provide recommendations and opinions to veterans regarding participation in State marijuana programs.\n#### 1. Short title\nThis Act may be cited as the Veterans Equal Access Act .\n#### 2. Provision by Department of Veterans Affairs health care providers of recommendations and opinions regarding veteran participation in State marijuana programs\n##### (a) In general\nNotwithstanding any other provision of law, the Secretary of Veterans Affairs shall authorize physicians and other health care providers employed by the Department of Veterans Affairs to\u2014\n**(1)**\nprovide recommendations and opinions to veterans who are residents of States with State marijuana programs regarding the participation of veterans in such State marijuana programs; and\n**(2)**\ncomplete forms reflecting such recommendations and opinions.\n##### (b) State defined\nIn this section, the term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, any territory or possession of the United States, and each federally recognized Indian Tribe.",
      "versionDate": "2025-02-14",
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
            "name": "Alternative treatments",
            "updateDate": "2025-06-13T19:11:55Z"
          },
          {
            "name": "Drug therapy",
            "updateDate": "2025-06-13T19:12:06Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-06-13T19:12:12Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-06-13T19:12:01Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-06-13T19:12:18Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-13T19:11:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T16:45:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-14",
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
          "measure-id": "id119hr1384",
          "measure-number": "1384",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1384v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Equal Access Act</strong></p> <p>This bill directs the Department of Veterans Affairs (VA) to authorize VA health care providers to (1) provide veterans with recommendations and opinions regarding participation in their state's marijuana programs, and (2) complete forms reflecting such recommendations and opinions.</p>"
        },
        "title": "Veterans Equal Access Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1384.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Equal Access Act</strong></p> <p>This bill directs the Department of Veterans Affairs (VA) to authorize VA health care providers to (1) provide veterans with recommendations and opinions regarding participation in their state's marijuana programs, and (2) complete forms reflecting such recommendations and opinions.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr1384"
    },
    "title": "Veterans Equal Access Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Equal Access Act</strong></p> <p>This bill directs the Department of Veterans Affairs (VA) to authorize VA health care providers to (1) provide veterans with recommendations and opinions regarding participation in their state's marijuana programs, and (2) complete forms reflecting such recommendations and opinions.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr1384"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1384ih.xml"
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
      "title": "Veterans Equal Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Equal Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize Department of Veterans Affairs health care providers to provide recommendations and opinions to veterans regarding participation in State marijuana programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:18:40Z"
    }
  ]
}
```
