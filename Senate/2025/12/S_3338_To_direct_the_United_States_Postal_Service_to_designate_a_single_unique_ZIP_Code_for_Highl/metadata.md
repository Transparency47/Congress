# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3338?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3338
- Title: A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Highland City, Utah.
- Congress: 119
- Bill type: S
- Bill number: 3338
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-04-16T19:21:58Z
- Update date including text: 2026-04-16T19:21:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3338",
    "number": "3338",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Highland City, Utah.",
    "type": "S",
    "updateDate": "2026-04-16T19:21:58Z",
    "updateDateIncludingText": "2026-04-16T19:21:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T22:14:42Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3338is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3338\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Mr. Curtis (for himself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo direct the United States Postal Service to designate a single, unique ZIP Code for Highland City, Utah.\n#### 1. Single, unique ZIP Code for Highland City, Utah\nNot later than 270 days after the date of enactment of this Act, the United States Postal Service shall designate a single, unique ZIP Code applicable to the area encompassing solely Highland City, Utah.",
      "versionDate": "2025-12-03",
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
        "actionDate": "2026-03-18",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0."
      },
      "number": "6399",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Highland City, Utah.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Postal service",
            "updateDate": "2026-04-16T19:21:57Z"
          },
          {
            "name": "Utah",
            "updateDate": "2026-04-16T19:21:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-06T22:01:11Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3338is.xml"
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
      "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Highland City, Utah.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-24T04:03:24Z"
    },
    {
      "title": "A bill to direct the United States Postal Service to designate a single, unique ZIP Code for Highland City, Utah.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T11:56:22Z"
    }
  ]
}
```
