# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1829?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1829
- Title: Apache County and Navajo County Conveyance Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1829
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-05-13 16:54:39 - Floor: Mr. Westerman moved to suspend the rules and pass the bill.
- 2025-05-13 16:54:52 - Floor: Considered under suspension of the rules. (consideration: CR H1975-1976)
- 2025-05-13 16:54:55 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 1829.
- 2025-05-13 17:00:44 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1975-1976)
- 2025-05-13 17:00:44 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1975-1976)
- 2025-05-13 17:00:46 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-05-14 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-03-04: Introduced in House

## Actions

- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-05-13 16:54:39 - Floor: Mr. Westerman moved to suspend the rules and pass the bill.
- 2025-05-13 16:54:52 - Floor: Considered under suspension of the rules. (consideration: CR H1975-1976)
- 2025-05-13 16:54:55 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 1829.
- 2025-05-13 17:00:44 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1975-1976)
- 2025-05-13 17:00:44 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1975-1976)
- 2025-05-13 17:00:46 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-05-14 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1829",
    "number": "1829",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001132",
        "district": "2",
        "firstName": "Elijah",
        "fullName": "Rep. Crane, Elijah [R-AZ-2]",
        "lastName": "Crane",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Apache County and Navajo County Conveyance Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
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
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate and Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2025-05-13",
      "actionTime": "17:00:46",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37300",
      "actionDate": "2025-05-13",
      "actionTime": "17:00:44",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1975-1976)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-05-13",
      "actionTime": "17:00:44",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H1975-1976)",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-05-13",
      "actionTime": "16:54:55",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "DEBATE - The House proceeded with forty minutes of debate on H.R. 1829.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-05-13",
      "actionTime": "16:54:52",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered under suspension of the rules. (consideration: CR H1975-1976)",
      "type": "Floor"
    },
    {
      "actionCode": "H30300",
      "actionDate": "2025-05-13",
      "actionTime": "16:54:39",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Mr. Westerman moved to suspend the rules and pass the bill.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-04",
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
        "item": [
          {
            "date": "2026-03-04T16:02:16Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-14T16:44:22Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T15:00:06Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "systemCode": "sseg00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-04T15:00:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1829ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1829\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Mr. Crane introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Secretary of Agriculture to convey certain lands within the Apache-Sitgreaves National Forest, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Apache County and Navajo County Conveyance Act of 2025 .\n#### 2. Conveyance of certain land within the Apache-Sitgreaves National Forests to Navajo County, Arizona\n##### (a) Definitions\nIn this section:\n**(1) County**\nThe term County means Navajo County, Arizona.\n**(2) Map**\nThe term map means the map entitled Pinedale Cemetery Expansion and dated May 23, 2022.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (b) Conveyance required\nSubject to this section, if the County submits to the Secretary a written request for conveyance of the property described in subsection (c)(1) not later than 180 days after the date of enactment of this Act, the Secretary shall convey to the County all right, title, and interest of the United States in and to the property described in subsection (c)(1).\n##### (c) Property described\n**(1) In general**\nThe property referred to in subsection (b) is\u2014\n**(A)**\nthe parcel of real property, including all land and improvements, generally depicted as Exist. Cemetery on the map, consisting of approximately 2.5 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona; and\n**(B)**\nthe parcel of real property, including all land and improvements, generally depicted as Proposed Expansion on the map, consisting of approximately 2.5 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona.\n**(2) Map**\n**(A) Minor errors**\nThe Secretary may correct minor errors in the map.\n**(B) Availability**\nA copy of the map shall be on file and available for public inspection in the appropriate offices of the Forest Service.\n**(3) Survey**\nThe exact acreage and legal description of the National Forest System land to be conveyed under subsection (b) shall be determined by a survey satisfactory to the Secretary.\n##### (d) Terms and conditions\nThe conveyance under subsection (b) shall\u2014\n**(1)**\nbe subject to valid existing rights;\n**(2)**\nbe made without consideration;\n**(3)**\nbe made by quitclaim deed;\n**(4)**\nnot be subject to section 120(h) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9620(h) ); and\n**(5)**\nbe subject to any other terms and conditions as the Secretary considers appropriate to protect the interests of the United States.\n##### (e) Costs of conveyance\nAs a condition of the conveyance under subsection (b), the County shall pay all costs associated with the conveyance, including the cost of\u2014\n**(1)**\na survey, if necessary, under subsection (c)(3); and\n**(2)**\nany environmental analysis and resource surveys required by Federal law.\n##### (f) Required use as cemetery\nThe property conveyed to the County under subsection (b) shall be used by the County as a cemetery.\n##### (g) Reversion\nIf the property conveyed under subsection (b) is used in a manner that is inconsistent with the requirement of subsection (f), all right, title, and interest in and to the property shall revert to the United States.\n#### 3. Conveyance of certain land within the Apache-Sitgreaves National Forests to Apache County, Arizona\n##### (a) Definitions\nIn this section:\n**(1) County**\nThe term County means Apache County, Arizona.\n**(2) Map**\nThe term map means the map entitled Exhibit, Alpine Cemetery Townsite and dated October, 2019.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (b) Conveyance required\nSubject to this section, if the County submits to the Secretary a written request for conveyance of the property described in subsection (c)(1) not later than 365 days after the date of enactment of this Act, the Secretary shall convey to the County all right, title, and interest of the United States in and to the property described in subsection (c)(1).\n##### (c) Property described\n**(1) In general**\nThe property referred to in subsection (b) is\u2014\n**(A)**\nthe parcel of real property, including all land and improvements, generally depicted as the Existing Alpine Cemetery on the map, consisting of approximately 2.56 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona; and\n**(B)**\nthe parcel of real property, including all land and improvements, generally depicted as the Proposed Townsite Tract on the map, consisting of approximately 8.06 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona.\n**(2) Map**\n**(A) Minor errors**\nThe Secretary may correct minor errors in the map.\n**(B) Availability**\nA copy of the map shall be on file and available for public inspection in the appropriate offices of the Forest Service.\n**(3) Survey**\nThe exact acreage and legal description of the National Forest System land to be conveyed under subsection (b) shall be determined by a survey satisfactory to the Secretary.\n##### (d) Terms and conditions\nThe conveyance under subsection (b) shall\u2014\n**(1)**\nbe subject to valid existing rights;\n**(2)**\nbe made without consideration;\n**(3)**\nbe made by quitclaim deed;\n**(4)**\nnot be subject to section 120(h) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9620(h) ); and\n**(5)**\nbe subject to any other terms and conditions as the Secretary considers appropriate to protect the interests of the United States.\n##### (e) Costs of conveyance\nAs a condition of the conveyance under subsection (b), the County shall pay all costs associated with the conveyance, including the cost of\u2014\n**(1)**\na survey, if necessary, under subsection (c)(3); and\n**(2)**\nany environmental analysis and resource surveys required by Federal law.\n##### (f) Required use as cemetery\nThe property conveyed to the County under subsection (b) shall be used by the County as a cemetery.\n##### (g) Reversion\nIf the property conveyed under subsection (b) is used in a manner that is inconsistent with the requirement of subsection (f), all right, title, and interest in and to the property shall revert to the United States.",
      "versionDate": "2025-03-04",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1829rfs.xml",
      "text": "IIB\n119th CONGRESS\n1st Session\nH. R. 1829\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Received; read twice and referred to the Committee on Energy and Natural Resources\nAN ACT\nTo require the Secretary of Agriculture to convey certain lands within the Apache-Sitgreaves National Forest, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Apache County and Navajo County Conveyance Act of 2025 .\n#### 2. Conveyance of certain land within the Apache-Sitgreaves National Forests to Navajo County, Arizona\n##### (a) Definitions\nIn this section:\n**(1) County**\nThe term County means Navajo County, Arizona.\n**(2) Map**\nThe term map means the map entitled Pinedale Cemetery Expansion and dated May 23, 2022.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (b) Conveyance required\nSubject to this section, if the County submits to the Secretary a written request for conveyance of the property described in subsection (c)(1) not later than 180 days after the date of enactment of this Act, the Secretary shall convey to the County all right, title, and interest of the United States in and to the property described in subsection (c)(1).\n##### (c) Property described\n**(1) In general**\nThe property referred to in subsection (b) is\u2014\n**(A)**\nthe parcel of real property, including all land and improvements, generally depicted as Exist. Cemetery on the map, consisting of approximately 2.5 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona; and\n**(B)**\nthe parcel of real property, including all land and improvements, generally depicted as Proposed Expansion on the map, consisting of approximately 2.5 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona.\n**(2) Map**\n**(A) Minor errors**\nThe Secretary may correct minor errors in the map.\n**(B) Availability**\nA copy of the map shall be on file and available for public inspection in the appropriate offices of the Forest Service.\n**(3) Survey**\nThe exact acreage and legal description of the National Forest System land to be conveyed under subsection (b) shall be determined by a survey satisfactory to the Secretary.\n##### (d) Terms and conditions\nThe conveyance under subsection (b) shall\u2014\n**(1)**\nbe subject to valid existing rights;\n**(2)**\nbe made without consideration;\n**(3)**\nbe made by quitclaim deed;\n**(4)**\nnot be subject to section 120(h) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9620(h) ); and\n**(5)**\nbe subject to any other terms and conditions as the Secretary considers appropriate to protect the interests of the United States.\n##### (e) Costs of conveyance\nAs a condition of the conveyance under subsection (b), the County shall pay all costs associated with the conveyance, including the cost of\u2014\n**(1)**\na survey, if necessary, under subsection (c)(3); and\n**(2)**\nany environmental analysis and resource surveys required by Federal law.\n##### (f) Required use as cemetery\nThe property conveyed to the County under subsection (b) shall be used by the County as a cemetery.\n##### (g) Reversion\nIf the property conveyed under subsection (b) is used in a manner that is inconsistent with the requirement of subsection (f), all right, title, and interest in and to the property shall revert to the United States.\n#### 3. Conveyance of certain land within the Apache-Sitgreaves National Forests to Apache County, Arizona\n##### (a) Definitions\nIn this section:\n**(1) County**\nThe term County means Apache County, Arizona.\n**(2) Map**\nThe term map means the map entitled Exhibit, Alpine Cemetery Townsite and dated October, 2019.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (b) Conveyance required\nSubject to this section, if the County submits to the Secretary a written request for conveyance of the property described in subsection (c)(1) not later than 365 days after the date of enactment of this Act, the Secretary shall convey to the County all right, title, and interest of the United States in and to the property described in subsection (c)(1).\n##### (c) Property described\n**(1) In general**\nThe property referred to in subsection (b) is\u2014\n**(A)**\nthe parcel of real property, including all land and improvements, generally depicted as the Existing Alpine Cemetery on the map, consisting of approximately 2.56 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona; and\n**(B)**\nthe parcel of real property, including all land and improvements, generally depicted as the Proposed Townsite Tract on the map, consisting of approximately 8.06 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona.\n**(2) Map**\n**(A) Minor errors**\nThe Secretary may correct minor errors in the map.\n**(B) Availability**\nA copy of the map shall be on file and available for public inspection in the appropriate offices of the Forest Service.\n**(3) Survey**\nThe exact acreage and legal description of the National Forest System land to be conveyed under subsection (b) shall be determined by a survey satisfactory to the Secretary.\n##### (d) Terms and conditions\nThe conveyance under subsection (b) shall\u2014\n**(1)**\nbe subject to valid existing rights;\n**(2)**\nbe made without consideration;\n**(3)**\nbe made by quitclaim deed;\n**(4)**\nnot be subject to section 120(h) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9620(h) ); and\n**(5)**\nbe subject to any other terms and conditions as the Secretary considers appropriate to protect the interests of the United States.\n##### (e) Costs of conveyance\nAs a condition of the conveyance under subsection (b), the County shall pay all costs associated with the conveyance, including the cost of\u2014\n**(1)**\na survey, if necessary, under subsection (c)(3); and\n**(2)**\nany environmental analysis and resource surveys required by Federal law.\n##### (f) Required use as cemetery\nThe property conveyed to the County under subsection (b) shall be used by the County as a cemetery.\n##### (g) Reversion\nIf the property conveyed under subsection (b) is used in a manner that is inconsistent with the requirement of subsection (f), all right, title, and interest in and to the property shall revert to the United States.",
      "versionDate": "2025-05-14",
      "versionType": "Referred in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1829eh.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1829\nIN THE HOUSE OF REPRESENTATIVES\nAN ACT\nTo require the Secretary of Agriculture to convey certain lands within the Apache-Sitgreaves National Forest, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Apache County and Navajo County Conveyance Act of 2025 .\n#### 2. Conveyance of certain land within the Apache-Sitgreaves National Forests to Navajo County, Arizona\n##### (a) Definitions\nIn this section:\n**(1) County**\nThe term County means Navajo County, Arizona.\n**(2) Map**\nThe term map means the map entitled Pinedale Cemetery Expansion and dated May 23, 2022.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (b) Conveyance required\nSubject to this section, if the County submits to the Secretary a written request for conveyance of the property described in subsection (c)(1) not later than 180 days after the date of enactment of this Act, the Secretary shall convey to the County all right, title, and interest of the United States in and to the property described in subsection (c)(1).\n##### (c) Property described\n**(1) In general**\nThe property referred to in subsection (b) is\u2014\n**(A)**\nthe parcel of real property, including all land and improvements, generally depicted as Exist. Cemetery on the map, consisting of approximately 2.5 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona; and\n**(B)**\nthe parcel of real property, including all land and improvements, generally depicted as Proposed Expansion on the map, consisting of approximately 2.5 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona.\n**(2) Map**\n**(A) Minor errors**\nThe Secretary may correct minor errors in the map.\n**(B) Availability**\nA copy of the map shall be on file and available for public inspection in the appropriate offices of the Forest Service.\n**(3) Survey**\nThe exact acreage and legal description of the National Forest System land to be conveyed under subsection (b) shall be determined by a survey satisfactory to the Secretary.\n##### (d) Terms and conditions\nThe conveyance under subsection (b) shall\u2014\n**(1)**\nbe subject to valid existing rights;\n**(2)**\nbe made without consideration;\n**(3)**\nbe made by quitclaim deed;\n**(4)**\nnot be subject to section 120(h) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9620(h) ); and\n**(5)**\nbe subject to any other terms and conditions as the Secretary considers appropriate to protect the interests of the United States.\n##### (e) Costs of conveyance\nAs a condition of the conveyance under subsection (b), the County shall pay all costs associated with the conveyance, including the cost of\u2014\n**(1)**\na survey, if necessary, under subsection (c)(3); and\n**(2)**\nany environmental analysis and resource surveys required by Federal law.\n##### (f) Required use as cemetery\nThe property conveyed to the County under subsection (b) shall be used by the County as a cemetery.\n##### (g) Reversion\nIf the property conveyed under subsection (b) is used in a manner that is inconsistent with the requirement of subsection (f), all right, title, and interest in and to the property shall revert to the United States.\n#### 3. Conveyance of certain land within the Apache-Sitgreaves National Forests to Apache County, Arizona\n##### (a) Definitions\nIn this section:\n**(1) County**\nThe term County means Apache County, Arizona.\n**(2) Map**\nThe term map means the map entitled Exhibit, Alpine Cemetery Townsite and dated October, 2019.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (b) Conveyance required\nSubject to this section, if the County submits to the Secretary a written request for conveyance of the property described in subsection (c)(1) not later than 365 days after the date of enactment of this Act, the Secretary shall convey to the County all right, title, and interest of the United States in and to the property described in subsection (c)(1).\n##### (c) Property described\n**(1) In general**\nThe property referred to in subsection (b) is\u2014\n**(A)**\nthe parcel of real property, including all land and improvements, generally depicted as the Existing Alpine Cemetery on the map, consisting of approximately 2.56 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona; and\n**(B)**\nthe parcel of real property, including all land and improvements, generally depicted as the Proposed Townsite Tract on the map, consisting of approximately 8.06 acres of National Forest System land located in the Apache-Sitgreaves National Forests in Arizona.\n**(2) Map**\n**(A) Minor errors**\nThe Secretary may correct minor errors in the map.\n**(B) Availability**\nA copy of the map shall be on file and available for public inspection in the appropriate offices of the Forest Service.\n**(3) Survey**\nThe exact acreage and legal description of the National Forest System land to be conveyed under subsection (b) shall be determined by a survey satisfactory to the Secretary.\n##### (d) Terms and conditions\nThe conveyance under subsection (b) shall\u2014\n**(1)**\nbe subject to valid existing rights;\n**(2)**\nbe made without consideration;\n**(3)**\nbe made by quitclaim deed;\n**(4)**\nnot be subject to section 120(h) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9620(h) ); and\n**(5)**\nbe subject to any other terms and conditions as the Secretary considers appropriate to protect the interests of the United States.\n##### (e) Costs of conveyance\nAs a condition of the conveyance under subsection (b), the County shall pay all costs associated with the conveyance, including the cost of\u2014\n**(1)**\na survey, if necessary, under subsection (c)(3); and\n**(2)**\nany environmental analysis and resource surveys required by Federal law.\n##### (f) Required use as cemetery\nThe property conveyed to the County under subsection (b) shall be used by the County as a cemetery.\n##### (g) Reversion\nIf the property conveyed under subsection (b) is used in a manner that is inconsistent with the requirement of subsection (f), all right, title, and interest in and to the property shall revert to the United States.",
      "versionDate": "",
      "versionType": "Engrossed in House"
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
            "name": "Arizona",
            "updateDate": "2025-05-14T14:32:08Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-05-14T14:32:08Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-05-14T14:32:08Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-05-14T14:32:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T13:59:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1829",
          "measure-number": "1829",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-04",
          "originChamber": "HOUSE",
          "update-date": "2025-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1829v00",
            "update-date": "2025-05-12"
          },
          "action-date": "2025-03-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Apache County and Navajo County Conveyance Act of 2025</strong></p><p>This bill requires the Forest Service to convey certain lands within the Apache-Sitgreaves National Forest to Navajo County and Apache County, Arizona. The counties must use the land as cemeteries.</p><p>As a condition of each conveyance, the counties must pay all associated costs, including the costs of surveys and environmental analyses.</p>"
        },
        "title": "Apache County and Navajo County Conveyance Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1829.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Apache County and Navajo County Conveyance Act of 2025</strong></p><p>This bill requires the Forest Service to convey certain lands within the Apache-Sitgreaves National Forest to Navajo County and Apache County, Arizona. The counties must use the land as cemeteries.</p><p>As a condition of each conveyance, the counties must pay all associated costs, including the costs of surveys and environmental analyses.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119hr1829"
    },
    "title": "Apache County and Navajo County Conveyance Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Apache County and Navajo County Conveyance Act of 2025</strong></p><p>This bill requires the Forest Service to convey certain lands within the Apache-Sitgreaves National Forest to Navajo County and Apache County, Arizona. The counties must use the land as cemeteries.</p><p>As a condition of each conveyance, the counties must pay all associated costs, including the costs of surveys and environmental analyses.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119hr1829"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1829ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1829rfs.xml"
        }
      ],
      "type": "Referred in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1829eh.xml"
        }
      ],
      "type": "Engrossed in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RFS",
      "billTextVersionName": "Referred in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Apache County and Navajo County Conveyance Act of 2025",
      "titleType": "Short Titles from RFS (Referred to Senate) bill text",
      "titleTypeCode": "255",
      "updateDate": "2025-05-17T02:53:20Z"
    },
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Apache County and Navajo County Conveyance Act of 2025",
      "titleType": "Short Title(s) as Passed House",
      "titleTypeCode": "104",
      "updateDate": "2025-05-15T03:38:24Z"
    },
    {
      "title": "Apache County and Navajo County Conveyance Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T10:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Apache County and Navajo County Conveyance Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Agriculture to convey certain lands within the Apache-Sitgreaves National Forest, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T10:48:23Z"
    }
  ]
}
```
