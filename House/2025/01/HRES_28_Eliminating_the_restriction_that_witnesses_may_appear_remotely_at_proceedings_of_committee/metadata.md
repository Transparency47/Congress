# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/28?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/28
- Title: BRIDGE to Congress Resolution
- Congress: 119
- Bill type: HRES
- Bill number: 28
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-02-03T18:19:04Z
- Update date including text: 2025-02-03T18:19:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-09 - Committee: Submitted in House
- 2025-01-09 - IntroReferral: Submitted in House
- Latest action: 2025-01-09: Submitted in House

## Actions

- 2025-01-09 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-09 - Committee: Submitted in House
- 2025-01-09 - IntroReferral: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/28",
    "number": "28",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "BRIDGE to Congress Resolution",
    "type": "HRES",
    "updateDate": "2025-02-03T18:19:04Z",
    "updateDateIncludingText": "2025-02-03T18:19:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-01-09T14:31:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres28ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 28\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Perez (for herself and Mr. Golden of Maine ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nEliminating the restriction that witnesses may appear remotely at proceedings of committees of the House of Representatives only at the discretion of the chair of the committee.\n#### 1. Short title\nThis resolution may be cited as the Bringing Real Ideas, Data, and Genuine Experience to Congress Resolution or the BRIDGE to Congress Resolution .\n#### 2. Elimination of restriction that witnesses may appear remotely at committee proceedings only at discretion of chair\nSection 3(i)(1) of House Resolution 5, agreed to January 3, 2025, is amended by striking at the discretion of the chair of the committee and .",
      "versionDate": "2025-01-09",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commuting",
            "updateDate": "2025-01-15T18:42:28Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-01-15T18:42:23Z"
          },
          {
            "name": "Congressional committees",
            "updateDate": "2025-01-15T18:41:55Z"
          },
          {
            "name": "Congressional operations and organization",
            "updateDate": "2025-01-15T18:42:11Z"
          },
          {
            "name": "Evidence and witnesses",
            "updateDate": "2025-01-15T18:42:18Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-01-15T18:42:34Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-15T18:42:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-10T15:28:25Z"
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
          "measure-id": "id119hres28",
          "measure-number": "28",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres28v00",
            "update-date": "2025-02-03"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bringing Real Ideas, Data, and Genuine Experience to Congress Resolution or the BRIDGE to Congress Resolution</strong></p><p>This resolution modifies the House Rules regarding remote testimony of witnesses in committee proceedings. Specifically, the resolution eliminates the requirement for the committee chair to approve remote testimony of witnesses. </p>"
        },
        "title": "BRIDGE to Congress Resolution"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres28.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bringing Real Ideas, Data, and Genuine Experience to Congress Resolution or the BRIDGE to Congress Resolution</strong></p><p>This resolution modifies the House Rules regarding remote testimony of witnesses in committee proceedings. Specifically, the resolution eliminates the requirement for the committee chair to approve remote testimony of witnesses. </p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hres28"
    },
    "title": "BRIDGE to Congress Resolution"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bringing Real Ideas, Data, and Genuine Experience to Congress Resolution or the BRIDGE to Congress Resolution</strong></p><p>This resolution modifies the House Rules regarding remote testimony of witnesses in committee proceedings. Specifically, the resolution eliminates the requirement for the committee chair to approve remote testimony of witnesses. </p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hres28"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres28ih.xml"
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
      "title": "BRIDGE to Congress Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BRIDGE to Congress Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-10T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bringing Real Ideas, Data, and Genuine Experience to Congress Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-10T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Eliminating the restriction that witnesses may appear remotely at proceedings of committees of the House of Representatives only at the discretion of the chair of the committee.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-10T09:18:18Z"
    }
  ]
}
```
