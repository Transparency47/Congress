# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4410?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4410
- Title: A bill to amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.
- Congress: 119
- Bill type: S
- Bill number: 4410
- Origin chamber: Senate
- Introduced date: 2026-04-28
- Update date: 2026-05-21T16:55:45Z
- Update date including text: 2026-05-21T16:55:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in Senate
- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S2083)
- Latest action: 2026-04-28: Introduced in Senate

## Actions

- 2026-04-28 - IntroReferral: Introduced in Senate
- 2026-04-28 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S2083)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4410",
    "number": "4410",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "A bill to amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.",
    "type": "S",
    "updateDate": "2026-05-21T16:55:45Z",
    "updateDateIncludingText": "2026-05-21T16:55:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S2083)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T20:34:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "WY"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "UT"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4410is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4410\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2026 Mr. Barrasso (for himself, Ms. Lummis , and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.\n#### 1. Bonus payments for certain coal leases issued under Mineral Leasing Act\nSection 2(a) of the Mineral Leasing Act ( 30 U.S.C. 201(a) ) is amended by adding at the end the following:\n(6) The bonus payments for a lease issued under this subsection under a system of deferred bonus payment shall be payable in 10 equal annual installments, the first of which shall be submitted with the bid for such lease. .",
      "versionDate": "2026-04-28",
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
        "actionDate": "2026-03-25",
        "text": "Subcommittee Hearings Held"
      },
      "number": "7872",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.",
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
        "name": "Energy",
        "updateDate": "2026-05-21T16:55:45Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4410is.xml"
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
      "title": "A bill to amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T02:48:34Z"
    },
    {
      "title": "A bill to amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T10:56:27Z"
    }
  ]
}
```
