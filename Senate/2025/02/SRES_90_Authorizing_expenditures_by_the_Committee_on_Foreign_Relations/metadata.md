# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/90?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/90
- Title: An original resolution authorizing expenditures by the Committee on Foreign Relations.
- Congress: 119
- Bill type: SRES
- Bill number: 90
- Origin chamber: Senate
- Introduced date: 2025-02-24
- Update date: 2025-05-15T17:34:51Z
- Update date including text: 2025-05-15T17:34:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-24: Introduced in Senate
- 2025-02-24 - Committee: Committee on Foreign Relations. Original measure reported to Senate by Senator Risch. Without written report.
- 2025-02-24 - Committee: Committee on Foreign Relations. Original measure reported to Senate by Senator Risch. Without written report.
- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S1314)
- Latest action: 2025-02-24: Introduced in Senate

## Actions

- 2025-02-24 - Committee: Committee on Foreign Relations. Original measure reported to Senate by Senator Risch. Without written report.
- 2025-02-24 - Committee: Committee on Foreign Relations. Original measure reported to Senate by Senator Risch. Without written report.
- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S1314)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/90",
    "number": "90",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "An original resolution authorizing expenditures by the Committee on Foreign Relations.",
    "type": "SRES",
    "updateDate": "2025-05-15T17:34:51Z",
    "updateDateIncludingText": "2025-05-15T17:34:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Rules and Administration. (text: CR S1314)",
      "type": "IntroReferral"
    },
    {
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Original measure reported to Senate by Senator Risch. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Original measure reported to Senate by Senator Risch. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T20:36:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-24T20:35:46Z",
          "name": "Reported Original Measure"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres90is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 90\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2025 Mr. Risch , from the Committee on Foreign Relations , reported the following original resolution; which was referred to the Committee on Rules and Administration\nRESOLUTION\nAuthorizing expenditures by the Committee on Foreign Relations.\n#### 1. General authority\nIn carrying out its powers, duties, and functions under the Standing Rules of the Senate, in accordance with its jurisdiction under rule XXV of the Standing Rules of the Senate, including holding hearings, reporting such hearings, and making investigations as authorized by paragraphs 1 and 8 of rule XXVI of the Standing Rules of the Senate, the Committee on Foreign Relations (in this resolution referred to as the committee ) is authorized from March 1, 2025, through February 28, 2027, in its discretion, to\u2014\n**(1)**\nmake expenditures from the contingent fund of the Senate;\n**(2)**\nemploy personnel; and\n**(3)**\nwith the prior consent of the Government department or agency concerned and the Committee on Rules and Administration, use on a reimbursable or nonreimbursable basis the services of personnel of any such department or agency.\n#### 2. Expenses\n##### (a) Expenses for period ending September 30, 2025\nThe expenses of the committee for the period March 1, 2025, through September 30, 2025, under this resolution shall not exceed $6,068,289, of which amount\u2014\n**(1)**\nnot to exceed $250,000 may be expended for the procurement of the services of individual consultants, or organizations thereof (as authorized by section 202(i) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4301(i) )); and\n**(2)**\nnot to exceed $30,000 may be expended for the training of the professional staff of the committee (under procedures specified by section 202(j) of that Act).\n##### (b) Expenses for fiscal year 2026 period\nThe expenses of the committee for the period October 1, 2025, through September 30, 2026, under this resolution shall not exceed $10,402,781, of which amount\u2014\n**(1)**\nnot to exceed $250,000 may be expended for the procurement of the services of individual consultants, or organizations thereof (as authorized by section 202(i) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4301(i) )); and\n**(2)**\nnot to exceed $30,000 may be expended for the training of the professional staff of the committee (under procedures specified by section 202(j) of that Act).\n##### (c) Expenses for period ending February 28, 2027\nThe expenses of the committee for the period October 1, 2026, through February 28, 2027, under this resolution shall not exceed $4,334,492, of which amount\u2014\n**(1)**\nnot to exceed $250,000 may be expended for the procurement of the services of individual consultants, or organizations thereof (as authorized by section 202(i) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4301(i) )); and\n**(2)**\nnot to exceed $30,000 may be expended for the training of the professional staff of the committee (under procedures specified by section 202(j) of that Act).\n#### 3. Expenses and agency contributions\n##### (a) Expenses of the committee\n**(1) In general**\nExcept as provided in paragraph (2), expenses of the committee under this resolution shall be paid from the contingent fund of the Senate upon vouchers approved by the chairman of the committee.\n**(2) Vouchers not required**\nVouchers shall not be required for\u2014\n**(A)**\nthe disbursement of salaries of employees paid at an annual rate;\n**(B)**\nthe payment of telecommunications provided by the Office of the Sergeant at Arms and Doorkeeper;\n**(C)**\nthe payment of stationery supplies purchased through the Keeper of the Stationery;\n**(D)**\npayments to the Postmaster of the Senate;\n**(E)**\nthe payment of metered charges on copying equipment provided by the Office of the Sergeant at Arms and Doorkeeper;\n**(F)**\nthe payment of Senate Recording and Photographic Services; or\n**(G)**\nthe payment of franked and mass mail costs by the Sergeant at Arms and Doorkeeper.\n##### (b) Agency contributions\nThere are authorized to be paid from the appropriations account for Expenses of Inquiries and Investigations of the Senate such sums as may be necessary for agency contributions related to the compensation of employees of the committee\u2014\n**(1)**\nfor the period March 1, 2025, through September 30, 2025;\n**(2)**\nfor the period October 1, 2025, through September 30, 2026; and\n**(3)**\nfor the period October 1, 2026, through February 28, 2027.",
      "versionDate": "2025-02-24",
      "versionType": "IS"
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
            "name": "Congressional committees",
            "updateDate": "2025-05-15T17:34:36Z"
          },
          {
            "name": "Senate Committee on Foreign Relations",
            "updateDate": "2025-05-15T17:34:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-05-14T16:18:53Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres90is.xml"
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
      "title": "An original resolution authorizing expenditures by the Committee on Foreign Relations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:18Z"
    },
    {
      "title": "An original resolution authorizing expenditures by the Committee on Foreign Relations.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T11:56:21Z"
    }
  ]
}
```
