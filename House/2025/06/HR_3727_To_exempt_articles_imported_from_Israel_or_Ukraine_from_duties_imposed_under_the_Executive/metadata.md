# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3727?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3727
- Title: Supporting American Allies Act
- Congress: 119
- Bill type: HR
- Bill number: 3727
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2026-03-30T16:25:33Z
- Update date including text: 2026-03-30T16:25:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3727",
    "number": "3727",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Supporting American Allies Act",
    "type": "HR",
    "updateDate": "2026-03-30T16:25:33Z",
    "updateDateIncludingText": "2026-03-30T16:25:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-06-04T14:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NJ"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3727ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3727\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mr. Moskowitz (for himself, Mrs. Cherfilus-McCormick , Mr. Gottheimer , and Mr. Goldman of New York ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo exempt articles imported from Israel or Ukraine from duties imposed under the Executive Order entitled Regulating Imports with a Reciprocal Tariff to Rectify Trade Practices that Contribute to Large and Persistent Annual United States Goods Trade Deficits .\n#### 1. Short title\nThis Act may be cited as the Supporting American Allies Act .\n#### 2. Exemption of articles from Israel and Ukraine from Executive Order imposing reciprocal tariffs\nThe duties imposed under the Executive Order entitled Regulating Imports with a Reciprocal Tariff to Rectify Trade Practices that Contribute to Large and Persistent Annual United States Goods Trade Deficits shall not apply to any article imported from\u2014\n**(1)**\nIsrael; or\n**(2)**\nUkraine.",
      "versionDate": "2025-06-04",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-04-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1364",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting American Allies Act",
      "type": "S"
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
        "updateDate": "2025-07-15T17:45:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-04",
    "originChamber": "House",
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
          "measure-id": "id119hr3727",
          "measure-number": "3727",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-04",
          "originChamber": "HOUSE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3727v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-06-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supporting American Allies Act</strong></p><p>This bill exempts articles imported into the United States from Israel or Ukraine from additional tariffs imposed by an April 2, 2025, <a href=\"https://www.govinfo.gov/content/pkg/FR-2025-04-07/pdf/2025-06063.pdf\">executive order</a>.</p><p>On April 2, 2025, President Donald J. Trump signed an executive order imposing an additional 10% tariff on most imports to the United States and additional country-specific tariffs on 57 trading partners (including a 17% tariff on Israel). Therefore, this executive order imposes an additional 10% tariff on imports from Ukraine and an additional 17% tariff on imports from Israel. This bill exempts articles from Israel or Ukraine from these additional tariffs.</p>"
        },
        "title": "Supporting American Allies Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3727.xml",
    "summary": {
      "actionDate": "2025-06-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting American Allies Act</strong></p><p>This bill exempts articles imported into the United States from Israel or Ukraine from additional tariffs imposed by an April 2, 2025, <a href=\"https://www.govinfo.gov/content/pkg/FR-2025-04-07/pdf/2025-06063.pdf\">executive order</a>.</p><p>On April 2, 2025, President Donald J. Trump signed an executive order imposing an additional 10% tariff on most imports to the United States and additional country-specific tariffs on 57 trading partners (including a 17% tariff on Israel). Therefore, this executive order imposes an additional 10% tariff on imports from Ukraine and an additional 17% tariff on imports from Israel. This bill exempts articles from Israel or Ukraine from these additional tariffs.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr3727"
    },
    "title": "Supporting American Allies Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting American Allies Act</strong></p><p>This bill exempts articles imported into the United States from Israel or Ukraine from additional tariffs imposed by an April 2, 2025, <a href=\"https://www.govinfo.gov/content/pkg/FR-2025-04-07/pdf/2025-06063.pdf\">executive order</a>.</p><p>On April 2, 2025, President Donald J. Trump signed an executive order imposing an additional 10% tariff on most imports to the United States and additional country-specific tariffs on 57 trading partners (including a 17% tariff on Israel). Therefore, this executive order imposes an additional 10% tariff on imports from Ukraine and an additional 17% tariff on imports from Israel. This bill exempts articles from Israel or Ukraine from these additional tariffs.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr3727"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3727ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "updateDate": "2025-06-11T09:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting American Allies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T09:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To exempt articles imported from Israel or Ukraine from duties imposed under the Executive Order entitled \"Regulating Imports with a Reciprocal Tariff to Rectify Trade Practices that Contribute to Large and Persistent Annual United States Goods Trade Deficits\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T09:33:25Z"
    }
  ]
}
```
