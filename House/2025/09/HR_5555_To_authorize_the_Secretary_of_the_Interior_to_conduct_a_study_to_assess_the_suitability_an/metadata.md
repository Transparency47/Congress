# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5555?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5555
- Title: Monterey Bay National Heritage Area Study Act
- Congress: 119
- Bill type: HR
- Bill number: 5555
- Origin chamber: House
- Introduced date: 2025-09-23
- Update date: 2026-03-30T18:16:14Z
- Update date including text: 2026-03-30T18:16:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-23: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-11 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-03-18 - Committee: Subcommittee Hearings Held
- Latest action: 2025-09-23: Introduced in House

## Actions

- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-11 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-03-18 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-23",
    "latestAction": {
      "actionDate": "2025-09-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5555",
    "number": "5555",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Monterey Bay National Heritage Area Study Act",
    "type": "HR",
    "updateDate": "2026-03-30T18:16:14Z",
    "updateDateIncludingText": "2026-03-30T18:16:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
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
      "actionDate": "2026-03-11",
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
      "actionDate": "2025-09-23",
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
      "actionDate": "2025-09-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-23",
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
          "date": "2025-09-23T13:00:15Z",
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
                "date": "2026-03-18T14:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-11T14:00:00Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "CA"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "CA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5555ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5555\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 23, 2025 Mr. Panetta (for himself, Mr. Mullin , Mr. Carbajal , Ms. Lofgren , and Mr. Liccardo ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo authorize the Secretary of the Interior to conduct a study to assess the suitability and feasibility of designating certain land in California as the Monterey Bay National Heritage Area, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Monterey Bay National Heritage Area Study Act .\n#### 2. Study\n##### (a) In general\nThe Secretary of the Interior, in consultation with the State of California, local organizations and governmental agencies, Tribal Governments, nonprofit organizations, and other appropriate entities, including the Monterey Bay Economic Partnership, shall conduct a study to assess the suitability and feasibility of designating the areas described in subsection (b) as a National Heritage Area, to be known as the Monterey Bay National Heritage Area .\n##### (b) Description of study area\nThe areas to be studied under subsection (a) include\u2014\n**(1)**\nMonterey, San Mateo, Santa Cruz, and San Luis Obispo counties in the State of California; and\n**(2)**\nany other area in the State of California that\u2014\n**(A)**\nhas heritage aspects that are similar to the heritage aspects of an area described in paragraph (1); and\n**(B)**\nis adjacent to, or in the vicinity of, an area described in paragraph (1).\n##### (c) Applicable Law\nThe study required under subsection (a) shall be conducted in accordance with section 120103(a) of title 54, United States Code.",
      "versionDate": "2025-09-23",
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
            "name": "California",
            "updateDate": "2026-03-30T18:15:54Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-03-30T18:15:59Z"
          },
          {
            "name": "Historic sites and heritage areas",
            "updateDate": "2026-03-30T18:16:03Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-03-30T18:16:14Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-03-30T18:16:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-01T17:11:17Z"
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
      "date": "2025-09-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5555ih.xml"
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
      "title": "Monterey Bay National Heritage Area Study Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Monterey Bay National Heritage Area Study Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of the Interior to conduct a study to assess the suitability and feasibility of designating certain land in California as the Monterey Bay National Heritage Area, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:14Z"
    }
  ]
}
```
