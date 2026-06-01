# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2899?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2899
- Title: Rail Service Continuity and Stability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2899
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2025-12-16T17:07:07Z
- Update date including text: 2025-12-16T17:07:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2899",
    "number": "2899",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Rail Service Continuity and Stability Act of 2025",
    "type": "S",
    "updateDate": "2025-12-16T17:07:07Z",
    "updateDateIncludingText": "2025-12-16T17:07:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T20:41:02Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2899is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2899\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Sheehy introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo authorize additional appropriations to Amtrak for long-distance routes.\n#### 1. Short title\nThis Act may be cited as the Rail Service Continuity and Stability Act of 2025 .\n#### 2. Additional appropriations to Amtrak for long-distance routes\nThere are authorized to be appropriated to Amtrak such additional sums as may be necessary to support service for long-distance routes (as that term is defined in section 24102 of title 49, United States Code) existing on the date of the enactment of this Act.",
      "versionDate": "2025-09-18",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-16T17:07:07Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2899is.xml"
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
      "title": "Rail Service Continuity and Stability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rail Service Continuity and Stability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize additional appropriations to Amtrak for long-distance routes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T05:48:13Z"
    }
  ]
}
```
