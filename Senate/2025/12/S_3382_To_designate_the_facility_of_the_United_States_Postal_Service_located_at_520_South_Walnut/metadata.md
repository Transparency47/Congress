# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3382?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3382
- Title: A bill to designate the facility of the United States Postal Service located at 520 South Walnut Street in Bloomington, Indiana, as the "Curt Cignetti Post Office".
- Congress: 119
- Bill type: S
- Bill number: 3382
- Origin chamber: Senate
- Introduced date: 2025-12-08
- Update date: 2026-01-07T17:13:40Z
- Update date including text: 2026-01-07T17:13:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-08: Introduced in Senate
- 2025-12-08 - IntroReferral: Introduced in Senate
- 2025-12-08 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-12-08: Introduced in Senate

## Actions

- 2025-12-08 - IntroReferral: Introduced in Senate
- 2025-12-08 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-08",
    "latestAction": {
      "actionDate": "2025-12-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3382",
    "number": "3382",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "A bill to designate the facility of the United States Postal Service located at 520 South Walnut Street in Bloomington, Indiana, as the \"Curt Cignetti Post Office\".",
    "type": "S",
    "updateDate": "2026-01-07T17:13:40Z",
    "updateDateIncludingText": "2026-01-07T17:13:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-08",
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
      "actionDate": "2025-12-08",
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
          "date": "2025-12-08T20:53:59Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3382is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3382\nIN THE SENATE OF THE UNITED STATES\nDecember 8 (legislative day, December 4), 2025 Mr. Banks introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo designate the facility of the United States Postal Service located at 520 South Walnut Street in Bloomington, Indiana, as the Curt Cignetti Post Office .\n#### 1. Curt Cignetti Post Office\n##### (a) Designation\nThe facility of the United States Postal Service located at 520 South Walnut Street in Bloomington, Indiana, shall be known and designated as the Curt Cignetti Post Office .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Curt Cignetti Post Office .",
      "versionDate": "2025-12-08",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-07T17:13:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-08",
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
          "measure-id": "id119s3382",
          "measure-number": "3382",
          "measure-type": "s",
          "orig-publish-date": "2025-12-08",
          "originChamber": "SENATE",
          "update-date": "2025-12-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3382v00",
            "update-date": "2025-12-31"
          },
          "action-date": "2025-12-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 520 South Walnut Street in Bloomington, Indiana, as the \"Curt Cignetti Post Office\"."
        },
        "title": "A bill to designate the facility of the United States Postal Service located at 520 South Walnut Street in Bloomington, Indiana, as the \"Curt Cignetti Post Office\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3382.xml",
    "summary": {
      "actionDate": "2025-12-08",
      "actionDesc": "Introduced in Senate",
      "text": "This bill designates the facility of the United States Postal Service located at 520 South Walnut Street in Bloomington, Indiana, as the \"Curt Cignetti Post Office\".",
      "updateDate": "2025-12-31",
      "versionCode": "id119s3382"
    },
    "title": "A bill to designate the facility of the United States Postal Service located at 520 South Walnut Street in Bloomington, Indiana, as the \"Curt Cignetti Post Office\"."
  },
  "summaries": [
    {
      "actionDate": "2025-12-08",
      "actionDesc": "Introduced in Senate",
      "text": "This bill designates the facility of the United States Postal Service located at 520 South Walnut Street in Bloomington, Indiana, as the \"Curt Cignetti Post Office\".",
      "updateDate": "2025-12-31",
      "versionCode": "id119s3382"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3382is.xml"
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
      "title": "A bill to designate the facility of the United States Postal Service located at 520 South Walnut Street in Bloomington, Indiana, as the \"Curt Cignetti Post Office\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:48:16Z"
    },
    {
      "title": "A bill to designate the facility of the United States Postal Service located at 520 South Walnut Street in Bloomington, Indiana, as the \"Curt Cignetti Post Office\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T11:56:23Z"
    }
  ]
}
```
