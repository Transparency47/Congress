# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1319?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1319
- Title: Pecos Watershed Protection Act
- Congress: 119
- Bill type: S
- Bill number: 1319
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1319",
    "number": "1319",
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
    "title": "Pecos Watershed Protection Act",
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
      "actionDate": "2025-12-02",
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
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:51:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:26Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1319is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1319\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Heinrich (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo withdraw certain Federal land in the Pecos Watershed area of the State of New Mexico from mineral entry, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pecos Watershed Protection Act .\n#### 2. Withdrawal of Federal land in Pecos Watershed area, New Mexico\n##### (a) Definition of Federal land\nIn this section, the term Federal land means the Federal land depicted as Pecos Withdrawal on the map entitled Proposed Mineral Withdrawal Legislative Map and dated September 11, 2023.\n##### (b) Withdrawal\nSubject to valid rights in existence on the date of enactment of this Act, the Federal land is withdrawn from all forms of\u2014\n**(1)**\nentry, appropriation, or disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\ndisposition under all laws pertaining to mineral and geothermal leasing or mineral materials.\n#### 3. Designation of Thompson Peak Wilderness Area, New Mexico\n##### (a) Definitions\nIn this section:\n**(1) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(2) State**\nThe term State means the State of New Mexico.\n**(3) Wilderness area**\nThe term wilderness area means the Thompson Peak Wilderness Area designated by subsection (b).\n##### (b) Designation\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the approximately 11,599 acres of land managed by the Forest Service in the State, as generally depicted on the map entitled Proposed Mineral Withdrawal Legislative Map and dated September 11, 2023, is designated as a wilderness area and as a component of the National Wilderness Preservation System, to be known as the Thompson Peak Wilderness Area .\n##### (c) Map and legal description\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file a map and legal description of the wilderness area with\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Natural Resources of the House of Representatives.\n**(2) Effect**\nThe map and legal description filed under paragraph (1) shall have the same force and effect as if included in this Act, except that the Secretary may correct clerical and typographical errors in the map and legal description.\n**(3) Availability**\nThe map and legal description filed under paragraph (1) shall be on file and available for public inspection in the Office of the Chief of the Forest Service.\n##### (d) Administration\n**(1) In general**\nSubject to valid existing rights, the wilderness area shall be administered by the Secretary in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), except that any reference in that Act to the effective date of that Act shall be considered to be a reference to the date of enactment of this Act.\n**(2) Adjacent management**\n**(A) No protective perimeters or buffer zones**\nCongress does not intend for the designation of the wilderness area to create a protective perimeter or buffer zone around the wilderness area.\n**(B) Nonwilderness activities**\nThe fact that nonwilderness activities or uses outside of the wilderness area can be seen or heard from an area within the wilderness area shall not preclude the conduct of the nonwilderness activities or uses outside the boundaries of the wilderness area.\n**(3) Fish and wildlife management**\nIn accordance with section 4(d)(7) of the Wilderness Act ( 16 U.S.C. 1133(d)(7) ), nothing in this section affects the jurisdiction or responsibilities of the State with respect to fish and wildlife management in the wilderness area (including the regulation of hunting, fishing, and trapping).\n**(4) Grazing**\nThe Secretary shall allow the continuation of the grazing of livestock in the wilderness area, if established before the date of enactment of this Act, in accordance with\u2014\n**(A)**\nsection 4(d)(4) of the Wilderness Act ( 16 U.S.C. 1133(d)(4) ); and\n**(B)**\nthe guidelines set forth in Appendix A of the report of the Committee on Interior and Insular Affairs of the House of Representatives accompanying H.R. 2570 of the 101st Congress (H. Rept. 101\u2013405).\n**(5) Wildfire, insect, and disease control**\nThe Secretary may carry out measures in the wilderness area that the Secretary determines to be necessary to control fire, insects, or diseases, in accordance with section 4(d)(1) of the Wilderness Act ( 16 U.S.C. 1133(d)(1) ).\n##### (e) Incorporation of acquired land and interests in land\nAny land or interest in land within the boundaries of the wilderness area that is acquired by the United States after the date of enactment of this Act shall be added to and administered as part of the wilderness area.\n##### (f) Withdrawal\nSubject to valid existing rights, the wilderness area is withdrawn from\u2014\n**(1)**\nentry, appropriation, or disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\ndisposition under all laws relating to mineral and geothermal leasing or mineral materials.",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-04-08",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2727",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Pecos Watershed Protection Act",
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
            "name": "Geography and mapping",
            "updateDate": "2025-12-09T15:17:15Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-12-09T15:17:15Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-12-09T15:17:15Z"
          },
          {
            "name": "New Mexico",
            "updateDate": "2025-12-09T15:17:15Z"
          },
          {
            "name": "Watersheds",
            "updateDate": "2025-12-09T15:17:15Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-12-09T15:17:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-21T21:48:20Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1319is.xml"
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
      "title": "Pecos Watershed Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pecos Watershed Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-22T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to withdraw certain Federal land in the Pecos Watershed area of the State of New Mexico from mineral entry, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-22T03:48:25Z"
    }
  ]
}
```
