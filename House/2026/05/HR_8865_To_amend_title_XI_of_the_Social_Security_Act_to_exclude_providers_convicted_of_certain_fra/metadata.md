# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8865?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8865
- Title: To amend title XI of the Social Security Act to exclude providers convicted of certain fraud-related criminal offenses from participation in Federal health care programs on a permanent basis.
- Congress: 119
- Bill type: HR
- Bill number: 8865
- Origin chamber: House
- Introduced date: 2026-05-15
- Update date: 2026-05-16T08:07:13Z
- Update date including text: 2026-05-16T10:58:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-15: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-05-15: Introduced in House

## Actions

- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-15",
    "latestAction": {
      "actionDate": "2026-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8865",
    "number": "8865",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001212",
        "district": "8",
        "firstName": "Pete",
        "fullName": "Rep. Stauber, Pete [R-MN-8]",
        "lastName": "Stauber",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "To amend title XI of the Social Security Act to exclude providers convicted of certain fraud-related criminal offenses from participation in Federal health care programs on a permanent basis.",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:13Z",
    "updateDateIncludingText": "2026-05-16T10:58:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-15",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-15",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-15",
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
          "date": "2026-05-15T13:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-15T13:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend title XI of the Social Security Act to exclude providers convicted of certain fraud-related criminal offenses from participation in Federal health care programs on a permanent basis.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-16T08:07:13Z"
    },
    {
      "title": "To amend title XI of the Social Security Act to exclude providers convicted of certain fraud-related criminal offenses from participation in Federal health care programs on a permanent basis.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-16T08:07:13Z"
    }
  ]
}
```
