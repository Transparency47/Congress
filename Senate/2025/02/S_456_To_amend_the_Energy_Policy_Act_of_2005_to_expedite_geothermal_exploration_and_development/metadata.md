# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/456?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/456
- Title: STEAM Act
- Congress: 119
- Bill type: S
- Bill number: 456
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/456",
    "number": "456",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
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
    "title": "STEAM Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
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
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
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
          "date": "2025-02-06T18:14:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AK"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MT"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s456is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 456\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Ms. Cortez Masto (for herself and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Energy Policy Act of 2005 to expedite geothermal exploration and development in previously studied or developed areas.\n#### 1. Short title\nThis Act may be cited as the Streamlining Thermal Energy through Advanced Mechanisms Act or the STEAM Act .\n#### 2. NEPA Review\nSection 390 of the Energy Policy Act of 2005 ( 42 U.S.C. 15942 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting , or the Geothermal Steam Act of 1970 ( 30 U.S.C. 1001 et seq. ) for the purpose of exploration or development of geothermal resources after or gas ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2), by striking or gas and inserting , gas, or geothermal ; and\n**(B)**\nin paragraph (3), by striking or gas and inserting , gas, or geothermal .",
      "versionDate": "2025-02-06",
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
        "actionDate": "2026-03-05",
        "text": "Ordered to be Reported by Unanimous Consent."
      },
      "number": "1077",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "STEAM Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alternative and renewable resources",
            "updateDate": "2026-01-05T18:23:27Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-01-05T18:23:27Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-01-05T18:23:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-12T16:16:17Z"
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
          "measure-id": "id119s456",
          "measure-number": "456",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-01-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s456v00",
            "update-date": "2026-01-22"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Streamlining Thermal Energy through Advanced Mechanisms Act or the STEAM Act</strong></p><p>This bill expedites the environmental review of certain geothermal energy activities under the National Environmental Policy Act of 1969 (NEPA). Specifically, the bill expands\u00a0the Energy Policy Act of 2005 to include certain geothermal exploration or development activities in an existing categorical exclusion from NEPA for certain oil or gas activities.\u00a0</p><p>A\u00a0categorical exclusion applies to a class of actions that do not require an environmental assessment nor an environmental impact statement under NEPA.</p><p>The categorical exclusion established by the bill applies to\u00a0drilling a geothermal well (1) in an area where drilling has occurred previously within the five years prior to the date when drilling begins; or (2) within a developed field for which an approved land use plan or environmental document prepared under NEPA determined drilling to be a reasonably foreseeable activity, so long as the plan or document was approved within the five years prior to the date when drilling begins.</p>"
        },
        "title": "STEAM Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s456.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Streamlining Thermal Energy through Advanced Mechanisms Act or the STEAM Act</strong></p><p>This bill expedites the environmental review of certain geothermal energy activities under the National Environmental Policy Act of 1969 (NEPA). Specifically, the bill expands\u00a0the Energy Policy Act of 2005 to include certain geothermal exploration or development activities in an existing categorical exclusion from NEPA for certain oil or gas activities.\u00a0</p><p>A\u00a0categorical exclusion applies to a class of actions that do not require an environmental assessment nor an environmental impact statement under NEPA.</p><p>The categorical exclusion established by the bill applies to\u00a0drilling a geothermal well (1) in an area where drilling has occurred previously within the five years prior to the date when drilling begins; or (2) within a developed field for which an approved land use plan or environmental document prepared under NEPA determined drilling to be a reasonably foreseeable activity, so long as the plan or document was approved within the five years prior to the date when drilling begins.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119s456"
    },
    "title": "STEAM Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Streamlining Thermal Energy through Advanced Mechanisms Act or the STEAM Act</strong></p><p>This bill expedites the environmental review of certain geothermal energy activities under the National Environmental Policy Act of 1969 (NEPA). Specifically, the bill expands\u00a0the Energy Policy Act of 2005 to include certain geothermal exploration or development activities in an existing categorical exclusion from NEPA for certain oil or gas activities.\u00a0</p><p>A\u00a0categorical exclusion applies to a class of actions that do not require an environmental assessment nor an environmental impact statement under NEPA.</p><p>The categorical exclusion established by the bill applies to\u00a0drilling a geothermal well (1) in an area where drilling has occurred previously within the five years prior to the date when drilling begins; or (2) within a developed field for which an approved land use plan or environmental document prepared under NEPA determined drilling to be a reasonably foreseeable activity, so long as the plan or document was approved within the five years prior to the date when drilling begins.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119s456"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s456is.xml"
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
      "title": "STEAM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STEAM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Streamlining Thermal Energy through Advanced Mechanisms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Energy Policy Act of 2005 to expedite geothermal exploration and development in previously studied or developed areas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:19:12Z"
    }
  ]
}
```
