# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1364?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1364
- Title: Supporting American Allies Act
- Congress: 119
- Bill type: S
- Bill number: 1364
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-03-30T15:45:17Z
- Update date including text: 2026-03-30T15:45:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1364",
    "number": "1364",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Supporting American Allies Act",
    "type": "S",
    "updateDate": "2026-03-30T15:45:17Z",
    "updateDateIncludingText": "2026-03-30T15:45:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T18:12:06Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1364is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1364\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Ms. Cortez Masto introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo exempt articles imported from Israel or Ukraine from duties imposed under the Executive Order entitled Regulating Imports with a Reciprocal Tariff to Rectify Trade Practices that Contribute to Large and Persistent Annual United States Goods Trade Deficits .\n#### 1. Short title\nThis Act may be cited as the Supporting American Allies Act .\n#### 2. Exemption of articles from Israel and Ukraine from Executive Order imposing reciprocal tariffs\nThe duties imposed under the Executive Order entitled Regulating Imports with a Reciprocal Tariff to Rectify Trade Practices that Contribute to Large and Persistent Annual United States Goods Trade Deficits shall not apply to any article imported from\u2014\n**(1)**\nIsrael; or\n**(2)**\nUkraine.",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-06-04",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "3727",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting American Allies Act",
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
        "updateDate": "2025-05-22T20:45:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-09",
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
          "measure-id": "id119s1364",
          "measure-number": "1364",
          "measure-type": "s",
          "orig-publish-date": "2025-04-09",
          "originChamber": "SENATE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1364v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Supporting American Allies Act</strong></p><p>This bill exempts articles imported into the United States from Israel or Ukraine from additional tariffs imposed by an April 2, 2025, <a href=\"https://www.govinfo.gov/content/pkg/FR-2025-04-07/pdf/2025-06063.pdf\">executive order</a>.</p><p>On April 2, 2025, President Donald J. Trump signed an executive order imposing an additional 10% tariff on most imports to the United States and additional country-specific tariffs on 57 trading partners (including a 17% tariff on Israel). Therefore, this executive order imposes an additional 10% tariff on imports from Ukraine and an additional 17% tariff on imports from Israel. This bill exempts articles from Israel or Ukraine from these additional tariffs.</p>"
        },
        "title": "Supporting American Allies Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1364.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting American Allies Act</strong></p><p>This bill exempts articles imported into the United States from Israel or Ukraine from additional tariffs imposed by an April 2, 2025, <a href=\"https://www.govinfo.gov/content/pkg/FR-2025-04-07/pdf/2025-06063.pdf\">executive order</a>.</p><p>On April 2, 2025, President Donald J. Trump signed an executive order imposing an additional 10% tariff on most imports to the United States and additional country-specific tariffs on 57 trading partners (including a 17% tariff on Israel). Therefore, this executive order imposes an additional 10% tariff on imports from Ukraine and an additional 17% tariff on imports from Israel. This bill exempts articles from Israel or Ukraine from these additional tariffs.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s1364"
    },
    "title": "Supporting American Allies Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting American Allies Act</strong></p><p>This bill exempts articles imported into the United States from Israel or Ukraine from additional tariffs imposed by an April 2, 2025, <a href=\"https://www.govinfo.gov/content/pkg/FR-2025-04-07/pdf/2025-06063.pdf\">executive order</a>.</p><p>On April 2, 2025, President Donald J. Trump signed an executive order imposing an additional 10% tariff on most imports to the United States and additional country-specific tariffs on 57 trading partners (including a 17% tariff on Israel). Therefore, this executive order imposes an additional 10% tariff on imports from Ukraine and an additional 17% tariff on imports from Israel. This bill exempts articles from Israel or Ukraine from these additional tariffs.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s1364"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1364is.xml"
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
      "title": "Supporting American Allies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting American Allies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to exempt articles imported from Israel or Ukraine from duties imposed under the Executive Order entitled \"Regulating Imports with a Reciprocal Tariff to Rectify Trade Practices that Contribute to Large and Persistent Annual United States Goods Trade Deficits\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:18Z"
    }
  ]
}
```
