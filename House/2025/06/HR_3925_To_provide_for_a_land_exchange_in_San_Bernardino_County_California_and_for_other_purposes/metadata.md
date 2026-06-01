# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3925?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3925
- Title: Yuhaaviatam of San Manuel Nation Land Exchange Act
- Congress: 119
- Bill type: HR
- Bill number: 3925
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-12-05T22:57:39Z
- Update date including text: 2025-12-05T22:57:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-09-04 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-09-09 - Committee: Subcommittee Hearings Held
- Latest action: 2025-06-11: Introduced in House

## Actions

- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-09-04 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-09-09 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3925",
    "number": "3925",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Yuhaaviatam of San Manuel Nation Land Exchange Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:57:39Z",
    "updateDateIncludingText": "2025-12-05T22:57:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-04",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-09-09T19:09:32Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-09-04T21:43:13Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3925ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3925\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. Obernolte introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo provide for a land exchange in San Bernardino County, California, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Yuhaaviatam of San Manuel Nation Land Exchange Act .\n#### 2. Exchange of land\n##### (a) Definitions\nIn this Act:\n**(1) Federal Land**\nThe term Federal Land means the approximately 1,475 acres of National Forest System land (including any and all privileges, easements, subsurface rights, hereditaments, improvements and appurtenances thereon and thereto) depicted as F\u20131 and F\u20132 on the Federal Land Maps.\n**(2) Federal Land Maps**\nThe term Federal Land Maps means the maps entitled\u2014\n**(A)**\nSan Manuel Ancestral Land Exchange, San Bernardino National Forest, San Bernardino County, California, Federal Lands Proposed for Exchange (map 1 of 2) , created July 8, 2022, revised January 10, 2023; and\n**(B)**\nSan Manuel Ancestral Land Exchange, San Bernardino National Forest, San Bernardino County, California, Federal Lands Proposed for Exchange (map 2 of 2) , created July 8, 2022, revised January 10, 2023.\n**(3) Nation**\nThe term Nation means the Yuhaaviatam of San Manuel Nation, a federally recognized tribe, also recognized as the San Manuel Band of Mission Indians.\n**(4) Non-Federal Land**\nThe term Non-Federal Land means the approximately 1,460 acres of land (including any and all privileges, easements, subsurface rights, hereditaments, improvements and appurtenances thereon and thereto) owned by the Nation and depicted on the Non-Federal Land Maps as NF\u20131, NF\u20132, NF\u20133, NF\u20134a, and NF\u20135.\n**(5) Non-Federal Land Maps**\nThe term Non-Federal Land Maps means the maps entitled\u2014\n**(A)**\nSan Manuel Ancestral Land Exchange San Bernardino National Forest, San Bernardino County, California, Non-Federal Lands Proposed for Exchange (map 1 of 4) , created March 8, 2022, revised January 9, 2023;\n**(B)**\nSan Manuel Ancestral Land Exchange San Bernardino National Forest, San Bernardino County, California, Non-Federal Lands Proposed for Exchange (map 2 of 4) , created March 8, 2022, revised January 9, 2023;\n**(C)**\nSan Manuel Ancestral Land Exchange San Bernardino National Forest, San Bernardino County, California, Non-Federal Lands Proposed for Exchange (map 3 of 4) , created March 8, 2022, revised January 9, 2023; and\n**(D)**\nSan Manuel Ancestral Land Exchange San Bernardino National Forest, San Bernardino County, California, Non-Federal Lands Proposed for Exchange (map 4 of 4) , created July 8, 2022, revised January 9, 2023.\n**(6) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (b) Land exchange\nSubject to the provisions of this section, if the Nation offers to convey to the United States all right, title, and interest of the Nation in and to the Non-Federal Land, the Secretary shall, as soon as practicable within the 120-day period beginning on the date on which the Secretary receives such offer\u2014\n**(1)**\naccept the offer; and\n**(2)**\nconvey to the Nation all right, title, and interest of the United States in and to the Federal Land, excepting and reserving an easement for access and use by the Forest Service any portion of Forest Service roads 1N22, 1N24, and 1N25 located on the Federal Land.\n##### (c) Survey\n**(1) Federal land**\nThe exact acreage and legal description of the Federal Land to be conveyed under subsection (b) shall be determined by a survey reasonably satisfactory to the Secretary and the Nation.\n**(2) Non-Federal land**\n**(A) In general**\nThe exact acreage and legal description of the Non-Federal Land to be conveyed under subsection (b) shall be determined by a survey reasonably satisfactory to the Secretary and the Nation.\n**(B) Cost**\nThe cost of the survey in subparagraph (A) shall be borne by the Nation.\n##### (d) Maps, estimates, and descriptions\n**(1) Minor error**\nThe Secretary and the Nation may, by mutual agreement\u2014\n**(A)**\nmake minor boundary adjustments to the lands to be exchanged under subsection (b); and\n**(B)**\ncorrect any minor errors in any map, acreage estimate, or description of the land to be exchanged under subsection (b).\n**(2) Conflict**\nIf there is a conflict between a map, acreage estimate, or description of any land to be exchanged under subsection (b), the map shall control unless the Secretary and the Nation mutually agree otherwise.\n**(3) Availability of maps**\nThe Federal Land Map and the Non-Federal Land Map shall be kept on file and available for public inspection in the office of the Regional Forester, Pacific Southwest Region, United States Forest Service, or any other appropriate office of the Forest Service, as determined by the Secretary.\n##### (e) Arrowhead Landmark preservation\n**(1) Agreement**\nAs a condition of the conveyance under subsection (b), not later than 120 days after the date of enactment of this Act, the Nation shall enter into an agreement with the Secretary under which the Nation agrees to preserve, to an extent mutually agreed upon, the historical and cultural integrity of the Arrowhead landmark site denoted on the Federal Land Maps as Arrowhead Landmark GA .\n**(2) Records**\nThe agreement entered into under paragraph (1) shall be recorded in the official records of the County of San Bernardino, California, and an in an appropriate records system of the Forest Service, as determined by the Secretary.\n##### (f) Management of land\nLand acquired by the Secretary under this section shall become part of the San Bernardino National Forest and be managed in accordance with the laws, rules, and regulations applicable to such National Forest.\n##### (g) Federal Land Policy Management Act of 1976\nThe land exchange under subsection (b) is not subject to section 206 of the Federal Land Policy Management Act of 1976 ( 43 U.S.C. 1716 ).",
      "versionDate": "2025-06-11",
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
        "actionDate": "2025-09-11",
        "text": "Read twice and referred to the Committee on Indian Affairs. (Sponsor introductory remarks on measure: CR S6578)"
      },
      "number": "2796",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Yuhaaviatam of San Manuel Nation Land Exchange Act",
      "type": "S"
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
            "name": "California",
            "updateDate": "2025-09-19T19:54:18Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-09-19T19:54:33Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-09-19T19:54:28Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-09-19T19:54:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-09-24T15:51:28Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3925ih.xml"
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
      "title": "Yuhaaviatam of San Manuel Nation Land Exchange Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Yuhaaviatam of San Manuel Nation Land Exchange Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for a land exchange in San Bernardino County, California, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T04:18:23Z"
    }
  ]
}
```
