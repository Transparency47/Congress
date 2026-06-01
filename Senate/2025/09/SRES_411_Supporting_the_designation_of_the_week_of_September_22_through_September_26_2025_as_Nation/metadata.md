# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/411?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/411
- Title: A resolution supporting the designation of the week of September 22 through September 26, 2025, as "National Hazing Awareness Week".
- Congress: 119
- Bill type: SRES
- Bill number: 411
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2025-09-24T13:28:32Z
- Update date including text: 2025-09-24T13:28:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S6741: 1)
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S6741: 1)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/411",
    "number": "411",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "A resolution supporting the designation of the week of September 22 through September 26, 2025, as \"National Hazing Awareness Week\".",
    "type": "SRES",
    "updateDate": "2025-09-24T13:28:32Z",
    "updateDateIncludingText": "2025-09-24T13:28:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S6741: 1)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T22:26:14Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres411is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 411\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Ms. Klobuchar (for herself and Mr. Cassidy ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nSupporting the designation of the week of September 22 through September 26, 2025, as National Hazing Awareness Week .\nThat the Senate\u2014\n**(1)**\nsupports the designation of the week of September 22 through September 26, 2025, as National Hazing Awareness Week ;\n**(2)**\nacknowledges hazing prevention is not limited to a single week of awareness but is an ongoing commitment; and\n**(3)**\nencourages the people of the United States to observe National Hazing Awareness Week through promoting hazing awareness and prevention.",
      "versionDate": "2025-09-18",
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
        "name": "Education",
        "updateDate": "2025-09-24T13:28:32Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres411is.xml"
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
      "title": "A resolution supporting the designation of the week of September 22 through September 26, 2025, as \"National Hazing Awareness Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-23T04:18:14Z"
    },
    {
      "title": "A resolution supporting the designation of the week of September 22 through September 26, 2025, as \"National Hazing Awareness Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T10:56:21Z"
    }
  ]
}
```
