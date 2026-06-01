# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3630?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3630
- Title: A bill to designate the facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, as the "Firefighter Trevor Brown Post Office Building".
- Congress: 119
- Bill type: S
- Bill number: 3630
- Origin chamber: Senate
- Introduced date: 2026-01-14
- Update date: 2026-04-21T20:33:42Z
- Update date including text: 2026-04-21T20:33:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-14: Introduced in Senate
- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-01-14: Introduced in Senate

## Actions

- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3630",
    "number": "3630",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "A bill to designate the facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, as the \"Firefighter Trevor Brown Post Office Building\".",
    "type": "S",
    "updateDate": "2026-04-21T20:33:42Z",
    "updateDateIncludingText": "2026-04-21T20:33:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-14",
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
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:45:22Z",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3630is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3630\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2026 Mr. Warner (for himself and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo designate the facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, as the Firefighter Trevor Brown Post Office Building .\n#### 1. Firefighter Trevor Brown Post Office Building\n##### (a) Designation\nThe facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, shall be known and designated as the Firefighter Trevor Brown Post Office Building .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Firefighter Trevor Brown Post Office Building .",
      "versionDate": "2026-01-14",
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
      "number": "5058",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To designate the facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, as the \"Firefighter Trevor Brown Post Office Building\".",
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
        "updateDate": "2026-02-10T23:10:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-14",
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
          "measure-id": "id119s3630",
          "measure-number": "3630",
          "measure-type": "s",
          "orig-publish-date": "2026-01-14",
          "originChamber": "SENATE",
          "update-date": "2026-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3630v00",
            "update-date": "2026-02-03"
          },
          "action-date": "2026-01-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, as the \"Firefighter Trevor Brown Post Office Building\"."
        },
        "title": "A bill to designate the facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, as the \"Firefighter Trevor Brown Post Office Building\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3630.xml",
    "summary": {
      "actionDate": "2026-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "This bill designates the facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, as the \"Firefighter Trevor Brown Post Office Building\".",
      "updateDate": "2026-02-03",
      "versionCode": "id119s3630"
    },
    "title": "A bill to designate the facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, as the \"Firefighter Trevor Brown Post Office Building\"."
  },
  "summaries": [
    {
      "actionDate": "2026-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "This bill designates the facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, as the \"Firefighter Trevor Brown Post Office Building\".",
      "updateDate": "2026-02-03",
      "versionCode": "id119s3630"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3630is.xml"
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
      "title": "A bill to designate the facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, as the \"Firefighter Trevor Brown Post Office Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:47Z"
    },
    {
      "title": "A bill to designate the facility of the United States Postal Service located at 46164 Westlake Drive in Sterling, Virginia, as the \"Firefighter Trevor Brown Post Office Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-15T11:56:16Z"
    }
  ]
}
```
