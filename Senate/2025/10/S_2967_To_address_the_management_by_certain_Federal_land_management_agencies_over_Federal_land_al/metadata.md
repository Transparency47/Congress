# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2967?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2967
- Title: Border Lands Conservation Act
- Congress: 119
- Bill type: S
- Bill number: 2967
- Origin chamber: Senate
- Introduced date: 2025-10-02
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-02: Introduced in Senate
- 2025-10-02 - IntroReferral: Introduced in Senate
- 2025-10-02 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-10-22 - Floor: Star Print ordered on the bill.
- Latest action: 2025-10-02: Introduced in Senate

## Actions

- 2025-10-02 - IntroReferral: Introduced in Senate
- 2025-10-02 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-10-22 - Floor: Star Print ordered on the bill.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-02",
    "latestAction": {
      "actionDate": "2025-10-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2967",
    "number": "2967",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Border Lands Conservation Act",
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
      "actionDate": "2025-10-22",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the bill.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-02",
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
      "actionDate": "2025-10-02",
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
          "date": "2025-10-02T16:46:14Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-10-02",
      "state": "TN"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-10-02",
      "state": "WY"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-02",
      "state": "WY"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-10-02",
      "state": "MS"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-02",
      "state": "FL"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "AR"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-10-15",
      "state": "TX"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2967is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2967\nIN THE SENATE OF THE UNITED STATES\nOctober 2, 2025 Mr. Lee (for himself, Mrs. Blackburn , Mr. Barrasso , Ms. Lummis , Mrs. Hyde-Smith , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo address the management by certain Federal land management agencies over Federal land along the southern border and northern border, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Border Lands Conservation Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Natural Resources of the House of Representatives; and\n**(B)**\nthe Committee on Energy and Natural Resources of the Senate.\n**(2) Border state**\nThe term Border State means a State that abuts the southern border or northern border.\n**(3) Covered federal land**\n**(A) In general**\nThe term covered Federal land means land\u2014\n**(i)**\nowned by the United States;\n**(ii)**\nlocated in a unit, or in a portion of a unit, or within 1 or more parcels of land that shares an exterior boundary with the southern border or northern border; and\n**(iii)**\nadministered by a Federal land management agency.\n**(B) Exclusion**\nThe term covered Federal land does not include Federal land held in trust for Indian Tribes.\n**(4) Federal land management agency**\nThe term Federal land management agency has the meaning given the term in section 802 of the Federal Lands Recreation Enhancement Act ( 16 U.S.C. 6801 ).\n**(5) Initiative**\nThe term Initiative means the Border Fuels Management Initiative established under section 8(a).\n**(6) Northern border**\nThe term northern border means the international border between the United States and Canada.\n**(7) Operational control**\nThe term operational control has the meaning given the term in section 2(b) of the Secure Fence Act of 2006 ( 8 U.S.C. 1701 note; Public Law 109\u2013367 ).\n**(8) Secretaries**\nThe term Secretaries means the Secretary of the Interior and the Secretary of Agriculture.\n**(9) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of the Interior, with respect to covered Federal land under the jurisdiction of the Secretary of the Interior; and\n**(B)**\nthe Secretary of Agriculture, acting through the Chief of the Forest Service, with respect to National Forest System land.\n**(10) Southern border**\nThe term southern border means the international border between the United States and Mexico.\n**(11) Tactical infrastructure**\nThe term tactical infrastructure means infrastructure for the detection of illegal southern border and northern border crossings, including observation points, remote video surveillance systems, motion sensors, vehicle barriers, fences, roads, bridges, drainage, and detection devices.\n#### 3. Navigable road infrastructure along covered Federal land\n##### (a) In general\nThe Secretaries, in consultation with the Secretary of Homeland Security, shall inventory existing roads and install navigable roads on covered Federal land\u2014\n**(1)**\nto deter illegal southern border and northern border crossings;\n**(2)**\nto gain operational control of the southern border and northern border; and\n**(3)**\nto increase Department of Homeland Security access to covered Federal land.\n##### (b) Administration\nThe Secretaries shall\u2014\n**(1)**\nadminister and maintain the roads installed under subsection (a); and\n**(2)**\nensure access to the roads installed under subsection (a) by the Department of Defense, Department of Homeland Security, local law enforcement, emergency personnel, and any other personnel that the Secretary concerned determines to be necessary to carry out the purposes described in that subsection.\n##### (c) Cooperative agreements\nThe Secretaries shall enter into cooperative agreements with the Secretary of Homeland Security\u2014\n**(1)**\nto install technology on covered Federal land that the Secretaries, in consultation with the Secretary of Homeland Security, determine to be necessary to deter illegal entry into the United States; and\n**(2)**\nto gain operational control of the southern border and northern border.\n#### 4. Access to wilderness areas\nSection 4(d) of the Wilderness Act ( 16 U.S.C. 1133(d) ) is amended by adding at the end the following:\n(8) Notwithstanding any other provision of this Act, the Secretary of Homeland Security may conduct the following activities within a wilderness area for the purpose of securing the international land borders of the United States: (A) Access structures, installations, and roads. (B) Execute search and rescue operations. (C) Use motor vehicles, motorboats, and motorized equipment. (D) Conduct patrols on foot and on horseback. (E) Notwithstanding any other law, including regulations, relating specifically to the use of aircraft in a wilderness area or in the airspace above a wilderness area, use aircraft, including approach, landing, and takeoff. (F) Deploy tactical infrastructure (as defined in section 2 of the Border Lands Conservation Act ) and technology. (G) Construct and maintain roads and physical barriers. .\n#### 5. Search and rescue operations\nThe Secretary of the Interior or the Secretary of Agriculture may not impede, prohibit, or restrict activities of the Department of Homeland Security on covered Federal land located within 100 miles of the southern border or northern border\u2014\n**(1)**\nto execute search and rescue operations; or\n**(2)**\nto prevent unlawful entries into the United States, including entries through the southern border or northern border\u2014\n**(A)**\nby terrorists and other unlawful aliens; and\n**(B)**\nof instruments of terrorism, narcotics, and other contraband.\n#### 6. Interagency cooperative agreement\nThe Secretary concerned shall enter into a cooperative agreement with the Secretary of Homeland Security to fulfill the commitments under\u2014\n**(1)**\nthe memorandum of understanding entitled Memorandum of Understanding Among U.S. Department of Homeland Security and U.S. Department of the Interior and U.S. Department of Agriculture Regarding Cooperative National Security and Counterterrorism Efforts on Federal Lands along the United States\u2019 Borders and signed March 2006; or\n**(2)**\nany successor to the memorandum of understanding described in paragraph (1).\n#### 7. Inventory of roads and trails on covered Federal land harmed by illegal aliens\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary concerned shall inventory all previously unauthorized roads and trails on covered Federal land that have been created by illegal southern border or northern border crossings.\n##### (b) Determination required\nNot later than 2 years after the date on which the inventory is completed under subsection (a), the Secretary concerned shall determine whether each previously unauthorized road or trail inventoried under that subsection has been damaged in such a manner that\u2014\n**(1)**\nthe applicable road or trail has permanently altered the original characteristics of the applicable covered Federal land; and\n**(2)**\nsignificant environmental degradation to the applicable road or trail has been identified.\n##### (c) Maintenance and administration\nIf the Secretary concerned makes an affirmative determination under subsection (b) with respect to a previously unauthorized road or trail inventoried under subsection (a), the Secretary concerned shall enter into a cooperative agreement with the Secretary of Homeland Security to use and maintain the applicable road or trail\u2014\n**(1)**\nto deter illegal entry into the United States; and\n**(2)**\nto gain operational control of the southern border or northern border, as applicable.\n#### 8. Establishment of the Border Fuels Management Initiative\n##### (a) Establishment\nNot later than 1 year after the date of enactment of this Act, the Secretaries shall establish a program, to be known as the Border Fuels Management Initiative .\n##### (b) Activities\nIn carrying out the Initiative, the Secretaries shall\u2014\n**(1)**\nreduce hazardous fuels on covered Federal land;\n**(2)**\naddress invasive or nonnative species along the covered Federal land that contribute to wildland fire risk or decrease the efficiency of U.S. Border Patrol operations;\n**(3)**\ninstall fuel breaks along the covered Federal land;\n**(4)**\nset targets for acres to treat under the Initiative for each fiscal year; and\n**(5)**\nin coordination with the Secretary of Homeland Security, prioritize fuels management on covered Federal land on which navigable roads are installed under section 3(a).\n##### (c) Coordination\nIn carrying out the Initiative, the Secretaries shall coordinate and may enter into memoranda of understanding with the U.S. Border Patrol and State, local, and Tribal law enforcement agencies.\n#### 9. Reports on environmental degradation and wildland fires caused by illegal immigration\n##### (a) Report to Congress on covered Federal land\nNot later than 1 year after the date of enactment of this Act, the Secretary concerned shall submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\na catalog of all reported incidents of environmental degradation caused, and wildland fires ignited, by aliens without lawful immigration status on covered Federal land, including\u2014\n**(A)**\nthe number of acres burned and total number of fires ignited;\n**(B)**\na description of each incident of environmental degradation and the total number of incidents;\n**(C)**\nthe estimated cost of cleaning up or remediating the environmental degradation;\n**(D)**\n**(i)**\nthe number of aliens without lawful immigration status connected to each fire; and\n**(ii)**\nwhether the aliens without lawful immigration status were apprehended; and\n**(E)**\nthe areas in which incidents of environmental degradation occurred, including areas congressionally designated for the protection of natural resources; and\n**(2)**\na description of additional resources or authorities necessary to mitigate, avoid, or prevent wildland fires and environmental degradation on covered Federal land caused by aliens without lawful immigration status crossing the southern border or northern border.\n##### (b) Report to Congress on units of the National Park System\nNot later than 1 year after the date of enactment of this Act, the Secretary of the Interior (acting through the Director of the National Park Service) shall submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\na catalog of all reported incidents of environmental degradation and impacts on visitor safety caused by aliens without lawful immigration status at units of the National Park System, including\u2014\n**(A)**\na description of each incident relating to visitor safety and the total number of incidents;\n**(B)**\na description of each incident of environmental degradation and the total number of incidents;\n**(C)**\nthe estimated cost of cleaning up or remediating the environmental degradation;\n**(D)**\n**(i)**\nthe number of aliens without lawful immigration status connected to each incident; and\n**(ii)**\nwhether the aliens without lawful immigration status were apprehended; and\n**(E)**\nthe areas in which incidents of environmental degradation occurred; and\n**(2)**\na description of additional resources or authorities necessary to mitigate or avoid environmental degradation and impacts on visitor safety at units of the National Park System caused by aliens without lawful immigration status crossing the southern border or northern border.\n##### (c) Report to Congress on units of the National Wildlife Refuge System\nNot later than 1 year after the date of enactment of this Act, the Secretary of the Interior (acting through the Director of the United States Fish and Wildlife Service) shall submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\na catalog of all reported incidents of environmental degradation, impacts on visitor safety, and limits on access to hunting and fishing caused by or as a result of aliens without lawful immigration status at units of the National Wildlife Refuge System, including\u2014\n**(A)**\na description of each incident relating to visitor safety and the total number of incidents;\n**(B)**\na description of each incident relating to limiting access to hunting and fishing and the total number of incidents;\n**(C)**\na description of each incident of environmental degradation and the total number of incidents;\n**(D)**\nthe estimated cost of cleaning up or remediating the environmental degradation;\n**(E)**\n**(i)**\nthe number of aliens without lawful immigration status connected to each incident; and\n**(ii)**\nwhether the aliens without lawful immigration status were apprehended; and\n**(F)**\nthe areas in which incidents of environmental degradation occurred; and\n**(2)**\na description of additional resources or authorities necessary to mitigate or avoid environmental degradation, impacts on visitor safety, and limits on access to hunting and fishing at units of the National Wildlife Refuge System caused by or as a result of aliens without lawful immigration status crossing the southern border or northern border.\n##### (d) Updated report\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall update the November 2011 report entitled Arizona Border Region: Federal Agencies Could Better Utilize Law Enforcement Resources in Support of Wildland Fire Management Activities .\n**(2) Additional States considered**\nIn updating the report under paragraph (1), the Comptroller General shall include relevant information with respect to each Border State.\n##### (e) Report on impacts of illegal immigration on ranching\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall submit to the appropriate congressional committees a report that describes\u2014\n**(1)**\nthe effects of illegal immigration on the ranching and livestock industries; and\n**(2)**\nany recommendations for policies that could be implemented by the Bureau of Land Management and the Forest Service to compensate impacted grazing permit holders for such effects.\n#### 10. Prohibition on providing housing to aliens on certain Federal land\n##### (a) In general\nExcept as provided in subsection (b), no Federal funds may be used to provide housing to aliens without lawful immigration status on any land under the administrative jurisdiction of the Federal land management agencies, including through leases, contracts, or agreements.\n##### (b) Exception\nSubsection (a) shall not apply to a facility that is used primarily for the custody, detention, holding, processing, or removal of aliens without lawful immigration status.\n#### 11. Savings clause\n##### (a) Protection of legal uses\nNothing in this Act provides\u2014\n**(1)**\nauthority to restrict legal uses, such as grazing, timber harvesting, oil and gas development, mining, or recreation on covered Federal land; or\n**(2)**\nany additional authority to restrict legal access to covered Federal land.\n##### (b) Effect on State or private land\n**(1) In general**\nThis Act has no force or effect on State or private land.\n**(2) Access**\nNothing in this Act provides to the Secretaries authority over, or access to, State or private land.\n##### (c) Tribal sovereignty\nNothing in this Act supersedes, replaces, negates, or diminishes any treaties or other agreements between the United States and Indian Tribes.",
      "versionDate": "2025-10-02",
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-12-11T17:15:51Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-11T17:16:13Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-12-11T17:16:35Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-12-11T17:16:18Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2025-12-11T17:16:00Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-12-11T17:16:41Z"
          },
          {
            "name": "Pest management",
            "updateDate": "2025-12-11T17:16:04Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2025-12-11T17:15:45Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-12-11T17:15:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-01T17:43:23Z"
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
      "date": "2025-10-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2967is.xml"
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
      "title": "Border Lands Conservation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T11:18:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Border Lands Conservation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T02:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address the management by certain Federal land management agencies over Federal land along the southern border and northern border, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T02:48:22Z"
    }
  ]
}
```
