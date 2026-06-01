# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/458?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/458
- Title: A resolution extending the enforcement of certain budgetary points of order in the Senate.
- Congress: 119
- Bill type: SRES
- Bill number: 458
- Origin chamber: Senate
- Introduced date: 2025-10-21
- Update date: 2026-04-24T11:37:23Z
- Update date including text: 2026-04-24T11:37:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-21: Introduced in Senate
- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Referred to the Committee on the Budget. (text: CR S7188)
- Latest action: 2025-10-21: Introduced in Senate

## Actions

- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Referred to the Committee on the Budget. (text: CR S7188)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/458",
    "number": "458",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "A resolution extending the enforcement of certain budgetary points of order in the Senate.",
    "type": "SRES",
    "updateDate": "2026-04-24T11:37:23Z",
    "updateDateIncludingText": "2026-04-24T11:37:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "ssbu00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Budget. (text: CR S7188)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-21",
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
          "date": "2025-10-21T15:44:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Budget Committee",
      "systemCode": "ssbu00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres458is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 458\nIN THE SENATE OF THE UNITED STATES\nOctober 21, 2025 Mr. Graham (for himself and Mr. Merkley ) submitted the following resolution; which was referred to the Committee on the Budget\nRESOLUTION\nExtending the enforcement of certain budgetary points of order in the Senate.\n#### 1. Extension of enforcement of budgetary points of order in the Senate\nNotwithstanding any provision of the Congressional Budget Act of 1974 ( 2 U.S.C. 621 et seq. ), subsections (c)(2) and (d)(3) of section 904 of the Congressional Budget Act of 1974 ( 2 U.S.C. 621 note) shall remain in effect for purposes of Senate enforcement through September 30, 2027.",
      "versionDate": "2025-10-21",
      "versionType": "IS"
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
        "actionDate": "2026-04-23",
        "actionTime": "11:56:22",
        "text": "Held at the desk."
      },
      "number": "33",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A concurrent resolution setting forth the congressional budget for the United States Government for fiscal year 2026 and setting forth the appropriate budgetary levels for fiscal years 2027 through 2035.",
      "type": "SCONRES"
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
        "updateDate": "2025-12-09T21:35:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-21",
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
          "measure-id": "id119sres458",
          "measure-number": "458",
          "measure-type": "sres",
          "orig-publish-date": "2025-10-21",
          "originChamber": "SENATE",
          "update-date": "2026-03-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres458v00",
            "update-date": "2026-03-05"
          },
          "action-date": "2025-10-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution extends authorities related to the enforcement of\u00a0several budget points of order in the Senate through FY2027.</p><p>Budget points of order are used to enforce congressional budget procedures and substantive provisions of a congressional budget resolution (e.g., spending allocations). If a Senator successfully raises a budget point of order against legislation, further consideration of the legislation is generally prohibited unless the Senate waives the budget point of order.\u00a0</p><p>A motion to waive most budget points of order in the Senate requires an affirmative vote of three-fifths of all Senators duly chosen and sworn (60 votes if there are no vacancies). This resolution extends provisions that require this three-fifths vote of the Senate to waive several specified budget points of order. \u00a0</p>"
        },
        "title": "A resolution extending the enforcement of certain budgetary points of order in the Senate."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres458.xml",
    "summary": {
      "actionDate": "2025-10-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution extends authorities related to the enforcement of\u00a0several budget points of order in the Senate through FY2027.</p><p>Budget points of order are used to enforce congressional budget procedures and substantive provisions of a congressional budget resolution (e.g., spending allocations). If a Senator successfully raises a budget point of order against legislation, further consideration of the legislation is generally prohibited unless the Senate waives the budget point of order.\u00a0</p><p>A motion to waive most budget points of order in the Senate requires an affirmative vote of three-fifths of all Senators duly chosen and sworn (60 votes if there are no vacancies). This resolution extends provisions that require this three-fifths vote of the Senate to waive several specified budget points of order. \u00a0</p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119sres458"
    },
    "title": "A resolution extending the enforcement of certain budgetary points of order in the Senate."
  },
  "summaries": [
    {
      "actionDate": "2025-10-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution extends authorities related to the enforcement of\u00a0several budget points of order in the Senate through FY2027.</p><p>Budget points of order are used to enforce congressional budget procedures and substantive provisions of a congressional budget resolution (e.g., spending allocations). If a Senator successfully raises a budget point of order against legislation, further consideration of the legislation is generally prohibited unless the Senate waives the budget point of order.\u00a0</p><p>A motion to waive most budget points of order in the Senate requires an affirmative vote of three-fifths of all Senators duly chosen and sworn (60 votes if there are no vacancies). This resolution extends provisions that require this three-fifths vote of the Senate to waive several specified budget points of order. \u00a0</p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119sres458"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres458is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution extending the enforcement of certain budgetary points of order in the Senate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T12:18:11Z"
    },
    {
      "title": "A resolution extending the enforcement of certain budgetary points of order in the Senate.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T10:56:20Z"
    }
  ]
}
```
