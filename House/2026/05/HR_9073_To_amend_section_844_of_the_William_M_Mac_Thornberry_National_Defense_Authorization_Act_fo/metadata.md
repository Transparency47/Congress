# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9073?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9073
- Title: To amend section 844 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 to change the applicability of the amendments made by such section, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 9073
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:06:10Z
- Update date including text: 2026-05-30T09:28:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-05-29: Introduced in House

## Actions

- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-29",
    "latestAction": {
      "actionDate": "2026-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9073",
    "number": "9073",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "O000176",
        "district": "2",
        "firstName": "Johnny",
        "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
        "lastName": "Olszewski",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "To amend section 844 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 to change the applicability of the amendments made by such section, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:10Z",
    "updateDateIncludingText": "2026-05-30T09:28:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-29",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-29",
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
          "date": "2026-05-29T16:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "VA"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend section 844 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 to change the applicability of the amendments made by such section, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:06:10Z"
    },
    {
      "title": "To amend section 844 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 to change the applicability of the amendments made by such section, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:06:10Z"
    }
  ]
}
```
