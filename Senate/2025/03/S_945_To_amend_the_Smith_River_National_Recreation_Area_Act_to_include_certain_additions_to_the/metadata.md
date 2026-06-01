# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/945?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/945
- Title: Smith River National Recreation Area Expansion Act
- Congress: 119
- Bill type: S
- Bill number: 945
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/945",
    "number": "945",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Smith River National Recreation Area Expansion Act",
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
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T20:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:16Z",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s945is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 945\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Merkley (for himself, Mr. Wyden , Mr. Padilla , and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Smith River National Recreation Area Act to include certain additions to the Smith River National Recreation Area, to amend the Wild and Scenic Rivers Act to designate certain wild rivers in the State of Oregon, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Smith River National Recreation Area Expansion Act .\n#### 2. Additions to the Smith River National Recreation Area\n##### (a) Definitions\nSection 3 of the Smith River National Recreation Area Act ( 16 U.S.C. 460bbb\u20131 ) is amended\u2014\n**(1)**\nin paragraph (1), by striking referred to in section 4(b) and inserting entitled Proposed Smith River National Recreation Area and dated July 1990 ; and\n**(2)**\nin paragraph (2), by striking the Six Rivers National Forest and inserting an applicable unit of the National Forest System .\n##### (b) Boundaries\nSection 4(b) of the Smith River National Recreation Area Act ( 16 U.S.C. 460bbb\u20132(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the first sentence, by inserting and on the map entitled Proposed Additions to the Smith River National Recreation Area and dated January 23, 2023 after 1990 ; and\n**(B)**\nin the second sentence, by striking map and inserting maps ; and\n**(2)**\nin paragraph (2), by striking map and inserting maps described in paragraph (1) .\n##### (c) Administration\nSection 5 of the Smith River National Recreation Area Act ( 16 U.S.C. 460bbb\u20133 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), in the first sentence, by striking the map and inserting the maps ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking area shall be on and inserting area and any portion of the recreation area in the State of Oregon shall be on roadless ; and\n**(ii)**\nby adding at the end the following:\n(I) The Kalmiopsis Wilderness shall be managed in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ). ;\n**(2)**\nin subsection (c), by striking by the amendments made by section 10(b) of this Act and inserting within the recreation area ; and\n**(3)**\nby adding at the end the following:\n(d) Study; report (1) In general Not later than 5 years after the date of enactment of this subsection, the Secretary shall conduct a study of the area depicted on the map entitled Proposed Additions to the Smith River National Recreation Area and dated January 23, 2023, that includes inventories and assessments of streams, fens, wetlands, lakes, other water features, and associated land, plants (including Port-Orford-cedar), animals, fungi, algae, and other values, and unstable and potentially unstable aquatic habitat areas in the study area. (2) Modification of management plans; report On completion of the study under paragraph (1), the Secretary shall\u2014 (A) modify any applicable management plan to fully protect the inventoried values under the study, including to implement additional standards and guidelines; and (B) submit to Congress a report describing the results of the study. (e) Wildfire management Nothing in this Act affects the authority of the Secretary (in cooperation with other Federal, State, and local agencies, as appropriate) to conduct wildland fire operations within the recreation area, consistent with the purposes of this Act. (f) Vegetation management Nothing in this Act prohibits the Secretary from conducting vegetation management projects (including wildfire resiliency and forest health projects) within the recreation area, to the extent consistent with the purposes of the recreation area. (g) Application of Northwest Forest Plan and roadless rule to certain portions of the recreation area Nothing in this Act affects the application of the Northwest Forest Plan or part 294 of title 36, Code of Federal Regulations (commonly referred to as the Roadless Rule ) (as in effect on the date of enactment of this subsection), to portions of the recreation area in the State of Oregon that are subject to the plan and those regulations as of the date of enactment of this subsection. (h) Protection of tribal rights (1) In general Nothing in this Act diminishes any right of an Indian Tribe. (2) Memorandum of understanding The Secretary shall seek to enter into a memorandum of understanding with applicable Indian Tribes with respect to\u2014 (A) providing the Indian Tribes with access to the portions of the recreation area in the State of Oregon to conduct historical and cultural activities, including the procurement of noncommercial forest products and materials for traditional and cultural purposes; and (B) the development of interpretive information to be provided to the public on the history of the Indian Tribes and the use of the recreation area by the Indian Tribes. .\n##### (d) Acquisition\nSection 6(a) of the Smith River National Recreation Area Act ( 16 U.S.C. 460bbb\u20134(a) ) is amended\u2014\n**(1)**\nin the fourth sentence, by striking All lands and inserting the following:\n(4) Applicable law All land ;\n**(2)**\nin the third sentence\u2014\n**(A)**\nby striking The Secretary and inserting the following:\n(3) Method of acquisition The Secretary ;\n**(B)**\nby striking or any of its political subdivisions and inserting , the State of Oregon, or any political subdivision of the State of California or the State of Oregon ; and\n**(C)**\nby striking donation or and inserting purchase, donation, or ;\n**(3)**\nin the second sentence, by striking In exercising and inserting the following:\n(2) Consideration of offers by Secretary In exercising ;\n**(4)**\nin the first sentence, by striking The Secretary and inserting the following:\n(1) In general The Secretary ; and\n**(5)**\nby adding at the end the following:\n(5) Acquisition of cedar creek parcel On the adoption of a resolution by the State Land Board of Oregon and subject to available funding, the Secretary shall acquire all right, title, and interest in and to the approximately 555 acres of land known as the Cedar Creek Parcel located in sec. 16, T. 41 S., R. 11 W., Willamette Meridian. .\n##### (e) Fish and game\nSection 7 of the Smith River National Recreation Area Act ( 16 U.S.C. 460bbb\u20135 ) is amended\u2014\n**(1)**\nin the first sentence, by inserting or the State of Oregon after State of California ; and\n**(2)**\nin the second sentence, by inserting or the State of Oregon, as applicable after State of California .\n##### (f) Management planning\nSection 9 of the Smith River National Recreation Area Act ( 16 U.S.C. 460bbb\u20137 ) is amended\u2014\n**(1)**\nin the first sentence, by striking The Secretary and inserting the following:\n(a) Revision of management plan The Secretary ; and\n**(2)**\nby adding at the end the following:\n(b) Smith River National Recreation Area Management Plan revision As soon as practicable after the date of the first revision of the forest plan after the date of enactment of this subsection, the Secretary shall revise the management plan for the recreation area\u2014 (1) to reflect the expansion of the recreation area into the State of Oregon under the Smith River National Recreation Area Expansion Act ; and (2) to include an updated recreation action schedule to identify specific use and development plans for the areas described in the map entitled Proposed Additions to the Smith River National Recreation Area and dated January 23, 2023. .\n##### (g) Streamside protection zones\nSection 11(b) of the Smith River National Recreation Area Act ( 16 U.S.C. 460bbb\u20138(b) ) is amended by adding at the end the following:\n(24) Each of the river segments described in subparagraph (B) of section 3(a)(92) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(a)(92) ). .\n##### (h) State and local jurisdiction and assistance\nSection 12 of the Smith River National Recreation Area Act ( 16 U.S.C. 460bbb\u20139 ) is amended\u2014\n**(1)**\nin subsection (a), by striking California or any political subdivision thereof and inserting California, the State of Oregon, or a political subdivision of the State of California or the State of Oregon ;\n**(2)**\nin subsection (b), in the matter preceding paragraph (1), by striking California or its political subdivisions and inserting California, the State of Oregon, or a political subdivision of the State of California or the State of Oregon ; and\n**(3)**\nin subsection (c), in the first sentence\u2014\n**(A)**\nby striking California and its political subdivisions and inserting California, the State of Oregon, and any political subdivision of the State of California or the State of Oregon ; and\n**(B)**\nby striking State and its political subdivisions and inserting State of California, the State of Oregon, and any political subdivision of the State of California or the State of Oregon .\n#### 3. Wild and scenic river designations\n##### (a) North Fork Smith additions, Oregon\n**(1) Finding**\nCongress finds that the source tributaries of the North Fork Smith River in the State of Oregon possess outstandingly remarkable wild anadromous fish and prehistoric, cultural, botanical, recreational, and water quality values.\n**(2) Designation**\nSection 3(a)(92) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(a)(92) ) is amended\u2014\n**(A)**\nin subparagraph (B), by striking scenic and inserting wild ;\n**(B)**\nby redesignating subparagraphs (A) through (C) as clauses (i) through (iii), respectively, and indenting appropriately;\n**(C)**\nin the matter preceding clause (i) (as so redesignated), by striking The 13-mile and inserting the following:\n(A) In general The 13-mile ; and\n**(D)**\nby adding at the end the following:\n(B) Additions The following segments of the source tributaries of the North Fork Smith River, to be administered by the Secretary of Agriculture in the following classes: (i) The 13.26-mile segment of Baldface Creek from its headwaters, including all perennial tributaries, to the confluence with the North Fork Smith in T. 39 S., R 10 W., T. 40 S., R. 10 W., and T. 41 S., R. 11 W., Willamette Meridian, as a wild river. (ii) The 3.58-mile segment from the headwaters of Taylor Creek to the confluence with Baldface Creek, as a wild river. (iii) The 4.38-mile segment from the headwaters of the unnamed tributary to Biscuit Creek and the headwaters of Biscuit Creek to the confluence with Baldface Creek, as a wild river. (iv) The 2.27-mile segment from the headwaters of Spokane Creek to the confluence with Baldface Creek, as a wild river. (v) The 1.25-mile segment from the headwaters of Rock Creek to the confluence with Baldface Creek, flowing south from sec. 19, T. 40 S., R. 10 W., Willamette Meridian, as a wild river. (vi) The 1.31-mile segment from the headwaters of the unnamed tributary number 2 to the confluence with Baldface Creek, flowing north from sec. 27, T. 40 S., R. 10 W., Willamette Meridian, as a wild river. (vii) The 3.6-mile segment from the 2 headwaters of the unnamed tributary number 3 to the confluence with Baldface Creek, flowing south from secs. 9 and 10, T. 40 S., R. 10 W., Willamette Meridian, as a wild river. (viii) The 1.57-mile segment from the headwaters of the unnamed tributary number 4 to the confluence with Baldface Creek, flowing north from sec. 26, T. 40 S., R. 10 W., Willamette Meridian, as a wild river. (ix) The 0.92-mile segment from the headwaters of the unnamed tributary number 5 to the confluence with Baldface Creek, flowing north from sec. 13, T. 40 S., R. 10 W., Willamette Meridian, as a wild river. (x) The 4.90-mile segment from the headwaters of Cedar Creek to the confluence with North Fork Smith River, as a wild river. (xi) The 2.38-mile segment from the headwaters of Packsaddle Gulch to the confluence with North Fork Smith River, as a wild river. (xii) The 2.4-mile segment from the headwaters of Hardtack Creek to the confluence with North Fork Smith River, as a wild river. (xiii) The 2.21-mile segment from the headwaters of the unnamed creek to the confluence with North Fork Smith River, flowing east from sec. 29, T. 40 S., R. 11 W., Willamette Meridian, as a wild river. (xiv) The 3.06-mile segment from the headwaters of Horse Creek to the confluence with North Fork Smith River, as a wild river. (xv) The 2.61-mile segment of Fall Creek from the Oregon State border to the confluence with North Fork Smith River, as a wild river. (xvi) (I) Except as provided in subclause (II), the 4.57-mile segment from the headwaters of North Fork Diamond Creek to the confluence with Diamond Creek, as a wild river. (II) Notwithstanding subclause (I), the portion of the segment described in that subclause that starts 100 feet above Forest Service Road 4402 and ends 100 feet below Forest Service Road 4402 shall be administered as a scenic river. (xvii) The 1.02-mile segment from the headwaters of Diamond Creek to the Oregon State border in sec. 14, T. 40 S., R. 10 W., Willamette Meridian, as a wild river. (xviii) The 1.14-mile segment from the headwaters of Acorn Creek to the confluence with Horse Creek, as a wild river. (xix) The 8.58-mile segment from the headwaters of Chrome Creek to the confluence with North Fork Smith River, as a wild river. (xx) The 2.98-mile segment from the headwaters Chrome Creek tributary number 1 to the confluence with Chrome Creek, 0.82 miles upstream from the mouth of Chrome Creek in the Kalmiopsis Wilderness, flowing south from sec. 15, T. 40 S., R. 11 W., Willamette Meridian, as a wild river. (xxi) The 2.19-mile segment from the headwaters of Chrome Creek tributary number 2 to the confluence with Chrome Creek, 3.33 miles upstream from the mouth of Chrome Creek in the Kalmiopsis Wilderness, flowing south from sec. 12, T. 40 S., R. 11 W., Willamette Meridian, as a wild river. (xxii) The 1.27-mile segment from the headwaters of Chrome Creek tributary number 3 to the confluence with Chrome Creek, 4.28 miles upstream from the mouth of Chrome Creek in the Kalmiopsis Wilderness, flowing north from sec. 18, T. 40 S., R. 10 W., Willamette Meridian, as a wild river. (xxiii) The 2.27-mile segment from the headwaters of Chrome Creek tributary number 4 to the confluence with Chrome Creek, 6.13 miles upstream from the mouth of Chrome Creek, flowing south from Chetco Peak in the Kalmiopsis Wilderness in sec. 36, T. 39 S., R. 11 W., Willamette Meridian, as a wild river. (xxiv) The 0.6-mile segment from the headwaters of Wimer Creek to the border between the States of Oregon and California, flowing south from sec. 17, T. 41 S., R. 10 W., Willamette Meridian, as a wild river. .\n##### (b) Expansion of smith river, oregon\nSection 3(a) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(a) ) is amended by striking paragraph (111) and inserting the following:\n(111) Smith river, california and oregon The segment from the confluence of the Middle Fork Smith River and the North Fork Smith River to the Six Rivers National Forest boundary, including the following segments of the mainstem and certain tributaries, to be administered by the Secretary of Agriculture in the following classes: (A) Mainstem The segment from the confluence of the Middle Fork Smith River and the South Fork Smith River to the Six Rivers National Forest boundary, as a recreational river. (B) Rowdy Creek (i) Upper The segment from and including the headwaters to the California-Oregon State line, as a wild river. (ii) Lower The segment from the California-Oregon State line to the Six Rivers National Forest boundary, as a recreational river. .",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-08-26",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "5041",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Smith River National Recreation Area Expansion Act",
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
            "name": "California",
            "updateDate": "2025-12-04T17:04:13Z"
          },
          {
            "name": "Federal-Indian relations",
            "updateDate": "2025-12-04T17:04:13Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-12-04T17:04:13Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-12-04T17:04:13Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2025-12-04T17:04:13Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-12-04T17:04:13Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-12-04T17:04:13Z"
          },
          {
            "name": "Oregon",
            "updateDate": "2025-12-04T17:04:13Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-12-04T17:04:13Z"
          },
          {
            "name": "Wetlands",
            "updateDate": "2025-12-04T17:04:13Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-12-04T17:04:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-20T14:20:42Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s945is.xml"
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
      "title": "Smith River National Recreation Area Expansion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Smith River National Recreation Area Expansion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Smith River National Recreation Area Act to include certain additions to the Smith River National Recreation Area, to amend the Wild and Scenic Rivers Act to designate certain wild rivers in the State of Oregon, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T02:48:33Z"
    }
  ]
}
```
