# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3668?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3668
- Title: A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Scotland, Connecticut.
- Congress: 119
- Bill type: S
- Bill number: 3668
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-02-11T14:47:39Z
- Update date including text: 2026-02-11T14:47:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3668",
    "number": "3668",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001169",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Murphy, Christopher [D-CT]",
        "lastName": "Murphy",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Scotland, Connecticut.",
    "type": "S",
    "updateDate": "2026-02-11T14:47:39Z",
    "updateDateIncludingText": "2026-02-11T14:47:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T18:21:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3668is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3668\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Mr. Murphy introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo direct the United States Postal Service to designate a single, unique ZIP Code for Scotland, Connecticut.\n#### 1. Single, unique ZIP code for Scotland, Connecticut\nNot later than 180 days after the date of enactment of this Act, the United States Postal Service shall designate a single, unique ZIP Code, to be numbered 06264, applicable to the area encompassing solely Scotland, Connecticut.",
      "versionDate": "2026-01-15",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-11T14:47:39Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3668is.xml"
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
      "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Scotland, Connecticut.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T05:48:26Z"
    },
    {
      "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Scotland, Connecticut.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T11:56:14Z"
    }
  ]
}
```
