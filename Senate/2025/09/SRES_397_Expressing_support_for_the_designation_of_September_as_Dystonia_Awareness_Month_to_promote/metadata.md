# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/397?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/397
- Title: A resolution expressing support for the designation of September as "Dystonia Awareness Month" to promote public awareness and understanding of dystonia.
- Congress: 119
- Bill type: SRES
- Bill number: 397
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2025-09-24T16:54:59Z
- Update date including text: 2025-09-24T16:54:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S6697)
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S6697)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/397",
    "number": "397",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "A resolution expressing support for the designation of September as \"Dystonia Awareness Month\" to promote public awareness and understanding of dystonia.",
    "type": "SRES",
    "updateDate": "2025-09-24T16:54:59Z",
    "updateDateIncludingText": "2025-09-24T16:54:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S6697)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T20:31:16Z",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres397is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 397\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. Banks (for himself and Mr. Merkley ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nExpressing support for the designation of September as Dystonia Awareness Month to promote public awareness and understanding of dystonia.\nThat the Senate\u2014\n**(1)**\nexpresses support for the designation of September as Dystonia Awareness Month ;\n**(2)**\nrecognizes the need for further research to discover new treatments and a cure for dystonia;\n**(3)**\ncommends the efforts of medical professionals and researchers who work to improve the lives of individuals with dystonia; and\n**(4)**\nencourages the people of the United States to observe Dystonia Awareness Month with appropriate programs and activities to raise public awareness and understanding of dystonia.",
      "versionDate": "2025-09-17",
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
        "name": "Health",
        "updateDate": "2025-09-23T16:54:26Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres397is.xml"
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
      "title": "A resolution expressing support for the designation of September as \"Dystonia Awareness Month\" to promote public awareness and understanding of dystonia.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:26Z"
    },
    {
      "title": "A resolution expressing support for the designation of September as \"Dystonia Awareness Month\" to promote public awareness and understanding of dystonia.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T10:56:22Z"
    }
  ]
}
```
