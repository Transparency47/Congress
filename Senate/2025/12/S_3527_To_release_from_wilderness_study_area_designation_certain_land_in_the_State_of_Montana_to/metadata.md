# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3527
- Title: Montana Sportsmen Conservation Act
- Congress: 119
- Bill type: S
- Bill number: 3527
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-04-16T18:35:25Z
- Update date including text: 2026-04-16T18:35:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3527",
    "number": "3527",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Montana Sportsmen Conservation Act",
    "type": "S",
    "updateDate": "2026-04-16T18:35:25Z",
    "updateDateIncludingText": "2026-04-16T18:35:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
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
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-17",
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
            "date": "2026-03-04T16:02:28Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-17T18:14:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T15:00:42Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3527is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3527\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Daines (for himself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo release from wilderness study area designation certain land in the State of Montana, to improve the management of that land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Montana Sportsmen Conservation Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nunder the Montana Wilderness Study Act of 1977 ( Public Law 95\u2013150 ; 91 Stat. 1243), 9 wilderness study areas comprising a total of 973,000 acres of land in the State of Montana were set aside for the Secretary of Agriculture to evaluate the suitability of the wilderness study areas for designation as wilderness, in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), with the evaluation to be completed not later than 5 years after the date of enactment of the Montana Wilderness Study Act of 1977 ( Public Law 95\u2013150 ; 91 Stat. 1243);\n**(2)**\nbetween 1979 and 1986, the Chief of the Forest Service\u2014\n**(A)**\ncompleted the studies of the 9 wilderness study areas referred to in paragraph (1); and\n**(B)**\nbased on those studies, determined that 608,700 acres of the original 973,000 acres designated as wilderness study areas by the Montana Wilderness Study Act of 1977 ( Public Law 95\u2013150 ; 91 Stat. 1243) were unsuitable for inclusion in the National Wilderness Preservation System, including the 81,000 acres within the Middle Fork Judith Wilderness Study Area;\n**(3)**\nin 2021, following a 6-year collaborative process, the Forest Service again determined, in the revision of the Helena Lewis and Clark National Forest plan, that the Middle Fork Judith Wilderness Study Area is unsuitable for inclusion in the National Wilderness Preservation System;\n**(4)**\nunder the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ), 38 wilderness study areas comprising a total of 447,327 acres of land in the State of Montana were set aside by the Bureau of Land Management to evaluate the suitability of the wilderness study areas for designation as wilderness, with the evaluation to be completed not later than 15 years after the date of enactment of that Act;\n**(5)**\nin 1991, the Director of the Bureau of Land Management submitted to the President a recommendation on the suitability for designation of the areas described in paragraph (4), which was subsequently submitted to Congress, under which the Director of the Bureau of Land Management determined that 273,828 acres in the State of Montana designated as wilderness study areas by the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ) were unsuitable for wilderness designation, including\u2014\n**(A)**\nthe 11,380 acres of land within the Hoodoo Mountain Wilderness Study Area; and\n**(B)**\nthe 11,580 acres of land within the Wales Creek Wilderness Study Area;\n**(6)**\nin 2020, following a 5-year collaborative process, the Bureau of Land Management, in the revision of the Missoula Resource Management Plan\u2014\n**(A)**\nreaffirmed that the Hoodoo Mountain Wilderness Study Area and the Wales Creek Wilderness Study Area were unsuitable for wilderness designation; and\n**(B)**\nrecommended alternative management parameters for the Hoodoo Mountain Wilderness Study Area and the Wales Creek Wilderness Study Area;\n**(7)**\ndespite the recommendations of the Forest Service and the Bureau of Land Management, after the completion of the studies for suitability of the land in the State of Montana designated as wilderness study areas under the Montana Wilderness Study Act of 1977 ( Public Law 95\u2013150 ; 91 Stat. 1243) and the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. )\u2014\n**(A)**\nover 1,100,000 acres of public land in the State of Montana remain as wilderness study areas until Congress acts; and\n**(B)**\nover 700,000 acres of public land in the State of Montana currently designated as wilderness study areas have been determined unsuitable for wilderness management;\n**(8)**\nif the wilderness study area designation was removed from each of the Middle Fork Judith Wilderness Study Area, the Hoodoo Mountain Wilderness Study Area, and the Wales Creek Wilderness Study Area, land managers would be able to better conserve and manage the areas in accordance with applicable land and resource management plans that retain certain protections for the areas, while providing for\u2014\n**(A)**\nenhanced sportsmen opportunities in the backcountry of Montana;\n**(B)**\nimproved public access; and\n**(C)**\nthe conduct of wildlife habitat and wildfire mitigation projects;\n**(9)**\nthe applicable land and resource management plans referred to in paragraph (8) were developed through a multi-year, collaborative process supported by\u2014\n**(A)**\nresource needs and conditions; and\n**(B)**\nthe best available science; and\n**(10)**\nfollowing release, the respective land management agencies shall continue managing the areas described in paragraph (8)\u2014\n**(A)**\nin accordance with applicable environmental and administrative laws; and\n**(B)**\nbased on local input, multiple-use and sustained yield principles, and land management objectives.\n#### 3. Release and improved management of land comprising certain wilderness study areas\n##### (a) Middle Fork Judith Wilderness Study Area\nThe approximately 81,000 acres of land comprising the Middle Fork Judith Wilderness Study Area\u2014\n**(1)**\nshall no longer be subject to section 3(a) of the Montana Wilderness Study Act of 1977 ( Public Law 95\u2013150 ; 91 Stat. 1244); and\n**(2)**\nshall be managed in accordance with the applicable land and resource management plan most recently adopted under section 6 of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1604 ).\n##### (b) Hoodoo Mountain Wilderness Study Area and Wales Creek Wilderness Study Area\nThe approximately 11,380 acres of land comprising the Hoodoo Mountain Wilderness Study Area and the approximately 11,580 acres of land comprising the Wales Creek Wilderness Study Area\u2014\n**(1)**\nshall no longer be subject to section 603(c) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1782(c) ); and\n**(2)**\nshall be managed in accordance with the applicable land management plans adopted under section 202 of that Act ( 43 U.S.C. 1712 ).",
      "versionDate": "2025-12-17",
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
        "actionDate": "2025-12-17",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "6788",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Montana Sportsmen Conservation Act",
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
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-02-19T19:40:49Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-02-19T19:40:49Z"
          },
          {
            "name": "Montana",
            "updateDate": "2026-02-19T19:40:49Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2026-02-19T19:40:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-01-13T16:01:53Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3527is.xml"
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
      "title": "Montana Sportsmen Conservation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Montana Sportsmen Conservation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T05:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to release from wilderness study area designation certain land in the State of Montana, to improve the management of that land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T05:18:19Z"
    }
  ]
}
```
