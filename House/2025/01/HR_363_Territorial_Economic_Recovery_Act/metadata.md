# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/363?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/363
- Title: Territorial Economic Recovery Act
- Congress: 119
- Bill type: HR
- Bill number: 363
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2026-04-29T19:18:00Z
- Update date including text: 2026-04-29T19:18:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/363",
    "number": "363",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000610",
        "district": "",
        "firstName": "Stacey",
        "fullName": "Del. Plaskett, Stacey E. [D-VI]",
        "lastName": "Plaskett",
        "party": "D",
        "state": "VI"
      }
    ],
    "title": "Territorial Economic Recovery Act",
    "type": "HR",
    "updateDate": "2026-04-29T19:18:00Z",
    "updateDateIncludingText": "2026-04-29T19:18:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:00:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr363ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 363\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Ms. Plaskett introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude certain amounts from the tested income of controlled foreign corporations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Territorial Economic Recovery Act .\n#### 2. Income of certain qualified possession corporations excluded from tested income\n##### (a) In general\nSection 951A of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (c)(2)(A)(i), by striking and at the end of subclause (IV), by striking over at the end of subclause (V) and inserting and , and by adding at the end the following new subclause:\n(VI) any income of a qualified possession corporation that is effectively connected with the active conduct of a trade or business within a possession of the United States, over ; and\n**(2)**\nby adding at the end the following new subsections:\n(g) Possession of the united states For purposes of this section, the term possession of the United States means Puerto Rico, the Virgin Islands, and any specified possession described in section 931(c). (h) Qualified possession corporation For purposes of this section, the term qualified possession corporation means any controlled foreign corporation for any taxable year, if, for the 3-year period (or the period during which the controlled foreign corporation has been in existence, if shorter) ending in the taxable year preceding the taxable year in which the determination is made\u2014 (1) 80 percent or more of the gross income of such corporation was derived from sources within a possession of the United States, and (2) 75 percent or more of the gross income of such corporation was effectively connected with the active conduct of a trade or business within a possession of the United States. .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years of foreign corporations beginning after December 31, 2023, and to taxable years of United States shareholders in which or with which such taxable years of foreign corporations end.",
      "versionDate": "2025-01-13",
      "versionType": "Introduced in House"
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
            "name": "American Samoa",
            "updateDate": "2025-03-19T20:25:14Z"
          },
          {
            "name": "Guam",
            "updateDate": "2025-03-19T20:25:14Z"
          },
          {
            "name": "Income tax exclusion",
            "updateDate": "2025-03-19T20:25:14Z"
          },
          {
            "name": "Northern Mariana Islands",
            "updateDate": "2025-03-19T20:25:14Z"
          },
          {
            "name": "Puerto Rico",
            "updateDate": "2025-03-19T20:25:14Z"
          },
          {
            "name": "Taxation of foreign income",
            "updateDate": "2025-03-19T20:25:14Z"
          },
          {
            "name": "U.S. territories and protectorates",
            "updateDate": "2025-03-19T20:25:14Z"
          },
          {
            "name": "Virgin Islands",
            "updateDate": "2025-03-19T20:25:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-14T18:46:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr363",
          "measure-number": "363",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2026-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr363v00",
            "update-date": "2026-04-29"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Territorial Economic Recovery Act</strong></p><p>This bill excludes the income of certain controlled foreign corporations in U.S. territories from the calculation of global intangible low-taxed income (GILTI) for federal tax purposes.</p><p>Under current law, a U.S. shareholder of a controlled foreign corporation is required to include in gross income the GILTI of the shareholder. The calculation of GILTI is based, in part, on the controlled foreign corporation\u2019s tested income (the controlled foreign corporation\u2019s gross income less certain exclusions).</p><p>Under the bill, the income from a qualified possession corporation that is effectively connected with an active trade or business within a U.S. territory (Puerto Rico, U.S. Virgin Islands, Guam, American Samoa, and the Northern Mariana Islands) is excluded from gross income for purposes of calculating a controlled foreign corporation\u2019s tested income.</p><p>The bill defines a\u00a0<em>qualified possession corporation</em> as any controlled foreign corporation if, for a three-year period ending in the prior tax year (or for the existence of the controlled foreign corporation if less than three years)\u00a0(1) 80% or more of the controlled foreign corporation\u2019s gross income was derived from a U.S. territory, and (2) 75% or more of the controlled foreign corporation\u2019s gross income was\u00a0effectively connected to the active conduct of a trade or business within a U.S. territory.</p>"
        },
        "title": "Territorial Economic Recovery Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr363.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Territorial Economic Recovery Act</strong></p><p>This bill excludes the income of certain controlled foreign corporations in U.S. territories from the calculation of global intangible low-taxed income (GILTI) for federal tax purposes.</p><p>Under current law, a U.S. shareholder of a controlled foreign corporation is required to include in gross income the GILTI of the shareholder. The calculation of GILTI is based, in part, on the controlled foreign corporation\u2019s tested income (the controlled foreign corporation\u2019s gross income less certain exclusions).</p><p>Under the bill, the income from a qualified possession corporation that is effectively connected with an active trade or business within a U.S. territory (Puerto Rico, U.S. Virgin Islands, Guam, American Samoa, and the Northern Mariana Islands) is excluded from gross income for purposes of calculating a controlled foreign corporation\u2019s tested income.</p><p>The bill defines a\u00a0<em>qualified possession corporation</em> as any controlled foreign corporation if, for a three-year period ending in the prior tax year (or for the existence of the controlled foreign corporation if less than three years)\u00a0(1) 80% or more of the controlled foreign corporation\u2019s gross income was derived from a U.S. territory, and (2) 75% or more of the controlled foreign corporation\u2019s gross income was\u00a0effectively connected to the active conduct of a trade or business within a U.S. territory.</p>",
      "updateDate": "2026-04-29",
      "versionCode": "id119hr363"
    },
    "title": "Territorial Economic Recovery Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Territorial Economic Recovery Act</strong></p><p>This bill excludes the income of certain controlled foreign corporations in U.S. territories from the calculation of global intangible low-taxed income (GILTI) for federal tax purposes.</p><p>Under current law, a U.S. shareholder of a controlled foreign corporation is required to include in gross income the GILTI of the shareholder. The calculation of GILTI is based, in part, on the controlled foreign corporation\u2019s tested income (the controlled foreign corporation\u2019s gross income less certain exclusions).</p><p>Under the bill, the income from a qualified possession corporation that is effectively connected with an active trade or business within a U.S. territory (Puerto Rico, U.S. Virgin Islands, Guam, American Samoa, and the Northern Mariana Islands) is excluded from gross income for purposes of calculating a controlled foreign corporation\u2019s tested income.</p><p>The bill defines a\u00a0<em>qualified possession corporation</em> as any controlled foreign corporation if, for a three-year period ending in the prior tax year (or for the existence of the controlled foreign corporation if less than three years)\u00a0(1) 80% or more of the controlled foreign corporation\u2019s gross income was derived from a U.S. territory, and (2) 75% or more of the controlled foreign corporation\u2019s gross income was\u00a0effectively connected to the active conduct of a trade or business within a U.S. territory.</p>",
      "updateDate": "2026-04-29",
      "versionCode": "id119hr363"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr363ih.xml"
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
      "title": "Territorial Economic Recovery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Territorial Economic Recovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude certain amounts from the tested income of controlled foreign corporations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:48:30Z"
    }
  ]
}
```
