# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2268?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2268
- Title: Veterans Homecare Choice Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2268
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2025-12-12T09:07:43Z
- Update date including text: 2025-12-12T09:07:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-26 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-26 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2268",
    "number": "2268",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Veterans Homecare Choice Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:43Z",
    "updateDateIncludingText": "2025-12-12T09:07:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-03-21T20:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-26T16:40:49Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "CO"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2268ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2268\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Mast (for himself and Mr. Neguse ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to recognize nurse registries for purposes of the Veterans Community Care Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Homecare Choice Act of 2025 .\n#### 2. Recognition of nurse registries for purposes of Veterans Community Care Program\nSection 1703 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nby redesignating paragraph (5) as paragraph (6); and\n**(B)**\nby inserting after paragraph (4) the following new paragraph:\n(5) Any nurse registry, including any registered nurse, licensed practical nurse, certified nursing assistant, home health aide, companion, or homemaker furnishing services through a nurse registry. ; and\n**(2)**\nin subsection (q), by adding at the end the following new paragraph:\n(3) The term nurse registry means a person that\u2014 (A) procures, or attempts to procure, contracts or other agreements on behalf of registered nurses, licensed practical nurses, certified nursing assistants, home health aides, companions, or homemakers, under which such individuals may provide health care-related or assistive services (including such services provided directly to patients or in support of health care facilities) and receive compensation for such services; and (B) satisfies any applicable State licensure requirement. .",
      "versionDate": "2025-03-21",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-30",
        "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably."
      },
      "number": "635",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veterans Homecare Choice Act of 2025",
      "type": "S"
    },
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
            "updateDate": "2025-06-02T20:17:38Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-06-02T20:17:38Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2025-06-02T20:17:38Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-02T20:17:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T13:58:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-21",
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
          "measure-id": "id119hr2268",
          "measure-number": "2268",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-21",
          "originChamber": "HOUSE",
          "update-date": "2025-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2268v00",
            "update-date": "2025-05-21"
          },
          "action-date": "2025-03-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Homecare Choice Act of 2025</strong></p><p>This bill includes any nurse registry as an eligible health care provider under the Veterans Community Care Program of the Department of Veterans Affairs. Under the bill, a nurse registry is a person who satisfies applicable state licensure requirements and procures, or attempts to procure, contracts or agreements on behalf of registered nurses, licensed practical nurses, certified nursing assistants, home health aides, companions, or homemakers under which such individuals may furnish health care-related or assistive services and receive compensation.</p>"
        },
        "title": "Veterans Homecare Choice Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2268.xml",
    "summary": {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Homecare Choice Act of 2025</strong></p><p>This bill includes any nurse registry as an eligible health care provider under the Veterans Community Care Program of the Department of Veterans Affairs. Under the bill, a nurse registry is a person who satisfies applicable state licensure requirements and procures, or attempts to procure, contracts or agreements on behalf of registered nurses, licensed practical nurses, certified nursing assistants, home health aides, companions, or homemakers under which such individuals may furnish health care-related or assistive services and receive compensation.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119hr2268"
    },
    "title": "Veterans Homecare Choice Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Homecare Choice Act of 2025</strong></p><p>This bill includes any nurse registry as an eligible health care provider under the Veterans Community Care Program of the Department of Veterans Affairs. Under the bill, a nurse registry is a person who satisfies applicable state licensure requirements and procures, or attempts to procure, contracts or agreements on behalf of registered nurses, licensed practical nurses, certified nursing assistants, home health aides, companions, or homemakers under which such individuals may furnish health care-related or assistive services and receive compensation.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119hr2268"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2268ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "updateDate": "2025-04-04T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Homecare Choice Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T07:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to recognize nurse registries for purposes of the Veterans Community Care Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T07:18:29Z"
    }
  ]
}
```
