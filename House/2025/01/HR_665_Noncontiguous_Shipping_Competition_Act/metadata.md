# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/665?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/665
- Title: Noncontiguous Shipping Competition Act
- Congress: 119
- Bill type: HR
- Bill number: 665
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-08-02T08:05:26Z
- Update date including text: 2025-08-02T08:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-24 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- 2025-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR E90-91)
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-24 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- 2025-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR E90-91)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/665",
    "number": "665",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "Noncontiguous Shipping Competition Act",
    "type": "HR",
    "updateDate": "2025-08-02T08:05:26Z",
    "updateDateIncludingText": "2025-08-02T08:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E90-91)",
      "type": "IntroReferral"
    },
    {
      "actionDate": "2025-01-24",
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
      "actionDate": "2025-01-23",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-24T15:40:22Z",
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
      "sponsorshipDate": "2025-01-23",
      "state": "GU"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr665ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 665\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Case (for himself and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 46, United States Code, to exempt certain noncontiguous trade from the coastwise laws.\n#### 1. Short title\nThis Act may be cited as the Noncontiguous Shipping Competition Act .\n#### 2. Shipping: Exemption of certain noncontiguous trade from the coastwise laws\nSection 55101(b) of title 46, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by striking or after the semicolon;\n**(2)**\nin paragraph (3), by striking the period and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(4) carriage on a route in noncontiguous trade (as that term is defined in section 53501), unless\u2014 (A) at least three owners or operators of coastwise qualified vessels (as that term is defined in section 55108(a)) regularly operate such a vessel on such route; (B) each of such owners or operators transports at least 20 percent of the volume of goods on that route; and (C) none of such owners or operators are under common ownership. .",
      "versionDate": "2025-01-23",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-26T18:51:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr665",
          "measure-number": "665",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-07-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr665v00",
            "update-date": "2025-07-03"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Noncontiguous Shipping Competition Act </strong></p><p>This bill revises coastwise laws, commonly known as the Jones Act, that govern domestic transportation of merchandise or passengers by vessels.</p><p>The Jones\u00a0Act generally requires that a vessel transporting merchandise or passengers\u00a0from one U.S. point to another U.S. point be (1) built in the United States, (2)\u00a0at least 75% owned by U.S. citizens, and (3) mostly crewed by U.S. citizens. The act also includes several exemptions and exceptions.</p><p>The bill exempts carriage on a route in noncontiguous trade from Jones Act requirements unless (1) at least three owners or operators of coastwise qualified vessels regularly operate such a vessel on the route, (2) each of such owners or operators transports at least 20% of the volume of goods on that route, and (3) none of such owners or operators are under common ownership.\u00a0(Generally, <em>noncontiguous trade</em> is trade between two U.S. points where at least one of the points is in Alaska, Hawaii, Puerto Rico, or an insular territory or U.S. possession.)</p>"
        },
        "title": "Noncontiguous Shipping Competition Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr665.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Noncontiguous Shipping Competition Act </strong></p><p>This bill revises coastwise laws, commonly known as the Jones Act, that govern domestic transportation of merchandise or passengers by vessels.</p><p>The Jones\u00a0Act generally requires that a vessel transporting merchandise or passengers\u00a0from one U.S. point to another U.S. point be (1) built in the United States, (2)\u00a0at least 75% owned by U.S. citizens, and (3) mostly crewed by U.S. citizens. The act also includes several exemptions and exceptions.</p><p>The bill exempts carriage on a route in noncontiguous trade from Jones Act requirements unless (1) at least three owners or operators of coastwise qualified vessels regularly operate such a vessel on the route, (2) each of such owners or operators transports at least 20% of the volume of goods on that route, and (3) none of such owners or operators are under common ownership.\u00a0(Generally, <em>noncontiguous trade</em> is trade between two U.S. points where at least one of the points is in Alaska, Hawaii, Puerto Rico, or an insular territory or U.S. possession.)</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119hr665"
    },
    "title": "Noncontiguous Shipping Competition Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Noncontiguous Shipping Competition Act </strong></p><p>This bill revises coastwise laws, commonly known as the Jones Act, that govern domestic transportation of merchandise or passengers by vessels.</p><p>The Jones\u00a0Act generally requires that a vessel transporting merchandise or passengers\u00a0from one U.S. point to another U.S. point be (1) built in the United States, (2)\u00a0at least 75% owned by U.S. citizens, and (3) mostly crewed by U.S. citizens. The act also includes several exemptions and exceptions.</p><p>The bill exempts carriage on a route in noncontiguous trade from Jones Act requirements unless (1) at least three owners or operators of coastwise qualified vessels regularly operate such a vessel on the route, (2) each of such owners or operators transports at least 20% of the volume of goods on that route, and (3) none of such owners or operators are under common ownership.\u00a0(Generally, <em>noncontiguous trade</em> is trade between two U.S. points where at least one of the points is in Alaska, Hawaii, Puerto Rico, or an insular territory or U.S. possession.)</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119hr665"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr665ih.xml"
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
      "title": "Noncontiguous Shipping Competition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:48Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Noncontiguous Shipping Competition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 46, United States Code, to exempt certain noncontiguous trade from the coastwise laws.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:29Z"
    }
  ]
}
```
