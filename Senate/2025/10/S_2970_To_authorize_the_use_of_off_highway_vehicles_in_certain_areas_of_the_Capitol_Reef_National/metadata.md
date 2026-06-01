# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2970?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2970
- Title: A bill to authorize the use of off-highway vehicles in certain areas of the Capitol Reef National Park, Utah.
- Congress: 119
- Bill type: S
- Bill number: 2970
- Origin chamber: Senate
- Introduced date: 2025-10-03
- Update date: 2026-04-08T20:10:36Z
- Update date including text: 2026-04-08T20:10:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-03: Introduced in Senate
- 2025-10-03 - IntroReferral: Introduced in Senate
- 2025-10-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- Latest action: 2025-10-03: Introduced in Senate

## Actions

- 2025-10-03 - IntroReferral: Introduced in Senate
- 2025-10-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2970",
    "number": "2970",
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
    "title": "A bill to authorize the use of off-highway vehicles in certain areas of the Capitol Reef National Park, Utah.",
    "type": "S",
    "updateDate": "2026-04-08T20:10:36Z",
    "updateDateIncludingText": "2026-04-08T20:10:36Z"
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
      "actionDate": "2025-10-03",
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
      "actionDate": "2025-10-03",
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
          "date": "2025-10-03T16:16:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T18:13:25Z",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2970is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2970\nIN THE SENATE OF THE UNITED STATES\nOctober 3, 2025 Mr. Lee (for himself and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo authorize the use of off-highway vehicles in certain areas of the Capitol Reef National Park, Utah.\n#### 1. Use of off-highway vehicles in certain areas of the Capitol Reef National Park, Utah\n##### (a) Definitions\nIn this section:\n**(1) Covered road**\nThe term covered road means the portions of each of Burr Trail Road, Cathedral Road, Hartnet Road, Highway 24, Notom Bullfrog Road, Polk Creek Road, Oil Well Bench Road, Baker Ranch Road, South Desert Overlook Road, Temple of the Sun and Moon Road, Gypsum Sinkhole Road, and Sulphur Creek Road that are located within the boundaries of the Capitol Reef National Park in the State.\n**(2) Off-highway vehicle**\nThe term off-highway vehicle has the meaning given the term in State law.\n**(3) State**\nThe term State means the State of Utah.\n##### (b) Applicable law\nState law shall apply to the use of motor vehicles (including off-highway vehicles) on a covered road.",
      "versionDate": "2025-10-03",
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
            "name": "Motor vehicles",
            "updateDate": "2026-01-09T16:57:38Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-01-09T16:57:38Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2026-01-09T16:57:38Z"
          },
          {
            "name": "Utah",
            "updateDate": "2026-01-09T16:57:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-02T17:44:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-03",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s2970",
          "measure-number": "2970",
          "measure-type": "s",
          "orig-publish-date": "2025-10-03",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2970v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-10-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill makes the state law of Utah applicable to the use of motor vehicles (including off-highway vehicles) on the portions of each of Burr Trail Road, Cathedral Road, Hartnet Road, Highway 24, Notom Bullfrog Road, Polk Creek Road,\u00a0Oil Well Bench Road, Baker Ranch Road, South Desert Overlook Road, Temple of the Sun and Moon Road, Gypsum Sinkhole Road, and Sulphur Creek Road\u00a0that are located within the boundaries of the Capitol Reef National Park in Utah.</p>"
        },
        "title": "A bill to authorize the use of off-highway vehicles in certain areas of the Capitol Reef National Park, Utah."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2970.xml",
    "summary": {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill makes the state law of Utah applicable to the use of motor vehicles (including off-highway vehicles) on the portions of each of Burr Trail Road, Cathedral Road, Hartnet Road, Highway 24, Notom Bullfrog Road, Polk Creek Road,\u00a0Oil Well Bench Road, Baker Ranch Road, South Desert Overlook Road, Temple of the Sun and Moon Road, Gypsum Sinkhole Road, and Sulphur Creek Road\u00a0that are located within the boundaries of the Capitol Reef National Park in Utah.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s2970"
    },
    "title": "A bill to authorize the use of off-highway vehicles in certain areas of the Capitol Reef National Park, Utah."
  },
  "summaries": [
    {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill makes the state law of Utah applicable to the use of motor vehicles (including off-highway vehicles) on the portions of each of Burr Trail Road, Cathedral Road, Hartnet Road, Highway 24, Notom Bullfrog Road, Polk Creek Road,\u00a0Oil Well Bench Road, Baker Ranch Road, South Desert Overlook Road, Temple of the Sun and Moon Road, Gypsum Sinkhole Road, and Sulphur Creek Road\u00a0that are located within the boundaries of the Capitol Reef National Park in Utah.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s2970"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2970is.xml"
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
      "title": "A bill to authorize the use of off-highway vehicles in certain areas of the Capitol Reef National Park, Utah.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:03:17Z"
    },
    {
      "title": "A bill to authorize the use of off-highway vehicles in certain areas of the Capitol Reef National Park, Utah.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:56:16Z"
    }
  ]
}
```
