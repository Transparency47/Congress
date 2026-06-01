# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6893?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6893
- Title: Chesapeake Bay Watershed Advancement for Training, Education, Restoration, and Science (WATERS) Act
- Congress: 119
- Bill type: HR
- Bill number: 6893
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-04-30T08:06:56Z
- Update date including text: 2026-04-30T08:06:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-19 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-03-26 - Committee: Subcommittee Hearings Held
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-19 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-03-26 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6893",
    "number": "6893",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S000185",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
        "lastName": "Scott",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Chesapeake Bay Watershed Advancement for Training, Education, Restoration, and Science (WATERS) Act",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:56Z",
    "updateDateIncludingText": "2026-04-30T08:06:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
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
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:04:20Z",
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
                "date": "2026-03-26T14:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-19T14:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
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
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "VA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "VA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MD"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "DC"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "MD"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "VA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6893ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6893\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Scott of Virginia (for himself, Mr. Wittman , Mrs. Kiggans of Virginia , and Ms. Elfreth ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo reauthorize the Chesapeake Bay Office of the National Oceanic and Atmospheric Administration, and for other purposes.\n#### 1. Short Title\nThis Act may be cited as the Chesapeake Bay Watershed Advancement for Training, Education, Restoration, and Science (WATERS) Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that the National Oceanic and Atmospheric Administration\u2019s Chesapeake Bay Office should be the primary representative of the National Oceanic and Atmospheric Administration in the Chesapeake Bay watershed.\n#### 3. Reauthorization of the National Oceanic and Atmospheric Administration Chesapeake Bay Office\nSection 307 of the National Oceanic and Atmospheric Administration Authorization Act of 1992 ( 15 U.S.C. 1511d ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1) by striking (in this section and all that follows and inserting a period;\n**(B)**\nby amending paragraph (2) to read as follows:\n(2) The Office shall be headed by a Director, who\u2014 (A) shall have knowledge and experience in research or resource management efforts in the Chesapeake Bay; and (B) shall be responsible for the administration and operation of the office and the implementation of this section. ; and\n**(C)**\nby striking paragraph (3);\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2), by striking Secretary of Commerce and inserting Administrator ;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nby inserting with and represent after coordinate ;\n**(ii)**\nby striking , the Chesapeake Bay Regional Sea Grant Programs, and the Chesapeake Bay units of the National Estuarine Research Reserve System, and inserting for the Chesapeake Bay Program and that relate to the Chesapeake Bay watershed in furtherance of such Administration\u2019s coastal resource stewardship mission, ;\n**(iii)**\nin subparagraph (A)\u2014\n**(I)**\nin clauses (vi) and (vii), by striking and at the end; and\n**(II)**\nby adding at the end the following:\n(viii) coastal hazards and climate change; and (ix) education; and ; and\n**(iv)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (iii), by striking and at the end;\n**(II)**\nin clause (iv), by inserting and after the semicolon; and\n**(III)**\nby adding at the end the following:\n(v) integrated ecosystem assessments; ;\n**(C)**\nin paragraph (4)\u2014\n**(i)**\nby striking Environmental Protection Agency and inserting Chesapeake Executive Council ; and\n**(ii)**\nby inserting before the semicolon at the end the following: as appropriate to further the purposes of this section ;\n**(D)**\nby striking paragraphs (5) and (7);\n**(E)**\nby redesignating paragraph (6) as paragraph (5); and\n**(F)**\nby adding at the end the following:\n(6) perform any functions necessary to support the programs referred to in paragraph (3). ;\n**(3)**\nby striking subsections (c), (d), and (e); and\n**(4)**\nby adding at the end the following:\n(c) Program Activities (1) In general The Administrator, through the Director, shall implement the program activities authorized by this section to support the activity of the Chesapeake Executive Council and to further the purposes of this section. (2) Ensuring scientific and technical merit The Director shall\u2014 (A) establish and use an effective and transparent mechanism to ensure that projects funded under this section have undergone appropriate peer review; and (B) provide other appropriate means to determine that such projects have acceptable scientific and technical merit for the purpose of achieving maximum use of available funds and resources to benefit the Chesapeake Bay area. (3) Consultation with Chesapeake Executive Council The Director shall, in the implementation of the program activities authorized under this section, consult with the Chesapeake Executive Council, to ensure that the activities of the Office are consistent with the purposes and priorities of the Chesapeake Bay Agreement and plans developed pursuant to such agreement. (4) Integrated coastal observations (A) In general The Administrator, through the Director, may collaborate with scientific and academic institutions, State and Federal agencies, non-governmental organizations, and other constituents in the Chesapeake Bay watershed, to support an integrated observations system for the Chesapeake Bay consistent with the purposes of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3601 et seq. ). (B) Specific requirements To support the system referred to in subparagraph (A) and provide a complete set of environmental information for the Chesapeake Bay, the Director shall\u2014 (i) coordinate monitoring with Federal and State agencies in the tidal portions of the Chesapeake Bay to understand impacts of water quality on living marine resources; (ii) identify new data collection needs and deploy new technologies, as appropriate; (iii) collect and analyze the scientific information necessary for the management of living marine resources and the marine habitat associated with such resources; and (iv) organize the information described in clause (iii) into products that are useful to policy makers, resource managers, scientists, and the public. (C) Chesapeake Bay Interpretive Buoy System To further the development and implementation of the Chesapeake Bay Interpretive Buoy System and associated monitoring assets to improve weather and ecological forecasts, monitor habitat conditions for living marine resources, the Director may\u2014 (i) support the establishment and implementation of the Captain John Smith Chesapeake National Historic Trail; (ii) delineate key waypoints along the trail and provide appropriate real-time data and information for trail users; (iii) interpret data and information for use by educators and students to inspire stewardship of the Chesapeake Bay; and (iv) incorporate the observational data from the Chesapeake Bay Interpretive Buoy System into the Integrated Ocean Observing System regional observing system network. (5) Chesapeake Bay Watershed Education and Training Program (A) In general The Administrator, through the Director, may establish a Chesapeake Bay watershed education and training program. The program shall\u2014 (i) continue and expand the Chesapeake Bay watershed education programs offered by the Office immediately before the enactment of the Chesapeake Bay Watershed Advancement for Training, Education, Restoration, and Science (WATERS) Act ; (ii) improve the understanding of elementary and secondary school students and teachers of the living resources of the ecosystem of the Chesapeake Bay; (iii) provide education and career pathway internships; and (iv) meet the educational goals of the Chesapeake Bay Watershed Agreement. (B) Grant program The Director may award grants for the purposes of this paragraph. Grants awarded under this subparagraph may be used to support education and training projects that enhance understanding and assessment of a specific environmental problem in the Chesapeake Bay watershed or a goal of the Chesapeake Bay Program, or protect or restore living resources of the Chesapeake Bay watershed, including projects that\u2014 (i) provide classroom education, including the development and use of distance learning and other innovative technologies, related to the Chesapeake Bay watershed; (ii) provide meaningful watershed educational experiences in the Chesapeake Bay watershed; (iii) provide professional development for teachers related to the Chesapeake Bay watershed and the dissemination of pertinent education materials oriented to varying grade levels; (iv) demonstrate or disseminate environmental educational tools and materials related to the Chesapeake Bay watershed; (v) demonstrate field methods, practices, and techniques including assessment of environmental and ecological conditions and analysis of environmental problems; and (vi) build the capacity of school districts and their partners to deliver high quality environmental education programs. (C) Coordination The Director shall implement the education and training program in coordination with the heads of other Federal agencies, as the Director determines appropriate. (6) Coastal and Living Resources Management and Habitat Program (A) In general The Administrator, through the Director, may establish a Chesapeake Bay Coastal Living Resources Management and Habitat Program to support coordinated management, protection, characterization, and restoration of priority Chesapeake Bay habitats and living resources, including oysters, blue crabs, submerged aquatic vegetation, and economically and ecologically important fish species such as striped bass and menhaden. (B) Activities Under the Chesapeake Bay Coastal Living Resources Management and Habitat Program, the Director may carry out or enter into grants, contracts, and cooperative agreements and provide technical assistance to support\u2014 (i) native oyster research and restoration; (ii) fish and shellfish aquaculture that is carried out in accordance with a valid Federal or State permit; (iii) establishment of submerged aquatic vegetation restoration programs; (iv) the development of programs that restore, protect, and build the resilience of critical coastal habitats and communities; (v) habitat mapping, characterization, and assessment techniques necessary to identify, assess, and monitor Chesapeake Bay conditions and restoration actions; (vi) application and transfer of applied scientific research and ecosystem management tools to fisheries and habitat managers; (vii) collection, synthesis, and sharing of information to inform and influence coastal and living resource management issues; (viii) ecologically and economically important fish and shellfish research; and (ix) other activities that the director determines are appropriate to carry out the purposes of such program. (d) Delegation (1) Authority The Administrator shall delegate to the Director such authority as may be necessary to carry out this section. (2) Staff The Administrator shall delegate to the Director appropriate staff representing expertise that covers the breadth of the duties of the Office. (e) Reports (1) In general The Administrator, through the Director, shall submit a biennial report to the Congress and the Secretary of Commerce on the activities of the Office and on progress made in protecting and restoring the living resources and habitat of the Chesapeake Bay. (2) Action plan Each such report shall include an action plan for the 2-year period following submission of the report, consisting of\u2014 (A) a list of recommended research, monitoring, and data collection activities necessary to continue implementation of the strategy under subsection (b)(2); and (B) recommendations to integrate National Oceanic and Atmospheric Administration activities with the activities of the partners in the Chesapeake Bay Program to meet the commitments of the Chesapeake Bay Agreement and subsequent agreements. (f) Agreements (1) In general The Administrator, through the Director, may enter into and perform such contracts, leases, grants, or cooperative agreements as may be necessary to carry out the purposes of this Act. (2) Use of other resources For purposes related to the understanding, protection, and restoration of Chesapeake Bay, the Director may use, with consent and with or without reimbursement, the land, services, equipment, personnel, and facilities of any Department, agency, or instrumentality of the United States, or of any State, local government, Indian Tribe, or of any political subdivision thereof. (g) Definitions In this section, the following definitions apply: (1) Administrator The term Administrator means the Administrator of the National Oceanic and Atmospheric Administration. (2) Chesapeake bay agreement; Chesapeake bay ecosystem; Chesapeake bay program; Chesapeake executive council The terms Chesapeake Bay Agreement , Chesapeake Bay ecosystem , Chesapeake Bay Program , and Chesapeake Executive Council have the meanings given those terms in section 117(a) of the Federal Water Pollution Control Act ( 33 U.S.C. 1267(a) ). (3) Director The term Director means the Director of the Office. (4) Office The term Office means the Chesapeake Bay Office established under this section. .",
      "versionDate": "2025-12-18",
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
        "actionDate": "2026-02-26",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3939",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Chesapeake WATERS Act",
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
        "name": "Environmental Protection",
        "updateDate": "2026-02-02T14:47:40Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6893ih.xml"
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
      "title": "Chesapeake Bay Watershed Advancement for Training, Education, Restoration, and Science (WATERS) Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Chesapeake Bay Watershed Advancement for Training, Education, Restoration, and Science (WATERS) Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize the Chesapeake Bay Office of the National Oceanic and Atmospheric Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-29T05:18:20Z"
    }
  ]
}
```
