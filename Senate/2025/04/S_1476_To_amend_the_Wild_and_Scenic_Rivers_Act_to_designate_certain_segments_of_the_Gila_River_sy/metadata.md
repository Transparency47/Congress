# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1476?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1476
- Title: M.H. Dutch Salmon Greater Gila Wild and Scenic River Act
- Congress: 119
- Bill type: S
- Bill number: 1476
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
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1476",
    "number": "1476",
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
    "title": "M.H. Dutch Salmon Greater Gila Wild and Scenic River Act",
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
          "date": "2025-04-10T20:38:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:36Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1476is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1476\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Heinrich (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Wild and Scenic Rivers Act to designate certain segments of the Gila River system in the State of New Mexico as components of the National Wild and Scenic Rivers System, to provide for the transfer of administrative jurisdiction over certain Federal land in the State of New Mexico, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the M.H. Dutch Salmon Greater Gila Wild and Scenic River Act .\n#### 2. Designation of wild and scenic rivers\n##### (a) Definitions\nIn this section:\n**(1) Covered segment**\nThe term covered segment means a river segment designated by paragraph (233) of section 3(a) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(a) ) (as added by subsection (b)).\n**(2) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of the Interior, with respect to a covered segment under the jurisdiction of the Secretary of the Interior; and\n**(B)**\nthe Secretary of Agriculture, with respect to a covered segment under the jurisdiction of the Secretary of Agriculture.\n**(3) State**\nThe term State means the State of New Mexico.\n##### (b) Designation of segments\nSection 3(a) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(a) ) is amended by adding at the end the following:\n(233) Gila River System, New Mexico The following segments of the Gila River system in Las Animas Creek, Holden Prong, and McKnight Canyon in the State of New Mexico, to be administered by the Secretary concerned (as defined in section 2(a) of the M.H. Dutch Salmon Greater Gila Wild and Scenic River Act ) in the following classifications: (A) Apache creek The approximately 10.5-mile segment, as generally depicted on the map entitled Apache Creek and dated April 30, 2020, as a wild river. (B) Black canyon creek (i) The 11.8-mile segment, as generally depicted on the map entitled Black Canyon Creek and dated April 30, 2020, as a wild river. (ii) The 0.6-mile segment, as generally depicted on the map entitled Black Canyon Creek and dated April 30, 2020, as a recreational river. (iii) The 1.9-mile segment, as generally depicted on the map entitled Black Canyon Creek and dated April 30, 2020, as a recreational river. (iv) The 11-mile segment, as generally depicted on the map entitled Black Canyon Creek and dated April 30, 2020, as a wild river. (C) Diamond creek (i) The approximately 13.3-mile segment, as generally depicted on the map entitled Diamond Creek and dated March 27, 2020, as a wild river. (ii) The approximately 4.7-mile segment, as generally depicted on the map entitled Diamond Creek and dated March 27, 2020, as a wild river. (iii) The approximately 3.1-mile segment, as generally depicted on the map entitled Diamond Creek and dated March 27, 2020, as a recreational river. (iv) The approximately 1.6-mile segment, as generally depicted on the map entitled \u2018Diamond Creek\u2019 and dated March 27, 2020, as a recreational river. (v) The approximately 4.1-mile segment, as generally depicted on the map entitled \u2018Diamond Creek\u2019 and dated March 27, 2020, as a wild river. (D) South diamond creek The approximately 16.1-mile segment, as generally depicted on the map entitled \u2018South Diamond Creek\u2019 and dated March 27, 2020, as a wild river. (E) Gila river (i) The approximately 34.9-mile segment, as generally depicted on the map entitled Gila River and dated April 30, 2020, as a wild river. (ii) The approximately 2.5-mile segment, as generally depicted on the map entitled \u2018Gila River\u2019 and dated April 30, 2020, as a recreational river. (iii) The approximately 3-mile segment, as generally depicted on the map entitled Gila River and dated April 30, 2020, as a wild river. (F) Gila river, east fork The approximately 10.3-mile segment, as generally depicted on the map entitled East Fork Gila River and dated April 30, 2020, as a wild river. (G) Gila river, lower box (i) The approximately 3.1-mile segment, as generally depicted on the map entitled Gila River, Lower Box and dated April 21, 2020, as a recreational river. (ii) The approximately 6.1-mile segment, as generally depicted on the map entitled Gila River, Lower Box and dated April 21, 2020, as a wild river. (H) Gila river, middle box (i) The approximately 0.6-mile segment, as generally depicted on the map entitled Gila River, Middle Box and dated April 30, 2020, as a recreational river. (ii) The approximately 0.4-mile segment, as generally depicted on the map entitled Gila River, Middle Box \u2019 and dated April 30, 2020, as a recreational river. (iii) The approximately 0.3-mile segment, as generally depicted on the map entitled Gila River, Middle Box and dated April 30, 2020, as a recreational river. (iv) The approximately 0.3-mile segment, as generally depicted on the map entitled Gila River, Middle Box and dated April 30, 2020, as a recreational river. (v) The approximately 1.6-mile segment, as generally depicted on the map entitled Gila River, Middle Box and dated April 30, 2020, as a recreational river. (vi) The approximately 9.8-mile segment, as generally depicted on the map entitled Gila River, Middle Box and dated April 30, 2020, as a wild river. (I) Gila river, middle fork (i) The approximately 1.2-mile segment, as generally depicted on the map entitled Middle Fork Gila River and dated May 1, 2020, as a recreational river. (ii) The approximately 35.5-mile segment, as generally depicted on the map entitled Middle Fork Gila River and dated May 1, 2020, as a wild river. (J) Gila river, west fork (i) The approximately 30.6-mile segment, as generally depicted on the map entitled West Fork Gila River and dated May 1, 2020, as a wild river. (ii) The approximately 4-mile segment, as generally depicted on the map entitled West Fork Gila River and dated May 1, 2020, as a recreational river. (K) Gilita creek The approximately 6.4-mile segment, as generally depicted on the map entitled Gilita Creek and dated March 4, 2020, as a wild river. (L) Holden prong The approximately 7.3-mile segment, as generally depicted on the map entitled Holden Prong and dated March 27, 2020, as a wild river. (M) Indian creek (i) The approximately 5-mile segment, as generally depicted on the map entitled Indian Creek and dated March 27, 2020, as a recreational river. (ii) The approximately 9.5-mile segment, as generally depicted on the map entitled Indian Creek and dated March 27, 2020, as a wild river. (N) Iron creek The approximately 13.2-mile segment, as generally depicted on the map entitled Iron Creek and dated March 4, 2020, as a wild river. (O) Las animas creek (i) The approximately 5.3-mile segment, as generally depicted on the map entitled Las Animas Creek and dated March 27, 2020, as a wild river. (ii) The approximately 2.3-mile segment, as generally depicted on the map entitled Las Animas Creek and dated March 27, 2020, as a scenic river. (P) Little creek (i) The approximately 0.3-mile segment, as generally depicted on the map entitled Little Creek and dated May 1, 2020, as a recreational river. (ii) The approximately 18.3-mile segment, as generally depicted on the map entitled Little Creek and dated May 1, 2020, as a wild river. (Q) Mcknight canyon The approximately 10.3-mile segment, as generally depicted on the map entitled McKnight Canyon and dated March 4, 2020, as a wild river. (R) Mineral creek (i) The approximately 8.3-mile segment, as generally depicted on the map entitled Mineral Creek and dated March 27, 2020, as a wild river. (ii) The approximately 0.5-mile segment, as generally depicted on the map entitled Mineral Creek and dated March 27, 2020, as a recreational river. (iii) The approximately 0.5-mile segment, as generally depicted on the map entitled Mineral Creek and dated March 27, 2020, as a recreational river. (iv) The approximately 0.1-mile segment, as generally depicted on the map entitled Mineral Creek and dated March 27, 2020, as a recreational river. (v) The approximately 0.03-mile segment, as generally depicted on the map entitled Mineral Creek and dated March 27, 2020, as a recreational river. (vi) The approximately 0.02-mile segment, as generally depicted on the map entitled Mineral Creek and dated March 27, 2020, as a recreational river. (vii) The approximately 0.6-mile segment, as generally depicted on the map entitled Mineral Creek and dated March 27, 2020, as a recreational river. (viii) The approximately 0.1-mile segment, as generally depicted on the map entitled Mineral Creek and dated March 27, 2020, as a recreational river. (ix) The approximately 0.03-mile segment, as generally depicted on the map entitled Mineral Creek and dated March 27, 2020, as a recreational river. (x) The approximately 0.7-mile segment, as generally depicted on the map entitled Mineral Creek and dated March 27, 2020, as a recreational river. (S) Mogollon creek The approximately 15.8-mile segment, as generally depicted on the map entitled Mogollon Creek and dated April 2, 2020, as a wild river. (T) West fork mogollon creek The approximately 8.5-mile segment, as generally depicted on the map entitled West Fork Mogollon Creek and dated March 4, 2020, as a wild river. (U) Mule creek The approximately 4.3-mile segment, as generally depicted on the map entitled Mule Creek and dated March 4, 2020, as a wild river. (V) San francisco river, devil\u2019s creek (i) The approximately 1.8-mile segment, as generally depicted on the map entitled San Francisco River, Devil's Creek and dated October 29, 2021, as a scenic river. (ii) The approximately 6.4-mile segment, as generally depicted on the map entitled San Francisco River, Devil's Creek and dated October 29, 2021, as a scenic river. (iii) The approximately 6.1-mile segment, as generally depicted on the map entitled San Francisco River, Devil's Creek and dated October 29, 2021, as a scenic river. (iv) The approximately 1.2-mile segment, as generally depicted on the map entitled San Francisco River, Devil\u2019s Creek and dated October 29, 2021, as a recreational river. (v) The approximately 5.9-mile segment, as generally depicted on the map entitled San Francisco River, Devil\u2019s Creek and dated October 29, 2021, as a recreational river. (W) San francisco river, lower san francisco river canyon (i) The approximately 1.8-mile segment, as generally depicted on the map entitled San Francisco River, Lower San Francisco River Canyon and dated March 27, 2020, as a wild river. (ii) The approximately 0.6-mile segment, as generally depicted on the map entitled San Francisco River, Lower San Francisco River Canyon and dated March 27, 2020, as a recreational river. (iii) The approximately 14.6-mile segment, as generally depicted on the map entitled San Francisco River, Lower San Francisco River Canyon and dated March 27, 2020, as a wild river. (X) San francisco river, upper frisco box The approximately 6-mile segment, as generally depicted on the map entitled San Francisco River, Upper Frisco Box and dated March 4, 2020, as a wild river. (Y) Sapillo creek The approximately 7.2-mile segment, as generally depicted on the map entitled Sapillo Creek and dated March 27, 2020, as a wild river. (Z) Spruce creek The approximately 3.7-mile segment, as generally depicted on the map entitled Spruce Creek and dated March 4, 2020, as a wild river. (AA) Taylor creek (i) The approximately 0.4-mile segment, as generally depicted on the map entitled Taylor Creek and dated April 30, 2020, as a scenic river. (ii) The approximately 6.1-mile segment, as generally depicted on the map entitled Taylor Creek and dated April 30, 2020, as a wild river. (iii) The approximately 6.7-mile segment, as generally depicted on the map entitled Taylor Creek and dated April 30, 2020, as a wild river. (BB) Turkey creek The approximately 17.1-mile segment, as generally depicted on the map entitled Turkey Creek and dated April 30, 2020, as a wild river. (CC) Whitewater creek (i) The approximately 13.5-mile segment, as generally depicted on the map entitled Whitewater Creek and dated March 27, 2020, as a wild river. (ii) The approximately 1.1-mile segment, as generally depicted on the map entitled Whitewater Creek and dated March 27, 2020, as a recreational river. (DD) Willow creek (i) The approximately 3-mile segment, as generally depicted on the map entitled Willow Creek and dated April 30, 2020, as a recreational river. (ii) The approximately 2.9-mile segment, as generally depicted on the map entitled Willow Creek and dated April 30, 2020, as a recreational river. .\n##### (c) Withdrawal\nSubject to valid existing rights, all Federal land within the boundary of a covered segment is withdrawn from all forms of\u2014\n**(1)**\nentry, appropriation, or disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\ndisposition under all laws pertaining to mineral and geothermal leasing or mineral materials.\n##### (d) Maps; legal descriptions\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary concerned shall prepare maps and legal descriptions of the covered segments.\n**(2) Force of law**\nThe maps and legal descriptions prepared under paragraph (1) shall have the same force and effect as if included in this section, except that the Secretary concerned may correct minor errors in the maps and legal descriptions.\n**(3) Availability**\nThe map and legal description prepared under paragraph (1) shall be on file and available for public inspection in the appropriate offices of the Forest Service, the Bureau of Land Management, and the National Park Service.\n##### (e) Comprehensive river management plan\nThe Secretary concerned shall prepare the comprehensive management plan for the covered segments pursuant to section 3(d) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(d) ) after consulting with Tribal governments, applicable political subdivisions of the State, and interested members of the public.\n##### (f) Incorporation of acquired land and interests in land\nIf the United States acquires any non-Federal land within or adjacent to a covered segment, the acquired land shall be incorporated in, and be administered as part of, the applicable covered segment.\n##### (g) Effect of section\n**(1) Effect on rights**\nIn accordance with section 12(b) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1283(b) ), nothing in this section or an amendment made by this section abrogates any existing rights of, privilege of, or contract held by any person, including any right, privilege, or contract that affects Federal land or private land, without the consent of the person, including\u2014\n**(A)**\ngrazing permits or leases;\n**(B)**\nexisting water rights, including the jurisdiction of the State in administering water rights;\n**(C)**\nexisting points of diversion, including maintenance, repair, or replacement;\n**(D)**\nexisting water distribution infrastructure, including maintenance, repair, or replacement; and\n**(E)**\nvalid existing rights for mining and mineral leases.\n**(2) Mining activities**\nThe designation of a covered segment by subparagraph (G) or (H) of paragraph (233) of section 3(a) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1274(a) ) (as added by subsection (b)) shall not\u2014\n**(A)**\nlimit the licensing, development, operation, or maintenance of mining activities or mineral processing facilities outside the boundaries of the applicable covered segment; or\n**(B)**\naffect any rights, obligations, privileges, or benefits granted under any permit or approval with respect to such mining activities or mineral processing facilities.\n**(3) Condemnation**\nNo land or interest in land shall be acquired under this section or an amendment made by this section without the consent of the owner.\n**(4) Relationship to other law**\nNothing in this section amends or otherwise affects the Arizona Water Settlements Act ( Public Law 108\u2013451 ; 118 Stat. 3478).\n**(5) Native fish habitat restoration**\n**(A) Existing projects**\nNothing in this section or an amendment made by this section affects the authority of the Secretary concerned or the State to operate, maintain, replace, or improve a native fish habitat restoration project (including fish barriers) in existence as of the date of enactment of this Act within a covered segment.\n**(B) New projects**\nNotwithstanding section 7 of the Wild and Scenic Rivers Act ( 16 U.S.C. 1278 ), the Secretary concerned may authorize the construction of a native fish habitat restoration project (including any necessary fish barriers) within a covered segment if the project\u2014\n**(i)**\nwould enhance the recovery of a species listed as threatened or endangered under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), a sensitive species, or a species of greatest conservation need, including the Gila Trout (Oncorhynchus gilae); and\n**(ii)**\nwould not unreasonably diminish the free-flowing nature or outstandingly remarkable values of the covered segment.\n**(C) Projects within wilderness areas**\nA native fish habitat restoration project (including fish barriers) located within an area designated as a component of the National Wilderness Preservation System shall be constructed consistent with\u2014\n**(i)**\nthe Wilderness Act ( 16 U.S.C. 1131 et seq. ); and\n**(ii)**\nthe applicable wilderness management plan.\n**(6) State land jurisdiction**\nNothing in this section or an amendment made by this section affects the jurisdiction of land under the jurisdiction of the State, including land under the jurisdiction of the New Mexico State Land Office and the New Mexico Department of Game and Fish.\n**(7) Fish and wildlife**\nNothing in this section or an amendment made by this section affects the jurisdiction of the State with respect to fish and wildlife in the State.\n**(8) Treaty rights**\nNothing in this section or an amendment made by this section alters, modifies, diminishes, or extinguishes the reserved treaty rights of any Indian Tribe with respect to hunting, fishing, gathering, and cultural or religious rights in the vicinity of a covered segment as protected by a treaty.\n#### 3. Modification of boundaries of Gila Cliff Dwellings National Monument and Gila National Forest\n##### (a) Transfer of administrative jurisdiction\n**(1) In general**\nAdministrative jurisdiction over the land described in paragraph (2) is transferred from the Secretary of Agriculture to the Secretary of the Interior.\n**(2) Description of land**\nThe land referred to in paragraph (1) is the approximately 440 acres of land identified as Transfer from USDA Forest Service to National Park Service on the map entitled Gila Cliff Dwellings National Monument Proposed Boundary Adjustment and dated March 2020.\n##### (b) Boundary modifications\n**(1) Gila Cliff Dwellings National Monument**\n**(A) In general**\nThe boundary of the Gila Cliff Dwellings National Monument is revised to incorporate the land transferred to the Secretary of the Interior under subsection (a)(1).\n**(B) Map**\n**(i) In general**\nThe Secretary of the Interior shall prepare and keep on file for public inspection in the appropriate office of the National Park Service a map and a legal description of the revised boundary of the Gila Cliff Dwellings National Monument.\n**(ii) Effect**\nThe map and legal description under clause (i) shall have the same force and effect as if included in this section, except that the Secretary of the Interior may correct minor errors in the map and legal description.\n**(2) Gila National Forest**\n**(A) In general**\nThe boundary of the Gila National Forest is modified to exclude the land transferred to the Secretary of the Interior under subsection (a)(1).\n**(B) Map**\n**(i) In general**\nThe Secretary of Agriculture shall prepare and keep on file for public inspection in the appropriate office of the Forest Service a map and a legal description of the revised boundary of the Gila National Forest.\n**(ii) Effect**\nThe map and legal description under clause (i) shall have the same force and effect as if included in this section, except that the Secretary of Agriculture may correct minor errors in the map and legal description.",
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
        "actionDate": "2025-04-10",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2903",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "M.H. Dutch Salmon Greater Gila Wild and Scenic River Act",
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
            "name": "Aquatic ecology",
            "updateDate": "2025-12-16T15:31:31Z"
          },
          {
            "name": "Fishes",
            "updateDate": "2025-12-16T15:31:31Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-12-16T15:31:31Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-12-16T15:31:31Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2025-12-16T15:31:31Z"
          },
          {
            "name": "New Mexico",
            "updateDate": "2025-12-16T15:31:31Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-12-16T15:31:31Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-12-16T15:31:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-22T15:14:53Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1476is.xml"
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
      "title": "M.H. Dutch Salmon Greater Gila Wild and Scenic River Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "M.H. Dutch Salmon Greater Gila Wild and Scenic River Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Wild and Scenic Rivers Act to designate certain segments of the Gila River system in the State of New Mexico as components of the National Wild and Scenic Rivers System, to provide for the transfer of administrative jurisdiction over certain Federal land in the State of New Mexico, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:45Z"
    }
  ]
}
```
