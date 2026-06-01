# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5662?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5662
- Title: Improving Access to Institutional Mental Health Care Act
- Congress: 119
- Bill type: HR
- Bill number: 5662
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-01-15T22:53:23Z
- Update date including text: 2026-01-15T22:53:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5662",
    "number": "5662",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000488",
        "district": "13",
        "firstName": "Shri",
        "fullName": "Rep. Thanedar, Shri [D-MI-13]",
        "lastName": "Thanedar",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Improving Access to Institutional Mental Health Care Act",
    "type": "HR",
    "updateDate": "2026-01-15T22:53:23Z",
    "updateDateIncludingText": "2026-01-15T22:53:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5662ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5662\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Thanedar introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to remove the exclusion from medical assistance under the Medicaid program of items and services for patients in an institution for mental diseases.\n#### 1. Short title\nThis Act may be cited as the Improving Access to Institutional Mental Health Care Act .\n#### 2. Removal of Medicaid exclusion from medical assistance of items and services furnished to patients in an institution for mental diseases\n##### (a) In general\nThe first sentence of section 1905(a) of the Social Security Act ( 42 U.S.C. 1396d(a) ) is amended, in the matter following paragraph (32)\u2014\n**(1)**\nby striking such term does not include\u2014 and all that follows through (A) any and inserting such term does not include any ;\n**(2)**\nby striking ; or and inserting a period; and\n**(3)**\nby striking subparagraph (B).\n##### (b) Conforming amendments To permit medical assistance for IMD patients under 65 years of age\nThe following provisions of such Act are each amended by striking 65 years of age or older and 65 years of age or over each place it appears:\n**(1)**\nParagraphs (20) and (21) of section 1902(a) ( 42 U.S.C. 1396a(a) ).\n**(2)**\nSection 1905(a)(14) ( 42 U.S.C. 1396d(a)(14) ).\n**(3)**\nSection 1919(e)(7)(B)(i)(I) ( 42 U.S.C. 1396r(e)(7)(B)(i)(I) ).\n##### (c) Effective date\nThe amendments made by this section shall take effect on October 1, 2025, and shall apply to items and services furnished on or after such date.",
      "versionDate": "2025-09-30",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-12-10T19:11:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
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
          "measure-id": "id119hr5662",
          "measure-number": "5662",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2026-01-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5662v00",
            "update-date": "2026-01-15"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Improving Access to Institutional Mental Health Care Act</strong></p><p>This bill repeals restrictions that generally prohibit federal payment under Medicaid for services provided in institutions for mental diseases (IMDs) for individuals under the age of 65. (Currently, states may receive payment for such services through certain mechanisms, such as through a Medicaid demonstration waiver.)</p>"
        },
        "title": "Improving Access to Institutional Mental Health Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5662.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Access to Institutional Mental Health Care Act</strong></p><p>This bill repeals restrictions that generally prohibit federal payment under Medicaid for services provided in institutions for mental diseases (IMDs) for individuals under the age of 65. (Currently, states may receive payment for such services through certain mechanisms, such as through a Medicaid demonstration waiver.)</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119hr5662"
    },
    "title": "Improving Access to Institutional Mental Health Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Access to Institutional Mental Health Care Act</strong></p><p>This bill repeals restrictions that generally prohibit federal payment under Medicaid for services provided in institutions for mental diseases (IMDs) for individuals under the age of 65. (Currently, states may receive payment for such services through certain mechanisms, such as through a Medicaid demonstration waiver.)</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119hr5662"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5662ih.xml"
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
      "title": "Improving Access to Institutional Mental Health Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T04:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Access to Institutional Mental Health Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T04:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to remove the exclusion from medical assistance under the Medicaid program of items and services for patients in an institution for mental diseases.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T04:18:26Z"
    }
  ]
}
```
