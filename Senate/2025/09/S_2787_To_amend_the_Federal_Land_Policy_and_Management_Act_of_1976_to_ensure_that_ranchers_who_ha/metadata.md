# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2787?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2787
- Title: Grasslands Grazing Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2787
- Origin chamber: Senate
- Introduced date: 2025-09-11
- Update date: 2026-04-06T16:42:11Z
- Update date including text: 2026-04-06T16:42:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in Senate
- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S6578)
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.
- Latest action: 2025-09-11: Introduced in Senate

## Actions

- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S6578)
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2787",
    "number": "2787",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Grasslands Grazing Act of 2025",
    "type": "S",
    "updateDate": "2026-04-06T16:42:11Z",
    "updateDateIncludingText": "2026-04-06T16:42:11Z"
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
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.",
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
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S6578)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-11",
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
            "date": "2026-03-04T16:02:52Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-11T18:33:14Z",
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
              "date": "2026-02-12T15:00:28Z",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "WY"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2787is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2787\nIN THE SENATE OF THE UNITED STATES\nSeptember 11, 2025 Mr. Barrasso (for himself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Federal Land Policy and Management Act of 1976 to ensure that ranchers who have grazing agreements on national grasslands are treated the same as permittees on other Federal land.\n#### 1. Short title\nThis Act may be cited as the Grasslands Grazing Act of 2025 .\n#### 2. Eligibility of national grasslands for grazing leases and permits\n##### (a) In general\nSection 402(a) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1752(a) ) is amended by striking lands within National Forests and inserting National Forest System (as defined in section 11(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1609(a) )) land .\n##### (b) Effect\nNothing in the amendment made by subsection (a) modifies or affects\u2014\n**(1)**\nthe applicability to national grasslands of any provision of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ) other than section 402 of that Act ( 43 U.S.C. 1752 );\n**(2)**\ntitle III of the Bankhead-Jones Farm Tenant Act ( 7 U.S.C. 1010 et seq. ); or\n**(3)**\nsection 11 of the Public Rangelands Improvement Act of 1978 ( 43 U.S.C. 1907 ).",
      "versionDate": "2025-09-11",
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
        "actionDate": "2026-02-11",
        "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 25 - 14."
      },
      "number": "6300",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Grasslands Grazing Act of 2025",
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
            "name": "Forests, forestry, trees",
            "updateDate": "2026-01-20T17:28:05Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-01-20T17:28:05Z"
          },
          {
            "name": "Livestock",
            "updateDate": "2026-01-20T17:28:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-29T18:51:43Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2787is.xml"
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
      "title": "Grasslands Grazing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Grasslands Grazing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Land Policy and Management Act of 1976 to ensure that ranchers who have grazing agreements on national grasslands are treated the same as permittees on other Federal land.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:33:18Z"
    }
  ]
}
```
