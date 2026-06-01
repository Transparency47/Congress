# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/208?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/208
- Title: A bill to amend the Public Health Service Act to reauthorize the Stop, Observe, Ask, and Respond to Health and Wellness Training Program.
- Congress: 119
- Bill type: S
- Bill number: 208
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-04-21T12:24:17Z
- Update date including text: 2025-04-21T12:24:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/208",
    "number": "208",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "A bill to amend the Public Health Service Act to reauthorize the Stop, Observe, Ask, and Respond to Health and Wellness Training Program.",
    "type": "S",
    "updateDate": "2025-04-21T12:24:17Z",
    "updateDateIncludingText": "2025-04-21T12:24:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T17:33:25Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s208is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 208\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Schmitt (for himself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to reauthorize the Stop, Observe, Ask, and Respond to Health and Wellness Training Program.\n#### 1. Reauthorization of the SOAR to Health and Wellness Training Program\n##### (a) In general\nSection 1254(h) of the Public Health Service Act ( 42 U.S.C. 300d\u201354(h) ) is amended by striking fiscal years 2020 through 2024 and inserting fiscal years 2025 through 2029 .\n##### (b) Rescission of funds\nOf the unobligated balances in the Nonrecurring Expenses Fund (009\u201390\u20130125) of the Department of Health and Human Services, there is rescinded $20,000,000.",
      "versionDate": "2025-01-23",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Crime victims",
            "updateDate": "2025-03-21T19:21:35Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-03-21T19:20:55Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-03-21T19:21:01Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-03-21T19:20:34Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-03-21T19:20:41Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-03-21T19:20:49Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-03-21T19:21:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-01T14:28:36Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s208is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to reauthorize the Stop, Observe, Ask, and Respond to Health and Wellness Training Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:22Z"
    },
    {
      "title": "A bill to amend the Public Health Service Act to reauthorize the Stop, Observe, Ask, and Respond to Health and Wellness Training Program.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T11:56:28Z"
    }
  ]
}
```
