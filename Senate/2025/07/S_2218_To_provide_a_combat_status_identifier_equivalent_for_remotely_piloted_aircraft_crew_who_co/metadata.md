# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2218?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2218
- Title: Combat Action Recognition and Evaluation (CARE) for Remotely Piloted Aircraft (RPA) Crews Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2218
- Origin chamber: Senate
- Introduced date: 2025-07-09
- Update date: 2025-09-04T15:24:53Z
- Update date including text: 2025-09-04T15:24:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-09: Introduced in Senate
- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-07-09: Introduced in Senate

## Actions

- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-09",
    "latestAction": {
      "actionDate": "2025-07-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2218",
    "number": "2218",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Combat Action Recognition and Evaluation (CARE) for Remotely Piloted Aircraft (RPA) Crews Act of 2025",
    "type": "S",
    "updateDate": "2025-09-04T15:24:53Z",
    "updateDateIncludingText": "2025-09-04T15:24:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-09",
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
      "actionDate": "2025-07-09",
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
          "date": "2025-07-09T15:31:20Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2218is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2218\nIN THE SENATE OF THE UNITED STATES\nJuly 9, 2025 Ms. Rosen (for herself and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo provide a combat status identifier equivalent for remotely piloted aircraft crew who conduct combat operations.\n#### 1. Short title\nThis Act may be cited as the Combat Action Recognition and Evaluation (CARE) for Remotely Piloted Aircraft (RPA) Crews Act of 2025 .\n#### 2. Combat status identifier equivalent for remotely piloted aircraft crew\nNot later than 180 days after the date of the enactment of this Act, the Secretaries of the military departments shall establish a status identifier of equivalent merit as a combat status identifier for remotely piloted aircraft (RPA) crew who conduct combat operations.",
      "versionDate": "2025-07-09",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-04T15:24:53Z"
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
      "date": "2025-07-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2218is.xml"
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
      "title": "Combat Action Recognition and Evaluation (CARE) for Remotely Piloted Aircraft (RPA) Crews Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T02:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Combat Action Recognition and Evaluation (CARE) for Remotely Piloted Aircraft (RPA) Crews Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide a combat status identifier equivalent for remotely piloted aircraft crew who conduct combat operations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T02:18:33Z"
    }
  ]
}
```
