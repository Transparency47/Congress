# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5063?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5063
- Title: Safe Beaches, Safe Swimmers Act
- Congress: 119
- Bill type: HR
- Bill number: 5063
- Origin chamber: House
- Introduced date: 2025-08-29
- Update date: 2026-01-07T16:59:02Z
- Update date including text: 2026-01-07T16:59:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-29: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-25 - Committee: Referred to the Subcommittee on Federal Lands.
- 2025-12-02 - Committee: Subcommittee Hearings Held
- Latest action: 2025-08-29: Introduced in House

## Actions

- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-25 - Committee: Referred to the Subcommittee on Federal Lands.
- 2025-12-02 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-29",
    "latestAction": {
      "actionDate": "2025-08-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5063",
    "number": "5063",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Safe Beaches, Safe Swimmers Act",
    "type": "HR",
    "updateDate": "2026-01-07T16:59:02Z",
    "updateDateIncludingText": "2026-01-07T16:59:02Z"
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
      "actionDate": "2025-08-29",
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
      "actionDate": "2025-08-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-29",
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
          "date": "2025-08-29T17:31:10Z",
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
                "date": "2025-11-25T19:23:49Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5063ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5063\nIN THE HOUSE OF REPRESENTATIVES\nAugust 29, 2025 Mrs. Kiggans of Virginia introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo ensure continuity of staffing at Federal beaches, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Beaches, Safe Swimmers Act .\n#### 2. Adequate lifeguard staffing at Federal swimming areas and beaches\n##### (a) In general\nIf the Secretary determines there is a staffing shortage with respect to a designated swim location, the Secretary shall seek to enter into an agreement with one or more local government agencies to enable lifeguards employed by those local government agencies to\u2014\n**(1)**\nadequately staff such designated swim location during normal seasonal operating hours; and\n**(2)**\nensure visitor safety and provide rescue and first aid services at the designated swim location as necessary.\n##### (b) Reimbursement\n**(1) In general**\nIn entering into an agreement under subsection (a), the Secretary shall ensure that the local government agency providing the lifeguard services is reimbursed for all reasonable costs incurred by the local government agency in carrying out the agreement.\n**(2) Current agreements**\nIf an agreement has been entered into by the Secretary and a local government agency for lifeguard services at a designated swim location on or before the date of the enactment of this Act, the Secretary shall amend such agreement as necessary to provide for the reimbursement of the local government agency for all reasonable costs incurred by the local government agency in carrying out the agreement, regardless of the terms of the original agreement relating to cost sharing.\n##### (c) Definitions\nIn this section:\n**(1) Designated swim location**\nThe term designated swim location means a swimming area or swimming beach\u2014\n**(A)**\non lands and waters managed by the National Park Service, the United States Fish and Wildlife Service, the Bureau of Land Management, or the Bureau of Reclamation; and\n**(B)**\nthat is typically monitored by federally employed lifeguards during normal seasonal operating hours.\n**(2) Staffing shortage**\n**(A) In general**\nThe term staffing shortage means a level of staffing that negatively impacts the ability to adequately staff a designated swim location with federally employed lifeguards and will likely result or has resulted in a designated swim location being left unmonitored by federally employed lifeguards during normal seasonal operating hours.\n**(B) Exclusion**\nThe term staffing shortage does not refer to short-term staffing shortages caused by temporary absences, such as an employee taking annual or sick leave.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.",
      "versionDate": "2025-08-29",
      "versionType": "Introduced in House"
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
            "name": "First responders and emergency personnel",
            "updateDate": "2026-01-07T16:58:51Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-01-07T16:58:57Z"
          },
          {
            "name": "Migrant, seasonal, agricultural labor",
            "updateDate": "2026-01-07T16:59:02Z"
          },
          {
            "name": "Seashores and lakeshores",
            "updateDate": "2026-01-07T16:58:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-12T18:53:41Z"
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
      "date": "2025-08-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5063ih.xml"
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
      "title": "Safe Beaches, Safe Swimmers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Beaches, Safe Swimmers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure continuity of staffing at Federal beaches, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-03T04:18:20Z"
    }
  ]
}
```
