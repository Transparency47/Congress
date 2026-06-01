# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2140?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2140
- Title: Diesel Emissions Reduction Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2140
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-04-06T13:06:07Z
- Update date including text: 2026-04-06T13:06:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2140",
    "number": "2140",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001163",
        "district": "7",
        "firstName": "Doris",
        "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
        "lastName": "Matsui",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Diesel Emissions Reduction Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-06T13:06:07Z",
    "updateDateIncludingText": "2026-04-06T13:06:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:04:30Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "True",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "ME"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2140ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2140\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Ms. Matsui (for herself, Mr. Calvert , Ms. Pingree , and Mr. Langworthy ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Energy Policy Act of 2005 to reauthorize the diesel emissions reduction program.\n#### 1. Short title\nThis Act may be cited as the Diesel Emissions Reduction Act of 2025 .\n#### 2. Reauthorization of diesel emissions reduction act\nSection 797(a) of the Energy Policy Act of 2005 ( 42 U.S.C. 16137(a) ) is amended by striking 2024 and inserting 2029 .",
      "versionDate": "2025-03-14",
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
        "actionDate": "2025-10-29",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 226."
      },
      "number": "2235",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Diesel Emissions Reduction Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Air quality",
            "updateDate": "2026-01-20T19:49:28Z"
          },
          {
            "name": "Climate change and greenhouse gases",
            "updateDate": "2026-01-20T19:49:28Z"
          },
          {
            "name": "Motor fuels",
            "updateDate": "2026-01-20T19:49:28Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-01-20T19:49:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-03-31T15:44:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hr2140",
          "measure-number": "2140",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2140v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Diesel Emissions Reduction Act of 2025 </strong></p><p>This bill reauthorizes through FY2029 a diesel emissions reduction program under which the Environmental Protection Agency provides grants, rebates, or loans for replacing diesel engines or retrofitting the engines with pollution control technologies.</p>"
        },
        "title": "Diesel Emissions Reduction Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2140.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Diesel Emissions Reduction Act of 2025 </strong></p><p>This bill reauthorizes through FY2029 a diesel emissions reduction program under which the Environmental Protection Agency provides grants, rebates, or loans for replacing diesel engines or retrofitting the engines with pollution control technologies.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr2140"
    },
    "title": "Diesel Emissions Reduction Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Diesel Emissions Reduction Act of 2025 </strong></p><p>This bill reauthorizes through FY2029 a diesel emissions reduction program under which the Environmental Protection Agency provides grants, rebates, or loans for replacing diesel engines or retrofitting the engines with pollution control technologies.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr2140"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2140ih.xml"
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
      "title": "Diesel Emissions Reduction Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Diesel Emissions Reduction Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Energy Policy Act of 2005 to reauthorize the diesel emissions reduction program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:18:50Z"
    }
  ]
}
```
