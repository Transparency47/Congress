# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4629?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4629
- Title: A bill to prohibit the provision of Federal funds to State and local governments and school districts for payment of obligations, to prohibit the Federal Reserve banks, the Department of the Treasury, and other Federal agencies from financially assisting State and local governments and school districts that have defaulted on their obligations, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4629
- Origin chamber: Senate
- Introduced date: 2026-05-21
- Update date: 2026-05-22T10:56:36Z
- Update date including text: 2026-05-22T10:56:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-21: Introduced in Senate
- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-05-21: Introduced in Senate

## Actions

- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4629",
    "number": "4629",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "A bill to prohibit the provision of Federal funds to State and local governments and school districts for payment of obligations, to prohibit the Federal Reserve banks, the Department of the Treasury, and other Federal agencies from financially assisting State and local governments and school districts that have defaulted on their obligations, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-22T10:56:36Z",
    "updateDateIncludingText": "2026-05-22T10:56:36Z"
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
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-21",
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
          "date": "2026-05-21T17:26:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "AR"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A bill to prohibit the provision of Federal funds to State and local governments and school districts for payment of obligations, to prohibit the Federal Reserve banks, the Department of the Treasury, and other Federal agencies from financially assisting State and local governments and school districts that have defaulted on their obligations, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:56:36Z"
    },
    {
      "title": "A bill to prohibit the provision of Federal funds to State and local governments and school districts for payment of obligations, to prohibit the Federal Reserve banks, the Department of the Treasury, and other Federal agencies from financially assisting State and local governments and school districts that have defaulted on their obligations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:56:36Z"
    }
  ]
}
```
