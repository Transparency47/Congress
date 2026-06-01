# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1280?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1280
- Title: Down East Remembrance Act
- Congress: 119
- Bill type: S
- Bill number: 1280
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1280",
    "number": "1280",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Down East Remembrance Act",
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
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T17:25:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T18:12:59Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1280is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1280\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mr. Tillis (for himself and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo designate six creeks in North Carolina in honor of the lives lost in a plane crash in Carteret County, North Carolina, on February 13, 2022, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Down East Remembrance Act .\n#### 2. Designation of creeks\n##### (a) Noah Styron Creek\nThe creek located at latitude 34\u00b059\u203249.33\u2032\u2032 N, longitude 76\u00b08\u203242.11\u2032\u2032 W, shall be known and designated as Noah Styron Creek .\n##### (b) Hunter Parks Creek\nThe creek located at latitude 34\u00b057\u203252.85\u2032\u2032 N, longitude 76\u00b011\u203211.25\u2032\u2032 W, shall be known and designated as Hunter Parks Creek .\n##### (c) Kole McInnis Creek\nThe creek located at latitude 34\u00b057\u203246.30\u2032\u2032 N, longitude 76\u00b011\u203218.18\u2032\u2032 W, shall be known and designated as Kole McInnis Creek .\n##### (d) Stephanie Fulcher Creek\nThe creek located at latitude 34\u00b057\u203238.08\u2032\u2032 N, longitude 76\u00b011\u203231.18\u2032\u2032 W, shall be known and designated as Stephanie Fulcher Creek .\n##### (e) Jacob Taylor Creek\nThe creek located at latitude 34\u00b052\u203243.45\u2032\u2032 N, longitude 76\u00b017\u203241.49\u2032\u2032 W, shall be known and designated as Jacob Taylor Creek .\n##### (f) Daily Shepherd Creek\nThe creek located at latitude 34\u00b052\u203228.26\u2032\u2032 N, longitude 76\u00b017\u203243.20\u2032\u2032 W, shall be known and designated as Daily Shepherd Creek .\n##### (g) References\nAny reference in any law, regulation, document, record, map, or other paper of the United States to a creek described in this section shall be considered a reference to that creek as it is designated under this section.",
      "versionDate": "2025-04-03",
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
        "actionDate": "2025-03-18",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2217",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Down East Remembrance Act",
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
            "name": "Accidents",
            "updateDate": "2025-12-12T20:25:47Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2025-12-12T20:25:47Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2025-12-12T20:25:47Z"
          },
          {
            "name": "North Carolina",
            "updateDate": "2025-12-12T20:25:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-14T12:59:44Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1280is.xml"
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
      "title": "Down East Remembrance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Down East Remembrance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to designate six creeks in North Carolina in honor of the lives lost in a plane crash in Carteret County, North Carolina, on February 13, 2022, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:23Z"
    }
  ]
}
```
