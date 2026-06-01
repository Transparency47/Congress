# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4076?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4076
- Title: Removing Medicare Mental Health Inpatient Limitations Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4076
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-04-09T20:46:34Z
- Update date including text: 2026-04-09T20:46:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4076",
    "number": "4076",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Removing Medicare Mental Health Inpatient Limitations Act of 2026",
    "type": "S",
    "updateDate": "2026-04-09T20:46:34Z",
    "updateDateIncludingText": "2026-04-09T20:46:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T16:01:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "ME"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4076is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4076\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Mr. Cassidy (for himself, Ms. Collins , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to eliminate the 190-day lifetime limit on inpatient psychiatric hospital services under the Medicare Program.\n#### 1. Short title\nThis Act may be cited as the Removing Medicare Mental Health Inpatient Limitations Act of 2026 .\n#### 2. Elimination of 190-day lifetime limit on inpatient psychiatric hospital services\n##### (a) In general\nSection 1812 of the Social Security Act ( 42 U.S.C. 1395d ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by adding or at the end;\n**(B)**\nin paragraph (2), by striking ; or at the end and inserting a period; and\n**(C)**\nby striking paragraph (3); and\n**(2)**\nin subsection (c), by striking (but shall not be included and all that follows before the period at the end.\n##### (b) Effective Date\nThe amendments made by subsection (a) shall apply to items and services furnished on or after January 1, 2027.",
      "versionDate": "2026-03-12",
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
        "actionDate": "2025-07-22",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "4619",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Medicare Mental Health Inpatient Equity Act of 2025",
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
        "name": "Health",
        "updateDate": "2026-04-02T18:35:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-12",
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
          "measure-id": "id119s4076",
          "measure-number": "4076",
          "measure-type": "s",
          "orig-publish-date": "2026-03-12",
          "originChamber": "SENATE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4076v00",
            "update-date": "2026-04-09"
          },
          "action-date": "2026-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Removing Medicare Mental Health Inpatient Limitations Act of 2026</strong><strong></strong></p><p>This bill removes the 190-day lifetime limit on inpatient psychiatric hospital services under Medicare.</p>"
        },
        "title": "Removing Medicare Mental Health Inpatient Limitations Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4076.xml",
    "summary": {
      "actionDate": "2026-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Removing Medicare Mental Health Inpatient Limitations Act of 2026</strong><strong></strong></p><p>This bill removes the 190-day lifetime limit on inpatient psychiatric hospital services under Medicare.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119s4076"
    },
    "title": "Removing Medicare Mental Health Inpatient Limitations Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Removing Medicare Mental Health Inpatient Limitations Act of 2026</strong><strong></strong></p><p>This bill removes the 190-day lifetime limit on inpatient psychiatric hospital services under Medicare.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119s4076"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4076is.xml"
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
      "title": "A bill to amend title XVIII of the Social Security Act to eliminate the 190-day lifetime limit on inpatient psychiatric hospital services under the Medicare Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:29Z"
    },
    {
      "title": "Removing Medicare Mental Health Inpatient Limitations Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Removing Medicare Mental Health Inpatient Limitations Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:18Z"
    }
  ]
}
```
