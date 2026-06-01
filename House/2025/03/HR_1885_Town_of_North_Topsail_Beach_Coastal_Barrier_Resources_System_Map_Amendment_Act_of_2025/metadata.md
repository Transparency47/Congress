# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1885?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1885
- Title: Town of North Topsail Beach Coastal Barrier Resources System Map Amendment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1885
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-05-21T08:06:21Z
- Update date including text: 2025-05-21T08:06:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-05-13 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-05-20 - Committee: Subcommittee Hearings Held
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-05-13 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-05-20 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1885",
    "number": "1885",
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
    "title": "Town of North Topsail Beach Coastal Barrier Resources System Map Amendment Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-21T08:06:21Z",
    "updateDateIncludingText": "2025-05-21T08:06:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
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
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:03:45Z",
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
                "date": "2025-05-20T21:08:29Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-05-13T14:54:12Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
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
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1885ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1885\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Murphy (for himself and Mr. Rouzer ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo revise the boundaries of a unit of the John H. Chafee Coastal Barrier Resources System in Topsail, North Carolina, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Town of North Topsail Beach Coastal Barrier Resources System Map Amendment Act of 2025 .\n#### 2. Correction to map\n##### (a) In general\nNot later than 30 days after the date of enactment of this Act, the Secretary of the Interior shall make such corrections to the map described in subsection (d) as are necessary to exclude from unit L06 of the John H. Chafee Coastal Barrier Resources System each parcel in the town of North Topsail Beach, North Carolina, that is designated by local zoning ordinance for purposes other than conservation as of the date of enactment of this Act.\n##### (b) Application of correction\n**(1) In general**\nThe Secretary shall consider each parcel described in subsection (a) to meet the criteria described in subparagraph (B) of section 4(g)(1) of the Coastal Barrier Resources Act ( 16 U.S.C. 3503(g)(1) ).\n**(2) Clarification**\nThis Act applies only to areas of unit L06 that are within the municipality of the town of North Topsail Beach.\n##### (c) Definition of local zoning ordinance\nIn this section, the term local zoning ordinance means zoning regulations in effect for the town of North Topsail Beach, North Carolina, as of the date of enactment of this Act.\n##### (d) Map described\nThe map referred to in subsection (a) is a map that\u2014\n**(1)**\nis included in a set of maps as part of the John H. Chafee Coastal Barrier Resources System entitled John H. Chafee Coastal Barrier Resources System and dated November 25, 2024; and\n**(2)**\nrelates to unit L06 of the John H. Chafee Coastal Barrier Resources System.",
      "versionDate": "2025-03-05",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-20T13:06:51Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1885ih.xml"
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
      "title": "Town of North Topsail Beach Coastal Barrier Resources System Map Amendment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T03:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Town of North Topsail Beach Coastal Barrier Resources System Map Amendment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To revise the boundaries of a unit of the John H. Chafee Coastal Barrier Resources System in Topsail, North Carolina, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:58Z"
    }
  ]
}
```
