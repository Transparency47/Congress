# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/703?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/703
- Title: CATCH Fentanyl Act
- Congress: 119
- Bill type: S
- Bill number: 703
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2025-09-16T23:09:23Z
- Update date including text: 2025-09-16T23:09:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/703",
    "number": "703",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "CATCH Fentanyl Act",
    "type": "S",
    "updateDate": "2025-09-16T23:09:23Z",
    "updateDateIncludingText": "2025-09-16T23:09:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T16:14:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NH"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "OK"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "WV"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "AZ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NM"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NM"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "OH"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NC"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "WV"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TN"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s703is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 703\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Cornyn (for himself, Ms. Hassan , Mr. Lankford , Mr. Justice , Mr. Kelly , Mr. Heinrich , Mr. Luj\u00e1n , Mr. Moreno , Mr. Tillis , Mrs. Capito , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo establish a pilot program to assess the use of technology to speed up and enhance the cargo inspection process at land ports of entry along the border.\n#### 1. Short titles\nThis Act may be cited as the Contraband Awareness Technology Catches Harmful Fentanyl Act or the CATCH Fentanyl Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate ; and\n**(B)**\nthe Committee on Homeland Security of the House of Representatives .\n**(2) Artificial intelligence; AI**\nThe terms artificial intelligence and AI have the meaning given the term artificial intelligence in section 238(g) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. 4061 note).\n**(3) CBP innovation team**\nThe term CBP Innovation Team means the U.S. Customs and Border Protection Innovation Team within the Office of the Commissioner.\n**(4) Nonintrusive inspection technology; NII technology**\nThe terms nonintrusive inspection technology and NII technology means technical equipment and machines, such as X-ray or gamma-ray imaging equipment, that allow cargo inspections without the need to open the means of transport and unload the cargo.\n**(5) Pilot projects**\nThe term pilot projects means the projects required under section 3(a) for testing and assessing the use of technologies to improve the inspection process at land ports of entry.\n**(6) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n#### 3. Pilot projects allowing additional technology providers to participate in inspecting cars, trucks, and cargo containers at certain ports of entry\n##### (a) Establishment\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary, acting through CBP Innovation Team, and in coordination with the Office of Field Operations and the Department of Homeland Security Science and Technology Directorate, shall begin the implementation of pilot projects for testing and assessing the use of technologies or technology enhancements to improve the process for inspecting, including by increasing efficiencies of such inspections, any conveyance or mode of transportation at land ports of entry along the borders of the United States. The technologies or technology enhancements tested and assessed under the pilot projects shall be for the purpose of assisting U.S. Customs and Border Protection personnel to detect contraband, illegal drugs, illegal weapons, human smuggling, and threats on inbound and outbound traffic, in conjunction with the use of imaging equipment, radiation portal monitors, and chemical detectors.\n**(2) Requirements**\n**(A) In general**\nIn implementing the pilot projects at ports of entry, the CBP Innovation Team, in coordination with the Department of Homeland Security Science and Technology Directorate, shall test and collect data regarding not fewer than 5 types of nonintrusive inspection technology enhancements that can be deployed at land ports of entry. The CBP Innovation Team shall test technology enhancements from at least 1 of the following categories:\n**(i)**\nArtificial intelligence.\n**(ii)**\nMachine learning.\n**(iii)**\nHigh-performance computing.\n**(iv)**\nQuantum information sciences, including quantum sensing.\n**(v)**\nOther emerging technologies.\n**(B) Identification of effective enhancements**\nThe pilot projects shall identify the most effective types of technology enhancements to improve the capabilities of nonintrusive inspection systems and other inspection systems used at land ports of entry based on\u2014\n**(i)**\nthe technology enhancement's ability to assist U.S. Customs and Border Protection accurately detect contraband, illegal drugs, illegal weapons, human smuggling, or threats in inbound and outbound traffic;\n**(ii)**\nthe technology enhancement's ability to increase efficiencies of inspections to assist U.S. Customs and Border Protection address long wait times;\n**(iii)**\nthe technology enhancement's ability to improve capabilities of aging detection equipment and infrastructure at land ports of entry;\n**(iv)**\nthe technology enhancement\u2019s safety relative to As Low As Reasonably Achievable (ALARA) standard practices;\n**(v)**\nthe ability to integrate the new technology into the existing workflow and infrastructure;\n**(vi)**\nthe technology enhancement\u2019s ability to incorporate automatic threat recognition technology using standard formats and open architecture;\n**(vii)**\nthe mobility of technology enhancements; and\n**(viii)**\nother performance measures identified by the CBP Innovation Team.\n**(C) Private sector involvement**\nThe CBP Innovation Team may solicit input from representatives of the private sector regarding commercially viable technologies.\n**(D) Cost effectiveness requirement**\nIn identifying the most effective types of technology enhancements under subparagraph (B), the pilot projects shall prioritize solutions that demonstrate the highest cost-effectiveness in achievement the objectives described in clauses (i) through (ix) of subparagraph (B). Cost effectiveness shall account for improved detection capabilities, increased inspection efficiencies, reduced wait times, and total cost of implementation (including infrastructure upgrades and maintenance expenses).\n**(3) Nonintrusive inspection systems program**\nThe CBP Innovation Team shall work with existing nonintrusive inspection systems programs within U.S. Customs and Border Protection when planning and developing the pilot projects required under paragraph (1).\n**(4) Data privacy protections**\nIn implementing the pilot projects and utilizing new technologies, the Secretary shall safeguard the privacy and security of personal data collected during inspections through appropriate measures, including\u2014\n**(A)**\nadherence to relevant privacy laws and regulations;\n**(B)**\nimplementation of data anonymization techniques, if applicable; and\n**(C)**\nregular audits to assess compliance with data privacy standards.\n**(5) Science and technology directorate**\nThe CBP Innovation Team shall work with the Department of Homeland Security Science and Technology Directorate to align existing nonintrusive inspection research and development efforts within the Science and Technology Directorate when planning and developing pilot projects required under paragraph (1).\n##### (b) Termination\nThe pilot projects shall terminate on the date that is 5 years after the date of the enactment of this Act.\n##### (c) Reports required\nNot later than 3 years after the date of the enactment of this Act, and 180 days after the termination of the pilot projects pursuant to subsection (b), the Secretary shall submit a report to the appropriate congressional committees that contains\u2014\n**(1)**\nan analysis of the effectiveness of technology enhancements tested based on the requirements described in subsection (a)(2);\n**(2)**\nany recommendations from the testing and analysis concerning the ability to utilize such technologies at all land ports of entry;\n**(3)**\na plan to utilize new technologies that meet the performance goals of the pilot projects across all U.S. Customs and Border Protection land ports of entry at the border, including total costs and a breakdown of the costs of such plan, including any infrastructure improvements that may be required to accommodate recommended technology enhancements;\n**(4)**\na comprehensive list of existing technologies owned and utilized by U.S. Customs and Border protection for cargo and vehicle inspection, including\u2014\n**(A)**\ndetails on the implementation status of such technologies, such as whether the technologies have been fully installed and utilized, or whether there are challenges with the installation and utilization of the technology;\n**(B)**\nan evaluation of the compatibility, interoperability, and scalability of existing cargo and vehicle inspection technologies within U.S. Customs and Border Protection\u2019s physical and information technology infrastructure; and\n**(C)**\nidentification of any obstacles to the effective deployment and integration of such technologies; and\n**(5)**\nthe analysis described in subsection (d).\n##### (d) Areas of analysis\nThe report required under subsection (c) shall include an analysis containing\u2014\n**(1)**\nquantitative measurements of performance based on the requirements described in subsection (a)(2) of each technology tested compared with the status quo to reveal a broad picture of the performance of technologies and technology enhancements, such as\u2014\n**(A)**\nthe probability of detection, false alarm rate, and throughput; and\n**(B)**\nan analysis determining whether such observed performance represents a significant increase, decrease, or no change compared with current systems;\n**(2)**\nan assessment of the relative merits of each such technology;\n**(3)**\nany descriptive trends and patterns observed; and\n**(4)**\nperformance measures for\u2014\n**(A)**\nthe technology enhancement's ability to assist with the detection of contraband on inbound and outbound traffic through automated (primary) inspection by measuring and reporting the probability of detection and false alarm rate for each NII system under operational conditions;\n**(B)**\nthe throughput of cargo through each NII system with a technology enhancement, including a breakdown of the time needed for U.S. Customs and Border Protection\u2014\n**(i)**\nto complete the image review process and clear low-risk shipments; and\n**(ii)**\nto complete additional inspections of high-risk items;\n**(C)**\nchanges in U.S. Customs and Border Protection officer time commitments and personnel needs to sustain high volume NII scanning operations when technology enhancements are utilized; and\n**(D)**\noperational costs, including\u2014\n**(i)**\nestimated implementation costs for each NII system with technology enhancements; and\n**(ii)**\nestimated cost savings due to improved efficiency due to technology enhancements, if applicable.\n##### (e) Privacy and civil liberties reports\nThe Secretary, in consultation with the CBP Innovation Team and other appropriate offices\u2014\n**(1)**\nprior to the implementation of the technologies referred to in this section, shall submit\u2014\n**(A)**\na report or reports to the appropriate congressional committees regarding the potential privacy, civil liberties, and civil rights impacts of technologies being tested under the pilot projects pursuant to this section, including an analysis of the impacts of the technology enhancements on individuals crossing the United States border; and\n**(B)**\nrecommendations for mitigation measures to address any identified impacts; and\n**(2)**\nnot later than 180 days after the termination of the pilot projects pursuant to subsection (b), shall submit a report to the appropriate congressional committees containing\u2014\n**(A)**\nfindings on the impacts to privacy, civil rights, and civil liberties resulting from the pilot projects;\n**(B)**\nrecommendations for mitigating these impacts in implementation of approved technologies; and\n**(C)**\nany additional recommendations based on the lessons learned from the pilot projects.\n#### 4. Prohibition on new appropriations\nNo additional funds are authorized to be appropriated to carry out this Act.",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-08-15",
        "text": "Placed on the Union Calendar, Calendar No. 187."
      },
      "number": "1569",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CATCH Fentanyl Act",
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
        "name": "Immigration",
        "updateDate": "2025-03-21T13:55:12Z"
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s703is.xml"
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
      "title": "CATCH Fentanyl Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CATCH Fentanyl Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Contraband Awareness Technology Catches Harmful Fentanyl Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a pilot program to assess the use of technology to speed up and enhance the cargo inspection process at land ports of entry along the border.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:25Z"
    }
  ]
}
```
