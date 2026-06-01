# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/814?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/814
- Title: A bill to designate the facility of the United States Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, as the "Charles L. Blockson Post Office Building".
- Congress: 119
- Bill type: S
- Bill number: 814
- Origin chamber: Senate
- Introduced date: 2025-03-03
- Update date: 2025-12-10T19:51:43Z
- Update date including text: 2025-12-10T19:51:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in Senate
- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-03-03: Introduced in Senate

## Actions

- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/814",
    "number": "814",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "A bill to designate the facility of the United States Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, as the \"Charles L. Blockson Post Office Building\".",
    "type": "S",
    "updateDate": "2025-12-10T19:51:43Z",
    "updateDateIncludingText": "2025-12-10T19:51:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T21:01:59Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s814is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 814\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2025 Mr. Fetterman introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo designate the facility of the United States Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, as the Charles L. Blockson Post Office Building .\n#### 1. Charles L. Blockson Post Office Building\n##### (a) Designation\nThe facility of the United States Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, shall be known and designated as the Charles L. Blockson Post Office Building .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Charles L. Blockson Post Office Building .",
      "versionDate": "2025-03-03",
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
        "actionDate": "2025-02-27",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "1673",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To designate the facility of the United States Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, as the \"Charles L. Blockson Post Office Building\".",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional tributes",
            "updateDate": "2025-08-13T13:43:23Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-08-13T13:43:23Z"
          },
          {
            "name": "Pennsylvania",
            "updateDate": "2025-08-13T13:43:26Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-08-13T13:43:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-08T13:46:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119s814",
          "measure-number": "814",
          "measure-type": "s",
          "orig-publish-date": "2025-03-03",
          "originChamber": "SENATE",
          "update-date": "2025-12-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s814v00",
            "update-date": "2025-12-10"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill designates the facility of the U.S. Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, as the Charles L. Blockson Post Office Building.</p>"
        },
        "title": "A bill to designate the facility of the United States Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, as the \"Charles L. Blockson Post Office Building\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s814.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill designates the facility of the U.S. Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, as the Charles L. Blockson Post Office Building.</p>",
      "updateDate": "2025-12-10",
      "versionCode": "id119s814"
    },
    "title": "A bill to designate the facility of the United States Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, as the \"Charles L. Blockson Post Office Building\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill designates the facility of the U.S. Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, as the Charles L. Blockson Post Office Building.</p>",
      "updateDate": "2025-12-10",
      "versionCode": "id119s814"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s814is.xml"
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
      "title": "A bill to designate the facility of the United States Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, as the \"Charles L. Blockson Post Office Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:33Z"
    },
    {
      "title": "A bill to designate the facility of the United States Postal Service located at 28 East Airy Street in Norristown, Pennsylvania, as the \"Charles L. Blockson Post Office Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T11:56:20Z"
    }
  ]
}
```
