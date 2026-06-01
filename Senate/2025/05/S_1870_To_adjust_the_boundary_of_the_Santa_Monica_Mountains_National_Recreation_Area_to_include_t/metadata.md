# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1870?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1870
- Title: Rim of the Valley Corridor Preservation Act
- Congress: 119
- Bill type: S
- Bill number: 1870
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1870",
    "number": "1870",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Rim of the Valley Corridor Preservation Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T16:29:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T18:13:09Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1870is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1870\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Schiff (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo adjust the boundary of the Santa Monica Mountains National Recreation Area to include the Rim of the Valley Corridor, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rim of the Valley Corridor Preservation Act .\n#### 2. Boundary adjustment\nSection 507(c) of the National Parks and Recreation Act of 1978 ( 16 U.S.C. 460kk(c) ) is amended by striking paragraph (1) and inserting the following:\n(1) Boundary (A) In general The recreation area shall consist of\u2014 (i) the land, water, and interests in land and water generally depicted as the recreation area on the map entitled Santa Monica Mountains National Recreation Area and Santa Monica Mountains Zone, California, Boundary Map , numbered 80,047\u2013C, and dated August 2001; and (ii) the land, water, and interests in land and water, as generally depicted as Rim of the Valley Unit Proposed Addition on the map entitled Proposed Addition - Rim of the Valley Unit Santa Monica Mountains National Recreation Area , numbered 638/179670x, and dated April 14, 2023. (B) Availability of maps The maps described in subparagraph (A) shall be on file and available for public inspection in the appropriate offices of the National Park Service. (C) Revisions After advising the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives, in writing, of the proposed revision, the Secretary may make minor revisions to the boundaries of the recreation area by publication of a revised drawing or other boundary description in the Federal Register. .\n#### 3. Administration\nAny land or interest in land acquired by the Secretary of the Interior within the Rim of the Valley Unit shall be administered as part of the Santa Monica Mountains National Recreation Area (referred to in this Act as the National Recreation Area ) in accordance with the laws (including regulations) applicable to the National Recreation Area.\n#### 4. Utilities and water resource facilities\nThe addition of the Rim of the Valley Unit to the National Recreation Area shall not affect the operation, maintenance, or modification of water resource facilities or public utilities within the Rim of the Valley Unit, except that any utility or water resource facility activities in the Rim of the Valley Unit shall be conducted in a manner that reasonably avoids or reduces the impact of the activities on resources of the Rim of the Valley Unit.",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-06-10",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "3874",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Rim of the Valley Corridor Preservation Act",
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
            "name": "California",
            "updateDate": "2025-12-16T15:42:35Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-12-16T15:42:35Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-12-16T15:42:35Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-12-16T15:42:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-06-18T15:42:35Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1870is.xml"
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
      "title": "Rim of the Valley Corridor Preservation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rim of the Valley Corridor Preservation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to adjust the boundary of the Santa Monica Mountains National Recreation Area to include the Rim of the Valley Corridor, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T07:48:29Z"
    }
  ]
}
```
