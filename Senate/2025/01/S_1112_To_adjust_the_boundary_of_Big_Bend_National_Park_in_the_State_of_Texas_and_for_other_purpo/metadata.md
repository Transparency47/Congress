# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1112?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1112
- Title: Big Bend National Park Boundary Adjustment Act
- Congress: 119
- Bill type: S
- Bill number: 1112
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-06-18 - Floor: Passed Senate without amendment by Voice Vote. (text: CR S3460)
- 2025-06-18 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Voice Vote.
- 2025-06-18 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2025-06-18 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent. (consideration: CR S3458)
- 2025-06-23 - Floor: Message on Senate action sent to the House.
- 2025-06-23 15:19:24 - Floor: Received in the House.
- 2025-06-23 15:28:55 - Floor: Held at the desk.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-06-18 - Floor: Passed Senate without amendment by Voice Vote. (text: CR S3460)
- 2025-06-18 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Voice Vote.
- 2025-06-18 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2025-06-18 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent. (consideration: CR S3458)
- 2025-06-23 - Floor: Message on Senate action sent to the House.
- 2025-06-23 15:19:24 - Floor: Received in the House.
- 2025-06-23 15:28:55 - Floor: Held at the desk.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1112",
    "number": "1112",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Big Bend National Park Boundary Adjustment Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-06-23",
      "actionTime": "15:28:55",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-06-23",
      "actionTime": "15:19:24",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Voice Vote. (text: CR S3460)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Voice Vote.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Energy and Natural Resources discharged by Unanimous Consent. (consideration: CR S3458)",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
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
            "date": "2025-06-18T17:24:45Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-03-25T18:46:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
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
      "sponsorshipDate": "2025-03-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1112is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1112\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Cornyn (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo adjust the boundary of Big Bend National Park in the State of Texas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Big Bend National Park Boundary Adjustment Act .\n#### 2. Definitions\nIn this Act:\n**(1) Map**\nThe term map means the map entitled Big Bend National Park, Proposed Boundary Adjustment , numbered 155/167,296, and dated November 2022.\n**(2) Park**\nThe term Park means the Big Bend National Park established under the Act of June 20, 1935 (49 Stat. 393, chapter 283; 16 U.S.C. 156 ).\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Big Bend National Park Boundary Adjustment\n##### (a) Land acquisition\nThe Secretary may acquire approximately 6,100 acres of land or interests in land generally depicted on the map as Tracts to Include in Boundary by donation or exchange.\n##### (b) Availability of map\nThe map shall be on file and available for public inspection in the appropriate offices of the National Park Service.\n##### (c) Boundary revision and administration\nOn acquisition of any land or interests in land under subsection (a), the Secretary shall\u2014\n**(1)**\nrevise the boundary of the Park to include the acquired land or interests in land; and\n**(2)**\nadminister the acquired land or interests in land as part of the Park in accordance with applicable laws (including regulations).\n##### (d) Eminent domain or condemnation\nIn carrying out this Act, the Secretary may not use eminent domain or condemnation.",
      "versionDate": "2025-03-25",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1112es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1112\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo adjust the boundary of Big Bend National Park in the State of Texas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Big Bend National Park Boundary Adjustment Act .\n#### 2. Definitions\nIn this Act:\n**(1) Map**\nThe term map means the map entitled Big Bend National Park, Proposed Boundary Adjustment , numbered 155/167,296, and dated November 2022.\n**(2) Park**\nThe term Park means the Big Bend National Park established under the Act of June 20, 1935 (49 Stat. 393, chapter 283; 16 U.S.C. 156 ).\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Big Bend National Park Boundary Adjustment\n##### (a) Land acquisition\nThe Secretary may acquire approximately 6,100 acres of land or interests in land generally depicted on the map as Tracts to Include in Boundary by donation or exchange.\n##### (b) Availability of map\nThe map shall be on file and available for public inspection in the appropriate offices of the National Park Service.\n##### (c) Boundary revision and administration\nOn acquisition of any land or interests in land under subsection (a), the Secretary shall\u2014\n**(1)**\nrevise the boundary of the Park to include the acquired land or interests in land; and\n**(2)**\nadminister the acquired land or interests in land as part of the Park in accordance with applicable laws (including regulations).\n##### (d) Eminent domain or condemnation\nIn carrying out this Act, the Secretary may not use eminent domain or condemnation.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-03-25",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2323",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Big Bend National Park Boundary Adjustment Act",
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
            "updateDate": "2025-06-20T15:35:36Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-06-20T15:35:44Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-06-20T15:35:50Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-06-20T15:35:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-21T16:10:44Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1112is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1112es.xml"
        }
      ],
      "type": "Engrossed in Senate"
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
      "updateDate": "2025-06-24T11:03:17Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Big Bend National Park Boundary Adjustment Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-06-19T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Big Bend National Park Boundary Adjustment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to adjust the boundary of Big Bend National Park in the State of Texas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T03:03:39Z"
    }
  ]
}
```
