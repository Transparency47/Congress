# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3249?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3249
- Title: Strategic Subsea Cables Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3249
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-05-22T19:48:25Z
- Update date including text: 2026-05-22T19:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 327.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 327.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3249",
    "number": "3249",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Strategic Subsea Cables Act of 2026",
    "type": "S",
    "updateDate": "2026-05-22T19:48:25Z",
    "updateDateIncludingText": "2026-05-22T19:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 327.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
            "date": "2026-02-10T16:29:45Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-29T14:30:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-20T18:48:13Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "WY"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "ID"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "DE"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "PA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "VA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3249is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3249\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mrs. Shaheen (for herself and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo enhance United States Government strategic coordination of the security, installation, maintenance, and repair of international subsea fiber-optic cables.\n#### 1. Short title\nThis Act may be cited as the Strategic Subsea Cables Act of 2025 .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nSec. 3. Definitions.\nTITLE I\u2014International coordination and engagement on subsea fiber-optic cables\nSec. 101. Findings.\nSec. 102. Sense of Congress.\nSec. 103. Enhancing United States Government engagement at the International Cable Protection Committee to safeguard United States interests.\nSec. 104. Imposition of sanctions with respect to damage to subsea fiber-optic cables.\nSec. 105. Report on subsea fiber-optic cable activities by the People\u2019s Republic of China and the Russian Federation.\nSec. 106. Engaging foreign partners to strengthen subsea fiber-optic cable security.\nTITLE II\u2014Department of State subsea fiber-optic expertise\nSec. 201. Expanding subsea fiber-optic cable expertise at the Department of State.\nTITLE III\u2014Subsea fiber-optic cable coordination, construction, and repair\nSec. 301. Improving United States Government coordination of subsea fiber-optic cables.\nSec. 302. Strengthening information sharing between United States Government and private sector actors on subsea fiber-optic cables.\n#### 3. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given the term in section 3502 of title 44, United States Code.\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs and the Committee on Appropriations of the House of Representatives.\n**(3) Appropriate Federal agencies**\nThe term appropriate Federal agencies means the following:\n**(A)**\nThe Department of Commerce.\n**(B)**\nThe Department of Defense.\n**(C)**\nThe Department of Homeland Security.\n**(D)**\nThe Office of the Director of National Intelligence.\n**(E)**\nThe Department of State.\n**(F)**\nThe Federal Communications Commission.\n**(G)**\nThe Department of the Treasury.\n**(H)**\nThe Department of the Judiciary.\n**(I)**\nAny additional Federal agencies, as determined by the President.\n**(4) Interagency committee**\nThe term interagency committee means the entity established under section 301(b) of this Act.\n**(5) Non-Federal entity**\nThe term non-Federal entity means any nongovernmental entity that is an individual, organization, or business involved in the operation, maintenance, repair, or construction of subsea fiber-optic cables, including subsea cable owners.\n**(6) Subsea fiber-optic cable threat**\nThe term subsea fiber-optic cable threat means an action or likely future action, in particular, actions taken with malicious intent, on or through a subsea fiber-optic cable network that may result in an unauthorized effort to adversely impact the privacy, efficacy, security, or integrity of a subsea fiber-optic cable network.\nI\nInternational coordination and engagement on subsea fiber-optic cables\n#### 101. Findings\nCongress makes the following findings:\n**(1)**\nFollowing subsea fiber-optic cable cuts in the Baltic Sea in December 2024, the North Atlantic Treaty Organization (NATO) established the Critical Undersea Infrastructure Network to conduct information and threat intelligence sharing among private and public sector actors to protect subsea cables.\n**(2)**\nOn February 21, 2025, the European Union published an EU Action Plan on Cable Security to include the development and deployment of an Integrated Surveillance Mechanism for Submarine cables work to establish a dedicated regional hub in the Baltic Sea to serve as a test bed of the integrated surveillance approach.\n**(3)**\nThe Association of Southeast Asian States (ASEAN) published guidelines for Strengthening Resilience and Repair of Submarine Cables and most recently announced plans to build a secure, diverse and resilient submarine cable network and to facilitate the expeditious deployment, repair, maintenance, removal, and protection of submarine cables, between ASEAN Member States .\n**(4)**\nOn July 1, 2025, the Quad, represented by the United States, India, Japan, and Australia, met to reaffirm its commitment to the Quad Partnership on Cable Connectivity and Resilience. In the meeting, the Quad underscored the need for digital infrastructure collaboration, organizing a subsea cables forum to be hosted by the United States and India and encouraging regulatory harmonization between Quad partners. Through this initiative, the Quad seeks to defend and promote resilient, secure, and transparent digital infrastructure across the Indo-Pacific region.\n#### 102. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nsubsea fiber-optic cables constitute the backbone of the global internet and therefore should be treated as a global public good;\n**(2)**\nthe United States Government has an important role to play in advancing the United States interests in international bodies that oversee subsea fiber-optic cable protection, promote network resilience and redundancy, and advance regulations in support of these goals;\n**(3)**\nthe United States Government should play a more active role in the International Cable Protection Committee (ICPC) in order to advance the United States national security and economic interests;\n**(4)**\nthe United States should lead efforts to promote the deployment of resilient subsea fiber-optic cable networks, enhance situational awareness, strengthen preparedness, and formalize collective responses among allies and partners through enhanced information sharing and coordination; and\n**(5)**\nwhile the United States and allied foreign governments have a role to play in the protection of subsea fiber-optic cables, cable owners and other associated private sector stakeholders carry significant responsibility in safeguarding subsea cables.\n#### 103. Enhancing United States Government engagement at the International Cable Protection Committee to safeguard United States interests\n##### (a) In general\nThe Secretary of State, in coordination with the interagency committee, shall seek to increase United States Government engagement in the International Cable Protection Committee (ICPC) to advance United States national security and economic interests.\n##### (b) Report\nNot later than one year after the date of the enactment of this Act, and annually thereafter for 5 years, the Secretary of State shall submit a report to the appropriate congressional committees that includes the following:\n**(1)**\nA description of how increased the United States Government engagement within the ICPC could support United States national security objectives as it relates to the protection of subsea fiber-optic cables.\n**(2)**\nA description of key objectives for promoting and protecting United States national security interests within the ICPC.\n**(3)**\nA description of how People's Republic of China entities leverage their engagement within the ICPC to further their strategic interests.\n**(4)**\nA description of how encouraging other countries and regional bodies to join the ICPC can better ensure coordinated, consistent global subsea fiber-optic cable policies.\n#### 104. Imposition of sanctions with respect to damage to subsea fiber-optic cables\n##### (a) In general\nThe President, in coordination with the Secretary of State and the Secretary of the Treasury, shall impose sanctions described in subsection (c) with respect to any foreign person that the President determines, on or after the date of the enactment of this Act, is responsible for or complicit in damaging subsea fiber-optic cables in a manner that undermines the national security interests of the United States.\n##### (b) Report required\nNot later than 15 days after imposing sanctions with respect to a foreign person under subsection (a), the President shall submit to the appropriate congressional committees, the Committee on Banking, Housing, and Urban Affairs of the Senate, and the Committee on Financial Services of the House of Representatives, a report that includes a detailed justification for the imposition of the sanctions.\n##### (c) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Blocking of property**\nThe President shall exercise all of the powers granted by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in all property and interests in property of a foreign person described in subsection (a), if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Ineligibility for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nAn alien described in subsection (a) shall be\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe visa or other entry documentation of an alien described in subsection (a) shall be revoked, regardless of when such visa or other entry documentation is or was issued.\n**(ii) Immediate effect**\nA revocation under clause (i) shall\u2014\n**(I)**\ntake effect immediately; and\n**(II)**\nautomatically cancel any other valid visa or entry documentation that is in the possession of the alien.\n##### (d) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of this section or any regulation, license, or order issued to carry out this section shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n##### (e) Exceptions\n**(1) Exception to comply with united nations headquarters agreement and law enforcement activities**\nSanctions under this section shall not apply with respect to the admission or parole of an alien to the United States if admitting or paroling the alien is necessary\u2014\n**(A)**\nto permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations of the United States; or\n**(B)**\nto carry out or assist authorized law enforcement activity in the United States.\n**(2) Exception to comply with intelligence activities**\nSanctions under this section shall not apply to any activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ) or any authorized intelligence activities of the United States.\n**(3) Exception relating to importation of goods**\n**(A) In general**\nA requirement to block and prohibit all transactions in all property and interests in property under this section shall not include the authority or requirement to impose sanctions on the importation of goods.\n**(B) Good defined**\nIn this paragraph, the term good means any article, natural or manmade substance, material, supply or manufactured product, including inspection and test equipment, and excluding technical data.\n##### (f) Definitions\nIn this section:\n**(1) Admission; admitted; alien**\nThe terms admission , admitted , and alien have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(3) United states person**\nThe term United States person means\u2014\n**(A)**\nany United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including any foreign branch of such an entity; or\n**(C)**\nany person in the United States.\n#### 105. Report on subsea fiber-optic cable activities by the People\u2019s Republic of China and the Russian Federation\n##### (a) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 5 years, the Secretary of State, in coordination with the heads of other relevant Federal agencies, shall submit a report to the appropriate congressional committees that includes the following:\n**(1)**\nA description, with respect to the applicable reporting period, of People\u2019s Republic of China and Russian subsea fiber-optic cable manufacturing, installation, and maintenance capabilities.\n**(2)**\nA description of any ongoing People\u2019s Republic of China and Russian efforts to produce vessels capable of severing or damaging subsea fiber-optic cables at sea depths of 4,000 meters or greater.\n**(3)**\nA list of instances during the previous calendar year in which the United States, or allies and partners of the United States, documented anomalous behavior from vessels, either flagged, crewed, or operated by the People\u2019s Republic of China or Russia, around subsea fiber-optic cable networks, including\u2014\n**(A)**\nany official United States Government response to counter the anomalous behavior; and\n**(B)**\nany coordinated diplomatic action with allies and partners.\n##### (b) Classification\nThe report required under subsection (a) shall be submitted in unclassified form but may include a classified annex.\n#### 106. Engaging foreign partners to strengthen subsea fiber-optic cable security\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nas international subsea fiber-optic cable networks expand, there are increasing challenges to the proper maintenance, repair, and protection of international subsea fiber-optic cables that have the potential to undermine United States and foreign partner national security interests;\n**(2)**\nthe United States is uniquely positioned to provide technical, material, and other forms of support to international partners to enhance the resilience of international subsea fiber-optic cables; and\n**(3)**\nthe United States Government should enhance its diplomatic efforts to work with foreign governments to improve efforts to quickly and effectively maintain, repair, and protect international subsea fiber-optic cables.\n##### (b) Commitment of personnel and resources\nThe Secretary of State shall devote sufficient personnel and resources towards engaging with foreign countries to improve security and reduce barriers to the maintenance and repair of subsea fiber-optic cables.\n##### (c) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for the next 5 years, the Secretary of State shall submit to the appropriate congressional committees a report that outlines efforts by the United States Government in the prior calendar year to work with international allies and partners to strengthen the security of and reduce barriers to the maintenance, repair, and protection of international subsea fiber-optic cable networks, including\u2014\n**(1)**\na list of current foreign policies or laws that create barriers to United States-led efforts to maintain, repair, and protect international subsea fiber-optic cable networks; and\n**(2)**\nprogress made in the previous calendar year as a result of United States engagement with allies and partners.\nII\nDepartment of State subsea fiber-optic expertise\n#### 201. Expanding subsea fiber-optic cable expertise at the Department of State\n##### (a) In general\nThe Secretary of State shall assign not fewer than two full-time equivalent individuals, to be located in the Bureau for Cyberspace and Digital Policy, in order to support the Department of State\u2019s interagency engagement on matters related to subsea cables, including\u2014\n**(1)**\nprotection and resilience;\n**(2)**\ncoordination with United States allies and partners; and\n**(3)**\nUnited States engagement in international bodies that cover subsea cables.\n##### (b) Assignment\nThe Bureau for Cyberspace and Digital Policy may not dual-hat currently employed personnel in meeting the minimum hiring requirement outlined in subsection (a).\n##### (c) Notification\nNot later than 15 days after fulfilling the hiring requirement in subsection (a), the Secretary of State shall notify the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives.\n##### (d) International cooperation on subsea cables\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate congressional committees a report on how the United States Government plans to prioritize diplomatic engagement within relevant international bodies to spur increased information-sharing between allied and partner governments and relevant private sector companies on subsea fiber-optic cables.\nIII\nSubsea fiber-optic cable coordination, construction, and repair\n#### 301. Improving United States Government coordination of subsea fiber-optic cables\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nAccording to a December 2024 Department of Homeland Security white paper, There currently exists no forum in which the full scope of the [subsea] cable industry can effectively collaborate with the U.S. government to identify and address shared challenges. .\n**(2)**\nUnited States Federal Government responsibilities for the protection of subsea fiber-optic cables, damage reporting, information and intelligence sharing, and emergency response are overseen by various government actors through a multitude of mechanisms spanning several Federal departments and agencies.\n**(3)**\nIn order for the subsea fiber-optic cable industry to align with United States economic and security interests, the United States Government must provide the industry a clearer concept of operations, assessed risks to cable supply chain and infrastructure, and defined lines of effort in cases of emergency.\n##### (b) Establishment\nNot later than one year after the date of the enactment of this Act, the President shall establish an interagency committee (referred to in this Act as the interagency committee ) comprised of the heads of the appropriate Federal agencies, to lead United States Government efforts to\u2014\n**(1)**\nprotect and improve the resilience of subsea fiber-optic cable networks;\n**(2)**\nfacilitate subsea fiber-optic cable permitting; and\n**(3)**\naddress other matters related to subsea fiber-optic cables deemed appropriate and necessary by the President.\n##### (c) Coordination\nThe President shall direct the interagency committee to conduct an overview of the United States Federal Government\u2019s operational authorities for subsea fiber-optic cable security and resilience. The overview shall include\u2014\n**(1)**\nan interagency concept of operations for partnering with non-Federal entities, including subsea fiber-optic cable owners and operators, to secure and repair subsea fiber-optic cable systems in a variety of crisis scenarios; and\n**(2)**\nan interagency review and action plan to streamline subsea fiber-optic cable permitting processes in order to promote United States international leadership in cable connectivity and deployments and risk-based prioritization and standardization of additional security and resilience assessments.\n##### (d) Analysis of subsea fiber-Optic cable cuts and outages\n**(1) In general**\nThe President shall direct the heads of the relevant Federal agencies to develop strategies to coordinate closely within the interagency process and with subsea fiber-optic cable industry stakeholders to review subsea fiber-optic cable cuts and outages, including by leveraging analysis from industry-wide data, to\u2014\n**(A)**\nidentify trends;\n**(B)**\nrefine attributions, particularly in cases where subsea fiber-optic cables have been intentionally damaged by malicious actors;\n**(C)**\nidentify high-risk geographic areas for subsea fiber-optic cable construction; and\n**(D)**\ninform future risk mitigation efforts to reduce damage to subsea fiber-optic cable systems.\n**(2) Strategy elements**\nThe strategies required under paragraph (1) shall include\u2014\n**(A)**\nresourcing requirements;\n**(B)**\ncoordination with United States allies and partners; and\n**(C)**\nthe necessary technical expertise to make attributions for intentional subsea fiber-optic cable cuts by malicious actors.\n##### (e) Report\nNot later than 30 days after establishing the required interagency committee under subsection (b), the President shall submit to Congress a report that includes the following elements:\n**(1)**\nAny resources required to sufficiently staff the interagency committee and United States Federal agencies overseeing the objectives outlined in subsection (b).\n**(2)**\nA detailed plan for how the interagency committee will advance the objectives outlined in subsection (b).\n#### 302. Strengthening information sharing between United States Government and private sector actors on subsea fiber-optic cables\n##### (a) Public-Private sector information sharing\nConsistent with the necessary protections of classified information, the sourcing of relevant intelligence material, and privacy and civil liberties, all appropriate agencies shall, with the approval of the interagency committee, issue procedures to establish and promote\u2014\n**(1)**\nthe timely sharing of classified subsea fiber-optic cable threats and any indications of potential threats held by members of the interagency committee with non-Federal entities that possess the necessary security clearances;\n**(2)**\nthe timely sharing between the interagency committee and non-Federal entities of subsea fiber-optic cable threats, information relating to indications of potential threats, or authorized uses under this Act, in the possession of the interagency committee that may be declassified and shared at an unclassified level;\n**(3)**\nthe timely sharing between the interagency committee and non-Federal entities of unclassified, including controlled unclassified, subsea fiber-optic cable threats and indications of potential threats held by members of the interagency committee or non-Federal entities; and\n**(4)**\nthe timely sharing between the interagency committee and non-Federal entities, when and if appropriate, of information relating to indications of potential subsea fiber-optic cable threats or authorized uses under this title, held by the interagency committee or non-Federal entities about subsea fiber-optic cable threats, in order to prevent breaches to the security, integrity, or efficacy of the subsea fiber-optic cable network and to mitigate any other potential adverse effects from such subsea fiber-optic cable threats.\n##### (b) Development of procedures\nThe procedures developed under subsection (b) shall\u2014\n**(1)**\nensure the interagency committee has and maintains the capacity to identify and inform subsea fiber-optic cable threats and indications of potential subsea fiber-optic cable threats in real time to the appropriate Federal agencies or non-Federal entities consistent with the protection of classified information;\n**(2)**\nincorporate, whenever possible, existing processes, roles, and responsibilities of members of the interagency committee and non-Federal entities for information sharing, including subsea fiber-optic cable-specific information sharing and analysis entities; and\n**(3)**\nrequire members of the interagency committee and other appropriate Federal agencies which are sharing subsea fiber-optic cable threat indicators or defensive measures to employ any applicable security controls to defend against unauthorized access to or acquisition of such information.\n##### (c) Submittal to Congress\nNot later than 60 days after the date of the enactment of this Act, the Director of National Intelligence, in consultation with the members of the interagency committee, shall submit to Congress the procedures required under subsection (b).",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3249rs.xml",
      "text": "II\nCalendar No. 327\n119th CONGRESS\n2d Session\nS. 3249\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mrs. Shaheen (for herself and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nFebruary 10, 2026 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo enhance United States Government strategic coordination of the security, installation, maintenance, and repair of international subsea fiber-optic cables.\n#### 1. Short title\nThis Act may be cited as the Strategic Subsea Cables Act of 2025 .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nSec. 3. Definitions.\nTITLE I\u2014International coordination and engagement on subsea fiber-optic cables\nSec. 101. Findings.\nSec. 102. Sense of Congress.\nSec. 103. Enhancing United States Government engagement at the International Cable Protection Committee to safeguard United States interests.\nSec. 104. Imposition of sanctions with respect to damage to subsea fiber-optic cables.\nSec. 105. Report on subsea fiber-optic cable activities by the People\u2019s Republic of China and the Russian Federation.\nSec. 106. Engaging foreign partners to strengthen subsea fiber-optic cable security.\nTITLE II\u2014Department of State subsea fiber-optic expertise\nSec. 201. Expanding subsea fiber-optic cable expertise at the Department of State.\nTITLE III\u2014Subsea fiber-optic cable coordination, construction, and repair\nSec. 301. Improving United States Government coordination of subsea fiber-optic cables.\nSec. 302. Strengthening information sharing between United States Government and private sector actors on subsea fiber-optic cables.\n#### 3. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given the term in section 3502 of title 44, United States Code.\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs and the Committee on Appropriations of the House of Representatives.\n**(3) Appropriate Federal agencies**\nThe term appropriate Federal agencies means the following:\n**(A)**\nThe Department of Commerce.\n**(B)**\nThe Department of Defense.\n**(C)**\nThe Department of Homeland Security.\n**(D)**\nThe Office of the Director of National Intelligence.\n**(E)**\nThe Department of State.\n**(F)**\nThe Federal Communications Commission.\n**(G)**\nThe Department of the Treasury.\n**(H)**\nThe Department of the Judiciary.\n**(I)**\nAny additional Federal agencies, as determined by the President.\n**(4) Interagency committee**\nThe term interagency committee means the entity established under section 301(b) of this Act.\n**(5) Non-Federal entity**\nThe term non-Federal entity means any nongovernmental entity that is an individual, organization, or business involved in the operation, maintenance, repair, or construction of subsea fiber-optic cables, including subsea cable owners.\n**(6) Subsea fiber-optic cable threat**\nThe term subsea fiber-optic cable threat means an action or likely future action, in particular, actions taken with malicious intent, on or through a subsea fiber-optic cable network that may result in an unauthorized effort to adversely impact the privacy, efficacy, security, or integrity of a subsea fiber-optic cable network.\nI\nInternational coordination and engagement on subsea fiber-optic cables\n#### 101. Findings\nCongress makes the following findings:\n**(1)**\nFollowing subsea fiber-optic cable cuts in the Baltic Sea in December 2024, the North Atlantic Treaty Organization (NATO) established the Critical Undersea Infrastructure Network to conduct information and threat intelligence sharing among private and public sector actors to protect subsea cables.\n**(2)**\nOn February 21, 2025, the European Union published an EU Action Plan on Cable Security to include the development and deployment of an Integrated Surveillance Mechanism for Submarine cables work to establish a dedicated regional hub in the Baltic Sea to serve as a test bed of the integrated surveillance approach.\n**(3)**\nThe Association of Southeast Asian States (ASEAN) published guidelines for Strengthening Resilience and Repair of Submarine Cables and most recently announced plans to build a secure, diverse and resilient submarine cable network and to facilitate the expeditious deployment, repair, maintenance, removal, and protection of submarine cables, between ASEAN Member States .\n**(4)**\nOn July 1, 2025, the Quad, represented by the United States, India, Japan, and Australia, met to reaffirm its commitment to the Quad Partnership on Cable Connectivity and Resilience. In the meeting, the Quad underscored the need for digital infrastructure collaboration, organizing a subsea cables forum to be hosted by the United States and India and encouraging regulatory harmonization between Quad partners. Through this initiative, the Quad seeks to defend and promote resilient, secure, and transparent digital infrastructure across the Indo-Pacific region.\n#### 102. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nsubsea fiber-optic cables constitute the backbone of the global internet and therefore should be treated as a global public good;\n**(2)**\nthe United States Government has an important role to play in advancing the United States interests in international bodies that oversee subsea fiber-optic cable protection, promote network resilience and redundancy, and advance regulations in support of these goals;\n**(3)**\nthe United States Government should play a more active role in the International Cable Protection Committee (ICPC) in order to advance the United States national security and economic interests;\n**(4)**\nthe United States should lead efforts to promote the deployment of resilient subsea fiber-optic cable networks, enhance situational awareness, strengthen preparedness, and formalize collective responses among allies and partners through enhanced information sharing and coordination; and\n**(5)**\nwhile the United States and allied foreign governments have a role to play in the protection of subsea fiber-optic cables, cable owners and other associated private sector stakeholders carry significant responsibility in safeguarding subsea cables.\n#### 103. Enhancing United States Government engagement at the International Cable Protection Committee to safeguard United States interests\n##### (a) In general\nThe Secretary of State, in coordination with the interagency committee, shall seek to increase United States Government engagement in the International Cable Protection Committee (ICPC) to advance United States national security and economic interests.\n##### (b) Report\nNot later than one year after the date of the enactment of this Act, and annually thereafter for 5 years, the Secretary of State shall submit a report to the appropriate congressional committees that includes the following:\n**(1)**\nA description of how increased the United States Government engagement within the ICPC could support United States national security objectives as it relates to the protection of subsea fiber-optic cables.\n**(2)**\nA description of key objectives for promoting and protecting United States national security interests within the ICPC.\n**(3)**\nA description of how People's Republic of China entities leverage their engagement within the ICPC to further their strategic interests.\n**(4)**\nA description of how encouraging other countries and regional bodies to join the ICPC can better ensure coordinated, consistent global subsea fiber-optic cable policies.\n#### 104. Imposition of sanctions with respect to damage to subsea fiber-optic cables\n##### (a) In general\nThe President, in coordination with the Secretary of State and the Secretary of the Treasury, shall impose sanctions described in subsection (c) with respect to any foreign person that the President determines, on or after the date of the enactment of this Act, is responsible for or complicit in damaging subsea fiber-optic cables in a manner that undermines the national security interests of the United States.\n##### (b) Report required\nNot later than 15 days after imposing sanctions with respect to a foreign person under subsection (a), the President shall submit to the appropriate congressional committees, the Committee on Banking, Housing, and Urban Affairs of the Senate, and the Committee on Financial Services of the House of Representatives, a report that includes a detailed justification for the imposition of the sanctions.\n##### (c) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Blocking of property**\nThe President shall exercise all of the powers granted by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in all property and interests in property of a foreign person described in subsection (a), if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Ineligibility for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nAn alien described in subsection (a) shall be\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe visa or other entry documentation of an alien described in subsection (a) shall be revoked, regardless of when such visa or other entry documentation is or was issued.\n**(ii) Immediate effect**\nA revocation under clause (i) shall\u2014\n**(I)**\ntake effect immediately; and\n**(II)**\nautomatically cancel any other valid visa or entry documentation that is in the possession of the alien.\n##### (d) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of this section or any regulation, license, or order issued to carry out this section shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n##### (e) Exceptions\n**(1) Exception to comply with united nations headquarters agreement and law enforcement activities**\nSanctions under this section shall not apply with respect to the admission or parole of an alien to the United States if admitting or paroling the alien is necessary\u2014\n**(A)**\nto permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations of the United States; or\n**(B)**\nto carry out or assist authorized law enforcement activity in the United States.\n**(2) Exception to comply with intelligence activities**\nSanctions under this section shall not apply to any activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ) or any authorized intelligence activities of the United States.\n**(3) Exception relating to importation of goods**\n**(A) In general**\nA requirement to block and prohibit all transactions in all property and interests in property under this section shall not include the authority or requirement to impose sanctions on the importation of goods.\n**(B) Good defined**\nIn this paragraph, the term good means any article, natural or manmade substance, material, supply or manufactured product, including inspection and test equipment, and excluding technical data.\n##### (f) Definitions\nIn this section:\n**(1) Admission; admitted; alien**\nThe terms admission , admitted , and alien have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(3) United states person**\nThe term United States person means\u2014\n**(A)**\nany United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including any foreign branch of such an entity; or\n**(C)**\nany person in the United States.\n#### 105. Report on subsea fiber-optic cable activities by the People\u2019s Republic of China and the Russian Federation\n##### (a) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 5 years, the Secretary of State, in coordination with the heads of other relevant Federal agencies, shall submit a report to the appropriate congressional committees that includes the following:\n**(1)**\nA description, with respect to the applicable reporting period, of People\u2019s Republic of China and Russian subsea fiber-optic cable manufacturing, installation, and maintenance capabilities.\n**(2)**\nA description of any ongoing People\u2019s Republic of China and Russian efforts to produce vessels capable of severing or damaging subsea fiber-optic cables at sea depths of 4,000 meters or greater.\n**(3)**\nA list of instances during the previous calendar year in which the United States, or allies and partners of the United States, documented anomalous behavior from vessels, either flagged, crewed, or operated by the People\u2019s Republic of China or Russia, around subsea fiber-optic cable networks, including\u2014\n**(A)**\nany official United States Government response to counter the anomalous behavior; and\n**(B)**\nany coordinated diplomatic action with allies and partners.\n##### (b) Classification\nThe report required under subsection (a) shall be submitted in unclassified form but may include a classified annex.\n#### 106. Engaging foreign partners to strengthen subsea fiber-optic cable security\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nas international subsea fiber-optic cable networks expand, there are increasing challenges to the proper maintenance, repair, and protection of international subsea fiber-optic cables that have the potential to undermine United States and foreign partner national security interests;\n**(2)**\nthe United States is uniquely positioned to provide technical, material, and other forms of support to international partners to enhance the resilience of international subsea fiber-optic cables; and\n**(3)**\nthe United States Government should enhance its diplomatic efforts to work with foreign governments to improve efforts to quickly and effectively maintain, repair, and protect international subsea fiber-optic cables.\n##### (b) Commitment of personnel and resources\nThe Secretary of State shall devote sufficient personnel and resources towards engaging with foreign countries to improve security and reduce barriers to the maintenance and repair of subsea fiber-optic cables.\n##### (c) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for the next 5 years, the Secretary of State shall submit to the appropriate congressional committees a report that outlines efforts by the United States Government in the prior calendar year to work with international allies and partners to strengthen the security of and reduce barriers to the maintenance, repair, and protection of international subsea fiber-optic cable networks, including\u2014\n**(1)**\na list of current foreign policies or laws that create barriers to United States-led efforts to maintain, repair, and protect international subsea fiber-optic cable networks; and\n**(2)**\nprogress made in the previous calendar year as a result of United States engagement with allies and partners.\nII\nDepartment of State subsea fiber-optic expertise\n#### 201. Expanding subsea fiber-optic cable expertise at the Department of State\n##### (a) In general\nThe Secretary of State shall assign not fewer than two full-time equivalent individuals, to be located in the Bureau for Cyberspace and Digital Policy, in order to support the Department of State\u2019s interagency engagement on matters related to subsea cables, including\u2014\n**(1)**\nprotection and resilience;\n**(2)**\ncoordination with United States allies and partners; and\n**(3)**\nUnited States engagement in international bodies that cover subsea cables.\n##### (b) Assignment\nThe Bureau for Cyberspace and Digital Policy may not dual-hat currently employed personnel in meeting the minimum hiring requirement outlined in subsection (a).\n##### (c) Notification\nNot later than 15 days after fulfilling the hiring requirement in subsection (a), the Secretary of State shall notify the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives.\n##### (d) International cooperation on subsea cables\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate congressional committees a report on how the United States Government plans to prioritize diplomatic engagement within relevant international bodies to spur increased information-sharing between allied and partner governments and relevant private sector companies on subsea fiber-optic cables.\nIII\nSubsea fiber-optic cable coordination, construction, and repair\n#### 301. Improving United States Government coordination of subsea fiber-optic cables\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nAccording to a December 2024 Department of Homeland Security white paper, There currently exists no forum in which the full scope of the [subsea] cable industry can effectively collaborate with the U.S. government to identify and address shared challenges. .\n**(2)**\nUnited States Federal Government responsibilities for the protection of subsea fiber-optic cables, damage reporting, information and intelligence sharing, and emergency response are overseen by various government actors through a multitude of mechanisms spanning several Federal departments and agencies.\n**(3)**\nIn order for the subsea fiber-optic cable industry to align with United States economic and security interests, the United States Government must provide the industry a clearer concept of operations, assessed risks to cable supply chain and infrastructure, and defined lines of effort in cases of emergency.\n##### (b) Establishment\nNot later than one year after the date of the enactment of this Act, the President shall establish an interagency committee (referred to in this Act as the interagency committee ) comprised of the heads of the appropriate Federal agencies, to lead United States Government efforts to\u2014\n**(1)**\nprotect and improve the resilience of subsea fiber-optic cable networks;\n**(2)**\nfacilitate subsea fiber-optic cable permitting; and\n**(3)**\naddress other matters related to subsea fiber-optic cables deemed appropriate and necessary by the President.\n##### (c) Coordination\nThe President shall direct the interagency committee to conduct an overview of the United States Federal Government\u2019s operational authorities for subsea fiber-optic cable security and resilience. The overview shall include\u2014\n**(1)**\nan interagency concept of operations for partnering with non-Federal entities, including subsea fiber-optic cable owners and operators, to secure and repair subsea fiber-optic cable systems in a variety of crisis scenarios; and\n**(2)**\nan interagency review and action plan to streamline subsea fiber-optic cable permitting processes in order to promote United States international leadership in cable connectivity and deployments and risk-based prioritization and standardization of additional security and resilience assessments.\n##### (d) Analysis of subsea fiber-Optic cable cuts and outages\n**(1) In general**\nThe President shall direct the heads of the relevant Federal agencies to develop strategies to coordinate closely within the interagency process and with subsea fiber-optic cable industry stakeholders to review subsea fiber-optic cable cuts and outages, including by leveraging analysis from industry-wide data, to\u2014\n**(A)**\nidentify trends;\n**(B)**\nrefine attributions, particularly in cases where subsea fiber-optic cables have been intentionally damaged by malicious actors;\n**(C)**\nidentify high-risk geographic areas for subsea fiber-optic cable construction; and\n**(D)**\ninform future risk mitigation efforts to reduce damage to subsea fiber-optic cable systems.\n**(2) Strategy elements**\nThe strategies required under paragraph (1) shall include\u2014\n**(A)**\nresourcing requirements;\n**(B)**\ncoordination with United States allies and partners; and\n**(C)**\nthe necessary technical expertise to make attributions for intentional subsea fiber-optic cable cuts by malicious actors.\n##### (e) Report\nNot later than 30 days after establishing the required interagency committee under subsection (b), the President shall submit to Congress a report that includes the following elements:\n**(1)**\nAny resources required to sufficiently staff the interagency committee and United States Federal agencies overseeing the objectives outlined in subsection (b).\n**(2)**\nA detailed plan for how the interagency committee will advance the objectives outlined in subsection (b).\n#### 302. Strengthening information sharing between United States Government and private sector actors on subsea fiber-optic cables\n##### (a) Public-Private sector information sharing\nConsistent with the necessary protections of classified information, the sourcing of relevant intelligence material, and privacy and civil liberties, all appropriate agencies shall, with the approval of the interagency committee, issue procedures to establish and promote\u2014\n**(1)**\nthe timely sharing of classified subsea fiber-optic cable threats and any indications of potential threats held by members of the interagency committee with non-Federal entities that possess the necessary security clearances;\n**(2)**\nthe timely sharing between the interagency committee and non-Federal entities of subsea fiber-optic cable threats, information relating to indications of potential threats, or authorized uses under this Act, in the possession of the interagency committee that may be declassified and shared at an unclassified level;\n**(3)**\nthe timely sharing between the interagency committee and non-Federal entities of unclassified, including controlled unclassified, subsea fiber-optic cable threats and indications of potential threats held by members of the interagency committee or non-Federal entities; and\n**(4)**\nthe timely sharing between the interagency committee and non-Federal entities, when and if appropriate, of information relating to indications of potential subsea fiber-optic cable threats or authorized uses under this title, held by the interagency committee or non-Federal entities about subsea fiber-optic cable threats, in order to prevent breaches to the security, integrity, or efficacy of the subsea fiber-optic cable network and to mitigate any other potential adverse effects from such subsea fiber-optic cable threats.\n##### (b) Development of procedures\nThe procedures developed under subsection (b) shall\u2014\n**(1)**\nensure the interagency committee has and maintains the capacity to identify and inform subsea fiber-optic cable threats and indications of potential subsea fiber-optic cable threats in real time to the appropriate Federal agencies or non-Federal entities consistent with the protection of classified information;\n**(2)**\nincorporate, whenever possible, existing processes, roles, and responsibilities of members of the interagency committee and non-Federal entities for information sharing, including subsea fiber-optic cable-specific information sharing and analysis entities; and\n**(3)**\nrequire members of the interagency committee and other appropriate Federal agencies which are sharing subsea fiber-optic cable threat indicators or defensive measures to employ any applicable security controls to defend against unauthorized access to or acquisition of such information.\n##### (c) Submittal to Congress\nNot later than 60 days after the date of the enactment of this Act, the Director of National Intelligence, in consultation with the members of the interagency committee, shall submit to Congress the procedures required under subsection (b).",
      "versionDate": "2026-02-10",
      "versionType": "Reported in Senate"
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
        "actionDate": "2026-03-24",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committees on the Judiciary, Intelligence (Permanent Select), and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8069",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Strategic Subsea Cables Act of 2026",
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
            "name": "Asia",
            "updateDate": "2026-04-01T20:25:31Z"
          },
          {
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2026-04-01T20:23:28Z"
          },
          {
            "name": "China",
            "updateDate": "2026-04-01T20:25:19Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-04-01T20:25:12Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-01T20:25:44Z"
          },
          {
            "name": "Crimes against property",
            "updateDate": "2026-04-01T20:24:13Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-01T20:24:27Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2026-04-01T20:24:44Z"
          },
          {
            "name": "Europe",
            "updateDate": "2026-04-01T20:25:37Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2026-04-01T20:24:58Z"
          },
          {
            "name": "Infrastructure development",
            "updateDate": "2026-04-01T20:23:14Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2026-04-01T20:24:37Z"
          },
          {
            "name": "Marine and inland water transportation",
            "updateDate": "2026-04-01T20:24:51Z"
          },
          {
            "name": "Pipelines",
            "updateDate": "2026-04-01T20:24:20Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-04-01T20:23:58Z"
          },
          {
            "name": "Russia",
            "updateDate": "2026-04-01T20:25:25Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2026-04-01T20:23:51Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-04-01T20:23:44Z"
          },
          {
            "name": "Visas and passports",
            "updateDate": "2026-04-01T20:25:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-12-17T15:32:37Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3249is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3249rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Strategic Subsea Cables Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Strategic Subsea Cables Act of 2026",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-12T04:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strategic Subsea Cables Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to enhance United States Government strategic coordination of the security, installation, maintenance, and repair of international subsea fiber-optic cables.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T06:18:37Z"
    }
  ]
}
```
