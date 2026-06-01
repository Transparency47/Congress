# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/62?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/62
- Title: Supporting the goals and ideals of a Juan Pablo Duarte Day.
- Congress: 119
- Bill type: HRES
- Bill number: 62
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-03-03T21:29:54Z
- Update date including text: 2025-03-03T21:29:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-01-23 - IntroReferral: Sponsor introductory remarks on measure. (CR H350)
- 2025-01-23 - Committee: Submitted in House
- 2025-01-23 - IntroReferral: Submitted in House
- Latest action: 2025-01-23: Submitted in House

## Actions

- 2025-01-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-01-23 - IntroReferral: Sponsor introductory remarks on measure. (CR H350)
- 2025-01-23 - Committee: Submitted in House
- 2025-01-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/62",
    "number": "62",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "E000297",
        "district": "13",
        "firstName": "Adriano",
        "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
        "lastName": "Espaillat",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Supporting the goals and ideals of a Juan Pablo Duarte Day.",
    "type": "HRES",
    "updateDate": "2025-03-03T21:29:54Z",
    "updateDateIncludingText": "2025-03-03T21:29:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionCode": "H12100",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H350)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:08:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres62ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 62\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Espaillat submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nSupporting the goals and ideals of a Juan Pablo Duarte Day.\nThat the House of Representatives\u2014\n**(1)**\nsupports the goals and ideals of the Juan Pablo Duarte Day of the Dominican Republic;\n**(2)**\nsupports the establishment of a national day of recognition for Juan Pablo Duarte in the United States to honor the founding father of the Dominican Republic; and\n**(3)**\nurges the people of the United States to observe a national day of recognition for Dominican Americans with appropriate ceremonies, programs, and activities.",
      "versionDate": "2025-01-23",
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
        "name": "International Affairs",
        "updateDate": "2025-01-27T22:41:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hres62",
          "measure-number": "62",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres62v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the establishment of a national day of recognition to honor Juan Pablo Duarte, the founding father of the Dominican Republic, and urges the people of the United States to observe a national day of recognition for Dominican Americans.</p>"
        },
        "title": "Supporting the goals and ideals of a Juan Pablo Duarte Day."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres62.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the establishment of a national day of recognition to honor Juan Pablo Duarte, the founding father of the Dominican Republic, and urges the people of the United States to observe a national day of recognition for Dominican Americans.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hres62"
    },
    "title": "Supporting the goals and ideals of a Juan Pablo Duarte Day."
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the establishment of a national day of recognition to honor Juan Pablo Duarte, the founding father of the Dominican Republic, and urges the people of the United States to observe a national day of recognition for Dominican Americans.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hres62"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres62ih.xml"
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
      "title": "Supporting the goals and ideals of a Juan Pablo Duarte Day.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-24T09:33:22Z"
    },
    {
      "title": "Supporting the goals and ideals of a Juan Pablo Duarte Day.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T09:05:32Z"
    }
  ]
}
```
