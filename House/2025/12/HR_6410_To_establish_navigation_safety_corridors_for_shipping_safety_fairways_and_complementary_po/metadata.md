# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6410?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6410
- Title: Atlantic Coast Shipping Safety Act
- Congress: 119
- Bill type: HR
- Bill number: 6410
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-02-03T09:05:43Z
- Update date including text: 2026-02-03T09:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6410",
    "number": "6410",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Atlantic Coast Shipping Safety Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:43Z",
    "updateDateIncludingText": "2026-02-03T09:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:27:57Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
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
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6410ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6410\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. Rouzer (for himself, Ms. Gillen , and Mr. Carter of Georgia ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish navigation safety corridors for shipping safety fairways and complementary port approaches, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Atlantic Coast Shipping Safety Act .\n#### 2. Port access routes\n##### (a) Regulation\nNot later than 1 year after the date of enactment of this Act, the Secretary of the department in which the Coast Guard is operating shall issue a regulation for nearshore and offshore shipping safety fairways, to include a minimum appropriate width of not less than the width proposed in the proposed rule of the Coast Guard titled Shipping Safety Fairways Along the Atlantic Coast , issued on January 19, 2024 (89 Fed. Reg. 3587).\n##### (b) Exception\nThe minimum appropriate width under subsection (a) shall not apply to connector, cut-across, or cutoff fairways, Traffic Separation Schemes, or precautionary areas.\n##### (c) Applicability\nIn issuing the regulation under subsection (a), the Secretary shall apply the regulation to the geographic area covered by the proposed rule of the Coast Guard titled Shipping Safety Fairways Along the Atlantic Coast , issued on January 19, 2024 (89 Fed. Reg. 3587).\n##### (d) Effective date\nThe regulation issued under subsection (a) shall take effect on December 31, 2026.",
      "versionDate": "2025-12-03",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-08T17:54:13Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6410ih.xml"
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
      "title": "Atlantic Coast Shipping Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Atlantic Coast Shipping Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish navigation safety corridors for shipping safety fairways and complementary port approaches, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T08:18:28Z"
    }
  ]
}
```
