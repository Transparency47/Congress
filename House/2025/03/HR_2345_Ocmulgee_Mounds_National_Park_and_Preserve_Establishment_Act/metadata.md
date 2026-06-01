# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2345?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2345
- Title: Ocmulgee Mounds National Park and Preserve Establishment Act
- Congress: 119
- Bill type: HR
- Bill number: 2345
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2025-12-10T06:45:10Z
- Update date including text: 2025-12-10T06:45:10Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2345",
    "number": "2345",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "S001189",
        "district": "8",
        "firstName": "Austin",
        "fullName": "Rep. Scott, Austin [R-GA-8]",
        "lastName": "Scott",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Ocmulgee Mounds National Park and Preserve Establishment Act",
    "type": "HR",
    "updateDate": "2025-12-10T06:45:10Z",
    "updateDateIncludingText": "2025-12-10T06:45:10Z"
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
          "date": "2025-03-25T14:05:10Z",
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2345ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2345\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Austin Scott of Georgia (for himself, Mr. Bishop , Mr. Carter of Georgia , Mrs. McBath , Mr. McCormick , Mr. David Scott of Georgia , Ms. Williams of Georgia , Mr. Allen , Mr. Loudermilk , Mr. Jack , Mr. Johnson of Georgia , Ms. Greene of Georgia , and Mr. Collins ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo establish the Ocmulgee Mounds National Park and Preserve in the State of Georgia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ocmulgee Mounds National Park and Preserve Establishment Act .\n#### 2. Definitions\nIn this Act:\n**(1) Advisory Council**\nThe term Advisory Council means the Ocmulgee Mounds National Park and Preserve Advisory Council established under section 5(a).\n**(2) Map**\nThe term Map means the map entitled Ocmulgee Mounds National Park and Preserve Proposed Boundary , numbered 363/193026, and dated September 2024.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(4) State**\nThe term State means the State of Georgia.\n**(5) Tribe**\nThe term Tribe means the Muscogee (Creek) Nation.\n#### 3. Redesignation of Ocmulgee Mounds National Park and establishment of Ocmulgee Mounds National Preserve\n##### (a) Redesignation of Ocmulgee Mounds National Park; land acquisition\n**(1) In general**\nThe Ocmulgee Mounds National Historical Park designated by section 2102(b)(1)(A) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( 16 U.S.C. 410yyy\u20133(b)(1)(A) ) shall be known and designated as the Ocmulgee Mounds National Park .\n**(2) References**\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the Ocmulgee Mounds National Historical Park shall be considered to be a reference to the Ocmulgee Mounds National Park .\n**(3) Land acquisition for Ocmulgee Mounds National Park**\n**(A) In general**\nThe Secretary may acquire land or any interest in land within the area depicted as National Park Area on the Map for inclusion in the Ocmulgee Mounds National Park by purchase from a willing seller, donation, or exchange.\n**(B) Administration**\nAny land or interest in land acquired under subparagraph (A) shall be\u2014\n**(i)**\nincorporated into the Ocmulgee Mounds National Park; and\n**(ii)**\nadministered by the Secretary in accordance with section 4.\n**(C) Prohibition on use of eminent domain**\nNothing in this paragraph authorizes the use of eminent domain to acquire land or an interest in land.\n##### (b) Establishment of Ocmulgee Mounds National Preserve\n**(1) In general**\nEffective on the date on which the Secretary publishes in the Federal Register a notice that the Secretary has determined that sufficient land within the area depicted as National Preserve Area on the Map has been acquired under paragraph (2) to constitute a manageable unit, there is established the Ocmulgee Mounds National Preserve in the State as a unit of the National Park System.\n**(2) Land acquisition for Ocmulgee Mounds National Preserve**\n**(A) In general**\nThe Secretary may acquire land or any interest in land within the area depicted as National Preserve Area on the Map for inclusion in the Ocmulgee Mounds National Preserve by purchase from a willing seller, donation, or exchange.\n**(B) Administration**\nAny land or interest in land acquired under subparagraph (A) shall be\u2014\n**(i)**\nincorporated into the Ocmulgee Mounds National Preserve; and\n**(ii)**\nadministered by the Secretary in accordance with section 4.\n**(C) Prohibition on use of eminent domain**\nNothing in this paragraph authorizes the use of eminent domain to acquire land or an interest in land.\n**(3) Boundaries**\nThe boundaries of the Ocmulgee Mounds National Preserve shall reflect the land and interests in land acquired for the Ocmulgee Mounds National Preserve under paragraph (2)(A).\n##### (c) Map\n**(1) Corrections**\nThe Secretary may make technical corrections to the Map.\n**(2) Availability**\nThe Map shall be on file and available for public inspection in the appropriate offices of the National Park Service.\n#### 4. Administration of Ocmulgee Mounds National Park and Preserve\n##### (a) In general\nThe Ocmulgee Mounds National Park and the Ocmulgee Mounds National Preserve shall\u2014\n**(1)**\nbe administered as a single unit of the National Park System in accordance with\u2014\n**(A)**\nthis section;\n**(B)**\nthe laws generally applicable to units of the National Park System, including\u2014\n**(i)**\nsection 100101(a), chapter 1003, and sections 100751(a), 100752, 100753, and 102101 of title 54, United States Code; and\n**(ii)**\nchapter 3201 of title 54, United States Code; and\n**(C)**\nany management plan developed under subsection (b); and\n**(2)**\ncollectively be known and designated as the Ocmulgee Mounds National Park and Preserve .\n##### (b) Management plan\n**(1) In general**\nNot later than 3 years after the date of enactment of this Act, the Secretary, in consultation with the Advisory Council, shall develop a general management plan for the preservation and use of the Ocmulgee Mounds National Park and Preserve in accordance with section 100502 of title 54, United States Code.\n**(2) Cultural resources and landscapes**\nThe general management plan developed under paragraph (1) shall provide for\u2014\n**(A)**\nthe interpretation and preservation of cultural resources of the Ocmulgee Mounds National Park and Preserve, including burial grounds and other sites that are sacred to the Tribe; and\n**(B)**\nan inventory of important cultural landscapes, including flora, that should be preserved, managed, developed, and maintained because of the cultural, natural, and public use significance of the cultural landscapes, including to the Tribe.\n##### (c) Hunting and fishing\n**(1) Hunting**\nThe Secretary shall allow hunting on land under the jurisdiction of the Secretary within the boundaries of the Ocmulgee Mounds National Preserve in accordance with applicable Federal and State laws.\n**(2) Fishing**\nThe Secretary shall allow fishing on waters under the jurisdiction of the Secretary within the boundaries of the Ocmulgee Mounds National Park and Preserve in accordance with applicable Federal and State laws.\n**(3) Limitation**\nThe Secretary may designate zones in which, and establish periods during which, no hunting, fishing, or both, shall be allowed for reasons of public safety, administration, fish or wildlife management, or emergencies.\n**(4) Consultation**\nThe Secretary shall ensure any regulations prescribing such restrictions under this subsection shall be put into effect only after consultation with the State.\n**(5) Private land**\nNothing in this subsection prohibits hunting, fishing, or trapping on private land in accordance with applicable State and Federal laws.\n**(6) Congressional intent**\nNothing in this Act is intended to affect the jurisdiction or responsibilities of the State with respect to fish and wildlife.\n##### (d) Hiring preference\nThe Secretary shall establish policies to provide a preference for hiring members of the Tribe for positions at the Ocmulgee Mounds National Park and Preserve, consistent with the Indian preference policy established by the Secretary of the Interior under section 12 of the Act of June 18, 1934 (commonly known as the Indian Reorganization Act ) (48 Stat. 986, chapter 576; 25 U.S.C. 5116 ).\n##### (e) Effect on administration of Bond swamp national wildlife refuge\n**(1) In general**\nExcept as provided in paragraph (2), nothing in this Act affects the continued administration of the Bond Swamp National Wildlife Refuge by the Director of the United States Fish and Wildlife Service as a unit of the National Wildlife Refuge System.\n**(2) Cultural interpretation activities**\nThe Director of the National Park Service shall consult with the Tribe to provide cultural programs and related activities with respect to the Bond Swamp National Wildlife Refuge with the consent of the Director of the United States Fish and Wildlife Service.\n##### (f) Tribal consultation\nNothing in this Act prevents continued consultation with federally recognized Indian Tribes pursuant to Executive Order 13175 ( 25 U.S.C. 5301 note; relating to consultation and coordination with Indian Tribal governments).\n##### (g) Military overflights\nNothing in this Act precludes\u2014\n**(1)**\nlow-level overflights of military aircraft over the Ocmulgee Mounds National Park and Preserve;\n**(2)**\nthe designation of new units of special use airspace over the Ocmulgee Mounds National Park and Preserve; or\n**(3)**\nthe use or establishment of military flight training routes over the Ocmulgee Mounds National Park and Preserve.\n##### (h) Sacred and cultural sites\nThe Secretary shall ensure the protection of sacred sites and cultural sites within the Ocmulgee Mounds National Park and Preserve and provide access to the sites by members of Indian Tribes who have ancestral connections to the Ocmulgee River Corridor, in accordance with Public Law 95\u2013341 (commonly known as the American Indian Religious Freedom Act ) ( 42 U.S.C. 1996 et seq. ) and Executive Order 13007 ( 42 U.S.C. 1996 note; relating to Indian sacred sites).\n#### 5. Advisory council\n##### (a) Establishment\nThe Secretary shall establish an advisory council, to be known as the Ocmulgee Mounds National Park and Preserve Advisory Council .\n##### (b) Duties\nThe Advisory Council shall\u2014\n**(1)**\nadvise the Secretary with respect to the development and implementation of the management plan for the Ocmulgee Mounds National Park and Preserve; and\n**(2)**\nnot later than 3 years after the date of enactment of this Act, submit to the Secretary recommendations regarding how the Secretary would consider and accommodate Tribal interests in the management of the Ocmulgee Mounds National Park and Preserve, including recommendations regarding how the Secretary and the Tribe may collaborate with respect to land management, species management, and the interpretation of cultural resources and resources of the Tribe at the Ocmulgee Mounds National Park and Preserve.\n##### (c) Members\nThe Advisory Council shall consist of 7 members, to be appointed by the Secretary, as follows:\n**(1)**\n1 member, who shall be a representative of the applicable National Park Service office.\n**(2)**\n1 member, who shall be a representative of the applicable United States Fish and Wildlife Service office.\n**(3)**\n3 members, who shall be representatives of the Tribe.\n**(4)**\n1 member, who shall be a representative of the State Department of Natural Resources.\n**(5)**\n1 member, who shall be appointed after considering recommendations from the Middle Georgia Regional Commission.\n##### (d) Applicable law\nThe Advisory Council shall be subject to chapter 10 of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act ) (other than section 1013 of that title), and other applicable laws.\n##### (e) Vacancy\nA vacancy on the Advisory Council shall be filled in the same manner as the original appointment.\n##### (f) Quorum\nA majority of the members of the Advisory Council (including not fewer than 1 member who is a designated representative of the Tribe) shall constitute a quorum.\n##### (g) Frequency of meetings\nThe Advisory Council shall meet 2 times per year, or more often as the Chairperson of the Advisory Council determines to be appropriate.\n##### (h) Chairperson\nThe Advisory Council shall\u2014\n**(1)**\nelect a chairperson of the Advisory Council from among the members of the Advisory Council; and\n**(2)**\nestablish any rules and procedures for the Advisory Council that the Advisory Council determines to be appropriate.\n##### (i) No compensation\nMembers of the Advisory Council shall serve without compensation.\n#### 6. Land to be held in trust\nAll right, title, and interest of the United States in and to the approximately 126 acres of land owned in fee by the Tribe are hereby taken into trust for the benefit of the Tribe. Such land\u2014\n**(1)**\nis part of Indian country (as defined in section 1151 of title 18, United States Code) of the Tribe; and\n**(2)**\nshall be administered in accordance with the laws and regulations generally applicable to property held in trust by the United States for the benefit of an Indian Tribe.\n#### 7. Authorization of appropriations\nThere are authorized to be appropriated such sums as are necessary to carry out this Act.",
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
        "actionDate": "2025-03-25",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "1131",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ocmulgee Mounds National Park and Preserve Establishment Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-21T15:16:03Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2345ih.xml"
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
      "title": "Ocmulgee Mounds National Park and Preserve Establishment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ocmulgee Mounds National Park and Preserve Establishment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Ocmulgee Mounds National Park and Preserve in the State of Georgia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:39Z"
    }
  ]
}
```
