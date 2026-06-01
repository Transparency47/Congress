# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/380?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/380
- Title: A resolution urging the protection of Medicare from the devastating cuts caused by H.R. 1.
- Congress: 119
- Bill type: SRES
- Bill number: 380
- Origin chamber: Senate
- Introduced date: 2025-09-09
- Update date: 2025-12-05T22:50:49Z
- Update date including text: 2025-12-05T22:50:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in Senate
- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Referred to the Committee on Finance. (text: CR S6472)
- Latest action: 2025-09-09: Introduced in Senate

## Actions

- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Referred to the Committee on Finance. (text: CR S6472)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/380",
    "number": "380",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "A resolution urging the protection of Medicare from the devastating cuts caused by H.R. 1.",
    "type": "SRES",
    "updateDate": "2025-12-05T22:50:49Z",
    "updateDateIncludingText": "2025-12-05T22:50:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Finance. (text: CR S6472)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-09",
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
          "date": "2025-09-09T23:17:11Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres380is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 380\nIN THE SENATE OF THE UNITED STATES\nSeptember 9, 2025 Mr. Whitehouse submitted the following resolution; which was referred to the Committee on Finance\nRESOLUTION\nUrging the protection of Medicare from the devastating cuts caused by H.R. 1.\nThat\u2014\n**(1)**\nthe Senate should protect the Medicare program established under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) from devastating cuts caused by the Act entitled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 , approved July 4, 2025 ( Public Law 119\u201321 ; 139 Stat. 72) (commonly known as the One Big Beautiful Bill Act and referred to in this resolution as H.R. 1 );\n**(2)**\nthe Senate should safeguard seniors\u2019 Medicare benefits and essential social services that are jeopardized by the cuts triggered by H.R. 1; and\n**(3)**\nseniors who have paid into Medicare throughout their working lives should be protected from reckless, across-the-board cuts to their health care.",
      "versionDate": "2025-09-09",
      "versionType": "IS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-18",
        "text": "Referred to the Committee on Finance. (text: CR S6736)"
      },
      "number": "404",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution urging the protection of Medicare from the devastating cuts caused by H.R. 1.",
      "type": "SRES"
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
        "updateDate": "2025-09-23T14:59:27Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres380is.xml"
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
      "title": "A resolution urging the protection of Medicare from the devastating cuts caused by H.R. 1.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T04:48:28Z"
    },
    {
      "title": "A resolution urging the protection of Medicare from the devastating cuts caused by H.R. 1.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-10T10:56:19Z"
    }
  ]
}
```
