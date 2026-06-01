# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/21?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/21
- Title: Disapproving of the rule submitted by the Department of Homeland Security relating to "Modernizing H-2 Program Requirements, Oversight, and Worker Protections".
- Congress: 119
- Bill type: HJRES
- Bill number: 21
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-01-23T02:57:56Z
- Update date including text: 2025-01-23T02:57:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/21",
    "number": "21",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Modernizing H-2 Program Requirements, Oversight, and Worker Protections\".",
    "type": "HJRES",
    "updateDate": "2025-01-23T02:57:56Z",
    "updateDateIncludingText": "2025-01-23T02:57:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:10:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres21ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 21\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Arrington (for himself, Mr. Self , and Mr. Moore of West Virginia ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nDisapproving of the rule submitted by the Department of Homeland Security relating to Modernizing H\u20132 Program Requirements, Oversight, and Worker Protections .\nThat Congress disapproves the rule submitted by the Department of Homeland Security relating to Modernizing H\u20132 Program Requirements, Oversight, and Worker Protections (89 Fed. Reg. 103202), and such rule shall have no force or effect.",
      "versionDate": "2025-01-16",
      "versionType": "IH"
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
        "name": "Immigration",
        "updateDate": "2025-01-17T19:37:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hjres21",
          "measure-number": "21",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres21v00",
            "update-date": "2025-01-23"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Modernizing H\u20132 Program Requirements, Oversight, and Worker Protections</em> and published on December 18, 2024. This rule modifies several regulations applicable to agricultural (H-2A) and nonagricultural (H-2B) temporary nonimmigrant workers, including by providing additional whistleblower protections for these workers, eliminating the differential treatment of nationals of countries designated as eligible, and establishing a 60-day grace period for workers after the revocation or cessation of eligible employment.</p>"
        },
        "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Modernizing H-2 Program Requirements, Oversight, and Worker Protections\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres21.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Modernizing H\u20132 Program Requirements, Oversight, and Worker Protections</em> and published on December 18, 2024. This rule modifies several regulations applicable to agricultural (H-2A) and nonagricultural (H-2B) temporary nonimmigrant workers, including by providing additional whistleblower protections for these workers, eliminating the differential treatment of nationals of countries designated as eligible, and establishing a 60-day grace period for workers after the revocation or cessation of eligible employment.</p>",
      "updateDate": "2025-01-23",
      "versionCode": "id119hjres21"
    },
    "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Modernizing H-2 Program Requirements, Oversight, and Worker Protections\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule issued by the Department of Homeland Security titled <em>Modernizing H\u20132 Program Requirements, Oversight, and Worker Protections</em> and published on December 18, 2024. This rule modifies several regulations applicable to agricultural (H-2A) and nonagricultural (H-2B) temporary nonimmigrant workers, including by providing additional whistleblower protections for these workers, eliminating the differential treatment of nationals of countries designated as eligible, and establishing a 60-day grace period for workers after the revocation or cessation of eligible employment.</p>",
      "updateDate": "2025-01-23",
      "versionCode": "id119hjres21"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres21ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Modernizing H-2 Program Requirements, Oversight, and Worker Protections\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-17T09:18:23Z"
    },
    {
      "title": "Disapproving of the rule submitted by the Department of Homeland Security relating to \"Modernizing H-2 Program Requirements, Oversight, and Worker Protections\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-17T09:05:47Z"
    }
  ]
}
```
