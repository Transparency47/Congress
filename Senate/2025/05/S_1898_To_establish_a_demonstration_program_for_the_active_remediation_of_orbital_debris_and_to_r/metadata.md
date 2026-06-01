# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1898?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1898
- Title: ORBITS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1898
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-02-13T12:03:21Z
- Update date including text: 2026-02-13T12:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1898",
    "number": "1898",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "ORBITS Act of 2025",
    "type": "S",
    "updateDate": "2026-02-13T12:03:21Z",
    "updateDateIncludingText": "2026-02-13T12:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
            "date": "2026-02-12T15:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-22T18:56:06Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "WA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "MS"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1898is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1898\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Hickenlooper (for himself, Ms. Cantwell , Mr. Wicker , and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish a demonstration program for the active remediation of orbital debris and to require the development of uniform orbital debris standard practices in order to support a safe and sustainable orbital environment, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Orbital Sustainability Act of 2025 or the ORBITS Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nThe safety and sustainability of operations in low-Earth orbit and nearby orbits in outer space have become increasingly endangered by a growing amount of orbital debris.\n**(2)**\nExploration and scientific research missions and commercial space services of critical importance to the United States rely on continued and secure access to outer space.\n**(3)**\nEfforts by nongovernmental space entities to apply lessons learned through standards and best practices will benefit from government support for implementation both domestically and internationally.\n##### (b) Sense of Congress\nIt is the sense of Congress that to preserve the sustainability of operations in space, the United States Government should\u2014\n**(1)**\nto the extent practicable, develop and carry out programs, establish or update regulations, and commence initiatives to minimize orbital debris, including initiatives to demonstrate active debris remediation of orbital debris generated by the United States Government or other entities under the jurisdiction of the United States;\n**(2)**\nlead international efforts to encourage other spacefaring countries to mitigate and remediate orbital debris under their jurisdiction and control; and\n**(3)**\nencourage space system operators to continue implementing best practices for space safety when deploying satellites and constellations of satellites, such as transparent data sharing and designing for system reliability, so as to limit the generation of future orbital debris.\n#### 3. Definitions\nIn this Act:\n**(1) Active debris remediation**\nThe term active debris remediation \u2014\n**(A)**\nmeans the deliberate process of facilitating the de-orbit, repurposing, or other disposal of orbital debris, which may include moving orbital debris to a safe position, using an object or technique that is external or internal to the orbital debris; and\n**(B)**\ndoes not include de-orbit, repurposing, or other disposal of orbital debris by passive means.\n**(2) Administrator**\nThe term Administrator means the Administrator of the National Aeronautics and Space Administration.\n**(3) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Appropriations, the Committee on Commerce, Science, and Transportation, the Committee on Foreign Relations, and the Committee on Armed Services of the Senate; and\n**(B)**\nthe Committee on Appropriations, the Committee on Science, Space, and Technology, the Committee on Foreign Affairs, and the Committee on Armed Services of the House of Representatives.\n**(4) Demonstration project**\nThe term demonstration project means the active orbital debris remediation demonstration project carried out under section 4(b).\n**(5) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na United States-based\u2014\n**(i)**\nnon-Federal, commercial entity;\n**(ii)**\ninstitution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )); or\n**(iii)**\nnonprofit organization;\n**(B)**\nany other United States-based entity the Administrator considers appropriate; and\n**(C)**\na partnership of entities described in subparagraphs (A) and (B).\n**(6) Orbital debris**\nThe term orbital debris means any human-made space object orbiting Earth that\u2014\n**(A)**\nno longer serves an intended purpose; and\n**(B)**\n**(i)**\nhas reached the end of its mission; or\n**(ii)**\nis incapable of safe maneuver or operation.\n**(7) Project**\nThe term project means a specific investment with defined requirements, a life-cycle cost, a period of duration with a beginning and an end, and a management structure that may interface with other projects, agencies, and international partners to yield new or revised technologies addressing strategic goals.\n**(8) Secretary**\nThe term Secretary means the Secretary of Commerce.\n**(9) Space traffic coordination**\nThe term space traffic coordination means the planning, coordination, and on-orbit synchronization of activities to enhance the safety and sustainability of operations in the space environment.\n#### 4. Active debris remediation\n##### (a) Prioritization of orbital debris\n**(1) List**\nNot later than 90 days after the date of the enactment of this Act, the Secretary, in consultation with the Administrator, the Secretary of Defense, the Secretary of State, the National Space Council, and representatives of the commercial space industry, academia, and nonprofit organizations, shall publish a list of select identified orbital debris that may be remediated to improve the safety and sustainability of orbiting satellites and on-orbit activities.\n**(2) Contents**\nThe list required under paragraph (1)\u2014\n**(A)**\nshall be developed using appropriate sources of data and information derived from governmental and nongovernmental sources, including space situational awareness data obtained by the Office of Space Commerce, to the extent practicable;\n**(B)**\nshall include, to the extent practicable\u2014\n**(i)**\na description of the approximate age, location in orbit, size, mass, tumbling state, post-mission passivation actions taken, and national jurisdiction of each orbital debris identified; and\n**(ii)**\ndata required to inform decisions regarding potential risk and feasibility of safe remediation;\n**(C)**\nmay include orbital debris that poses a significant risk to terrestrial people and assets, including risk resulting from potential environmental impacts from the uncontrolled reentry of the orbital debris identified; and\n**(D)**\nmay include collections of small debris that, as of the date of the enactment of this Act, are untracked.\n**(3) Public availability; periodic updates**\n**(A) In general**\nSubject to subparagraph (B), the list required under paragraph (1) shall be published in unclassified form on a publicly accessible internet website of the Department of Commerce.\n**(B) Exclusion**\nThe Secretary may not include on the list published under subparagraph (A) data acquired from nonpublic sources.\n**(C) Periodic updates**\nSuch list shall be updated periodically.\n**(4) Acquisition, access, use, and handling of data or information**\nIn carrying out the activities under this subsection, the Secretary\u2014\n**(A)**\nshall acquire, access, use, and handle data or information in a manner consistent with applicable provisions of law and policy, including laws and policies providing for the protection of privacy and civil liberties, and subject to any restrictions required by the source of the information;\n**(B)**\nshall have access, upon written request, to all information, data, or reports of any executive agency that the Secretary determines necessary to carry out the activities under this subsection, provided that such access is\u2014\n**(i)**\nconducted in a manner consistent with applicable provisions of law and policy of the originating agency, including laws and policies providing for the protection of privacy and civil liberties; and\n**(ii)**\nconsistent with due regard for the protection from unauthorized disclosure of classified information relating to sensitive intelligence sources and methods or other exceptionally sensitive matters; and\n**(C)**\nmay obtain commercially available information that may not be publicly available.\n##### (b) Active orbital debris remediation demonstration project\n**(1) Establishment**\nNot later than 180 days after the date of the enactment of this Act, subject to the availability of appropriations, the Administrator, in consultation with the head of each relevant Federal department or agency, shall establish a demonstration project to make competitive awards for the research, development, and demonstration of technologies leading to the remediation of selected orbital debris identified under subsection (a)(1).\n**(2) Purpose**\nThe purpose of the demonstration project shall be to enable eligible entities to pursue the phased development and demonstration of technologies and processes required for active debris remediation.\n**(3) Procedures and criteria**\nIn establishing the demonstration project, the Administrator shall\u2014\n**(A)**\nestablish\u2014\n**(i)**\neligibility criteria for participation;\n**(ii)**\na process for soliciting proposals from eligible entities;\n**(iii)**\ncriteria for the contents of such proposals;\n**(iv)**\nproject compliance and evaluation metrics; and\n**(v)**\nproject phases and milestones;\n**(B)**\nidentify government-furnished data or equipment;\n**(C)**\ndevelop a plan for National Aeronautics and Space Administration participation, as appropriate, in technology development and intellectual property rights that\u2014\n**(i)**\nleverages National Aeronautics and Space Administration Centers that have demonstrated expertise and historical knowledge in measuring, modeling, characterizing, and describing the current and future orbital debris environment; and\n**(ii)**\ndevelops the technical consensus for adopting mitigation measures for such participation; and\n**(D)**\n**(i)**\nassign a project manager to oversee the demonstration project and carry out project activities under this subsection; and\n**(ii)**\nin assigning such project manager, leverage National Aeronautics and Space Administration Centers and the personnel of National Aeronautics and Space Administration Centers, as practicable.\n**(4) Research and development phase**\nWith respect to orbital debris identified under paragraph (1) of subsection (a), the Administrator shall, to the extent practicable and subject to the availability of appropriations, carry out the additional research and development activities necessary to mature technologies, in partnership with eligible entities, with the intent to close commercial capability gaps and enable potential future remediation missions for such orbital debris, with a preference for technologies that are capable of remediating orbital debris that have a broad range of characteristics described in paragraph (2)(B)(i) of that subsection.\n**(5) Demonstration mission phase**\n**(A) In general**\nThe Administrator shall evaluate proposals for a demonstration mission, and select and enter into a partnership with an eligible entity, subject to the availability of appropriations, with the intent to demonstrate technologies determined by the Administrator to meet a level of technology readiness sufficient to carry out on-orbit remediation of select orbital debris.\n**(B) Evaluation**\nIn evaluating proposals for the demonstration project, the Administrator shall\u2014\n**(i)**\nconsider the safety, feasibility, cost, benefit, and maturity of the proposed technology;\n**(ii)**\nconsider the potential for the proposed demonstration to successfully remediate orbital debris and to advance the commercial state of the art with respect to active debris remediation;\n**(iii)**\ncarry out a risk analysis of the proposed technology that takes into consideration the potential casualty risk to humans in space or on the Earth\u2019s surface;\n**(iv)**\nin an appropriate setting, conduct thorough testing and evaluation of the proposed technology and each component of such technology or system of technologies; and\n**(v)**\nconsider the technical and financial feasibility of using the proposed technology to conduct multiple remediation missions.\n**(C) Consultation**\nThe Administrator shall consult with the head of each relevant Federal department or agency before carrying out any demonstration mission under this paragraph.\n**(D) Active debris remediation demonstration mission**\nIt is the sense of Congress that the Administrator should consider maximizing competition for, and use best practices to engage commercial entities in, an active debris remediation demonstration mission.\n**(6) Briefing and reports**\n**(A) Initial briefing**\nNot later than 30 days after the establishment of the demonstration project under paragraph (1), the Administrator shall provide to the appropriate committees of Congress a briefing on the details of the demonstration project.\n**(B) Annual report**\nNot later than 1 year after the initial briefing under subparagraph (A), and annually thereafter until the conclusion of the 1 or more demonstration missions, the Administrator shall submit to the appropriate committees of Congress a status report on\u2014\n**(i)**\nthe technology developed under the demonstration project;\n**(ii)**\nprogress toward the accomplishment of the 1 or more demonstration missions; and\n**(iii)**\nany duplicative efforts carried out or supported by the National Aeronautics and Space Administration or the Department of Defense.\n**(C) Recommendations**\nNot later than 1 year after the date on which the first demonstration mission is carried out under this subsection, the Administrator, in consultation with the head of each relevant Federal department or agency, shall submit to Congress a report that provides legislative, regulatory, and policy recommendations to improve active debris remediation missions, as applicable.\n**(D) Technical analysis**\n**(i) In general**\nTo inform decisions regarding the acquisition of active debris remediation services by the Federal Government, not later than 1 year after the date on which an award is made under paragraph (1), the Administrator shall submit to Congress a report that\u2014\n**(I)**\nsummarizes the cost-effectiveness, and provides a technical analysis of, technologies developed under the demonstration project;\n**(II)**\nidentifies any technology gaps addressed by the demonstration project and any remaining technology gaps; and\n**(III)**\nprovides, as applicable, any further legislative, regulatory, and policy recommendations to enable active debris remediation missions.\n**(ii) Availability**\nThe Administration shall make the report submitted under clause (i) available to the Secretary, the Secretary of Defense, and other relevant Federal departments and agencies, as determined by the Administrator.\n**(7) Sense of Congress on international cooperation**\nIt is the sense of Congress that, in carrying out the demonstration project, it is critical that the Administrator, in coordination with the Secretary of State and in consultation with the National Space Council, cooperate with one or more partner countries to enable the remediation of orbital debris that is under their respective jurisdictions.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to the Administrator to carry out this section $150,000,000 for the period of fiscal years 2026 through 2030.\n##### (d) Rescission of unobligated funds\nUnobligated balances of amounts appropriated or otherwise made available by subsection (c) as of September 30, 2030, shall be rescinded not later than December 31, 2030.\n##### (e) Rule of construction\nNothing in this section may be construed to grant the Administrator the authority to issue any regulation relating to activities under subsection (b) or related space activities under title 51, United States Code.\n#### 5. Active debris remediation services\n##### (a) In general\nTo foster the competitive development, operation, improvement, and commercial availability of active debris remediation services, and in consideration of the economic analysis required by subsection (b) and the briefing and reports under section 4(b)(6), the Administrator and the head of each relevant Federal department or agency may acquire services for the remediation of orbital debris, whenever practicable, through fair and open competition for contracts that are well-defined, milestone-based, and in accordance with the Federal Acquisition Regulation.\n##### (b) Economic analysis\nBased on the results of the demonstration project, the Secretary, acting through the Office of Space Commerce, shall publish an assessment of the estimated Federal Government and private sector demand for orbital debris remediation services for the 10-year period beginning in 2026.\n#### 6. Uniform orbital debris standard practices for United States space activities\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the National Space Council, in coordination with the Secretary, the Administrator of the Federal Aviation Administration, the Secretary of Defense, the Secretary of State, the Federal Communications Commission, and the Administrator, shall initiate an update to the Orbital Debris Mitigation Standard Practices that\u2014\n**(1)**\nconsiders planned space systems, including satellite constellations; and\n**(2)**\naddresses\u2014\n**(A)**\ncollision risk;\n**(B)**\nexplosion risk;\n**(C)**\ncasualty probability;\n**(D)**\npost-mission disposal of space systems;\n**(E)**\ntime to disposal or de-orbit;\n**(F)**\nspacecraft collision avoidance and automated identification capability; and\n**(G)**\nthe ability to track orbital debris of decreasing size.\n##### (b) Consultation\nIn developing the update under subsection (a), the National Space Council, or a designee of the National Space Council, shall seek advice and input on commercial standards and best practices from representatives of the commercial space industry, academia, and nonprofit organizations, including through workshops and, as appropriate, advance public notice and comment processes under chapter 5 of title 5, United States Code.\n##### (c) Publication\nNot later than 1 year after the date of the enactment of this Act, such update shall be published in the Federal Register and posted to the relevant Federal Government internet websites.\n##### (d) Regulations\nTo promote uniformity and avoid duplication in the regulation of space activity, including licensing by the Federal Aviation Administration, the National Oceanic and Atmospheric Administration, and the Federal Communications Commission, such update, after publication, shall be used to inform the further development and promulgation of Federal regulations relating to orbital debris.\n##### (e) International promotion\nTo encourage effective and nondiscriminatory standards, best practices, rules, and regulations implemented by other countries, such update shall inform bilateral and multilateral discussions focused on the authorization and continuing supervision of nongovernmental space activities.\n##### (f) Periodic review\nNot less frequently than every 5 years, the Orbital Debris Mitigation Standard Practices referred to in subsection (a) shall be assessed and, if necessary, updated, used, and promulgated in a manner consistent with this section.\n#### 7. Standard practices for space traffic coordination\n##### (a) In general\nThe Secretary, in coordination with the Secretary of Defense and members of the National Space Council and the Federal Communications Commission, shall facilitate the development of standard practices for on-orbit space traffic coordination based on existing guidelines and best practices used by Government and commercial space industry operators.\n##### (b) Consultation\nIn facilitating the development of standard practices under subsection (a), the Secretary, through the Office of Space Commerce, in consultation with the National Institute of Standards and Technology, shall engage in frequent and routine consultation with representatives of the commercial space industry, academia, and nonprofit organizations.\n##### (c) Promotion of standard practices\nOn completion of such standard practices, the Secretary, the Secretary of State, the Secretary of Transportation, the Administrator, and the Secretary of Defense shall promote the adoption and use of the standard practices for domestic and international space missions.",
      "versionDate": "2025-05-22",
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
        "updateDate": "2025-06-16T17:17:20Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1898is.xml"
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
      "title": "ORBITS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ORBITS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Orbital Sustainability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a demonstration program for the active remediation of orbital debris and to require the development of uniform orbital debris standard practices in order to support a safe and sustainable orbital environment, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T07:48:30Z"
    }
  ]
}
```
