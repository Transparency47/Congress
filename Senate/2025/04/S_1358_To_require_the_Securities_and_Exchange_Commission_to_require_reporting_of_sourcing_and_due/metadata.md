# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1358?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1358
- Title: TASK Act
- Congress: 119
- Bill type: S
- Bill number: 1358
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2025-05-20T13:15:07Z
- Update date including text: 2026-05-05T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1358",
    "number": "1358",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "TASK Act",
    "type": "S",
    "updateDate": "2025-05-20T13:15:07Z",
    "updateDateIncludingText": "2026-05-05T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T21:59:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sponsorshipDate": "2025-04-08",
      "state": "TN"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1358is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1358\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Scott of Florida (for himself, Mrs. Blackburn , and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Securities and Exchange Commission to require reporting of sourcing and due diligence activities of companies involving supply chains of products that are imported into the United States that are directly linked to products utilizing forced labor from Xinjiang, China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transaction and Sourcing Knowledge Act or the TASK Act .\n#### 2. SEC reporting\nThe Securities and Exchange Commission, as part of its evaluation of potential guidance on reporting on environmental, social, and governance matters by publicly traded companies, shall require reporting of\u2014\n**(1)**\nsourcing and due diligence activities of such companies involving supply chains of products that are imported into the United States that are directly linked to products utilizing forced labor from Xinjiang, China;\n**(2)**\ntransactions with companies that have been\u2014\n**(A)**\nplaced on the Entity List by the Department of Commerce; or\n**(B)**\ndesignated by the Department of the Treasury as Chinese Military-Industrial Complex Companies; and\n**(3)**\nwith respect to publicly traded United States companies with facilities in China, on an annual basis\u2014\n**(A)**\nwhether there is a Chinese Communist Party committee in the operations of the company; and\n**(B)**\na summary of the actions and corporate decisions in which any committee described in subparagraph (A) may have participated.",
      "versionDate": "2025-04-08",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-20T13:15:07Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1358is.xml"
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
      "title": "TASK Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TASK Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Transaction and Sourcing Knowledge Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Securities and Exchange Commission to require reporting of sourcing and due diligence activities of companies involving supply chains of products that are imported into the United States that are directly linked to products utilizing forced labor from Xinjiang, China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T04:18:26Z"
    }
  ]
}
```
