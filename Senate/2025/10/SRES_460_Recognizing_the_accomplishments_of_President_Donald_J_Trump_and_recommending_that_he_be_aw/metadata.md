# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/460?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/460
- Title: A resolution recognizing the accomplishments of President Donald J. Trump and recommending that he be awarded the Nobel Peace Prize in 2026.
- Congress: 119
- Bill type: SRES
- Bill number: 460
- Origin chamber: Senate
- Introduced date: 2025-10-21
- Update date: 2025-12-05T16:11:34Z
- Update date including text: 2025-12-05T16:11:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-21: Introduced in Senate
- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S7188)
- Latest action: 2025-10-21: Introduced in Senate

## Actions

- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S7188)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/460",
    "number": "460",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
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
    "title": "A resolution recognizing the accomplishments of President Donald J. Trump and recommending that he be awarded the Nobel Peace Prize in 2026.",
    "type": "SRES",
    "updateDate": "2025-12-05T16:11:34Z",
    "updateDateIncludingText": "2025-12-05T16:11:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S7188)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-21",
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
          "date": "2025-10-21T20:51:46Z",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres460is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 460\nIN THE SENATE OF THE UNITED STATES\nOctober 21, 2025 Mr. Cassidy (for himself and Mr. Barrasso ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nRecognizing the accomplishments of President Donald J. Trump and recommending that he be awarded the Nobel Peace Prize in 2026.\nThat the Senate\u2014\n**(1)**\nrecognizes President Donald J. Trump in bringing all available Federal resources to bear through Operation Warp Speed to counter a novel pathogen;\n**(2)**\ncommends President Trump for his steadfast commitment to partnering with the private sector to save lives, protect public health, and revitalize economies; and\n**(3)**\nrecommends that President Donald J. Trump be awarded the 2026 Nobel Peace Prize, in recognition of his accomplishments and legacy of saving lives.",
      "versionDate": "2025-10-21",
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
        "updateDate": "2025-12-05T16:11:33Z"
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
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres460is.xml"
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
      "title": "A resolution recognizing the accomplishments of President Donald J. Trump and recommending that he be awarded the Nobel Peace Prize in 2026.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T12:32:04Z"
    },
    {
      "title": "A resolution recognizing the accomplishments of President Donald J. Trump and recommending that he be awarded the Nobel Peace Prize in 2026.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T10:56:22Z"
    }
  ]
}
```
