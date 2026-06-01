# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/297?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/297
- Title: A resolution commemorating the passage of 4 years since the tragic building collapse in Surfside, Florida, on June 24, 2021.
- Congress: 119
- Bill type: SRES
- Bill number: 297
- Origin chamber: Senate
- Introduced date: 2025-06-24
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in Senate
- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3518)
- Latest action: 2025-06-24: Introduced in Senate

## Actions

- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3518)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/297",
    "number": "297",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
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
    "title": "A resolution commemorating the passage of 4 years since the tragic building collapse in Surfside, Florida, on June 24, 2021.",
    "type": "SRES",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S3518)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T21:09:55Z",
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
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres297is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 297\nIN THE SENATE OF THE UNITED STATES\nJune 24, 2025 Mr. Scott of Florida (for himself and Mrs. Moody ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCommemorating the passage of 4 years since the tragic building collapse in Surfside, Florida, on June 24, 2021.\nThat the Senate\u2014\n**(1)**\ncommemorates the passage of 4 years since the tragic building collapse in Surfside, Florida, on June 24, 2021;\n**(2)**\nhonors the survivors and the 98 lives lost in the collapse of the Champlain Towers South condominium building and offers heartfelt condolences to the families, loved ones, and friends of the victims;\n**(3)**\ncommends the bravery and selfless service demonstrated by the local, State, national, and international teams of first responders deployed in the aftermath of the collapse; and\n**(4)**\nexpresses support for the survivors and community of Surfside, Florida.",
      "versionDate": "2025-06-24",
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
        "name": "Emergency Management",
        "updateDate": "2025-07-21T15:26:27Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres297is.xml"
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
      "title": "A resolution commemorating the passage of 4 years since the tragic building collapse in Surfside, Florida, on June 24, 2021.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T06:48:17Z"
    },
    {
      "title": "A resolution commemorating the passage of 4 years since the tragic building collapse in Surfside, Florida, on June 24, 2021.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T10:56:21Z"
    }
  ]
}
```
