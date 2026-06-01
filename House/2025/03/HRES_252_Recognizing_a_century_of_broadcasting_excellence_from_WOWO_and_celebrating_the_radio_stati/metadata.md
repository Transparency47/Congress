# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/252?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/252
- Title: Recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary.
- Congress: 119
- Bill type: HRES
- Bill number: 252
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2025-05-23T10:45:11Z
- Update date including text: 2025-05-23T10:45:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-03-31 - IntroReferral: Sponsor introductory remarks on measure. (CR H1344)
- Latest action: 2025-03-25: Submitted in House

## Actions

- 2025-03-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-03-31 - IntroReferral: Sponsor introductory remarks on measure. (CR H1344)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/252",
    "number": "252",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S001188",
        "district": "3",
        "firstName": "Marlin",
        "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
        "lastName": "Stutzman",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary.",
    "type": "HRES",
    "updateDate": "2025-05-23T10:45:11Z",
    "updateDateIncludingText": "2025-05-23T10:45:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1344)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:03:45Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres252ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 252\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Stutzman (for himself and Mr. Yakym ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nRecognizing a century of broadcasting excellence from WOWO and celebrating the radio station\u2019s 100th anniversary.\nThat the House\u2014\n**(1)**\ncelebrates WOWO\u2019s 100th anniversary on air;\n**(2)**\nrecognizes WOWO\u2019s record of exemplary broadcasting, which has strengthened communities and educated countless families on the most important issues; and\n**(3)**\nsupports WOWO\u2019s efforts to continue informing and inspiring generations to come.",
      "versionDate": "2025-03-25",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-26T18:05:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
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
          "measure-id": "id119hres252",
          "measure-number": "252",
          "measure-type": "hres",
          "orig-publish-date": "2025-03-25",
          "originChamber": "HOUSE",
          "update-date": "2025-05-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres252v00",
            "update-date": "2025-05-23"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution celebrates the 100th anniversary of the Fort Wayne, Indiana radio station WOWO.\u00a0</p>"
        },
        "title": "Recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres252.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution celebrates the 100th anniversary of the Fort Wayne, Indiana radio station WOWO.\u00a0</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119hres252"
    },
    "title": "Recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary."
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution celebrates the 100th anniversary of the Fort Wayne, Indiana radio station WOWO.\u00a0</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119hres252"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres252ih.xml"
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
      "title": "Recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T10:33:16Z"
    },
    {
      "title": "Recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T08:06:14Z"
    }
  ]
}
```
