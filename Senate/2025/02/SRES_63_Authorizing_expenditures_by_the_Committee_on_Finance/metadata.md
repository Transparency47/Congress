# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/63?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/63
- Title: An original resolution authorizing expenditures by the Committee on Finance.
- Congress: 119
- Bill type: SRES
- Bill number: 63
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-05-01T13:40:38Z
- Update date including text: 2025-05-01T13:40:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - Committee: Committee on Finance. Original measure reported to Senate by Senator Crapo. Without written report.
- 2025-02-06 - Committee: Committee on Finance. Original measure reported to Senate by Senator Crapo. Without written report.
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S798)
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - Committee: Committee on Finance. Original measure reported to Senate by Senator Crapo. Without written report.
- 2025-02-06 - Committee: Committee on Finance. Original measure reported to Senate by Senator Crapo. Without written report.
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S798)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/63",
    "number": "63",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "An original resolution authorizing expenditures by the Committee on Finance.",
    "type": "SRES",
    "updateDate": "2025-05-01T13:40:38Z",
    "updateDateIncludingText": "2025-05-01T13:40:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Rules and Administration. (text: CR S798)",
      "type": "IntroReferral"
    },
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Finance. Original measure reported to Senate by Senator Crapo. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Finance. Original measure reported to Senate by Senator Crapo. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T19:19:54Z",
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
          "date": "2025-02-06T19:19:02Z",
          "name": "Reported Original Measure"
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres63is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 63\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Crapo , from the Committee on Finance , reported the following original resolution; which was referred to the Committee on Rules and Administration\nRESOLUTION\nAuthorizing expenditures by the Committee on Finance.\n#### 1. General authority\nIn carrying out its powers, duties, and functions under the Standing Rules of the Senate, in accordance with its jurisdiction under rule XXV of the Standing Rules of the Senate, including holding hearings, reporting such hearings, and making investigations as authorized by paragraphs 1 and 8 of rule XXVI of the Standing Rules of the Senate, the Committee on Finance (in this resolution referred to as the committee ) is authorized from March 1, 2025, through February 28, 2027, in its discretion, to\u2014\n**(1)**\nmake expenditures from the contingent fund of the Senate;\n**(2)**\nemploy personnel; and\n**(3)**\nwith the prior consent of the Government department or agency concerned and the Committee on Rules and Administration, use on a reimbursable or nonreimbursable basis the services of personnel of any such department or agency.\n#### 2. Expenses\n##### (a) Expenses for period ending September 30, 2025\nThe expenses of the committee for the period March 1, 2025, through September 30, 2025, under this resolution shall not exceed $7,638,723, of which amount\u2014\n**(1)**\nnot to exceed $17,500 may be expended for the procurement of the services of individual consultants, or organizations thereof (as authorized by section 202(i) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4301(i) )); and\n**(2)**\nnot to exceed $5,833 may be expended for the training of the professional staff of the committee (under procedures specified by section 202(j) of that Act).\n##### (b) Expenses for fiscal year 2026 period\nThe expenses of the committee for the period October 1, 2025, through September 30, 2026, under this resolution shall not exceed $13,094,954, of which amount\u2014\n**(1)**\nnot to exceed $30,000 may be expended for the procurement of the services of individual consultants, or organizations thereof (as authorized by section 202(i) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4301(i) )); and\n**(2)**\nnot to exceed $10,000 may be expended for the training of the professional staff of the committee (under procedures specified by section 202(j) of that Act).\n##### (c) Expenses for period ending February 28, 2027\nThe expenses of the committee for the period October 1, 2026, through February 28, 2027, under this resolution shall not exceed $5,456,231, of which amount\u2014\n**(1)**\nnot to exceed $12,500 may be expended for the procurement of the services of individual consultants, or organizations thereof (as authorized by section 202(i) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4301(i) )); and\n**(2)**\nnot to exceed $4,166 may be expended for the training of the professional staff of the committee (under procedures specified by section 202(j) of that Act).\n#### 3. Expenses and agency contributions\n##### (a) Expenses of the committee\n**(1) In general**\nExcept as provided in paragraph (2), expenses of the committee under this resolution shall be paid from the contingent fund of the Senate upon vouchers approved by the chairman of the committee.\n**(2) Vouchers not required**\nVouchers shall not be required for\u2014\n**(A)**\nthe disbursement of salaries of employees paid at an annual rate;\n**(B)**\nthe payment of telecommunications provided by the Office of the Sergeant at Arms and Doorkeeper;\n**(C)**\nthe payment of stationery supplies purchased through the Keeper of the Stationery;\n**(D)**\npayments to the Postmaster of the Senate;\n**(E)**\nthe payment of metered charges on copying equipment provided by the Office of the Sergeant at Arms and Doorkeeper;\n**(F)**\nthe payment of Senate Recording and Photographic Services; or\n**(G)**\nthe payment of franked and mass mail costs by the Sergeant at Arms and Doorkeeper.\n##### (b) Agency contributions\nThere are authorized to be paid from the appropriations account for Expenses of Inquiries and Investigations of the Senate such sums as may be necessary for agency contributions related to the compensation of employees of the committee\u2014\n**(1)**\nfor the period March 1, 2025, through September 30, 2025;\n**(2)**\nfor the period October 1, 2025, through September 30, 2026; and\n**(3)**\nfor the period October 1, 2026, through February 28, 2027.",
      "versionDate": "2025-02-06",
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
            "updateDate": "2025-02-24T19:47:36Z"
          },
          {
            "name": "Senate Committee on Finance",
            "updateDate": "2025-02-24T19:47:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-21T14:49:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119sres63",
          "measure-number": "63",
          "measure-type": "sres",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-05-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres63v00",
            "update-date": "2025-05-01"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution authorizes the Senate Committee on Finance to make specified expenditures and employ personnel for the 119th Congress.</p>"
        },
        "title": "An original resolution authorizing expenditures by the Committee on Finance."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres63.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution authorizes the Senate Committee on Finance to make specified expenditures and employ personnel for the 119th Congress.</p>",
      "updateDate": "2025-05-01",
      "versionCode": "id119sres63"
    },
    "title": "An original resolution authorizing expenditures by the Committee on Finance."
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution authorizes the Senate Committee on Finance to make specified expenditures and employ personnel for the 119th Congress.</p>",
      "updateDate": "2025-05-01",
      "versionCode": "id119sres63"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres63is.xml"
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
      "title": "An original resolution authorizing expenditures by the Committee on Finance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:28Z"
    },
    {
      "title": "An original resolution authorizing expenditures by the Committee on Finance.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-07T11:56:28Z"
    }
  ]
}
```
