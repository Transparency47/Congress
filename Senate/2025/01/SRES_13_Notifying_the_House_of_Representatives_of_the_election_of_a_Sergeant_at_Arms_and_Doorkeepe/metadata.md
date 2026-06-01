# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/13?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/13
- Title: A resolution notifying the House of Representatives of the election of a Sergeant at Arms and Doorkeeper of the Senate.
- Congress: 119
- Bill type: SRES
- Bill number: 13
- Origin chamber: Senate
- Introduced date: 2025-01-03
- Update date: 2025-01-30T18:59:00Z
- Update date including text: 2025-01-30T18:59:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in Senate
- 2025-01-03 - IntroReferral: Introduced in Senate
- 2025-01-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-01-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S8; text: CR S8)
- 2025-01-06 - Floor: Message on Senate action sent to the House.
- Latest action: 2025-01-03: Introduced in Senate

## Actions

- 2025-01-03 - IntroReferral: Introduced in Senate
- 2025-01-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-01-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S8; text: CR S8)
- 2025-01-06 - Floor: Message on Senate action sent to the House.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/13",
    "number": "13",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "A resolution notifying the House of Representatives of the election of a Sergeant at Arms and Doorkeeper of the Senate.",
    "type": "SRES",
    "updateDate": "2025-01-30T18:59:00Z",
    "updateDateIncludingText": "2025-01-30T18:59:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-06",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S8; text: CR S8)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-03",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres13ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 13\nIN THE SENATE OF THE UNITED STATES\nJanuary 3, 2025 Mr. Thune submitted the following resolution; which was considered and agreed to\nRESOLUTION\nNotifying the House of Representatives of the election of a Sergeant at Arms and Doorkeeper of the Senate.\nThat the House of Representatives be notified of the election of the Honorable Jennifer A. Hemingway as Sergeant at Arms and Doorkeeper of the Senate.",
      "versionDate": "2025-01-03",
      "versionType": "ATS"
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
            "name": "Congressional officers and employees",
            "updateDate": "2025-01-15T18:44:59Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-01-15T18:45:15Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-01-15T18:45:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-13T12:55:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119sres13",
          "measure-number": "13",
          "measure-type": "sres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "SENATE",
          "update-date": "2025-01-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres13v00",
            "update-date": "2025-01-30"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution provides for the Senate to notify the House of Representatives of the election of the Honorable Jennifer A. Hemingway as Sergeant at Arms and Doorkeeper of the Senate.</p>"
        },
        "title": "A resolution notifying the House of Representatives of the election of a Sergeant at Arms and Doorkeeper of the Senate."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres13.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution provides for the Senate to notify the House of Representatives of the election of the Honorable Jennifer A. Hemingway as Sergeant at Arms and Doorkeeper of the Senate.</p>",
      "updateDate": "2025-01-30",
      "versionCode": "id119sres13"
    },
    "title": "A resolution notifying the House of Representatives of the election of a Sergeant at Arms and Doorkeeper of the Senate."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution provides for the Senate to notify the House of Representatives of the election of the Honorable Jennifer A. Hemingway as Sergeant at Arms and Doorkeeper of the Senate.</p>",
      "updateDate": "2025-01-30",
      "versionCode": "id119sres13"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres13ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A resolution notifying the House of Representatives of the election of a Sergeant at Arms and Doorkeeper of the Senate.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-04T11:56:16Z"
    },
    {
      "title": "A resolution notifying the House of Representatives of the election of a Sergeant at Arms and Doorkeeper of the Senate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-04T11:56:16Z"
    }
  ]
}
```
