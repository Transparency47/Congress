# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2968?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2968
- Title: Outdoor Americans with Disabilities Act
- Congress: 119
- Bill type: S
- Bill number: 2968
- Origin chamber: Senate
- Introduced date: 2025-10-03
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-03: Introduced in Senate
- 2025-10-03 - IntroReferral: Introduced in Senate
- 2025-10-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-10-03: Introduced in Senate

## Actions

- 2025-10-03 - IntroReferral: Introduced in Senate
- 2025-10-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2968",
    "number": "2968",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Outdoor Americans with Disabilities Act",
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
      "actionDate": "2025-10-03",
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
      "actionDate": "2025-10-03",
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
        "item": {
          "date": "2025-10-03T16:16:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T15:00:32Z",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2968is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2968\nIN THE SENATE OF THE UNITED STATES\nOctober 3, 2025 Mr. Lee (for himself and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo ensure access to certain public land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Outdoor Americans with Disabilities Act .\n#### 2. Definitions\nIn this Act:\n**(1) Disability-accessible land**\nThe term disability-accessible land means each square mile of public land assessed, as of the date of enactment of this Act, to have not less than 2.5 miles of authorized road accessible to motorized vehicles or off-road vehicles.\n**(2) Off-road vehicle**\nThe term off-road vehicle means any motorized vehicle capable of, or designed for, travel on or immediately over land, water, or other natural terrain.\n**(3) Public land**\nThe term public land means\u2014\n**(A)**\nNational Forest System land; and\n**(B)**\nland under the jurisdiction of the Secretary of the Interior.\n**(4) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of Agriculture (acting through the Chief of the Forest Service), with respect to National Forest System land; and\n**(B)**\nthe Secretary of the Interior, with respect to land under the jurisdiction of the Secretary of the Interior.\n#### 3. Updates to travel management plans and motor vehicle use plans\nNotwithstanding any other provision of law (including regulations), the Secretaries concerned shall prioritize updating travel management plans and motor vehicle use plans of the Bureau of Land Management and the Forest Service.\n#### 4. Motor vehicle use maps and designation of certain public land as open, limited, or closed to off-road vehicles\n##### (a) In general\nNotwithstanding any other provision of law (including regulations), the Secretary of Agriculture (acting through the Chief of the Forest Service), for purposes of developing motor vehicle use maps under section 212.56 of title 36, Code of Federal Regulations (or a successor regulation), and the Secretary of the Interior, for purposes of designating public land under the jurisdiction of the Secretary of the Interior as open, limited, or closed to off-road vehicles under section 8342.3 of title 43, Code of Federal Regulations (or a successor regulation), shall\u2014\n**(1)**\naccount for the total length of traversable, approved roads in each square mile of public land managed by the applicable Secretary concerned;\n**(2)**\nfor purposes of closing roads under the jurisdiction of the Secretary concerned, comply with the requirements established under subsection (b);\n**(3)**\nprioritize the inclusion and approval of roads on public land that provide access to diverse opportunities for recreation, including hunting, fishing, visiting cultural and natural sites, birdwatching, hiking, picnicking, camping, boating, mountain biking, and the use of motorized vehicles or off-road vehicles (including electric bicycles and over-snow vehicles);\n**(4)**\ncoordinate with appropriate Federal agencies, State, county, and other local governmental entities, and Tribal governments for purposes of identifying routes on public land that are considered to be desirable for recreation to ensure the public land is disability-accessible land;\n**(5)**\nhave the authority to revise a route on public land as the Secretary concerned determines to be necessary to address changes to conditions occurring after the date of the designation of the route; and\n**(6)**\nensure that any road that is subject to a claim under section 2477 of the Revised Statutes ( 43 U.S.C. 932 ) (repealed by section 706 of the Federal Land Policy and Management Act of 1976 ( Public Law 94\u2013579 ; 90 Stat. 2793)) that has not been adjudicated or litigated shall remain open until the adjudication or litigation has been completed.\n##### (b) Road closures\n**(1) In general**\nFor purposes of subsection (a)(2)\u2014\n**(A)**\nin the case of disability-accessible land, the Secretary concerned shall not close roads that would result in a net decrease of authorized road accessible to motorized vehicles or off-road vehicles to the extent that the public land would no longer be designated as disability-accessible land, unless\u2014\n**(i)**\nthe road on public land being closed was established during the 1-year period ending on the date of the closure to address a temporary need or emergency; or\n**(ii)**\nthe Secretary concerned\u2014\n**(I)**\ndetermines that the road on public land being closed poses a direct threat to the health or safety of personnel or visitors to the public land; and\n**(II)**\ncomplies with the requirements of paragraphs (3) and (4) with respect to the closure; and\n**(B)**\nin the case of public land that is not considered to be disability-accessible land\u2014\n**(i)**\nthe Secretary concerned shall consider opening any road on public land that was closed during the 10-year period ending on the date of enactment of this Act;\n**(ii)**\nthe Secretary concerned shall not close any additional roads on public land, unless the Secretary concerned\u2014\n**(I)**\ndetermines that the road poses a direct threat to the health or safety of personnel or visitors to the public land; and\n**(II)**\ncomplies with the requirements of paragraphs (3) and (4) with respect to the closure; and\n**(iii)**\nthe Secretary concerned shall not close any roads on public land that the Secretary concerned determines are beneficial for fuels reduction treatments, wildfire response, or search and rescue activities.\n**(2) Notice and hearing**\nFor purposes of a road closure under subparagraph (A) or (B) of paragraph (1), the Secretary concerned shall\u2014\n**(A)**\nprovide notice of the proposed closure to allow for public comment, which may be provided after the closure if the Secretary concerned determines that there is an immediate threat to the health or safety of personnel or visitors to the public land; and\n**(B)**\nconduct a public hearing with respect to the closure, which may be held after the closure if the Secretary concerned makes a determination in the affirmative under subparagraph (A).\n**(3) New roads**\nFor purposes of a road closure under subparagraph (A) or (B) of paragraph (1), the Secretary concerned shall\u2014\n**(A)**\nprovide for the nomination of new roads on public land to be added to a motor vehicle use plan or travel management plan of the Secretary concerned; and\n**(B)**\nestablish an appropriate new road on public land not later than 1 year after the date on which the road is closed under that paragraph.\n**(4) Categorical exclusion**\nA road closure that the Secretary concerned determines to be necessary under subparagraph (A) or (B) of paragraph (1) or the establishment of a new road nominated for establishment under subparagraph (A) of paragraph (3) shall be categorically excluded from the requirements of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), subject to any regulations requiring a determination that there are no extraordinary circumstances that warrant the preparation of an environmental assessment or an environmental impact statement with respect to the proposed road closure or establishment of the new road.\n**(5) Rebuttable presumption**\nFor purposes of the review of a road closure under subparagraph (A) or (B) of paragraph (1), there shall be a rebuttable presumption that roads shall remain open for public use, which may only be rebutted by clear and compelling evidence demonstrating that the closure of the road is necessary in accordance with this Act.\n##### (c) Regulations\nThe Secretaries concerned may issue or revise regulations to carry out this section.\n#### 5. Effect of Act\nNothing in this Act\u2014\n**(1)**\nprohibits the Secretary concerned from developing new roads or trails on public land for the use of motorized vehicles or off-road vehicles; or\n**(2)**\nestablishes new roads or trails in a component of the National Wilderness System, inventoried roadless area, congressionally designated primitive area, or unit of the National Park System (other than a National Recreation Area).",
      "versionDate": "2025-10-03",
      "versionType": "Introduced in Senate"
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
            "name": "Disability and health-based discrimination",
            "updateDate": "2026-02-27T17:58:45Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-02-27T17:58:39Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-02-27T17:58:54Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-02-27T17:58:49Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-02-27T17:58:30Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-02-27T17:58:25Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2026-02-27T17:58:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-01T17:43:49Z"
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
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2968is.xml"
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
      "title": "Outdoor Americans with Disabilities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Outdoor Americans with Disabilities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T02:53:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure access to certain public land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T02:48:20Z"
    }
  ]
}
```
