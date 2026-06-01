# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7872?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7872
- Title: To amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.
- Congress: 119
- Bill type: HR
- Bill number: 7872
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-05-21T16:55:32Z
- Update date including text: 2026-05-21T16:55:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-18 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-18 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-03-25 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7872",
    "number": "7872",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "To amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.",
    "type": "HR",
    "updateDate": "2026-05-21T16:55:32Z",
    "updateDateIncludingText": "2026-05-21T16:55:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
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
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy and Mineral Resources.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:01:40Z",
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
                "date": "2026-03-25T14:15:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-18T15:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7872ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7872\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Ms. Hageman introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.\n#### 1. Bonus payments for certain coal leases issued under Mineral Leasing Act\nSection 2(a) of the Mineral Leasing Act ( 30 U.S.C. 201(a) ) is amended by adding at the end the following:\n(6) The bonus payments for a lease issued under this subsection under a system of deferred bonus payment shall be payable in 10 equal annual installments, the first of which shall be submitted with the bid for such lease. .",
      "versionDate": "2026-03-09",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-04-28",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S2083)"
      },
      "number": "4410",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.",
      "type": "S"
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
            "name": "Coal",
            "updateDate": "2026-03-31T16:40:16Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-03-31T17:22:06Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-03-31T17:32:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-03-11T14:44:01Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7872ih.xml"
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
      "title": "To amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T08:18:30Z"
    },
    {
      "title": "To amend the Mineral Leasing Act to provide for the payment of bonus payments of certain coal leases issued under that Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T08:05:31Z"
    }
  ]
}
```
