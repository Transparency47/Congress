# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/437?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/437
- Title: Commemorating the 80th Anniversary of the Georgia Ports Authority.
- Congress: 119
- Bill type: HRES
- Bill number: 437
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2026-04-03T10:55:27Z
- Update date including text: 2026-04-03T10:55:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-21 - IntroReferral: Submitted in House
- 2025-05-21 - IntroReferral: Submitted in House
- 2025-05-22 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-05-21: Submitted in House

## Actions

- 2025-05-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-21 - IntroReferral: Submitted in House
- 2025-05-21 - IntroReferral: Submitted in House
- 2025-05-22 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/437",
    "number": "437",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Commemorating the 80th Anniversary of the Georgia Ports Authority.",
    "type": "HRES",
    "updateDate": "2026-04-03T10:55:27Z",
    "updateDateIncludingText": "2026-04-03T10:55:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-05-21T14:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-22T21:03:05Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres437ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 437\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mr. Carter of Georgia submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nCommemorating the 80th Anniversary of the Georgia Ports Authority.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the Georgia Ports Authority for 80 years of strengthening Georgia\u2019s economy and connecting the State to global commerce; and\n**(2)**\ncommemorates the 80th anniversary of the Georgia Ports Authority.",
      "versionDate": "2025-05-21",
      "versionType": "IH"
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-28T12:33:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-21",
    "originChamber": "House",
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
          "measure-id": "id119hres437",
          "measure-number": "437",
          "measure-type": "hres",
          "orig-publish-date": "2025-05-21",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres437v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-05-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution commemorates the 80<sup>th</sup> anniversary of the Georgia Ports Authority.</p>"
        },
        "title": "Commemorating the 80th Anniversary of the Georgia Ports Authority."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres437.xml",
    "summary": {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution commemorates the 80<sup>th</sup> anniversary of the Georgia Ports Authority.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres437"
    },
    "title": "Commemorating the 80th Anniversary of the Georgia Ports Authority."
  },
  "summaries": [
    {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution commemorates the 80<sup>th</sup> anniversary of the Georgia Ports Authority.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres437"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres437ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Commemorating the 80th Anniversary of the Georgia Ports Authority.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-23T02:48:19Z"
    },
    {
      "title": "Commemorating the 80th Anniversary of the Georgia Ports Authority.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-22T12:22:21Z"
    }
  ]
}
```
