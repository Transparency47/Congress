# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4931?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4931
- Title: National Park System Long-Term Lease Investment Act
- Congress: 119
- Bill type: HR
- Bill number: 4931
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2026-01-23T18:24:53Z
- Update date including text: 2026-01-23T18:24:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-25 - Committee: Referred to the Subcommittee on Federal Lands.
- 2025-12-02 - Committee: Subcommittee Hearings Held
- Latest action: 2025-08-08: Introduced in House

## Actions

- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-25 - Committee: Referred to the Subcommittee on Federal Lands.
- 2025-12-02 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4931",
    "number": "4931",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "National Park System Long-Term Lease Investment Act",
    "type": "HR",
    "updateDate": "2026-01-23T18:24:53Z",
    "updateDateIncludingText": "2026-01-23T18:24:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
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
      "actionDate": "2025-11-25",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
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
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:31:00Z",
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
                "date": "2025-12-02T15:15:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-11-25T19:21:56Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4931ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4931\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Murphy introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo authorize the Secretary of the Interior to extend certain leases within units of the National Park System without opening the lease to bidding.\n#### 1. Short title\nThis Act may be cited as the National Park System Long-Term Lease Investment Act .\n#### 2. Authorization to extend certain leases\n##### (a) In general\nThe Secretary of the Interior, acting through the Director of the National Park Service, may extend a lease entered into under part 18 of title 36, Code of Federal Regulations (as in effect on January 3, 2025), without complying with the requirements of sections 18.7 or 18.8 of that part, if\u2014\n**(1)**\nthe lessee\u2014\n**(A)**\nentered into the lease not less than 5 years before the date on which the extension takes effect; and\n**(B)**\nis in compliance with the terms and conditions of the lease; and\n**(2)**\nthe Director of the National Park Service determines that extending the lease is in the best interests of the administration of the applicable unit of the National Park System.\n##### (b) Revision of regulation\nNot later than 90 days after the date of the enactment of this Act, the Secretary of the Interior shall revise part 18 of title 36, Code of Federal Regulations, to reflect the authority granted under subsection (a).",
      "versionDate": "2025-08-08",
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
        "actionDate": "2025-07-29",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "2498",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Park System Long-Term Lease Investment Act",
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
            "name": "Land use and conservation",
            "updateDate": "2026-01-23T18:24:53Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-01-23T18:24:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-18T16:25:22Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4931ih.xml"
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
      "title": "National Park System Long-Term Lease Investment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T03:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Park System Long-Term Lease Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of the Interior to extend certain leases within units of the National Park System without opening the lease to bidding.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:35Z"
    }
  ]
}
```
