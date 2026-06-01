# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2691?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2691
- Title: Rural Microentrepreneur Assistance Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2691
- Origin chamber: Senate
- Introduced date: 2025-09-03
- Update date: 2026-04-01T15:20:06Z
- Update date including text: 2026-04-01T15:20:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-03: Introduced in Senate
- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-09-03: Introduced in Senate

## Actions

- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2691",
    "number": "2691",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Rural Microentrepreneur Assistance Act of 2025",
    "type": "S",
    "updateDate": "2026-04-01T15:20:06Z",
    "updateDateIncludingText": "2026-04-01T15:20:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T15:21:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2691is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2691\nIN THE SENATE OF THE UNITED STATES\nSeptember 3, 2025 Mr. Ricketts (for himself and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to extend and enhance the Rural Microentrepreneur Assistance Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Microentrepreneur Assistance Act of 2025 .\n#### 2. Increase in funding for the Rural Microentrepreneur Assistance Program\nSection 379E of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2008s ) is amended\u2014\n**(1)**\nin subsection (a)(4), by striking $50,000 and inserting $75,000 ;\n**(2)**\nin subsection (b)(3), by adding at the end the following:\n(E) Use of funds A microloan made by a microenterprise development organization to a microentrepreneur under this paragraph for a project may be used to cover not more than 50 percent of any demolition, construction, or related costs of real estate improvements under the project. ;\n**(3)**\nin subsection (c)(1)(A), by striking 75 percent and inserting 100 percent ; and\n**(4)**\nin subsection (d), by striking 2019 through 2023 and inserting 2026 through 2030 .",
      "versionDate": "2025-09-03",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-09-12T17:01:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-03",
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
          "measure-id": "id119s2691",
          "measure-number": "2691",
          "measure-type": "s",
          "orig-publish-date": "2025-09-03",
          "originChamber": "SENATE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2691v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-09-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Rural Microentrepreneur Assistance Act of 2025</strong></p><p>This bill reauthorizes through FY2030 and revises the\u00a0Rural Microentrepreneur Assistance Program (RMAP).\u00a0This Department of Agriculture program provides loans and grants\u00a0to eligible microenterprise development organizations to (1) capitalize revolving loan funds that provide loans to qualified rural microenterprises (i.e.,\u00a0sole proprietorships located in\u00a0rural areas or\u00a0business entities with not more than 10 full-time employees located in a rural area), and (2) provide related training and technical assistance.</p><p>The bill increases the amount a rural microenterprise may borrow to up to $75,000 (from up to $50,000).</p><p>The bill also increases the maximum allowable federal cost share to 100% (from 75%). The bill further specifies that a RMAP project loan may not be used to cover more than 50% of any demolition, construction, or related costs of real estate improvements.</p>"
        },
        "title": "Rural Microentrepreneur Assistance Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2691.xml",
    "summary": {
      "actionDate": "2025-09-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Microentrepreneur Assistance Act of 2025</strong></p><p>This bill reauthorizes through FY2030 and revises the\u00a0Rural Microentrepreneur Assistance Program (RMAP).\u00a0This Department of Agriculture program provides loans and grants\u00a0to eligible microenterprise development organizations to (1) capitalize revolving loan funds that provide loans to qualified rural microenterprises (i.e.,\u00a0sole proprietorships located in\u00a0rural areas or\u00a0business entities with not more than 10 full-time employees located in a rural area), and (2) provide related training and technical assistance.</p><p>The bill increases the amount a rural microenterprise may borrow to up to $75,000 (from up to $50,000).</p><p>The bill also increases the maximum allowable federal cost share to 100% (from 75%). The bill further specifies that a RMAP project loan may not be used to cover more than 50% of any demolition, construction, or related costs of real estate improvements.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119s2691"
    },
    "title": "Rural Microentrepreneur Assistance Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-09-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Microentrepreneur Assistance Act of 2025</strong></p><p>This bill reauthorizes through FY2030 and revises the\u00a0Rural Microentrepreneur Assistance Program (RMAP).\u00a0This Department of Agriculture program provides loans and grants\u00a0to eligible microenterprise development organizations to (1) capitalize revolving loan funds that provide loans to qualified rural microenterprises (i.e.,\u00a0sole proprietorships located in\u00a0rural areas or\u00a0business entities with not more than 10 full-time employees located in a rural area), and (2) provide related training and technical assistance.</p><p>The bill increases the amount a rural microenterprise may borrow to up to $75,000 (from up to $50,000).</p><p>The bill also increases the maximum allowable federal cost share to 100% (from 75%). The bill further specifies that a RMAP project loan may not be used to cover more than 50% of any demolition, construction, or related costs of real estate improvements.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119s2691"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2691is.xml"
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
      "title": "Rural Microentrepreneur Assistance Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-06T07:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Microentrepreneur Assistance Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-06T07:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Consolidated Farm and Rural Development Act to extend and enhance the Rural Microentrepreneur Assistance Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-06T07:33:18Z"
    }
  ]
}
```
