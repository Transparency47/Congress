# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/551?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/551
- Title: Ensuring Outpatient Quality for Rural States Act
- Congress: 119
- Bill type: S
- Bill number: 551
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2025-12-05T22:52:26Z
- Update date including text: 2025-12-05T22:52:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/551",
    "number": "551",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Ensuring Outpatient Quality for Rural States Act",
    "type": "S",
    "updateDate": "2025-12-05T22:52:26Z",
    "updateDateIncludingText": "2025-12-05T22:52:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T21:46:58Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "HI"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s551is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 551\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Sullivan (for himself, Mr. Schatz , and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide for the application of a cost-of-living adjustment to the non-labor related portion for hospital outpatient department services furnished in Alaska and Hawaii.\n#### 1. Short title\nThis Act may be cited as the Ensuring Outpatient Quality for Rural States Act .\n#### 2. Application of cost-of-living adjustment to non-labor related portion for hospital outpatient department services furnished in Alaska and Hawaii\nSection 1833(t) of the Social Security Act ( 42 U.S.C. 1395l(t) ) is amended by adding at the end the following new paragraph:\n(23) Application of cost-of-living adjustment to non-labor related portion for hospital outpatient department services furnished in Alaska and Hawaii With respect to covered OPD services furnished on or after January 1, 2026, the Secretary may provide for adjustments to the payment amounts under this subsection for such services in the same manner that is provided under section 1886(d)(5)(H) with respect to the application of the cost-of-living adjustment to the non-labor related portion of such payment amounts to take into account the unique circumstances of hospitals located in Alaska or Hawaii. The preceding sentence shall not be applied in a budget neutral manner. .",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-06-30",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4269",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ensuring Outpatient Quality for Rural States Act",
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
            "name": "Alaska",
            "updateDate": "2025-06-13T18:51:34Z"
          },
          {
            "name": "Hawaii",
            "updateDate": "2025-06-13T18:51:40Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-06-13T18:51:51Z"
          },
          {
            "name": "Home and outpatient care",
            "updateDate": "2025-06-13T18:51:29Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-06-13T18:51:45Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-06-13T18:51:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-13T17:36:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119s551",
          "measure-number": "551",
          "measure-type": "s",
          "orig-publish-date": "2025-02-12",
          "originChamber": "SENATE",
          "update-date": "2025-04-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s551v00",
            "update-date": "2025-04-28"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Ensuring Outpatient Quality for Rural States Act</strong></p><p>This bill allows Medicare payments for covered hospital outpatient services in Alaska or Hawaii to include certain cost-of-living adjustments.</p>"
        },
        "title": "Ensuring Outpatient Quality for Rural States Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s551.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ensuring Outpatient Quality for Rural States Act</strong></p><p>This bill allows Medicare payments for covered hospital outpatient services in Alaska or Hawaii to include certain cost-of-living adjustments.</p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119s551"
    },
    "title": "Ensuring Outpatient Quality for Rural States Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ensuring Outpatient Quality for Rural States Act</strong></p><p>This bill allows Medicare payments for covered hospital outpatient services in Alaska or Hawaii to include certain cost-of-living adjustments.</p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119s551"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s551is.xml"
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
      "title": "Ensuring Outpatient Quality for Rural States Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Outpatient Quality for Rural States Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide for the application of a cost-of-living adjustment to the non-labor related portion for hospital outpatient department services furnished in Alaska and Hawaii.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:39Z"
    }
  ]
}
```
