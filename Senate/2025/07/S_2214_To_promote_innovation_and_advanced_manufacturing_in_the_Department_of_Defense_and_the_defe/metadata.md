# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2214?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2214
- Title: Future of Defense Manufacturing Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2214
- Origin chamber: Senate
- Introduced date: 2025-07-08
- Update date: 2025-09-19T17:06:59Z
- Update date including text: 2025-09-19T17:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-08: Introduced in Senate
- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-07-08: Introduced in Senate

## Actions

- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-08",
    "latestAction": {
      "actionDate": "2025-07-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2214",
    "number": "2214",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001208",
        "district": "",
        "firstName": "Elissa",
        "fullName": "Sen. Slotkin, Elissa [D-MI]",
        "lastName": "Slotkin",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Future of Defense Manufacturing Act of 2025",
    "type": "S",
    "updateDate": "2025-09-19T17:06:59Z",
    "updateDateIncludingText": "2025-09-19T17:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-08",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-08",
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
          "date": "2025-07-08T21:54:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2214is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2214\nIN THE SENATE OF THE UNITED STATES\nJuly 8, 2025 Ms. Slotkin introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo promote innovation and advanced manufacturing in the Department of Defense and the defense industrial base, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Future of Defense Manufacturing Act of 2025 .\n#### 2. Prohibition on operation, procurement, and contracting related to foreign-made additive manufacturing machines\n##### (a) Prohibition on agency operation or procurement\nThe Secretary of Defense may not operate, or enter into or renew a contract for the procurement of\u2014\n**(1)**\na covered additive manufacturing machine that\u2014\n**(A)**\nis manufactured in a covered foreign country or by an entity domiciled in a covered foreign country;\n**(B)**\nuses operating software developed in a covered foreign country or by an entity domiciled in a covered foreign country; or\n**(C)**\nuses network connectivity or data storage located in or administered by an entity domiciled in a covered foreign country; or\n**(2)**\na system or systems that incorporates, interfaces with, or otherwise uses additive manufacturing systems or machines described in paragraph (1).\n##### (b) Exception\nThe prohibition under subsection (a) does not apply to the operation or procurement of additive manufacturing systems or machines for the purposes of testing, analysis, and training related to intelligence, electronic warfare, and information warfare operations.\n##### (c) Waiver\nThe Secretary of Defense may waive the prohibition under subsection (a) on a case by case basis by certifying in writing to the congressional defense committees that the operation or procurement of additive manufacturing systems or machines is required in the national interest of the United States.\n##### (d) Definitions\nIn this section:\n**(1) Additive manufacturing machine**\nThe term additive manufacturing machine means a system of integrated hardware and software used to realize an additive manufacturing process, including the deposition of material and the associated post-processing steps as applicable.\n**(2) Additive manufacturing process**\nThe term additive manufacturing process means a process of joining materials to make parts from 3D model data, usually layer upon layer, as opposed to subtractive manufacturing methodologies.\n**(3) Covered additive manufacturing company**\nThe term covered additive manufacturing company means any of the following:\n**(A)**\nAny entity that produces or provides additive manufacturing machines and is included on\u2014\n**(i)**\nthe Consolidated Screening List maintained by the International Trade Administration of the Department of Commerce; or\n**(ii)**\nthe civil-military fusion list maintained under section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 10 U.S.C. 113 note).\n**(B)**\nAny entity that produces or provides additive manufacturing machines and\u2014\n**(i)**\nis domiciled in a covered foreign country; or\n**(ii)**\nis subject to unmitigated foreign ownership, control, or influence by a covered foreign country, as determined by the Secretary of Defense in accordance with the National Industrial Security Program or any successor to such program.\n**(4) Covered additive manufacturing machine**\nThe term covered additive manufacturing machine means additive manufacturing machines and any related services and equipment manufactured by a covered additive manufacturing company.\n**(5) Covered foreign country**\nThe term covered foreign country means the People\u2019s Republic of China, Iran, the Democratic People's Republic of Korea, and the Russian Federation.\n#### 3. Improvements to demonstration and prototyping program to advance international product support capabilities in a contested logistics environment\nSection 842(b)(2) of the National Defense Authorization Act for Fiscal Year 2024 ( Public Law 118\u201331 ; 10 U.S.C. 2341 note) is amended\u2014\n**(1)**\nin subparagraph (A), by striking ; and and inserting a semicolon;\n**(2)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(3)**\nby inserting after subparagraph (A) the following new subparagraph (B):\n(B) commercial advanced, digital manufacturing facilities for rapid, distributed parts production closer to the point of use; and .\n#### 4. Dual-use and defense advanced manufacturing innovation hubs\n##### (a) Establishment\nThe Secretary of Defense shall establish one or more dual-use advanced manufacturing hubs that co-locate and share resources among public and private stakeholders from industry, academia, government, nongovernment agencies, and workforce and economic development resources. The hub or hubs should span the full spectrum of advanced manufacturing capabilities and cover the full development timeline between prototyping and fielding.\n##### (b) Requirements\nA hub established under subsection (a) shall\u2014\n**(1)**\nutilize, to the maximum extent possible, the Department of Defense Manufacturing Innovation Institutes (MII) and encourage the MIIs to coordinate efforts in a joint manner;\n**(2)**\nprovide shared advanced manufacturing infrastructure and equipment, such as high-speed metal printers and material testing laboratories;\n**(3)**\nestablish a process to provide advanced manufacturing capability, including on shared classified space as needed;\n**(4)**\nutilize, to the maximum extent possible, the Defense Logistics Agency\u2019s Joint Additive Manufacturing Model Exchange (JAMMEX) as a central data repository for technical data packages for advanced manufacturing;\n**(5)**\nbuild on the Defense Innovation Unit\u2019s Blue Manufacturing Initiative and Blue Manufacturing Marketplace to match hardware and software manufacturers in defense technology with advanced manufacturing providers; and\n**(6)**\nmeet annual production benchmarks for defense applications.\n##### (c) Consultation\nThe Secretary shall consult with the Under Secretary of Defense for Research and Engineering and the Under Secretary of Defense for Acquisition and Sustainment in establishing a dual-use advanced manufacturing hub under subsection (a).\n##### (d) Recommendation\nNot later than September 30, 2026, the Secretary shall submit to the congressional defense committees a recommendation for the appropriate number of regional hubs to be established under subsection (a) for the Department of Defense to meet its sustainment needs and such requirements, specifications, and capabilities as the regional hubs may require.\n#### 5. Department of Defense Advanced Manufacturing Program\nNot later than December 31, 2027, the Secretary of Defense, in coordination with the Secretaries of the military departments, shall aim to qualify and approve for manufacturing and delivery not fewer than 1,000,000 parts or components of the Department of Defense that use advanced manufacturing techniques, with funding subject to the availability of appropriations or other funds. In doing so, the Secretary shall ensure that expedited processes for adoption of advanced manufacturing products are utilized across the components of the Department of Defense and lifecycle phases for new and existing systems.\n#### 6. Program to additively manufacture certain types of unmanned aerial systems\nNot later than September 30, 2026, the Secretary of Defense shall carry out a program to certify new materials and processes to manufacture 25 to 100 percent of the parts of one of each type of the following unmanned aerial system (UAS) categories using advanced or additive manufacturing techniques:\n**(1)**\nSmall unmanned aerial systems used as tactical loitering munitions.\n**(2)**\nSmall unmanned aerial systems used for surveillance and reconnaissance missions.\n**(3)**\nSmall unmanned aerial systems used for logistics missions.\n#### 7. Program to certify additively manufactured parts for military systems with diminishing manufacturing sources and material shortages\n##### (a) Program required\nNot later than September 30, 2026, the Under Secretary of Defense for Acquisition and Sustainment shall, in coordination with the Under Secretary of Defense for Research and Engineering and the Secretaries of the military departments, carry out a program to produce replacement parts for military systems with diminishing manufacturing sources and material shortages using advanced or additive manufacturing techniques.\n##### (b) Tested parts\nIn carrying out the program required by subsection (a), the Under Secretary of Defense for Acquisition and Sustainment shall select not less than five parts for test, evaluation, and certification under the program.\n##### (c) Test and evaluation\n**(1) In general**\nIn carrying out the program required by subsection (a), the Under Secretary shall use additive manufacturing techniques to manufacture the parts selected pursuant to subsection (b) and then test and evaluate the manufactured parts.\n**(2) Evaluation**\nEvaluation under paragraph (1) shall be based on performance rather than specifications.\n##### (d) Sharing of results and data\nIn carrying out the program required by subsection (a), the Under Secretary shall share test data across all military departments and establish mechanisms for data reciprocity for test and evaluation results for additively manufactured parts across all military departments.\n##### (e) List of obsolete parts\nThe Under Secretary shall, in coordination with the Secretaries of the military departments, make a list of all parts for military systems with diminishing manufacturing sources and material shortages.\n##### (f) New licensing agreements\nThe Under Secretary shall, in coordination with the Secretaries of the military departments, create new licensing agreements with owners of intellectual property for the platforms with parts included in the list required by subsection (e) that allow additive manufacture of the parts.\n#### 8. Program to additively manufacture metal parts\n##### (a) Program required\nThe Under Secretary of Defense for Acquisition and Sustainment shall carry out a program across all military departments to additively manufacture three commonly used metal parts of each military department, such as titanium, stainless steel, and aluminum.\n##### (b) Assessment required\nNot later than September 30, 2026, the Under Secretary shall\u2014\n**(1)**\ncomplete an assessment to determine how to additively manufacture 10 metal parts of each military department, with a preference for parts that require long lead times to manufacture or have sole-source suppliers; and\n**(2)**\nsubmit to the congressional defense committees a report on the findings of the Under Secretary with respect to the assessment completed under paragraph (1).\n#### 9. Program to additively manufacture parts for ground combat systems\nThe Under Secretary of Defense for Acquisition and Sustainment shall, in coordination with the Secretary of the Army and the Director of the Defense Logistics Agency\u2014\n**(1)**\nidentify sustainment vulnerabilities in the ground equipment supply chain of the Army, including at the manufacturing arsenals and maintenance depots of the Army that comprise the Organic Industrial Base, where additive manufacturing could be used to repair, upgrade, or modernize ground combat systems;\n**(2)**\nchoose not less than five parts that have long lead times for fabricating the greatest degree of customized specifications or have the most limited quantity in inventory and additively manufacture replacement parts for them;\n**(3)**\ncreate a critical parts list identifying parts and components across ground combat systems with long lead times eligible to be additively manufactured; and\n**(4)**\ndevelop plans, in coordination with Army Development Command, to integrate additive manufacturing techniques and technologies in the design, production, and sustainment of next-generation combat vehicles and their technologies. The developed technologies should prioritize interoperability across military platforms and integration with other military services.\n#### 10. Enhance international coordination for advanced manufacturing techniques, technologies, and adoption\nThe Under Secretary of Defense for Acquisition and Sustainment and the Under Secretary of Defense for Research and Engineering shall establish a subordinate working group within the Joint Additive Manufacturing Working Group to coordinate and support international activities that facilitate information-sharing, enhance interoperability, explore joint research and development opportunities, identify technology licensing requirements, incorporate advanced manufacturing capabilities into combined trainings and exercises, and set technical expertise and training standards for advanced manufacturing techniques, technologies, and adoption. The countries involved should be those with which the United States has reciprocal defense procurement agreements or security of supply arrangements.\n#### 11. Composition of Joint Defense Manufacturing Technology Panel\nSection 4842(b)(2) of title 10, United States Code, is amended by inserting selected by the Under Secretary of Defense for Acquisition and Sustainment and one individual after one individual .\n#### 12. Advanced manufacturing guidance and manual\n##### (a) Guidance, DoD I update, and manual required\nNot later than September 30, 2026, the Under Secretary of Defense for Acquisition and Sustainment and the Under Secretary of Defense for Research and Engineering, in consultation with the Secretaries of the military departments, shall\u2014\n**(1)**\ndevelop guidance to incorporate innovations in advanced manufacturing in such a way that the Department of Defense can better and faster deliver capabilities, sustain operations, and protect the warfighter with the latest technology while still ensuring quality, reliability, and compatibility;\n**(2)**\nupdate Department of Defense Instruction 5000.93 (relating to use of additive manufacturing in the Department of Defense) dated June 10, 2021, to waive the requirement to maintain records of all additively produced end-items put into operational use where the additively produced part meets or exceeds performance of the traditionally manufactured end-item;\n**(3)**\ncreate a manual in accordance with such instruction that gets at the technical standards required to qualify parts, components, or products that use advanced manufacturing technologies and techniques; and\n**(4)**\nnot later than March 1, 2026, provide the Committees on Armed Services of the Senate and the House of Representatives a briefing on plans to update the guidance developed under paragraph (1) and the updates made under paragraph (2).\n##### (b) Considerations\nIn carrying out subsection (a), the Under Secretary of Defense for Acquisition and Sustainment and the Under Secretary of Defense for Research and Engineering shall consider the most current versions of Department of Defense Additive Manufacturing Roadmap, the Department of Defense Additive Manufacturing Strategy, the National Strategy for Advanced Manufacturing, and Department of Defense Instruction 5000.93.\n##### (c) Alignment\nThe Under Secretary of Defense for Acquisition and Sustainment and the Under Secretary of Defense for Research and Engineering shall ensure that the guidance on the use of advanced manufacturing required by subsection (a)(1)\u2014\n**(1)**\naligns with Department of Defense acquisition to prioritize flexibility, interoperability, and domestic sourcing;\n**(2)**\nrequires the Department to prefer United States manufacturers and equipment and document a justification whenever the Department uses a foreign source; and\n**(3)**\nrequires the Department to partner with and direct funds to the Department\u2019s Manufacturing Innovation Institutes whenever feasible.\n##### (d) Elements\n**(1) Guidance**\nThe guidance required by subsection (a)(1) shall include guidance for all types of advanced manufacturing, including the following:\n**(A)**\nAdditive manufacturing.\n**(B)**\nAdvanced materials.\n**(C)**\nAdvanced composite materials.\n**(D)**\nRobotics and automation.\n**(E)**\nLaser, machining, and welding.\n**(F)**\nNanotechnology.\n**(G)**\nNetwork and information technology integration.\n**(2) Manual**\n**(A)**\nThe guidance required by paragraph (1) of subsection (a) shall utilize expedited qualification and testing procedures established in section 865 of the National Defense Authorization Act for Fiscal Year 2025 and result in a manual under paragraph (3) of such subsection to establish standardized processes to qualify parts and components produced by advanced manufacturing techniques and technologies based on performance, rather than specifications for testing and evaluation.\n**(B)**\nThe process described in subparagraph (A) shall include a methodology for standardizing technical production specifications, testing processes, and data reciprocity to share and accept test results of the same additively manufactured parts across all military departments.\n**(C)**\nThe process described in subparagraph (A) shall include test and evaluation results that facilitate data reciprocity across military departments, removing the need for each military department to independently validate the same parts another military department has already validated.\n**(D)**\nThe manual shall include steps to allow for streamlined incremental qualification, rather than complete requalification, when the design and manufacturing process incorporates changes.\n**(E)**\nThe process described in subparagraph (A) shall explore the option for third-party, external certification for companies that cannot afford or do not have the in-house expertise to do this on their own but have the technology that the Department needs.\n**(3) Advanced materials and advanced composite materials research**\nThe guidance required by subsection (a)(1) and the manual required by subsection (a)(3)\u2014\n**(A)**\nshall cover requirements for development, test, and evaluation of the material properties of advanced materials and advanced composite materials used in advanced manufacturing, including metals, polymers, ceramics, composites, and hybrid metals;\n**(B)**\nshould include how to incorporate integrated computational materials engineering to predict the material properties and the distribution of those properties in additively manufactured parts and scale-up additive manufacturing; and\n**(C)**\nshall include a list of recommendations for the types of amounts of critical metals to stockpile for the Department\u2019s use in additive manufacturing, which should be accessible to users of the Defense Logistics Agency\u2019s Joint Additive Manufacturing Model Exchange (JAMMEX).\n**(4) Cybersecurity**\n**(A)**\nThe guidance required by subsection (a)(1) and the manual required by subsection (a)(3) shall include cybersecurity standards and guidelines for advanced manufacturing developed in consultation with the Chief Information Officer.\n**(B)**\nThe guidance and manual should address the unique challenges that advanced manufacturing poses to Department information networks.\n**(C)**\nThe guidance and manual shall include matters relating to cybersecurity compliance.\n**(D)**\nThe guidance and manual shall call for periodic security and compliance reviews.\n**(5) Modeling and simulation**\nThe guidance and manual required by subsection (a)\u2014\n**(A)**\nshall include software-driven, artificial intelligence-enabled modeling and simulation techniques for design, development, test, and evaluation to the maximum extent possible; and\n**(B)**\nshould include integrating modeling and simulation at every level, from enterprise to individual operation, including utilizing digital engineering.\n**(6) Intellectual property**\n**(A)**\nThe guidance required by subsection (a)(1) and the manual required by subsection (a)(3) shall include processes and contracting mechanisms to protect and manage intellectual property.\n**(B)**\nThe processes and contracting mechanisms described in subparagraph (A) shall be designed to incentivize innovation while allowing the Department to additively manufacture parts and products for military systems at scale and on demand in case of contingency or crisis. This can include new licensing agreements with terms and conditions that allow for innovative intellectual property strategies.\n**(C)**\nThe guidance and manual shall include considerations to incorporate the Defense Logistics Agency\u2019s Joint Additive Manufacturing Model Exchange (JAMMEX).\n**(7) Quality assurance**\n**(A)**\nThe guidance required by subsection (a)(1) and the manual required by subsection (a)(3) shall include processes, materials, and technologies to ensure continuous quality control throughout the entire manufacturing process and post-production.\n**(B)**\nThe guidance and manual shall incorporate the process window qualification methodology, which is designed to be machine-agnostic, or independent of specific machine brands or software providers, as well as the following:\n**(i)**\nReal-time process monitoring leveraging machine sensors and software analytics to detect and instantly mitigate deviations prevents defects and unauthorized parameter changes.\n**(ii)**\nIntegration of machine learning algorithms that analyze production data in real-time allows the identification of anomalies indicative of potential quality or security threats, enabling proactive mitigation.\n**(iii)**\nSoftware-defined quality assurance protocols enforce standardized, repeatable verification processes, greatly improving reliability and simplifying security audits.\n**(8) Proliferation of additive manufacturing capabilities**\nThe guidance required by subsection (a) shall include a plan that includes phasing and funding requirements to proliferate advanced manufacturing technologies and techniques across the entire Department, at the enterprise level to tactical operational units. This guidance shall\u2014\n**(A)**\nidentify end-user access and operational needs for advanced manufacturing and associated resourcing, infrastructure, and basing requirements;\n**(B)**\nestablish logistics models for production of additively manufactured parts in the continental United States and at forward operating locations;\n**(C)**\nimprove supply chain risk management; and\n**(D)**\nstimulate supply chain agility within the Department.\n**(9) Training**\nThe guidance required by subsection (a)(1) shall include training program requirements, phasing, and sequencing to ensure each warfighter is equipped with the knowledge and skills to use advanced manufacturing techniques and technologies efficiently and safely. The guidance shall\u2014\n**(A)**\noutline which military occupational specialty career fields to train in advanced manufacturing equipment, techniques, and procedures with each military service and the degree of proficiency and training time required;\n**(B)**\nexplore partnerships to establish apprenticeships and skilled technician training pipelines to support Department of Defense research and development programs and programs of record; and\n**(C)**\nconsider creating new initiatives within existing transition assistance programs to create pathways for members of the Armed Forces to receive the training necessary to adapt their military skills to civilian jobs in advanced manufacturing.\n##### (e) Manual required\nThe manual created under subsection (a)(3) shall be a service-agnostic, vendor-agnostic manual on advanced manufacturing techniques and technologies for the Department of Defense\u2014\n**(1)**\nto standardize across the military departments the technical parameters for manufacturing parts and products using advanced manufacturing techniques;\n**(2)**\nto outline the categories and levels of risk associated with such parts and products, including distinguishing between safety-critical and non-safety-critical parts and providing expedited approvals for low-risk parts through standardized material datasets and pre-qualified manufacturing protocols;\n**(3)**\nto lay out the processes for qualification and certification across categories of such parts and products;\n**(4)**\nto establish data reciprocity for test and evaluation data across all military departments with respect to qualifying such parts and products;\n**(5)**\nto utilize the Defense Logistics Agency\u2019s Joint Additive Manufacturing Model Exchange (JAMMEX) as the central data repository for technical data packages for advanced manufacturing; and\n**(6)**\nto incorporate new proposed qualification approaches proposed by industry consortiums, Manufacturing Innovation Institutes, and Small Business Innovation Research (SBIR) and Small Business Technology Transfer (STTR) programs.\n##### (f) Timeline\n**(1) Initial**\nThe Secretary shall ensure that the guidance required by subsection (a)(1) goes into effect in fiscal year 2026 by providing guidance with respect to the top three essential metals each military department needs to maintain its operational platforms.\n**(2) Subsequent**\nThe Secretary shall ensure that the guidance required by subsection (a)(1) goes into effect not later than January 1, 2027, for all essential metals not covered by paragraph (1).",
      "versionDate": "2025-07-08",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-19T17:06:59Z"
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
      "date": "2025-07-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2214is.xml"
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
      "title": "Future of Defense Manufacturing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T01:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Future of Defense Manufacturing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote innovation and advanced manufacturing in the Department of Defense and the defense industrial base, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:30Z"
    }
  ]
}
```
