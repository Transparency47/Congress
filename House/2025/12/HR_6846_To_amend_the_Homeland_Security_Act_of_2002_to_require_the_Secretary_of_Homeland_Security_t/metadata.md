# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6846?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6846
- Title: DEFEND Act
- Congress: 119
- Bill type: HR
- Bill number: 6846
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-05-16T08:07:40Z
- Update date including text: 2026-05-16T08:07:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-12-19 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2025-12-19 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-12-19 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2025-12-19 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6846",
    "number": "6846",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001132",
        "district": "2",
        "firstName": "Elijah",
        "fullName": "Rep. Crane, Elijah [R-AZ-2]",
        "lastName": "Crane",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "DEFEND Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:40Z",
    "updateDateIncludingText": "2026-05-16T08:07:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-19",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:08:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-12-19T21:07:43Z",
                "name": "Referred to"
              }
            },
            "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
            "systemCode": "hshm05"
          },
          {
            "activities": {
              "item": {
                "date": "2025-12-19T21:07:43Z",
                "name": "Referred to"
              }
            },
            "name": "Transportation and Maritime Security Subcommittee",
            "systemCode": "hshm07"
          }
        ]
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "TX"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "AL"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "TN"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6846ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6846\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Crane (for himself, Mr. Garbarino , Mr. McCaul , Mr. Strong , and Mr. Ogles ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to require the Secretary of Homeland Security to conduct annual assessments on terrorism threats to the United States relating to the malicious use of unmanned aircraft systems by covered foreign adversaries, including terrorist organizations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Detecting and Evaluating Foreign Exploitation of Novel Drones Act or the DEFEND Act .\n#### 2. Annual assessment on terrorism threats to the United States arising from the global proliferation and malicious use of unmanned aircraft systems\n##### (a) In general\nTitle III of the Homeland Security Act of 2002 ( 6 U.S.C. 231 et seq. ) is amended by adding at the end the following new section:\n324. Annual assessment on terrorism threats to the United States relating to the use of unmanned aircraft systems by covered foreign adversaries, including terrorist organizations (a) In general Not later than 270 days after the date of the enactment of this section and annually thereafter for six years, the Secretary shall submit to the appropriate congressional committees an assessment of terrorism threats to the United States relating to the global proliferation and malicious use of covered unmanned aircraft systems by covered foreign adversaries, including terrorist organizations, and the resulting implications such activities present for the homeland security of the United States, including implications for domestic preparedness for the malicious use of unmanned aircraft systems and the collective response to related terrorism threats. (b) Matters included Each assessment of terrorism threats under subsection (a) shall include the following: (1) An analysis of the methods, trends, tactics, and technologies, as of the date of such assessment, by which covered foreign adversaries, including terrorist organizations, seek to use covered unmanned aircraft systems to surveil, disrupt, damage, or destroy critical infrastructure of the United States or a foreign country, target civilian populations, conduct kinetic strikes or terrorism attacks, or otherwise undermine public safety or regional stability. (2) An evaluation of the risks that such methods, trends, tactics, and technologies may be replicated, adapted, or learned from by other covered foreign adversaries, including terrorist organizations, or by lone actors or domestic violent extremists, to carry out similar terrorist attacks within the homeland, including efforts to compromise border security or port security, exploit vulnerabilities in the homeland\u2019s transportation systems, soft targets, mass gathering events, or other high-risk venues, or to cause mass casualties or disruption through the use of covered unmanned aircraft systems. (3) An assessment of how covered unmanned aircraft systems are employed for intelligence, surveillance, or reconnaissance purposes by covered foreign adversaries, including terrorist organizations, including the collection, transmission, or exploitation of imagery or geospatial data, and how such data could be leveraged to facilitate espionage, cross-border operations, or attacks against critical infrastructure of the United States. (4) An analysis of how covered foreign adversaries, including terrorist organizations, acquire, manufacture, smuggle, or divert covered unmanned aircraft systems into conflict zones, including via ground convoys, commercial shipping containers, rail shipments, small vessels, fixed- or rotary-wing aircraft, over-the-road freight transport that may conceal or co-transport other illicit or seemingly innocuous goods, or any other illicit trafficking networks, and the applicability of such methods to potential entry into the homeland through seaports, airports, or land border crossings. (5) An analysis of emerging technologies integrated into covered unmanned aircraft systems that enhance their operational effectiveness, resilience, and lethality, when used by covered foreign adversaries, including terrorist organizations, including the use of artificial intelligence, autonomous navigation and targeting systems, advanced surveillance sensors, precision-guided payloads, encrypted communications links, physical tethering mechanisms (such as fiber optic cables that enable uninterrupted command and control in contested environments), cybersecurity-resilient architectures designed to prevent intrusion or remote exploitation, or any other adaptations intended to defeat or bypass electronic warfare countermeasures through resistance to jamming, spoofing, or signal degradation. (6) An evaluation of the use of low-cost, high-volume swarms of covered unmanned aircraft systems deployed by covered foreign adversaries, including terrorist organizations, in any region of active conflict as determined by the Secretary, in consultation with the heads of other relevant Federal departments or agencies the Secretary determines appropriate, and the extent to which similar swarm tactics could overwhelm law enforcement within the homeland or overwhelm homeland defense systems, including the potential to exhaust counter-UAS systems and associated resources or create mass panic. (7) An assessment of the use of covered unmanned aircraft systems by covered foreign adversaries, including terrorist organizations, in any region of active conflict as determined by the Secretary, in consultation with the heads of other relevant Federal departments or agencies the Secretary determines appropriate, to deliver chemical, biological, radiological, or nuclear payloads or simulants, including efforts to repurpose agricultural or industrial spraying unmanned aircraft systems for nonconventional attacks, and whether such scenarios are adequately modeled or prepared for in homeland security planning. (8) A review of how covered foreign adversaries, including terrorist organizations, in any region of active conflict as determined by the Secretary, in consultation with the heads of other relevant Federal departments or agencies the Secretary determines appropriate, have experimented with water-launched unmanned aircraft systems and unmanned aircraft systems deployed from shipping containers or disguised vehicles, and the implications such tactics may pose for port security, land border security, or the security of critical infrastructure of the United States or a foreign country in proximity to seaports within the homeland. (9) An assessment of lessons learned from ongoing and recent global conflicts regarding the utilization, defense, and defeat of covered unmanned aircraft systems, and from the experiences of allied and partner countries in countering unmanned aircraft system-enabled attacks conducted by covered foreign adversaries, including terrorist organizations, including an evaluation of the effectiveness of mobile counter-UAS system platforms, passive detection and tracking technologies, airspace management and deconfliction tools, and regulatory mechanisms (such as drone zoning laws), the applicability of such lessons to Federal, State, and local homeland security operations, and the manner in which the Department has incorporated, or plans to incorporate, such lessons into its homeland security planning, counter-UAS systems strategy, and interagency coordination activities. (10) An assessment of the adoption, adaptation, and potential operational use of unmanned aircraft systems by transnational criminal organizations, cartels, or other illicit groups in the Western Hemisphere that are supplied by or emulating covered foreign adversaries, including terrorist organizations, including cross-border weaponization trends, narcotics trafficking, and surveillance of law enforcement operations. (11) A review of the Department\u2019s research and development efforts to counter emerging threats posed by covered unmanned aircraft systems used by covered foreign adversaries, including terrorist organizations, and how such efforts contribute to domestic preparedness for and collective response to terrorism. (12) A description of how the Secretary has incorporated input, technology, and best practices from private sector entities, including such entities the counter-UAS systems or detection technologies of which are currently deployed in regions of active conflict as determined by the Secretary, in consultation with the heads of other relevant Federal departments or agencies the Secretary determines appropriate, involving covered foreign adversaries, including terrorist organizations, in order to strengthen domestic preparedness and accelerate adoption of effective counter-UAS system capabilities. (13) Any other matter relating to covered unmanned aircraft systems the Secretary determines appropriate. (c) Training and capacity building To enhance domestic preparedness against terrorism threats assessed in accordance with subsection (a), the Secretary, in consultation with the heads of relevant components and offices of the Department, as determined by the Secretary, shall develop recommendations, training modules, and exercises for Federal, State, local, Tribal, and territorial law enforcement to recognize, report, and respond to malicious use of unmanned aircraft systems by covered foreign adversaries, including terrorist organizations, incorporating lessons learned from current and recent global conflicts. (d) Consultation The Secretary shall develop each assessment of terrorism threats under subsection (a) in consultation with representatives of the following: (1) Components and offices of the Department. (2) The Department of Defense. (3) The Office of the Director of National Intelligence. (4) Any other representatives of Federal departments or agencies the Secretary determines appropriate. (e) Collaboration In carrying out subsection (a), the Secretary shall seek to collaborate with representatives of private sector entities, each of whom shall be, in the determination of the Secretary, a highly accomplished leader in the field of counter-UAS systems with demonstrated experience in developing, deploying, or advising on covered unmanned aircraft systems used in regions in which covered foreign adversaries, including terrorist organizations, operate, in order to leverage private-sector expertise and resources for research, analysis, and evaluation of emerging threats relating to unmanned aircraft systems. (f) Briefing required Not later than seven days after the submission of each assessment of terrorism threats under subsection (a), the Secretary shall provide to the appropriate congressional committees a classified briefing on the findings, conclusions, and recommendations contained in such assessment. (g) Form Each assessment of terrorism threats under subsection (a) shall be submitted in classified form. The Secretary shall also prepare an unclassified annex to each such assessment, which shall be made publicly available on the website of the Department. (h) Definitions In this section: (1) Appropriate congressional committees The term appropriate congressional committees means\u2014 (A) the Committee on Homeland Security of the House of Representatives; and (B) the Committee on Homeland Security and Governmental Affairs of the Senate. (2) Counter-UAS system The term counter-UAS system has the meaning given such term in section 44801 of title 49, United States Code. (3) Covered foreign adversary The term covered foreign adversary means\u2014 (A) any foreign government, military, intelligence service, or other authority of a covered foreign country acting independently; or (B) any organization, group, or person acting on behalf of, with the support, direction, control, or influence of, or trained or supplied by, such a foreign government, military, intelligence service, or other authority, including any proxy, militia, paramilitary organization, intelligence or security service, or other state-sponsored actor that receives material support, training, technical assistance, or operational coordination from a covered foreign country and engages in activities that threaten the national security of the United States or its allies. (4) Covered foreign country The term covered foreign country means a country that\u2014 (A) the intelligence community (as such term is defined in section 3(4) of the National Security Act of 1947 ( 50 U.S.C. 3003(4) )) has identified as a foreign adversary in its most recent Annual Threat Assessment; or (B) the Secretary, in coordination with the Director of National Intelligence, has identified as a foreign adversary that is not included in such Annual Threat Assessment. (5) Covered unmanned aircraft system The term covered unmanned aircraft system means any unmanned aircraft system that\u2014 (A) is manufactured in a covered foreign country or by an entity domiciled in a covered foreign country; (B) uses flight controllers, radios, data transmission devices, cameras, or gimbals manufactured in a covered foreign country or by an entity domiciled in a covered foreign country; (C) uses a ground control system or operating software developed in a covered foreign country or by an entity domiciled in a covered foreign country; or (D) uses network connectivity or data storage located in a covered foreign country or administered by an entity domiciled in a covered foreign country. (6) Homeland Security Enterprise The term Homeland Security Enterprise has the meaning given such term in section 2200. (7) Terrorist organization The term terrorist organization means\u2014 (A) any entity designated as a foreign terrorist organization pursuant to section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ); or (B) any entity engaged in terrorism, as such term is defined in section 2(18). (8) Unmanned aircraft system The term unmanned aircraft system has the meaning given such term in section 44801 of title 49, United States Code, except that the requirement relating to safe and efficient operation in the national airspace system shall not apply for purposes of this section. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Homeland Security Act of 2002 is amended by inserting after the item relating to section 323 the following new item:\nSec. 324. Annual assessment on terrorism threats to the United States relating to the use of unmanned aircraft systems by covered foreign adversaries, including terrorist organizations. .",
      "versionDate": "2025-12-18",
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
        "name": "Immigration",
        "updateDate": "2026-01-20T14:55:42Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6846ih.xml"
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
      "title": "DEFEND Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T06:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DEFEND Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T06:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Detecting and Evaluating Foreign Exploitation of Novel Drones Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T06:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to require the Secretary of Homeland Security to conduct annual assessments on terrorism threats to the United States relating to the malicious use of unmanned aircraft systems by covered foreign adversaries, including terrorist organizations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T06:18:51Z"
    }
  ]
}
```
