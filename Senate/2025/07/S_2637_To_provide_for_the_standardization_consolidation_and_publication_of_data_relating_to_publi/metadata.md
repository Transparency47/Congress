# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2637?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2637
- Title: MAPWaters Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2637
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2026-04-07T12:58:03Z
- Update date including text: 2026-04-07T12:58:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S5001)
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S5001)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2637",
    "number": "2637",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "MAPWaters Act of 2025",
    "type": "S",
    "updateDate": "2026-04-07T12:58:03Z",
    "updateDateIncludingText": "2026-04-07T12:58:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S5001)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T23:36:29Z",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-31",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2637is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2637\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Barrasso (for himself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo provide for the standardization, consolidation, and publication of data relating to public outdoor recreational use of Federal waterways among Federal land and water management agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modernizing Access to our Public Waters Act of 2025 or the MAPWaters Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Federal fishing restriction**\nThe term Federal fishing restriction means a defined area in which all or certain fishing activities are temporarily or permanently prohibited or restricted by a Federal land or water management agency.\n**(2) Federal land or water management agency**\nThe term Federal land or water management agency means\u2014\n**(A)**\nthe Bureau of Reclamation;\n**(B)**\nthe National Park Service;\n**(C)**\nthe Bureau of Land Management;\n**(D)**\nthe United States Fish and Wildlife Service; and\n**(E)**\nthe Forest Service.\n**(3) Federal waterway**\nThe term Federal waterway means waters managed by 1 or more of the relevant Secretaries.\n**(4) Federal waterway restriction**\nThe term Federal waterway restriction means a restriction on the access or use of a Federal waterway applied under applicable law by 1 or more of the Secretaries.\n**(5) Secretaries**\nThe term Secretaries means\u2014\n**(A)**\nthe Secretary of Agriculture, acting through the Chief of the Forest Service; and\n**(B)**\nthe Secretary of the Interior.\n**(6) State**\nThe term State means each of the several States, the District of Columbia, and each territory of the United States.\n#### 3. Interagency data standardization\nNot later than 30 months after the date of enactment of this Act, the Secretaries, in coordination with the Federal Geographic Data Committee established by section 753(a) of the FAA Reauthorization Act of 2018 ( 43 U.S.C. 2802(a) ), shall jointly develop and adopt interagency standards to ensure compatibility and interoperability among applicable Federal databases with respect to the collection and dissemination of geospatial data relating to public outdoor recreational access of Federal waterways and Federal fishing restrictions.\n#### 4. Data consolidation and publication\n##### (a) Federal waterway restrictions\nNot later than 5 years after the date of enactment of this Act, each of the Secretaries, to the maximum extent practicable, shall digitize and make publicly available online, as applicable, geographic information system data that includes, with respect to Federal waterway restrictions\u2014\n**(1)**\nstatus information with respect to the conditions under which Federal waterways are open or closed to entry or watercraft, including watercraft inspection, decontamination requirements, low-elevation aircraft, or diving;\n**(2)**\nthe dates on which Federal waterways are seasonally closed to entry or watercraft;\n**(3)**\nthe areas of Federal waterways with restrictions on motorized propulsion, horsepower, or fuel type;\n**(4)**\nthe areas of Federal waterways with anchoring restrictions, no wake zones, exclusion zones, danger areas, or vessel speed restrictions;\n**(5)**\nFederal waterway restrictions on the direction of travel, including upstream or downstream travel; and\n**(6)**\nthe uses, including by watercraft, that are restricted on each area of a Federal waterway, including the permissibility of\u2014\n**(A)**\ncanoes and other paddlecraft;\n**(B)**\nrafts and driftboats;\n**(C)**\nmotorboats;\n**(D)**\npersonal watercraft;\n**(E)**\nairboats;\n**(F)**\namphibious aircraft;\n**(G)**\nhovercraft;\n**(H)**\noversnow vehicles and other motorized vehicles on frozen bodies of water;\n**(I)**\noceangoing ships;\n**(J)**\nswimming; and\n**(K)**\nother applicable recreational activities, as determined to be appropriate by the Secretaries.\n##### (b) Federal waterway access and navigation information\nNot later than 5 years after the date of enactment of this Act, each of the Secretaries, to the maximum extent practicable, shall digitize and make publicly available online, as applicable, geographic information system data that includes, with respect to Federal waterway access and navigation information\u2014\n**(1)**\n**(A)**\nthe location of boat ramps, portages, and fishing access sites under the authority of the Federal land or water management agency; and\n**(B)**\nthe identification of the dates on which the facilities and sites identified under subparagraph (A) are open or closed, as applicable; and\n**(2)**\nbathymetric information and depth charts, as feasible.\n##### (c) Federal fishing restrictions\nNot later than 5 years after the date of enactment of this Act, each of the Secretaries, to the maximum extent practicable, shall digitize and make publicly available online geographic information system data that describes, with respect to Federal fishing restrictions\u2014\n**(1)**\nthe location and geographic boundaries of Federal fishing restrictions on recreational and commercial fishing, including\u2014\n**(A)**\nfull or partial closures;\n**(B)**\nno-take zones; and\n**(C)**\nFederal fishing restrictions within or surrounding marine protected areas;\n**(2)**\nFederal fishing restrictions on the use of specific types of equipment or bait; and\n**(3)**\nFederal requirements with respect to catch and release.\n##### (d) Public comment\nThe Secretaries shall develop a process to allow members of the public to submit questions or comments regarding the information described in subsections (a) and (b).\n##### (e) Updates\nThe Secretaries, to the maximum extent practicable, shall update\u2014\n**(1)**\nthe data described in subsections (a) and (b) not less frequently than 2 times per year; and\n**(2)**\nthe data described in subsection (c) in real time as changes go into effect.\n##### (f) Exclusion\nThis section shall not apply to irrigation canals and flowage easements.\n##### (g) Disclosure\nAny geographic information system data made publicly available under this section shall not disclose information regarding the nature, location, character, or ownership of historic, paleontological, or archaeological resources, consistent with applicable law.\n#### 5. Cooperation and coordination\n##### (a) Community partners and third-Party providers\nFor purposes of carrying out this Act, the Secretaries may\u2014\n**(1)**\ncoordinate and partner with non-Federal agencies and private sector and nonprofit partners, including\u2014\n**(A)**\nState natural resource agencies;\n**(B)**\nTribal natural resource agencies;\n**(C)**\ntechnology companies;\n**(D)**\ngeospatial data companies; and\n**(E)**\nexperts in data science, analytics, and operations research; and\n**(2)**\nenter into an agreement with a third party to carry out any provision of this Act.\n##### (b) United states geological survey\nThe Secretaries may work with the Director of the United States Geological Survey to collect, aggregate, digitize, standardize, and publish data on behalf of the Secretaries to meet the requirements of this Act.\n##### (c) Requirement\nWith respect to data developed and distributed under this Act, the Secretaries shall\u2014\n**(1)**\ndevelop the data in accordance with applicable Federal, State, and Tribal laws (including regulations); and\n**(2)**\ninclude a notice that any geospatial data are subject to applicable Federal, State, and Tribal laws (including regulations).\n##### (d) Existing efforts\nTo the extent practicable, the Secretary concerned shall use or incorporate existing applicable data, maps, and resources in carrying out this Act, including data, maps, and resources developed and published under\u2014\n**(1)**\nthe Modernizing Access to Our Public Land Act ( 16 U.S.C. 6851 et seq. );\n**(2)**\nsection 103 of division DD of the Consolidated Appropriations Act, 2023 ( 43 U.S.C. 776 ); or\n**(3)**\nother applicable law.\n#### 6. Reports\nNot later than 1 year after the date of enactment of this Act and annually thereafter through March 30, 2034, the Secretaries shall submit a report that describes the progress made by the Secretaries with respect to meeting the requirements of this Act to\u2014\n**(1)**\nthe Committee on Natural Resources of the House of Representatives;\n**(2)**\nthe Committee on Energy and Commerce of the House of Representatives;\n**(3)**\nthe Committee on Agriculture of the House of Representatives;\n**(4)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(5)**\nthe Committee on Agriculture, Nutrition, and Forestry of the Senate.\n#### 7. Effect\nNothing in this Act\u2014\n**(1)**\nmodifies or alters the definition of the term navigable waters under Federal law;\n**(2)**\naffects the jurisdiction or authority of State or Federal agencies to regulate navigable waters;\n**(3)**\nmodifies or alters the authority or jurisdiction of Federal or State agencies to manage fisheries; or\n**(4)**\nauthorizes or is intended to result in a change in the accessibility of waters open to hunting, fishing, or other forms of outdoor recreation as of the date of the enactment of this Act.",
      "versionDate": "2025-07-31",
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
        "actionDate": "2025-12-26",
        "text": "Became Public Law No: 119-62."
      },
      "number": "187",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MAPWaters Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-18T16:18:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-31",
    "originChamber": "Senate",
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
          "measure-id": "id119s2637",
          "measure-number": "2637",
          "measure-type": "s",
          "orig-publish-date": "2025-07-31",
          "originChamber": "SENATE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2637v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-07-31",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Modernizing Access to our Public Waters Act or the MAPWaters Act of 2025 or the MAPWaters Act of 2025</strong></p><p>This bill directs the Forest Service and the Department of the Interior to standardize and publish data relating to public's access to\u00a0federal waterways for recreational use.</p><p>Specifically, the Forest Service and Interior must jointly develop and adopt interagency standards for data collection and dissemination of geospatial data relating to public outdoor recreational access of federal waterways and federal fishing restrictions. The standards must ensure compatibility and interoperability among applicable federal databases with respect to collection and dissemination of such data.</p><p>Within five years, the Forest Service and Interior must also digitize and make publicly available online certain geographic information system data about (1) federal waterway restrictions, (2) federal waterway access and navigation information, and (3) federal fishing restrictions. They must also update the data about waterway restrictions, waterway access, and navigation information at least twice per year. Data about fishing restrictions must be updated in real time as changes go into effect. </p><p>Finally, the\u00a0Forest Service and Interior\u00a0must develop a process to allow members of the public to submit questions or comments regarding the data regarding waterway restrictions,\u00a0waterway access, and navigation information.</p>"
        },
        "title": "MAPWaters Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2637.xml",
    "summary": {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Modernizing Access to our Public Waters Act or the MAPWaters Act of 2025 or the MAPWaters Act of 2025</strong></p><p>This bill directs the Forest Service and the Department of the Interior to standardize and publish data relating to public's access to\u00a0federal waterways for recreational use.</p><p>Specifically, the Forest Service and Interior must jointly develop and adopt interagency standards for data collection and dissemination of geospatial data relating to public outdoor recreational access of federal waterways and federal fishing restrictions. The standards must ensure compatibility and interoperability among applicable federal databases with respect to collection and dissemination of such data.</p><p>Within five years, the Forest Service and Interior must also digitize and make publicly available online certain geographic information system data about (1) federal waterway restrictions, (2) federal waterway access and navigation information, and (3) federal fishing restrictions. They must also update the data about waterway restrictions, waterway access, and navigation information at least twice per year. Data about fishing restrictions must be updated in real time as changes go into effect. </p><p>Finally, the\u00a0Forest Service and Interior\u00a0must develop a process to allow members of the public to submit questions or comments regarding the data regarding waterway restrictions,\u00a0waterway access, and navigation information.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s2637"
    },
    "title": "MAPWaters Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Modernizing Access to our Public Waters Act or the MAPWaters Act of 2025 or the MAPWaters Act of 2025</strong></p><p>This bill directs the Forest Service and the Department of the Interior to standardize and publish data relating to public's access to\u00a0federal waterways for recreational use.</p><p>Specifically, the Forest Service and Interior must jointly develop and adopt interagency standards for data collection and dissemination of geospatial data relating to public outdoor recreational access of federal waterways and federal fishing restrictions. The standards must ensure compatibility and interoperability among applicable federal databases with respect to collection and dissemination of such data.</p><p>Within five years, the Forest Service and Interior must also digitize and make publicly available online certain geographic information system data about (1) federal waterway restrictions, (2) federal waterway access and navigation information, and (3) federal fishing restrictions. They must also update the data about waterway restrictions, waterway access, and navigation information at least twice per year. Data about fishing restrictions must be updated in real time as changes go into effect. </p><p>Finally, the\u00a0Forest Service and Interior\u00a0must develop a process to allow members of the public to submit questions or comments regarding the data regarding waterway restrictions,\u00a0waterway access, and navigation information.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s2637"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2637is.xml"
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
      "title": "MAPWaters Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MAPWaters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Modernizing Access to our Public Waters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the standardization, consolidation, and publication of data relating to public outdoor recreational use of Federal waterways among Federal land and water management agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:26Z"
    }
  ]
}
```
