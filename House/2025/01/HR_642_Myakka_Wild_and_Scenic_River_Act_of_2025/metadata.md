# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/642?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/642
- Title: Myakka Wild and Scenic River Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 642
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-05-30T08:06:09Z
- Update date including text: 2026-05-30T08:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Natural Resources.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/642",
    "number": "642",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Myakka Wild and Scenic River Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:09Z",
    "updateDateIncludingText": "2026-05-30T08:06:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:05:00Z",
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
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "FL"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "FL"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "FL"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr642ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 642\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Steube (for himself and Mr. Buchanan ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Wild and Scenic Rivers Act to designate the portion of the Myakka River lying within Sarasota County, Florida as a component of the National Wild and Scenic Rivers System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Myakka Wild and Scenic River Act of 2025 .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nPublic Law 95\u2013625 amended section 5 of the Wild and Scenic Rivers Act ( 16 U.S.C. 1276 ) to require the study of the Myakka River for potential inclusion in the national wild and scenic rivers system.\n**(2)**\nThe study determined the Myakka River, was eligible for inclusion in the National Wild and Scenic Rivers System.\n**(3)**\nThe State of Florida has demonstrated its commitment to protecting this river by the enactment of the Myakka River Wild and Scenic Designation and Protection Act (Florida Statute Chapter 258.501).\n**(4)**\nThe Florida county of Sarasota and the cities of Venice and North Port have demonstrated their commitment to protect this river in their comprehensive land use plans, local ordinances, and land development regulations.\n**(5)**\nThe desire for designation of this river as a component of the National Wild and Scenic Rivers System has been demonstrated through strong public support, State and local agency support, and the endorsement of designation by the Myakka River Management Coordinating Council, which represents a broad cross section of State and local agencies, agricultural interests, landowners, environmental, and nonprofit organizations.\n**(6)**\nA 12-mile segment of the Myakka River is within the Myakka River State Park with an additional 22-mile segment containing conservation lands held in public ownership or conservation easements within the Myakka River Watershed.\n#### 3. Designation of Myakka River, Florida, as a component of the National Wild and Scenic Rivers System\n##### (a)\nSection 3(a) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(a) ) is amended by adding at the end the following new paragraph:\n(___) Myakka River, Florida The 34-mile segments, within Sarasota County referred to in this paragraph, to be administered by the Secretary of the Interior, in partnership with the Myakka River Management Coordinating Council. .\n##### (b) In general\nThe following segments of the Myakka River, within Sarasota County, to be administered in the following classifications:\n(A) The approximately 8.0-mile segment from the Manatee County/Sarasota County line to S.R. 72, as a scenic river. (B) The approximately 11.2-mile segment, from S.R. 72 to Laurel Road, as a wild river. (C) The approximately 1.9-mile segment, from Laurel Road to Border Road, as a scenic river. (D) The approximately 1.5-mile segment, from Border Road to just south of the I-75 Bridge, as a recreational river. (E) The approximately 1.5-mile segment, from south of the I-75 Bridge to Snook Haven, as a scenic river. (F) The approximately 3.2-mile segment, from Snook Haven to Ramblers Rest, as a wild river. (G) The approximately 2.7-mile segment, from Ramblers Rest to U.S. 41, as a scenic river. (H) The approximately 4.0-mile segment, from U.S. 41 to the Charlotte County Line, as a scenic river. .\n#### 4. Special requirements applicable to Myakka River\n##### (a) Definitions\nIn this section and section 5:\n**(1) Myakka river**\nThe term Myakka River means the segments of the Myakka River in the State of Florida designated as components of the National Wild and Scenic Rivers System by paragraph (_) of section 3(a) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(a) ), as added by this Act.\n**(2) Council**\nThe term Council means the Myakka River Management Coordinating Council established pursuant to Florida Statute Chapter 258.501.\n**(3) Comprehensive management plan**\nThe terms comprehensive management plan and plan mean the Myakka River Wild and Scenic Management Plan developed by the Council shall be considered to satisfy the requirements for the comprehensive management plan under section 3(d) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(d) ).\n**(4) Secretary**\nThe term Secretary means the Secretary of the Interior.\n##### (b) Cooperative agreements\n**(1) Use authorized**\nIn order to provide for the long-term protection, preservation, and enhancement of the Myakka River, the Secretary shall coordinate administration responsibilities under this section, and may enter into cooperative agreements pursuant to sections 10(e) and 11(b)(1) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1281(e) , 1282(b)(1)) with the State of Florida Department of Environmental Protection, Division of Recreation and Parks, appropriate local political jurisdictions of the State, the county of Sarasota, City of North Port, City of Venice and appropriate local planning and non-profit organizations.\n**(2) Effect of agreement**\nAdministration of the Myakka River by the Secretary of the Interior through the use of cooperative agreements shall not\u2014\n**(A)**\nconstitute National Park Service administration of the Myakka River for purposes of section 10(c) of such Act ( U.S.C. 1281(c)); or\n**(B)**\ncause the Myakka River to be considered a unit of the National Park System.\n**(3) Publicly owned lands**\nNothing in this Act or an agreement under this Act shall affect the management of publicly or privately owned lands within the boundaries of the Myakka River watershed by the agencies having jurisdiction over the lands, in accordance with the statutory authority of Florida Statute 258.501 and the mission of such agencies.\n**(4) Technical assistance and other support**\nThe Secretary may provide technical assistance, staff support, and funding to assist in the updating and implementation of the comprehensive management plan.\n**(5) Acquisition of land**\nthe authority of the Secretary to acquire land for the Myakka River segments shall be limited to acquisition by donation or acquisition with the consent of the owner thereof.\n**(6) No condemnation**\nNo land or interest in land may be acquired for the Myakka River segments by condemnation.\n#### 5. Myakka River Management Council\n##### (a) Existing structure\nthe Secretary shall coordinate the management responsibilities of the Secretary with the Council in the updating and implementation of the comprehensive management plan for the Myakka River.\n##### (b) Representative from DOI\nThe Secretary shall select a representative who shall be added to the Council to represent the National Park Service.\n##### (c) Additional members\nOther interested parties may be added to the Council, in accordance with the statutory authority under Florida Statute 258.501.\n##### (d) Coordination with council\nThe Secretary shall coordinate the management responsibilities with the Council in the updating and implementation of the Management plan for the Myakka River, to assist the Secretary in carrying out the management responsibilities of the Secretary under this Act.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Florida",
            "updateDate": "2025-03-25T17:13:09Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-03-25T17:13:33Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2025-03-25T17:13:14Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-03-25T17:13:19Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-03-25T17:13:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-02-27T21:10:02Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr642ih.xml"
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
      "title": "Myakka Wild and Scenic River Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:56Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Myakka Wild and Scenic River Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Wild and Scenic Rivers Act to designate the portion of the Myakka River lying within Sarasota County, Florida as a component of the National Wild and Scenic Rivers System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:19:06Z"
    }
  ]
}
```
