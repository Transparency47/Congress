# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3620?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3620
- Title: Emergency Rural Water Response Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3620
- Origin chamber: Senate
- Introduced date: 2026-01-13
- Update date: 2026-02-10T13:50:59Z
- Update date including text: 2026-02-10T13:50:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in Senate
- 2026-01-13 - IntroReferral: Introduced in Senate
- 2026-01-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-01-13: Introduced in Senate

## Actions

- 2026-01-13 - IntroReferral: Introduced in Senate
- 2026-01-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3620",
    "number": "3620",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Emergency Rural Water Response Act of 2026",
    "type": "S",
    "updateDate": "2026-02-10T13:50:59Z",
    "updateDateIncludingText": "2026-02-10T13:50:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
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
      "actionDate": "2026-01-13",
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
          "date": "2026-01-13T19:28:24Z",
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
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3620is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3620\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2026 Mr. Schiff (for himself and Mr. Husted ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to expand eligibility for grants related to emergency water assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Emergency Rural Water Response Act of 2026 .\n#### 2. Emergency and imminent community water assistance grant program\nSection 306A of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926a ) is amended\u2014\n**(1)**\nin subsection (d)(1)\u2014\n**(A)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (D) and (E), respectively; and\n**(B)**\nby inserting after subparagraph (B) the following:\n(C) for associated uses related to water resources infrastructure, including facilities for potable water, wastewater, storm drainage, or solid waste; ; and\n**(2)**\nin subsection (e)(1)(A), by striking 10,000 and inserting 35,000 .",
      "versionDate": "2026-01-13",
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
        "actionDate": "2025-08-06",
        "text": "Referred to the Subcommittee on Water Resources and Environment."
      },
      "number": "4879",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Emergency Rural Water Response Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-02-10T00:07:36Z"
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
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3620is.xml"
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
      "title": "Emergency Rural Water Response Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T05:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Emergency Rural Water Response Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Consolidated Farm and Rural Development Act to expand eligibility for grants related to emergency water assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T05:48:38Z"
    }
  ]
}
```
