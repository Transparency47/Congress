# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/124?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/124
- Title: Byron Nash Renal Medullary Carcinoma Awareness Act of 2023
- Congress: 119
- Bill type: HR
- Bill number: 124
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-03-19T16:00:15Z
- Update date including text: 2025-03-19T16:00:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/124",
    "number": "124",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000553",
        "district": "9",
        "firstName": "Al",
        "fullName": "Rep. Green, Al [D-TX-9]",
        "lastName": "Green",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Byron Nash Renal Medullary Carcinoma Awareness Act of 2023",
    "type": "HR",
    "updateDate": "2025-03-19T16:00:15Z",
    "updateDateIncludingText": "2025-03-19T16:00:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:22:10Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr124ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 124\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Green of Texas introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to provide incentives for education on the risk of renal medullary carcinoma in individuals who are receiving medical assistance under such title and who have sickle cell disease.\n#### 1. Short title\nThis Act may be cited as the Byron Nash Renal Medullary Carcinoma Awareness Act of 2023 .\n#### 2. Providing incentives for education on risk of renal medullary carcinoma to individuals with Sickle Cell Disease under Medicaid\n##### (a) In general\nSection 1903(a)(3)(E)(ii) of the Social Security Act ( 42 U.S.C. 1396b(a)(3)(E)(ii) ) is amended by inserting , renal medullary carcinoma, after stroke each place it appears.\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply with respect to items and services furnished on or after the date of the enactment of this Act.",
      "versionDate": "2023-01-09",
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
            "name": "Cancer",
            "updateDate": "2025-03-19T16:00:00Z"
          },
          {
            "name": "Digestive and metabolic diseases",
            "updateDate": "2025-03-19T16:00:05Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-03-19T16:00:11Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-03-19T16:00:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-17T12:02:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr124",
          "measure-number": "124",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr124v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Byron Nash Renal Medullary Carcinoma Awareness Act of </strong><strong>2023\u00a0[<em>sic</em>]</strong></p><p>This bill allows states to receive federal payment under Medicaid for 50% of their costs for providing education on the risk of renal medullary carcinoma to individuals with sickle cell disease. (Renal medullary carcinoma is a rare kidney disease usually found in individuals with the sickle cell trait.)</p>"
        },
        "title": "Byron Nash Renal Medullary Carcinoma Awareness Act of 2023"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr124.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Byron Nash Renal Medullary Carcinoma Awareness Act of </strong><strong>2023\u00a0[<em>sic</em>]</strong></p><p>This bill allows states to receive federal payment under Medicaid for 50% of their costs for providing education on the risk of renal medullary carcinoma to individuals with sickle cell disease. (Renal medullary carcinoma is a rare kidney disease usually found in individuals with the sickle cell trait.)</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr124"
    },
    "title": "Byron Nash Renal Medullary Carcinoma Awareness Act of 2023"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Byron Nash Renal Medullary Carcinoma Awareness Act of </strong><strong>2023\u00a0[<em>sic</em>]</strong></p><p>This bill allows states to receive federal payment under Medicaid for 50% of their costs for providing education on the risk of renal medullary carcinoma to individuals with sickle cell disease. (Renal medullary carcinoma is a rare kidney disease usually found in individuals with the sickle cell trait.)</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr124"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2023-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr124ih.xml"
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
      "title": "Byron Nash Renal Medullary Carcinoma Awareness Act of 2023",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Byron Nash Renal Medullary Carcinoma Awareness Act of 2023",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to provide incentives for education on the risk of renal medullary carcinoma in individuals who are receiving medical assistance under such title and who have sickle cell disease.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:32Z"
    }
  ]
}
```
