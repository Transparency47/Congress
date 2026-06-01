# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/175?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/175
- Title: A bill to rescind the unobligated balances of amounts appropriated for Internal Revenue Service enhancements and use such funding for an External Revenue Service.
- Congress: 119
- Bill type: S
- Bill number: 175
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2025-05-27T14:12:54Z
- Update date including text: 2025-05-27T14:12:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/175",
    "number": "175",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "A bill to rescind the unobligated balances of amounts appropriated for Internal Revenue Service enhancements and use such funding for an External Revenue Service.",
    "type": "S",
    "updateDate": "2025-05-27T14:12:54Z",
    "updateDateIncludingText": "2025-05-27T14:12:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
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
          "date": "2025-01-22T00:13:31Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s175is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 175\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mr. Moreno introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo rescind the unobligated balances of amounts appropriated for Internal Revenue Service enhancements and use such funding for an External Revenue Service.\n#### 1. Rescission of enhanced Internal Revenue Service resources\n##### (a) In general\nThere are hereby rescinded all unobligated balances from amounts appropriated or otherwise made available under section 10301 of Public Law 117\u2013169 (commonly known as the Inflation Reduction Act of 2022 ).\n##### (b) Sense of Congress\nIt is the sense of Congress that amounts equal to the amounts rescinded under subsection (a) should be appropriated for the establishment and administration of an External Revenue Service.",
      "versionDate": "2025-01-21",
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
        "name": "Taxation",
        "updateDate": "2025-02-25T20:33:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119s175",
          "measure-number": "175",
          "measure-type": "s",
          "orig-publish-date": "2025-01-21",
          "originChamber": "SENATE",
          "update-date": "2025-04-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s175v00",
            "update-date": "2025-04-16"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Family and Small Business Taxpayer Protection Act </strong></p><p>This bill rescinds unobligated funds that were provided by the Inflation Reduction Act of 2022 to the Internal Revenue Service (IRS)\u00a0for enforcement activities related to the determination and collection of taxes, for taxpayer services, for operations support for taxpayer services and enforcement activities, for business system modernization, and for a task force to research options for a free, direct electronic filing (e-filing) tax return system.\u00a0</p><p>The bill also rescinds unobligated funds that were provided by the Inflation Reduction Act of 2022 for expenses of the</p><ul><li>Treasury Inspector General for Tax Administration,</li><li>Office of Tax Policy,</li><li>U.S. Tax Court, and</li><li>offices within the Department of the Treasury that provide oversight and support for the IRS.</li></ul><p>Finally, the bill expresses the sense of Congress that the rescinded unobligated funds that were appropriated to the IRS by the Inflation Reduction Act of 2022 should be appropriated for the establishment and administration of an External Revenue Service.</p>"
        },
        "title": "A bill to rescind the unobligated balances of amounts appropriated for Internal Revenue Service enhancements and use such funding for an External Revenue Service."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s175.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Family and Small Business Taxpayer Protection Act </strong></p><p>This bill rescinds unobligated funds that were provided by the Inflation Reduction Act of 2022 to the Internal Revenue Service (IRS)\u00a0for enforcement activities related to the determination and collection of taxes, for taxpayer services, for operations support for taxpayer services and enforcement activities, for business system modernization, and for a task force to research options for a free, direct electronic filing (e-filing) tax return system.\u00a0</p><p>The bill also rescinds unobligated funds that were provided by the Inflation Reduction Act of 2022 for expenses of the</p><ul><li>Treasury Inspector General for Tax Administration,</li><li>Office of Tax Policy,</li><li>U.S. Tax Court, and</li><li>offices within the Department of the Treasury that provide oversight and support for the IRS.</li></ul><p>Finally, the bill expresses the sense of Congress that the rescinded unobligated funds that were appropriated to the IRS by the Inflation Reduction Act of 2022 should be appropriated for the establishment and administration of an External Revenue Service.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119s175"
    },
    "title": "A bill to rescind the unobligated balances of amounts appropriated for Internal Revenue Service enhancements and use such funding for an External Revenue Service."
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Family and Small Business Taxpayer Protection Act </strong></p><p>This bill rescinds unobligated funds that were provided by the Inflation Reduction Act of 2022 to the Internal Revenue Service (IRS)\u00a0for enforcement activities related to the determination and collection of taxes, for taxpayer services, for operations support for taxpayer services and enforcement activities, for business system modernization, and for a task force to research options for a free, direct electronic filing (e-filing) tax return system.\u00a0</p><p>The bill also rescinds unobligated funds that were provided by the Inflation Reduction Act of 2022 for expenses of the</p><ul><li>Treasury Inspector General for Tax Administration,</li><li>Office of Tax Policy,</li><li>U.S. Tax Court, and</li><li>offices within the Department of the Treasury that provide oversight and support for the IRS.</li></ul><p>Finally, the bill expresses the sense of Congress that the rescinded unobligated funds that were appropriated to the IRS by the Inflation Reduction Act of 2022 should be appropriated for the establishment and administration of an External Revenue Service.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119s175"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s175is.xml"
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
      "title": "A bill to rescind the unobligated balances of amounts appropriated for Internal Revenue Service enhancements and use such funding for an External Revenue Service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:26Z"
    },
    {
      "title": "A bill to rescind the unobligated balances of amounts appropriated for Internal Revenue Service enhancements and use such funding for an External Revenue Service.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-22T11:56:15Z"
    }
  ]
}
```
