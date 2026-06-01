# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8762?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8762
- Title: To amend the Commodity Credit Corporation Charter Act to exclude crops used to produce biofuel with respect to an agricultural commodity.
- Congress: 119
- Bill type: HR
- Bill number: 8762
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-29T15:50:03Z
- Update date including text: 2026-05-29T15:50:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8762",
    "number": "8762",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
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
    "title": "To amend the Commodity Credit Corporation Charter Act to exclude crops used to produce biofuel with respect to an agricultural commodity.",
    "type": "HR",
    "updateDate": "2026-05-29T15:50:03Z",
    "updateDateIncludingText": "2026-05-29T15:50:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T16:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8762ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8762\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Mr. Perry introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Commodity Credit Corporation Charter Act to exclude crops used to produce biofuel with respect to an agricultural commodity.\n#### 1. Exclusion of crops used to produce biofuel with respect to agricultural commodity in Commodity Credit Corporation Charter Act\nSection 5 of the Commodity Credit Corporation Charter Act ( 15 U.S.C. 714c ) is amended by inserting or crops used to produce biofuel (including any infrastructure relating to such crops) after tobacco each place such term appears.",
      "versionDate": "2026-05-12",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-05-29T15:50:03Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8762ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Commodity Credit Corporation Charter Act to exclude crops used to produce biofuel with respect to an agricultural commodity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T05:18:40Z"
    },
    {
      "title": "To amend the Commodity Credit Corporation Charter Act to exclude crops used to produce biofuel with respect to an agricultural commodity.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T08:06:13Z"
    }
  ]
}
```
