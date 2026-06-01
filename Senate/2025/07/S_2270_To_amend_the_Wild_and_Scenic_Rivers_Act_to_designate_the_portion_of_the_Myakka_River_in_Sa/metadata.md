# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2270?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2270
- Title: Myakka Wild and Scenic River Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2270
- Origin chamber: Senate
- Introduced date: 2025-07-14
- Update date: 2026-04-23T11:03:25Z
- Update date including text: 2026-04-23T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-14: Introduced in Senate
- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- Latest action: 2025-07-14: Introduced in Senate

## Actions

- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2270",
    "number": "2270",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Myakka Wild and Scenic River Act of 2025",
    "type": "S",
    "updateDate": "2026-04-23T11:03:25Z",
    "updateDateIncludingText": "2026-04-23T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-14",
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
      "actionDate": "2025-07-14",
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
          "date": "2025-07-14T21:11:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-09T18:13:13Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-12-09T18:13:13Z",
                "name": "Hearings By (subcommittee)"
              }
            ]
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
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
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2270is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2270\nIN THE SENATE OF THE UNITED STATES\nJuly 14, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Wild and Scenic Rivers Act to designate the portion of the Myakka River in Sarasota County, Florida, as a component of the National Wild and Scenic Rivers System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Myakka Wild and Scenic River Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nsection 5(a)(70) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1276(a)(70) ) requires the study of the Myakka River for potential inclusion in the National Wild and Scenic Rivers System;\n**(2)**\nthe study referred to in paragraph (1) determined that the Myakka River was eligible for inclusion in the National Wild and Scenic Rivers System;\n**(3)**\nthe State of Florida has demonstrated the commitment of the State of Florida to protecting the Myakka River by enacting the Myakka River Wild and Scenic Designation and Protection Act (section 258.501, Florida Statutes);\n**(4)**\nSarasota County, Florida, and the cities of Venice and North Port, Florida, have demonstrated their commitment to protecting the Myakka River in comprehensive land use plans, local ordinances, and land development regulations;\n**(5)**\nthe desire for designation of the Myakka River as a component of the National Wild and Scenic Rivers System has been demonstrated through strong public support, State and local agency support, and the endorsement of designation by the Myakka River Management Coordinating Council, which represents a broad cross-section of State and local agencies, agricultural interests, landowners, and environmental and nonprofit organizations; and\n**(6)**\na 12-mile segment of the Myakka River is within the Myakka River State Park, with an additional 22-mile segment containing conservation land held in public ownership or conservation easements within the Myakka River watershed.\n#### 3. Designation of Myakka River, Florida, as a component of the National Wild and Scenic Rivers System\nSection 3(a) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(a) ) is amended by adding at the end the following:\n(233) Myakka River, Florida The following segments of the Myakka River in Sarasota County, Florida, totaling approximately 34 miles, to be administered by the Secretary of the Interior, in partnership with the Myakka River Management Coordinating Council, in the following classes: (A) The approximately 8.0-mile segment from the Manatee County/Sarasota County line to S.R. 72, as a scenic river. (B) The approximately 11.2-mile segment, from S.R. 72 to Laurel Road, as a wild river. (C) The approximately 1.9-mile segment, from Laurel Road to Border Road, as a scenic river. (D) The approximately 1.5-mile segment, from Border Road to south of the I\u201375 Bridge, as a recreational river. (E) The approximately 1.5-mile segment, from south of the I\u201375 Bridge to Snook Haven, as a scenic river. (F) The approximately 3.2-mile segment, from Snook Haven to Ramblers Rest, as a wild river. (G) The approximately 2.7-mile segment, from Ramblers Rest to U.S. 41, as a scenic river. (H) The approximately 4.0-mile segment, from U.S. 41 to the Charlotte County Line, as a scenic river. .\n#### 4. Special requirements applicable to Myakka River\n##### (a) Definitions\nIn this section:\n**(1) Comprehensive management plan**\nThe term comprehensive management plan means the Myakka River Wild and Scenic Management Plan developed by the Council, which shall be considered to satisfy the requirements for the comprehensive management plan under section 3(d) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(d) ).\n**(2) Council**\nThe term Council means the Myakka River Management Coordinating Council established pursuant to section 258.501, Florida Statutes.\n**(3) Myakka river**\nThe term Myakka River means the segments of the Myakka River in the State that are designated as components of the National Wild and Scenic Rivers System by paragraph (233) of section 3(a) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(a) ) (as added by section 3).\n**(4) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(5) State**\nThe term State means the State of Florida.\n##### (b) Cooperative agreements\n**(1) Use authorized**\nTo provide for the long-term protection, preservation, and enhancement of the Myakka River, the Secretary shall coordinate administration responsibilities under this section, and may enter into cooperative agreements pursuant to sections 10(e) and 11(b)(1) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1281(e) , 1282(b)(1)), with\u2014\n**(A)**\nthe Division of Recreation and Parks of the Department of Environmental Protection of the State;\n**(B)**\nappropriate local political jurisdictions of the State;\n**(C)**\nSarasota County, Florida;\n**(D)**\nthe city of North Port, Florida;\n**(E)**\nthe city of Venice, Florida; and\n**(F)**\nappropriate local planning and nonprofit organizations.\n**(2) Effect of agreement**\nThe administration of the Myakka River by the Secretary through the use of cooperative agreements entered into under paragraph (1) shall not\u2014\n**(A)**\nconstitute National Park Service administration of the Myakka River for purposes of section 10(c) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1281(c) ); or\n**(B)**\ncause the Myakka River to be considered a unit of the National Park System.\n**(3) Publicly or privately owned land**\nNothing in this section or a cooperative agreement entered into under paragraph (1) affects the management of publicly or privately owned land within the boundaries of the Myakka River watershed by an agency having jurisdiction over the land, in accordance with section 258.501, Florida Statutes, and the mission of the applicable agency.\n**(4) Technical assistance and other support**\nThe Secretary may provide technical assistance, staff support, and funding to assist in the updating and implementation of the comprehensive management plan.\n**(5) Acquisition of land**\n**(A) In general**\nThe authority of the Secretary to acquire land for the Myakka River shall be limited to\u2014\n**(i)**\nacquisition by donation; and\n**(ii)**\nacquisition with the consent of the owner of the land.\n**(B) No condemnation**\nNo land or interest in land may be acquired for the Myakka River by condemnation.\n##### (c) Myakka River Management Council\n**(1) In general**\nThe Secretary shall coordinate the management responsibilities of the Secretary with the Council in the updating and implementation of the comprehensive management plan.\n**(2) Representative from NPS**\nThe Secretary shall select a representative to be added to the Council to represent the National Park Service.\n**(3) Other additional members**\nNothing in this section affects the authority to add other interested representatives to the Council in accordance with section 258.501, Florida Statutes.",
      "versionDate": "2025-07-14",
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
            "name": "Florida",
            "updateDate": "2025-12-16T15:07:16Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-12-16T15:07:16Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2025-12-16T15:07:16Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-12-16T15:07:16Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-12-16T15:07:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-30T22:40:14Z"
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
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2270is.xml"
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
      "title": "Myakka Wild and Scenic River Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Myakka Wild and Scenic River Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Wild and Scenic Rivers Act to designate the portion of the Myakka River in Sarasota County, Florida, as a component of the National Wild and Scenic Rivers System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T02:18:20Z"
    }
  ]
}
```
