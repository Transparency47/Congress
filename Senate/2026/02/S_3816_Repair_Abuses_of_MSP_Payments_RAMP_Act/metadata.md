# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3816?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3816
- Title: Repair Abuses of MSP Payments (RAMP) Act
- Congress: 119
- Bill type: S
- Bill number: 3816
- Origin chamber: Senate
- Introduced date: 2026-02-10
- Update date: 2026-03-30T20:17:07Z
- Update date including text: 2026-03-30T20:17:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-10: Introduced in Senate
- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-10: Introduced in Senate

## Actions

- 2026-02-10 - IntroReferral: Introduced in Senate
- 2026-02-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3816",
    "number": "3816",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Repair Abuses of MSP Payments (RAMP) Act",
    "type": "S",
    "updateDate": "2026-03-30T20:17:07Z",
    "updateDateIncludingText": "2026-03-30T20:17:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T19:27:20Z",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3816is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3816\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2026 Mr. Scott of South Carolina (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to permit a private cause of action for damages in the case of a group health plan which fails to provide for primary payment or appropriate reimbursement.\n#### 1. Short title\nThis Act may be cited as the Repair Abuses of MSP Payments (RAMP) Act .\n#### 2. Private cause of action for damages in the case of a group health plan which fails to provide for primary payment or appropriate reimbursement\nSection 1862(b)(3)(A) of the Social Security Act ( 42 U.S.C. 1395y(b)(3)(A) ) is amended by striking primary plan and inserting group health plan (as defined in paragraph (1)(A)(v)) .",
      "versionDate": "2026-02-10",
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
        "actionDate": "2025-06-20",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4056",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RAMP Act",
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
        "updateDate": "2026-02-27T19:11:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-10",
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
          "measure-id": "id119s3816",
          "measure-number": "3816",
          "measure-type": "s",
          "orig-publish-date": "2026-02-10",
          "originChamber": "SENATE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3816v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2026-02-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Repair Abuses of MSP Payments (RAMP) Act</strong></p><p>This bill restricts the private right of action against insurance plans that do not provide appropriate primary payment in cases in which Medicare is a secondary payer.</p><p>Current law allows for a private right of action against primary plans that do not provide appropriate primary payment in cases in which Medicare is a secondary payer; this provision applies to group health plans, workers' compensation plans, automobile or liability insurance plans, and no-fault insurance plans. The bill limits this provision to group health plans.</p>"
        },
        "title": "Repair Abuses of MSP Payments (RAMP) Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3816.xml",
    "summary": {
      "actionDate": "2026-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Repair Abuses of MSP Payments (RAMP) Act</strong></p><p>This bill restricts the private right of action against insurance plans that do not provide appropriate primary payment in cases in which Medicare is a secondary payer.</p><p>Current law allows for a private right of action against primary plans that do not provide appropriate primary payment in cases in which Medicare is a secondary payer; this provision applies to group health plans, workers' compensation plans, automobile or liability insurance plans, and no-fault insurance plans. The bill limits this provision to group health plans.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s3816"
    },
    "title": "Repair Abuses of MSP Payments (RAMP) Act"
  },
  "summaries": [
    {
      "actionDate": "2026-02-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Repair Abuses of MSP Payments (RAMP) Act</strong></p><p>This bill restricts the private right of action against insurance plans that do not provide appropriate primary payment in cases in which Medicare is a secondary payer.</p><p>Current law allows for a private right of action against primary plans that do not provide appropriate primary payment in cases in which Medicare is a secondary payer; this provision applies to group health plans, workers' compensation plans, automobile or liability insurance plans, and no-fault insurance plans. The bill limits this provision to group health plans.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s3816"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3816is.xml"
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
      "title": "Repair Abuses of MSP Payments (RAMP) Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Repair Abuses of MSP Payments (RAMP) Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to permit a private cause of action for damages in the case of a group health plan which fails to provide for primary payment or appropriate reimbursement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T04:48:25Z"
    }
  ]
}
```
