# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4128?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4128
- Title: CIRCUIT Act
- Congress: 119
- Bill type: HR
- Bill number: 4128
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2026-02-24T09:05:38Z
- Update date including text: 2026-05-02T16:27:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4128",
    "number": "4128",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000478",
        "district": "7",
        "firstName": "Russell",
        "fullName": "Rep. Fry, Russell [R-SC-7]",
        "lastName": "Fry",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "CIRCUIT Act",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:38Z",
    "updateDateIncludingText": "2026-05-02T16:27:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T14:01:40Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "KS"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "VA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "WA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4128ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4128\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Fry (for himself and Ms. Davids of Kansas ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand the advanced manufacturing production credit to include distribution transformers.\n#### 1. Short title\nThis Act may be cited as the Credit Incentives for Resilient Critical Utility Infrastructure and Transformers Act or the CIRCUIT Act .\n#### 2. Expansion of advanced manufacturing production credit to include distribution transformers\n##### (a) In general\nSection 45X of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (b)(1)\u2014\n**(A)**\nin subparagraph (L)(ii), by striking and at the end,\n**(B)**\nin subparagraph (M), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following new subparagraph:\n(N) in the case of any distribution transformer, an amount equal to 10 percent of the costs incurred by the taxpayer with respect to production of such transformer. , and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(A)\u2014\n**(i)**\nin clause (iv), by striking and at the end,\n**(ii)**\nin clause (v), by striking the period at the end and inserting , and , and\n**(iii)**\nby adding at the end the following new clause:\n(vi) any distribution transformer. , and\n**(B)**\nby adding at the end the following new paragraph:\n(7) Distribution transformer The term distribution transformer has the same meaning given such term under section 321(35) of the Energy Policy and Conservation Act ( 42 U.S.C. 6291(35) ). .\n##### (b) Effective date\nThe amendments made by this section shall apply to components produced and sold after the date which is 90 days after the date of enactment of this Act.",
      "versionDate": "2025-06-25",
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
        "actionDate": "2025-02-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "448",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CIRCUIT Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-07-17T18:58:55Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4128ih.xml"
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
      "title": "CIRCUIT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CIRCUIT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Credit Incentives for Resilient Critical Utility Infrastructure and Transformers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to expand the advanced manufacturing production credit to include distribution transformers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T05:18:34Z"
    }
  ]
}
```
