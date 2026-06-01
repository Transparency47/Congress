# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/257?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/257
- Title: A resolution expressing the sense of the Senate concerning the arrest and continued detention of Ekrem Imamoglu and urging the Government of Turkiye to uphold democratic values.
- Congress: 119
- Bill type: SRES
- Bill number: 257
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-06-20T13:28:31Z
- Update date including text: 2025-06-20T13:28:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S3125)
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S3125)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/257",
    "number": "257",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "A resolution expressing the sense of the Senate concerning the arrest and continued detention of Ekrem Imamoglu and urging the Government of Turkiye to uphold democratic values.",
    "type": "SRES",
    "updateDate": "2025-06-20T13:28:31Z",
    "updateDateIncludingText": "2025-06-20T13:28:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S3125)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T20:19:34Z",
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
      "sponsorshipDate": "2025-05-22",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres257is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 257\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Schiff (for himself and Mr. Durbin ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the sense of the Senate concerning the arrest and continued detention of Ekrem \u0130mamo\u011flu and urging the Government of T\u00fcrkiye to uphold democratic values.\nThat the Senate\u2014\n**(1)**\ncalls on President Erdo\u011fan and law enforcement authorities in T\u00fcrkiye to present any credible evidence against Ekrem \u0130mamo\u011flu or immediately release him from detention;\n**(2)**\nurges the Government of T\u00fcrkiye to uphold democratic values, including free and fair elections; and\n**(3)**\nurges the Secretary of State to issue forceful and timely statements and to engage diplomatically with the Government of T\u00fcrkiye over anti-democratic behavior.",
      "versionDate": "2025-05-22",
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
        "updateDate": "2025-06-20T13:28:31Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres257is.xml"
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
      "title": "A resolution expressing the sense of the Senate concerning the arrest and continued detention of Ekrem Imamoglu and urging the Government of Turkiye to uphold democratic values.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-24T03:33:31Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate concerning the arrest and continued detention of Ekrem Imamoglu and urging the Government of Turkiye to uphold democratic values.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-23T10:56:32Z"
    }
  ]
}
```
