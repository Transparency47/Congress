# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1353?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1353
- Title: A bill to extend the authority for modifications to the Second Division Memorial in the District of Columbia.
- Congress: 119
- Bill type: S
- Bill number: 1353
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1353",
    "number": "1353",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "A bill to extend the authority for modifications to the Second Division Memorial in the District of Columbia.",
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
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.",
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
        "item": [
          {
            "date": "2026-02-04T22:05:39Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-08T21:57:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-09T18:13:01Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-12-09T18:13:01Z",
                "name": "Hearings By (subcommittee)"
              }
            ]
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
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1353is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1353\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Ms. Murkowski introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo extend the authority for modifications to the Second Division Memorial in the District of Columbia.\n#### 1. Extension of authority for modifications to Second Division Memorial\nNotwithstanding section 8903(e) of title 40, United States Code, the authority provided by section 352 of the National Defense Authorization Act for Fiscal Year 2018 ( Public Law 115\u201391 ; 131 Stat. 1367) shall continue to apply through September 30, 2032.",
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
            "name": "District of Columbia",
            "updateDate": "2025-12-12T21:04:16Z"
          },
          {
            "name": "Military history",
            "updateDate": "2025-12-12T21:04:23Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2025-12-12T21:04:08Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-12-12T21:04:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-27T15:41:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-08",
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
          "measure-id": "id119s1353",
          "measure-number": "1353",
          "measure-type": "s",
          "orig-publish-date": "2025-04-08",
          "originChamber": "SENATE",
          "update-date": "2026-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1353v00",
            "update-date": "2026-02-10"
          },
          "action-date": "2025-04-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill extends through September 30, 2032, the authority to modify the Second Division Memorial located in President\u2019s Park in the District of Columbia. Specifically, it extends the authority of the Second Indianhead Division Association, Inc., Scholarship and Memorials Foundation to place additional commemorative elements or engravings on the raised platform or stone work to honor the members of the Second Infantry Division who have given their lives in service to the United States.\u00a0</p>"
        },
        "title": "A bill to extend the authority for modifications to the Second Division Memorial in the District of Columbia."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1353.xml",
    "summary": {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill extends through September 30, 2032, the authority to modify the Second Division Memorial located in President\u2019s Park in the District of Columbia. Specifically, it extends the authority of the Second Indianhead Division Association, Inc., Scholarship and Memorials Foundation to place additional commemorative elements or engravings on the raised platform or stone work to honor the members of the Second Infantry Division who have given their lives in service to the United States.\u00a0</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s1353"
    },
    "title": "A bill to extend the authority for modifications to the Second Division Memorial in the District of Columbia."
  },
  "summaries": [
    {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill extends through September 30, 2032, the authority to modify the Second Division Memorial located in President\u2019s Park in the District of Columbia. Specifically, it extends the authority of the Second Indianhead Division Association, Inc., Scholarship and Memorials Foundation to place additional commemorative elements or engravings on the raised platform or stone work to honor the members of the Second Infantry Division who have given their lives in service to the United States.\u00a0</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s1353"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1353is.xml"
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
      "title": "A bill to extend the authority for modifications to the Second Division Memorial in the District of Columbia.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:17Z"
    },
    {
      "title": "A bill to extend the authority for modifications to the Second Division Memorial in the District of Columbia.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T10:56:14Z"
    }
  ]
}
```
