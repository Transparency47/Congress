# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1569?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1569
- Title: CATCH Fentanyl Act
- Congress: 119
- Bill type: HR
- Bill number: 1569
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2026-02-04T04:11:39Z
- Update date including text: 2026-02-04T04:11:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-25 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2025-04-09 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-09 - Committee: Ordered to be Reported by Voice Vote.
- 2025-04-09 - Committee: Subcommittee on Border Security and Enforcement Discharged
- 2025-08-15 - Calendars: Placed on the Union Calendar, Calendar No. 187.
- 2025-08-15 - Committee: Reported by the Committee on Homeland Security. H. Rept. 119-229.
- 2025-08-15 - Committee: Reported by the Committee on Homeland Security. H. Rept. 119-229.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-25 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2025-04-09 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-09 - Committee: Ordered to be Reported by Voice Vote.
- 2025-04-09 - Committee: Subcommittee on Border Security and Enforcement Discharged
- 2025-08-15 - Calendars: Placed on the Union Calendar, Calendar No. 187.
- 2025-08-15 - Committee: Reported by the Committee on Homeland Security. H. Rept. 119-229.
- 2025-08-15 - Committee: Reported by the Committee on Homeland Security. H. Rept. 119-229.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1569",
    "number": "1569",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "H001077",
        "district": "3",
        "firstName": "Clay",
        "fullName": "Rep. Higgins, Clay [R-LA-3]",
        "lastName": "Higgins",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "CATCH Fentanyl Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:11:39Z",
    "updateDateIncludingText": "2026-02-04T04:11:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-08-15",
      "calendarNumber": {
        "calendar": "U00187"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 187.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-08-15",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported by the Committee on Homeland Security. H. Rept. 119-229.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-08-15",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported by the Committee on Homeland Security. H. Rept. 119-229.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee on Border Security and Enforcement Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
            "date": "2025-08-15T16:44:14Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-09T13:28:51Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-09T13:19:39Z",
            "name": "Discharged from"
          },
          {
            "date": "2025-02-25T15:00:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-25T18:20:56Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "RI"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "FL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TN"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NC"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "LA"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "CO"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MN"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "WA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MS"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "PA"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NJ"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "CA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NY"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NC"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1569ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1569\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mr. Higgins of Louisiana (for himself, Mr. Magaziner , Mr. Gimenez , Mr. Goldman of New York , Mr. Green of Tennessee , Mr. Haridopolos , Mr. Davis of North Carolina , Mr. Fields , Mr. Evans of Colorado , Mr. Riley of New York , and Ms. Craig ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo establish a pilot program to assess the use of technology to speed up and enhance the cargo inspection process at land ports of entry along the border.\n#### 1. Short titles\nThis Act may be cited as the Contraband Awareness Technology Catches Harmful Fentanyl Act or the CATCH Fentanyl Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate ; and\n**(B)**\nthe Committee on Homeland Security of the House of Representatives .\n**(2) Artificial intelligence; AI**\nThe terms artificial intelligence and AI have the meaning given the term artificial intelligence in section 238(g) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. 4061 note).\n**(3) CBP innovation team**\nThe term CBP Innovation Team means the U.S. Customs and Border Protection Innovation Team within the Office of the Commissioner.\n**(4) Nonintrusive inspection technology; NII technology**\nThe terms nonintrusive inspection technology and NII technology means technical equipment and machines, such as X-ray or gamma-ray imaging equipment, that allow cargo inspections without the need to open the means of transport and unload the cargo.\n**(5) Pilot projects**\nThe term pilot projects means the projects required under section 3(a) for testing and assessing the use of technologies to improve the inspection process at land ports of entry.\n#### 3. Pilot projects allowing additional technology providers to participate in inspecting cars, trucks, and cargo containers at certain ports of entry\n##### (a) Establishment\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Homeland Security, acting through CBP Innovation Team, and in coordination with the Office of Field Operations and the Department of Homeland Security Science and Technology Directorate, shall begin the implementation of pilot projects for testing and assessing the use of technologies or technology enhancements to improve the process for inspecting, including by increasing efficiencies of such inspections, any conveyance or mode of transportation at land ports of entry along the borders of the United States. The technologies or technology enhancements tested and assessed under the pilot projects shall be for the purpose of assisting U.S. Customs and Border Protection personnel to detect contraband, illegal drugs, illegal weapons, human smuggling, and threats on inbound and outbound traffic, in conjunction with the use of imaging equipment, radiation portal monitors, and chemical detectors.\n**(2) Requirements**\n**(A) In general**\nIn implementing the pilot projects at ports of entry, the CBP Innovation Team, in coordination with the Department of Homeland Security Science and Technology Directorate, shall test and collect data regarding not fewer than 5 types of nonintrusive inspection technology enhancements that can be deployed at land ports of entry. The CBP Innovation Team shall test technology enhancements from not fewer than 1 of the following categories:\n**(i)**\nArtificial intelligence.\n**(ii)**\nMachine learning.\n**(iii)**\nHigh-performance computing.\n**(iv)**\nQuantum information sciences, including quantum sensing.\n**(v)**\nOther emerging technologies.\n**(B) Identification of effective enhancements**\nThe pilot projects shall identify the most effective types of technology enhancements to improve the capabilities of nonintrusive inspection systems and other inspection systems used at land ports of entry based on\u2014\n**(i)**\nthe technology enhancement's ability to assist U.S. Customs and Border Protection accurately detect contraband, illegal drugs, illegal weapons, human smuggling, or threats in inbound and outbound traffic;\n**(ii)**\nthe technology enhancement's ability to increase efficiencies of inspections to assist U.S. Customs and Border Protection address long wait times;\n**(iii)**\nthe technology enhancement's ability to improve capabilities of aging detection equipment and infrastructure at land ports of entry;\n**(iv)**\nthe technology enhancement\u2019s safety relative to As Low As Reasonably Achievable (ALARA) standard practices;\n**(v)**\nthe ability to integrate the new technology into the existing workflow and infrastructure;\n**(vi)**\nthe technology enhancement\u2019s ability to incorporate automatic threat recognition technology using standard formats and open architecture;\n**(vii)**\nthe mobility of technology enhancements; and\n**(viii)**\nother performance measures identified by the CBP Innovation Team.\n**(C) Private sector involvement**\nThe CBP Innovation Team may solicit input from representatives of the private sector regarding commercially viable technologies.\n**(D) Cost effectiveness requirement**\nIn identifying the most effective types of technology enhancements under subparagraph (B), the pilot projects shall prioritize solutions that demonstrate the highest cost-effectiveness in achievement the objectives described in clauses (i) through (ix) of subparagraph (B). Cost effectiveness shall account for improved detection capabilities, increased inspection efficiencies, reduced wait times, and total cost of implementation (including infrastructure upgrades and maintenance expenses).\n**(3) Nonintrusive inspection systems program**\nThe CBP Innovation Team shall work with existing nonintrusive inspection systems programs within U.S. Customs and Border Protection when planning and developing the pilot projects required under paragraph (1).\n**(4) Data privacy protections**\nIn implementing the pilot projects and utilizing new technologies, the Secretary of Homeland Security shall safeguard the privacy and security of personal data collected during inspections through appropriate measures, including\u2014\n**(A)**\nadherence to relevant privacy laws and regulations;\n**(B)**\nimplementation of data anonymization techniques, if applicable; and\n**(C)**\nregular audits to assess compliance with data privacy standards.\n**(5) Science and technology directorate**\nThe CBP Innovation Team shall work with the Department of Homeland Security Science and Technology Directorate to align existing nonintrusive inspection research and development efforts within the Science and Technology Directorate when planning and developing pilot projects required under paragraph (1).\n##### (b) Termination\nThe pilot projects shall terminate on the date that is 5 years after the date of the enactment of this Act.\n##### (c) Reports required\nNot later than 3 years after the date of the enactment of this Act, and 180 days after the termination of the pilot projects pursuant to subsection (b), the Secretary of Homeland Security shall submit a report to the appropriate congressional committees that contains\u2014\n**(1)**\nan analysis of the effectiveness of technology enhancements tested based on the requirements described in subsection (a)(2);\n**(2)**\nany recommendations from the testing and analysis concerning the ability to utilize such technologies at all land ports of entry;\n**(3)**\na plan to utilize new technologies that meet the performance goals of the pilot projects across all U.S. Customs and Border Protection land ports of entry at the border, including total costs and a breakdown of the costs of such plan, including any infrastructure improvements that may be required to accommodate recommended technology enhancements;\n**(4)**\na comprehensive list of existing technologies owned and utilized by U.S. Customs and Border protection for cargo and vehicle inspection, including\u2014\n**(A)**\ndetails on the implementation status of such technologies, such as whether the technologies have been fully installed and utilized, or whether there are challenges with the installation and utilization of the technology;\n**(B)**\nan evaluation of the compatibility, interoperability, and scalability of existing cargo and vehicle inspection technologies within U.S. Customs and Border Protection\u2019s physical and information technology infrastructure; and\n**(C)**\nidentification of any obstacles to the effective deployment and integration of such technologies; and\n**(5)**\nthe analysis described in subsection (d).\n##### (d) Areas of analysis\nThe report required under subsection (c) shall include an analysis containing\u2014\n**(1)**\nquantitative measurements of performance based on the requirements described in subsection (a)(2) of each technology tested compared with the status quo to reveal a broad picture of the performance of technologies and technology enhancements, such as\u2014\n**(A)**\nthe probability of detection, false alarm rate, and throughput; and\n**(B)**\nan analysis determining whether such observed performance represents a significant increase, decrease, or no change compared with current systems;\n**(2)**\nan assessment of the relative merits of each such technology;\n**(3)**\nany descriptive trends and patterns observed; and\n**(4)**\nperformance measures for\u2014\n**(A)**\nthe technology enhancement's ability to assist with the detection of contraband on inbound and outbound traffic through automated (primary) inspection by measuring and reporting the probability of detection and false alarm rate for each NII system under operational conditions;\n**(B)**\nthe throughput of cargo through each NII system with a technology enhancement, including a breakdown of the time needed for U.S. Customs and Border Protection\u2014\n**(i)**\nto complete the image review process and clear low-risk shipments; and\n**(ii)**\nto complete additional inspections of high-risk items;\n**(C)**\nchanges in U.S. Customs and Border Protection officer time commitments and personnel needs to sustain high volume NII scanning operations when technology enhancements are utilized; and\n**(D)**\noperational costs, including\u2014\n**(i)**\nestimated implementation costs for each NII system with technology enhancements; and\n**(ii)**\nestimated cost savings due to improved efficiency due to technology enhancements, if applicable.\n##### (e) Privacy and civil liberties reports\nThe Secretary of Homeland Security, in consultation with the CBP Innovation Team and other appropriate offices, shall\u2014\n**(1)**\nprior to the implementation of these technologies, submit\u2014\n**(A)**\na report or reports to the appropriate congressional committees regarding the potential privacy, civil liberties, and civil rights impacts of technologies being tested under the pilot projects pursuant to this section, including an analysis of the impacts of the technology enhancements on individuals crossing the United States border; and\n**(B)**\nrecommendations for mitigation measures to address any identified impacts; and\n**(2)**\nnot later than 180 days after the termination of the pilot projects pursuant to subsection (b), submit a report to the appropriate congressional committees containing\u2014\n**(A)**\nfindings on the impacts to privacy, civil rights, and civil liberties resulting from the pilot projects;\n**(B)**\nrecommendations for mitigating these impacts in implementation of approved technologies; and\n**(C)**\nany additional recommendations based on the lessons learned from the pilot projects.\n##### (f) Prohibition on new appropriations\nNo additional funds are authorized to be appropriated to carry out this Act.",
      "versionDate": "2025-02-25",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1569rh.xml",
      "text": "IB\nUnion Calendar No. 187\n119th CONGRESS\n1st Session\nH. R. 1569\n[Report No. 119\u2013229]\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mr. Higgins of Louisiana (for himself, Mr. Magaziner , Mr. Gimenez , Mr. Goldman of New York , Mr. Green of Tennessee , Mr. Haridopolos , Mr. Davis of North Carolina , Mr. Fields , Mr. Evans of Colorado , Mr. Riley of New York , and Ms. Craig ) introduced the following bill; which was referred to the Committee on Homeland Security\nAugust 15, 2025 Additional sponsors: Mr. Garcia of California , Mr. Baumgartner , Mr. Guest , Mr. Goldman of Texas , Mr. Meuser , Mr. Moskowitz , Mr. Gottheimer , Mr. Calvert , Ms. Tenney , Mr. McDowell , and Ms. Bynum\nAugust 15, 2025 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo establish a pilot program to assess the use of technology to speed up and enhance the cargo inspection process at land ports of entry along the border.\n#### 1. Short titles\nThis Act may be cited as the Contraband Awareness Technology Catches Harmful Fentanyl Act or the CATCH Fentanyl Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate ; and\n**(B)**\nthe Committee on Homeland Security of the House of Representatives .\n**(2) Artificial intelligence; AI**\nThe terms artificial intelligence and AI have the meaning given the term artificial intelligence in section 238(g) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. 4061 note).\n**(3) CBP innovation team**\nThe term CBP Innovation Team means the U.S. Customs and Border Protection Innovation Team within the Office of the Commissioner.\n**(4) Nonintrusive inspection technology; NII technology**\nThe terms nonintrusive inspection technology and NII technology means technical equipment and machines, such as X-ray or gamma-ray imaging equipment, that allow cargo inspections without the need to open the means of transport and unload the cargo.\n**(5) Pilot projects**\nThe term pilot projects means the projects required under section 3(a) for testing and assessing the use of technologies to improve the inspection process at land ports of entry.\n#### 3. Pilot projects allowing additional technology providers to participate in inspecting cars, trucks, and cargo containers at certain ports of entry\n##### (a) Establishment\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Homeland Security, acting through CBP Innovation Team, and in coordination with the Office of Field Operations and the Department of Homeland Security Science and Technology Directorate, shall begin the implementation of pilot projects for testing and assessing the use of technologies or technology enhancements to improve the process for inspecting, including by increasing efficiencies of such inspections, any conveyance or mode of transportation at land ports of entry along the borders of the United States. The technologies or technology enhancements tested and assessed under the pilot projects shall be for the purpose of assisting U.S. Customs and Border Protection personnel to detect contraband, illegal drugs, illegal weapons, human smuggling, and threats on inbound and outbound traffic, in conjunction with the use of imaging equipment, radiation portal monitors, and chemical detectors.\n**(2) Requirements**\n**(A) In general**\nIn implementing the pilot projects at ports of entry, the CBP Innovation Team, in coordination with the Department of Homeland Security Science and Technology Directorate, shall test and collect data regarding not fewer than 5 types of nonintrusive inspection technology enhancements that can be deployed at land ports of entry. The CBP Innovation Team shall test technology enhancements from not fewer than 1 of the following categories:\n**(i)**\nArtificial intelligence.\n**(ii)**\nMachine learning.\n**(iii)**\nHigh-performance computing.\n**(iv)**\nQuantum information sciences, including quantum sensing.\n**(v)**\nOther emerging technologies.\n**(B) Identification of effective enhancements**\nThe pilot projects shall identify the most effective types of technology enhancements to improve the capabilities of nonintrusive inspection systems and other inspection systems used at land ports of entry based on\u2014\n**(i)**\nthe technology enhancement's ability to assist U.S. Customs and Border Protection accurately detect contraband, illegal drugs, illegal weapons, human smuggling, or threats in inbound and outbound traffic;\n**(ii)**\nthe technology enhancement's ability to increase efficiencies of inspections to assist U.S. Customs and Border Protection address long wait times;\n**(iii)**\nthe technology enhancement's ability to improve capabilities of aging detection equipment and infrastructure at land ports of entry;\n**(iv)**\nthe technology enhancement\u2019s safety relative to As Low As Reasonably Achievable (ALARA) standard practices;\n**(v)**\nthe ability to integrate the new technology into the existing workflow and infrastructure;\n**(vi)**\nthe technology enhancement\u2019s ability to incorporate automatic threat recognition technology using standard formats and open architecture;\n**(vii)**\nthe mobility of technology enhancements; and\n**(viii)**\nother performance measures identified by the CBP Innovation Team.\n**(C) Private sector involvement**\nThe CBP Innovation Team may solicit input from representatives of the private sector regarding commercially viable technologies.\n**(D) Cost effectiveness requirement**\nIn identifying the most effective types of technology enhancements under subparagraph (B), the pilot projects shall prioritize solutions that demonstrate the highest cost-effectiveness in achievement the objectives described in clauses (i) through (ix) of subparagraph (B). Cost effectiveness shall account for improved detection capabilities, increased inspection efficiencies, reduced wait times, and total cost of implementation (including infrastructure upgrades and maintenance expenses).\n**(3) Nonintrusive inspection systems program**\nThe CBP Innovation Team shall work with existing nonintrusive inspection systems programs within U.S. Customs and Border Protection when planning and developing the pilot projects required under paragraph (1).\n**(4) Data privacy protections**\nIn implementing the pilot projects and utilizing new technologies, the Secretary of Homeland Security shall safeguard the privacy and security of personal data collected during inspections through appropriate measures, including\u2014\n**(A)**\nadherence to relevant privacy laws and regulations;\n**(B)**\nimplementation of data anonymization techniques, if applicable; and\n**(C)**\nregular audits to assess compliance with data privacy standards.\n**(5) Science and technology directorate**\nThe CBP Innovation Team shall work with the Department of Homeland Security Science and Technology Directorate to align existing nonintrusive inspection research and development efforts within the Science and Technology Directorate when planning and developing pilot projects required under paragraph (1).\n##### (b) Termination\nThe pilot projects shall terminate on the date that is 5 years after the date of the enactment of this Act.\n##### (c) Reports required\nNot later than 3 years after the date of the enactment of this Act, and 180 days after the termination of the pilot projects pursuant to subsection (b), the Secretary of Homeland Security shall submit a report to the appropriate congressional committees that contains\u2014\n**(1)**\nan analysis of the effectiveness of technology enhancements tested based on the requirements described in subsection (a)(2);\n**(2)**\nany recommendations from the testing and analysis concerning the ability to utilize such technologies at all land ports of entry;\n**(3)**\na plan to utilize new technologies that meet the performance goals of the pilot projects across all U.S. Customs and Border Protection land ports of entry at the border, including total costs and a breakdown of the costs of such plan, including any infrastructure improvements that may be required to accommodate recommended technology enhancements;\n**(4)**\na comprehensive list of existing technologies owned and utilized by U.S. Customs and Border protection for cargo and vehicle inspection, including\u2014\n**(A)**\ndetails on the implementation status of such technologies, such as whether the technologies have been fully installed and utilized, or whether there are challenges with the installation and utilization of the technology;\n**(B)**\nan evaluation of the compatibility, interoperability, and scalability of existing cargo and vehicle inspection technologies within U.S. Customs and Border Protection\u2019s physical and information technology infrastructure; and\n**(C)**\nidentification of any obstacles to the effective deployment and integration of such technologies; and\n**(5)**\nthe analysis described in subsection (d).\n##### (d) Areas of analysis\nThe report required under subsection (c) shall include an analysis containing\u2014\n**(1)**\nquantitative measurements of performance based on the requirements described in subsection (a)(2) of each technology tested compared with the status quo to reveal a broad picture of the performance of technologies and technology enhancements, such as\u2014\n**(A)**\nthe probability of detection, false alarm rate, and throughput; and\n**(B)**\nan analysis determining whether such observed performance represents a significant increase, decrease, or no change compared with current systems;\n**(2)**\nan assessment of the relative merits of each such technology;\n**(3)**\nany descriptive trends and patterns observed; and\n**(4)**\nperformance measures for\u2014\n**(A)**\nthe technology enhancement's ability to assist with the detection of contraband on inbound and outbound traffic through automated (primary) inspection by measuring and reporting the probability of detection and false alarm rate for each NII system under operational conditions;\n**(B)**\nthe throughput of cargo through each NII system with a technology enhancement, including a breakdown of the time needed for U.S. Customs and Border Protection\u2014\n**(i)**\nto complete the image review process and clear low-risk shipments; and\n**(ii)**\nto complete additional inspections of high-risk items;\n**(C)**\nchanges in U.S. Customs and Border Protection officer time commitments and personnel needs to sustain high volume NII scanning operations when technology enhancements are utilized; and\n**(D)**\noperational costs, including\u2014\n**(i)**\nestimated implementation costs for each NII system with technology enhancements; and\n**(ii)**\nestimated cost savings due to improved efficiency due to technology enhancements, if applicable.\n##### (e) Privacy and civil liberties reports\nThe Secretary of Homeland Security, in consultation with the CBP Innovation Team and other appropriate offices, shall\u2014\n**(1)**\nprior to the implementation of these technologies, submit\u2014\n**(A)**\na report or reports to the appropriate congressional committees regarding the potential privacy, civil liberties, and civil rights impacts of technologies being tested under the pilot projects pursuant to this section, including an analysis of the impacts of the technology enhancements on individuals crossing the United States border; and\n**(B)**\nrecommendations for mitigation measures to address any identified impacts; and\n**(2)**\nnot later than 180 days after the termination of the pilot projects pursuant to subsection (b), submit a report to the appropriate congressional committees containing\u2014\n**(A)**\nfindings on the impacts to privacy, civil rights, and civil liberties resulting from the pilot projects;\n**(B)**\nrecommendations for mitigating these impacts in implementation of approved technologies; and\n**(C)**\nany additional recommendations based on the lessons learned from the pilot projects.\n##### (f) Prohibition on new appropriations\nNo additional funds are authorized to be appropriated to carry out this Act.",
      "versionDate": "2025-08-15",
      "versionType": "Reported in House"
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
        "actionDate": "2025-02-25",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "703",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CATCH Fentanyl Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-04-23T13:43:22Z"
          },
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-04-23T13:43:22Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-04-23T13:43:22Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-23T13:43:22Z"
          },
          {
            "name": "Customs enforcement",
            "updateDate": "2025-04-23T13:43:22Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-04-23T13:43:22Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-04-23T13:43:22Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-04-23T13:43:22Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-04-23T13:43:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-03-21T14:35:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119hr1569",
          "measure-number": "1569",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-25",
          "originChamber": "HOUSE",
          "update-date": "2025-06-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1569v00",
            "update-date": "2025-06-11"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Contraband Awareness Technology Catches Harmful Fentanyl Act or the CATCH Fentanyl Act\u00a0</strong></p><p>This bill establishes a pilot program for improving the inspection of conveyances or modes of transportation at land ports of entry along U.S. borders\u00a0to detect contraband, illegal drugs, illegal weapons, human smuggling, and threats. Specifically, the U.S. Customs and Border Protection Innovation Team must test technology in at least one of the categories of artificial intelligence, machine learning, high-performance computing, quantum information sciences, or other emerging technologies.\u00a0The team must also test and collect data regarding at least five types of enhancements to nonintrusive inspection technology (e.g., X-ray machines) able to be deployed at land ports of entry.</p>"
        },
        "title": "CATCH Fentanyl Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1569.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Contraband Awareness Technology Catches Harmful Fentanyl Act or the CATCH Fentanyl Act\u00a0</strong></p><p>This bill establishes a pilot program for improving the inspection of conveyances or modes of transportation at land ports of entry along U.S. borders\u00a0to detect contraband, illegal drugs, illegal weapons, human smuggling, and threats. Specifically, the U.S. Customs and Border Protection Innovation Team must test technology in at least one of the categories of artificial intelligence, machine learning, high-performance computing, quantum information sciences, or other emerging technologies.\u00a0The team must also test and collect data regarding at least five types of enhancements to nonintrusive inspection technology (e.g., X-ray machines) able to be deployed at land ports of entry.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hr1569"
    },
    "title": "CATCH Fentanyl Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Contraband Awareness Technology Catches Harmful Fentanyl Act or the CATCH Fentanyl Act\u00a0</strong></p><p>This bill establishes a pilot program for improving the inspection of conveyances or modes of transportation at land ports of entry along U.S. borders\u00a0to detect contraband, illegal drugs, illegal weapons, human smuggling, and threats. Specifically, the U.S. Customs and Border Protection Innovation Team must test technology in at least one of the categories of artificial intelligence, machine learning, high-performance computing, quantum information sciences, or other emerging technologies.\u00a0The team must also test and collect data regarding at least five types of enhancements to nonintrusive inspection technology (e.g., X-ray machines) able to be deployed at land ports of entry.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hr1569"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1569ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1569rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "CATCH Fentanyl Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-08-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Contraband Awareness Technology Catches Harmful Fentanyl Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-08-16T03:38:18Z"
    },
    {
      "title": "CATCH Fentanyl Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:09Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CATCH Fentanyl Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Contraband Awareness Technology Catches Harmful Fentanyl Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a pilot program to assess the use of technology to speed up and enhance the cargo inspection process at land ports of entry along the border.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T07:18:27Z"
    }
  ]
}
```
