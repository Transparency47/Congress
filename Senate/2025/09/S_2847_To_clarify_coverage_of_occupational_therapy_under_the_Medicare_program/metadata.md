# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2847?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2847
- Title: Occupational Therapy Mental Health Parity Act
- Congress: 119
- Bill type: S
- Bill number: 2847
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2026-01-26T16:33:11Z
- Update date including text: 2026-01-26T16:33:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2847",
    "number": "2847",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Occupational Therapy Mental Health Parity Act",
    "type": "S",
    "updateDate": "2026-01-26T16:33:11Z",
    "updateDateIncludingText": "2026-01-26T16:33:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T20:32:03Z",
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
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2847is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2847\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Ms. Hassan (for herself and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo clarify coverage of occupational therapy under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Occupational Therapy Mental Health Parity Act .\n#### 2. Clarifying coverage of occupational therapy under Medicare\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services shall provide education and outreach to stakeholders about the Medicare Benefit Policy Manual with respect to occupational therapy services furnished to individuals under the Medicare program for the treatment of a substance use or mental health disorder diagnosis using applicable Healthcare Common Procedure Coding System (HCPCS) codes.",
      "versionDate": "2025-09-17",
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
        "actionDate": "2025-06-17",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4037",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Occupational Therapy Mental Health Parity Act.",
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
        "updateDate": "2025-12-16T16:46:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-17",
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
          "measure-id": "id119s2847",
          "measure-number": "2847",
          "measure-type": "s",
          "orig-publish-date": "2025-09-17",
          "originChamber": "SENATE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2847v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-09-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Occupational Therapy Mental Health Parity Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to conduct outreach on Medicare coverage of occupational therapy services to treat substance use or mental health disorders. </p>"
        },
        "title": "Occupational Therapy Mental Health Parity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2847.xml",
    "summary": {
      "actionDate": "2025-09-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Occupational Therapy Mental Health Parity Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to conduct outreach on Medicare coverage of occupational therapy services to treat substance use or mental health disorders. </p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s2847"
    },
    "title": "Occupational Therapy Mental Health Parity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Occupational Therapy Mental Health Parity Act</b></p> <p>This bill requires the Centers for Medicare & Medicaid Services to conduct outreach on Medicare coverage of occupational therapy services to treat substance use or mental health disorders. </p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s2847"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2847is.xml"
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
      "title": "Occupational Therapy Mental Health Parity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Occupational Therapy Mental Health Parity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to clarify coverage of occupational therapy under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T05:48:14Z"
    }
  ]
}
```
