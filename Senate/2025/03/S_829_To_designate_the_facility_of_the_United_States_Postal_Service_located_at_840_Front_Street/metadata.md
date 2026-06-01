# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/829?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/829
- Title: A bill to designate the facility of the United States Postal Service located at 840 Front Street in Casselton, North Dakota, as the "Commander Delbert Austin Olson Post Office".
- Congress: 119
- Bill type: S
- Bill number: 829
- Origin chamber: Senate
- Introduced date: 2025-03-04
- Update date: 2025-12-10T19:52:55Z
- Update date including text: 2025-12-10T19:52:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-04: Introduced in Senate
- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-03-04: Introduced in Senate

## Actions

- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/829",
    "number": "829",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "A bill to designate the facility of the United States Postal Service located at 840 Front Street in Casselton, North Dakota, as the \"Commander Delbert Austin Olson Post Office\".",
    "type": "S",
    "updateDate": "2025-12-10T19:52:55Z",
    "updateDateIncludingText": "2025-12-10T19:52:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T17:18:30Z",
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
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s829is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 829\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Mr. Cramer (for himself and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo designate the facility of the United States Postal Service located at 840 Front Street in Casselton, North Dakota, as the Commander Delbert Austin Olson Post Office .\n#### 1. Commander Delbert Austin Olson Post Office\n##### (a) Designation\nThe facility of the United States Postal Service located at 840 Front Street in Casselton, North Dakota, shall be known and designated as the Commander Delbert Austin Olson Post Office .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Commander Delbert Austin Olson Post Office .",
      "versionDate": "2025-03-04",
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
        "actionDate": "2025-12-09",
        "actionTime": "17:23:29",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "1830",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To designate the facility of the United States Postal Service located at 840 Front Street in Casselton, North Dakota, as the \"Commander Delbert Austin Olson Post Office\".",
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
            "updateDate": "2025-08-13T13:43:01Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-08-13T13:43:01Z"
          },
          {
            "name": "North Dakota",
            "updateDate": "2025-08-13T13:43:07Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-08-13T13:43:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-08T13:48:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
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
          "measure-id": "id119s829",
          "measure-number": "829",
          "measure-type": "s",
          "orig-publish-date": "2025-03-04",
          "originChamber": "SENATE",
          "update-date": "2025-12-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s829v00",
            "update-date": "2025-12-10"
          },
          "action-date": "2025-03-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill designates the facility of the U.S. Postal Service located at 840 Front Street in Casselton, North Dakota, as the Commander Delbert Austin Olson Post Office.</p>"
        },
        "title": "A bill to designate the facility of the United States Postal Service located at 840 Front Street in Casselton, North Dakota, as the \"Commander Delbert Austin Olson Post Office\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s829.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill designates the facility of the U.S. Postal Service located at 840 Front Street in Casselton, North Dakota, as the Commander Delbert Austin Olson Post Office.</p>",
      "updateDate": "2025-12-10",
      "versionCode": "id119s829"
    },
    "title": "A bill to designate the facility of the United States Postal Service located at 840 Front Street in Casselton, North Dakota, as the \"Commander Delbert Austin Olson Post Office\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill designates the facility of the U.S. Postal Service located at 840 Front Street in Casselton, North Dakota, as the Commander Delbert Austin Olson Post Office.</p>",
      "updateDate": "2025-12-10",
      "versionCode": "id119s829"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s829is.xml"
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
      "title": "A bill to designate the facility of the United States Postal Service located at 840 Front Street in Casselton, North Dakota, as the \"Commander Delbert Austin Olson Post Office\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:56Z"
    },
    {
      "title": "A bill to designate the facility of the United States Postal Service located at 840 Front Street in Casselton, North Dakota, as the \"Commander Delbert Austin Olson Post Office\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T11:56:19Z"
    }
  ]
}
```
