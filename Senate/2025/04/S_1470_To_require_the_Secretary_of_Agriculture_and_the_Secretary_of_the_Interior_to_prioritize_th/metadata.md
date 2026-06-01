# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1470?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1470
- Title: Continental Divide National Scenic Trail Completion Act
- Congress: 119
- Bill type: S
- Bill number: 1470
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1470",
    "number": "1470",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Continental Divide National Scenic Trail Completion Act",
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
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
            "date": "2025-12-17T14:30:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-17T14:30:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-10T19:57:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MT"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "MT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1470is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1470\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Heinrich (for himself and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of Agriculture and the Secretary of the Interior to prioritize the completion of the Continental Divide National Scenic Trail, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Continental Divide National Scenic Trail Completion Act .\n#### 2. Definitions\nIn this Act:\n**(1) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(2) Trail**\nThe term Trail means the Continental Divide National Scenic Trail.\n**(3) Trail Completion Team**\nThe term Trail Completion Team means the joint Forest Service-Bureau of Land Management Trail completion team established under section 4(a).\n#### 3. Completion of Continental Divide National Scenic Trail\nSubject to the availability of appropriations, the Secretary and the Secretary of the Interior shall seek to complete the Trail as a continuous route not later than 10 years after the date of enactment of this Act.\n#### 4. Trail Completion Team\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary and the Secretary of the Interior shall establish a joint Forest Service-Bureau of Land Management Trail completion team to work in coordination with the administrator of the Trail\u2014\n**(1)**\nto facilitate the completion and optimization of the Trail, consistent with the purposes of the Trail; and\n**(2)**\nto assist in the development of the comprehensive development plan for the Trail under section 5.\n##### (b) Consultation\nAs appropriate, the Trail Completion Team shall consult with other Federal agencies, affected State, Tribal, and local governments, landowners, affected land-grant mercedes owners and users, acequias, and other interested parties in\u2014\n**(1)**\nthe completion and optimization of the Trail; and\n**(2)**\nthe development and completion of the comprehensive development plan for the Trail under section 5.\n#### 5. Comprehensive development plan for the Continental Divide National Scenic Trail\n##### (a) In general\nNot later than 3 years after the date of establishment of the Trail Completion Team under section 4(a), the Secretary shall complete a comprehensive development plan for the Trail.\n##### (b) Plan inclusions\nThe comprehensive development plan under subsection (a) shall\u2014\n**(1)**\nidentify any gaps in the Trail for which the Secretary and the Secretary of the Interior have not been able to acquire land;\n**(2)**\nidentify opportunities for the use of easements acquired from willing sellers to facilitate completion of the Trail; and\n**(3)**\ninclude general and site-specific Trail development plans, including anticipated costs of the plans.\n#### 6. Partnerships\nThe Secretary and the Secretary of the Interior shall seek to enter into agreements with volunteer and nonprofit organizations, as appropriate, to facilitate the completion and administration of the Trail.\n#### 7. Effect\nNothing in this Act\u2014\n**(1)**\nprovides any authority to acquire land or interests in land for inclusion in the Trail beyond the authorities provided for the Trail in the National Trails System Act ( 16 U.S.C. 1241 et seq. ), including acquisition by eminent domain; or\n**(2)**\nmakes the acquisition of land or interests in land for the Trail a priority over other land acquisition authorizations.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-10",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2877",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Continental Divide National Scenic Trail Completion Act",
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
            "name": "Colorado",
            "updateDate": "2026-01-07T19:42:01Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-07T19:42:01Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2026-01-07T19:42:01Z"
          },
          {
            "name": "Idaho",
            "updateDate": "2026-01-07T19:42:01Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-01-07T19:42:02Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-01-07T19:42:01Z"
          },
          {
            "name": "Montana",
            "updateDate": "2026-01-07T19:42:01Z"
          },
          {
            "name": "New Mexico",
            "updateDate": "2026-01-07T19:42:01Z"
          },
          {
            "name": "Outdoor recreation",
            "updateDate": "2026-01-07T19:42:01Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-01-07T19:42:01Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2026-01-07T19:42:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-22T15:15:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119s1470",
          "measure-number": "1470",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2026-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1470v00",
            "update-date": "2026-02-10"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Continental Divide National Scenic Trail Completion Act</strong></p><p>This bill directs the Department of Agriculture (USDA) and the Department of the Interior to seek to complete the Continental Divide National Scenic Trail no later than 10 years after the enactment of this bill.</p><p>USDA and Interior must\u00a0establish a joint Forest Service and Bureau of Land Management trail completion team to work in coordination with the administrator of the trail to facilitate its completion and optimization.</p><p>USDA must complete a comprehensive development plan for the trail within three years.</p><p>USDA and Interior must also seek to enter into agreements with volunteer and nonprofit organizations to facilitate the completion and administration of the trail.</p>"
        },
        "title": "Continental Divide National Scenic Trail Completion Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1470.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Continental Divide National Scenic Trail Completion Act</strong></p><p>This bill directs the Department of Agriculture (USDA) and the Department of the Interior to seek to complete the Continental Divide National Scenic Trail no later than 10 years after the enactment of this bill.</p><p>USDA and Interior must\u00a0establish a joint Forest Service and Bureau of Land Management trail completion team to work in coordination with the administrator of the trail to facilitate its completion and optimization.</p><p>USDA must complete a comprehensive development plan for the trail within three years.</p><p>USDA and Interior must also seek to enter into agreements with volunteer and nonprofit organizations to facilitate the completion and administration of the trail.</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s1470"
    },
    "title": "Continental Divide National Scenic Trail Completion Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Continental Divide National Scenic Trail Completion Act</strong></p><p>This bill directs the Department of Agriculture (USDA) and the Department of the Interior to seek to complete the Continental Divide National Scenic Trail no later than 10 years after the enactment of this bill.</p><p>USDA and Interior must\u00a0establish a joint Forest Service and Bureau of Land Management trail completion team to work in coordination with the administrator of the trail to facilitate its completion and optimization.</p><p>USDA must complete a comprehensive development plan for the trail within three years.</p><p>USDA and Interior must also seek to enter into agreements with volunteer and nonprofit organizations to facilitate the completion and administration of the trail.</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s1470"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1470is.xml"
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
      "title": "Continental Divide National Scenic Trail Completion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Continental Divide National Scenic Trail Completion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Agriculture and the Secretary of the Interior to prioritize the completion of the Continental Divide National Scenic Trail, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:20Z"
    }
  ]
}
```
