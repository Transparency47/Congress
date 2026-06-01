# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/466?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/466
- Title: Fairness for Disabled Young Adults Act
- Congress: 119
- Bill type: S
- Bill number: 466
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-07-23T18:43:20Z
- Update date including text: 2025-07-23T18:43:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/466",
    "number": "466",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Fairness for Disabled Young Adults Act",
    "type": "S",
    "updateDate": "2025-07-23T18:43:20Z",
    "updateDateIncludingText": "2025-07-23T18:43:20Z"
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
          "date": "2025-02-06T19:49:54Z",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s466is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 466\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Cassidy (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title II of the Social Security Act to increase the age threshold for eligibility for child\u2019s insurance benefits on the basis of disability.\n#### 1. Short title\nThis Act may be cited as the Fairness for Disabled Young Adults Act .\n#### 2. Increase to age threshold for child\u2019s insurance benefits on the basis of disability\n##### (a) In general\nSection 202(d) of the Social Security Act ( 42 U.S.C. 402(d) ) is amended by striking age of 22 each place it appears and inserting age of 26 .\n##### (b) Conforming amendments\n**(1)**\nSection 205(j)(2)(C)(vi)(II)(cc) of the Social Security Act (42 U.S.C. 405(j)(2)(C)(vi)(II)(cc)) is amended by striking age of 22 and inserting age of 26 .\n**(2)**\nSection 225(a) of the Social Security Act ( 42 U.S.C. 425(a) ) is amended by striking age of 22 and inserting age of 26 .\n**(3)**\nSection 1631(a)(2)(B)(xvii)(II)(cc) of the Social Security Act (42 U.S.C. 1383(a)(2)(B)(xvii)(II)(cc)) is amended by striking age of 22 and inserting age of 26 .\n**(4)**\nSection 1634(c) of the Social Security Act ( 42 U.S.C. 1383c(c) ) is amended by striking age of 22 and inserting age of 26 .",
      "versionDate": "2025-02-06",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child health",
            "updateDate": "2025-04-24T15:55:59Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-04-24T15:55:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-03-12T17:35:44Z"
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
          "measure-id": "id119s466",
          "measure-number": "466",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-07-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s466v00",
            "update-date": "2025-07-23"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fairness for Disabled Young Adults Act</strong></p><p>This bill expands eligibility for Social Security child\u2019s benefits to include the disabled children of eligible or deceased workers for whom the disability began between ages 22 and 25. (Under current law, such disabled children are eligible for benefits only if their disability began before age 22.)</p>"
        },
        "title": "Fairness for Disabled Young Adults Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s466.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fairness for Disabled Young Adults Act</strong></p><p>This bill expands eligibility for Social Security child\u2019s benefits to include the disabled children of eligible or deceased workers for whom the disability began between ages 22 and 25. (Under current law, such disabled children are eligible for benefits only if their disability began before age 22.)</p>",
      "updateDate": "2025-07-23",
      "versionCode": "id119s466"
    },
    "title": "Fairness for Disabled Young Adults Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fairness for Disabled Young Adults Act</strong></p><p>This bill expands eligibility for Social Security child\u2019s benefits to include the disabled children of eligible or deceased workers for whom the disability began between ages 22 and 25. (Under current law, such disabled children are eligible for benefits only if their disability began before age 22.)</p>",
      "updateDate": "2025-07-23",
      "versionCode": "id119s466"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s466is.xml"
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
      "title": "Fairness for Disabled Young Adults Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fairness for Disabled Young Adults Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title II of the Social Security Act to increase the age threshold for eligibility for child's insurance benefits on the basis of disability.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:35:00Z"
    }
  ]
}
```
