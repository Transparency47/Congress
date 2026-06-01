# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/24?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/24
- Title: A bill to designate the facility of the United States Postal Service located at 154 First Avenue East in Jerome, Idaho, as the "Representative Maxine Bell Post Office".
- Congress: 119
- Bill type: S
- Bill number: 24
- Origin chamber: Senate
- Introduced date: 2025-01-07
- Update date: 2025-02-24T19:21:47Z
- Update date including text: 2025-02-24T19:21:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in Senate
- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-07: Introduced in Senate

## Actions

- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/24",
    "number": "24",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "A bill to designate the facility of the United States Postal Service located at 154 First Avenue East in Jerome, Idaho, as the \"Representative Maxine Bell Post Office\".",
    "type": "S",
    "updateDate": "2025-02-24T19:21:47Z",
    "updateDateIncludingText": "2025-02-24T19:21:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-07",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:34:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s24is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 24\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2025 Mr. Crapo (for himself and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo designate the facility of the United States Postal Service located at 154 First Avenue East in Jerome, Idaho, as the Representative Maxine Bell Post Office .\n#### 1. Representative Maxine Bell Post Office\n##### (a) Designation\nThe facility of the United States Postal Service located at 154 First Avenue East in Jerome, Idaho, shall be known and designated as the Representative Maxine Bell Post Office .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Representative Maxine Bell Post Office .",
      "versionDate": "2025-01-07",
      "versionType": "Introduced in Senate"
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
            "name": "Congressional tributes",
            "updateDate": "2025-02-24T19:21:39Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-02-24T19:21:47Z"
          },
          {
            "name": "Idaho",
            "updateDate": "2025-02-24T19:21:27Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-02-24T19:21:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-19T15:53:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119s24",
          "measure-number": "24",
          "measure-type": "s",
          "orig-publish-date": "2025-01-07",
          "originChamber": "SENATE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s24v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill designates the facility of the U.S. Postal Service located at 154 First Avenue East in Jerome, Idaho, as the Representative Maxine Bell Post Office.</p>"
        },
        "title": "A bill to designate the facility of the United States Postal Service located at 154 First Avenue East in Jerome, Idaho, as the \"Representative Maxine Bell Post Office\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s24.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill designates the facility of the U.S. Postal Service located at 154 First Avenue East in Jerome, Idaho, as the Representative Maxine Bell Post Office.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119s24"
    },
    "title": "A bill to designate the facility of the United States Postal Service located at 154 First Avenue East in Jerome, Idaho, as the \"Representative Maxine Bell Post Office\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill designates the facility of the U.S. Postal Service located at 154 First Avenue East in Jerome, Idaho, as the Representative Maxine Bell Post Office.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119s24"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s24is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to designate the facility of the United States Postal Service located at 154 First Avenue East in Jerome, Idaho, as the \"Representative Maxine Bell Post Office\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:21Z"
    },
    {
      "title": "A bill to designate the facility of the United States Postal Service located at 154 First Avenue East in Jerome, Idaho, as the \"Representative Maxine Bell Post Office\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-08T11:56:18Z"
    }
  ]
}
```
