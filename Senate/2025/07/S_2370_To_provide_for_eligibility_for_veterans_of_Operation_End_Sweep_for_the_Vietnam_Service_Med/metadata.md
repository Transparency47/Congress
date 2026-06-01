# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2370?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2370
- Title: A bill to provide for eligibility for veterans of Operation End Sweep for the Vietnam Service Medal.
- Congress: 119
- Bill type: S
- Bill number: 2370
- Origin chamber: Senate
- Introduced date: 2025-07-22
- Update date: 2025-12-05T21:36:18Z
- Update date including text: 2025-12-05T21:36:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in Senate
- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-07-22: Introduced in Senate

## Actions

- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2370",
    "number": "2370",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "A bill to provide for eligibility for veterans of Operation End Sweep for the Vietnam Service Medal.",
    "type": "S",
    "updateDate": "2025-12-05T21:36:18Z",
    "updateDateIncludingText": "2025-12-05T21:36:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T16:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2370is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2370\nIN THE SENATE OF THE UNITED STATES\nJuly 22, 2025 Ms. Baldwin introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo provide for eligibility for veterans of Operation End Sweep for the Vietnam Service Medal.\n#### 1. Eligibility of veterans of Operation End Sweep for Vietnam Service Medal\nThe Secretary of the military department concerned may, upon the application of an individual who is a veteran who participated in Operation End Sweep, award that individual the Vietnam Service Medal.",
      "versionDate": "2025-07-22",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-22",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "4622",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To provide for eligibility for veterans of Operation End Sweep for the Vietnam Service Medal.",
      "type": "HR"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-08-06T19:02:55Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2370is.xml"
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
      "title": "A bill to provide for eligibility for veterans of Operation End Sweep for the Vietnam Service Medal.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:18Z"
    },
    {
      "title": "A bill to provide for eligibility for veterans of Operation End Sweep for the Vietnam Service Medal.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T10:56:17Z"
    }
  ]
}
```
