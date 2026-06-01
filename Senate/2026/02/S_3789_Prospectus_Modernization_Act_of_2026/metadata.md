# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3789?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3789
- Title: Prospectus Modernization Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3789
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-03-03T12:03:27Z
- Update date including text: 2026-03-03T12:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-02-05: Introduced in Senate

## Actions

- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3789",
    "number": "3789",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Prospectus Modernization Act of 2026",
    "type": "S",
    "updateDate": "2026-03-03T12:03:27Z",
    "updateDateIncludingText": "2026-03-03T12:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T18:30:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3789is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3789\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo provide for a temporary adjustment to the prospectus thresholds for certain General Services Administration projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prospectus Modernization Act of 2026 .\n#### 2. GSA prospectus threshold\n##### (a) In general\nNotwithstanding any other provision of law, for fiscal years 2026 through 2028, section 3307(a) of title 40, United States Code, shall be applied\u2014\n**(1)**\nby substituting $10,000,000 for $1,500,000 in each of paragraphs (1) and (2) of that section; and\n**(2)**\nby substituting $5,000,000 for $750,000 in paragraph (3) of that section.\n##### (b) No adjustment\nFor purposes of fiscal years 2026 through 2028, section 3307(h) of title 40, United States Code, shall not apply to the amounts substituted under subsection (a).",
      "versionDate": "2026-02-05",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-23T23:37:15Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3789is.xml"
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
      "title": "Prospectus Modernization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T12:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prospectus Modernization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for a temporary adjustment to the prospectus thresholds for certain General Services Administration projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:20Z"
    }
  ]
}
```
