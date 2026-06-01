# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/448?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/448
- Title: CIRCUIT Act
- Congress: 119
- Bill type: S
- Bill number: 448
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-12-05T22:55:28Z
- Update date including text: 2026-05-02T16:27:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/448",
    "number": "448",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "CIRCUIT Act",
    "type": "S",
    "updateDate": "2025-12-05T22:55:28Z",
    "updateDateIncludingText": "2026-05-02T16:27:18Z"
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
          "date": "2025-02-06T17:59:29Z",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s448is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 448\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Moran (for himself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand the advanced manufacturing production credit to include distribution transformers.\n#### 1. Short title\nThis Act may be cited as the Credit Incentives for Resilient Critical Utility Infrastructure and Transformers Act or the CIRCUIT Act .\n#### 2. Expansion of advanced manufacturing production credit to include distribution transformers\n##### (a) In general\nSection 45X of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (b)(1)\u2014\n**(A)**\nin subparagraph (L)(ii), by striking and at the end,\n**(B)**\nin subparagraph (M), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following new subparagraph:\n(N) in the case of any distribution transformer, an amount equal to 10 percent of the costs incurred by the taxpayer with respect to production of such transformer. , and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(A)\u2014\n**(i)**\nin clause (iv), by striking and at the end,\n**(ii)**\nin clause (v), by striking the period at the end and inserting , and , and\n**(iii)**\nby adding at the end the following new clause:\n(vi) any distribution transformer. , and\n**(B)**\nby adding at the end the following new paragraph:\n(7) Distribution transformer The term distribution transformer has the same meaning given such term under section 321(35) of the Energy Policy and Conservation Act ( 42 U.S.C. 6291(35) ). .\n##### (b) Effective date\nThe amendments made by this section shall apply to components produced and sold after the date which is 90 days after the date of enactment of this Act.",
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
        "actionDate": "2025-06-25",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "4128",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CIRCUIT Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-05T17:05:01Z"
      }
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s448is.xml"
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
      "title": "CIRCUIT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CIRCUIT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Credit Incentives for Resilient Critical Utility Infrastructure and Transformers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to expand the advanced manufacturing production credit to include distribution transformers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:23Z"
    }
  ]
}
```
