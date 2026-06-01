# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2548?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2548
- Title: Shawnee National Forest Conservation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2548
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2026-01-07T16:57:57Z
- Update date including text: 2026-01-07T16:57:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S4907)
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman with an amendment in the nature of a substitute. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman with an amendment in the nature of a substitute. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 217.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S4907)
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman with an amendment in the nature of a substitute. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman with an amendment in the nature of a substitute. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 217.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2548",
    "number": "2548",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Shawnee National Forest Conservation Act of 2025",
    "type": "S",
    "updateDate": "2026-01-07T16:57:57Z",
    "updateDateIncludingText": "2026-01-07T16:57:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-27",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 217.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S4907)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
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
            "date": "2025-10-27T22:51:24Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-21T20:12:53Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-30T21:14:31Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2548is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2548\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Durbin introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo designate the Camp Hutchins Wilderness and establish Special Management Areas in the Shawnee National Forest in the State of Illinois, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shawnee National Forest Conservation Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Designated natural area**\nThe term designated natural area means an area determined to be of exceptional ecological, botanical, geologic, scenic, or archeological value by\u2014\n**(A)**\nthe Secretary; and\n**(B)**\n**(i)**\nthe State of Illinois; or\n**(ii)**\nthe Secretary of the Interior, acting through the Director of the National Park Service.\n**(2) Designated research natural area**\nThe term designated research natural area means an area that has been selected by the Secretary, and is managed by the Forest Service, for scientific research value.\n**(3) Map**\nThe term Map means the map prepared by the Environmental Law and Policy Center entitled Camp Hutchins Wilderness Area and Special Management Area and dated November 23, 2023.\n**(4) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n**(5) Special Management Area**\nThe term Special Management Area means a Special Management Area established by section 4(a).\n#### 3. Camp Hutchins Wilderness\n##### (a) Addition to the National Wilderness Preservation System\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), certain land in the Shawnee National Forest in the State of Illinois managed by the Forest Service, comprising approximately 750 acres and generally depicted on the Map as Camp Hutchins Wilderness Area\u2014Proposed , is designated as wilderness and as a component of the National Wilderness Preservation System, and shall be known as the Camp Hutchins Wilderness .\n##### (b) Management\nSubject to valid existing rights, the Camp Hutchins Wilderness shall be administered by the Secretary in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), except that any reference in that Act to the effective date shall be considered to be a reference to the date of enactment of this Act.\n##### (c) Hiking trail\nForest Road 211 shall be closed to public vehicular traffic and shall be maintained as a hiking trail, including the eastern extension of Forest Road 211 formerly known as the Hutchins Creek Spur up to the area known as Hutchins Creek Corridor , as generally depicted on the Map.\n##### (d) Withdrawal\nSubject to valid existing rights, all Federal land within the Camp Hutchins Wilderness, including any land or interest in land that is acquired by the United States within the Camp Hutchins Wilderness after the date of enactment of this Act, is withdrawn from\u2014\n**(1)**\nentry, appropriation, or disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\noperation of the mineral leasing, mineral materials, and geothermal leasing laws.\n##### (e) Map and legal description\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file a map and legal description of the Camp Hutchins Wilderness with\u2014\n**(A)**\nthe Committee on Agriculture, Nutrition, and Forestry of the Senate; and\n**(B)**\nthe Committee on Agriculture of the House of Representatives.\n**(2) Effect**\nThe map and legal description filed under paragraph (1) shall have the same force and effect as if included in this Act, except that the Secretary may correct clerical and typographical errors in the map and legal description.\n**(3) Availability**\nThe map and legal description filed under paragraph (1) shall be on file and available for public inspection in the appropriate office of the Secretary and on the Forest Service website.\n#### 4. Establishment of Special Management Areas\n##### (a) Establishment\nSubject to valid existing rights, the following Special Management Areas within the Shawnee National Forest in the State of Illinois are established:\n**(1) Camp Hutchins Special Management Area**\nCertain Federal land managed by the Forest Service, comprising approximately 2,953 acres and generally depicted on the Map as Camp Hutchins Special Management Area\u2014Proposed , which shall be known as the Camp Hutchins Special Management Area .\n**(2) Ripple Hollow Special Management Area**\nCertain Federal land managed by the Forest Service, comprising approximately 3,445 acres and generally depicted as Ripple Hollow Special Management Area\u2014Proposed on the map prepared by the Environmental Law and Policy Center entitled Ripple Hollow Special Management Area and dated November 23, 2023, which shall be known as the Ripple Hollow Special Management Area .\n**(3) Burke Branch Special Management Area**\nCertain Federal land managed by the Forest Service, comprising approximately 6,310 acres and generally depicted as Burke Branch Special Management Area\u2014Proposed , on the map prepared by the Environmental Law and Policy Center entitled Burke Branch Special Management Area and dated November 23, 2023, which shall be known as the Burke Branch Special Management Area .\n##### (b) Purposes\nThe purposes of the Special Management Areas are\u2014\n**(1)**\nto conserve, protect, and enhance the ecological, scenic, wildlife, recreational, cultural, historic, educational, and scientific resources of the Special Management Areas for the benefit and enjoyment of present and future generations;\n**(2)**\nto promote biodiversity and control invasive species; and\n**(3)**\nto allow for the continuation of restoration efforts and scientific study of the designated natural areas and designated research natural areas within the Special Management Areas.\n#### 5. Administration of Special Management Areas\n##### (a) In general\nThe Secretary shall administer the Special Management Areas\u2014\n**(1)**\nin a manner that conserves, protects, and enhances the purposes for which the Special Management Areas are established; and\n**(2)**\nin accordance with\u2014\n**(A)**\nthis section; and\n**(B)**\nother applicable laws.\n##### (b) Management plan\nNot later than 3 years after the date of enactment of this Act, the Secretary shall develop a comprehensive management plan for the long-term protection and management of the Special Management Areas.\n##### (c) Uses\n**(1) In general**\nThe Secretary shall allow only uses of the Special Management Areas that are consistent with the purposes for which the Special Management Areas are established.\n**(2) Prescribed fire**\nThe Secretary may use prescribed fire to sustain the ecological structure and composition of the Special Management Areas to sustain the biodiversity of the Special Management Areas.\n**(3) Management tools**\n**(A) In general**\nThe Secretary may use herbicides, insecticides, and mechanized equipment in the control of fire, insects, disease, and invasive species, including the use of chainsaws, drones, aircraft, pickup trucks, all-terrain vehicles, and rubber and tracked vehicles to carry out management of the Special Management Areas approved by the Secretary.\n**(B) Requirement**\nIn carrying out management of the Special Management Areas, the Secretary shall use the best available technology and science.\n**(4) Motorized vehicles**\nExcept in cases in which motorized vehicles are needed for administrative purposes, emergency response, or access on established roads accessing trailheads, or are essential to provide off-road access for ecosystem management of habitat, the use of motor vehicles in the Special Management Areas shall be prohibited.\n**(5) Roads**\nThe Secretary shall decommission and remove roads within the Special Management Areas, except roads needed for management or access to trailheads, as soon as practicable.\n**(6) Timber**\n**(A) In general**\nCommercial timber harvesting, except as needed for fire, insect, and disease control, and for visitor and administrative safety, in the Special Management Areas shall be prohibited.\n**(B) Activities permitted**\nThinning of trees and other vegetation in the Special Management Areas shall be permitted for restoration of the designated natural areas and designated research natural areas and to further the management objectives described in this section.\n**(7) Inholdings**\n**(A) In general**\nAccess to private inholdings in the Special Management Areas shall be preserved.\n**(B) Acquisitions**\nThe Secretary shall acquire any private inholdings in the Special Management Areas by purchase or exchange as soon as feasible.\n**(8) Hunting and trapping**\n**(A) Hunting**\nHunting shall be permitted in the Special Management Areas as permitted by the State of Illinois and in accordance with regulations of the State of Illinois and regulations of the Forest Service.\n**(B) Trapping**\nTrapping shall not be permitted in the Special Management Areas.\n**(C) Access by motorized vehicles**\nAccess within the Special Management Areas by hunters in motorized vehicles shall be prohibited.\n**(9) Volunteer restoration and research**\n**(A) Volunteers**\nThe Secretary shall allow organized groups of volunteers to participate in ecological restoration activities under the guidance of Forest Service ecologists and botanists within the Special Management Areas through cooperative agreements.\n**(B) Access for research purposes**\nThe Secretary shall allow access to the Special Management Areas for scientific research by qualified individuals and organizations, as determined by the Secretary.\n**(10) Ongoing management decisions**\nThe Supervisor of the Shawnee National Forest shall have the authority, without requiring the permission of the Secretary, to make management decisions concerning any designated natural area or designated research natural area within the Special Management Areas pursuant to the land and resource management plan for the Shawnee National Forest.\n##### (d) Withdrawal\nSubject to valid existing rights, all Federal land within the Special Management Areas, including any land or interest in land that is acquired by the United States within the Special Management Areas after the date of enactment of this Act, is withdrawn from\u2014\n**(1)**\nentry, appropriation, or disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\noperation of the mineral leasing, mineral materials, and geothermal leasing laws.\n##### (e) Maps and legal descriptions\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file a map and legal description of each Special Management Area with\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Natural Resources of the House of Representatives.\n**(2) Effect**\nThe maps and legal descriptions filed under paragraph (1) shall have the same force and effect as if included in this Act, except that the Secretary may correct clerical and typographical errors in the maps and legal descriptions.\n**(3) Availability**\nThe maps and legal descriptions filed under paragraph (1) shall be on file and available for public inspection in the appropriate office of the Secretary and on the Forest Service website.\n##### (f) Public information\nAnnually, the Secretary shall make publicly available on the website of the Shawnee National Forest information describing the progress in achieving the management objectives described in this section.",
      "versionDate": "2025-07-30",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2548rs.xml",
      "text": "II\nCalendar No. 217\n119th CONGRESS\n1st Session\nS. 2548\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Durbin (for himself and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nOctober 27, 2025 Reported by Mr. Boozman , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo designate the Camp Hutchins Wilderness and establish Special Management Areas in the Shawnee National Forest in the State of Illinois, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shawnee National Forest Conservation Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Designated natural area**\nThe term designated natural area means an area determined to be of exceptional ecological, botanical, geologic, scenic, or archeological value by\u2014\n**(A)**\nthe Secretary; and\n**(B)**\n**(i)**\nthe State of Illinois; or\n**(ii)**\nthe Secretary of the Interior, acting through the Director of the National Park Service.\n**(2) Designated research natural area**\nThe term designated research natural area means an area that has been selected by the Secretary, and is managed by the Forest Service, for scientific research value.\n**(3) Map**\nThe term Map means the map prepared by the Environmental Law and Policy Center entitled Camp Hutchins Wilderness Area and Special Management Area and dated November 23, 2023.\n**(4) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n**(5) Special Management Area**\nThe term Special Management Area means a Special Management Area established by section 4(a).\n#### 3. Camp Hutchins Wilderness\n##### (a) Addition to the National Wilderness Preservation System\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), certain land in the Shawnee National Forest in the State of Illinois managed by the Forest Service, comprising approximately 750 acres and generally depicted on the Map as Camp Hutchins Wilderness Area\u2014Proposed , is designated as wilderness and as a component of the National Wilderness Preservation System, and shall be known as the Camp Hutchins Wilderness .\n##### (b) Management\nSubject to valid existing rights, the Camp Hutchins Wilderness shall be administered by the Secretary in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), except that any reference in that Act to the effective date shall be considered to be a reference to the date of enactment of this Act.\n##### (c) Hiking trail\nForest Road 211 shall be closed to public vehicular traffic and shall be maintained as a hiking trail, including the eastern extension of Forest Road 211 formerly known as the Hutchins Creek Spur up to the area known as Hutchins Creek Corridor , as generally depicted on the Map.\n##### (d) Withdrawal\nSubject to valid existing rights, all Federal land within the Camp Hutchins Wilderness, including any land or interest in land that is acquired by the United States within the Camp Hutchins Wilderness after the date of enactment of this Act, is withdrawn from\u2014\n**(1)**\nentry, appropriation, or disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\noperation of the mineral leasing, mineral materials, and geothermal leasing laws.\n##### (e) Map and legal description\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file a map and legal description of the Camp Hutchins Wilderness with\u2014\n**(A)**\nthe Committee on Agriculture, Nutrition, and Forestry of the Senate; and\n**(B)**\nthe Committee on Agriculture of the House of Representatives.\n**(2) Effect**\nThe map and legal description filed under paragraph (1) shall have the same force and effect as if included in this Act, except that the Secretary may correct clerical and typographical errors in the map and legal description.\n**(3) Availability**\nThe map and legal description filed under paragraph (1) shall be on file and available for public inspection in the appropriate office of the Secretary and on the Forest Service website.\n#### 4. Establishment of Special Management Areas\n##### (a) Establishment\nSubject to valid existing rights, the following Special Management Areas within the Shawnee National Forest in the State of Illinois are established:\n**(1) Camp Hutchins Special Management Area**\nCertain Federal land managed by the Forest Service, comprising approximately 2,953 acres and generally depicted on the Map as Camp Hutchins Special Management Area\u2014Proposed , which shall be known as the Camp Hutchins Special Management Area .\n**(2) Ripple Hollow Special Management Area**\nCertain Federal land managed by the Forest Service, comprising approximately 3,445 acres and generally depicted as Ripple Hollow Special Management Area\u2014Proposed on the map prepared by the Environmental Law and Policy Center entitled Ripple Hollow Special Management Area and dated November 23, 2023, which shall be known as the Ripple Hollow Special Management Area .\n**(3) Burke Branch Special Management Area**\nCertain Federal land managed by the Forest Service, comprising approximately 6,310 acres and generally depicted as Burke Branch Special Management Area\u2014Proposed , on the map prepared by the Environmental Law and Policy Center entitled Burke Branch Special Management Area and dated November 23, 2023, which shall be known as the Burke Branch Special Management Area .\n##### (b) Purposes\nThe purposes of the Special Management Areas are\u2014\n**(1)**\nto conserve, protect, and enhance the ecological, scenic, wildlife, recreational, cultural, historic, educational, and scientific resources of the Special Management Areas for the benefit and enjoyment of present and future generations;\n**(2)**\nto promote biodiversity and control invasive species; and\n**(3)**\nto allow for the continuation of restoration efforts and scientific study of the designated natural areas and designated research natural areas within the Special Management Areas.\n#### 5. Administration of Special Management Areas\n##### (a) In general\nThe Secretary shall administer the Special Management Areas\u2014\n**(1)**\nin a manner that conserves, protects, and enhances the purposes for which the Special Management Areas are established; and\n**(2)**\nin accordance with\u2014\n**(A)**\nthis section; and\n**(B)**\nother applicable laws.\n##### (b) Management plan\nNot later than 3 years after the date of enactment of this Act, the Secretary shall develop a comprehensive management plan for the long-term protection and management of the Special Management Areas.\n##### (c) Uses\n**(1) In general**\nThe Secretary shall allow only uses of the Special Management Areas that are consistent with the purposes for which the Special Management Areas are established.\n**(2) Prescribed fire**\nThe Secretary may use prescribed fire to sustain the ecological structure and composition of the Special Management Areas to sustain the biodiversity of the Special Management Areas.\n**(3) Management tools**\n**(A) In general**\nThe Secretary may use herbicides, insecticides, and mechanized equipment in the control of fire, insects, disease, and invasive species, including the use of chainsaws, drones, aircraft, pickup trucks, all-terrain vehicles, and rubber and tracked vehicles to carry out management of the Special Management Areas approved by the Secretary.\n**(B) Requirement**\nIn carrying out management of the Special Management Areas, the Secretary shall use the best available technology and science.\n**(4) Motorized vehicles**\nExcept in cases in which motorized vehicles are needed for administrative purposes, emergency response, or access on established roads accessing trailheads, or are essential to provide off-road access for ecosystem management of habitat, the use of motor vehicles in the Special Management Areas shall be prohibited.\n**(5) Roads**\nThe Secretary shall decommission and remove roads within the Special Management Areas, except roads needed for management or access to trailheads, as soon as practicable.\n**(6) Timber**\n**(A) In general**\nCommercial timber harvesting, except as needed for fire, insect, and disease control, and for visitor and administrative safety, in the Special Management Areas shall be prohibited.\n**(B) Activities permitted**\nThinning of trees and other vegetation in the Special Management Areas shall be permitted for restoration of the designated natural areas and designated research natural areas and to further the management objectives described in this section.\n**(7) Inholdings**\n**(A) In general**\nAccess to private inholdings in the Special Management Areas shall be preserved.\n**(B) Acquisitions**\nThe Secretary shall acquire any private inholdings in the Special Management Areas by purchase or exchange as soon as feasible.\n**(8) Hunting and trapping**\n**(A) Hunting**\nHunting shall be permitted in the Special Management Areas as permitted by the State of Illinois and in accordance with regulations of the State of Illinois and regulations of the Forest Service.\n**(B) Trapping**\nTrapping shall not be permitted in the Special Management Areas.\n**(C) Access by motorized vehicles**\nAccess within the Special Management Areas by hunters in motorized vehicles shall be prohibited.\n**(9) Volunteer restoration and research**\n**(A) Volunteers**\nThe Secretary shall allow organized groups of volunteers to participate in ecological restoration activities under the guidance of Forest Service ecologists and botanists within the Special Management Areas through cooperative agreements.\n**(B) Access for research purposes**\nThe Secretary shall allow access to the Special Management Areas for scientific research by qualified individuals and organizations, as determined by the Secretary.\n**(10) Ongoing management decisions**\nThe Supervisor of the Shawnee National Forest shall have the authority, without requiring the permission of the Secretary, to make management decisions concerning any designated natural area or designated research natural area within the Special Management Areas pursuant to the land and resource management plan for the Shawnee National Forest.\n##### (d) Withdrawal\nSubject to valid existing rights, all Federal land within the Special Management Areas, including any land or interest in land that is acquired by the United States within the Special Management Areas after the date of enactment of this Act, is withdrawn from\u2014\n**(1)**\nentry, appropriation, or disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\noperation of the mineral leasing, mineral materials, and geothermal leasing laws.\n##### (e) Maps and legal descriptions\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file a map and legal description of each Special Management Area with\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Natural Resources of the House of Representatives.\n**(2) Effect**\nThe maps and legal descriptions filed under paragraph (1) shall have the same force and effect as if included in this Act, except that the Secretary may correct clerical and typographical errors in the maps and legal descriptions.\n**(3) Availability**\nThe maps and legal descriptions filed under paragraph (1) shall be on file and available for public inspection in the appropriate office of the Secretary and on the Forest Service website.\n##### (f) Public information\nAnnually, the Secretary shall make publicly available on the website of the Shawnee National Forest information describing the progress in achieving the management objectives described in this section.",
      "versionDate": "2025-10-27",
      "versionType": "Reported in Senate"
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
            "name": "Forests, forestry, trees",
            "updateDate": "2026-01-07T16:57:27Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2026-01-07T16:57:40Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-01-07T16:57:57Z"
          },
          {
            "name": "Illinois",
            "updateDate": "2026-01-07T16:57:23Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-01-07T16:57:45Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-01-07T16:57:36Z"
          },
          {
            "name": "Pest management",
            "updateDate": "2026-01-07T16:57:50Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2026-01-07T16:57:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-18T16:18:44Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2548is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2548rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Shawnee National Forest Conservation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-29T10:58:14Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Shawnee National Forest Conservation Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-29T06:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Shawnee National Forest Conservation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to designate the Camp Hutchins Wilderness and establish Special Management Areas in the Shawnee National Forest in the State of Illinois, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:45Z"
    }
  ]
}
```
