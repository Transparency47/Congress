# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5497?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5497
- Title: Apostle Islands National Park and Preserve Act
- Congress: 119
- Bill type: HR
- Bill number: 5497
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-04-07T20:29:55Z
- Update date including text: 2026-04-07T20:29:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-11 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-11 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 20 - 17.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-11 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-11 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 20 - 17.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5497",
    "number": "5497",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "T000165",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
        "lastName": "Tiffany",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Apostle Islands National Park and Preserve Act",
    "type": "HR",
    "updateDate": "2026-04-07T20:29:55Z",
    "updateDateIncludingText": "2026-04-07T20:29:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 20 - 17.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
        "item": [
          {
            "date": "2026-02-11T18:45:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-18T14:07:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "WI"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "WI"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "WI"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "WI"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5497ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5497\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Tiffany (for himself, Mr. Steil , Mr. Wied , Mr. Grothman , Mr. Fitzgerald , and Mr. Van Orden ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo provide for the designation of Apostle Islands National Park and Preserve, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Apostle Islands National Park and Preserve Act .\n#### 2. Apostle Islands National Park and Preserve\n##### (a) In general\n**(1) Redesignation**\nApostle Islands National Lakeshore, established under Public Law 91\u2013424 ( 16 U.S.C. 460w et seq. ), shall be known and designated as Apostle Islands National Park and Preserve , comprised of\u2014\n**(A)**\nApostle Islands National Park; and\n**(B)**\nApostle Islands National Preserve.\n**(2) Apostle islands national park**\n**(A) Boundaries**\nThe boundaries of Apostle Islands National Park are the boundaries of the area generally depicted as Apostle Islands National Park Proposed Boundary on the Map.\n**(B) Ashland harbor breakwater light**\nNothing in this Act creates a protective perimeter or buffer zone around the boundary of the property labeled Ashland Harbor Breakwater Light on the Map.\n**(3) Apostle Islands national preserve**\nThe boundaries of Apostle Islands National Preserve are the boundaries of the area generally depicted as Apostle Islands National Preserve Proposed Boundary on the Map.\n##### (b) Administration\n**(1) In general**\nThe Apostle Islands National Park and Preserve shall be administered by the Secretary as a single unit of the National Park System in accordance with\u2014\n**(A)**\nthis section;\n**(B)**\nthe laws generally applicable to units of the National Park System, including\u2014\n**(i)**\nsections 100101(a), 100751(a), 100752, 100753, and 102101 of title 54, United States Code; and\n**(ii)**\nchapters 1003 and 3201 of title 54, United States Code; and\n**(C)**\nexcept as provided in paragraph (2), Public Law 91\u2013424 ( 16 U.S.C. 460w et seq. ).\n**(2) Hunting, fishing, and trapping**\n**(A) Hunting and trapping**\n**(i) Apostle Islands National Park**\nExcept where permitted under a treaty, statute, or executive order pertaining to a Tribe, hunting and trapping are prohibited within Apostle Islands National Park.\n**(ii) Apostle Islands National Preserve**\nThe Secretary shall administer hunting and trapping within Apostle Islands National Preserve\u2014\n**(I)**\nin the same manner that hunting and trapping were administered on the day before the date of the enactment of this Act within the portion of Apostle Islands National Lakeshore that comprises Apostle Islands National Preserve; and\n**(II)**\nin accordance with section 5 of Public Law 91\u2013424 ( 16 U.S.C. 460w\u20134 ) and other applicable laws.\n**(B) Fishing**\nThe Secretary shall administer fishing within the Apostle Islands National Park and Preserve\u2014\n**(i)**\nin the same manner that fishing was administered within the Apostle Islands National Lakeshore on the day before the date of enactment of this Act; and\n**(ii)**\nin accordance with section 5 of Public Law 91\u2013424 ( 16 U.S.C. 460w\u20134 ) and other applicable laws.\n**(C) Private land**\nNothing in this section prohibits hunting, fishing, or trapping on private land in accordance with applicable State and Federal laws.\n##### (c) References and map\n**(1) References**\n**(A) In general**\nAny reference in a law, map, regulation, document, paper, or other record of the United States to Apostle Islands National Lakeshore shall be deemed to be a reference to Apostle Islands National Park and Preserve .\n**(B) Public law 91\u2013424**\nAny reference in Public Law 91\u2013424 ( 16 U.S.C. 460w et seq. ) to the lakeshore shall be deemed to be a reference to Apostle Islands National Park and Preserve .\n**(2) Map**\nThe Map shall be on file and available for public inspection in the appropriate offices of the National Park Service.\n##### (d) Interpretive features\nThe Secretary shall include at the principal visitor centers of the Apostle Islands National Park and Preserve the following interpretive features:\n**(1)**\nSignage that describes the history of the region, including information about the Ojibwe tribes, early European settlers, fur trade, logging, stone quarries, lighthouses and commercial fishing.\n**(2)**\nA copy of this Act.\n##### (e) Treaty and reserved rights\nNothing in this Act shall be construed as affecting any rights granted, reserved, or established pursuant to treaty, statute, or executive order pertaining to any Tribe, including, but not limited to, rights to hunt, trap, fish, and gather on lands included within the boundary of Apostle Islands National Park and Preserve or any other rights asserted by any Tribe.\n##### (f) Definitions\nIn this Act:\n**(1) Map**\nThe term Map means the map titled Apostle Islands National Park and Preserve Proposed Boundaries , numbered 633/193,514, and dated October 2024.\n**(2) Secretary**\nThe term Secretary means the Secretary of the Interior.",
      "versionDate": "2025-09-18",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Geography and mapping",
            "updateDate": "2026-02-27T16:32:53Z"
          },
          {
            "name": "Historic sites and heritage areas",
            "updateDate": "2026-02-27T16:32:58Z"
          },
          {
            "name": "Hunting and fishing",
            "updateDate": "2026-02-27T16:32:47Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-02-27T16:29:04Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-02-27T16:28:59Z"
          },
          {
            "name": "Wisconsin",
            "updateDate": "2026-02-27T16:28:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-01T16:29:05Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5497ih.xml"
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
      "title": "Apostle Islands National Park and Preserve Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T08:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Apostle Islands National Park and Preserve Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T08:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the designation of Apostle Islands National Park and Preserve, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T08:48:37Z"
    }
  ]
}
```
