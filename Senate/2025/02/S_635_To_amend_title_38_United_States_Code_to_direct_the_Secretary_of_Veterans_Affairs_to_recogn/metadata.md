# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/635?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/635
- Title: Veterans Homecare Choice Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 635
- Origin chamber: Senate
- Introduced date: 2025-02-19
- Update date: 2026-03-19T11:03:25Z
- Update date including text: 2026-03-19T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-19: Introduced in Senate
- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-02-19: Introduced in Senate

## Actions

- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-19",
    "latestAction": {
      "actionDate": "2025-02-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/635",
    "number": "635",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Veterans Homecare Choice Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T11:03:25Z",
    "updateDateIncludingText": "2026-03-19T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-19",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-19",
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
            "date": "2025-07-30T20:00:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-21T20:00:12Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:12Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-19T20:35:48Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s635is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 635\nIN THE SENATE OF THE UNITED STATES\nFebruary 19, 2025 Mr. Tuberville (for himself and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to recognize nurse registries for purposes of the Veterans Community Care Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Homecare Choice Act of 2025 .\n#### 2. Recognition of nurse registries for purposes of Veterans Community Care Program\nSection 1703 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nby redesignating paragraph (5) as paragraph (6); and\n**(B)**\nby inserting after paragraph (4) the following new paragraph:\n(5) Any nurse registry, including any registered nurse, licensed practical nurse, certified nursing assistant, home health aide, companion, or homemaker furnishing services through a nurse registry. ; and\n**(2)**\nin subsection (q), by adding at the end the following new paragraph:\n(3) The term nurse registry means a person that\u2014 (A) procures, or attempts to procure, contracts or other agreements on behalf of registered nurses, licensed practical nurses, certified nursing assistants, home health aides, companions, or homemakers, under which such individuals may provide health care-related or assistive services (including such services provided directly to patients or in support of health care facilities) and receive compensation for such services; and (B) satisfies any applicable State licensure requirement. .",
      "versionDate": "2025-02-19",
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
        "actionDate": "2025-03-27",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "1937",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veterans Homecare Choice Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-26",
        "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs."
      },
      "number": "2268",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veterans Homecare Choice Act of 2025",
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
            "name": "Health personnel",
            "updateDate": "2025-06-02T20:17:07Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-06-02T20:17:07Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2025-06-02T20:17:07Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-02T20:17:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T17:28:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-19",
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
          "measure-id": "id119s635",
          "measure-number": "635",
          "measure-type": "s",
          "orig-publish-date": "2025-02-19",
          "originChamber": "SENATE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s635v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-02-19",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veterans Homecare Choice Act of 2025</strong></p><p>This bill includes any nurse registry as an eligible health care provider under the Veterans Community Care Program of the Department of Veterans Affairs. Under the bill, a nurse registry is a person who satisfies applicable state licensure requirements and procures, or attempts to procure, contracts or agreements on behalf of registered nurses, licensed practical nurses, certified nursing assistants, home health aides, companions, or homemakers under which such individuals may furnish health care-related or assistive services and receive compensation.</p>"
        },
        "title": "Veterans Homecare Choice Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s635.xml",
    "summary": {
      "actionDate": "2025-02-19",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Homecare Choice Act of 2025</strong></p><p>This bill includes any nurse registry as an eligible health care provider under the Veterans Community Care Program of the Department of Veterans Affairs. Under the bill, a nurse registry is a person who satisfies applicable state licensure requirements and procures, or attempts to procure, contracts or agreements on behalf of registered nurses, licensed practical nurses, certified nursing assistants, home health aides, companions, or homemakers under which such individuals may furnish health care-related or assistive services and receive compensation.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119s635"
    },
    "title": "Veterans Homecare Choice Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-19",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Homecare Choice Act of 2025</strong></p><p>This bill includes any nurse registry as an eligible health care provider under the Veterans Community Care Program of the Department of Veterans Affairs. Under the bill, a nurse registry is a person who satisfies applicable state licensure requirements and procures, or attempts to procure, contracts or agreements on behalf of registered nurses, licensed practical nurses, certified nursing assistants, home health aides, companions, or homemakers under which such individuals may furnish health care-related or assistive services and receive compensation.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119s635"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s635is.xml"
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
      "title": "Veterans Homecare Choice Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Homecare Choice Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to direct the Secretary of Veterans Affairs to recognize nurse registries for purposes of the Veterans Community Care Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:33:31Z"
    }
  ]
}
```
