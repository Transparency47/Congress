# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3444?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3444
- Title: A bill to designate the facility of the United States Postal Service at 1300 East Northwest Highway in Palatine, Illinois, as the "Bernie Bluestein Post Office Building".
- Congress: 119
- Bill type: S
- Bill number: 3444
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-04-21T20:34:50Z
- Update date including text: 2026-04-21T20:34:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S8672)
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S8672)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3444",
    "number": "3444",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "A bill to designate the facility of the United States Postal Service at 1300 East Northwest Highway in Palatine, Illinois, as the \"Bernie Bluestein Post Office Building\".",
    "type": "S",
    "updateDate": "2026-04-21T20:34:50Z",
    "updateDateIncludingText": "2026-04-21T20:34:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S8672)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T18:42:35Z",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3444is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3444\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Durbin (for himself and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo designate the facility of the United States Postal Service at 1300 East Northwest Highway in Palatine, Illinois, as the Bernie Bluestein Post Office Building .\n#### 1. Bernie Bluestein Post Office Building\n##### (a) Designation\nThe facility of the United States Postal Service located at 1300 East Northwest Highway in Palatine, Illinois, shall be known and designated as the Bernie Bluestein Post Office Building .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Bernie Bluestein Post Office Building .",
      "versionDate": "2025-12-11",
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
        "actionDate": "2026-04-15",
        "text": "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "5773",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To designate the facility of the United States Postal Service at 1300 East Northwest Highway in Palatine, Illinois, as the \"Bernie Bluestein Post Office Building\".",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-07T17:14:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-11",
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
          "measure-id": "id119s3444",
          "measure-number": "3444",
          "measure-type": "s",
          "orig-publish-date": "2025-12-11",
          "originChamber": "SENATE",
          "update-date": "2026-01-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3444v00",
            "update-date": "2026-01-06"
          },
          "action-date": "2025-12-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "This bill designates the facility of the United States Postal Service at 1300 East Northwest Highway in Palatine, Illinois, as the \"Bernie Bluestein Post Office Building\"."
        },
        "title": "A bill to designate the facility of the United States Postal Service at 1300 East Northwest Highway in Palatine, Illinois, as the \"Bernie Bluestein Post Office Building\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3444.xml",
    "summary": {
      "actionDate": "2025-12-11",
      "actionDesc": "Introduced in Senate",
      "text": "This bill designates the facility of the United States Postal Service at 1300 East Northwest Highway in Palatine, Illinois, as the \"Bernie Bluestein Post Office Building\".",
      "updateDate": "2026-01-06",
      "versionCode": "id119s3444"
    },
    "title": "A bill to designate the facility of the United States Postal Service at 1300 East Northwest Highway in Palatine, Illinois, as the \"Bernie Bluestein Post Office Building\"."
  },
  "summaries": [
    {
      "actionDate": "2025-12-11",
      "actionDesc": "Introduced in Senate",
      "text": "This bill designates the facility of the United States Postal Service at 1300 East Northwest Highway in Palatine, Illinois, as the \"Bernie Bluestein Post Office Building\".",
      "updateDate": "2026-01-06",
      "versionCode": "id119s3444"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3444is.xml"
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
      "title": "A bill to designate the facility of the United States Postal Service at 1300 East Northwest Highway in Palatine, Illinois, as the \"Bernie Bluestein Post Office Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:19Z"
    },
    {
      "title": "A bill to designate the facility of the United States Postal Service at 1300 East Northwest Highway in Palatine, Illinois, as the \"Bernie Bluestein Post Office Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T11:56:20Z"
    }
  ]
}
```
