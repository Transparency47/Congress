# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6275?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6275
- Title: China AI Power Report Act
- Congress: 119
- Bill type: HR
- Bill number: 6275
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-02-12T09:06:18Z
- Update date including text: 2026-02-12T09:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6275",
    "number": "6275",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "China AI Power Report Act",
    "type": "HR",
    "updateDate": "2026-02-12T09:06:18Z",
    "updateDateIncludingText": "2026-02-12T09:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "VA"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "MI"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "IN"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6275ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6275\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Moylan (for himself, Mr. Vindman , and Mr. Huizenga ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Secretary of Commerce to submit a report annually on the advanced artificial intelligence capabilities of the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the China AI Power Report Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nexport controls on artificial intelligence technologies and related capabilities must be dynamic and adaptive to effectively address the evolving national security challenges posed by the People\u2019s Republic of China ( China );\n**(2)**\nsuch controls should be regularly updated to reflect rapid technological innovations, China\u2019s advancing capabilities, and emerging methods of diversion, circumvention, and avoidance, to ensure the United States maintains its strategic advantage and to protect the national security interests of the United States; and\n**(3)**\nto ensure Congress can exercise oversight and, as necessary, update export control authorities to enable necessary updates to export controls, Congress must be kept fully and currently informed of the current and projected future states of China\u2019s artificial intelligence capabilities.\n#### 3. Report on artificial intelligence power of china\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 3 years, the Secretary of Commerce, in consultation with the covered agency heads, shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate a report on the advanced artificial intelligence capabilities of China, including the efforts by China relating to supply chains for advanced artificial intelligence systems.\n##### (b) Components\nEach report required under subsection (a) shall also include the following:\n**(1)**\nAn assessment of integrated circuits designed or optimized for advanced artificial intelligence training or inference by leading artificial intelligence chip designers in China, including Huawei Technologies Co., Ltd. and Cambricon Technologies, that includes\u2014\n**(A)**\nwith respect to such integrated circuits, the\u2014\n**(i)**\ntotal processing power;\n**(ii)**\ninteger and floating point operations per second at relevant precision levels;\n**(iii)**\nmemory capacity and bandwidth;\n**(iv)**\ninterconnect bandwidth;\n**(v)**\npower efficiency;\n**(vi)**\ntransistor count and die size;\n**(vii)**\nprocess node used per design;\n**(viii)**\nenergy efficiency;\n**(ix)**\nmanufacturing cost and yield assumptions;\n**(x)**\nability of the integrated circuit to effectively run artificial intelligence models trained on a different chip designer\u2019s integrated circuit, including measurements such as model inference in tokens per second and cost per token with and without a software application layer that improves model translation ability;\n**(xi)**\nthe capability of the most advanced server configuration produced using the chip designer\u2019s integrated circuits including such technical specifications like floating point operations per second, memory capacity and bandwidth, energy efficiency, and ability to function at scale; and\n**(xii)**\nany future specification that becomes relevant to the development of future artificial intelligence capability; and\n**(B)**\nwith respect to such chip designers\u2014\n**(i)**\nthe total number and types of integrated circuits produced in the year preceding submission of such report and the projected production number for the year proceeding submission of such report;\n**(ii)**\nthe foundries used in the production of the integrated circuits;\n**(iii)**\nthe software ecosystem, including any parallel computing platforms, programming models, or development frameworks that enable accelerated computing for artificial intelligence training or inference;\n**(iv)**\nthe method and extent to which such integrated circuits are used in other countries, including in the United States; and\n**(v)**\nthe manufacturer\u2019s ability to produce a software application layer required to achieve an improved token per seconds and cost per token rate.\n**(2)**\nAn assessment of leading semiconductor fabrication facilities in China that produce logic integrated circuits for use in advanced artificial intelligence training or inference, including such facilities owned or operated by the Semiconductor Manufacturing International Corporation, that includes, with respect to such facilities, the\u2014\n**(A)**\ntotal monthly production capacity per advanced process node with non-planar transistors or 16/14 nm and below and the percentage of that monthly production capacity dedicated to production of logic integrated circuits for use in advanced artificial training or inference;\n**(B)**\nyield for producing such logic integrated circuits for use in advanced artificial intelligence training or inference at each facility with an assessment of that yield in industry relevant terms, such as compared to Chinese firms, compared to non-Chinese firms, or how many are in current industry-leading datacenters;\n**(C)**\nmost advanced process node under production;\n**(D)**\ntypes and volume of semiconductor manufacturing equipment used, the country of origin for such equipment, and the export control regulatory regime under which such equipment was procured;\n**(E)**\ncollaborations, licit or illicit, between Chinese firms or their subsidiaries and non-Chinese firms and the advancements those collaborations produce for the Chinese firm;\n**(F)**\nprogress Chinese firms are making at indigenizing export controlled technologies;\n**(G)**\nmarket share Chinese firms have in China and internationally; and\n**(H)**\nyear-over-year trends in leading semiconductor fabrication facilities during at least the preceding 5-year period;\n**(3)**\nAn assessment of leading semiconductor fabrication facilities in China that produce memory integrated circuits used for advanced artificial intelligence training or inference, including such facilities owned or operated by ChangXin Memory Technologies or Yangtze Memory Technologies Corp., that includes\u2014\n**(A)**\nwith respect to such circuits, the\u2014\n**(i)**\nmost advanced generation of high-bandwidth memory, including the technical specifications and stack height;\n**(ii)**\nsmallest half-pitch and the per-die capacity of other dynamic random access memory integrated circuits; and\n**(iii)**\nhighest number of layers in three-dimensional NOT\u2013AND memory integrated circuits;\n**(B)**\nwith respect to such facilities, the\u2014\n**(i)**\nyield and total monthly production capacity for memory integrated circuits, including dynamic random access memory such as high-bandwidth memory, and NOT\u2013AND memory; and\n**(ii)**\ntypes and volume of semiconductor manufacturing equipment used, including the country of origin of such equipment and the export control regulatory regime such equipment was procured under.\n**(C)**\ncollaborations, licit or illicit, between Chinese firms or their subsidiaries and non-Chinese firms and the advancements those collaborations produce for the Chinese firm;\n**(D)**\nprogress Chinese firms are making at indigenizing export controlled technologies;\n**(E)**\nmarket share Chinese firms have in China and internationally; and\n**(F)**\nyear-over-year trends in China\u2019s advanced memory integrated circuit production for a minimum of the 5 previous years.\n**(4)**\nAn assessment of leading semiconductor manufacturing equipment companies in China, including NAURA Technology Group, KINGSEMI, Advanced Micro-Fabrication Equipment Inc., Shanghai Micro Electronics Equipment, and Shenzhen SiCarrier Technologies Co., Ltd, that includes\u2014\n**(A)**\na categorical breakdown of annual unit production volume and technical specifications, including minimum feature size, throughput, and defect rate, of all major equipment classes installed or under development for wafer production in foundries in China, including\u2014\n**(i)**\nlithography tools, including photolithography, nanoimprint, and electron beam lithography tools;\n**(ii)**\netch equipment, including wet etching and dry etching;\n**(iii)**\ndeposition equipment, including chemical vapor deposition, physical vapor deposition, and atomic layer deposition;\n**(iv)**\ncleaning systems;\n**(v)**\nchemical mechanical planarization tools;\n**(vi)**\nion implantation and diffusion systems;\n**(vii)**\nwafer inspection, metrology, and process control tools;\n**(viii)**\nback-end packaging equipment, including wafer dicing equipment and wire bonders;\n**(ix)**\ncapabilities and advancements in advanced packaging technologies;\n**(x)**\nthermal processing equipment;\n**(xi)**\nbonding equipment, including thermo compression bonders and hybrid bonders;\n**(xii)**\nenvironmental control systems;\n**(xiii)**\nlaser systems; and\n**(xiv)**\nreticle and photomask writing and inspection tools;\n**(B)**\nthe country of origin and supplier company for each piece of semiconductor manufacturing equipment used in foundries in China for advanced-node logic or high-bandwidth memory production by such companies;\n**(C)**\nthe foreign-sourced subcomponents integrated into the semiconductor manufacturing equipment produced by such companies, including precision motion stages, lasers, electrostatic chucks, optical systems, radio frequency generators, or extreme-purity gas handling systems;\n**(D)**\ncollaborations, licit or illicit, between Chinese firms or their subsidiaries and non-Chinese firms and the advancements those collaborations produce for the Chinese firm;\n**(E)**\nprogress Chinese firms are making at indigenizing export controlled technologies;\n**(F)**\nmarket share Chinese firms have in China and internationally; and\n**(G)**\nyear-over-year trends in leading semiconductor manufacturing equipment companies in China for a minimum of the 5 previous years.\n**(5)**\nAn assessment of electronic design automation (EDA) software used in the design of integrated circuits for advanced artificial intelligence applications in China, including software developed or provided by leading Chinese EDA companies such as Empyrean Technology Co., Ltd. and Primarius Technologies Co., Ltd., that includes\u2014\n**(A)**\nwith respect to such software tools, the\u2014\n**(i)**\nrange of design stages supported, including front-end design such as architecture and register-transfer level design, logic synthesis, verification, physical design, place-and-route, timing closure, and final signoff;\n**(ii)**\ncompatibility with advanced process nodes, including sub-7 nanometer technologies, gate-all-around devices, and three-dimensional integration;\n**(iii)**\ncapabilities for designing artificial intelligence-specific components of such integrated circuits, including tensor processing cores, systolic array processing units, matrix multiplier units, and high-bandwidth memory interfaces;\n**(iv)**\nability to model and optimize for power, performance, and thermal constraints in artificial intelligence workloads;\n**(v)**\nscale and performance of the software in handling large designs, such as chips exceeding 50\u2013100 billion transistors; and\n**(vi)**\nintegration with cloud compute resources or distributed workflows for large-scale artificial intelligence chip development;\n**(B)**\nwith respect to such companies, the\u2014\n**(i)**\ntotal market share within China and internationally, including the share of advanced-node integrated circuits designed or optimized for advanced artificial intelligence training or inference designs supported by each company; and\n**(ii)**\ntypes, volume, and origin of critical technology components used in software development, including intellectual property cores, third-party libraries, verification suites, and artificial intelligence-assisted optimization algorithms;\n**(C)**\nprogress Chinese firms are making at indigenizing export-controlled or foreign-origin technologies used in EDA, including high-performance computing integration, advanced verification engines, and proprietary intellectual property cores;\n**(D)**\nyear-over-year trends for China\u2019s EDA industry over a minimum of the previous 5 years, including technology adoption, market share, and software capability evolution; and\n**(E)**\nidentification of technical gaps relative to leading global EDA providers, particularly in relation to artificial intelligence-focused design, advanced nodes, and large-scale verification.\n**(6)**\nAn assessment of the advanced artificial intelligence models determined by the Secretary to be the most relevant to the national security of the United States that were developed by artificial intelligence laboratories or companies based in China, especially those laboratories and companies affiliated with the People\u2019s Liberation Army or any university in China, including the most advanced models, open-weight and closed-weight models, based on model size, total compute used during training, benchmark performance, and any other advanced capabilities the Secretary determines relevant, that includes, with respect to each such model\u2014\n**(A)**\nthe number of model parameters;\n**(B)**\nthe total training compute used, measured in floating-point operations and their relevant precision level;\n**(C)**\nthe model performance on benchmark tasks;\n**(D)**\nan evaluation of the extent to which the model exhibits advanced cyber offensive capabilities, an advanced understanding of biological and virological application domains, and the ability to substantially automate or accelerate artificial intelligence research, and a comparison of such models to the most advanced artificial intelligence models from United States developers;\n**(E)**\nif the model is open-weight, an evaluation of the files provided and the security implications of following the developer\u2019s deployment instructions;\n**(F)**\na description of the algorithmic alignment training used;\n**(G)**\nthe type and scale of compute infrastructure used in training and inference, including the cluster configurations, the number and type of integrated circuits specifically designed or optimized for advanced artificial intelligence training or inference, how such integrated circuits were acquired and from which companies, where those clusters are located, and how they are being accessed;\n**(H)**\nthe manner and extent to which the model is used throughout society in China, including throughout the following industries or sectors:\n**(i)**\nthe People\u2019s Liberation Army;\n**(ii)**\nthe surveillance and intelligence collection functions of the Chinese Communist Party (CCP), including the genocide of Uyghur Muslims and other religious and ethnic minorities in the Xinjiang Uyghur Autonomous Region;\n**(iii)**\nthe Government of China;\n**(iv)**\nbusiness and finance;\n**(v)**\neducation;\n**(vi)**\nhealthcare;\n**(vii)**\ncritical infrastructure sectors, including the power grid and transportation; and\n**(viii)**\nany other sectors that the Secretary determines to be relevant, such as high-risk industries where artificial intelligence failure would have outsized safety or mission consequences.\n**(I)**\nwhether and where such models are deployed for public use, including API access or mobile app deployment;\n**(J)**\nthe manner and extent to which such models are diffused in other countries, including the United States;\n**(K)**\nthe alignment of those models to CCP propaganda;\n**(L)**\nthe potential of those models to inject or create vulnerabilities for users or other ways they could be used to further CCP national security objectives;\n**(M)**\nan assessment of global market share of Chinese models and the effect that global market share is enabling China to set artificial intelligence hardware or software standards; and\n**(N)**\nthe total number of tokens inferenced globally using the model, the types of hardware utilized for such inference and the percent breakdown between company of origin for such hardware, and the percentage of global inferenced tokens attributable to the model.\n**(7)**\nAn assessment of emerging artificial intelligence research in China, based on indicators such as academic publications, patent filings, and research funding, including\u2014\n**(A)**\nthe development of novel artificial intelligence algorithms and techniques, including advancements in reinforcement learning, natural language processing, or computer vision, with a focus on algorithms and techniques most relevant for developing or deploying the most advanced artificial intelligence systems;\n**(B)**\nadvancements in hardware designed to enhance artificial intelligence capabilities, including custom integrated circuits, quantum computing technologies, or neuromorphic computing systems, with a focus on hardware advancements most relevant for developing or deploying the most advanced artificial intelligence systems;\n**(C)**\nthe scale and focus of research efforts, including the number of researchers, institutions, and collaborations involved, and the funding levels and sources, with a focus on those most relevant for developing or deploying the most advanced frontier artificial intelligence systems;\n**(D)**\nan evaluation of the potential impact of such research on future artificial intelligence capabilities relevant to national security competitiveness; and\n**(E)**\na description of licit or illicit methods or tactics such as unauthorized model distillation used by Chinese entities to steal non-Chinese artificial intelligence related intellectual property.\n**(8)**\nAn assessment of the aggregate public funding and capital flows supporting artificial intelligence development in China, including\u2014\n**(A)**\nthe sum total of China\u2019s national, provincial, and municipal investment in artificial intelligence;\n**(B)**\nsubsidies that are underwriting the costs of artificial intelligence development in areas such as compute, infrastructure, water, and energy;\n**(C)**\nan assessment of foreign capital investments, including the total amount invested and a breakdown by entity, including the country of origin and the amount invested; and\n**(D)**\nan assessment of the PRC-based entities that have received the funding, including the name of the entity and the amount of funding received.\n**(9)**\nThe aggregate artificial intelligence computational capacity in China, including\u2014\n**(A)**\na detailed analysis of computational capacity of the 5 most capable entities in China, including the number and types of integrated circuits and server systems used and their aggregate computational power;\n**(B)**\nthe countries and companies with respect to which China sourced their computational capacity; and\n**(C)**\nthe locations and specifications, including energy and computational capacity, of datacenters used for advanced artificial intelligence training and inference.\n**(10)**\nAn assessment of leading humanoid robot manufacturers in China, including Unitree Robotics and Fourier, that includes\u2014\n**(A)**\nwith respect to such manufacturers, the\u2014\n**(i)**\nproduction capacity per year; and\n**(ii)**\nunit cost and pricing trends for such robots intended for commercial deployment; and\n**(B)**\nwith respect to the humanoid robots produced by such manufactures\u2014\n**(i)**\nthe number, type, and country and company of origin of the semiconductor components, including integrated circuits, used to build, run, or train such robots;\n**(ii)**\nthe country and company of origin and the technical specifications of critical components used in such robots, including actuators, sensors, and battery systems, and if not Chinese, the progress toward indigenization;\n**(iii)**\na description of the tasks such robots can perform;\n**(iv)**\nwhether such robots are teleoperated, operated through hard-coded instructions, or function autonomously using artificial intelligence models;\n**(v)**\nwhether inference is performed locally or via remote cloud services;\n**(vi)**\nthe number of such robots deployed across China, including in the military, manufacturing, logistics, health care, security, and personal assistance sectors;\n**(vii)**\nthe extent to which, and ways in which, such robots are diffused in other countries, including in the United States; and\n**(viii)**\nan assessment of the cybersecurity and other vulnerabilities of Chinese origin robotic systems.\n**(11)**\nAn assessment of the most advanced or widely used artificial intelligence-powered applications developed by Chinese entities or built on Chinese artificial intelligence models, including\u2014\n**(A)**\nthe artificial intelligence models used to power these applications, including the company and country of origin for each model and whether the models are open-weight or closed-weight;\n**(B)**\nthe means of deployment and the extent to which such applications are used, including in the United States;\n**(C)**\nthe purposes, capabilities, and promoted uses of the applications;\n**(D)**\nan analysis of how data collected or generated by the applications is used, including for artificial intelligence model training, surveillance, or other national security-relevant purposes; and\n**(E)**\nan evaluation of the potential risks posed by these applications to United States national security, foreign policy objectives, or data privacy.\n**(12)**\nAn assessment of the regulatory framework governing artificial intelligence development, deployment, and usage in China, that includes\u2014\n**(A)**\nthe explicit restrictions on artificial intelligence models, including laws, regulations, and government policies that directly limit or control the development, deployment, or use of artificial intelligence models in China;\n**(B)**\nan analysis of the implicit restrictions on artificial intelligence models, including censorship, data access limitations, or other indirect controls that may constrain artificial intelligence model capabilities;\n**(C)**\nhow such explicit and implicit restrictions impact the development, deployment, and diffusion of artificial intelligence models both within China and internationally, including the effects on innovation, competitiveness, and national security;\n**(D)**\nan analysis of efforts by the CCP to acquire greater insight into advanced artificial intelligence and reduce strategic surprise, such as efforts that require advanced artificial intelligence developers to disclose information about artificial intelligence systems or provide models to government entities;\n**(E)**\nan analysis of efforts in China to assess or mitigate national security or public safety threats from advanced artificial intelligence systems, including efforts to prevent loss of control from autonomous artificial intelligence systems; and\n**(F)**\nthe goals for artificial intelligence development explicitly and implicitly stated by the CCP.\n**(13)**\nAn assessment of China\u2019s global artificial intelligence standards diplomacy efforts, including\u2014\n**(A)**\nmapping the fora where Chinese actors aimed to shape global standards;\n**(B)**\njurisdictions where Chinese-promoted standards, model laws, guidance, or procurement criteria have been adopted or referenced;\n**(C)**\nthe effects on procurement and vendor eligibility; and\n**(D)**\nopportunities for the United States to shape global artificial intelligence standards and counter Chinese efforts.\n**(14)**\nAn assessment of the degree to which entities in China remotely accessed artificial intelligence computational resources, including through cloud services, international data centers, or through circumvention or avoidance of United States export controls.\n**(15)**\nAn assessment of the methods, pathways, quantities, and companies and countries of origin of United States-controlled integrated circuits specifically designed or optimized for advanced artificial intelligence training or inference, including graphics processing units or application-specific integrated circuits, that have been diverted to mainland China, the estimated total compute capacity enabled through these chip diversions, and the percent of China\u2019s total compute capacity enabled through these chip diversions.\n**(16)**\nAn assessment of the effectiveness of United States export controls in restricting access by China to artificial intelligence-relevant technologies, including an identification of loopholes within United States export controls and recommendations for legislative and administrative action to strengthen export controls and enforcement that is consistent with United States national security and foreign policy objectives.\n##### (c) Prioritization\nIn conducting the assessments required under subsection (b), the Secretary shall prioritize the identification and analysis of\u2014\n**(1)**\nsemiconductors, semiconductor manufacturing equipment, and critical components of semiconductor manufacturing equipment that are, or are likely to become, critical to the supply chains for the training or inference of the most advanced artificial intelligence systems; and\n**(2)**\nitems that enable or could enable advanced model performance, are associated with systems that pose significant national security or strategic implications to the United States, or are likely to be foundational to the development of future advanced artificial intelligence systems, including those not yet deployed or publicly disclosed.\n##### (d) Reference class\nWhere applicable, the Secretary shall provide context to all statistics regarding China\u2019s artificial intelligence power in the report by presenting China\u2019s capabilities and production numbers in comparison to relevant United States and partner country production numbers and capabilities.\n##### (e) Coordination with expert entities\nIn carrying out this section, the Secretary may consult and coordinate with other Federal departments and agencies, private industry or research organizations, federally funded research and development centers, national laboratories, academic institutions, relevant media outlets, or any other entities with expertise in semiconductor technologies, artificial intelligence, or national security that the Secretary determines relevant.\n##### (f) Form\nThe report required by subsection (a) shall be submitted in unclassified form and may contain a classified annex.\n##### (g) Mandatory unclassified elements\nIn the unclassified portion of the report required under subsection (a), the Secretary shall include\u2014\n**(1)**\nthe number of integrated circuits specifically designed or optimized for advanced artificial intelligence training or inference produced by leading entities in China in the year preceding submission of such report;\n**(2)**\nthe projected production numbers of integrated circuits from China specifically designed or optimized for advanced artificial intelligence training or inference, including identification of foundries responsible for such production, for the year proceeding submission of such report; and\n**(3)**\nthe extent to which and ways artificial intelligence-relevant technologies in China, including integrated circuits, models, semiconductor manufacturing equipment, and humanoid robots are diffused in other countries, including the United States.\n##### (h) Definitions\nIn this Act:\n**(1) Secretary**\nThe term Secretary means the Secretary of Commerce.\n**(2) Covered agency heads**\nThe term covered agency heads means the\u2014\n**(A)**\nSecretary of State;\n**(B)**\nSecretary of Defense;\n**(C)**\nSecretary of Energy;\n**(D)**\nDirector of National Intelligence;\n**(E)**\nDirector for the White House Office of Science and Technology Policy; and\n**(F)**\nhead of any other relevant Federal department or agency the Secretary determines necessary.",
      "versionDate": "2025-11-21",
      "versionType": "Introduced in House"
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
        "name": "International Affairs",
        "updateDate": "2025-12-16T17:11:58Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6275ih.xml"
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
      "title": "China AI Power Report Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T06:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "China AI Power Report Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-16T06:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Commerce to submit a report annually on the advanced artificial intelligence capabilities of the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-16T06:48:18Z"
    }
  ]
}
```
