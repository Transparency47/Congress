# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3004?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3004
- Title: Upper Price River Watershed Project Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3004
- Origin chamber: Senate
- Introduced date: 2025-10-14
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-14: Introduced in Senate
- 2025-10-14 - IntroReferral: Introduced in Senate
- 2025-10-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-10-14: Introduced in Senate

## Actions

- 2025-10-14 - IntroReferral: Introduced in Senate
- 2025-10-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-14",
    "latestAction": {
      "actionDate": "2025-10-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3004",
    "number": "3004",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Upper Price River Watershed Project Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-14",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-14",
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
        "item": [
          {
            "date": "2026-03-04T16:02:24Z",
            "name": "Markup By"
          },
          {
            "date": "2025-10-14T19:25:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T15:00:34Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3004is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3004\nIN THE SENATE OF THE UNITED STATES\nOctober 14, 2025 Mr. Lee (for himself and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo direct the Secretary of the Interior to convey certain Bureau of Land Management land to the city of Price, Utah, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Upper Price River Watershed Project Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) City**\nThe term City means the city of Price, Utah.\n**(2) Federal land**\nThe term Federal land means the approximately 124.23 acres of Bureau of Land Management land in the State of Utah depicted as Proposed Conveyance Parcels on the Map.\n**(3) Map**\nThe term Map means the map prepared by the Bureau of Land Management entitled Land Conveyance near Price, Utah and dated May 8, 2025.\n**(4) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the Bureau of Land Management.\n#### 3. Conveyance of certain Bureau of Land Management land to the city of Price, Utah\n##### (a) In general\nNotwithstanding sections 202 and 203 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1712 , 1713) and subject to valid existing rights, at the request of the City, the Secretary shall convey to the City all right, title, and interest of the United States in and to the Federal land, to be used by the City for public purposes, as defined by the City.\n##### (b) Map\n**(1) Availability**\nThe Map shall be on file and available for public inspection in the appropriate offices of the Bureau of Land Management.\n**(2) Minor errors**\nThe Secretary may correct any minor errors in the Map.",
      "versionDate": "2025-10-14",
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
        "actionDate": "2025-10-14",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "5752",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Upper Price River Watershed Project Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Geography and mapping",
            "updateDate": "2026-02-27T17:59:57Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-02-27T18:00:02Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-02-27T17:59:52Z"
          },
          {
            "name": "Utah",
            "updateDate": "2026-02-27T17:59:47Z"
          },
          {
            "name": "Water storage",
            "updateDate": "2026-02-27T18:00:07Z"
          },
          {
            "name": "Watersheds",
            "updateDate": "2026-02-27T18:00:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-02T17:49:23Z"
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
      "date": "2025-10-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3004is.xml"
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
      "title": "Upper Price River Watershed Project Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Upper Price River Watershed Project Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of the Interior to convey certain Bureau of Land Management land to the city of Price, Utah, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:14Z"
    }
  ]
}
```
