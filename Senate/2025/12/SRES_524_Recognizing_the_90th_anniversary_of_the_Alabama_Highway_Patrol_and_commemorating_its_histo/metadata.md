# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/524?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/524
- Title: A resolution recognizing the 90th anniversary of the Alabama Highway Patrol and commemorating its history of excellence.
- Congress: 119
- Bill type: SRES
- Bill number: 524
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2025-12-05T15:29:10Z
- Update date including text: 2025-12-05T15:29:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S8485)
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S8485)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/524",
    "number": "524",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "A resolution recognizing the 90th anniversary of the Alabama Highway Patrol and commemorating its history of excellence.",
    "type": "SRES",
    "updateDate": "2025-12-05T15:29:10Z",
    "updateDateIncludingText": "2025-12-05T15:29:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S8485)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:39:48Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres524is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 524\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Mr. Tuberville submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing the 90th anniversary of the Alabama Highway Patrol and commemorating its history of excellence.\nThat the Senate\u2014\n**(1)**\ncommemorates the 90th Anniversary of the Alabama Highway Patrol; and\n**(2)**\nextends gratitude and commendation for the Alabama Highway Patrol's 9 decades of exceptional service and devotion to the State of Alabama.",
      "versionDate": "2025-12-03",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-05T15:29:10Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres524is.xml"
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
      "title": "A resolution recognizing the 90th anniversary of the Alabama Highway Patrol and commemorating its history of excellence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T14:33:50Z"
    },
    {
      "title": "A resolution recognizing the 90th anniversary of the Alabama Highway Patrol and commemorating its history of excellence.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T11:56:22Z"
    }
  ]
}
```
