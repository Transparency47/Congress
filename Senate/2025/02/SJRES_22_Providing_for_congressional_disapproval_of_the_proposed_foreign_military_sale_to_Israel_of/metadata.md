# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/22?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/22
- Title: A joint resolution providing for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services.
- Congress: 119
- Bill type: SJRES
- Bill number: 22
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-12-05T21:42:22Z
- Update date including text: 2025-12-05T21:42:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/22",
    "number": "22",
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
    "updateDate": "2025-12-05T21:42:22Z",
    "updateDateIncludingText": "2025-12-05T21:42:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T19:11:53Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres22is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 22\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Sanders introduced the following joint resolution; which was read twice and referred to the Committee on Foreign Relations\nJOINT RESOLUTION\nProviding for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services.\nThat the following proposed foreign military sale to Israel is prohibited:\n**(1)**\nThe sale of the following defense articles and services, described in Transmittal No. 24\u2013104, submitted to Congress pursuant to section 36(b)(1) of the Arms Export Control Act ( 22 U.S.C. 2776(b)(1) ), and published in the Congressional Record on February 10, 2025: three thousand (3,000) AGM\u2013114 Hellfire Air-to-Ground Missiles, to include one or any combination of the R3, F, F/A, K1, K1A, K2, K3, K3A, KA, N, N3, and/or R variants. The following non-MDE items will also be included: support and test equipment; integration and test support; spare and repair parts; software delivery and support; publications and technical documentation; personnel training and training equipment; U.S. Government and contractor engineering; technical and logistics support services; storage; and other related elements of logistics and program support.",
      "versionDate": "2025-02-20",
      "versionType": "IS"
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
        "actionDate": "2025-03-03",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "71",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Providing for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services.",
      "type": "HJRES"
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
        "updateDate": "2025-05-06T15:57:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
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
          "measure-id": "id119sjres22",
          "measure-number": "22",
          "measure-type": "sjres",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2025-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres22v00",
            "update-date": "2025-05-12"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution prohibits the proposed foreign military sale of certain defense articles and services to Israel.</p>"
        },
        "title": "A joint resolution providing for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres22.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution prohibits the proposed foreign military sale of certain defense articles and services to Israel.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119sjres22"
    },
    "title": "A joint resolution providing for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services."
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution prohibits the proposed foreign military sale of certain defense articles and services to Israel.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119sjres22"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres22is.xml"
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
      "updateDate": "2025-02-25T05:18:36Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval of the proposed foreign military sale to Israel of certain defense articles and services.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T11:56:26Z"
    }
  ]
}
```
