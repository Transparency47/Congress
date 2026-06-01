# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5280?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5280
- Title: Protecting Farmers from Natural Disasters Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5280
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2026-05-16T08:07:57Z
- Update date including text: 2026-05-16T08:07:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2026-01-13 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2026-01-13 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5280",
    "number": "5280",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Protecting Farmers from Natural Disasters Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:57Z",
    "updateDateIncludingText": "2026-05-16T08:07:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2026-01-13T19:55:19Z",
                "name": "Referred to"
              }
            },
            "name": "Conservation, Research, and Biotechnology Subcommittee",
            "systemCode": "hsag14"
          },
          {
            "activities": {
              "item": {
                "date": "2026-01-13T19:55:13Z",
                "name": "Referred to"
              }
            },
            "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
            "systemCode": "hsag16"
          }
        ]
      },
      "systemCode": "hsag00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NC"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5280ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5280\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Nunn of Iowa (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Credit Act of 1978 to enhance the long-term protection of watersheds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Farmers from Natural Disasters Act of 2025 .\n#### 2. Level of restoration\nSection 403 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2203 ) is amended\u2014\n**(1)**\nby redesignating subsection (b) as subsection (c); and\n**(2)**\nby inserting after subsection (a) the following:\n(b) Level of restoration The Secretary may allow restoration above pre-disaster conditions if that restoration is in the best interest of the long-term health and protection of the watershed. .",
      "versionDate": "2025-09-10",
      "versionType": "Introduced in House"
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
        "name": "Agriculture and Food",
        "updateDate": "2025-09-24T15:10:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-10",
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
          "measure-id": "id119hr5280",
          "measure-number": "5280",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-10",
          "originChamber": "HOUSE",
          "update-date": "2025-09-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5280v00",
            "update-date": "2025-09-24"
          },
          "action-date": "2025-09-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Farmers from Natural Disasters Act of 2025</strong></p><p>This bill amends the Emergency Watershed Protection (EWP) Program to allow the Department of Agriculture (USDA) to provide for certain restoration activities.\u00a0The EWP Program offers technical and financial assistance, including the purchase of floodplain easements, to safeguard people and property from floods, drought, fires, windstorms, and other natural disasters that impair a watershed.</p><p>Under the bill, USDA may\u00a0allow restoration above pre-disaster conditions if that restoration is in the best interest of the long-term health and protection of the watershed.</p>"
        },
        "title": "Protecting Farmers from Natural Disasters Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5280.xml",
    "summary": {
      "actionDate": "2025-09-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Farmers from Natural Disasters Act of 2025</strong></p><p>This bill amends the Emergency Watershed Protection (EWP) Program to allow the Department of Agriculture (USDA) to provide for certain restoration activities.\u00a0The EWP Program offers technical and financial assistance, including the purchase of floodplain easements, to safeguard people and property from floods, drought, fires, windstorms, and other natural disasters that impair a watershed.</p><p>Under the bill, USDA may\u00a0allow restoration above pre-disaster conditions if that restoration is in the best interest of the long-term health and protection of the watershed.</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119hr5280"
    },
    "title": "Protecting Farmers from Natural Disasters Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-09-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Farmers from Natural Disasters Act of 2025</strong></p><p>This bill amends the Emergency Watershed Protection (EWP) Program to allow the Department of Agriculture (USDA) to provide for certain restoration activities.\u00a0The EWP Program offers technical and financial assistance, including the purchase of floodplain easements, to safeguard people and property from floods, drought, fires, windstorms, and other natural disasters that impair a watershed.</p><p>Under the bill, USDA may\u00a0allow restoration above pre-disaster conditions if that restoration is in the best interest of the long-term health and protection of the watershed.</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119hr5280"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5280ih.xml"
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
      "title": "Protecting Farmers from Natural Disasters Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Farmers from Natural Disasters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Credit Act of 1978 to enhance the long-term protection of watersheds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:35Z"
    }
  ]
}
```
