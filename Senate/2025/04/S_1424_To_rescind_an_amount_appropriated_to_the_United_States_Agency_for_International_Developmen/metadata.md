# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1424?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1424
- Title: Veterans First Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1424
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-12-05T22:55:44Z
- Update date including text: 2025-12-05T22:55:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1424",
    "number": "1424",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Veterans First Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:55:44Z",
    "updateDateIncludingText": "2025-12-05T22:55:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T17:25:48Z",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1424is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1424\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Tuberville (for himself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo rescind an amount appropriated to the United States Agency for International Development and appropriate such amount to the Department of Veterans Affairs for the construction of State homes for veterans.\n#### 1. Short title\nThis Act may be cited as the Veterans First Act of 2025 .\n#### 2. Funding for grants for construction of State homes for veterans\n##### (a) Rescission\nFrom the unobligated balance of amounts made available to the United States Agency for International Development, $2,000,000,000 is hereby permanently rescinded.\n##### (b) Appropriation\nThere is appropriated to the Department of Veterans Affairs $2,000,000,000 for grants to assist States to acquire or construct State nursing home and domiciliary facilities and to remodel, modify, or alter existing hospital, nursing home, and domiciliary facilities in State homes for purposes of furnishing care to veterans, as authorized by sections 8131 through 8138 of title 38, United States Code, to remain available until expended.",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on Appropriations."
      },
      "number": "2083",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans First Act of 2025",
      "type": "HR"
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-05-09T12:55:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119s1424",
          "measure-number": "1424",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2025-05-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1424v00",
            "update-date": "2025-05-09"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veterans First Act of 2025</strong></p><p>This bill rescinds $2 billion of the unobligated funds that were provided to the U.S. Agency for International Development. It also provides $2 billion in appropriations to the Department of Veterans Affairs for grants to assist states to acquire or construct state nursing home and\u00a0domiciliary facilities\u00a0and to remodel, modify, or alter existing hospital, nursing home, and domiciliary facilities in state homes for furnishing care to veterans,\u00a0</p>"
        },
        "title": "Veterans First Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1424.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans First Act of 2025</strong></p><p>This bill rescinds $2 billion of the unobligated funds that were provided to the U.S. Agency for International Development. It also provides $2 billion in appropriations to the Department of Veterans Affairs for grants to assist states to acquire or construct state nursing home and\u00a0domiciliary facilities\u00a0and to remodel, modify, or alter existing hospital, nursing home, and domiciliary facilities in state homes for furnishing care to veterans,\u00a0</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119s1424"
    },
    "title": "Veterans First Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans First Act of 2025</strong></p><p>This bill rescinds $2 billion of the unobligated funds that were provided to the U.S. Agency for International Development. It also provides $2 billion in appropriations to the Department of Veterans Affairs for grants to assist states to acquire or construct state nursing home and\u00a0domiciliary facilities\u00a0and to remodel, modify, or alter existing hospital, nursing home, and domiciliary facilities in state homes for furnishing care to veterans,\u00a0</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119s1424"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1424is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Veterans First Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans First Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to rescind an amount appropriated to the United States Agency for International Development and appropriate such amount to the Department of Veterans Affairs for the construction of State homes for veterans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:32Z"
    }
  ]
}
```
