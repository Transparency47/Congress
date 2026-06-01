# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8225?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8225
- Title: To designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the "Sorensen-Estrada Post Office".
- Congress: 119
- Bill type: HR
- Bill number: 8225
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-05-14T19:20:19Z
- Update date including text: 2026-05-14T19:20:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported by Voice Vote.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8225",
    "number": "8225",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\".",
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
      "text": "Ordered to be Reported by Voice Vote.",
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
      "actionDate": "2026-04-09",
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
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
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
            "date": "2026-04-29T13:09:31Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-09T15:33:30Z",
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
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "UT"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "UT"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8225ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8225\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Moore of Utah (for himself, Ms. Maloy , Mr. Owens , and Mr. Kennedy of Utah ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the Sorensen-Estrada Post Office .\n#### 1. Sorensen-Estrada Post Office\n##### (a) Designation\nThe facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, shall be known and designated as the Sorensen-Estrada Post Office .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Sorensen-Estrada Post Office .",
      "versionDate": "2026-04-09",
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
            "updateDate": "2026-05-08T17:21:21Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2026-05-08T17:21:28Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2026-05-08T17:21:13Z"
          },
          {
            "name": "Utah",
            "updateDate": "2026-05-08T17:21:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-14T01:37:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-09",
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
          "measure-id": "id119hr8225",
          "measure-number": "8225",
          "measure-type": "hr",
          "orig-publish-date": "2026-04-09",
          "originChamber": "HOUSE",
          "update-date": "2026-04-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr8225v00",
            "update-date": "2026-04-11"
          },
          "action-date": "2026-04-09",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr8225.xml",
    "summary": {
      "actionDate": "2026-04-09",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\".",
      "updateDate": "2026-04-11",
      "versionCode": "id119hr8225"
    },
    "title": "To designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\"."
  },
  "summaries": [
    {
      "actionDate": "2026-04-09",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\".",
      "updateDate": "2026-04-11",
      "versionCode": "id119hr8225"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8225ih.xml"
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
      "title": "To designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:24Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-10T08:06:11Z"
    }
  ]
}
```
