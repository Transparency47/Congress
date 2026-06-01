# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/315?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/315
- Title: To waive certain provisions in the case of an emergency declaration under the Robert T. Stafford Disaster Relief and Emergency Assistance Act.
- Congress: 119
- Bill type: HR
- Bill number: 315
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-03-13T16:31:13Z
- Update date including text: 2025-03-13T16:31:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-10 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-10 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/315",
    "number": "315",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "R000600",
        "district": "",
        "firstName": "Aumua Amata",
        "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS]",
        "lastName": "Radewagen",
        "party": "R",
        "state": "AS"
      }
    ],
    "title": "To waive certain provisions in the case of an emergency declaration under the Robert T. Stafford Disaster Relief and Emergency Assistance Act.",
    "type": "HR",
    "updateDate": "2025-03-13T16:31:13Z",
    "updateDateIncludingText": "2025-03-13T16:31:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-10",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:34:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-10T15:32:20Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr315ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 315\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mrs. Radewagen introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo waive certain provisions in the case of an emergency declaration under the Robert T. Stafford Disaster Relief and Emergency Assistance Act.\n#### 1. Waiver of certain provisions\nIn the case of an emergency declared pursuant to section 501 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5191 ), the Administrator of the Federal Emergency Management Agency shall not require the application of chapter 83 of title 41, United States Code, with respect to purchases made or contracts issued by Puerto Rico, the District of Columbia, American Samoa, or the Virgin Islands of the United States.",
      "versionDate": "2025-01-09",
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
        "name": "Emergency Management",
        "updateDate": "2025-02-18T20:37:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr315",
          "measure-number": "315",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr315v00",
            "update-date": "2025-03-13"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill prohibits the Federal Emergency Management Agency from requiring the application of the Buy American requirements (requirements for the use of goods mined, produced, or manufactured in the United States) with respect to purchases made or contracts issued by Puerto Rico, the District of Columbia, American Samoa, or the U.S. Virgin Islands\u00a0in the case of an emergency declaration.</p>"
        },
        "title": "To waive certain provisions in the case of an emergency declaration under the Robert T. Stafford Disaster Relief and Emergency Assistance Act."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr315.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits the Federal Emergency Management Agency from requiring the application of the Buy American requirements (requirements for the use of goods mined, produced, or manufactured in the United States) with respect to purchases made or contracts issued by Puerto Rico, the District of Columbia, American Samoa, or the U.S. Virgin Islands\u00a0in the case of an emergency declaration.</p>",
      "updateDate": "2025-03-13",
      "versionCode": "id119hr315"
    },
    "title": "To waive certain provisions in the case of an emergency declaration under the Robert T. Stafford Disaster Relief and Emergency Assistance Act."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits the Federal Emergency Management Agency from requiring the application of the Buy American requirements (requirements for the use of goods mined, produced, or manufactured in the United States) with respect to purchases made or contracts issued by Puerto Rico, the District of Columbia, American Samoa, or the U.S. Virgin Islands\u00a0in the case of an emergency declaration.</p>",
      "updateDate": "2025-03-13",
      "versionCode": "id119hr315"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr315ih.xml"
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
      "title": "To waive certain provisions in the case of an emergency declaration under the Robert T. Stafford Disaster Relief and Emergency Assistance Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:27Z"
    },
    {
      "title": "To waive certain provisions in the case of an emergency declaration under the Robert T. Stafford Disaster Relief and Emergency Assistance Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T09:05:35Z"
    }
  ]
}
```
