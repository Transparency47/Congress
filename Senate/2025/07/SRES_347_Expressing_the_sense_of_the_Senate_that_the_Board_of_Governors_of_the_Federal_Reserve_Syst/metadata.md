# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/347?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/347
- Title: A resolution expressing the sense of the Senate that the Board of Governors of the Federal Reserve System and the Federal Open Market Committee should take immediate steps to lower interest rates to support economic growth, job creation, and affordability for American families and businesses.
- Congress: 119
- Bill type: SRES
- Bill number: 347
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2025-09-05T16:19:45Z
- Update date including text: 2025-09-05T16:19:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S4909: 1)
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S4909: 1)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/347",
    "number": "347",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "A resolution expressing the sense of the Senate that the Board of Governors of the Federal Reserve System and the Federal Open Market Committee should take immediate steps to lower interest rates to support economic growth, job creation, and affordability for American families and businesses.",
    "type": "SRES",
    "updateDate": "2025-09-05T16:19:45Z",
    "updateDateIncludingText": "2025-09-05T16:19:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S4909: 1)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
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
          "date": "2025-07-30T22:14:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres347is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 347\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Moreno submitted the following resolution; which was referred to the Committee on Banking, Housing, and Urban Affairs\nRESOLUTION\nExpressing the sense of the Senate that the Board of Governors of the Federal Reserve System and the Federal Open Market Committee should take immediate steps to lower interest rates to support economic growth, job creation, and affordability for American families and businesses.\nThat it is the sense of the Senate that the Board of Governors of the Federal Reserve System and the Federal Open Market Committee should immediately take such actions as may be necessary to reduce interest rates, especially the Federal funds rate.",
      "versionDate": "2025-07-30",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-05T16:19:45Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres347is.xml"
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
      "title": "A resolution expressing the sense of the Senate that the Board of Governors of the Federal Reserve System and the Federal Open Market Committee should take immediate steps to lower interest rates to support economic growth, job creation, and affordability for American families and businesses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:16Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate that the Board of Governors of the Federal Reserve System and the Federal Open Market Committee should take immediate steps to lower interest rates to support economic growth, job creation, and affordability for American families and businesses.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T10:56:23Z"
    }
  ]
}
```
