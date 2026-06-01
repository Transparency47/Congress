# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5735?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5735
- Title: Coastal Infrastructure Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 5735
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2026-01-28T09:05:36Z
- Update date including text: 2026-01-28T09:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- 2025-12-01 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-10-10: Introduced in House

## Actions

- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- 2025-12-01 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5735",
    "number": "5735",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000602",
        "district": "4",
        "firstName": "Laura",
        "fullName": "Rep. Gillen, Laura [D-NY-4]",
        "lastName": "Gillen",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Coastal Infrastructure Improvement Act",
    "type": "HR",
    "updateDate": "2026-01-28T09:05:36Z",
    "updateDateIncludingText": "2026-01-28T09:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-01",
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
      "actionDate": "2025-10-10",
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
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-10",
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
          "date": "2025-10-10T16:31:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-12-01T20:01:22Z",
                "name": "Referred to"
              }
            },
            "name": "Water Resources and Environment Subcommittee",
            "systemCode": "hspw02"
          },
          {
            "activities": {
              "item": {
                "date": "2025-12-01T20:01:03Z",
                "name": "Referred to"
              }
            },
            "name": "Coast Guard and Maritime Transportation Subcommittee",
            "systemCode": "hspw07"
          }
        ]
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "NJ"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5735ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5735\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Ms. Gillen (for herself and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of the Army to implement a program for the testing and implementation of stabilization and erosion control technology to prevent coastal erosion.\n#### 1. Short title\nThis Act may be cited as the Coastal Infrastructure Improvement Act .\n#### 2. Stabilization and Erosion Control Technology program\n##### (a) In general\nSubject to the availability of appropriations, and for a period of 6 years beginning on the date on which funds are made available to carry out this section, the Secretary and, where appropriate, in consultation with other Federal agencies and States carrying out State management programs approved under section 306 of the Coastal Zone Management Act of 1972 ( 16 U.S.C. 1455 ), shall establish a program to carry out research and development activities relating to stabilization and erosion control technology, including the estimated cost and longevity of such technology, as\u2014\n**(1)**\nbiomimetic methods for the protection of estuaries, cliffs, bluffs, beaches, dunes, and shoreline stabilization;\n**(2)**\napplicable for coastal application in areas exposed to coastal floods and erosion hazards, including monitoring and maintenance; and\n**(3)**\nalternatives to hardened structures that are static, disruptive to local habitat, and contributive to erosion in adjacent areas.\n##### (b) Testing diversity\nThe Secretary shall ensure that research and development activities carried out under this section are carried out in diverse geographic locations.\n##### (c) Report\nNot later than 60 days after the end of the period described in subsection (a), the Secretary shall submit to the Committee on Environment and Public Works of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report on the program carried out under this section, including a comprehensive evaluation of such program and recommendations for the continuation of such program.\n##### (d) Definitions\nIn this section:\n**(1) Biomimetic method**\nThe term biomimetic method means an engineered system that mimics natural processes, is temporary, adjustable, removable, and reusable, and includes hybrid approaches that combine natural and engineered elements to enhance ecosystem function while providing protection.\n**(2) Secretary**\nThe term Secretary means the Secretary of the Army, acting through the Director of the Engineer Research and Development Center.",
      "versionDate": "2025-10-10",
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
        "updateDate": "2025-12-09T22:30:37Z"
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
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5735ih.xml"
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
      "title": "Coastal Infrastructure Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Coastal Infrastructure Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Army to implement a program for the testing and implementation of stabilization and erosion control technology to prevent coastal erosion.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T11:18:15Z"
    }
  ]
}
```
