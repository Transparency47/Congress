# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/579?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/579
- Title: Department of Energy Quantum Leadership Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 579
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S974-977)
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S974-977)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/579",
    "number": "579",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
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
    "title": "Department of Energy Quantum Leadership Act of 2025",
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
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S974-977)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T18:11:14Z",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "MT"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AK"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s579is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 579\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Durbin (for himself, Mr. Daines , Mr. Schumer , Ms. Murkowski , Mr. Young , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the National Quantum Initiative Act to provide for a research, development, and demonstration program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Department of Energy Quantum Leadership Act of 2025 .\n#### 2. Department of Energy quantum information science research program\nSection 401 of the National Quantum Initiative Act ( 15 U.S.C. 8851 ) is amended\u2014\n**(1)**\nby striking subsection (a) and inserting the following:\n(a) In general The Secretary of Energy shall carry out a research, development, and demonstration program on quantum information science, engineering, and technology. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by inserting , engineering, and technology after science ;\n**(B)**\nin paragraph (2), by inserting , engineering, and technology after science ;\n**(C)**\nby striking paragraph (3) and inserting the following:\n(3) provide research experiences and training for additional undergraduate and graduate students in quantum information science, engineering, and technology, including in the fields specified in paragraph (4); ;\n**(D)**\nby redesignating paragraphs (3) through (5) as paragraphs (5) through (7), respectively;\n**(E)**\nby inserting after paragraph (2) the following:\n(3) operate National Quantum Information Science Research Centers under section 402 to accelerate and scale scientific and technical breakthroughs in quantum information science, engineering, and technology, and maintain state-of-the-art infrastructure for quantum researchers and industry partners; (4) conduct cooperative basic and applied research with industry, National Laboratories, institutions of higher education, and other research institutions to facilitate the development, demonstration, and commercial application of quantum information science, engineering, and technology priorities, as determined by the Secretary of Energy, including in the fields of\u2014 (A) quantum information theory; (B) quantum physics; (C) quantum computational science, including hardware and software, machine learning, and data science; (D) applied mathematics and algorithm development; (E) quantum communications and networking, including hardware and software for quantum communications and networking; (F) quantum sensing, imaging, and detection; (G) materials science and engineering; (H) quantum modeling and simulation, including molecular modeling; (I) near- and long-term application development, as determined by the Secretary of Energy; (J) quantum chemistry; (K) quantum biology; (L) superconductive and high-performance microelectronics; and (M) quantum security technologies; ;\n**(F)**\nin paragraph (6) (as so redesignated), in subparagraph (F), by striking and at the end;\n**(G)**\nin paragraph (7) (as so redesignated)\u2014\n**(i)**\nby striking and before potential ; and\n**(ii)**\nby striking the period at the end and inserting , and other relevant stakeholders, as determined by the Secretary of Energy; and ; and\n**(H)**\nby adding at the end the following:\n(8) leverage the collective body of knowledge and data, including experience and resources from existing Federal research activities and commercially available quantum computing hardware and software, to the extent practicable. ; and\n**(3)**\nby adding at the end the following:\n(c) Industry outreach In carrying out the program under subsection (a), the Secretary of Energy shall engage with the quantum technology industry and promote commercialization of applications of quantum technology relevant to the activities of the Department of Energy by\u2014 (1) educating\u2014 (A) the energy industry on near-term and commercially available quantum technologies; and (B) the quantum industry on potential energy applications; (2) accelerating the advancements of United States quantum computing, communications, networking, sensing, and security capabilities to protect and optimize the energy sector; (3) advancing relevant domestic supply chains, manufacturing capabilities, and associated simulations or modeling capabilities; (4) facilitating commercialization of quantum technologies from National Laboratories and engaging with the Quantum Economic Development Consortium and other organizations, as applicable, to transition component technologies that advance the development of a quantum supply chain; and (5) to the extent practicable, ensuring industry partner access, especially for small- and medium-sized businesses, to specialized quantum instrumentation, equipment, testbeds, and other infrastructure to design, prototype, and test novel quantum hardware and streamline user access to reduce costs and other administrative burdens. (d) High-Performance computing strategic plan (1) In general Not later than 1 year after the date of enactment of this subsection, the Secretary of Energy shall submit to Congress a 10-year strategic plan to guide Federal programs in designing, expanding, and procuring hybrid, energy-efficient high-performance computing systems capable of integrating with a diverse set of accelerators, including quantum, artificial intelligence, and machine learning accelerators, to enable the computing facilities of the Department of Energy to advance national computing resources. (2) Contents The strategic plan under paragraph (1) shall include the following: (A) A conceptual plan to leverage capabilities and infrastructure from the exascale computing program, as the Secretary of Energy determines necessary. (B) A plan to minimize disruptions to the advanced scientific computing workforce. (C) A consideration of a diversity of quantum computing modalities. (D) A plan to integrate cloud access of commercially available quantum hardware and software to complement on-premises high-performance computing systems and resources consistent with the QUEST program established under section 404. (e) Early-Stage quantum high-Performance computing research and development program (1) Definition of quantum high-performance computing In this subsection, the term quantum high-performance computing means the use of classical high-performance computing systems with quantum processing units and hybrid quantum-classical algorithms to leverage the strength of computational architectures and solve complex problems. (2) Program The Secretary of Energy shall establish an early-stage research and development program in quantum high-performance computing\u2014 (A) to inform the 10-year strategic plan described in subsection (d)(1); and (B) to build the necessary scientific computing workforce to fulfill the objectives of that plan. (3) Activities The program established under paragraph (2) shall\u2014 (A) support early-stage quantum supercomputing testbeds and prototypes; and (B) connect early-stage quantum high-performance computing projects to the Centers funded under this Act. (4) Funding Of funds made available under subsection (i)(1), the Secretary of Energy shall use not more than $20,000,000 for each of fiscal years 2026 through 2030 to carry out the activities under this subsection. (f) Supply chain study Not later than 1 year after the date of enactment of this subsection, the Secretary of Energy, in consultation with the Secretary of Commerce, shall conduct a study on quantum science, engineering, and technology supply chain needs, including\u2014 (1) identifying hurdles to growth in the quantum industry by leveraging the expertise of relevant stakeholders in academia and industry, including the Quantum Economic Development Consortium; and (2) making recommendations on how to strengthen the domestic supply of materials and technologies necessary for the development of a robust manufacturing base and workforce. (g) Traineeship program (1) In general The Secretary of Energy shall establish a university-led traineeship program\u2014 (A) to address workforce development needs in quantum information science, engineering, and technology; and (B) that will focus on supporting increased participation, workforce development, and research experiences for underrepresented undergraduate and graduate students. (2) Funding Of funds made available under subsection (i)(1), the Secretary of Energy shall use not more than $5,000,000 for each of fiscal years 2026 through 2030 to carry out the activities under this subsection. (h) Coordination of activities In carrying out this section, the Secretary of Energy shall, to the maximum extent practicable, coordinate with the Director of the National Science Foundation, the Director of the National Institute of Standards and Technology, the Administrator of the National Aeronautics and Space Administration, the Director of the Defense Advanced Research Projects Agency, and the heads of other relevant Federal departments and agencies to ensure that programs and activities carried out under this section complement and do not duplicate existing efforts across the Federal government. (i) Funding (1) In general Of amounts authorized to be appropriated for the Department of Energy, the Secretary of Energy shall use not more than $175,000,000 for each of fiscal years 2026 through 2030 to carry out activities under this section. (2) Restrictions (A) Confucius Institute None of the funds made available under this subsection may be obligated to or expended by an institution of higher education that maintains a contract or other agreement with a Confucius Institute or any successor of a Confucius Institute. (B) Foreign countries and entities of concern (i) Definitions In this subparagraph: (I) Foreign country of concern The term foreign country of concern means\u2014 (aa) a covered nation (as defined in section 4872(d) of title 10, United States Code); and (bb) any other country that the Secretary of Energy, in consultation with the Secretary of Defense, the Secretary of State, and the Director of National Intelligence, determines to be engaged in conduct that is detrimental to the national security or foreign policy of the United States. (II) Foreign entity of concern The term foreign entity of concern means a foreign entity that\u2014 (aa) is designated as a foreign terrorist organization by the Secretary of State under section 219(a) of the Immigration and Nationality Act ( 8 U.S.C. 1189(a) ); (bb) is included on the list of specially designated nationals and blocked persons maintained by the Office of Foreign Assets Control of the Department of the Treasury; (cc) is owned by, controlled by, or subject to the jurisdiction or direction of a government of a foreign country that is a covered nation (as defined in section 4872(d) of title 10, United States Code); (dd) is alleged by the Attorney General to have been involved in activities for which a conviction was obtained under\u2014 (AA) chapter 37 of title 18, United States Code (commonly known as the Espionage Act ); (BB) section 951 or 1030 of title 18, United States Code; (CC) chapter 90 of title 18, United States Code (commonly known as the Economic Espionage Act of 1996 ); (DD) the Arms Export Control Act ( 22 U.S.C. 2751 et seq. ); (EE) section 224, 225, 226, 227, or 236 of the Atomic Energy Act of 1954 ( 42 U.S.C. 2274 , 2275, 2276, 2277, 2284); (FF) the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ); or (GG) the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ); or (ee) is determined by the Secretary of Energy, in consultation with the Secretary of Defense and the Director of National Intelligence, to be engaged in unauthorized conduct that is detrimental to the national security or foreign policy of the United States. (ii) Restriction None of the funds made available under this subsection may be obligated or expended to promote, establish, or finance quantum research activities between a United States entity and a foreign country of concern or a foreign entity of concern. .\n#### 3. DOE Quantum Instrumentation and Foundry Program\nThe National Quantum Initiative Act is amended by inserting after section 401 ( 15 U.S.C. 8851 ) the following:\n401A. Department of Energy Quantum Instrumentation and Foundry Program (a) In general The Secretary of Energy shall establish an instrumentation and infrastructure program to carry out the following: (1) Maintain United States leadership in quantum information science, engineering, and technology. (2) Develop domestic quantum supply chains. (3) Provide resources for the broader scientific community. (4) Support activities carried out under sections 401, 402, 403, and 404. (b) Program Components In carrying out the program under subsection (a), the Secretary of Energy shall\u2014 (1) develop, design, build, purchase, and commercialize specialized equipment, laboratory infrastructure, and state-of-the-art instrumentation to advance quantum engineering research and the development of quantum component technologies at a scale sufficient to meet the needs of the scientific community and enable commercialization of quantum technology; (2) leverage the capabilities of National Laboratories and Nanoscale Science Research Centers, including facilities and experts that research and develop novel quantum materials and devices; and (3) consider the technologies and end-use applications that have significant economic potential, as determined by the Secretary, based on consultation with relevant stakeholders in academia and industry, including the Quantum Economic Development Consortium. (c) Quantum foundries In carrying out the program under subsection (a), and in coordination with institutions of higher education and industry, the Secretary of Energy shall support the development of quantum foundries focused on meeting the device, hardware, software, and materials needs of the scientific community and the quantum supply chain. (d) Consultation In carrying out the program under subsection (a), the Secretary of Energy shall consult with the following entities to identify the instrumentation, equipment, infrastructure, and materials needed to support the objectives of that program: (1) The National Institute of Standards and Technology. (2) The National Science Foundation. (3) The National Aeronautics and Space Administration. (4) Any other relevant Federal agency. (5) The National Laboratories. (6) National Quantum Information Science Research Centers. (7) Industry stakeholders. (8) Institutions of higher education. (9) Any other research institution. (e) Funding Of amounts authorized to be appropriated for the Department of Energy, the Secretary of Energy shall use not more than $50,000,000 for each of fiscal years 2026 through 2030 to carry out this section. .\n#### 4. National Quantum Information Science Research Centers\nSection 402 of the National Quantum Initiative Act ( 15 U.S.C. 8852 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking basic ; and\n**(ii)**\nby striking science and technology and to support research conducted under section 401 and inserting science, engineering, and technology, expand capacity for the domestic quantum workforce, and support research conducted under sections 401, 403, and 404 ; and\n**(B)**\nin paragraph (2)(C), by inserting that may include 1 or more commercial entities after collaborations ;\n**(2)**\nin subsection (b), by inserting and should be inclusive of the variety of viable quantum technologies, as appropriate before the period at the end;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby striking basic ; and\n**(B)**\nby inserting , engineering, and technology, accelerating quantum workforce development, after science ;\n**(4)**\nin subsection (e), by striking paragraph (2) and inserting the following:\n(2) Renewal Each Center established under this section may be renewed for an additional period of 5 years following a successful, merit-based review and approval by the Director. ; and\n**(5)**\nin subsection (f), in the first sentence\u2014\n**(A)**\nby striking $25,000,000 and inserting $35,000,000 ; and\n**(B)**\nby striking 2019 through 2023 and inserting 2026 through 2030 .\n#### 5. Department of Energy quantum network infrastructure research and development program\nSection 403 of the National Quantum Initiative Act ( 15 U.S.C. 8853 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (4)\u2014\n**(i)**\nby inserting , including after networking ; and\n**(ii)**\nby striking and at the end;\n**(B)**\nin paragraph (5), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(6) as applicable, leverage a diversity of modalities and commercially available quantum hardware and software; and (7) develop education and training pathways related to quantum network infrastructure investments, aligned with existing programmatic investments by the Department of Energy. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (D) and (E), respectively; and\n**(ii)**\nby inserting after subparagraph (B) the following:\n(C) the Administrator of the National Aeronautics and Space Administration and the head of any other relevant Federal agency, as determined by the Secretary; ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by inserting ground-to-space and before space-to-ground ;\n**(ii)**\nin subparagraph (E), by striking photon-based and inserting all applicable modalities of ;\n**(iii)**\nin subparagraph (F), by inserting , quantum sensors, after quantum repeaters ;\n**(iv)**\nin subparagraph (G)\u2014\n**(I)**\nby inserting data centers, after repeaters, ; and\n**(II)**\nby striking and at the end;\n**(v)**\nin subparagraph (H)\u2014\n**(I)**\nby striking the quantum technology stack and inserting quantum technology modality stacks ; and\n**(II)**\nby striking National Laboratories in and inserting National Laboratories such as ; and\n**(vi)**\nby adding at the end the following:\n(I) development of quantum network and entanglement distribution protocols or applications, including development of network stack protocols and protocols enabling integration with existing technologies or infrastructure; and (J) development of high-efficiency room-temperature photon detectors for quantum photonic applications, including quantum networking and communications; ;\n**(C)**\nin paragraph (4)\u2014\n**(i)**\nby striking basic ; and\n**(ii)**\nby striking material and inserting materials ; and\n**(D)**\nin paragraph (5), by striking fundamental ; and\n**(3)**\nin subsection (d), by striking basic research and inserting research, development, and demonstration .\n#### 6. Department of Energy Quantum User Expansion for Science and Technology program\nSection 404 of the National Quantum Initiative Act ( 15 U.S.C. 8854 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking and quantum computing clouds and inserting , software, and cloud-based quantum computing ;\n**(B)**\nin paragraph (3), by striking and at the end;\n**(C)**\nin paragraph (4), by striking the period at the end and inserting a semicolon; and\n**(D)**\nby adding at the end the following:\n(5) to enable development of software and applications, including estimation of resources needed to scale applications; and (6) to develop near-term quantum applications to solve public and private sector problems. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (4), by striking and at the end;\n**(B)**\nin paragraph (5), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(6) enable users to develop algorithms, software tools, simulators, and applications for quantum systems using cloud-based quantum computers; and (7) partner with appropriate public- and private-sector entities to develop training and education opportunities on prototype and early-stage devices to support commercial applications. ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby redesignating paragraphs (4) through (8) as paragraphs (5) through (9), respectively; and\n**(B)**\nby inserting after paragraph (3) the following:\n(4) the National Oceanic and Atmospheric Administration; ; and\n**(4)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (4), by striking and at the end;\n**(B)**\nin paragraph (5), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(6) $38,000,000 for fiscal year 2028; (7) $39,900,000 for fiscal year 2029; and (8) $41,895,000 for fiscal year 2030. .",
      "versionDate": "2025-02-13",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-15T16:26:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119s579",
          "measure-number": "579",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2026-02-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s579v00",
            "update-date": "2026-02-05"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Department of Energy Quantum Leadership Act of 2025</strong></p><p>This bill modifies and reauthorizes various Department of Energy (DOE) programs related to quantum research and development and establishes several new, related research programs.</p><p>Specifically, the bill expands the scope of DOE\u2019s quantum information science research program to include research, development, and demonstration on quantum information science, engineering, and technology. Among other requirements, DOE must (1) establish an early-stage research and development program in high-performance quantum computing; (2) study quantum science, engineering, and technology supply chain needs; and (3) establish a university-led trainee program to address quantum workforce development needs.</p><p>The bill also reauthorizes the National Quantum Information Science Research Centers and the Quantum User Expansion for Science and Technology program through FY2030. Further, the bill modifies DOE\u2019s quantum network infrastructure program to require research related to the development of (1) quantum network and entanglement distribution protocols or applications, and (2) high-efficiency room-temperature photon detectors for quantum photonic applications.</p><p>Finally, the bill establishes an instrumentation and infrastructure program to maintain U.S. leadership in quantum information science, engineering, and technology; develop domestic quantum supply chains; and provide resources for the broader scientific community. In carrying out the program, DOE must develop, design, build, purchase, and commercialize specialized equipment, laboratory infrastructure, and state-of-the-art instrumentation. In coordination with industry and institutions of higher education, DOE must support the development of quantum foundries focused on meeting the device, hardware, software, and materials needs of the scientific community and the quantum supply chain.</p>"
        },
        "title": "Department of Energy Quantum Leadership Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s579.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Department of Energy Quantum Leadership Act of 2025</strong></p><p>This bill modifies and reauthorizes various Department of Energy (DOE) programs related to quantum research and development and establishes several new, related research programs.</p><p>Specifically, the bill expands the scope of DOE\u2019s quantum information science research program to include research, development, and demonstration on quantum information science, engineering, and technology. Among other requirements, DOE must (1) establish an early-stage research and development program in high-performance quantum computing; (2) study quantum science, engineering, and technology supply chain needs; and (3) establish a university-led trainee program to address quantum workforce development needs.</p><p>The bill also reauthorizes the National Quantum Information Science Research Centers and the Quantum User Expansion for Science and Technology program through FY2030. Further, the bill modifies DOE\u2019s quantum network infrastructure program to require research related to the development of (1) quantum network and entanglement distribution protocols or applications, and (2) high-efficiency room-temperature photon detectors for quantum photonic applications.</p><p>Finally, the bill establishes an instrumentation and infrastructure program to maintain U.S. leadership in quantum information science, engineering, and technology; develop domestic quantum supply chains; and provide resources for the broader scientific community. In carrying out the program, DOE must develop, design, build, purchase, and commercialize specialized equipment, laboratory infrastructure, and state-of-the-art instrumentation. In coordination with industry and institutions of higher education, DOE must support the development of quantum foundries focused on meeting the device, hardware, software, and materials needs of the scientific community and the quantum supply chain.</p>",
      "updateDate": "2026-02-05",
      "versionCode": "id119s579"
    },
    "title": "Department of Energy Quantum Leadership Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Department of Energy Quantum Leadership Act of 2025</strong></p><p>This bill modifies and reauthorizes various Department of Energy (DOE) programs related to quantum research and development and establishes several new, related research programs.</p><p>Specifically, the bill expands the scope of DOE\u2019s quantum information science research program to include research, development, and demonstration on quantum information science, engineering, and technology. Among other requirements, DOE must (1) establish an early-stage research and development program in high-performance quantum computing; (2) study quantum science, engineering, and technology supply chain needs; and (3) establish a university-led trainee program to address quantum workforce development needs.</p><p>The bill also reauthorizes the National Quantum Information Science Research Centers and the Quantum User Expansion for Science and Technology program through FY2030. Further, the bill modifies DOE\u2019s quantum network infrastructure program to require research related to the development of (1) quantum network and entanglement distribution protocols or applications, and (2) high-efficiency room-temperature photon detectors for quantum photonic applications.</p><p>Finally, the bill establishes an instrumentation and infrastructure program to maintain U.S. leadership in quantum information science, engineering, and technology; develop domestic quantum supply chains; and provide resources for the broader scientific community. In carrying out the program, DOE must develop, design, build, purchase, and commercialize specialized equipment, laboratory infrastructure, and state-of-the-art instrumentation. In coordination with industry and institutions of higher education, DOE must support the development of quantum foundries focused on meeting the device, hardware, software, and materials needs of the scientific community and the quantum supply chain.</p>",
      "updateDate": "2026-02-05",
      "versionCode": "id119s579"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s579is.xml"
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
      "title": "Department of Energy Quantum Leadership Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Department of Energy Quantum Leadership Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Quantum Initiative Act to provide for a research, development, and demonstration program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:47Z"
    }
  ]
}
```
