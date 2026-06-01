# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/302?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/302
- Title: A resolution designating June 30, 2025 as "Asteroid Day".
- Congress: 119
- Bill type: SRES
- Bill number: 302
- Origin chamber: Senate
- Introduced date: 2025-06-25
- Update date: 2025-09-10T17:02:19Z
- Update date including text: 2025-09-10T17:02:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in Senate
- 2025-06-25 - IntroReferral: Introduced in Senate
- 2025-06-25 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3534)
- Latest action: 2025-06-25: Introduced in Senate

## Actions

- 2025-06-25 - IntroReferral: Introduced in Senate
- 2025-06-25 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3534)

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/302",
    "number": "302",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "A resolution designating June 30, 2025 as \"Asteroid Day\".",
    "type": "SRES",
    "updateDate": "2025-09-10T17:02:19Z",
    "updateDateIncludingText": "2025-09-10T17:02:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S3534)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T21:22:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres302is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 302\nIN THE SENATE OF THE UNITED STATES\nJune 25 (legislative day, June 24), 2025 Mr. Kelly (for himself and Mr. Cornyn ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating June 30, 2025 as Asteroid Day .\nThat the Senate\u2014\n**(1)**\ndesignates June 30, 2025 as Asteroid Day ; and\n**(2)**\nencourages increased public awareness about the risks posed by asteroids and promotes understanding of the importance of asteroid research and planetary defense.",
      "versionDate": "2025-06-25",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Astronomy",
            "updateDate": "2025-09-10T17:01:58Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-09-10T17:02:19Z"
          },
          {
            "name": "Space flight and exploration",
            "updateDate": "2025-09-10T17:02:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-07-23T13:40:42Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres302is.xml"
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
      "title": "A resolution designating June 30, 2025 as \"Asteroid Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-27T02:18:24Z"
    },
    {
      "title": "A resolution designating June 30, 2025 as \"Asteroid Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T10:56:15Z"
    }
  ]
}
```
