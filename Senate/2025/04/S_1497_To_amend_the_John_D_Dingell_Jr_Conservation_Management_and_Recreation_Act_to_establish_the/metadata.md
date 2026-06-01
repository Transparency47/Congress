# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1497?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1497
- Title: Cerro de la Olla Wilderness Establishment Act
- Congress: 119
- Bill type: S
- Bill number: 1497
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1497",
    "number": "1497",
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
    "title": "Cerro de la Olla Wilderness Establishment Act",
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
        "item": {
          "date": "2025-04-11T02:44:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T15:00:18Z",
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
      "sponsorshipDate": "2025-04-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1497is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1497\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Heinrich (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to establish the Cerro de la Olla Wilderness in the R\u00edo Grande del Norte National Monument and to modify the boundary of the R\u00edo Grande del Norte National Monument.\n#### 1. Short title\nThis Act may be cited as the Cerro de la Olla Wilderness Establishment Act .\n#### 2. Designation of Cerro de la Olla Wilderness\n##### (a) Designation\n**(1) In general**\nSection 1202 of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( 16 U.S.C. 1132 note; Public Law 116\u20139 ; 133 Stat. 651) is amended\u2014\n**(A)**\nin the section heading, by striking Cerro del Yuta and R\u00edo San Antonio and inserting R\u00edo Grande del Norte National Monument ;\n**(B)**\nin subsection (a), by striking paragraph (1) and inserting the following:\n(1) Map The term map means the map entitled Proposed Cerro de la Olla Wilderness and R\u00edo Grande del Norte National Monument Boundary and dated April 1, 2025. ; and\n**(C)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), by adding at the end the following:\n(C) Cerro de la olla wilderness Certain Federal land administered by the Bureau of Land Management in Taos County, New Mexico, comprising approximately 12,295 acres as generally depicted on the map, which shall be known as the Cerro de la Olla Wilderness . ;\n**(ii)**\nin paragraph (4), in the matter preceding subparagraph (A), by striking this Act and inserting this Act (including a reserve common grazing allotment) ; and\n**(iii)**\nby adding at the end the following:\n(12) Wildlife water development projects in cerro de la olla wilderness (A) In general Subject to subparagraph (B) and in accordance with section 4(c) of the Wilderness Act ( 16 U.S.C. 1133(c) ), the Secretary may authorize the maintenance of any structure or facility in existence on the date of enactment of this paragraph for wildlife water development projects (including guzzlers) in the Cerro de la Olla Wilderness if, as determined by the Secretary\u2014 (i) the structure or facility would enhance wilderness values by promoting healthy, viable, and more naturally distributed wildlife populations; and (ii) the visual impacts of the structure or facility on the Cerro de la Olla Wilderness can reasonably be minimized. (B) Cooperative agreement Not later than 1 year after the date of enactment of this paragraph, the Secretary shall enter into a cooperative agreement with the State of New Mexico that specifies, subject to section 4(c) of the Wilderness Act ( 16 U.S.C. 1133(c) ), the terms and conditions under which wildlife management activities in the Cerro de la Olla Wilderness may be carried out. .\n**(2) Clerical amendment**\nThe table of contents for the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 581) is amended by striking the item relating to section 1202 and inserting the following:\nSec. 1202. R\u00edo Grande del Norte National Monument Wilderness Areas. .\n##### (b) R\u00edo grande del norte national monument boundary modification\nThe boundary of the R\u00edo Grande del Norte National Monument in the State of New Mexico is modified, as depicted on the map entitled Proposed Cerro de la Olla Wilderness and R\u00edo Grande del Norte National Monument Boundary and dated April 1, 2025.",
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
        "actionDate": "2025-04-17",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2944",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Cerro de la Olla Wilderness Establishment Act",
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
            "name": "Land use and conservation",
            "updateDate": "2026-02-13T17:06:30Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2026-02-13T17:06:30Z"
          },
          {
            "name": "New Mexico",
            "updateDate": "2026-02-13T17:06:30Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-02-13T17:06:30Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-02-13T17:06:30Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2026-02-13T17:06:30Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-02-13T17:06:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-22T15:14:11Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1497is.xml"
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
      "title": "Cerro de la Olla Wilderness Establishment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Cerro de la Olla Wilderness Establishment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to establish the Cerro de la Olla Wilderness in the Rio Grande del Norte National Monument and to modify the boundary of the Rio Grande del Norte National Monument.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T03:48:25Z"
    }
  ]
}
```
