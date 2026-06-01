# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3074?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3074
- Title: SNAP BACK Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3074
- Origin chamber: Senate
- Introduced date: 2025-10-29
- Update date: 2025-11-08T12:03:14Z
- Update date including text: 2025-11-08T12:03:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-29: Introduced in Senate
- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-10-29: Introduced in Senate

## Actions

- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-29",
    "latestAction": {
      "actionDate": "2025-10-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3074",
    "number": "3074",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001303",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
        "lastName": "Blunt Rochester",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "SNAP BACK Act of 2025",
    "type": "S",
    "updateDate": "2025-11-08T12:03:14Z",
    "updateDateIncludingText": "2025-11-08T12:03:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-29",
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
          "date": "2025-10-29T20:26:59Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3074is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3074\nIN THE SENATE OF THE UNITED STATES\nOctober 29, 2025 Ms. Blunt Rochester introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo direct the Secretary of Agriculture to reimburse State agencies for costs incurred in carrying out the supplemental nutrition assistance program during a lapse in appropriations.\n#### 1. Short title\nThis Act may be cited as the Supplemental Nutrition Assistance Program Benefits And Compensation for Keep-up Act of 2025 or the SNAP BACK Act of 2025 .\n#### 2. SNAP reimbursement to States\nThe Secretary of Agriculture shall reimburse States for costs incurred in carrying out the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) during a lapse in appropriations for that program, to the extent that the State carried out that program in accordance with Federal law (including regulations) during that lapse.",
      "versionDate": "2025-10-29",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-06T15:03:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-29",
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
          "measure-id": "id119s3074",
          "measure-number": "3074",
          "measure-type": "s",
          "orig-publish-date": "2025-10-29",
          "originChamber": "SENATE",
          "update-date": "2025-11-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3074v00",
            "update-date": "2025-11-06"
          },
          "action-date": "2025-10-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Supplemental Nutrition Assistance Program Benefits And Compensation for Keep-up Act of 2025 or the\u00a0 SNAP BACK Act of 2025</strong></p><p>This bill requires the Department of Agriculture to reimburse states\u00a0for costs incurred to carry out the Supplemental Nutrition Assistance Program (SNAP)\u00a0during a lapse in appropriations for SNAP, to the extent that the state carried out SNAP\u00a0in accordance with federal law (including regulations) during the lapse.</p>"
        },
        "title": "SNAP BACK Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3074.xml",
    "summary": {
      "actionDate": "2025-10-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supplemental Nutrition Assistance Program Benefits And Compensation for Keep-up Act of 2025 or the\u00a0 SNAP BACK Act of 2025</strong></p><p>This bill requires the Department of Agriculture to reimburse states\u00a0for costs incurred to carry out the Supplemental Nutrition Assistance Program (SNAP)\u00a0during a lapse in appropriations for SNAP, to the extent that the state carried out SNAP\u00a0in accordance with federal law (including regulations) during the lapse.</p>",
      "updateDate": "2025-11-06",
      "versionCode": "id119s3074"
    },
    "title": "SNAP BACK Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supplemental Nutrition Assistance Program Benefits And Compensation for Keep-up Act of 2025 or the\u00a0 SNAP BACK Act of 2025</strong></p><p>This bill requires the Department of Agriculture to reimburse states\u00a0for costs incurred to carry out the Supplemental Nutrition Assistance Program (SNAP)\u00a0during a lapse in appropriations for SNAP, to the extent that the state carried out SNAP\u00a0in accordance with federal law (including regulations) during the lapse.</p>",
      "updateDate": "2025-11-06",
      "versionCode": "id119s3074"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3074is.xml"
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
      "title": "SNAP BACK Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-08T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SNAP BACK Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T07:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supplemental Nutrition Assistance Program Benefits And Compensation for Keep-up Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T07:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Agriculture to reimburse State agencies for costs incurred in carrying out the supplemental nutrition assistance program during a lapse in appropriations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T07:48:21Z"
    }
  ]
}
```
