# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/282?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/282
- Title: Katahdin Woods and Waters National Monument Access Act
- Congress: 119
- Bill type: S
- Bill number: 282
- Origin chamber: Senate
- Introduced date: 2025-01-28
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-01-28: Introduced in Senate
- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-06-18 - Floor: Passed Senate without amendment by Voice Vote. (text: CR S3459)
- 2025-06-18 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Voice Vote.
- 2025-06-18 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2025-06-18 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent. (consideration: CR S3458)
- 2025-06-23 - Floor: Message on Senate action sent to the House.
- 2025-06-23 15:19:22 - Floor: Received in the House.
- 2025-06-23 15:28:46 - Floor: Held at the desk.
- 2026-02-02 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-03 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-02-10 - Committee: Subcommittee Hearings Held
- Latest action: 2025-01-28: Introduced in Senate

## Actions

- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-06-18 - Floor: Passed Senate without amendment by Voice Vote. (text: CR S3459)
- 2025-06-18 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Voice Vote.
- 2025-06-18 - Committee: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent.
- 2025-06-18 - Discharge: Senate Committee on Energy and Natural Resources discharged by Unanimous Consent. (consideration: CR S3458)
- 2025-06-23 - Floor: Message on Senate action sent to the House.
- 2025-06-23 15:19:22 - Floor: Received in the House.
- 2025-06-23 15:28:46 - Floor: Held at the desk.
- 2026-02-02 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-03 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-02-10 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/282",
    "number": "282",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "Katahdin Woods and Waters National Monument Access Act",
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
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-02",
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
      "actionCode": "H15000",
      "actionDate": "2025-06-23",
      "actionTime": "15:28:46",
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
      "actionTime": "15:19:22",
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
      "text": "Passed Senate without amendment by Voice Vote. (text: CR S3459)",
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
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
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
          "date": "2026-02-02T20:50:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-10T19:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-02-03T18:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": [
          {
            "date": "2025-06-18T17:23:39Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-01-28T20:32:54Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s282rfh.xml",
      "text": "IC\n119th CONGRESS\n2d Session\nS. 282\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 2, 2026 Referred to the Committee on Natural Resources\nAN ACT\nTo provide greater regional access to the Katahdin Woods and Waters National Monument in the State of Maine, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Katahdin Woods and Waters National Monument Access Act .\n#### 2. Definitions\nIn this Act:\n**(1) Authorized acquisition area**\nThe term authorized acquisition area means the designated area outside the boundary of the National Monument depicted as Authorized Acquisition Area on the map entitled Katahdin Woods and Waters National Monument Proposed Boundary Adjustment , numbered 686/193,181 and dated March 2024.\n**(2) National Monument**\nThe term National Monument means the Katahdin Woods and Waters National Monument in the State of Maine established by the Proclamation.\n**(3) Proclamation**\nThe term Proclamation means Presidential Proclamation Number 9476, dated August 24, 2016 ( 54 U.S.C. 320301 note).\n**(4) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Acquisition of additional land for National Monument\n##### (a) Boundary\nThe boundaries of the National Monument shall be the boundaries established by the Proclamation.\n##### (b) Acquisition\n**(1) In general**\nSubject to paragraph (2), the Secretary may acquire, by purchase from a willing seller, donation, or exchange, land or interests in land within the authorized acquisition area.\n**(2) Prohibition on use of eminent domain**\nNothing in this Act authorizes the use of eminent domain to acquire land or an interest in land.\n##### (c) Treatment of acquired land; boundary adjustment\nOn acquisition by the Secretary of any land pursuant to subsection (b)\u2014\n**(1)**\nthe land shall be included in the National Monument; and\n**(2)**\nthe boundaries of the National Monument shall be adjusted accordingly.\n#### 4. Administration of National Monument\n##### (a) Administration\nThe Secretary shall administer the National Monument (including the land added to the National Monument under this Act) in accordance with\u2014\n**(1)**\nthis Act;\n**(2)**\nthe Proclamation; and\n**(3)**\nthe laws generally applicable to units of the National Park System.\n##### (b) Hunting, fishing, and outdoor recreation on acquired land\nThe Secretary shall allow hunting, fishing, or any other outdoor recreation activity on land acquired pursuant to section 3(b)\u2014\n**(1)**\nif that activity was in existence on the day before the date of acquisition of the land; and\n**(2)**\nconsistent with the management of that activity under the Proclamation.\n##### (c) Collection of fiddlehead ferns\n**(1) In general**\nSubject to paragraph (2), the Secretary shall allow the gathering by hand of fiddlehead ferns (Matteuccia struthiopteris) in the National Monument for noncommercial personal use and consumption by the general public.\n**(2) Limitation**\nIf the Secretary determines that the gathering of fiddlehead ferns (Matteuccia struthiopteris) under paragraph (1) may adversely affect resources of the National Monument, the Secretary may limit the gathering of fiddlehead ferns (Matteuccia struthiopteris) under that paragraph in accordance with applicable regulations.\n##### (d) Public education\nIn accordance with the mission of the National Park Service, the Secretary shall collaborate with local communities and Tribal governments to educate the public regarding the natural environment and history of land management in the National Monument, including the shaping of that landscape by Native communities and practices, successive generations of timber management, and other activities.\n##### (e) Forestry\nIn accordance with the management plan for the National Monument, the Secretary may conduct such noncommercial timber harvests as the Secretary determines to be necessary.\n##### (f) Protection of existing access\nNothing in this Act affects valid existing rights, including existing rights of access through the National Monument for the removal of timber outside the boundaries of the National Monument.\n##### (g) Public safety\n**(1) In general**\nThe Secretary shall provide to the public appropriate safety education and notification materials to ensure safe interactions between visitors and logging trucks, equipment, and operations on roads in or adjacent to the National Monument.\n**(2) Procedures**\nThe Secretary shall collaborate with affected stakeholders to establish procedures to meet the needs of visitors to the National Monument, logging and trucking operations, and other users of roads in or adjacent to the National Monument to ensure safe interactions between active logging operations and visitors.\n#### 5. Administrative sites and visitor facilities\n##### (a) In general\nTo facilitate the administration of the National Monument, the Secretary may acquire, by purchase from a willing seller, donation, or exchange, not more than 10 acres of land or interests in land, including improvements, for the administration of the National Monument and visitor services outside the boundaries, but within the vicinity, of the National Monument.\n##### (b) Agreements\nThe Secretary may enter into agreements with State of Maine, units of Tribal or local government, or private entities\u2014\n**(1)**\nto carry out this section; and\n**(2)**\nto develop a cooperative information center for the National Monument.",
      "versionDate": "2026-02-02",
      "versionType": "Referred in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s282is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 282\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mr. King introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo provide greater regional access to the Katahdin Woods and Waters National Monument in the State of Maine, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Katahdin Woods and Waters National Monument Access Act .\n#### 2. Definitions\nIn this Act:\n**(1) Authorized acquisition area**\nThe term authorized acquisition area means the designated area outside the boundary of the National Monument depicted as Authorized Acquisition Area on the map entitled Katahdin Woods and Waters National Monument Proposed Boundary Adjustment , numbered 686/193,181 and dated March 2024.\n**(2) National Monument**\nThe term National Monument means the Katahdin Woods and Waters National Monument in the State of Maine established by the Proclamation.\n**(3) Proclamation**\nThe term Proclamation means Presidential Proclamation Number 9476, dated August 24, 2016 ( 54 U.S.C. 320301 note).\n**(4) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Acquisition of additional land for National Monument\n##### (a) Boundary\nThe boundaries of the National Monument shall be the boundaries established by the Proclamation.\n##### (b) Acquisition\n**(1) In general**\nSubject to paragraph (2), the Secretary may acquire, by purchase from a willing seller, donation, or exchange, land or interests in land within the authorized acquisition area.\n**(2) Prohibition on use of eminent domain**\nNothing in this Act authorizes the use of eminent domain to acquire land or an interest in land.\n##### (c) Treatment of acquired land; boundary adjustment\nOn acquisition by the Secretary of any land pursuant to subsection (b)\u2014\n**(1)**\nthe land shall be included in the National Monument; and\n**(2)**\nthe boundaries of the National Monument shall be adjusted accordingly.\n#### 4. Administration of National Monument\n##### (a) Administration\nThe Secretary shall administer the National Monument (including the land added to the National Monument under this Act) in accordance with\u2014\n**(1)**\nthis Act;\n**(2)**\nthe Proclamation; and\n**(3)**\nthe laws generally applicable to units of the National Park System.\n##### (b) Hunting, fishing, and outdoor recreation on acquired land\nThe Secretary shall allow hunting, fishing, or any other outdoor recreation activity on land acquired pursuant to section 3(b)\u2014\n**(1)**\nif that activity was in existence on the day before the date of acquisition of the land; and\n**(2)**\nconsistent with the management of that activity under the Proclamation.\n##### (c) Collection of fiddlehead ferns\n**(1) In general**\nSubject to paragraph (2), the Secretary shall allow the gathering by hand of fiddlehead ferns (Matteuccia struthiopteris) in the National Monument for noncommercial personal use and consumption by the general public.\n**(2) Limitation**\nIf the Secretary determines that the gathering of fiddlehead ferns (Matteuccia struthiopteris) under paragraph (1) may adversely affect resources of the National Monument, the Secretary may limit the gathering of fiddlehead ferns (Matteuccia struthiopteris) under that paragraph in accordance with applicable regulations.\n##### (d) Public education\nIn accordance with the mission of the National Park Service, the Secretary shall collaborate with local communities and Tribal governments to educate the public regarding the natural environment and history of land management in the National Monument, including the shaping of that landscape by Native communities and practices, successive generations of timber management, and other activities.\n##### (e) Forestry\nIn accordance with the management plan for the National Monument, the Secretary may conduct such noncommercial timber harvests as the Secretary determines to be necessary.\n##### (f) Protection of existing access\nNothing in this Act affects valid existing rights, including existing rights of access through the National Monument for the removal of timber outside the boundaries of the National Monument.\n##### (g) Public safety\n**(1) In general**\nThe Secretary shall provide to the public appropriate safety education and notification materials to ensure safe interactions between visitors and logging trucks, equipment, and operations on roads in or adjacent to the National Monument.\n**(2) Procedures**\nThe Secretary shall collaborate with affected stakeholders to establish procedures to meet the needs of visitors to the National Monument, logging and trucking operations, and other users of roads in or adjacent to the National Monument to ensure safe interactions between active logging operations and visitors.\n#### 5. Administrative sites and visitor facilities\n##### (a) In general\nTo facilitate the administration of the National Monument, the Secretary may acquire, by purchase from a willing seller, donation, or exchange, not more than 10 acres of land or interests in land, including improvements, for the administration of the National Monument and visitor services outside the boundaries, but within the vicinity, of the National Monument.\n##### (b) Agreements\nThe Secretary may enter into agreements with State of Maine, units of Tribal or local government, or private entities\u2014\n**(1)**\nto carry out this section; and\n**(2)**\nto develop a cooperative information center for the National Monument.",
      "versionDate": "2025-01-28",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s282es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 282\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo provide greater regional access to the Katahdin Woods and Waters National Monument in the State of Maine, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Katahdin Woods and Waters National Monument Access Act .\n#### 2. Definitions\nIn this Act:\n**(1) Authorized acquisition area**\nThe term authorized acquisition area means the designated area outside the boundary of the National Monument depicted as Authorized Acquisition Area on the map entitled Katahdin Woods and Waters National Monument Proposed Boundary Adjustment , numbered 686/193,181 and dated March 2024.\n**(2) National Monument**\nThe term National Monument means the Katahdin Woods and Waters National Monument in the State of Maine established by the Proclamation.\n**(3) Proclamation**\nThe term Proclamation means Presidential Proclamation Number 9476, dated August 24, 2016 ( 54 U.S.C. 320301 note).\n**(4) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Acquisition of additional land for National Monument\n##### (a) Boundary\nThe boundaries of the National Monument shall be the boundaries established by the Proclamation.\n##### (b) Acquisition\n**(1) In general**\nSubject to paragraph (2), the Secretary may acquire, by purchase from a willing seller, donation, or exchange, land or interests in land within the authorized acquisition area.\n**(2) Prohibition on use of eminent domain**\nNothing in this Act authorizes the use of eminent domain to acquire land or an interest in land.\n##### (c) Treatment of acquired land; boundary adjustment\nOn acquisition by the Secretary of any land pursuant to subsection (b)\u2014\n**(1)**\nthe land shall be included in the National Monument; and\n**(2)**\nthe boundaries of the National Monument shall be adjusted accordingly.\n#### 4. Administration of National Monument\n##### (a) Administration\nThe Secretary shall administer the National Monument (including the land added to the National Monument under this Act) in accordance with\u2014\n**(1)**\nthis Act;\n**(2)**\nthe Proclamation; and\n**(3)**\nthe laws generally applicable to units of the National Park System.\n##### (b) Hunting, fishing, and outdoor recreation on acquired land\nThe Secretary shall allow hunting, fishing, or any other outdoor recreation activity on land acquired pursuant to section 3(b)\u2014\n**(1)**\nif that activity was in existence on the day before the date of acquisition of the land; and\n**(2)**\nconsistent with the management of that activity under the Proclamation.\n##### (c) Collection of fiddlehead ferns\n**(1) In general**\nSubject to paragraph (2), the Secretary shall allow the gathering by hand of fiddlehead ferns (Matteuccia struthiopteris) in the National Monument for noncommercial personal use and consumption by the general public.\n**(2) Limitation**\nIf the Secretary determines that the gathering of fiddlehead ferns (Matteuccia struthiopteris) under paragraph (1) may adversely affect resources of the National Monument, the Secretary may limit the gathering of fiddlehead ferns (Matteuccia struthiopteris) under that paragraph in accordance with applicable regulations.\n##### (d) Public education\nIn accordance with the mission of the National Park Service, the Secretary shall collaborate with local communities and Tribal governments to educate the public regarding the natural environment and history of land management in the National Monument, including the shaping of that landscape by Native communities and practices, successive generations of timber management, and other activities.\n##### (e) Forestry\nIn accordance with the management plan for the National Monument, the Secretary may conduct such noncommercial timber harvests as the Secretary determines to be necessary.\n##### (f) Protection of existing access\nNothing in this Act affects valid existing rights, including existing rights of access through the National Monument for the removal of timber outside the boundaries of the National Monument.\n##### (g) Public safety\n**(1) In general**\nThe Secretary shall provide to the public appropriate safety education and notification materials to ensure safe interactions between visitors and logging trucks, equipment, and operations on roads in or adjacent to the National Monument.\n**(2) Procedures**\nThe Secretary shall collaborate with affected stakeholders to establish procedures to meet the needs of visitors to the National Monument, logging and trucking operations, and other users of roads in or adjacent to the National Monument to ensure safe interactions between active logging operations and visitors.\n#### 5. Administrative sites and visitor facilities\n##### (a) In general\nTo facilitate the administration of the National Monument, the Secretary may acquire, by purchase from a willing seller, donation, or exchange, not more than 10 acres of land or interests in land, including improvements, for the administration of the National Monument and visitor services outside the boundaries, but within the vicinity, of the National Monument.\n##### (b) Agreements\nThe Secretary may enter into agreements with State of Maine, units of Tribal or local government, or private entities\u2014\n**(1)**\nto carry out this section; and\n**(2)**\nto develop a cooperative information center for the National Monument.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Environmental education",
            "updateDate": "2025-06-20T15:37:38Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-06-20T15:37:44Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-06-20T15:37:30Z"
          },
          {
            "name": "Horticulture and plants",
            "updateDate": "2025-06-20T15:37:14Z"
          },
          {
            "name": "Hunting and fishing",
            "updateDate": "2025-06-20T15:37:14Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-06-20T15:37:14Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-06-20T15:37:14Z"
          },
          {
            "name": "Maine",
            "updateDate": "2025-06-20T15:37:14Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2025-06-20T15:37:14Z"
          },
          {
            "name": "Outdoor recreation",
            "updateDate": "2025-06-20T15:37:14Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-06-20T15:37:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-01T20:14:32Z"
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
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s282rfh.xml"
        }
      ],
      "type": "Referred in House"
    },
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s282is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s282es.xml"
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
      "billTextVersionCode": "RFH",
      "billTextVersionName": "Referred in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Katahdin Woods and Waters National Monument Access Act",
      "titleType": "Short Titles from RFH (Referred to House) bill text",
      "titleTypeCode": "257",
      "updateDate": "2026-02-03T13:08:18Z"
    },
    {
      "title": "Katahdin Woods and Waters National Monument Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T11:03:17Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Katahdin Woods and Waters National Monument Access Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-06-19T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Katahdin Woods and Waters National Monument Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-27T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide greater regional access to the Katahdin Woods and Waters National Monument in the State of Maine, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-27T03:18:18Z"
    }
  ]
}
```
