# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/196?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/196
- Title: Expressing support for the designation of the week beginning March 2, 2025, as "School Social Work Week".
- Congress: 119
- Bill type: HRES
- Bill number: 196
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-05-29T19:21:44Z
- Update date including text: 2026-05-29T19:21:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-03-05 - Committee: Submitted in House
- Latest action: 2025-03-05: Submitted in House

## Actions

- 2025-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-03-05 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/196",
    "number": "196",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001160",
        "district": "4",
        "firstName": "Gwen",
        "fullName": "Rep. Moore, Gwen [D-WI-4]",
        "lastName": "Moore",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Expressing support for the designation of the week beginning March 2, 2025, as \"School Social Work Week\".",
    "type": "HRES",
    "updateDate": "2026-05-29T19:21:44Z",
    "updateDateIncludingText": "2026-05-29T19:21:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-03-05T15:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres196ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 196\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Ms. Moore of Wisconsin (for herself, Ms. Scholten , and Ms. Garcia of Texas ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing support for the designation of the week beginning March 2, 2025, as School Social Work Week .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of School Social Work Week ;\n**(2)**\nhonors and recognizes the contributions of school social workers to the successes of students in schools across the Nation; and\n**(3)**\nencourages the people of the United States to observe School Social Work Week with appropriate ceremonies and activities that promote awareness of the vital role of school social workers, in schools and in the community as a whole, in helping students prepare for their futures as productive citizens.",
      "versionDate": "2025-03-05",
      "versionType": "IH"
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
        "actionDate": "2026-03-04",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1103",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of the week beginning March 2, 2026, as \"School Social Work Week\".",
      "type": "HRES"
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
            "name": "Commemorative events and holidays",
            "updateDate": "2026-02-11T16:53:58Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2026-02-11T16:53:58Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-02-11T16:53:58Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2026-02-11T16:53:58Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2026-02-11T16:53:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-10T17:41:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hres196",
          "measure-number": "196",
          "measure-type": "hres",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres196v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of School Social Work Week.</p>"
        },
        "title": "Expressing support for the designation of the week beginning March 2, 2025, as \"School Social Work Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres196.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of School Social Work Week.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hres196"
    },
    "title": "Expressing support for the designation of the week beginning March 2, 2025, as \"School Social Work Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of School Social Work Week.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hres196"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres196ih.xml"
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
      "title": "Expressing support for the designation of the week beginning March 2, 2025, as \"School Social Work Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T11:33:40Z"
    },
    {
      "title": "Expressing support for the designation of the week beginning March 2, 2025, as \"School Social Work Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T09:06:20Z"
    }
  ]
}
```
