# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/380?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/380
- Title: Affordable Shipping for All Act
- Congress: 119
- Bill type: HR
- Bill number: 380
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2025-05-05T20:46:34Z
- Update date including text: 2025-05-05T20:46:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-14 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-14 - IntroReferral: Sponsor introductory remarks on measure. (CR E28)
- Latest action: 2025-01-14: Introduced in House

## Actions

- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-14 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-14 - IntroReferral: Sponsor introductory remarks on measure. (CR E28)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/380",
    "number": "380",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001055",
        "district": "1",
        "firstName": "Ed",
        "fullName": "Rep. Case, Ed [D-HI-1]",
        "lastName": "Case",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Affordable Shipping for All Act",
    "type": "HR",
    "updateDate": "2025-05-05T20:46:34Z",
    "updateDateIncludingText": "2025-05-05T20:46:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E28)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T15:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-14T15:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "GU"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jos\u00e9",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "PR"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "AS"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "MP"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI]",
      "isOriginalCosponsor": "False",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "VI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr380ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 380\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2025 Mr. Case (for himself, Mr. Moylan , Mr. Hern\u00e1ndez , Mrs. Radewagen , and Mrs. King-Hinds ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require fair shipping prices for noncontiguous areas of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Affordable Shipping for All Act .\n#### 2. Prohibition on higher shipping fees\nNo shipping service may exceed the shipping charge for the same product to and from a location in the contiguous United States as charged to a consumer product or producer good to the noncontiguous area of the United States.\n#### 3. Prohibition on excluding noncontiguous areas\nNo shipping service may exclude\u2014\n**(1)**\na noncontiguous area of the United States from its shipping polices; or\n**(2)**\na noncontiguous area of the United States from shipping to its location.\n#### 4. Exemptions\nAny consumer product or producer good valued at more than $10,000 shall be exempt from the requirements of this Act.\n#### 5. Definitions\nIn this Act:\n**(1) Consumer products**\nThe term consumer products means the finished commodities for end-user use that will go directly to the consumer.\n**(2) Contiguous United States**\nThe term contiguous United States shall refer to the 48 contiguous States and the District of Columbia.\n**(3) Noncontiguous area**\nThe term noncontiguous area means any part of the United States not physically connected to the contiguous United States, including Alaska and Hawaii and any commonwealth, territory, or possession of the United States, including Puerto Rico, Guam, the U.S. Virgin Islands, American Samoa, and the Northern Mariana Islands.\n**(4) Producer goods**\nThe term producer goods means raw materials used to produce other products.\n**(5) Shipping services**\nThe term shipping service \u2014\n**(A)**\nmeans private companies whose primary business model is the transporting of products for retailers; and\n**(B)**\nincludes the United States Postal Service.",
      "versionDate": "2025-01-14",
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
        "name": "Commerce",
        "updateDate": "2025-02-18T14:33:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119hr380",
          "measure-number": "380",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-05-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr380v00",
            "update-date": "2025-05-05"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Affordable Shipping for All Act</strong></p><p>This bill limits shipping services from excluding service or charging higher prices to noncontiguous areas of the United States.</p><p>Specifically, private shipping services (e.g., FedEx) and the U.S. Postal Service are prohibited from charging a higher rate to ship a consumer\u00a0product or producer good (e.g., raw material)\u00a0to a noncontiguous area of the United States than they charge to ship the same product\u00a0to and from a location within the contiguous United States. Under the bill, a noncontiguous area includes Alaska and Hawaii and any commonwealth, territory, or possession of the United States (including Puerto Rico, Guam, the U.S. Virgin Islands, American Samoa, and the Northern Mariana Islands).</p><p>Additionally, such shipping services may not exclude services to such a noncontiguous location.</p><p>Consumer products or producer goods valued at more than $10,000 are exempt from the requirements of this bill.</p>"
        },
        "title": "Affordable Shipping for All Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr380.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Affordable Shipping for All Act</strong></p><p>This bill limits shipping services from excluding service or charging higher prices to noncontiguous areas of the United States.</p><p>Specifically, private shipping services (e.g., FedEx) and the U.S. Postal Service are prohibited from charging a higher rate to ship a consumer\u00a0product or producer good (e.g., raw material)\u00a0to a noncontiguous area of the United States than they charge to ship the same product\u00a0to and from a location within the contiguous United States. Under the bill, a noncontiguous area includes Alaska and Hawaii and any commonwealth, territory, or possession of the United States (including Puerto Rico, Guam, the U.S. Virgin Islands, American Samoa, and the Northern Mariana Islands).</p><p>Additionally, such shipping services may not exclude services to such a noncontiguous location.</p><p>Consumer products or producer goods valued at more than $10,000 are exempt from the requirements of this bill.</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119hr380"
    },
    "title": "Affordable Shipping for All Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Affordable Shipping for All Act</strong></p><p>This bill limits shipping services from excluding service or charging higher prices to noncontiguous areas of the United States.</p><p>Specifically, private shipping services (e.g., FedEx) and the U.S. Postal Service are prohibited from charging a higher rate to ship a consumer\u00a0product or producer good (e.g., raw material)\u00a0to a noncontiguous area of the United States than they charge to ship the same product\u00a0to and from a location within the contiguous United States. Under the bill, a noncontiguous area includes Alaska and Hawaii and any commonwealth, territory, or possession of the United States (including Puerto Rico, Guam, the U.S. Virgin Islands, American Samoa, and the Northern Mariana Islands).</p><p>Additionally, such shipping services may not exclude services to such a noncontiguous location.</p><p>Consumer products or producer goods valued at more than $10,000 are exempt from the requirements of this bill.</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119hr380"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr380ih.xml"
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
      "title": "Affordable Shipping for All Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affordable Shipping for All Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require fair shipping prices for noncontiguous areas of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:26Z"
    }
  ]
}
```
