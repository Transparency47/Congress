# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/91?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/91
- Title: Western Wildfire Support Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 91
- Origin chamber: Senate
- Introduced date: 2025-01-14
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in Senate
- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-01-14: Introduced in Senate

## Actions

- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/91",
    "number": "91",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Western Wildfire Support Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-14",
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
      "actionDate": "2025-01-14",
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
        "item": [
          {
            "date": "2026-02-04T22:02:18Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-14T21:46:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:02Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s91is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 91\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2025 Ms. Cortez Masto (for herself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo improve Federal activities relating to wildfires, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Western Wildfire Support Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014Preparation\nSec. 101. Firefighting account transparency.\nSec. 102. Reimbursement for wildfires caused by military training.\nSec. 103. Strategic wildland fire management planning.\nSec. 104. Study on integrating local firefighters into wildfire response.\nTITLE II\u2014Wildfire detection and suppression support\nSec. 201. Wildfire detection equipment.\nSec. 202. Slip-on tank units.\nSec. 203. Research and development of unmanned aircraft system fire applications.\nSec. 204. Study on drone incursions on wildfire suppression.\nSec. 205. Study on modernizing wildfire response technologies.\nTITLE III\u2014Post-fire recovery support\nSec. 301. Funding for online guides for post-disaster assistance.\nSec. 302. Post-fire management and recovery.\nSec. 303. Long-Term Burned Area Rehabilitation account.\nSec. 304. Prize for wildfire-related invasive species reduction.\n#### 2. Definitions\nIn this Act:\n**(1) Congressional committees**\nThe term congressional committees means\u2014\n**(A)**\nthe Committee on Energy and Natural Resources and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Natural Resources and the Committee on Appropriations of the House of Representatives.\n**(2) Federal land**\nThe term Federal land means\u2014\n**(A)**\npublic lands (as defined in section 103 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1702 ));\n**(B)**\nunits of the National Park System;\n**(C)**\nunits of the National Wildlife Refuge System;\n**(D)**\nland held in trust by the United States for the benefit of Indian Tribes or members of an Indian Tribe; and\n**(E)**\nland in the National Forest System.\n**(3) Fireshed**\nThe term fireshed means a geographically delineated forest landscape, within which a fire ignition would threaten homes, communities, or critical infrastructure.\n**(4) National forest system**\n**(A) In general**\nThe term National Forest System has the meaning given the term in section 11(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1609(a) ).\n**(B) Exclusion**\nThe term National Forest System does not include\u2014\n**(i)**\nthe national grasslands and land utilization projects administered under title III of the Bankhead-Jones Farm Tenant Act ( 7 U.S.C. 1010 et seq. ); or\n**(ii)**\nNational Forest System land east of the 100th meridian.\n**(5) Resource management plan**\nThe term resource management plan has the meaning given the term in section 101 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6511 ).\n**(6) Secretaries**\nThe term Secretaries means\u2014\n**(A)**\nthe Secretary of the Interior; and\n**(B)**\nthe Secretary of Agriculture.\n**(7) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of the Interior, in the case of Federal land under the jurisdiction of the Secretary of the Interior; and\n**(B)**\nthe Secretary of Agriculture, in the case of Federal land under the jurisdiction of the Secretary of Agriculture.\nI\nPreparation\n#### 101. Firefighting account transparency\n##### (a) Annual reporting\nSection 104(a) of division O of the Consolidated Appropriations Act, 2018 ( 43 U.S.C. 1748a\u20132(a) ), is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking the fiscal year and all that follows through this division, and inserting each fiscal year, ; and\n**(2)**\nin paragraph (1), by striking report with respect to the additional new budget authority; and inserting report on the amounts obligated and the amounts expended from Wildland Fire Management accounts, including any amounts obligated or expended using additional new budget authority under section 251(b)(2)(F) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 901(b)(2)(F) ), in the preceding fiscal year; .\n##### (b) Inclusions\nSection 104(b) of division O of the Consolidated Appropriations Act, 2018 ( 43 U.S.C. 1748a\u20132(b) ), is amended\u2014\n**(1)**\nin paragraph (3), in the matter preceding subparagraph (A), by striking a statistically significant sample of large fires, including an analysis for each fire and inserting each catastrophic wildfire described in subsection (c), including an analysis for each such catastrophic wildfire ; and\n**(2)**\nin paragraph (4), by striking by fire size and all that follows through the semicolon at the end and inserting the following: \u201cby\u2014\n(A) the total ground-based operations costs; (B) the total aircraft operations costs; (C) the total personnel costs; (D) the total on-incident and off-incident support costs; (E) the total funding allocated from the Wildland Fire Management account of the Secretary of the Interior or the Secretary of Agriculture (as applicable) to pay for administrative costs; and (F) any other relevant factors, as determined by the Secretary of the Interior or the Secretary of Agriculture (as applicable); .\n##### (c) Catastrophic wildfire described\nSection 104 of division O of the Consolidated Appropriations Act, 2018 ( 43 U.S.C. 1748a\u20132 ), is amended by adding at the end the following:\n(c) Catastrophic wildfire described A catastrophic wildfire referred to in subsection (b)(3) is a wildfire incident or wildfire complex that\u2014 (1) requires the mobilization or use of Federal firefighting resources; (2) (A) burns at least 100,000 acres of land; or (B) burns at least 50,000 acres of land, with a 50 percent or greater portion at high severity; and (3) (A) results in total suppression costs of $50,000,000 or more; (B) destroys 1 or more primary residences; or (C) directly results in the death of 1 or more individuals. .\n#### 102. Reimbursement for wildfires caused by military training\n##### (a) Mutual aid\nIn accordance with section 2 of the Act of May 27, 1955 ( 42 U.S.C. 1856a ) (commonly known as the Reciprocal Fire Protection Act ), the Secretary of Defense shall seek to enter into reciprocal agreements with State agencies for mutual aid in furnishing fire suppression services.\n##### (b) Reimbursements\nEach reciprocal agreement entered into under subsection (a) shall provide for the reimbursement of the State agency that is a party to the agreement for fire suppression services provided by the State agency as a result of a fire caused by military training or other planned actions carried out by the Department of Defense in support of military operations.\n##### (c) Limitation\nServices reimbursable under subsection (b) shall be limited to services directly attributable to the fire for which reimbursement is sought.\n##### (d) Application\nEach application from a State agency for reimbursement for services under subsection (b) shall provide an itemized request of the services covered by the application, including the costs of the services.\n##### (e) Funds\nReimbursements under subsection (b) shall be made from amounts authorized to be appropriated to the Department of Defense for operation and maintenance.\n##### (f) Existing agreements\nAn agreement in effect as of the date of enactment of this Act shall be considered an agreement entered into under subsection (a) if the agreement otherwise meets the requirements of such an agreement under this section.\n#### 103. Strategic wildland fire management planning\n##### (a) In general\nNot later than September 30, 2026, the Secretary concerned shall review existing spatial fire management policies for each fireshed on Federal land and issue, as appropriate, new or revised policies that incorporate the best available science and planning tools.\n##### (b) Requirements\nSpatial fire management policies issued under subsection (a) shall\u2014\n**(1)**\nbe routinely reviewed and updated\u2014\n**(A)**\nto include forest management activities or changes in accessibility;\n**(B)**\nnot later than 1 year after the date on which a wildfire incident has occurred within the applicable fireshed; and\n**(C)**\nnot less frequently than once every 10 years;\n**(2)**\nidentify potential wildfire and smoke risks to first responders, communities, critical infrastructure, and high-value resources;\n**(3)**\nbe consistent with any resource management plan developed for the applicable fireshed;\n**(4)**\nin coordination with any State that includes that fireshed, delineate potential wildland fire operational delineations that\u2014\n**(A)**\nidentify potential wildfire control locations; and\n**(B)**\nspecify the places in which risk to wildfire responders may be elevated as a result of\u2014\n**(i)**\nexceeding a certain slope for the landscape;\n**(ii)**\ncontaining an excess of hazardous fuels such that a threat would be posed under severe fire weather conditions; or\n**(iii)**\ncontaining other known hazards;\n**(5)**\ninclude a description of the weather conditions for the fireshed that would comprise severe fire weather conditions; and\n**(6)**\ninclude other prefire planning provisions relevant to wildfire response, at the discretion of the Secretary concerned.\n##### (c) Wildfire consideration during land management planning\nTo the maximum extent practicable, the Secretary concerned shall include, on a team carrying out any development or revision of a resource management plan for Federal land containing 1 more firesheds, an employee that was involved in the development of the spatial fire management policies for that fireshed.\n#### 104. Study and report on integrating local firefighters into wildfire response\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Homeland Security, acting through the Administrator of the U.S. Fire Administration and in coordination with the National Wildfire Coordinating Group, shall\u2014\n**(1)**\nconduct a study on the gaps in training for structural firefighters in high wildfire risk areas; and\n**(2)**\nsubmit to the congressional committees a report describing the results of the study conducted under paragraph (1).\n##### (b) Inclusions\nThe report submitted under subsection (a)(2) shall include\u2014\n**(1)**\na summary of existing coordination practices between Federal wildland firefighters and State, local, or Tribal firefighters;\n**(2)**\nan analysis of the differences in best response practices for State, local, or Tribal firefighters when responding to a fire incident that threatens a single structure as compared to a wildfire that threatens a community;\n**(3)**\nexisting training modules, or gaps in existing training modules, available through the National Fire Academy to train State, local, or Tribal firefighters on best response practices for a wildfire that threatens a community; and\n**(4)**\nan estimated cost and spending plan to address any gaps in existing training modules described in paragraph (3).\nII\nWildfire detection and suppression support\n#### 201. Wildfire detection equipment\nTo the extent practicable, the Secretary concerned shall\u2014\n**(1)**\nexpedite the placement of wildfire detection equipment, such as sensors, cameras, and other relevant equipment, in areas at risk of wildfire;\n**(2)**\nexpand the use of satellite data to improve wildfire detection and response;\n**(3)**\nexpedite any permitting required by the Secretary concerned for the installation, maintenance, or removal of wildfire detection equipment;\n**(4)**\nuse unmanned aerial vehicles to assess wildland fires in their incipient stages to determine the appropriate initial response actions;\n**(5)**\nreview permitting described in paragraph (3) and procurement requirements for wildfire detection equipment within the context of modern and innovative technology; and\n**(6)**\nannually provide a forum for companies engaging in the development and testing of emergent wildland fire technology to engage with wildland fire managers.\n#### 202. Slip-on tanker units\n##### (a) Financial assistance for acquisition of firefighting slip-on tanker units\nSection 40803(c)(5) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592(c)(5) ) is amended by inserting and Indian Tribes after local governments .\n##### (b) Reporting requirement\n**(1) In general**\nThe Secretary of the Interior shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives an annual report on the implementation of section 40803(c)(5) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592(c)(5) ), including a description of\u2014\n**(A)**\nthe total number of slip-on tanker units purchased with financial assistance provided by the Secretary of the Interior under that section in the preceding year, by State;\n**(B)**\nthe number of requests received by the Secretary of the Interior for financial assistance under that section to purchase slip-on tanker units in the preceding year; and\n**(C)**\nany barriers identified by the Secretary of the Interior to the ability of local governments and Indian Tribes to participate in the pilot program established under that section.\n**(2) Timing**\n**(A) Initial report**\nThe Secretary of the Interior shall submit the first report required under paragraph (1) not later than October 1, 2026.\n**(B) Sunset**\nThe requirements of this subsection shall expire on October 1, 2028.\n##### (c) Integration into wildfire response\nThe Secretaries, in coordination with recipients of financial assistance for slip-on tanker units provided under section 40803(c)(5) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592(c)(5) ), shall\u2014\n**(1)**\nin coordination with the Administrator of the U.S. Fire Administration, promulgate guidance for the mobilization of slip-on tanker units for wildfire response;\n**(2)**\nas practicable, incorporate mobilized slip-on tanker units into resource tracking systems; and\n**(3)**\ncollaborate with the Administrator of the U.S. Fire Administration regarding any necessary training for operators of slip-on tanker units.\n#### 203. Research and development of unmanned aircraft system fire applications\n##### (a) Definition of unmanned aircraft system\nIn this section, the term unmanned aircraft system means an unmanned aircraft and associated elements (including, if applicable, communication links and the components that control the unmanned aircraft) that are required for the operator to operate safely and efficiently.\n##### (b) Research\nThe Secretaries shall, acting through the Joint Fire Science Program, work with universities and other research institutions to carry out research and development on the wildfire response applications of unmanned aircraft systems.\n##### (c) Testing\nThe Secretaries may coordinate with the Administrator of the Federal Aviation Administration to test an unmanned aircraft system developed under this section at an unmanned aircraft test range in accordance with section 44803 of title 49, United States Code.\n##### (d) Authorization of appropriations\nThere are authorized to be appropriated to the Secretaries such sums as are necessary to carry out this section.\n#### 204. Study on drone incursions on wildfire suppression\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Federal Aviation Administration.\n**(2) Drone**\nThe term drone means an unmanned aircraft system owned by a private individual or entity.\n**(3) Drone incursion**\nThe term drone incursion means the operation of a drone within any airspace for which the Administrator has issued a temporary flight restriction because of a wildfire.\n##### (b) Study required\nThe Administrator, in consultation with the Secretary of the Interior and the Secretary of Agriculture, acting through the Chief of the Forest Service, shall conduct a study on the effects of drone incursions on wildfire suppression with respect to land managed by the Department of the Interior or the Department of Agriculture.\n##### (c) Study contents\nIn conducting the study required under subsection (b), the Administrator shall\u2014\n**(1)**\ndetermine, for each of the 5 most recent calendar years\u2014\n**(A)**\nthe number of occurrences in which a drone incursion interfered with wildfire suppression; and\n**(B)**\nthe estimated effect of each occurrence described in subparagraph (A) on\u2014\n**(i)**\nthe length of time required to achieve complete suppression;\n**(ii)**\nany associated delay in the fielding of aerial firefighting response units; and\n**(iii)**\nthe amounts expended by the Federal Government; and\n**(2)**\nevaluate the feasibility and effectiveness of various actions to prevent drone incursions, including\u2014\n**(A)**\nthe use of counter-drone radio towers;\n**(B)**\nthe use of reasonable force to disable, damage, or destroy a drone;\n**(C)**\nthe seizure of a drone, including seizure with a net device; and\n**(D)**\nthe dissemination of educational materials relating to the effects of drone incursions on wildfire suppression.\n##### (d) Report\nNot later than 18 months after the date of enactment of this Act, the Administrator shall submit to the congressional committees, the Committee on Commerce, Science, and Transportation of the Senate, and the Committee on Transportation and Infrastructure of the House of Representatives a report describing\u2014\n**(1)**\nthe findings of the study required under subsection (b); and\n**(2)**\nany recommendations relating to those findings.\n#### 205. Study on modernizing wildfire response technologies\n##### (a) In general\nThe Secretaries shall conduct a study on\u2014\n**(1)**\nnecessary improvements to radio communications systems and infrastructure during wildland fire or prescribed fire operations, including\u2014\n**(A)**\nan assessment of the quality and reliability of existing radio infrastructure;\n**(B)**\nfor any instance in which existing radio communications infrastructure has failed, an assessment of the impacts on forest management or wildfire response activities;\n**(C)**\na comparison of existing options to improve on-the-ground communications; and\n**(D)**\na cost analysis and estimated timeline to install the most feasible option identified under subparagraph (C);\n**(2)**\nreal-time or near-real-time situational awareness tools for operational firefighters, including\u2014\n**(A)**\nstandards and requirements for such tools to ensure interoperability between Federal firefighting entities and applicable State, local, Tribal, or other partners;\n**(B)**\nany requirements for additional remote sensing and mapping capabilities to fully leverage such situational awareness tools; and\n**(C)**\na cost comparison between commercially available systems and internally developed systems; and\n**(3)**\nwildland fire predictive modeling, including\u2014\n**(A)**\nan analysis of the data required to reduce predictive error for existing or developing models;\n**(B)**\nan analysis of computing needs to more swiftly or accurately model wildland fire using existing or developing models;\n**(C)**\nthe feasibility of using artificial intelligence for wildland fire modeling; and\n**(D)**\nexisting or developing wildland fire predictive models that could assist with establishing safe conditions for igniting a prescribed fire.\n##### (b) Submission and public availability\nNot later than 1 year after the date of enactment of this Act, the Secretaries shall submit to the congressional committees and make publicly available the results of the study conducted under subsection (a).\nIII\nPost-fire recovery support\n#### 301. Funding for online guides for post-disaster assistance\n##### (a) Use of services of other agencies\nSection 201(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5131(a) ) is amended\u2014\n**(1)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(2)**\nby adding at the end the following:\n(8) post-disaster assistance. .\n##### (b) Funding for online guides for assistance\nSection 201 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5131 ) is amended by adding at the end the following:\n(e) Funding for online guides for assistance (1) In general The Administrator of the Federal Emergency Management Agency may enter into cooperative agreements to provide funding or technical assistance to a State agency designated or established under subsection (c) to establish, update, or operate a website to provide information relating to post-disaster recovery funding and resources to a community or an individual impacted by a major disaster or emergency. (2) Management A website established, updated, or operated under this subsection shall be\u2014 (A) managed by the State agency; and (B) suitable for the residents of the State of the State agency. (3) Content The Administrator may provide funding to a State agency under this subsection to establish, update, or operate a website that provides only 1 or more of the following: (A) A list of Federal, State, and local sources of post-disaster recovery funding or assistance that may be available to a community after a disaster or emergency. (B) A list of Federal, State, and local sources of post-disaster recovery funding or assistance that may be available to an individual impacted by a major disaster or emergency. (C) A technical guide that lists and explains the costs and benefits of alternatives available to a community to mitigate the impacts of a major disaster or emergency and prepare for sequential hazards, such as flooding after a wildfire. (4) Cooperation A State agency that receives funding or technical assistance to establish, update, or operate a website under this subsection shall cooperate with the Secretary of the Interior, the Secretary of Agriculture, the Secretary of Housing and Urban Development, the Administrator of the Small Business Administration, and the Administrator of the Federal Emergency Management Agency in establishing, updating, or operating the website under this subsection. (5) Updates A State agency that receives funding to establish, update, or operate a website under this subsection shall update the website not less frequently than once every 180 days. .\n#### 302. Post-fire management and recovery\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary concerned shall establish 1 or more permanent Burned Area Emergency Response Teams (referred to in this section as a BAER Team ) to coordinate immediate post-wildfire emergency stabilization and erosion planning efforts.\n##### (b) Requirements\nA BAER Team shall\u2014\n**(1)**\nsurvey the landscape affected by a wildfire to determine burn severity;\n**(2)**\nidentify and remove, as necessary, dead or dying trees that may pose an immediate hazard to individuals, communities, or critical infrastructure;\n**(3)**\nstabilize or remove hazardous materials resulting from a wildfire that may pose an immediate hazard to individuals, communities, or the environment;\n**(4)**\nconduct emergency landscape stabilization and erosion prevention work, prioritizing efforts that ensure public safety;\n**(5)**\nprevent the proliferation and spread of invasive species;\n**(6)**\nassist with informing the public of hazards resulting from a wildfire;\n**(7)**\ncollaborate, as necessary, with activities under section 303; and\n**(8)**\nconduct such other work as the Secretary concerned determines to be necessary.\n##### (c) Duration\nTo the maximum extent practicable, a BAER Team shall coordinate and respond to immediate post-wildfire emergency stabilization and erosion planning needs for a period of not more than 1 year after the date of containment of a wildfire.\n##### (d) Funding\nThe Secretary concerned may use to carry out this section funds made available by section 40803(c)(16) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592(c)(16) ).\n#### 303. Long-Term Burned Area Rehabilitation account\n##### (a) Establishment of account\nThere is established in the Treasury of the United States the Long-Term Burned Area Rehabilitation account for the Department of Agriculture.\n##### (b) Authorization of appropriations\nThere are authorized to be appropriated for fiscal year 2025 and each fiscal year thereafter for the account established by subsection (a) such sums as are necessary to carry out the activities described in subsection (d), not to exceed $100,000,000.\n##### (c) Presidential budget requests\nFor fiscal year 2026 and each fiscal year thereafter, the Secretary of Agriculture shall submit through the budget request of the President and in accordance with subsection (b), a request for amounts in the National Forest System appropriation account to carry out the activities described in subsection (d).\n##### (d) Authorized activities\nThe Secretary of Agriculture shall use amounts in the account established by subsection (a) for rehabilitation projects located at sites impacted by a wildfire or post-wildfire flooding primarily on Federal land, but may include areas on non-Federal land, that\u2014\n**(1)**\nrestore the functions of an ecosystem, including\u2014\n**(A)**\nidentifying areas where natural regeneration is unlikely to occur;\n**(B)**\nrevegetation and reforestation, including coordinating any necessary site preparation, salvage harvesting, and replanting;\n**(C)**\nwatershed restoration;\n**(D)**\ninvasive species mitigation and removal; and\n**(E)**\nwildlife habitat restoration; or\n**(2)**\nrepair or replace infrastructure or facilities critical for land management activities.\n##### (e) Duration of activities\nA rehabilitation project under subsection (d) shall\u2014\n**(1)**\nbegin not earlier than the date on which the wildfire was contained; and\n**(2)**\nbe completed not later than 5 years after the date on which the wildfire was contained.\n##### (f) Agreement authority\n**(1) In general**\nThe Secretary of Agriculture may enter to agreements with non-Federal entities to carry out activities described in subsection (d).\n**(2) Cost share**\nThe non-Federal share of the costs of implementing activities under an agreement entered into under paragraph (1)\u2014\n**(A)**\nshall be not more than 20 percent; and\n**(B)**\nmay include in-kind contributions.\n**(3) Savings provision**\nNothing in this subsection\u2014\n**(A)**\nrequires the Secretary of Agriculture to enter into agreements with non-Federal entities to carry out activities described in subsection (d); or\n**(B)**\nlimits the effect of the prioritization requirements under subsection (g).\n##### (g) Prioritization of funding\nThe Secretary of Agriculture shall prioritize, on a nationwide basis, projects for which funding requests are submitted under this section based on downstream effects on water resources.\n##### (h) Reporting\nBeginning in fiscal year 2027, and each fiscal year thereafter, the Secretary of Agriculture shall annually submit to Congress a report on the burned area recovery work performed using\u2014\n**(1)**\namounts from the account established by subsection (a);\n**(2)**\namounts made available under the Act of June 9, 1930 ( 16 U.S.C. 576 et seq. ); and\n**(3)**\namounts from the Reforestation Trust Fund established by section 303(a) of Public Law 96\u2013451 ( 16 U.S.C. 1606a(a) ).\n#### 304. Prize for wildfire-related invasive species reduction\nSection 7001(d) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( 16 U.S.C. 742b note; Public Law 116\u20139 ) is amended\u2014\n**(1)**\nby striking paragraph (8)(A) each place it appears and inserting paragraph (9)(A) ;\n**(2)**\nby striking paragraph (8)(B) each place it appears and inserting paragraph (9)(B) ;\n**(3)**\nby redesignating paragraph (8) as paragraph (9);\n**(4)**\nby inserting after paragraph (7) the following:\n(8) Theodore roosevelt genius prize for management of wildfire-related invasive species (A) Definitions In this paragraph: (i) Board The term Board means the Management of Wildfire-Related Invasive Species Technology Advisory Board established by subparagraph (C)(i). (ii) Prize competition The term prize competition means the Theodore Roosevelt Genius Prize for the management of wildfire-related invasive species established under subparagraph (B). (B) Authority Not later than 180 days after the date of enactment of the Western Wildfire Support Act of 2025 , the Secretary shall establish under section 24 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3719 ) a prize competition, to be known as the Theodore Roosevelt Genius Prize for the management of wildfire-related invasive species \u2014 (i) to encourage technological innovation with the potential to advance the mission of the National Invasive Species Council with respect to the management of wildfire-related invasive species; and (ii) to award 1 or more prizes annually for a technological advancement that manages wildfire-related invasive species. (C) Advisory board (i) Establishment There is established an advisory board, to be known as the Management of Wildfire-Related Invasive Species Technology Advisory Board . (ii) Composition The Board shall be composed of not fewer than 9 members appointed by the Secretary, who shall provide expertise in\u2014 (I) invasive species; (II) biology; (III) technology development; (IV) engineering; (V) economics; (VI) business development and management; (VII) wildfire; and (VIII) any other discipline, as the Secretary determines to be necessary to achieve the purposes of this paragraph. (iii) Duties Subject to clause (iv), with respect to the prize competition, the Board shall\u2014 (I) select a topic; (II) issue a problem statement; (III) advise the Secretary regarding any opportunity for technological innovation to manage wildfire-related invasive species; and (IV) advise winners of the prize competition regarding opportunities to pilot and implement winning technologies in relevant fields, including in partnership with conservation organizations, Federal or State agencies, federally recognized Indian Tribes, private entities, and research institutions with expertise or interest relating to the management of wildfire-related invasive species. (iv) Consultation In selecting a topic and issuing a problem statement for the prize competition, the Board shall consult widely with Federal and non-Federal stakeholders, including\u2014 (I) 1 or more Federal agencies with jurisdiction over the management of invasive species; (II) 1 or more Federal agencies with jurisdiction over the management of wildfire; (III) 1 or more State agencies with jurisdiction over the management of invasive species; (IV) 1 or more State agencies with jurisdiction over the management of wildfire; (V) 1 or more State, regional, or local wildlife organizations, the mission of which relates to the management of invasive species; and (VI) 1 or more wildlife conservation groups, technology companies, research institutions, institutions of higher education, industry associations, or individual stakeholders with an interest in the management of wildfire-related invasive species. (v) Requirements The Board shall comply with all requirements under paragraph (9)(A). (D) Administration by the national invasive species council The Secretary, acting through the Executive Director of the National Invasive Species Council, shall administer the prize competition and perform the duties described in paragraph (9)(B)(i). (E) Judges (i) Appointment The Secretary shall appoint not fewer than 3 judges who shall, except as provided in clause (ii), select the 1 or more annual winners of the prize competition. (ii) Determination by secretary The judges appointed under clause (i) shall not select any annual winner of the prize competition if the Secretary makes a determination that, in any fiscal year, none of the technological advancements entered into the prize competition merits an award. (F) Report to congress Not later than 60 days after the date on which a cash prize is awarded under this paragraph, the Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives a report on the prize competition that includes\u2014 (i) a statement by the Board that describes the activities carried out by the Board relating to the duties described in subparagraph (C)(iii); (ii) a description of the 1 or more annual winners of the prize competition; and (iii) a statement by 1 or more of the judges appointed under subparagraph (E) that explains the basis on which the 1 or more winners of the prize competition was selected. (G) Termination of authority The Board and all authority provided under this paragraph shall terminate on December 31, 2028. ; and\n**(5)**\nin paragraph (9) (as so redesignated)\u2014\n**(A)**\nin subparagraph (A), in the matter preceding clause (i), by striking or (7)(C)(i) and inserting (7)(C)(i), or (8)(C)(i) ; and\n**(B)**\nin subparagraph (C)\u2014\n**(i)**\nin clause (i), by inserting and the amount of the initial cash prize awarded for a year under paragraph (8) after subparagraph (B)(i)(IX) ; and\n**(ii)**\nby adding at the end the following:\n(iii) Additional wildfire cash prizes If the Secretary determines that funds are available for an additional cash prize under the prize competition under paragraph (8) for a year, the Secretary shall determine the amount of the additional cash prize. .",
      "versionDate": "2025-01-14",
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
        "actionDate": "2025-12-01",
        "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management."
      },
      "number": "5782",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Western Wildfire Support Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Accounting and auditing",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Appropriations",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Atmospheric science and weather",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-12-04T16:36:07Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-04T16:36:07Z"
          },
          {
            "name": "Department of Agriculture",
            "updateDate": "2025-12-04T16:36:07Z"
          },
          {
            "name": "Department of the Interior",
            "updateDate": "2025-12-04T16:36:07Z"
          },
          {
            "name": "Disaster relief and insurance",
            "updateDate": "2025-12-04T16:36:07Z"
          },
          {
            "name": "Ecology",
            "updateDate": "2025-12-04T16:36:07Z"
          },
          {
            "name": "Emergency planning and evacuation",
            "updateDate": "2025-12-04T16:36:07Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-12-04T16:36:07Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-12-04T16:36:07Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-12-04T16:36:07Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Military education and training",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Military operations and strategy",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2025-12-04T16:36:08Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-12-04T16:36:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-01T20:06:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119s91",
          "measure-number": "91",
          "measure-type": "s",
          "orig-publish-date": "2025-01-14",
          "originChamber": "SENATE",
          "update-date": "2025-08-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s91v00",
            "update-date": "2025-08-18"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Western Wildfire Support Act of 2025\u00a0</strong></p><p>This bill addresses wildfires by authorizing post-fire recovery activities, supporting adoption of technology, and requiring additional federal coordination.</p><p>The bill authorizes federal wildfire response and recovery activities by</p><ul><li>providing statutory authority for Burned Area Emergency Response Teams to coordinate emergency stabilization and erosion planning, and</li><li>establishing an account to fund federal rehabilitation projects in areas impacted by a wildfire (e.g., ecosystem restoration, replacing infrastructure critical for land management).</li></ul><p>Additionally, for all hazard types, the bill includes post-disaster assistance in the federal disaster preparedness program and authorizes assistance to states for operating websites to provide information on post-disaster recovery resources.</p><p>The bill requires federal agencies to develop and utilize technologies for managing wildfires by</p><ul><li>expediting the permitting and use of wildfire detection equipment (e.g., sensors, cameras);</li><li>providing funding to Indian tribes for slip-on tanker units that convert vehicles into fire engines;</li><li>performing research and development on wildfire response applications of unmanned aircraft systems (e.g., drones);</li><li>studying radio communications systems, situational awareness tools, and\u00a0wildland fire predictive modeling; and</li><li>administering a prize competition for technological innovation for managing wildfire-related invasive species.</li></ul><p>The bill directs federal agencies to plan and coordinate on wildfire management by</p><ul><li>incorporating the best available science and planning tools into spatial fire management policies for federal lands, \u00a0</li><li>collaborating with state agencies for mutual aid in fire suppression (including reimbursing states for suppressing fires caused by military operations), and\u00a0</li><li>studying training gaps for integrating structural (e.g., local) firefighters into wildfire response.</li></ul>"
        },
        "title": "Western Wildfire Support Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s91.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Western Wildfire Support Act of 2025\u00a0</strong></p><p>This bill addresses wildfires by authorizing post-fire recovery activities, supporting adoption of technology, and requiring additional federal coordination.</p><p>The bill authorizes federal wildfire response and recovery activities by</p><ul><li>providing statutory authority for Burned Area Emergency Response Teams to coordinate emergency stabilization and erosion planning, and</li><li>establishing an account to fund federal rehabilitation projects in areas impacted by a wildfire (e.g., ecosystem restoration, replacing infrastructure critical for land management).</li></ul><p>Additionally, for all hazard types, the bill includes post-disaster assistance in the federal disaster preparedness program and authorizes assistance to states for operating websites to provide information on post-disaster recovery resources.</p><p>The bill requires federal agencies to develop and utilize technologies for managing wildfires by</p><ul><li>expediting the permitting and use of wildfire detection equipment (e.g., sensors, cameras);</li><li>providing funding to Indian tribes for slip-on tanker units that convert vehicles into fire engines;</li><li>performing research and development on wildfire response applications of unmanned aircraft systems (e.g., drones);</li><li>studying radio communications systems, situational awareness tools, and\u00a0wildland fire predictive modeling; and</li><li>administering a prize competition for technological innovation for managing wildfire-related invasive species.</li></ul><p>The bill directs federal agencies to plan and coordinate on wildfire management by</p><ul><li>incorporating the best available science and planning tools into spatial fire management policies for federal lands, \u00a0</li><li>collaborating with state agencies for mutual aid in fire suppression (including reimbursing states for suppressing fires caused by military operations), and\u00a0</li><li>studying training gaps for integrating structural (e.g., local) firefighters into wildfire response.</li></ul>",
      "updateDate": "2025-08-18",
      "versionCode": "id119s91"
    },
    "title": "Western Wildfire Support Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Western Wildfire Support Act of 2025\u00a0</strong></p><p>This bill addresses wildfires by authorizing post-fire recovery activities, supporting adoption of technology, and requiring additional federal coordination.</p><p>The bill authorizes federal wildfire response and recovery activities by</p><ul><li>providing statutory authority for Burned Area Emergency Response Teams to coordinate emergency stabilization and erosion planning, and</li><li>establishing an account to fund federal rehabilitation projects in areas impacted by a wildfire (e.g., ecosystem restoration, replacing infrastructure critical for land management).</li></ul><p>Additionally, for all hazard types, the bill includes post-disaster assistance in the federal disaster preparedness program and authorizes assistance to states for operating websites to provide information on post-disaster recovery resources.</p><p>The bill requires federal agencies to develop and utilize technologies for managing wildfires by</p><ul><li>expediting the permitting and use of wildfire detection equipment (e.g., sensors, cameras);</li><li>providing funding to Indian tribes for slip-on tanker units that convert vehicles into fire engines;</li><li>performing research and development on wildfire response applications of unmanned aircraft systems (e.g., drones);</li><li>studying radio communications systems, situational awareness tools, and\u00a0wildland fire predictive modeling; and</li><li>administering a prize competition for technological innovation for managing wildfire-related invasive species.</li></ul><p>The bill directs federal agencies to plan and coordinate on wildfire management by</p><ul><li>incorporating the best available science and planning tools into spatial fire management policies for federal lands, \u00a0</li><li>collaborating with state agencies for mutual aid in fire suppression (including reimbursing states for suppressing fires caused by military operations), and\u00a0</li><li>studying training gaps for integrating structural (e.g., local) firefighters into wildfire response.</li></ul>",
      "updateDate": "2025-08-18",
      "versionCode": "id119s91"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s91is.xml"
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
      "title": "Western Wildfire Support Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Western Wildfire Support Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve Federal activities relating to wildfires, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:41Z"
    }
  ]
}
```
