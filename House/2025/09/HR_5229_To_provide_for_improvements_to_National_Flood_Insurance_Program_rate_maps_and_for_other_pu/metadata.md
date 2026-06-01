# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5229?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5229
- Title: IMAGES Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5229
- Origin chamber: House
- Introduced date: 2025-09-09
- Update date: 2025-09-23T18:51:13Z
- Update date including text: 2025-09-23T18:51:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-09-09: Introduced in House

## Actions

- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5229",
    "number": "5229",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000634",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Downing, Troy [R-MT-2]",
        "lastName": "Downing",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "IMAGES Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-23T18:51:13Z",
    "updateDateIncludingText": "2025-09-23T18:51:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-09",
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
          "date": "2025-09-09T14:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5229ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5229\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 9, 2025 Mr. Downing (for himself and Mr. Vicente Gonzalez of Texas ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo provide for improvements to National Flood Insurance Program rate maps, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improvement of Mapping, Addresses, Geography, Elevations, and Structures Act of 2025 or the IMAGES Act of 2025 .\n#### 2. National Flood Mapping Program\n##### (a) Inclusion of planimetric features in rate maps\nSection 100216(b)(3) of the Biggert-Waters Flood Insurance Reform Act of 2012 ( 42 U.S.C. 4101b(b)(3) ) is amended\u2014\n**(1)**\nin subparagraph (D), by striking and at the end;\n**(2)**\nin subparagraph (E), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(F) planimetric features, including, for each planimetric feature\u2014 (i) the associated parcel identification data for such planimetric feature; and (ii) to the maximum extent practicable, using public and private sector address data, the address of such planimetric feature. .\n##### (b) Format of rate maps\nSection 100216(c)(2) of the Biggert-Waters Flood Insurance Reform Act of 2012 ( 42 U.S.C. 4101b(c)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking and at the end;\n**(2)**\nin subparagraph (C), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(D) not later than 5 years after the date that the National Geodetic Survey completes the National Spatial Reference System 2022, updated to conform with the geospatial data provided by such system; and (E) spatially accurate in accordance with the common protocols for geographic information systems under section 216 of the E-Government Act of 2002 ( 44 U.S.C. 3501 note). .\n##### (c) Additional considerations\nSection 100216 of the Biggert-Waters Flood Insurance Reform Act of 2012 ( 42 U.S.C. 4101b ) is amended\u2014\n**(1)**\nby redesignating subsection (f) as subsection (k); and\n**(2)**\nby inserting after subsection (e) the following:\n(f) Stream flow networks (1) In general The Administrator shall coordinate with the United States Geological Survey to ensure that, to the extent necessary to maintain the stream flow networks critical to the National Flood Insurance Program, flood risk mapping, and flood risk assessments\u2014 (A) the stream gage stations in such stream flow networks are operational and use modern hardware; (B) such stream flow networks are sufficiently densified by adding new stream gage stations in high-risk areas; (C) inactive critical stream gage stations in such stream flow networks are reactivated; and (D) the speed of the geospatial real-time data feeds from such stream gage stations is increased. (2) Definitions In this subsection: (A) Stream flow network The term stream flow network means a network of stream flow gages maintained under the direction of the United States Geological Survey and its partners that is used to measure or record the flow of water down a stream or river, or through an entire watershed system, and transmit such information using a geospatial real-time data feed. (B) Stream gage station The term stream gage station means a device installed at the edge of a river or stream that measures or records the flow of water down the stream and additional information such as water height, water chemistry, and water temperature. (g) Availability of data to public The Administrator shall make available to the public on the website of the Federal Emergency Management Agency a national geospatial data repository that\u2014 (1) provides access to the raw data used to include the planimetric features and parcel identification data in National Flood Insurance Program rate maps; (2) to the extent that such data is available, allows users to view, query, and obtain such data at multiple levels of detail, including down to the property level; (3) allows users to view flood risks, flood insurance zones, and flood elevations; (4) provides access to flood mapping and related information such as\u2014 (A) hydrologic and hydraulic models used in determining flood risk; (B) structure footprints where available; (C) flood depth grids; (D) flood risk reports; (E) flood risk assessments (Hazus ana\u00adlyses); (F) hazard mitigation plans; and (G) other flood risk products at the discretion of the Administrator; and (5) maintains and disseminates such data in a consistent manner. (h) Ensuring current data Not less frequently than once every 5 years, the Administrator shall verify that each National Flood Insurance Program rate map contains data that is current and credible. (i) Qualifications-Based Selection Contracting (1) In general With respect to a contract awarded by the Administrator under this Act, or by an entity receiving a grant under this Act, for program management, architectural and engineering services, or surveying and mapping, such a contract shall be awarded to a contractor selected in accordance with the procedures described in section 1103 of title 40, United States Code (or an applicable equivalent State qualifications-based statute). The Administrator, or entity, as the case may be, shall require such contractor, as a condition of such contract, to award any subcontract for program management, architectural and engineering services, or surveying and mapping in accordance with the procedures described in the previous sentence, or the applicable equivalent State statute. (2) Relationship to State law Nothing in this subsection shall supersede any applicable State licensing law governing professional licensure. (3) Definitions In this subsection: (A) Architectural and engineering services The term architectural and engineering services has the meaning given that term in section 1102 of title 40, United States Code. (B) Surveying and mapping The term surveying and mapping includes geo\u00adspa\u00adtial activities associated with measuring, locating, and preparing maps, charts, or other graphical or digital presentations depicting natural and man-made physical features, phenomena, and legal boundaries of the earth, including the following: (i) Topographic Engineering Surveying, including acquisition of topographic oriented surveying and mapping data for design, construction, master planning, operations, as-built conditions, precise structure stability studies using conventional and electronic instrumentation, photogrammetric, LiDAR, remote sensing, inertial, satellite, and other manned and unmanned survey methods as applicable. (ii) Hydrographic Engineering Surveying, including acquisition of hydrographic oriented surveying and mapping data for design, construction, dredging, master planning, operations, and as-built conditions using conventional and electronic instrumentation, and pho\u00adto\u00adgram\u00adme\u00adtric, remote sensing, inertial, satellite, side scan sonar, subbottom profiling, and other surveying methods, as applicable. (iii) Land Surveying, including property and boundary surveys, mon\u00adu\u00admen\u00adta\u00adtion, marking and posting, and preparation of tract descriptions, using conventional, electronic instrumentation, pho\u00adto\u00adgram\u00adme\u00adtric, inertial, satellite, and other survey methods, as applicable. (iv) Geodetic Surveying, including first-, second-, and third-order horizontal and vertical control surveys, geodetic astronomy, gravity and magnetic surveys using conventional, electronic instrumentation, photogrammetric, inertial, satellite, and other survey methods, as applicable. (v) Cartographic Surveying, including acquisition of topographic and hydrographic oriented surveying and mapping data for construction of maps, charts, and similar products for planning, flood analysis, and general use purposes using conventional and electronic instrumentation, photogrammetric, inertial, satellite, mobile, terrestrial, and other survey methods, as applicable. (vi) Mapping, charting, and related geospatial database development, including the design, compilation, digitizing, attributing, scribing, drafting, printing and dissemination of printed or digital map, chart, and related geospatial database products associated with planning, engineering, operations, and related real estate activities using photogrammetric, geographic information systems, and other manual and computer assisted methods, as applicable. (j) Definitions In this section: (1) Planimetric feature The term planimetric feature means the geographic elements and features\u2014 (A) that are independent of elevation, such as roads, structure footprints, and rivers and lakes; (B) which are represented on maps to show the true location and size of the elements in relationship to each other, as they are seen from the air; and (C) that are mapped from LiDAR or aerial photography by employing basic photogrammetry. (2) Parcel identification data The term parcel identification data means the information associated with a parcel of land, including the geographic location, unique parcel identifier, boundaries, structures contained within the parcel, zoning classification, and owner. .\n##### (d) Funding for elevation data\nSection 1310 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4017 ) is amended by adding at the end the following:\n(g) Allocation from the National Flood Insurance Fund Each fiscal quarter the Administrator shall allocate from the National Flood Insurance Fund an amount equal to 5 percent of any revenue collected under section 1308(b)(3) for use for creating or maintaining current and accurate National Flood Insurance Program Rate Maps. .",
      "versionDate": "2025-09-09",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-23T18:51:13Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5229ih.xml"
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
      "title": "IMAGES Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-13T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "IMAGES Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-13T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improvement of Mapping, Addresses, Geography, Elevations, and Structures Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-13T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for improvements to National Flood Insurance Program rate maps, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-13T03:48:22Z"
    }
  ]
}
```
