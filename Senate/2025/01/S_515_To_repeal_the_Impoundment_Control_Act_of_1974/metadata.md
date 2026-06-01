# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/515?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/515
- Title: A bill to repeal the Impoundment Control Act of 1974.
- Congress: 119
- Bill type: S
- Bill number: 515
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2025-12-05T22:49:25Z
- Update date including text: 2025-12-05T22:49:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on the Budget.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/515",
    "number": "515",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A bill to repeal the Impoundment Control Act of 1974.",
    "type": "S",
    "updateDate": "2025-12-05T22:49:25Z",
    "updateDateIncludingText": "2025-12-05T22:49:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "ssbu00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T20:24:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Budget Committee",
      "systemCode": "ssbu00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s515is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 515\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on the Budget\nA BILL\nTo repeal the Impoundment Control Act of 1974.\n#### 1. Repeal of Impoundment Control Act of 1974\nThe Impoundment Control Act of 1974 (2 U.S.C. 681 et seq.) is hereby repealed.",
      "versionDate": "",
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
        "actionDate": "2025-02-11",
        "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1180",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To repeal the Impoundment Control Act of 1974.",
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
            "name": "Budget process",
            "updateDate": "2025-07-03T13:31:14Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-07-03T13:31:14Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-07-03T13:31:14Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-07-03T13:31:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-05-05T19:45:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119s515",
          "measure-number": "515",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2025-09-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s515v00",
            "update-date": "2025-09-26"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill repeals the Impoundment Control Act of 1974 (ICA).\u00a0The\u00a0ICA generally limits the authority of the President to impound (i.e., withhold from obligation or expenditure) funds that have been appropriated by Congress and establishes related procedures. It\u00a0also establishes expedited legislative procedures that Congress may use to consider legislation to enact rescissions proposed by the President.\u00a0</p>"
        },
        "title": "A bill to repeal the Impoundment Control Act of 1974."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s515.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill repeals the Impoundment Control Act of 1974 (ICA).\u00a0The\u00a0ICA generally limits the authority of the President to impound (i.e., withhold from obligation or expenditure) funds that have been appropriated by Congress and establishes related procedures. It\u00a0also establishes expedited legislative procedures that Congress may use to consider legislation to enact rescissions proposed by the President.\u00a0</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119s515"
    },
    "title": "A bill to repeal the Impoundment Control Act of 1974."
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill repeals the Impoundment Control Act of 1974 (ICA).\u00a0The\u00a0ICA generally limits the authority of the President to impound (i.e., withhold from obligation or expenditure) funds that have been appropriated by Congress and establishes related procedures. It\u00a0also establishes expedited legislative procedures that Congress may use to consider legislation to enact rescissions proposed by the President.\u00a0</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119s515"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s515is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal the Impoundment Control Act of 1974.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:37Z"
    },
    {
      "title": "A bill to repeal the Impoundment Control Act of 1974.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T11:56:21Z"
    }
  ]
}
```
