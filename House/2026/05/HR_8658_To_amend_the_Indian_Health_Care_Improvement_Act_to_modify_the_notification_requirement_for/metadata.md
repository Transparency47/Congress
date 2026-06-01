# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8658?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8658
- Title: To amend the Indian Health Care Improvement Act to modify the notification requirement for emergency contract health services for certain beneficiaries, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8658
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-27T08:05:59Z
- Update date including text: 2026-05-27T08:05:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-04 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2026-05-21 - Committee: Subcommittee Hearings Held
- Latest action: 2026-05-04: Introduced in House

## Actions

- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-04 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2026-05-21 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-04",
    "latestAction": {
      "actionDate": "2026-05-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8658",
    "number": "8658",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "K000403",
        "district": "3",
        "firstName": "Mike",
        "fullName": "Rep. Kennedy, Mike [R-UT-3]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "To amend the Indian Health Care Improvement Act to modify the notification requirement for emergency contract health services for certain beneficiaries, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:59Z",
    "updateDateIncludingText": "2026-05-27T08:05:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-04",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-04",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-04",
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
          "date": "2026-05-04T14:33:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-05-21T18:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-05-12T21:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-04T14:33:05Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "CO"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend the Indian Health Care Improvement Act to modify the notification requirement for emergency contract health services for certain beneficiaries, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T08:05:37Z"
    },
    {
      "title": "To amend the Indian Health Care Improvement Act to modify the notification requirement for emergency contract health services for certain beneficiaries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T08:05:37Z"
    }
  ]
}
```
