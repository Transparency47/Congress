# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/281?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/281
- Title: A resolution commemorating the 95th anniversary of the enactment of the Tariff Act of 1930.
- Congress: 119
- Bill type: SRES
- Bill number: 281
- Origin chamber: Senate
- Introduced date: 2025-06-17
- Update date: 2026-05-14T16:24:59Z
- Update date including text: 2026-05-14T16:24:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-17: Introduced in Senate
- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Referred to the Committee on Finance. (text: CR S3437-3438)
- Latest action: 2025-06-17: Introduced in Senate

## Actions

- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Referred to the Committee on Finance. (text: CR S3437-3438)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/281",
    "number": "281",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C000127",
        "district": "",
        "firstName": "Maria",
        "fullName": "Sen. Cantwell, Maria [D-WA]",
        "lastName": "Cantwell",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "A resolution commemorating the 95th anniversary of the enactment of the Tariff Act of 1930.",
    "type": "SRES",
    "updateDate": "2026-05-14T16:24:59Z",
    "updateDateIncludingText": "2026-05-14T16:24:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-17",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Finance. (text: CR S3437-3438)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T17:04:12Z",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "NH"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "VT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres281is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 281\nIN THE SENATE OF THE UNITED STATES\nJune 17, 2025 Ms. Cantwell (for herself, Mrs. Shaheen , and Mr. Welch ) submitted the following resolution; which was referred to the Committee on Finance\nRESOLUTION\nCommemorating the 95th anniversary of the enactment of the Tariff Act of 1930.\nThat the Senate\u2014\n**(1)**\nobserves the 95th anniversary of the enactment of the Tariff Act of 1930 (commonly known as the Smoot-Hawley Tariff Act of 1930 ) as a moment of historical reflection on the consequences of protectionist economic policies;\n**(2)**\nviews the Tariff Act of 1930 as a significant contributor to the Great Depression;\n**(3)**\naffirms the importance of rules-based trade policy that reduces production costs for farmers, manufacturers, and construction firms in the United States, strengthens international economic cooperation, helps provide consumers in the United States with a larger variety of affordable goods, and opens up vast foreign markets to exports from the United States; and\n**(4)**\ncommits to encouraging trade and economic policies that encourage economic growth and avoid the repetition of historic policy mistakes.",
      "versionDate": "2025-06-17",
      "versionType": "IS"
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-07-22T12:40:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-17",
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
          "measure-id": "id119sres281",
          "measure-number": "281",
          "measure-type": "sres",
          "orig-publish-date": "2025-06-17",
          "originChamber": "SENATE",
          "update-date": "2026-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres281v00",
            "update-date": "2026-05-14"
          },
          "action-date": "2025-06-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution observes the 95th anniversary of the enactment of the Tariff Act of 1930 (also known as the\u00a0Smoot-Hawley Tariff Act) and expresses the view that this act was a significant contributor to the Great Depression. (The act raised U.S. tariffs to their highest levels since 1828 and was the last tariff act in which Congress set rates.)</p>"
        },
        "title": "A resolution commemorating the 95th anniversary of the enactment of the Tariff Act of 1930."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres281.xml",
    "summary": {
      "actionDate": "2025-06-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution observes the 95th anniversary of the enactment of the Tariff Act of 1930 (also known as the\u00a0Smoot-Hawley Tariff Act) and expresses the view that this act was a significant contributor to the Great Depression. (The act raised U.S. tariffs to their highest levels since 1828 and was the last tariff act in which Congress set rates.)</p>",
      "updateDate": "2026-05-14",
      "versionCode": "id119sres281"
    },
    "title": "A resolution commemorating the 95th anniversary of the enactment of the Tariff Act of 1930."
  },
  "summaries": [
    {
      "actionDate": "2025-06-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution observes the 95th anniversary of the enactment of the Tariff Act of 1930 (also known as the\u00a0Smoot-Hawley Tariff Act) and expresses the view that this act was a significant contributor to the Great Depression. (The act raised U.S. tariffs to their highest levels since 1828 and was the last tariff act in which Congress set rates.)</p>",
      "updateDate": "2026-05-14",
      "versionCode": "id119sres281"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres281is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution commemorating the 95th anniversary of the enactment of the Tariff Act of 1930.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:27Z"
    },
    {
      "title": "A resolution commemorating the 95th anniversary of the enactment of the Tariff Act of 1930.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-18T10:56:14Z"
    }
  ]
}
```
