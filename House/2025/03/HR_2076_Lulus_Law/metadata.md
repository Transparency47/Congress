# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2076?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2076
- Title: Lulu’s Law
- Congress: 119
- Bill type: HR
- Bill number: 2076
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2026-04-22T14:41:20Z
- Update date including text: 2026-04-22T14:41:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-11 - Committee: Referred to the Subcommittee on Communications and Technology.
- 2026-01-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-01-15 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-04-09 - Calendars: Placed on the Union Calendar, Calendar No. 518.
- 2026-04-09 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-598.
- 2026-04-09 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-598.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-11 - Committee: Referred to the Subcommittee on Communications and Technology.
- 2026-01-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-01-15 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-04-09 - Calendars: Placed on the Union Calendar, Calendar No. 518.
- 2026-04-09 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-598.
- 2026-04-09 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-598.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2076",
    "number": "2076",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000609",
        "district": "6",
        "firstName": "Gary",
        "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
        "lastName": "Palmer",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Lulu\u2019s Law",
    "type": "HR",
    "updateDate": "2026-04-22T14:41:20Z",
    "updateDateIncludingText": "2026-04-22T14:41:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-04-09",
      "calendarNumber": {
        "calendar": "U00518"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 518.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-598.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-598.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Communications and Technology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
            "date": "2026-04-09T15:57:46Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-11T14:07:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-01-15T22:00:10Z",
                "name": "Reported by"
              },
              {
                "date": "2026-01-15T21:59:26Z",
                "name": "Markup by"
              },
              {
                "date": "2025-03-11T20:58:54Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "AL"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "AL"
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
      "sponsorshipDate": "2025-12-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2076ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2076\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Palmer introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Federal Communications Commission to issue an order providing that a shark attack is an event for which a wireless emergency alert may be transmitted, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Lulu\u2019s Law .\n#### 2. Wireless emergency alerts\n##### (a) Definition\nIn this section, the term Alert Message has the meaning given the term in section 10.10(a) of title 47, Code of Federal Regulations, or any successor regulation.\n##### (b) Requirement\nNot later than 180 days after the date of enactment of this Act, the Federal Communications Commission shall issue an order to provide that a shark attack is an event for which an Alert Message may be transmitted.",
      "versionDate": "2025-03-11",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr2076rh.xml",
      "text": "IB\nUnion Calendar No. 518\n119th CONGRESS\n2d Session\nH. R. 2076\n[Report No. 119\u2013598]\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Palmer introduced the following bill; which was referred to the Committee on Energy and Commerce\nApril 9, 2026 Additional sponsors: Mr. Figures , Ms. Sewell , and Mr. Vindman\nApril 9, 2026 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo require the Federal Communications Commission to issue an order providing that a shark attack is an event for which a wireless emergency alert may be transmitted, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Lulu\u2019s Law .\n#### 2. Wireless emergency alerts\n##### (a) Definition\nIn this section, the term Alert Message has the meaning given the term in section 10.10(a) of title 47, Code of Federal Regulations, or any successor regulation.\n##### (b) Requirement\nNot later than 180 days after the date of enactment of this Act, the Federal Communications Commission shall issue an order to provide that a shark attack is an event for which an Alert Message may be transmitted.",
      "versionDate": "2026-04-09",
      "versionType": "Reported in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-10",
        "actionTime": "11:05:00",
        "text": "Held at the desk."
      },
      "number": "1003",
      "relationshipDetails": {
        "item": [
          {
            "identifiedBy": "House",
            "type": "Related bill"
          },
          {
            "identifiedBy": "CRS",
            "type": "Identical bill"
          }
        ]
      },
      "title": "Lulu\u2019s Law",
      "type": "S"
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
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2026-01-21T17:02:00Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2026-01-21T17:02:00Z"
          },
          {
            "name": "Fishes",
            "updateDate": "2026-01-21T17:02:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-26T13:50:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119hr2076",
          "measure-number": "2076",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2025-04-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2076v00",
            "update-date": "2025-04-28"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Lulu\u2019s Law</strong></p><p>This bill requires the Federal Communications Commission to issue an order explicitly permitting the transmission of wireless emergency alerts to mobile phones in the event of a shark attack.\u00a0</p><p>(Under current regulations, authorized government authorities are permitted to send wireless emergency alerts regarding public safety emergencies, including severe weather, missing children, and other threats to life or property.)</p>"
        },
        "title": "Lulu\u2019s Law"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2076.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Lulu\u2019s Law</strong></p><p>This bill requires the Federal Communications Commission to issue an order explicitly permitting the transmission of wireless emergency alerts to mobile phones in the event of a shark attack.\u00a0</p><p>(Under current regulations, authorized government authorities are permitted to send wireless emergency alerts regarding public safety emergencies, including severe weather, missing children, and other threats to life or property.)</p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119hr2076"
    },
    "title": "Lulu\u2019s Law"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Lulu\u2019s Law</strong></p><p>This bill requires the Federal Communications Commission to issue an order explicitly permitting the transmission of wireless emergency alerts to mobile phones in the event of a shark attack.\u00a0</p><p>(Under current regulations, authorized government authorities are permitted to send wireless emergency alerts regarding public safety emergencies, including severe weather, missing children, and other threats to life or property.)</p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119hr2076"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2076ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr2076rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Lulu\u2019s Law",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-04-10T06:08:23Z"
    },
    {
      "title": "Lulu\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lulu\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Federal Communications Commission to issue an order providing that a shark attack is an event for which a wireless emergency alert may be transmitted, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:28Z"
    }
  ]
}
```
