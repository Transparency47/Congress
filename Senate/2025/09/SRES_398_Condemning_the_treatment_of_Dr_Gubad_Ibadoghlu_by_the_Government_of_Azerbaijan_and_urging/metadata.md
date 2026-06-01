# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/398?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/398
- Title: A resolution condemning the treatment of Dr. Gubad Ibadoghlu by the Government of Azerbaijan and urging his immediate release.
- Congress: 119
- Bill type: SRES
- Bill number: 398
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2025-09-19T16:32:31Z
- Update date including text: 2025-09-19T16:32:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S6698: 1)
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S6698: 1)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/398",
    "number": "398",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "A resolution condemning the treatment of Dr. Gubad Ibadoghlu by the Government of Azerbaijan and urging his immediate release.",
    "type": "SRES",
    "updateDate": "2025-09-19T16:32:31Z",
    "updateDateIncludingText": "2025-09-19T16:32:31Z"
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
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S6698: 1)",
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
          "date": "2025-09-17T20:41:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "IL"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "LA"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "PA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres398is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 398\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. Tillis (for himself, Mr. Durbin , Mr. Cassidy , Mr. Fetterman , and Mr. Kaine ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCondemning the treatment of Dr. Gubad Ibadoghlu by the Government of Azerbaijan and urging his immediate release.\nThat the Senate\u2014\n**(1)**\ncommends the progress made in peace negotiations between Armenia and Azerbaijan, and expresses hope that such progress will lead to lasting peace and greater international engagement;\n**(2)**\ncondemns\u2014\n**(A)**\nthe treatment of Dr. Ibadoghlu and other political prisoners by the Government of Azerbaijan;\n**(B)**\nthe Government of Azerbaijan's practice of wrongful detention; and\n**(C)**\nthe suppression of academic freedom and peaceful expression;\n**(3)**\ncalls for the immediate and unconditional release of political prisoners in Azerbaijan, including Dr. Ibadoghlu, and specifically urges his release in advance of Azerbaijan\u2019s hosting of international events such as the Formula 1 Grand Prix, further underscoring that until such release occurs, the United States cannot treat those events as positive opportunities for partnership and will instead continue to highlight in such forums the persistence of wrongful detentions and human rights concerns; and\n**(4)**\nurges all responsible officials and agencies of the United States Government, including the Department of State, the Department of the Treasury, and other relevant entities, to make Dr. Ibadoghlu\u2019s well-being and release a priority in all engagements with the Government of Azerbaijan, reinforcing that genuine peace must be accompanied by respect for human rights and academic freedom.",
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
        "name": "International Affairs",
        "updateDate": "2025-09-19T16:32:31Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres398is.xml"
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
      "title": "A resolution condemning the treatment of Dr. Gubad Ibadoghlu by the Government of Azerbaijan and urging his immediate release.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:16Z"
    },
    {
      "title": "A resolution condemning the treatment of Dr. Gubad Ibadoghlu by the Government of Azerbaijan and urging his immediate release.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T10:56:16Z"
    }
  ]
}
```
