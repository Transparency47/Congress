# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/59?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/59
- Title: An original resolution authorizing expenditures by the Committee on Environment and Public Works.
- Congress: 119
- Bill type: SRES
- Bill number: 59
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2026-05-08T10:56:19Z
- Update date including text: 2026-05-08T10:56:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - Committee: Committee on Environment and Public Works. Committee consideration held. Business Meeting printed. S. Hrg. 119-267.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Original measure reported to Senate by Senator Capito. Without written report.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Original measure reported to Senate by Senator Capito. Without written report.
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S672)
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - Committee: Committee on Environment and Public Works. Committee consideration held. Business Meeting printed. S. Hrg. 119-267.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Original measure reported to Senate by Senator Capito. Without written report.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Original measure reported to Senate by Senator Capito. Without written report.
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S672)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/59",
    "number": "59",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001047",
        "district": "",
        "firstName": "Shelley",
        "fullName": "Sen. Capito, Shelley Moore [R-WV]",
        "lastName": "Capito",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "An original resolution authorizing expenditures by the Committee on Environment and Public Works.",
    "type": "SRES",
    "updateDate": "2026-05-08T10:56:19Z",
    "updateDateIncludingText": "2026-05-08T10:56:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Rules and Administration. (text: CR S672)",
      "type": "IntroReferral"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Original measure reported to Senate by Senator Capito. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Environment and Public Works. Original measure reported to Senate by Senator Capito. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Committee consideration held. Business Meeting printed. S. Hrg. 119-267.",
      "type": "Committee"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T20:14:18Z",
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
        "item": [
          {
            "date": "2025-02-05T20:14:00Z",
            "name": "Reported Original Measure"
          },
          {
            "date": "2025-02-05T17:33:22Z",
            "name": "Markup By"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres59is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 59\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mrs. Capito , from the Committee on Environment and Public Works , reported the following original resolution; which was referred to the Committee on Rules and Administration\nRESOLUTION\nAuthorizing expenditures by the Committee on Environment and Public Works.\n#### 1. General authority\nIn carrying out its powers, duties, and functions under the Standing Rules of the Senate, in accordance with its jurisdiction under rule XXV of the Standing Rules of the Senate, including holding hearings, reporting such hearings, and making investigations as authorized by paragraphs 1 and 8 of rule XXVI of the Standing Rules of the Senate, the Committee on Environment and Public Works (in this resolution referred to as the committee ) is authorized from March 1, 2025, through February 28, 2027, in its discretion, to\u2014\n**(1)**\nmake expenditures from the contingent fund of the Senate;\n**(2)**\nemploy personnel; and\n**(3)**\nwith the prior consent of the Government department or agency concerned and the Committee on Rules and Administration, use on a reimbursable or nonreimbursable basis the services of personnel of any such department or agency.\n#### 2. Expenses\n##### (a) Expenses for period ending September 30, 2025\nThe expenses of the committee for the period March 1, 2025, through September 30, 2025, under this resolution shall not exceed $4,107,247, of which amount\u2014\n**(1)**\nnot to exceed $4,666 may be expended for the procurement of the services of individual consultants, or organizations thereof (as authorized by section 202(i) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4301(i) )); and\n**(2)**\nnot to exceed $1,166 may be expended for the training of the professional staff of the committee (under procedures specified by section 202(j) of that Act).\n##### (b) Expenses for fiscal year 2026 period\nThe expenses of the committee for the period October 1, 2025, through September 30, 2026, under this resolution shall not exceed $7,040,996, of which amount\u2014\n**(1)**\nnot to exceed $8,000 may be expended for the procurement of the services of individual consultants, or organizations thereof (as authorized by section 202(i) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4301(i) )); and\n**(2)**\nnot to exceed $2,000 may be expended for the training of the professional staff of the committee (under procedures specified by section 202(j) of that Act).\n##### (c) Expenses for period ending February 28, 2027\nThe expenses of the committee for the period October 1, 2026, through February 28, 2027, under this resolution shall not exceed $2,933,748, of which amount\u2014\n**(1)**\nnot to exceed $3,334 may be expended for the procurement of the services of individual consultants, or organizations thereof (as authorized by section 202(i) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4301(i) )); and\n**(2)**\nnot to exceed $834 may be expended for the training of the professional staff of the committee (under procedures specified by section 202(j) of that Act).\n#### 3. Expenses and agency contributions\n##### (a) Expenses of the committee\n**(1) In general**\nExcept as provided in paragraph (2), expenses of the committee under this resolution shall be paid from the contingent fund of the Senate upon vouchers approved by the chairman of the committee.\n**(2) Vouchers not required**\nVouchers shall not be required for\u2014\n**(A)**\nthe disbursement of salaries of employees paid at an annual rate;\n**(B)**\nthe payment of telecommunications provided by the Office of the Sergeant at Arms and Doorkeeper;\n**(C)**\nthe payment of stationery supplies purchased through the Keeper of the Stationery;\n**(D)**\npayments to the Postmaster of the Senate;\n**(E)**\nthe payment of metered charges on copying equipment provided by the Office of the Sergeant at Arms and Doorkeeper;\n**(F)**\nthe payment of Senate Recording and Photographic Services; or\n**(G)**\nthe payment of franked and mass mail costs by the Sergeant at Arms and Doorkeeper.\n##### (b) Agency contributions\nThere are authorized to be paid from the appropriations account for Expenses of Inquiries and Investigations of the Senate such sums as may be necessary for agency contributions related to the compensation of employees of the committee\u2014\n**(1)**\nfor the period March 1, 2025, through September 30, 2025;\n**(2)**\nfor the period October 1, 2025, through September 30, 2026; and\n**(3)**\nfor the period October 1, 2026, through February 28, 2027.",
      "versionDate": "2025-02-05",
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
            "name": "Congressional operations and organization",
            "updateDate": "2025-05-15T14:35:53Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-05-15T14:37:01Z"
          },
          {
            "name": "Senate Committee on Environment and Public Works",
            "updateDate": "2025-05-15T14:34:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-05-14T17:51:37Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres59is.xml"
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
      "title": "An original resolution authorizing expenditures by the Committee on Environment and Public Works.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:33Z"
    },
    {
      "title": "An original resolution authorizing expenditures by the Committee on Environment and Public Works.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-07T11:56:45Z"
    }
  ]
}
```
