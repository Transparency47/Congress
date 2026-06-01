# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/420?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/420
- Title: Dairy Business Innovation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 420
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2025-03-24T10:42:31Z
- Update date including text: 2025-03-24T10:42:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/420",
    "number": "420",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Dairy Business Innovation Act of 2025",
    "type": "S",
    "updateDate": "2025-03-24T10:42:31Z",
    "updateDateIncludingText": "2025-03-24T10:42:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
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
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T20:16:40Z",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s420is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 420\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Ms. Baldwin (for herself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agriculture Improvement Act of 2018 to reauthorize the dairy business innovation initiatives.\n#### 1. Short title\nThis Act may be cited as the Dairy Business Innovation Act of 2025 .\n#### 2. Dairy business innovation initiatives\nSection 12513(i) of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 1632d(i) ) is amended by striking $20,000,000 and inserting $36,000,000 .",
      "versionDate": "2025-02-05",
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
        "updateDate": "2025-03-20T18:42:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119s420",
          "measure-number": "420",
          "measure-type": "s",
          "orig-publish-date": "2025-02-05",
          "originChamber": "SENATE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s420v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Dairy Business Innovation Act of 2025</strong></p><p>This bill increases the authorization of appropriations for the Dairy Business Innovation\u00a0(DBI) Initiatives<strong> </strong>for each fiscal year. Under the Agricultural Marketing Service, the\u00a0DBI Initiatives support dairy businesses in the development, production, marketing, and distribution of dairy products. The DBI Initiatives provide direct technical assistance and subawards to dairy businesses, including for niche dairy products and dairy products derived from cow milk, sheep milk, and goat milk.</p>"
        },
        "title": "Dairy Business Innovation Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s420.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dairy Business Innovation Act of 2025</strong></p><p>This bill increases the authorization of appropriations for the Dairy Business Innovation\u00a0(DBI) Initiatives<strong> </strong>for each fiscal year. Under the Agricultural Marketing Service, the\u00a0DBI Initiatives support dairy businesses in the development, production, marketing, and distribution of dairy products. The DBI Initiatives provide direct technical assistance and subawards to dairy businesses, including for niche dairy products and dairy products derived from cow milk, sheep milk, and goat milk.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119s420"
    },
    "title": "Dairy Business Innovation Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dairy Business Innovation Act of 2025</strong></p><p>This bill increases the authorization of appropriations for the Dairy Business Innovation\u00a0(DBI) Initiatives<strong> </strong>for each fiscal year. Under the Agricultural Marketing Service, the\u00a0DBI Initiatives support dairy businesses in the development, production, marketing, and distribution of dairy products. The DBI Initiatives provide direct technical assistance and subawards to dairy businesses, including for niche dairy products and dairy products derived from cow milk, sheep milk, and goat milk.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119s420"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s420is.xml"
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
      "title": "Dairy Business Innovation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-08T06:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dairy Business Innovation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agriculture Improvement Act of 2018 to reauthorize the dairy business innovation initiatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:27Z"
    }
  ]
}
```
