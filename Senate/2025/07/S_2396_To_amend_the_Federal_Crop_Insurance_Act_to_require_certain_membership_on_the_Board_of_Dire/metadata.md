# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2396?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2396
- Title: Farm Board Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2396
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2025-08-07T16:46:44Z
- Update date including text: 2025-08-07T16:46:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2396",
    "number": "2396",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
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
    "title": "Farm Board Act of 2025",
    "type": "S",
    "updateDate": "2025-08-07T16:46:44Z",
    "updateDateIncludingText": "2025-08-07T16:46:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T16:08:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2396is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2396\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Tuberville introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Federal Crop Insurance Act to require certain membership on the Board of Directors of the Federal Crop Insurance Corporation.\n#### 1. Short title\nThis Act may be cited as the Farm Board Act of 2025 .\n#### 2. Board of Directors composition\nSection 505(a)(2)(G) of the Federal Crop Insurance Act ( 7 U.S.C. 1505(a)(2)(G) ) is amended by striking at least one specialty crop producer. and inserting the following:\nat least\u2014 (i) 1 specialty crop producer; and (ii) beginning with the Board of Directors serving on or after May 1, 2027, 1 producer that actively engages in livestock production and crop production of agricultural commodities. .",
      "versionDate": "2025-07-23",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-08-07T16:46:44Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2396is.xml"
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
      "title": "Farm Board Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Farm Board Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Crop Insurance Act to require certain membership on the Board of Directors of the Federal Crop Insurance Corporation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T05:03:38Z"
    }
  ]
}
```
