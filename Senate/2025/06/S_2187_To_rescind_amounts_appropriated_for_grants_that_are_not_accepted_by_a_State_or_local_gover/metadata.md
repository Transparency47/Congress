# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2187?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2187
- Title: Pay Down the Debt Act
- Congress: 119
- Bill type: S
- Bill number: 2187
- Origin chamber: Senate
- Introduced date: 2025-06-26
- Update date: 2025-09-09T16:55:57Z
- Update date including text: 2025-09-09T16:55:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-26: Introduced in Senate
- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Appropriations.
- Latest action: 2025-06-26: Introduced in Senate

## Actions

- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2187",
    "number": "2187",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Pay Down the Debt Act",
    "type": "S",
    "updateDate": "2025-09-09T16:55:57Z",
    "updateDateIncludingText": "2025-09-09T16:55:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T20:28:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2187is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2187\nIN THE SENATE OF THE UNITED STATES\nJune 26 (legislative day, June 24), 2025 Ms. Lummis (for herself and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nTo rescind amounts appropriated for grants that are not accepted by a State or local government and use the amounts for deficit reduction.\n#### 1. Short title\nThis Act may be cited as the Pay Down the Debt Act .\n#### 2. Rescission of grant funds not accepted by States and local governments\n##### (a) In general\nIf a State or local government does not accept amounts that are to be awarded to the State or local government under a grant from the Federal Government, an amount equal to the amount to be awarded to the State or local government shall be rescinded from the applicable appropriation account.\n##### (b) Use for deficit reduction\nAmounts rescinded under subsection (a) shall be deposited in the general fund of the Treasury for the sole purpose of deficit reduction.",
      "versionDate": "2025-06-26",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-09-09T15:56:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-26",
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
          "measure-id": "id119s2187",
          "measure-number": "2187",
          "measure-type": "s",
          "orig-publish-date": "2025-06-26",
          "originChamber": "SENATE",
          "update-date": "2025-09-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2187v00",
            "update-date": "2025-09-09"
          },
          "action-date": "2025-06-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Pay Down the Debt Act</strong></p><p>This bill rescinds appropriations that were provided for grants that were not accepted by a state or local government. The rescinded funds must be deposited in the Treasury and used for deficit reduction.</p>"
        },
        "title": "Pay Down the Debt Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2187.xml",
    "summary": {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pay Down the Debt Act</strong></p><p>This bill rescinds appropriations that were provided for grants that were not accepted by a state or local government. The rescinded funds must be deposited in the Treasury and used for deficit reduction.</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119s2187"
    },
    "title": "Pay Down the Debt Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pay Down the Debt Act</strong></p><p>This bill rescinds appropriations that were provided for grants that were not accepted by a state or local government. The rescinded funds must be deposited in the Treasury and used for deficit reduction.</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119s2187"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2187is.xml"
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
      "title": "Pay Down the Debt Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pay Down the Debt Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to rescind amounts appropriated for grants that are not accepted by a State or local government and use the amounts for deficit reduction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T03:33:24Z"
    }
  ]
}
```
