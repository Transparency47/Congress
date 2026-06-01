# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2063?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2063
- Title: ESTUARIES Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2063
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2026-04-06T16:23:49Z
- Update date including text: 2026-04-06T16:23:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2063",
    "number": "2063",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "ESTUARIES Act of 2025",
    "type": "S",
    "updateDate": "2026-04-06T16:23:49Z",
    "updateDateIncludingText": "2026-04-06T16:23:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T17:40:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2063is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2063\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Whitehouse (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Federal Water Pollution Control Act to reauthorize the National Estuary Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing Science, Treatment, and Upkeep of America\u2019s Resilient and Important Estuarine Systems Act of 2025 or the ESTUARIES Act of 2025 .\n#### 2. National Estuary Program\nSection 320(i)(1) of the Federal Water Pollution Control Act ( 33 U.S.C. 1330(i)(1) ), in the matter preceding subparagraph (A), is amended by striking 2026 and inserting 2031 .",
      "versionDate": "2025-06-12",
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
        "actionDate": "2025-12-16",
        "text": "Received in the Senate and Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "3962",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ESTUARIES Act",
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
            "name": "Intergovernmental relations",
            "updateDate": "2025-11-18T20:24:57Z"
          },
          {
            "name": "Marine pollution",
            "updateDate": "2025-11-18T20:24:57Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-11-18T20:24:57Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2025-11-18T20:24:57Z"
          },
          {
            "name": "Wetlands",
            "updateDate": "2025-11-18T20:24:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-07-02T18:32:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
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
          "measure-id": "id119s2063",
          "measure-number": "2063",
          "measure-type": "s",
          "orig-publish-date": "2025-06-12",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2063v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-06-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Enhancing Science, Treatment, and Upkeep of America\u2019s Resilient and Important Estuarine Systems Act of 2025 or the ESTUARIES Act\u00a0of 2025</strong></p><p>This bill reauthorizes through FY2031 grants provided under the National Estuary\u00a0Program to protect and restore estuaries of national significance.\u00a0Estuaries are coastal waterbodies where freshwater from rivers and streams mixes with the ocean\u2019s saltwater. Under the existing program, the Environmental Protection Agency provides grants for (1) developing and implementing comprehensive conservation and management plans for estuaries of national significance, and (2) addressing issues that threaten the ecological and economic well-being of such estuaries. The existing program provides grants to states, regional water pollution control agencies and entities, state coastal zone management agencies, interstate agencies, other public or nonprofit private agencies, institutions, organizations, and individuals.</p>"
        },
        "title": "ESTUARIES Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2063.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Enhancing Science, Treatment, and Upkeep of America\u2019s Resilient and Important Estuarine Systems Act of 2025 or the ESTUARIES Act\u00a0of 2025</strong></p><p>This bill reauthorizes through FY2031 grants provided under the National Estuary\u00a0Program to protect and restore estuaries of national significance.\u00a0Estuaries are coastal waterbodies where freshwater from rivers and streams mixes with the ocean\u2019s saltwater. Under the existing program, the Environmental Protection Agency provides grants for (1) developing and implementing comprehensive conservation and management plans for estuaries of national significance, and (2) addressing issues that threaten the ecological and economic well-being of such estuaries. The existing program provides grants to states, regional water pollution control agencies and entities, state coastal zone management agencies, interstate agencies, other public or nonprofit private agencies, institutions, organizations, and individuals.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2063"
    },
    "title": "ESTUARIES Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Enhancing Science, Treatment, and Upkeep of America\u2019s Resilient and Important Estuarine Systems Act of 2025 or the ESTUARIES Act\u00a0of 2025</strong></p><p>This bill reauthorizes through FY2031 grants provided under the National Estuary\u00a0Program to protect and restore estuaries of national significance.\u00a0Estuaries are coastal waterbodies where freshwater from rivers and streams mixes with the ocean\u2019s saltwater. Under the existing program, the Environmental Protection Agency provides grants for (1) developing and implementing comprehensive conservation and management plans for estuaries of national significance, and (2) addressing issues that threaten the ecological and economic well-being of such estuaries. The existing program provides grants to states, regional water pollution control agencies and entities, state coastal zone management agencies, interstate agencies, other public or nonprofit private agencies, institutions, organizations, and individuals.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2063"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2063is.xml"
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
      "title": "ESTUARIES Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ESTUARIES Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Enhancing Science, Treatment, and Upkeep of America\u2019s Resilient and Important Estuarine Systems Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Water Pollution Control Act to reauthorize the National Estuary Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T03:03:26Z"
    }
  ]
}
```
