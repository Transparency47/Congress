# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7582?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7582
- Title: CAR Act
- Congress: 119
- Bill type: HR
- Bill number: 7582
- Origin chamber: House
- Introduced date: 2026-02-13
- Update date: 2026-03-11T23:02:00Z
- Update date including text: 2026-03-11T23:02:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-13: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-13: Introduced in House

## Actions

- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-13",
    "latestAction": {
      "actionDate": "2026-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7582",
    "number": "7582",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "CAR Act",
    "type": "HR",
    "updateDate": "2026-03-11T23:02:00Z",
    "updateDateIncludingText": "2026-03-11T23:02:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-13",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-02-13T15:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7582ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7582\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2026 Mr. Perry introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude automobiles from being treated as collectibles for purposes of capital gains tax, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Collector Automobile Relief Act or the CAR Act .\n#### 2. Automobiles not treated as collectibles for purposes of capital gains tax\n##### (a) In general\nSection 1(h)(5)(A) of the Internal Revenue Code of 1986 is amended by inserting and excluding automobiles after collectible (as defined in section 408(m) without regard to paragraph (3) thereof .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-02-13",
      "versionType": "Introduced in House"
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
        "name": "Taxation",
        "updateDate": "2026-03-11T23:02:00Z"
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
      "date": "2026-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7582ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "CAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T06:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T06:23:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Collector Automobile Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T06:23:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude automobiles from being treated as collectibles for purposes of capital gains tax, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T06:18:27Z"
    }
  ]
}
```
