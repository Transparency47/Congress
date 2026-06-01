# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8508?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8508
- Title: To amend title 23, United States Code, to provide for resilience grants for strengthening, upgrading, or improving municipal piers under the Promoting Resilient Operations for Transformative, Efficient, and Cost-saving Transportation program, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8508
- Origin chamber: House
- Introduced date: 2026-04-27
- Update date: 2026-04-28T08:06:01Z
- Update date including text: 2026-04-28T12:58:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-04-27: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-04-27: Introduced in House

## Actions

- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8508",
    "number": "8508",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "G000598",
        "district": "42",
        "firstName": "Robert",
        "fullName": "Rep. Garcia, Robert [D-CA-42]",
        "lastName": "Garcia",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To amend title 23, United States Code, to provide for resilience grants for strengthening, upgrading, or improving municipal piers under the Promoting Resilient Operations for Transformative, Efficient, and Cost-saving Transportation program, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:01Z",
    "updateDateIncludingText": "2026-04-28T12:58:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-27",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T16:05:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend title 23, United States Code, to provide for resilience grants for strengthening, upgrading, or improving municipal piers under the Promoting Resilient Operations for Transformative, Efficient, and Cost-saving Transportation program, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T08:06:01Z"
    },
    {
      "title": "To amend title 23, United States Code, to provide for resilience grants for strengthening, upgrading, or improving municipal piers under the Promoting Resilient Operations for Transformative, Efficient, and Cost-saving Transportation program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T08:06:01Z"
    }
  ]
}
```
