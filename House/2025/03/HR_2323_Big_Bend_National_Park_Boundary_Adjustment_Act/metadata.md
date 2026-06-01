# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2323?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2323
- Title: Big Bend National Park Boundary Adjustment Act
- Congress: 119
- Bill type: HR
- Bill number: 2323
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2025-11-11T04:51:23Z
- Update date including text: 2025-11-11T04:51:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2323",
    "number": "2323",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "G000594",
        "district": "23",
        "firstName": "Tony",
        "fullName": "Rep. Gonzales, Tony [R-TX-23]",
        "lastName": "Gonzales",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Big Bend National Park Boundary Adjustment Act",
    "type": "HR",
    "updateDate": "2025-11-11T04:51:23Z",
    "updateDateIncludingText": "2025-11-11T04:51:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:00:50Z",
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
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "TX"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "TX"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2323ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2323\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Tony Gonzales of Texas introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo adjust the boundary of Big Bend National Park in the State of Texas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Big Bend National Park Boundary Adjustment Act .\n#### 2. Definitions\nIn this Act:\n**(1) Map**\nThe term map means the map entitled Big Bend National Park, Proposed Boundary Adjustment , numbered 155/167,296, and dated November 2022.\n**(2) Park**\nThe term Park means the Big Bend National Park established under the Act of June 20, 1935 (49 Stat. 393, chapter 283; 16 U.S.C. 156 ).\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Big Bend National Park Boundary Adjustment\n##### (a) Land acquisition\nThe Secretary may acquire approximately 6,100 acres of land or interests in land generally depicted on the map as Tracts to Include in Boundary by donation or exchange.\n##### (b) Availability of map\nThe map shall be on file and available for public inspection in the appropriate offices of the National Park Service.\n##### (c) Boundary revision and administration\nOn acquisition of any land or interests in land under subsection (a), the Secretary shall\u2014\n**(1)**\nrevise the boundary of the Park to include the acquired land or interests in land; and\n**(2)**\nadminister the acquired land or interests in land as part of the Park in accordance with applicable laws (including regulations).\n##### (d) Eminent domain or condemnation\nIn carrying out this Act, the Secretary may not use eminent domain or condemnation.",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-06-23",
        "actionTime": "15:28:55",
        "text": "Held at the desk."
      },
      "number": "1112",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Big Bend National Park Boundary Adjustment Act",
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
            "updateDate": "2025-06-20T15:36:20Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-06-20T15:36:20Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-06-20T15:36:20Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-06-20T15:36:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-21T15:19:59Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2323ih.xml"
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
      "title": "Big Bend National Park Boundary Adjustment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Big Bend National Park Boundary Adjustment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To adjust the boundary of Big Bend National Park in the State of Texas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:25Z"
    }
  ]
}
```
