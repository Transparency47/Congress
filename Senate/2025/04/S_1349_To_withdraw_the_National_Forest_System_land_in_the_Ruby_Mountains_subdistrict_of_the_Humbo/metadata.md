# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1349?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1349
- Title: Ruby Mountains Protection Act
- Congress: 119
- Bill type: S
- Bill number: 1349
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1349",
    "number": "1349",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Ruby Mountains Protection Act",
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
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T21:30:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T15:00:14Z",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1349is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1349\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Ms. Cortez Masto (for herself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo withdraw the National Forest System land in the Ruby Mountains subdistrict of the Humboldt-Toiyabe National Forest and the National Wildlife Refuge System land in Ruby Lake National Wildlife Refuge, Elko and White Pine Counties, Nevada, from operation under the mineral leasing laws.\n#### 1. Short title\nThis Act may be cited as the Ruby Mountains Protection Act .\n#### 2. Withdrawal of certain National Forest System land\n##### (a) Withdrawal\nSubject to valid existing rights, the approximately 309,272 acres of Federal land and interests in the land located in the Ruby Mountains subdistrict of the Humboldt-Toiyabe National Forest within the area depicted on the Forest Service map entitled S. 258 Ruby Mountains Protective Act and dated December 5, 2019, as National Forest System Lands are withdrawn from all forms of operation under the mineral leasing laws.\n##### (b) Application\nAny land or interest in land within the boundary of the Ruby Mountains subdistrict of the Humboldt-Toiyabe National Forest that is acquired by the United States after the date of enactment of this Act shall be withdrawn in accordance with subsection (a).\n##### (c) Availability of map\nThe map described in subsection (a) shall be on file and available for public inspection in the appropriate offices of the Forest Service.\n#### 3. Withdrawal of certain National Wildlife Refuge System land\n##### (a) Withdrawal\n**(1) In general**\nSubject to valid existing rights, the approximately 39,926.10 acres of Federal land and interests in the land located in the Ruby Lake National Wildlife Refuge and depicted on the United States Fish and Wildlife Service map entitled S. XXX Ruby Mountains Protection Act and dated February 23, 2021, as Ruby Lake National Wildlife Refuge are withdrawn from all forms of operation under the mineral leasing laws, subject to paragraph (2).\n**(2) Exception**\nThe withdrawal under paragraph (1) shall not apply to noncommercial refuge management activities by the United States Fish and Wildlife Service.\n##### (b) Application\nAny land or interest in land within the boundary of the Ruby Lake National Wildlife Refuge that is acquired by the United States after the date of enactment of this Act shall be withdrawn in accordance with subsection (a).\n##### (c) Availability of map\nThe map described in subsection (a)(1) shall be on file and available for public inspection in the appropriate offices of the United States Fish and Wildlife Service.",
      "versionDate": "2025-04-08",
      "versionType": "Introduced in Senate"
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
            "updateDate": "2026-02-13T17:01:26Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-02-13T17:01:26Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-02-13T17:01:26Z"
          },
          {
            "name": "Nevada",
            "updateDate": "2026-02-13T17:01:26Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2026-02-13T17:01:26Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2026-02-13T17:01:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-21T21:44:18Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1349is.xml"
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
      "title": "Ruby Mountains Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ruby Mountains Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to withdraw the National Forest System land in the Ruby Mountains subdistrict of the Humboldt-Toiyabe National Forest and the National Wildlife Refuge System land in Ruby Lake National Wildlife Refuge, Elko and White Pine Counties, Nevada, from operation under the mineral leasing laws.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:26Z"
    }
  ]
}
```
