# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1135?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1135
- Title: A bill to amend the National Trails System Act to direct the Secretary of the Interior to conduct a study on the feasibility of designating the Bonneville Shoreline Trail.
- Congress: 119
- Bill type: S
- Bill number: 1135
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2026-04-13T19:20:28Z
- Update date including text: 2026-04-13T19:20:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1135",
    "number": "1135",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A bill to amend the National Trails System Act to direct the Secretary of the Interior to conduct a study on the feasibility of designating the Bonneville Shoreline Trail.",
    "type": "S",
    "updateDate": "2026-04-13T19:20:28Z",
    "updateDateIncludingText": "2026-04-13T19:20:28Z"
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
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
            "date": "2026-03-04T16:02:20Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-26T15:15:05Z",
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
              "date": "2025-12-09T18:12:57Z",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1135is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1135\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Curtis (for himself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the National Trails System Act to direct the Secretary of the Interior to conduct a study on the feasibility of designating the Bonneville Shoreline Trail.\n#### 1. Bonneville Shoreline Trail feasibility study\nSection 5(c) of the National Trails System Act ( 16 U.S.C. 1244(c) ) is amended by adding at the end the following:\n(50) Bonneville Shoreline Trail The Bonneville Shoreline Trail, a system of trails and potential trails extending approximately 280 miles from the Idaho-Utah border to Nephi, Utah, following the Bonneville bench that was created by the historic Lake Bonneville. .",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-05-15",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "3451",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To amend the National Trails System Act to direct the Secretary of the Interior to conduct a study on the feasibility of designating the Bonneville Shoreline Trail.",
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
            "name": "Government studies and investigations",
            "updateDate": "2026-01-07T16:53:47Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-01-07T16:53:37Z"
          },
          {
            "name": "Utah",
            "updateDate": "2026-01-07T16:53:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-21T18:41:50Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1135is.xml"
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
      "title": "A bill to amend the National Trails System Act to direct the Secretary of the Interior to conduct a study on the feasibility of designating the Bonneville Shoreline Trail.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:26Z"
    },
    {
      "title": "A bill to amend the National Trails System Act to direct the Secretary of the Interior to conduct a study on the feasibility of designating the Bonneville Shoreline Trail.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T10:56:28Z"
    }
  ]
}
```
