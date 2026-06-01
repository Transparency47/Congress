# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/27?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sjres/27
- Title: A joint resolution providing for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services.
- Congress: 119
- Bill type: SJRES
- Bill number: 27
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2025-05-21T16:49:14Z
- Update date including text: 2025-05-21T16:49:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sjres/27",
    "number": "27",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services.",
    "type": "SJRES",
    "updateDate": "2025-05-21T16:49:14Z",
    "updateDateIncludingText": "2025-05-21T16:49:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-02-25T23:38:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres27is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 27\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Sanders introduced the following joint resolution; which was read twice and referred to the Committee on Foreign Relations\nJOINT RESOLUTION\nProviding for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services.\nThat the following proposed foreign military sale to Israel is prohibited:\n**(1)**\nThe sale of the following defense articles and services, described in Transmittal No. 24\u20130U, submitted to Congress pursuant to section 36(b)(1) of the Arms Export Control Act ( 22 U.S.C. 2776(b)(1) ), and published in the Congressional Record on February 10, 2025: an additional ten thousand (10,000) M107 and/ or M795 155mm High Explosive projectiles. Also included are the following non-MDE items: various 155mm projectiles; publications; technical documentation; U.S. Government and contractor engineering, technical and logistics support services; studies and surveys; and other related elements of logistical and program support.",
      "versionDate": "2025-02-25",
      "versionType": "IS"
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
        "updateDate": "2025-05-07T13:40:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
    "originChamber": "Senate",
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
          "measure-id": "id119sjres27",
          "measure-number": "27",
          "measure-type": "sjres",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2025-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres27v00",
            "update-date": "2025-05-21"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution prohibits a proposed foreign military sale of certain defense articles and services to Israel.</p>"
        },
        "title": "A joint resolution providing for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres27.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution prohibits a proposed foreign military sale of certain defense articles and services to Israel.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119sjres27"
    },
    "title": "A joint resolution providing for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services."
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution prohibits a proposed foreign military sale of certain defense articles and services to Israel.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119sjres27"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres27is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:22Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T11:56:15Z"
    }
  ]
}
```
