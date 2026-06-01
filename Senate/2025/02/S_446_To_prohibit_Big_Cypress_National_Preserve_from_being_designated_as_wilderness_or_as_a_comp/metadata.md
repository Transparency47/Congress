# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/446?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/446
- Title: A bill to prohibit Big Cypress National Preserve from being designated as wilderness or as a component of the National Wilderness Preservation System, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 446
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably and an amendment to the title.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably and an amendment to the title.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/446",
    "number": "446",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A bill to prohibit Big Cypress National Preserve from being designated as wilderness or as a component of the National Wilderness Preservation System, and for other purposes.",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably and an amendment to the title.",
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
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
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
            "date": "2026-02-04T22:06:03Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-06T17:57:43Z",
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
              "date": "2025-12-09T18:12:41Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s446is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 446\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo prohibit Big Cypress National Preserve from being designated as wilderness or as a component of the National Wilderness Preservation System, and for other purposes.\n#### 1. Prohibition on designation of Big Cypress National Preserve as wilderness\nBig Cypress National Preserve may not be designated as wilderness or as a component of the National Wilderness Preservation System.",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-11",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "1192",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To ensure that Big Cypress National Preserve may not be designated as wilderness or as a component of the National Wilderness Preservation System, and for other purposes.",
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
            "name": "Florida",
            "updateDate": "2025-09-25T20:04:36Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-09-25T20:04:36Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-09-25T20:04:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-06T12:39:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s446",
          "measure-number": "446",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-02-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s446v00",
            "update-date": "2026-02-09"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill prohibits the Big Cypress National Preserve in Florida from being designated as wilderness or as a component of the National Wilderness Preservation System. The National Park Service currently manages Big Cypress National\u00a0Preserve, which is a freshwater swamp ecosystem of 729,000 acres.\u00a0</p><p>In general, development activities, commercial activities, permanent structures, and roads are prohibited in wilderness areas. In contrast, natural preserves typically allow some\u00a0development activities, such as hunting or oil and gas exploration.</p>"
        },
        "title": "A bill to prohibit Big Cypress National Preserve from being designated as wilderness or as a component of the National Wilderness Preservation System, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s446.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill prohibits the Big Cypress National Preserve in Florida from being designated as wilderness or as a component of the National Wilderness Preservation System. The National Park Service currently manages Big Cypress National\u00a0Preserve, which is a freshwater swamp ecosystem of 729,000 acres.\u00a0</p><p>In general, development activities, commercial activities, permanent structures, and roads are prohibited in wilderness areas. In contrast, natural preserves typically allow some\u00a0development activities, such as hunting or oil and gas exploration.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s446"
    },
    "title": "A bill to prohibit Big Cypress National Preserve from being designated as wilderness or as a component of the National Wilderness Preservation System, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill prohibits the Big Cypress National Preserve in Florida from being designated as wilderness or as a component of the National Wilderness Preservation System. The National Park Service currently manages Big Cypress National\u00a0Preserve, which is a freshwater swamp ecosystem of 729,000 acres.\u00a0</p><p>In general, development activities, commercial activities, permanent structures, and roads are prohibited in wilderness areas. In contrast, natural preserves typically allow some\u00a0development activities, such as hunting or oil and gas exploration.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s446"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s446is.xml"
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
      "title": "A bill to prohibit Big Cypress National Preserve from being designated as wilderness or as a component of the National Wilderness Preservation System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:41Z"
    },
    {
      "title": "A bill to prohibit Big Cypress National Preserve from being designated as wilderness or as a component of the National Wilderness Preservation System, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-07T11:56:33Z"
    }
  ]
}
```
