# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/51?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sjres/51
- Title: A joint resolution for congressional disapproval of the proposed foreign military sale to the Government of the United Arab Emirates of certain defense articles and services.
- Congress: 119
- Bill type: SJRES
- Bill number: 51
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2025-08-13T14:05:12Z
- Update date including text: 2025-08-13T14:05:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sjres/51",
    "number": "51",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001169",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Murphy, Christopher [D-CT]",
        "lastName": "Murphy",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "A joint resolution for congressional disapproval of the proposed foreign military sale to the Government of the United Arab Emirates of certain defense articles and services.",
    "type": "SJRES",
    "updateDate": "2025-08-13T14:05:12Z",
    "updateDateIncludingText": "2025-08-13T14:05:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T17:50:13Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MD"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "VA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-05-15",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres51is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 51\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mr. Murphy (for himself, Mr. Van Hollen , Mr. Kaine , and Mr. Sanders ) introduced the following joint resolution; which was read twice and referred to the Committee on Foreign Relations\nJOINT RESOLUTION\nProviding for congressional disapproval of the proposed foreign military sale to the Government of the United Arab Emirates of certain defense articles and services.\nThat the following proposed foreign military sale to the Government of the United Arab Emirates is prohibited:\n**(1)**\nThe sale of the following defense articles and services described in Transmittal No. 25\u201325, submitted to Congress pursuant to section 36(b)(1) of the Arms Export Control Act ( 22 U.S.C. 2776(b)(1) ), and published in the Congressional Record on May 13, 2025: The following non-Major Defense Equipment: Common Munitions Built-in-Test Reprogramming Equipment (CMBRE); munitions support equipment; night vision device (NVD) support and spare equipment; spare parts, consumables and accessories; repair and return support; classified and unclassified software delivery and support; classified and unclassified publications and technical documentation; site surveys; studies and surveys; transportation support; U.S. Government and contractor engineering, technical, and logistics support services; aircraft components, spares, and accessories; and other related elements of logistics and program support.",
      "versionDate": "2025-05-15",
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
        "updateDate": "2025-06-20T18:15:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-15",
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
          "measure-id": "id119sjres51",
          "measure-number": "51",
          "measure-type": "sjres",
          "orig-publish-date": "2025-05-15",
          "originChamber": "SENATE",
          "update-date": "2025-08-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres51v00",
            "update-date": "2025-08-13"
          },
          "action-date": "2025-05-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution prohibits a proposed foreign military sale of certain defense articles and services to the United Arab Emirates.</p>"
        },
        "title": "A joint resolution for congressional disapproval of the proposed foreign military sale to the Government of the United Arab Emirates of certain defense articles and services."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres51.xml",
    "summary": {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution prohibits a proposed foreign military sale of certain defense articles and services to the United Arab Emirates.</p>",
      "updateDate": "2025-08-13",
      "versionCode": "id119sjres51"
    },
    "title": "A joint resolution for congressional disapproval of the proposed foreign military sale to the Government of the United Arab Emirates of certain defense articles and services."
  },
  "summaries": [
    {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution prohibits a proposed foreign military sale of certain defense articles and services to the United Arab Emirates.</p>",
      "updateDate": "2025-08-13",
      "versionCode": "id119sjres51"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres51is.xml"
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
      "title": "A joint resolution for congressional disapproval of the proposed foreign military sale to the Government of the United Arab Emirates of certain defense articles and services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-17T04:03:25Z"
    },
    {
      "title": "A joint resolution for congressional disapproval of the proposed foreign military sale to the Government of the United Arab Emirates of certain defense articles and services.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-16T10:56:22Z"
    }
  ]
}
```
