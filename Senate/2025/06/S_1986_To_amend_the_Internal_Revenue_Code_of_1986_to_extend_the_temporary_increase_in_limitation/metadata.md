# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1986?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1986
- Title: A bill to amend the Internal Revenue Code of 1986 to extend the temporary increase in limitation on the cover over of distilled spirits taxes to Puerto Rico and the Virgin Islands.
- Congress: 119
- Bill type: S
- Bill number: 1986
- Origin chamber: Senate
- Introduced date: 2025-06-09
- Update date: 2025-12-05T21:52:26Z
- Update date including text: 2025-12-05T21:52:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in Senate
- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-09: Introduced in Senate

## Actions

- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1986",
    "number": "1986",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to extend the temporary increase in limitation on the cover over of distilled spirits taxes to Puerto Rico and the Virgin Islands.",
    "type": "S",
    "updateDate": "2025-12-05T21:52:26Z",
    "updateDateIncludingText": "2025-12-05T21:52:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-09",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-09",
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
          "date": "2025-06-09T21:22:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1986is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1986\nIN THE SENATE OF THE UNITED STATES\nJune 9, 2025 Mr. Cassidy introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the temporary increase in limitation on the cover over of distilled spirits taxes to Puerto Rico and the Virgin Islands.\n#### 1. Extension of temporary increase on cover over of distilled spirits taxes to Puerto Rico and Virgin Islands\n##### (a) In general\nSection 7652(f)(1) of the Internal Revenue Code of 1986 is amended by striking January 1, 2022 and inserting January 1, 2032 .\n##### (b) Effective date\nThe amendments made by this section shall apply to distilled spirits brought into the United States after December 31, 2021.",
      "versionDate": "2025-06-09",
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
        "actionDate": "2025-02-14",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1378",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to extend the temporary increase in limitation on the cover over of distilled spirits taxes to Puerto Rico and the Virgin Islands.",
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
        "name": "Taxation",
        "updateDate": "2025-06-30T15:53:24Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1986is.xml"
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
      "title": "A bill to amend the Internal Revenue Code of 1986 to extend the temporary increase in limitation on the cover over of distilled spirits taxes to Puerto Rico and the Virgin Islands.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T03:33:15Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to extend the temporary increase in limitation on the cover over of distilled spirits taxes to Puerto Rico and the Virgin Islands.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-10T10:56:18Z"
    }
  ]
}
```
