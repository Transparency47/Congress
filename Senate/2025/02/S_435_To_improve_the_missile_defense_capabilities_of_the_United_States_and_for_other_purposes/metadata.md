# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/435?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/435
- Title: IRONDOME Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 435
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2026-04-09T15:26:36Z
- Update date including text: 2026-04-09T15:26:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/435",
    "number": "435",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "IRONDOME Act of 2025",
    "type": "S",
    "updateDate": "2026-04-09T15:26:36Z",
    "updateDateIncludingText": "2026-04-09T15:26:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
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
      "actionDate": "2025-02-05",
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
          "date": "2025-02-06T00:17:08Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "ND"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s435is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 435\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Sullivan (for himself and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo improve the missile defense capabilities of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Increasing Response Options and Deterrence of Missile Engagements Act of 2025 or the IRONDOME Act of 2025 .\n#### 2. Findings; sense of the Senate\n##### (a) Findings\n**(1) Missile Defense review**\nCongress finds that the 2022 Missile Defense Review found the following:\n**(A)**\nSince the release of the 2019 Missile Defense Review, missile-related threats have rapidly expanded in quantity, diversity, and sophistication.\n**(B)**\nUnited States national security interests are increasingly at risk from wide-ranging missile arsenals that include offensive ballistic, cruise, and hypersonic weapons.\n**(C)**\nIn support of the homeland missile defense mission, continued modernization and expansion of the Ground-based Midcourse Defense (GMD) system will remain an essential element of our comprehensive missile defeat approach. In addition, the United States will also continue to improve defensive capabilities to address the threat of evolving cruise missile strikes by any adversary against the homeland.\n**(D)**\nThe continued evolution and progress of missiles as a principal means by which adversaries seek to project conventional or nuclear military power makes missile defense a core deterrence-by-denial component of an integrated deterrence strategy.\n**(E)**\nMissile defense capabilities add resilience and undermine adversary confidence in missile use by introducing doubt and uncertainty into strike planning and execution, reducing the incentive to conduct small-scale coercive attacks, decreasing the probability of attack success, and raising the threshold of conflict.\n**(2) Congressional Commission on the Strategic Posture of the United States**\nCongress finds that, in its October 2023 report, the Congressional Commission on the Strategic Posture of the United States recommended the following:\n**(A)**\nThe United States should develop and field homeland integrated air and missile defense (IAMD) that can deter and defeat coercive attacks by Russia and China, and determine the capabilities needed to stay ahead of the North Korean threat.\n**(B)**\nThe Secretary of Defense should direct research, development, test and evaluation into advanced integrated air and missile defense capabilities leveraging all domains, including land, sea, air, and space. These activities should focus on sensor architectures, integrated command and control, interceptors, cruise and hypersonic missile defenses, and area or point defenses. The Department of Defense should urgently pursue deployment of any capabilities that prove feasible.\n**(C)**\nThe Secretary and the military departments should transfer operations and sustainment responsibility for missile defense to the appropriate military departments by October 1, 2024, to allow the Missile Defense Agency (MDA) to focus on research, development, prototyping, and testing.\n**(3) Commission on the National Defense Strategy**\nCongress finds the following:\n**(A)**\nIn its July 2024 report, the Commission on the National Defense Strategy found the following:\n**(i)**\nThere is an increasing threat from expanding ability of China, Russia, and North Korea to deliver nuclear weapons against the United States, including the territories of the United States.\n**(ii)**\nThe military planners of the Department of Defense and United States Northern Command need to prepare for a worst-case scenario in which nuclear and other strikes are launched against the United States, which could be done in large numbers with specialized delivery systems.\n**(B)**\nIn the report described in subparagraph (A), the Commission shared the same threat assessment about missile attacks as the Commission on the Strategic Posture of the United States and agreed with the recommendation that the United States should enhance missile defense for the homeland.\n**(4) Policy**\nCongress finds that it is the policy of the Federal Government that \u2014\n**(A)**\nthe Federal Government will provide for the common defense of the citizens of the United States and the United States by deploying and maintaining a next-generation missile defense shield;\n**(B)**\nthe Federal Government will deter and defend the citizens and critical infrastructure of the United States against any foreign attack on the United States homeland; and\n**(C)**\nthe Federal Government will guarantee the secure second-strike capability of the Federal Government.\n##### (b) Sense of the Senate\nIt is the sense of the Senate that\u2014\n**(1)**\nthe threat of attack by ballistic, cruise, and hypersonic missiles remains a catastrophic threat facing the United States and defense against it is a form of both national security and border security;\n**(2)**\nChina is rapidly expanding and modernizing its conventional forces to include ballistic missile systems posing an increasing threat to citizens, forces, and allies of the United States;\n**(3)**\nover the past 40 years, rather than lessening, the threat from next-generation strategic weapons, including hypersonic, has become more complex with the development of next-generation delivery systems by adversaries of the United States;\n**(4)**\nnotwithstanding this increasing threat, homeland missile defense policy of the United States has been severely limited to staying ahead of rogue nation threats and accidental or unauthorized missile launches;\n**(5)**\nby empowering the United States with a second-strike capability, the Iron Dome will deter adversaries from attacks on the homeland;\n**(6)**\nthe midcourse defense system is the primary system capable of defending the United States homeland from long-range ballistic missile threats and is critical to our national security;\n**(7)**\nthe Next Generation Interceptor is a top priority for the Missile Defense Agency and a critical element to increasing system reliability to build warfighter competence; and\n**(8)**\nthe United States must gain and maintain total domain awareness to provide early warning and defeat of missile threats from both the northern and southern hemispheres and from outer space.\n#### 3. Definitions\nIn this Act:\n**(1) Congressional defense committees**\nThe term congressional defense committees has the meaning given such term in section 101(a) of title 10, United States Code.\n**(2) Secretary**\nThe term Secretary means the Secretary of Defense.\n#### 4. Improving United States missile defense capabilities\n##### (a) Plan for transfer of operations and sustainment of missile defense to the military departments\n**(1) Plan required**\nNot later than 120 days after the date of the enactment of this Act, the Secretary shall submit to Congress a multi-year phased plan to transfer operations and sustainment responsibility for missile defense from the Missile Defense Agency to the appropriate military departments to allow the Missile Defense Agency to focus on research, development, and prototyping and testing.\n**(2) Execution of plan**\nThe Secretary shall execute the plan submitted pursuant to paragraph (1) pursuant to a specific authorization of such plan enacted after the date of the enactment of this Act.\n##### (b) Middle-Tier acquisition program for drone-Based missile threat audio detection system\nThe Commander of United States Northern Command shall use a process for conducting a middle tier acquisition described in section 3602 of title 10, United States Code, as added by section 804 of the Servicemember Quality of Life Improvement and National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ), for rapid fielding and prototyping of a drone-based network for both forward deployed armed forces and homeland defense capable of detecting through audio sensing technology the approach of advanced missiles, including advanced cruise missiles and hypersonic missiles.\n##### (c) Middle-Tier acquisition program for proliferated warfighter space architecture of Space Development Agency\nThe Director of the Space Development Agency shall use a process for conducting a middle tier acquisition described in section 3602 of title 10, United States Code, as added by section 804 of the Servicemember Quality of Life Improvement and National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ), for rapid fielding of satellites and associated systems for tranches 3, 4, and 5 of the proliferated warfighter space architecture of the Agency.\n##### (d) Requirement for next generation interceptor fielding and silo construction\nThe Secretary shall take such actions as may be necessary to expand Next Generation Interceptor production and silo construction at Fort Greely, Alaska, to field a minimum of 80 interceptors at Fort Greely for defense of the United States to be completed not later than January 1, 2038.\n##### (e) Requirement for combatant commands To account for missile defense interceptors and sensor requirements in their annual requests\nFor each fiscal year beginning after the date of the enactment of this Act, each commander of a combatant command shall include the missile defense interceptor requirements, terrestrial-based sensor requirements, and space-based sensor requirements of the combatant command of the commander in the supporting information for the Department of Defense submitted along with the budget of the President to Congress for such fiscal year pursuant to section 1105(a) of title 31, United States Code.\n##### (f) Accelerating development of Glide Phase Interceptor\n**(1) Use of authorities to accelerate development**\nThe Secretary shall use all authorities available to the Secretary to accelerate development of the Glide Phase Interceptor to defend against hypersonic threats to the United States homeland.\n**(2) Report on potential for parallel development**\nNot later than one year after the date of the enactment of this Act, the Director of the Missile Defense Agency shall submit to the Secretary a report on the potential for parallel development of capabilities, revised program schedule, and the risk associated with pursuing only one alternative for the Glide Phase Interceptor.\n##### (g) Accelerating production and fielding of Terminal High Altitude Area Defense system\nThe Secretary shall use all authorities available to the Secretary to accelerate the production and fielding of the Terminal High Altitude Area Defense (THAAD) system (including AN/TPY\u20132 radars) for forward deployment and homeland defense as the Secretary and President consider appropriate.\n##### (h) Accelerating development of autonomous agents To defend against cruise missiles and drones\nThe Secretary shall use all authorities available to the Secretary to accelerate development of autonomous agents to cost-effectively defend the United States homeland and forward-deployed armed forces against raids of both large cruise missiles and drones.\n##### (i) Accelerating development and deployment of space-Based interceptors\nThe Secretary shall use all authorities available to the Secretary to accelerate development and deployment of proliferated space-based interceptors capable of boost-phase intercept.\n##### (j) Report To reduce cost savings per round for space-Based interceptors\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense shall submit a feasibility study to the congressional defense committees outlining multiple methods for reducing the cost per round of various space-based interceptors including kinetic and non-kinetic capabilities.\n##### (k) Accelerating modernization of certain terrestrial domain capabilities\nThe Secretary shall use all authorities available to the Secretary to accelerate modernization of terrestrial-based radar capabilities, including those located at or known as Cobra Dane, Thule Ballistic Missile Early Warning System (BMEWS), Upgraded Early Warning Radar (UEWR) in Greenland and Cape Cod, Homeland Defense Radar in Hawaii, and the Alaska Radar System.\n##### (l) Modernization of Perimeter Acquisition Radar Attack Characterization System\nThe Secretary shall use all authorities available to the Secretary to accelerate the modernization and digitization of the Perimeter Acquisition Radar Attack Characterization System (PARCS) to improve detection of intercontinental and sea-launched missile threats, as well as improve space domain awareness capabilities.\n##### (m) Site selection and program execution plan for southern hemisphere-Facing early warning radar system\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall submit to Congress a report detailing a site selection and proposed program execution plan for a southern hemisphere-facing early warning radar system capable of detecting threats from next generation complex missile attacks.\n##### (n) Site selection and program execution plan for construction of east coast-Based Aegis Ashore system\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall submit to Congress a report detailing a site selection and proposed program execution plan for an east coast-based Aegis Ashore missile defense system.\n##### (o) Site selection and program execution plan for construction of Alaska-Based Aegis Ashore system\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall submit to Congress a report detailing a site selection and proposed program execution plan for an Alaska-based Aegis Ashore missile defense system.\n##### (p) Completion and certification of Aegis Ashore system in Hawaii\nThe Secretary shall use all authorities available to the Secretary to accelerate completion and certification of an Aegis Ashore system based in Hawaii.\n##### (q) Acceleration of munitions production for missile defense\nThe Secretary shall use all authorities available to the Secretary to accelerate production of critical munitions used for missile interception, including Standard Missile 3 Blocks IB and IIA and PAC\u20132 and PAC\u20133 munitions.\n##### (r) Expedited military construction authority\n**(1) Waiver of regulations**\nThe Secretary may waive any and all regulations, including environmental regulations, that the Secretary determines would slow down, impede, block, or otherwise hinder the construction, upgrade, or modernization of infrastructure supporting a Joint Urgent Operational Need (JUON) associated with homeland or forward deployed missile defense.\n**(2) Congressional notice**\nWhenever the Secretary uses the authority provided by paragraph (1), the Secretary shall, not later than 45 days after using the authority, submit to the congressional defense committees notice of such use.\n##### (s) Acceleration of integrated air and missile defense technology exchanges\n**(1) In general**\nThe Secretary shall, in collaboration with the Secretary of State, look for and exploit opportunities to accelerate technology exchanges and transfers of integrated missile defense technology, including over the horizon radar with trusted allies under current defense agreements and arrangements.\n**(2) Rule of construction**\nNothing in this subsection shall be construed to require the Secretary to exchange technology with a foreign country if the President or the Secretary determines that doing so would present a grave national security threat to the United States.\n##### (t) Development and securing of supply chains critical to missile defense\nThe Secretary shall, in collaboration with the Secretary of State, the Secretary of Commerce, and the Secretary of the Interior, identify critical shortages and vulnerabilities in supply chains critical to missile defense component production and shall use all authorities available to the Secretaries to develop and secure such supply chains.\n##### (u) Requirement for procurement and fielding of dirigibles T o support missile defense\n**(1) In general**\nThe Secretary of the Army shall procure and field dirigibles, including airships and aerostats, in support of the missile defense of the United States homeland from ballistic, hypersonic, and cruise missiles, and drones.\n**(2) Requirements**\nThe requirements of paragraph (1) cover\u2014\n**(A)**\nhigh altitude air defense systems to detect, characterize, track, and engage current and emerging advanced missile threats; and\n**(B)**\nboth short-term and long-term solutions that leverage the innovative dirigible and associated sensor development that the Armed Forces, partners of the United States, such as Israel, and United States industry have undertaken during the 30-year period ending on the date of the enactment of this Act.\n**(3) Consideration**\nIn carrying out paragraph (1), the Secretary of the Army shall consider the use of dirigibles in supporting resilient military and emergency communication networks in a crisis.\n#### 5. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $19,548,100,000 for fiscal year 2026, of which\u2014\n**(1)**\n$500,000,000 shall be available for requirements of this Act relating to SM\u20133 Block 1B;\n**(2)**\n$500,000,000 shall be available for requirements of this Act relating to SM\u20133 Block IIA;\n**(3)**\n$1,400,000,000 shall be available for requirements of this Act relating to Terminal High Altitude Area Defense (THAAD) Systems;\n**(4)**\n$1,500,000,000 shall be available for requirements of this Act relating to PAC\u20132 and PAC\u20133 Munitions and MM\u2013104 Patriot batteries;\n**(5)**\n$1,000,000,000 shall be available for requirements of this Act relating to east coast and Alaska-based Aegis Ashore station construction;\n**(6)**\n$12,000,000,000 shall be available for expansion of missile interceptor fields available at Fort Greely, Alaska, to 80 units with the Next Generation Interceptor;\n**(7)**\n$250,000,000 shall be available for requirements of this Act relating to completion and certification of Hawaii Aegis Ashore system;\n**(8)**\n$60,000,000 shall be available for requirements of this Act relating to Space Development Agency satellite sensors;\n**(9)**\n$750,000,000 shall be available for requirements of this Act relating to modernization of terrestrial-based domain awareness radars;\n**(10)**\n$500,000,000 shall be available for requirements of this Act relating to research and development relating to directed energy or missile interception across the military departments;\n**(11)**\n$900,000,000 shall be available for requirements of this Act relating to research and development of space based missile defense;\n**(12)**\n$63,100,000 shall be available for requirements of this Act relating to Missile Defense Complex (MDC) and Fire Team Readiness Facility (FTRF);\n**(13)**\n$100,000,000 shall be available for requirements of this Act relating to procurement and fielding of dirigibles; and\n**(14)**\n$25,000,000 shall be available for Missile Defense Agency military construction to continue planning and design activities for an east coast missile defense interceptor site.",
      "versionDate": "2025-02-05",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-07-03T13:06:09Z"
          },
          {
            "name": "Alaska",
            "updateDate": "2025-07-03T13:05:51Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2025-07-03T13:05:46Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-03T13:05:38Z"
          },
          {
            "name": "Department of Defense",
            "updateDate": "2025-07-03T13:06:14Z"
          },
          {
            "name": "Hawaii",
            "updateDate": "2025-07-03T13:06:05Z"
          },
          {
            "name": "Military facilities and property",
            "updateDate": "2025-07-03T13:05:56Z"
          },
          {
            "name": "Military procurement, research, weapons development",
            "updateDate": "2025-07-03T13:05:34Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-07-03T13:05:43Z"
          },
          {
            "name": "Spacecraft and satellites",
            "updateDate": "2025-07-03T13:06:01Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-09T15:26:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-29T18:44:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119s435",
          "measure-number": "435",
          "measure-type": "s",
          "orig-publish-date": "2025-02-05",
          "originChamber": "SENATE",
          "update-date": "2025-07-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s435v00",
            "update-date": "2025-07-22"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Increasing Response Options and Deterrence of Missile Engagements Act of 2025 or the IRONDOME Act of 2025</strong></p><p>This bill requires the Department of Defense (DOD) and other entities to take specified actions to support U.S. missile defense capabilities, particularly with respect to the U.S. homeland.</p><p>DOD must submit to Congress a multi-year phased plan to transfer operations and\u00a0sustainment responsibility for missile defense from the Missile Defense Agency to the appropriate military departments to allow the Missile Defense Agency to focus on research, development, and prototyping and testing.</p><p>Additionally, among other elements, the bill requires</p><ul><li>the United States Northern Command and the Space Development Agency within DOD to use a specified acquisition process to conduct rapid testing and development of\u00a0certain drone and satellite systems;</li><li>each commander of a combatant command to include the missile defense interceptor and sensor requirements of the command in annual budget requests;</li><li>DOD to use all authorities available to accelerate the development, production, and modernization of various defense systems and technology, including certain space-based interceptors; and</li><li>the Department of the Army to procure and field airships in support of the missile defense of the U.S. homeland from drones and\u00a0ballistic, hypersonic, and cruise missiles.</li></ul><p>On January 27, 2025, President Trump signed an executive order titled\u00a0<em>The Iron Dome for America. </em>The order directs DOD to develop plans for a next-generation missile defense shield to protect the U.S. homeland from ballistic, hypersonic, and advanced cruise missiles, and other next-generation aerial attacks.\u00a0</p>"
        },
        "title": "IRONDOME Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s435.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Increasing Response Options and Deterrence of Missile Engagements Act of 2025 or the IRONDOME Act of 2025</strong></p><p>This bill requires the Department of Defense (DOD) and other entities to take specified actions to support U.S. missile defense capabilities, particularly with respect to the U.S. homeland.</p><p>DOD must submit to Congress a multi-year phased plan to transfer operations and\u00a0sustainment responsibility for missile defense from the Missile Defense Agency to the appropriate military departments to allow the Missile Defense Agency to focus on research, development, and prototyping and testing.</p><p>Additionally, among other elements, the bill requires</p><ul><li>the United States Northern Command and the Space Development Agency within DOD to use a specified acquisition process to conduct rapid testing and development of\u00a0certain drone and satellite systems;</li><li>each commander of a combatant command to include the missile defense interceptor and sensor requirements of the command in annual budget requests;</li><li>DOD to use all authorities available to accelerate the development, production, and modernization of various defense systems and technology, including certain space-based interceptors; and</li><li>the Department of the Army to procure and field airships in support of the missile defense of the U.S. homeland from drones and\u00a0ballistic, hypersonic, and cruise missiles.</li></ul><p>On January 27, 2025, President Trump signed an executive order titled\u00a0<em>The Iron Dome for America. </em>The order directs DOD to develop plans for a next-generation missile defense shield to protect the U.S. homeland from ballistic, hypersonic, and advanced cruise missiles, and other next-generation aerial attacks.\u00a0</p>",
      "updateDate": "2025-07-22",
      "versionCode": "id119s435"
    },
    "title": "IRONDOME Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Increasing Response Options and Deterrence of Missile Engagements Act of 2025 or the IRONDOME Act of 2025</strong></p><p>This bill requires the Department of Defense (DOD) and other entities to take specified actions to support U.S. missile defense capabilities, particularly with respect to the U.S. homeland.</p><p>DOD must submit to Congress a multi-year phased plan to transfer operations and\u00a0sustainment responsibility for missile defense from the Missile Defense Agency to the appropriate military departments to allow the Missile Defense Agency to focus on research, development, and prototyping and testing.</p><p>Additionally, among other elements, the bill requires</p><ul><li>the United States Northern Command and the Space Development Agency within DOD to use a specified acquisition process to conduct rapid testing and development of\u00a0certain drone and satellite systems;</li><li>each commander of a combatant command to include the missile defense interceptor and sensor requirements of the command in annual budget requests;</li><li>DOD to use all authorities available to accelerate the development, production, and modernization of various defense systems and technology, including certain space-based interceptors; and</li><li>the Department of the Army to procure and field airships in support of the missile defense of the U.S. homeland from drones and\u00a0ballistic, hypersonic, and cruise missiles.</li></ul><p>On January 27, 2025, President Trump signed an executive order titled\u00a0<em>The Iron Dome for America. </em>The order directs DOD to develop plans for a next-generation missile defense shield to protect the U.S. homeland from ballistic, hypersonic, and advanced cruise missiles, and other next-generation aerial attacks.\u00a0</p>",
      "updateDate": "2025-07-22",
      "versionCode": "id119s435"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s435is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the missile defense capabilities of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:27Z"
    },
    {
      "title": "IRONDOME Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "IRONDOME Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Increasing Response Options and Deterrence of Missile Engagements Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    }
  ]
}
```
