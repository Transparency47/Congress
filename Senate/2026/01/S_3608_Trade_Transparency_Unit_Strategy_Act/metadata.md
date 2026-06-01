# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3608?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3608
- Title: Trade Transparency Unit Strategy Act
- Congress: 119
- Bill type: S
- Bill number: 3608
- Origin chamber: Senate
- Introduced date: 2026-01-08
- Update date: 2026-05-27T18:01:57Z
- Update date including text: 2026-05-27T18:01:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-08: Introduced in Senate
- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-08: Introduced in Senate

## Actions

- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3608",
    "number": "3608",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Trade Transparency Unit Strategy Act",
    "type": "S",
    "updateDate": "2026-05-27T18:01:57Z",
    "updateDateIncludingText": "2026-05-27T18:01:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-08",
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
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T20:29:49Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3608is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3608\nIN THE SENATE OF THE UNITED STATES\nJanuary 8 (legislative day, January 7), 2026 Mr. Sheehy introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require a strategy for the expanded use of Trade Transparency Units.\n#### 1. Short title\nThis Act may be cited as the Trade Transparency Unit Strategy Act .\n#### 2. Strategy for the expansion of Trade Transparency Units\n##### (a) Sense of Congress\nIt is the sense of Congress that Trade Transparency Units are a critical bilateral and multilateral tool to identify, disrupt, and dismantle international money laundering networks.\n##### (b) Strategy\n**(1) In General**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Homeland Security, in coordination with the Secretary of State, the Secretary of Commerce, and the Secretary of the Treasury, shall submit to the appropriate congressional committees a strategy to\u2014\n**(A)**\nexpand information sharing between U.S. Customs and Border Protection, Homeland Security Investigations, appropriate elements of the Department of Commerce, the Financial Crimes Enforcement Network of the Department of the Treasury, and appropriate counterparts of foreign customs agencies through Trade Transparency Units; and\n**(B)**\nimprove intra-agency, inter-agency, and other multilateral information-sharing with respect to Trade Transparency Units.\n**(2) Form**\nThe strategy required by paragraph (1) shall be submitted in unclassified form and may contain a classified annex.\n##### (c) Comptroller General assessment\nNot later than 180 days after the submission of the strategy required by subsection (b), the Comptroller General of the United States shall submit to the appropriate congressional committees a report that includes an assessment of the strategy required by subsection (b).\n##### (d) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Homeland Security, the Committee on Foreign Affairs, and the Committee on Ways and Means of the House of Representatives; and\n**(2)**\nthe Committee on Homeland Security and Governmental Affairs, the Committee on Finance, and the Committee on Foreign Relations of the Senate.",
      "versionDate": "2026-01-08",
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
        "actionDate": "2026-01-08",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "6988",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Trade Transparency Unit Strategy Act",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-01-26T17:16:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-08",
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
          "measure-id": "id119s3608",
          "measure-number": "3608",
          "measure-type": "s",
          "orig-publish-date": "2026-01-08",
          "originChamber": "SENATE",
          "update-date": "2026-05-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3608v00",
            "update-date": "2026-05-27"
          },
          "action-date": "2026-01-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Trade Transparency Unit Strategy Act</strong></p><p>This bill requires a strategy and report related to the expansion of trade transparency units. Trade transparency units examine trade anomalies and financial irregularities associated with trade-based money laundering, customs fraud, contraband smuggling, and tax evasion.</p><p>Specifically, the Department of Homeland Security must coordinate with the Departments of State, Commerce, and the Treasury to submit a strategy to Congress. This strategy must (1) expand information sharing between U.S. Customs and Border Protection, Homeland Security Investigations of U.S. Immigration and Customs Enforcement, appropriate elements of the Department of Commerce, the Financial Crimes Enforcement Network of the Department of the Treasury, and appropriate counterparts of foreign customs agencies through trade transparency units; and (2) improve\u00a0intra-agency, interagency, and other multilateral information sharing with respect to these units.</p><p>The Government Accountability Office must submit a report to Congress that includes an assessment of the strategy.</p>"
        },
        "title": "Trade Transparency Unit Strategy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3608.xml",
    "summary": {
      "actionDate": "2026-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Trade Transparency Unit Strategy Act</strong></p><p>This bill requires a strategy and report related to the expansion of trade transparency units. Trade transparency units examine trade anomalies and financial irregularities associated with trade-based money laundering, customs fraud, contraband smuggling, and tax evasion.</p><p>Specifically, the Department of Homeland Security must coordinate with the Departments of State, Commerce, and the Treasury to submit a strategy to Congress. This strategy must (1) expand information sharing between U.S. Customs and Border Protection, Homeland Security Investigations of U.S. Immigration and Customs Enforcement, appropriate elements of the Department of Commerce, the Financial Crimes Enforcement Network of the Department of the Treasury, and appropriate counterparts of foreign customs agencies through trade transparency units; and (2) improve\u00a0intra-agency, interagency, and other multilateral information sharing with respect to these units.</p><p>The Government Accountability Office must submit a report to Congress that includes an assessment of the strategy.</p>",
      "updateDate": "2026-05-27",
      "versionCode": "id119s3608"
    },
    "title": "Trade Transparency Unit Strategy Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Trade Transparency Unit Strategy Act</strong></p><p>This bill requires a strategy and report related to the expansion of trade transparency units. Trade transparency units examine trade anomalies and financial irregularities associated with trade-based money laundering, customs fraud, contraband smuggling, and tax evasion.</p><p>Specifically, the Department of Homeland Security must coordinate with the Departments of State, Commerce, and the Treasury to submit a strategy to Congress. This strategy must (1) expand information sharing between U.S. Customs and Border Protection, Homeland Security Investigations of U.S. Immigration and Customs Enforcement, appropriate elements of the Department of Commerce, the Financial Crimes Enforcement Network of the Department of the Treasury, and appropriate counterparts of foreign customs agencies through trade transparency units; and (2) improve\u00a0intra-agency, interagency, and other multilateral information sharing with respect to these units.</p><p>The Government Accountability Office must submit a report to Congress that includes an assessment of the strategy.</p>",
      "updateDate": "2026-05-27",
      "versionCode": "id119s3608"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3608is.xml"
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
      "title": "Trade Transparency Unit Strategy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-24T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Trade Transparency Unit Strategy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-24T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a strategy for the expanded use of Trade Transparency Units.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-24T03:48:21Z"
    }
  ]
}
```
