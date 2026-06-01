# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/644?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/644
- Title: Harmful Algal Bloom and Hypoxia Research and Control Amendments Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 644
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-12-19T21:39:48Z
- Update date including text: 2025-12-19T21:39:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/644",
    "number": "644",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Harmful Algal Bloom and Hypoxia Research and Control Amendments Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-19T21:39:48Z",
    "updateDateIncludingText": "2025-12-19T21:39:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:09:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-23T15:09:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OH"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "DE"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MI"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr644ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 644\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Bonamici (for herself and Mr. Joyce of Ohio ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Harmful Algal Bloom and Hypoxia Research and Control Act of 1998 to address harmful algal blooms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Harmful Algal Bloom and Hypoxia Research and Control Amendments Act of 2025 .\n#### 2. Amendments to the Harmful Algal Bloom and Hypoxia Research and Control Act of 1998\n##### (a) Assessments\n**(1) In general**\nSection 603 of the Harmful Algal Bloom and Hypoxia Research and Control Act of 1998 ( 33 U.S.C. 4001 ) is amended\u2014\n**(A)**\nin the section heading, by striking Assessments and inserting Task Force, assessments, and Action Strategy ;\n**(B)**\nin subsection (a)\u2014\n**(i)**\nby redesignating paragraphs (13) and (14) as paragraphs (14) and (15), respectively; and\n**(ii)**\nby inserting after paragraph (12) the following:\n(13) the Department of Energy; ;\n**(C)**\nby striking subsections (b), (c), (d), (e), (g), (h), and (i) and redesignating subsection (f) as subsection (b);\n**(D)**\nin subsection (b), as so redesignated\u2014\n**(i)**\nin paragraph (1), in the first sentence, by striking coastal waters including the Great Lakes and inserting marine, estuarine, and freshwater systems ; and\n**(ii)**\nin paragraph (2)\u2014\n**(I)**\nby amending subparagraph (A) to read as follows:\n(A) examine\u2014 (i) the causes and ecological consequences of hypoxia on marine and aquatic species in their environments; and (ii) the costs of hypoxia, including impacts on food safety and security; ;\n**(II)**\nby redesignating subparagraphs (B), (C), and (D) as subparagraphs (D), (E), and (F), respectively;\n**(III)**\nby inserting after subparagraph (A) the following:\n(B) examine the effect of other environmental stressors on hypoxia; (C) evaluate alternatives for reducing, mitigating, and controlling hypoxia and its environmental impacts; ; and\n**(IV)**\nin subparagraph (E), as redesignated by subclause (II), by striking hypoxia modeling and monitoring data and inserting hypoxia modeling, forecasting, and monitoring and observation data ; and\n**(E)**\nby adding at the end the following:\n(c) Action Strategy and scientific assessment for marine and freshwater harmful algal blooms (1) In general Not less frequently than once every 5 years, the Task Force shall complete and submit to Congress an action strategy for harmful algal blooms in the United States. (2) Elements Each Action Strategy shall\u2014 (A) examine, and include a scientific assessment of, marine and freshwater harmful algal blooms, including such blooms\u2014 (i) in the Great Lakes; (ii) in the upper reaches of estuaries; (iii) in freshwater lakes and rivers; (iv) in coastal and marine waters; and (v) that originate in freshwater lakes or rivers and migrate to coastal waters; (B) examine the causes, ecological consequences or physiological consequences on wildlife function, and economic or cultural impacts, including food safety and security and subsistence use, of harmful algal blooms; (C) examine the effect of other environmental stressors on harmful algal blooms; (D) examine potential methods to prevent, control, and mitigate harmful algal blooms and the potential ecological, subsistence use, and economic costs and benefits of such methods; (E) identify priorities for research needed to advance techniques and technologies to detect, predict, monitor, respond to, and minimize the occurrence, duration, and severity of harmful algal blooms, including recommendations to eliminate significant gaps in harmful algal bloom forecasting, monitoring, and observation data; (F) evaluate progress made by, and the needs of, activities and actions of the Task Force to prevent, control, and mitigate harmful algal blooms; (G) identify ways to improve coordination and prevent unnecessary duplication of effort among Federal agencies with respect to research on harmful algal blooms; and (H) include regional chapters relating to the requirements described in this paragraph in order to highlight geographically and ecologically diverse locations with significant ecological, subsistence use, cultural, and economic impacts from harmful algal blooms. (d) Consultation In carrying out subsections (b) and (c), the Task Force shall consult with\u2014 (1) States, Indian tribes, and local governments; and (2) appropriate industries (including fisheries, agriculture, and fertilizer), academic institutions, and nongovernmental organizations with relevant expertise. .\n**(2) Clerical amendment**\nThe table of contents in section 2 of the Coast Guard Authorization Act of 1998 ( Public Law 105\u2013383 ; 112 Stat. 3412; 136 Stat. 1268) is amended by striking the item relating to section 603 and inserting the following:\nSec. 603. Task Force, assessments, and Action Strategy. .\n**(3) Conforming amendment**\nSection 102 of the Harmful Algal Bloom and Hypoxia Amendments Act of 2004 ( 33 U.S.C. 4001a ) is amended by striking In developing and all that follows through management. .\n##### (b) National Harmful Algal Bloom and Hypoxia Program\nSection 603A of the Harmful Algal Bloom and Hypoxia Research and Control Act of 1998 ( 33 U.S.C. 4002 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking predicting, and inserting monitoring, observing, forecasting, ; and\n**(ii)**\nby striking and after the semicolon; and\n**(B)**\nby striking paragraph (2) and inserting the following:\n(2) the scientific assessment submitted under section 603(b); and (3) the Action Strategy. ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (3), by striking ocean and Great Lakes science and management programs and centers and inserting programs and centers relating to the science and management of marine, estuarine, and freshwater systems ; and\n**(B)**\nin paragraph (5), by inserting while recognizing each agency is acting under its own independent mission and authority before the semicolon;\n**(3)**\nin subsection (d), by striking Except as provided in subsection (h), the and inserting The ;\n**(4)**\nin subsection (e)\u2014\n**(A)**\nby striking paragraph (2) and inserting the following:\n(2) examine the causes, ecological consequences, and costs of harmful algal blooms and hypoxia; ;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (B), by inserting , including the annual Gulf of Mexico hypoxia zone mapping cruise after Program ;\n**(ii)**\nin subparagraph (C), by striking and after the semicolon; and\n**(iii)**\nby adding at the end the following:\n(E) to identify opportunities to improve monitoring of harmful algal blooms and hypoxia, with a particular focus on waters that may affect fisheries, public health, or subsistence harvest; (F) to evaluate adaptation and mitigation strategies to address the impacts of harmful algal blooms and hypoxia; (G) to support the resilience of the seafood industry to harmful algal blooms and to expand access to testing for harmful algal bloom toxins, including for subsistence and recreational harvesters, through innovative methods that increase the efficiency and effectiveness of such testing in rural and remote areas; (H) to support sustained observations to provide State and local entities, Indian tribes, and other entities access to real-time or near real-time observations data for decision-making to protect human and ecological health and local economies; and (I) to assess the combined effects of harmful algal blooms, hypoxia, and stressors such as runoff and infrastructure changes on marine, freshwater, or estuarine ecosystems and living resources; ;\n**(C)**\nin paragraph (4), by striking agencies and inserting entities, regional coastal observing systems (as defined in section 12303 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3602 )), ;\n**(D)**\nin paragraph (6), by inserting and communities after ecosystems ;\n**(E)**\nin paragraph (8), by inserting and Indian tribes after managers ;\n**(F)**\nin paragraph (9)(A), by striking , tribal, and local stakeholders and inserting and local stakeholders and Indian tribes, Tribal organizations, and Native Hawaiian organizations ;\n**(G)**\nby redesignating paragraphs (3), (4), (5), (6), (7), (8), (9), (10), and (11) as paragraphs (4), (5), (6), (7), (8), (9), (10), (12), and (13), respectively;\n**(H)**\nby inserting after paragraph (2) the following:\n(3) consult with entities that are most dependent on coastal and water resources that may be impacted by marine and freshwater harmful algal blooms and hypoxia, including\u2014 (A) State and local entities; (B) Indian tribes, Tribal organizations, and Native Hawaiians organizations; (C) island communities; (D) low-population rural communities; (E) subsistence communities; and (F) fisheries and recreation industries; ; and\n**(I)**\nby inserting after paragraph (10), as redesignated by subparagraph (G), the following:\n(11) expand access to testing for harmful algal bloom toxins, including for subsistence and recreational harvesters, through innovative methods that increase the efficiency and effectiveness of such testing in rural and remote areas; ;\n**(5)**\nby amending subsection (f) to read as follows:\n(f) Cooperation; duplication of effort The Under Secretary shall work cooperatively with and avoid duplication of effort of other agencies on the Task Force and States, Indian tribes, Tribal organizations, Native Hawaiian organizations, and nongovernmental organizations concerned with marine and freshwater issues. ; and\n**(6)**\nby striking subsections (g), (h), and (i).\n##### (c) National Oceanic and Atmospheric Administration activities\n**(1) In general**\nSection 603B of the Harmful Algal Bloom and Hypoxia Research and Control Act of 1998 ( 33 U.S.C. 4003 ) is amended to read as follows:\n603B. National Oceanic and Atmospheric Administration activities (a) In general The Under Secretary shall\u2014 (1) carry out response activities for marine, coastal, and Great Lakes harmful algal bloom and hypoxia events; (2) develop and enhance operational harmful algal bloom observing and forecasting programs, including operational observations and forecasting, monitoring, modeling, data management, and information dissemination; (3) develop forecast modeling that includes the effect of hurricanes and other weather events on the resuspension of bioavailable nutrients in sediments and related interactions with harmful algal blooms; (4) enhance communication and coordination among Federal agencies carrying out activities and research relating to marine and freshwater harmful algal blooms and hypoxia; (5) leverage existing resources and expertise available from local research universities and institutions; and (6) use cost effective methods in carrying out this section. (b) Integrated Coastal and Ocean Observation System The collection of monitoring and observing data under this section shall comply with all data standards and protocols developed pursuant to the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3601 et seq. ). Such data shall be made available through the National Integrated Coastal and Ocean Observation System established under section 12304 of that Act ( 33 U.S.C. 3603 ). .\n**(2) Clerical amendment**\nThe table of contents in section 2 of the Coast Guard Authorization Act of 1998 ( Public Law 105\u2013383 ; 112 Stat. 3412; 136 Stat. 1268) is amended by striking the item relating to section 603B and inserting the following:\nSec. 603B. National Oceanic and Atmospheric Administration activities. .\n##### (d) Environmental Protection Agency activities\n**(1) In general**\nThe Harmful Algal Bloom and Hypoxia Research and Control Act of 1998 is amended by inserting after section 603B ( 33 U.S.C. 4003 ) the following:\n603C. Environmental Protection Agency activities (a) In general The Administrator shall\u2014 (1) carry out research on the ecology and human health impacts of freshwater harmful algal blooms and hypoxia events; (2) develop and enhance operational freshwater harmful algal bloom monitoring, observing, and forecasting programs in lakes, rivers, and reservoirs, and coordinate with the National Oceanic and Atmospheric Administration on such programs in the Great Lakes and estuaries (including tributaries thereof), including operational observations and forecasting, monitoring, modeling, data management, and information dissemination, to support event response, prioritization, prevention, adaptation, and mitigation activities; (3) enhance communication and coordination among Federal agencies carrying out freshwater harmful algal bloom and hypoxia activities and research; (4) to the greatest extent practicable, leverage existing resources and expertise available from Federal and State partners and local research universities and institutions; and (5) use cost-effective methods in carrying out this section. (b) Nonduplication The Administrator shall ensure that activities carried out under subsection (a) focus on new approaches to addressing freshwater harmful algal blooms and are not duplicative of existing research and development programs authorized by this title or any other law. .\n**(2) Clerical amendment**\nThe table of contents in section 2 of the Coast Guard Authorization Act of 1998 ( Public Law 105\u2013383 ; 112 Stat. 3412; 136 Stat. 1268) is amended by inserting after the item relating to section 603B the following:\nSec. 603C. Environmental Protection Agency activities. .\n##### (e) National harmful algal bloom observing network\n**(1) In general**\nSection 606 of the Harmful Algal Bloom and Hypoxia Research and Control Act of 1998 ( 33 U.S.C. 4005 ) is amended to read as follows:\n606. National harmful algal bloom observing network (a) In general The Under Secretary, acting through the National Centers for Coastal Ocean Science and the Integrated Ocean Observing System of the National Oceanic and Atmospheric Administration, shall integrate Federal, State, regional, and local observing capabilities to establish a national network of observing systems for the monitoring, detection, and forecasting of harmful algal blooms by leveraging the capacity of regional associations of the Integrated Ocean Observing System, including through the incorporation of emerging technologies and new data integration methods. (b) Coordination and data assembly In carrying out subsection (a), the Program Office of the Integrated Ocean Observing System shall\u2014 (1) coordinate with the National Centers for Coastal Ocean Science regarding observations, data integration, and information dissemination; (2) organize, integrate, disseminate, and provide a central architecture to support ecological forecasting of harmful algal blooms; and (3) coordinate with the Water Quality Portal to store and serve discrete data related to the monitoring of freshwater, estuarine, and coastal harmful algal blooms. .\n**(2) Clerical amendment**\nThe table of contents in section 2 of the Coast Guard Authorization Act of 1998 ( Public Law 105\u2013383 ; 112 Stat. 3412; 136 Stat. 1268) is amended by striking the item relating to section 606 and inserting the following:\nSec. 606. National harmful algal bloom observing network. .\n##### (f) National-Level incubator program\n**(1) In general**\nThe Harmful Algal Bloom and Hypoxia Research and Control Act of 1998 is amended by inserting after section 606 ( 33 U.S.C. 4005 ) the following:\n606A. National-level incubator program (a) In general The Under Secretary, in collaboration with the Administrator and research universities and institutions, shall establish a national-level incubator program (in this section referred to as the program ) to increase the number of strategies, technologies, and measures available to prevent, mitigate, and control harmful algal blooms. (b) Framework The program shall establish a framework for preliminary assessments of novel strategies, technologies, and measures to prevent, mitigate, and control harmful algal blooms in order to determine the potential effectiveness and scalability of such technologies. (c) Funding The program shall provide merit-based funding, using amounts otherwise available to the Under Secretary for the award of grants, for strategies, technologies, and measures that eliminate or reduce, through biological, chemical, or physical means, the levels of harmful algae and associated toxins resulting from harmful algal blooms. (d) Database The program shall include a database for cataloging the licensing and permitting requirements, economic costs, feasibility, effectiveness, and scalability of novel and established strategies, technologies, and measures to prevent, mitigate, and control harmful algal blooms. (e) Prioritization In carrying out the program, the Under Secretary shall prioritize proposed strategies, technologies, and measures that would, to the maximum extent practicable\u2014 (1) protect key habitats for fish and wildlife; (2) maintain biodiversity; (3) protect public health; (4) protect coastal resources of national, historical, and cultural significance; or (5) benefit low-income communities, Indian tribes, and rural communities. .\n**(2) Clerical amendment**\nThe table of contents in section 2 of the Coast Guard Authorization Act of 1998 ( Public Law 105\u2013383 ; 112 Stat. 3412; 136 Stat. 1268) is amended by inserting after the item relating to section 606 the following:\nSec. 606A. National-level incubator program. .\n##### (g) Definitions\nSection 609 of the Harmful Algal Bloom and Hypoxia Research and Control Act of 1998 ( 33 U.S.C. 4008 ) is amended\u2014\n**(1)**\nin paragraph (1), by striking means the comprehensive research plan and action strategy established under section 603B and inserting means the action strategy for harmful algal blooms in the United States most recently submitted under section 603(c) ;\n**(2)**\nby amending paragraph (3) to read as follows:\n(3) Harmful algal bloom The term harmful algal bloom means a high concentration of marine or freshwater algae (including diatoms), macroalgae (including Sargassum), or cyanobacteria resulting in nuisance conditions or harmful impacts on marine and freshwater ecosystems, subsistence resources, communities, or human health through the production of toxic compounds or other biological, chemical, or physical impacts of the bloom. ;\n**(3)**\nby striking paragraph (9);\n**(4)**\nby redesignating paragraphs (4), (5), (6), (7), and (8) as paragraphs (5), (8), (9), (11), and (13), respectively;\n**(5)**\nby inserting after paragraph (3) the following:\n(4) Harmful algal bloom and hypoxia event The term harmful algal bloom and hypoxia event means the occurrence of a harmful algal bloom or hypoxia as a result of a natural, anthropogenic, or undetermined cause. ;\n**(6)**\nin paragraph (5), as redesignated by paragraph (4)\u2014\n**(A)**\nby striking aquatic and inserting marine or freshwater ; and\n**(B)**\nby striking resident and inserting marine or freshwater ;\n**(7)**\nby inserting after paragraph (5), as redesignated by paragraph (4), the following:\n(6) Indian tribe The term Indian tribe has the meaning given that term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (7) Native Hawaiian organization The term Native Hawaiian organization has the meaning given that term in section 6207 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7517 ) and includes the Department of Hawaiian Home Lands and the Office of Hawaiian Affairs. ;\n**(8)**\nby inserting after paragraph (9), as redesignated by paragraph (4), the following:\n(10) Subsistence use The term subsistence use means the customary and traditional use of fish, wildlife, or other freshwater, coastal, or marine resources by any individual or community to meet personal or family needs, including essential economic, nutritional, or cultural applications. ; and\n**(9)**\nby inserting after paragraph (11), as redesignated by paragraph (4), the following:\n(12) Tribal organization The term Tribal organization has the meaning given that term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). .\n##### (h) Authorization of appropriations\nSection 610 of the Harmful Algal Bloom and Hypoxia Research and Control Act of 1998 ( 33 U.S.C. 4009 ) is amended\u2014\n**(1)**\nby amending subsection (a) to read as follows:\n(a) In general There is authorized to be appropriated to carry out this title, for each of fiscal years 2026 through 2030\u2014 (1) $19,500,000 to the Under Secretary; and (2) $8,000,000 to the Administrator. ; and\n**(2)**\nby adding at the end the following:\n(c) Transfer authority As specifically provided in advance in appropriations Acts, the Under Secretary or the Administrator may transfer funds made available to carry out this title to the head of any Federal department or agency, with the concurrence of such head, to carry out, as appropriate, relevant provisions of this title and section 9(g) of the National Integrated Drought Information System Reauthorization Act of 2018 ( 33 U.S.C. 4010 ). .\n#### 3. Other harmful algal bloom and hypoxia matters\nSection 9(g) of the National Integrated Drought Information System Reauthorization Act of 2018 ( 33 U.S.C. 4010 ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (B), by adding at the end the following new sentence: The appropriate Federal official may waive the non-Federal share requirements of the preceding sentence if such official determines no reasonable means are available through which the recipient of the Federal share can meet the non-Federal share requirement. ; and\n**(B)**\nby adding at the end the following:\n(D) Contract, cooperative agreement, and grant authority The appropriate Federal official may enter into contracts, cooperative agreements, and grants with States, Indian Tribes, Tribal organizations, Native Hawaiian organizations, local governments, or other entities to pay for or reimburse costs incurred by such entities for the purposes of supporting the determination of, and assessing the environmental, economic, subsistence use, and public health effects of, an event of national significance. ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A), by inserting a leadership official of an affected Indian Tribe, the executive official of the District of Columbia, or the executive official of an affected territory or possession of the United States, after State, ; and\n**(B)**\nin subparagraph (B), by striking consider and all that follows through boundary. and inserting \u201cconsider factors such as\u2014\n(i) the risk to public health and the potential severity of the detrimental environmental effects of the hypoxia or harmful algal bloom event, as indicated by\u2014 (I) data on shellfish or water quality obtained through sampling programs, including baseline data, and regulatory or advisory thresholds established to explain management actions related to the event; (II) toxin levels in fish, marine mammals, seabirds, shellfish, or water during the event; (III) toxic aerosols produced during the event, including potential human exposures to toxic aerosols; (IV) reports of human or animal illnesses or mortalities during the event; (V) any closures of fishing or shellfish harvesting locations or recreational public waters, including beaches, during the event; (VI) the duration and spatial extent of the event; or (VII) impacts to habitats or ecosystems associated with the event; (ii) the potential economic, food safety and security, and subsistence impacts associated with the hypoxia or harmful algal bloom event, including to fisheries and aquaculture, recreation and tourism, monitoring and management, resource use, and event response activities, assessed in comparison with historical data from when a State or region did not experience such an event, as possible, as indicated by\u2014 (I) increases in public health expenditures; (II) losses to commercial fisheries and aquaculture industries, recreation and tourism, real estate, and other impacted industries or businesses; (III) increases in monitoring and management expenditures, including costs incurred for event response and clean-up (such as for beach clean-up following an influx of biomass or a fish-kill) by public or private sectors; or (IV) impacts to subsistence resources, including nutritional, resource use, and economic effects on subsistence communities; (iii) the relative magnitude of those impacts in relation to past occurrences of hypoxia or harmful algal bloom events that occur on a recurrent or annual basis; and (iv) the geographic scope of the hypoxia or harmful algal bloom event, including the potential of the event to affect several municipalities, to affect more than 1 State, or to cross an international boundary. ;\n**(3)**\nin paragraph (3), by adding at the end the following:\n(D) Indian Tribe The term Indian Tribe has the meaning given that term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (E) Native Hawaiian organization The term Native Hawaiian organization has the meaning given that term in section 6207 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7517 ) and includes the Department of Hawaiian Home Lands and the Office of Hawaiian Affairs. (F) Subsistence use The term subsistence use means the customary and traditional use of fish, wildlife, or other freshwater, coastal, or marine resources by any individual or community to meet personal or family needs, including essential economic, nutritional, or cultural applications. (G) Tribal organization The term Tribal organization has the meaning given that term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). ; and\n**(4)**\nby adding at the end the following:\n(4) Authorization of appropriations There is authorized to be appropriated to carry out this subsection $2,000,000 for each of fiscal years 2026 through 2030, to remain available until expended. .",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-09-11",
        "actionTime": "11:20:47",
        "text": "Held at the desk."
      },
      "number": "93",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Harmful Algal Bloom and Hypoxia Research and Control Amendments Act of 2025",
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
        "updateDate": "2025-03-04T20:31:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr644",
          "measure-number": "644",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-12-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr644v00",
            "update-date": "2025-12-19"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Harmful Algal Bloom and Hypoxia Research and Control Amendments Act of 2025</strong></p><p>This bill extends through FY2030 and modifies the Harmful Algal Bloom and\u00a0Hypoxia Research and Control Act to address algal blooms and hypoxia (deficiency of oxygen) in U.S. marine, estuarine, and freshwater systems. Harmful algal blooms are high concentrations of algae that may create nuisance or toxic conditions that are harmful to humans, animals, aquatic ecosystems, and the economy.</p><p>The bill directs the Inter-Agency Task Force on Harmful Algal Blooms and Hypoxia to submit to Congress an action strategy for harmful algal blooms at least once every five years. The bill also expands the task force's membership\u00a0to include the Department of Energy.</p><p>The bill also expands the duties of the National Oceanic and Atmospheric Administration (NOAA) under the National Harmful Algal Bloom and Hypoxia program. NOAA must also carry out a variety of activities related to monitoring, predicting, preventing, mitigating, and responding to marine, coastal, and Great Lakes harmful algal bloom and hypoxia events. For example, NOAA must establish\u00a0(1) a national network of observing systems for monitoring, detecting, and forecasting harmful algal blooms; and (2) a national-level incubator program to increase the number of strategies, technologies, and measures available to prevent, mitigate, and control harmful algal blooms.</p><p>Additionally, the Environmental Protection Agency must develop and enhance operational freshwater harmful algal bloom monitoring, observing, and forecasting programs in lakes, rivers, and reservoirs and carry out other activities related to researching freshwater harmful algal blooms and hypoxia events.</p>"
        },
        "title": "Harmful Algal Bloom and Hypoxia Research and Control Amendments Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr644.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Harmful Algal Bloom and Hypoxia Research and Control Amendments Act of 2025</strong></p><p>This bill extends through FY2030 and modifies the Harmful Algal Bloom and\u00a0Hypoxia Research and Control Act to address algal blooms and hypoxia (deficiency of oxygen) in U.S. marine, estuarine, and freshwater systems. Harmful algal blooms are high concentrations of algae that may create nuisance or toxic conditions that are harmful to humans, animals, aquatic ecosystems, and the economy.</p><p>The bill directs the Inter-Agency Task Force on Harmful Algal Blooms and Hypoxia to submit to Congress an action strategy for harmful algal blooms at least once every five years. The bill also expands the task force's membership\u00a0to include the Department of Energy.</p><p>The bill also expands the duties of the National Oceanic and Atmospheric Administration (NOAA) under the National Harmful Algal Bloom and Hypoxia program. NOAA must also carry out a variety of activities related to monitoring, predicting, preventing, mitigating, and responding to marine, coastal, and Great Lakes harmful algal bloom and hypoxia events. For example, NOAA must establish\u00a0(1) a national network of observing systems for monitoring, detecting, and forecasting harmful algal blooms; and (2) a national-level incubator program to increase the number of strategies, technologies, and measures available to prevent, mitigate, and control harmful algal blooms.</p><p>Additionally, the Environmental Protection Agency must develop and enhance operational freshwater harmful algal bloom monitoring, observing, and forecasting programs in lakes, rivers, and reservoirs and carry out other activities related to researching freshwater harmful algal blooms and hypoxia events.</p>",
      "updateDate": "2025-12-19",
      "versionCode": "id119hr644"
    },
    "title": "Harmful Algal Bloom and Hypoxia Research and Control Amendments Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Harmful Algal Bloom and Hypoxia Research and Control Amendments Act of 2025</strong></p><p>This bill extends through FY2030 and modifies the Harmful Algal Bloom and\u00a0Hypoxia Research and Control Act to address algal blooms and hypoxia (deficiency of oxygen) in U.S. marine, estuarine, and freshwater systems. Harmful algal blooms are high concentrations of algae that may create nuisance or toxic conditions that are harmful to humans, animals, aquatic ecosystems, and the economy.</p><p>The bill directs the Inter-Agency Task Force on Harmful Algal Blooms and Hypoxia to submit to Congress an action strategy for harmful algal blooms at least once every five years. The bill also expands the task force's membership\u00a0to include the Department of Energy.</p><p>The bill also expands the duties of the National Oceanic and Atmospheric Administration (NOAA) under the National Harmful Algal Bloom and Hypoxia program. NOAA must also carry out a variety of activities related to monitoring, predicting, preventing, mitigating, and responding to marine, coastal, and Great Lakes harmful algal bloom and hypoxia events. For example, NOAA must establish\u00a0(1) a national network of observing systems for monitoring, detecting, and forecasting harmful algal blooms; and (2) a national-level incubator program to increase the number of strategies, technologies, and measures available to prevent, mitigate, and control harmful algal blooms.</p><p>Additionally, the Environmental Protection Agency must develop and enhance operational freshwater harmful algal bloom monitoring, observing, and forecasting programs in lakes, rivers, and reservoirs and carry out other activities related to researching freshwater harmful algal blooms and hypoxia events.</p>",
      "updateDate": "2025-12-19",
      "versionCode": "id119hr644"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr644ih.xml"
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
      "title": "Harmful Algal Bloom and Hypoxia Research and Control Amendments Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:52Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Harmful Algal Bloom and Hypoxia Research and Control Amendments Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Harmful Algal Bloom and Hypoxia Research and Control Act of 1998 to address harmful algal blooms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:51Z"
    }
  ]
}
```
