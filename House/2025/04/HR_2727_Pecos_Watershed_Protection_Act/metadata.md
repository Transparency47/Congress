# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2727?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2727
- Title: Pecos Watershed Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 2727
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2026-01-16T09:06:16Z
- Update date including text: 2026-01-16T09:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Natural Resources.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2727",
    "number": "2727",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000273",
        "district": "3",
        "firstName": "Teresa",
        "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
        "lastName": "Leger Fernandez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Pecos Watershed Protection Act",
    "type": "HR",
    "updateDate": "2026-01-16T09:06:16Z",
    "updateDateIncludingText": "2026-01-16T09:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:02:00Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NM"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "NM"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2727ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2727\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Ms. Leger Fernandez (for herself and Ms. Stansbury ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo withdraw certain Federal land in the Pecos Watershed area of the State of New Mexico from mineral entry, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pecos Watershed Protection Act .\n#### 2. Withdrawal of Federal land in Pecos Watershed area, New Mexico\n##### (a) Definition of Federal land\nIn this section, the term Federal land means the Federal land depicted as Pecos Withdrawal on the map entitled Proposed Mineral Withdrawal Legislative Map and dated September 11, 2023.\n##### (b) Withdrawal\nSubject to valid rights in existence on the date of enactment of this Act, the Federal land is withdrawn from all forms of\u2014\n**(1)**\nentry, appropriation, or disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\ndisposition under all laws pertaining to mineral and geothermal leasing or mineral materials.\n#### 3. Designation of Thompson Peak Wilderness Area, New Mexico\n##### (a) Definitions\nIn this section:\n**(1) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(2) State**\nThe term State means the State of New Mexico.\n**(3) Wilderness area**\nThe term wilderness area means the Thompson Peak Wilderness Area designated by subsection (b).\n##### (b) Designation\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the approximately 11,599 acres of land managed by the Forest Service in the State, as generally depicted on the map entitled Proposed Mineral Withdrawal Legislative Map and dated September 11, 2023, is designated as a wilderness area and as a component of the National Wilderness Preservation System, to be known as the Thompson Peak Wilderness Area .\n##### (c) Map and legal description\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file a map and legal description of the wilderness area with\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Natural Resources of the House of Representatives.\n**(2) Effect**\nThe map and legal description filed under paragraph (1) shall have the same force and effect as if included in this Act, except that the Secretary may correct clerical and typographical errors in the map and legal description.\n**(3) Availability**\nThe map and legal description filed under paragraph (1) shall be on file and available for public inspection in the Office of the Chief of the Forest Service.\n##### (d) Administration\n**(1) In general**\nSubject to valid existing rights, the wilderness area shall be administered by the Secretary in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), except that any reference in that Act to the effective date of that Act shall be considered to be a reference to the date of enactment of this Act.\n**(2) Adjacent management**\n**(A) No protective perimeters or buffer zones**\nCongress does not intend for the designation of the wilderness area to create a protective perimeter or buffer zone around the wilderness area.\n**(B) Nonwilderness activities**\nThe fact that nonwilderness activities or uses outside of the wilderness area can be seen or heard from an area within the wilderness area shall not preclude the conduct of the nonwilderness activities or uses outside the boundaries of the wilderness area.\n**(3) Fish and wildlife management**\nIn accordance with section 4(d)(7) of the Wilderness Act ( 16 U.S.C. 1133(d)(7) ), nothing in this section affects the jurisdiction or responsibilities of the State with respect to fish and wildlife management in the wilderness area (including the regulation of hunting, fishing, and trapping).\n**(4) Grazing**\nThe Secretary shall allow the continuation of the grazing of livestock in the wilderness area, if established before the date of enactment of this Act, in accordance with\u2014\n**(A)**\nsection 4(d)(4) of the Wilderness Act ( 16 U.S.C. 1133(d)(4) ); and\n**(B)**\nthe guidelines set forth in Appendix A of the report of the Committee on Interior and Insular Affairs of the House of Representatives accompanying H.R. 2570 of the 101st Congress (H. Rept. 101\u2013405).\n**(5) Wildfire, insect, and disease control**\nThe Secretary may carry out measures in the wilderness area that the Secretary determines to be necessary to control fire, insects, or diseases, in accordance with section 4(d)(1) of the Wilderness Act ( 16 U.S.C. 1133(d)(1) ).\n##### (e) Incorporation of acquired land and interests in land\nAny land or interest in land within the boundaries of the wilderness area that is acquired by the United States after the date of enactment of this Act shall be added to and administered as part of the wilderness area.\n##### (f) Withdrawal\nSubject to valid existing rights, the wilderness area is withdrawn from\u2014\n**(1)**\nentry, appropriation, or disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\ndisposition under all laws relating to mineral and geothermal leasing or mineral materials.",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-12-02",
        "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held."
      },
      "number": "1319",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Pecos Watershed Protection Act",
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
            "name": "Geography and mapping",
            "updateDate": "2025-12-09T15:17:31Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-12-09T15:17:31Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-12-09T15:17:31Z"
          },
          {
            "name": "New Mexico",
            "updateDate": "2025-12-09T15:17:31Z"
          },
          {
            "name": "Watersheds",
            "updateDate": "2025-12-09T15:17:31Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-12-09T15:17:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-21T21:41:26Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2727ih.xml"
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
      "title": "Pecos Watershed Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-17T05:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pecos Watershed Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T05:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To withdraw certain Federal land in the Pecos Watershed area of the State of New Mexico from mineral entry, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T05:33:39Z"
    }
  ]
}
```
