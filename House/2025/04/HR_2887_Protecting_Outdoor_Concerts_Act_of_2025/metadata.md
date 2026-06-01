# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2887?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2887
- Title: Protecting Outdoor Concerts Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2887
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2025-06-12T08:06:59Z
- Update date including text: 2025-06-12T08:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-10 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-10 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2887",
    "number": "2887",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "R000599",
        "district": "25",
        "firstName": "Raul",
        "fullName": "Rep. Ruiz, Raul [D-CA-25]",
        "lastName": "Ruiz",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Protecting Outdoor Concerts Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-12T08:06:59Z",
    "updateDateIncludingText": "2025-06-12T08:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:11:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-10T20:49:25Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2887ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2887\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Ruiz introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Aviation Administration to issue or revise regulations to provide for temporary flight restrictions in the vicinity of outdoor music festivals.\n#### 1. Short title\nThis Act may be cited as the Protecting Outdoor Concerts Act of 2025 .\n#### 2. Temporary flight restrictions for outdoor concerts or music festivals\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Aviation Administration shall issue or revise regulations to ensure that the Federal Aviation Administration issues a Notice to Airmen designating an area of airspace in which a temporary flight restriction applies to manned aircraft and unmanned aircraft when the Administrator determines that a temporary flight restriction is necessary to protect persons or property on the surface or in the air, to maintain air safety and efficiency, or to prevent the unsafe congestion of aircraft in the vicinity of an outdoor concert or music festival with an attendance of not fewer than 30,000 people per day.\n##### (b) Relationship to existing regulations\nIn issuing or revising regulations under subsection (a), the Administrator, to the extent practicable, shall\u2014\n**(1)**\ntreat an outdoor concert or music festival in the same manner as an aerial demonstration or major sporting event is treated under section 91.145 of title 14, Code of Federal Regulations; and\n**(2)**\ndesignate areas of airspace in which a temporary flight restriction applies in the same manner as areas are designated under section 44812 of title 49, United States Code, with respect to unmanned aircraft.",
      "versionDate": "2025-04-10",
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
        "updateDate": "2025-05-19T16:04:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2887",
          "measure-number": "2887",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2025-05-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2887v00",
            "update-date": "2025-05-22"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Outdoor Concerts Act of 2025</strong></p><p>This bill requires the Federal Aviation Administration to issue or revise regulations to provide for temporary flight restrictions in the vicinity of an outdoor concert or music festival that has a daily attendance of 30,000 people or more. This requirement applies to manned aircraft and unmanned aircraft (i.e., drones).</p><p>\u00a0</p>"
        },
        "title": "Protecting Outdoor Concerts Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2887.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Outdoor Concerts Act of 2025</strong></p><p>This bill requires the Federal Aviation Administration to issue or revise regulations to provide for temporary flight restrictions in the vicinity of an outdoor concert or music festival that has a daily attendance of 30,000 people or more. This requirement applies to manned aircraft and unmanned aircraft (i.e., drones).</p><p>\u00a0</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119hr2887"
    },
    "title": "Protecting Outdoor Concerts Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Outdoor Concerts Act of 2025</strong></p><p>This bill requires the Federal Aviation Administration to issue or revise regulations to provide for temporary flight restrictions in the vicinity of an outdoor concert or music festival that has a daily attendance of 30,000 people or more. This requirement applies to manned aircraft and unmanned aircraft (i.e., drones).</p><p>\u00a0</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119hr2887"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2887ih.xml"
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
      "title": "Protecting Outdoor Concerts Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Outdoor Concerts Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Aviation Administration to issue or revise regulations to provide for temporary flight restrictions in the vicinity of outdoor music festivals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T04:18:18Z"
    }
  ]
}
```
