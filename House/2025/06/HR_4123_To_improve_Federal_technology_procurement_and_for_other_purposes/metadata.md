# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4123?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4123
- Title: FIT Procurement Act
- Congress: 119
- Bill type: HR
- Bill number: 4123
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2026-02-06T09:06:20Z
- Update date including text: 2026-02-06T09:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-25 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-04 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-04 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 42 - 0.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-25 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-04 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-04 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 42 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4123",
    "number": "4123",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001316",
        "district": "7",
        "firstName": "Eric",
        "fullName": "Rep. Burlison, Eric [R-MO-7]",
        "lastName": "Burlison",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "FIT Procurement Act",
    "type": "HR",
    "updateDate": "2026-02-06T09:06:20Z",
    "updateDateIncludingText": "2026-02-06T09:06:20Z"
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
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 42 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
        "item": [
          {
            "date": "2026-02-04T14:56:36Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-25T14:02:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-25T14:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "VA"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "FL"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4123ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4123\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Burlison (for himself, Mr. Subramanyam , Mrs. Luna , and Mr. Lynch ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Small Business , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo improve Federal technology procurement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Improvement in Technology Procurement Act or the FIT Procurement Act .\n#### 2. Definitions\nIn this Act:\n**(1) Acquisition workforce**\nThe term acquisition workforce means employees of an executive agency who are responsible for procurement, contracting, program or project management that involves the performance of acquisition-related functions, or others as designated by the Chief Acquisition Officer, senior procurement executive, or head of the contracting activity.\n**(2) Administrator**\nThe term Administrator means the Administrator for Federal Procurement Policy.\n**(3) Chief Acquisition Officer**\nThe term Chief Acquisition Officer means a Chief Acquisition Officer appointed pursuant to section 1702 of title 41, United States Code.\n**(4) Cross-functional**\nThe term cross-functional means a structure in which individuals with different functional expertise or from different areas of an organization work together as a team.\n**(5) Executive agency**\nThe term executive agency has the meaning given the term in section 133 of title 41, United States Code.\n**(6) Experiential learning**\nThe term experiential learning means on-the-job experiences or simulations that serve to enhance workforce professional skills.\n**(7) Information and communications technology**\nThe term information and communications technology \u2014\n**(A)**\nhas the meaning given the term in section 4713(k) of title 41, United States Code; and\n**(B)**\nincludes information and communications technologies covered by any definition contained in the Federal Acquisition Regulation, including a definition added after the date of the enactment of this Act by the Federal Acquisition Regulatory Council pursuant to notice and comment.\n**(8) Relevant committees of congress**\nThe term relevant committees of Congress means the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives.\n**(9) Senior procurement executive**\nThe term senior procurement executive means a senior procurement executive designated pursuant to section 1702(c) of title 41, United States Code.\n**(10) Small business**\nThe term small business has the meaning given the term small business concern in section 3 of the Small Business Act ( 15 U.S.C. 632 ).\n#### 3. Acquisition workforce\n##### (a) Experiential learning\nNot later than 18 months after the date of the enactment of this Act, the Federal Acquisition Institute shall establish a pilot program to consider the incorporation of experiential learning into the Federal Credentials Program, the Federal Acquisition Certification-Contracting Officer\u2019s Representative Program, and the Federal Acquisition Certification for Program and Project Managers Program, or any successor program.\n##### (b) Training on information and communications technology acquisition\n**(1) In general**\nNot later than 18 months after the date of the enactment of this Act, the Director of the Federal Acquisition Institute, in coordination with the Administrator, the Administrator of General Services, and the Administrator of the Office of Electronic Government, and in consultation with the heads of other executive agencies as determined to be appropriate by the Director of the Federal Acquisition Institute, shall develop and implement or otherwise provide a cross-functional information and communications technology acquisition training program for acquisition workforce members involved in acquiring information and communications technology. The training shall do the following:\n**(A)**\nInclude learning objectives related to market research, communicating with industry and industry perspectives on the procurement process, including how investment decisions are impacted by Government communication and engagement, developing requirements, acquisition planning, best practices for developing and executing outcome-based contracts, and source selection strategy, evaluating proposals, and awarding and administering contracts for information and communications technology.\n**(B)**\nInclude learning objectives that provide a basic understanding of key technologies executive agencies need, such as cloud computing, artificial intelligence and artificial intelligence-enabled applications, and cybersecurity solutions.\n**(C)**\nInclude learning objectives that encourage the use of commercial or commercially available off-the-shelf technologies to the greatest extent practicable.\n**(D)**\nInclude case studies of lessons learned from Federal information and communications technology procurements and contracts, and related matters as determined to be relevant by the Director of the Federal Acquisition Institute.\n**(E)**\nInclude experiential learning opportunities, and opportunities to practice acquisition teaming involving collaboration of team members with varied relevant domain expertise to complete acquisition-related tasks, including tasks with accelerated timelines.\n**(F)**\nInclude continuous learning recommendations and resources to keep the skills of acquisition workforce members current, including tools that help adopt or adapt the use of innovative acquisition practices or other flexible business practices commonly used in commercial buys.\n**(G)**\nBe made available to acquisition workforce members designated by a Chief Acquisition Officer, senior procurement executive, or head of the contracting activity to participate in the training program.\n**(H)**\nInform executive agencies about streamlined and alternative procurement methods for procurement of information and communications technology, including\u2014\n**(i)**\nsimplified procedures for certain commercial products and commercial services in accordance with subpart 13.5 of the Federal Acquisition Regulation, prize competitions under the America COMPETES Reauthorization Act of 2010 ( Public Law 111\u2013358 ), competitive programs that encourage businesses to engage in Federal research or research and development with the potential for commercialization, and joint venture partnerships;\n**(ii)**\ninnovative procurement techniques designed to streamline the procurement process and lower barriers to entry, such as use of oral presentations and product demonstrations instead of lengthy written proposals, appropriately leveraging performance and outcomes-based contracting, and other techniques discussed on the Periodic Table of Acquisition Innovations or other similar successor knowledge management portals; and\n**(iii)**\ninformation on appropriate use, examples and templates, and any other information determined relevant by the Administrator to assist contracting officers and other members of the acquisition workforce in using the procedures described in clauses (i) and (ii).\n**(I)**\nIncorporate learning objectives to identify and mitigate waste, fraud, and abuse and ensure the protection of established privacy, civil rights, and civil liberties in the procurement process.\n**(2) Report**\nNot later than 2 years after the date of the enactment of this Act, the Director of the Federal Acquisition Institute shall provide to the relevant committees of Congress, the Chief Acquisition Officers Council, and the Chief Information Officers Council\u2014\n**(A)**\na report on the progress of the Director in developing and implementing or otherwise providing the information and communications technology acquisition training described in paragraph (1); and\n**(B)**\na list of any acquisition training that the Director determines to be outdated or no longer necessary.\n**(3) Duration**\nThe training program shall be updated as appropriate, but at least every 2 years after implementation, and offered for a minimum of 6 years following the date of implementation of the training program.\n##### (c) Acquisition workforce training fund\nSection 1703(i)(3) of title 41, United States Code, is amended by striking Five percent and inserting Seven and a half percent .\n##### (d) Harmonization of acquisition workforce training requirements\nSection 2 of the Artificial Intelligence Training for the Acquisition Workforce Act ( Public Law 117\u2013207 ; 41 U.S.C. 1703 note) is amended\u2014\n**(1)**\nin subsection (a)(4), by striking Director. \u2014The term Director means the Director of the Office of Management and Budget. and inserting Administrator. \u2014The term Administrator means the Administrator of General Services. .\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking Director, in coordination with the Administrator of General Services and any other person determined relevant by the Director and inserting Administrator, in coordination with the Director of the Office of Management and Budget ;\n**(B)**\nin paragraph (4), by striking Director and inserting Administrator ;\n**(C)**\nin paragraph (5), by striking Director and inserting Administrator ; and\n**(D)**\nin paragraph (6), by striking Director and inserting Administrator .\n#### 4. Innovative procurement methods\n##### (a) Increase in simplified acquisition threshold\nSection 134 of title 41, United States Code, is amended by striking $250,000 and inserting $500,000 .\n##### (b) Increase in micro purchase threshold\nSection 1902(a)(1) of title 41, United States Code, is amended by striking $10,000 and inserting $25,000. .\n##### (c) Advances for commercial technology subscriptions and tenancy\nSection 3324(d) of title 31, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)(C), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby inserting or commercially available content after publication ; and\n**(B)**\nby striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new paragraph:\n(3) charges for information and communications technology subscriptions, reservations, or tenancy, which means the sharing of computing resources in a private or public environment, including cloud environments, for which the ordering agency defines appropriate access and security standards. .\n#### 5. Increasing competition in Federal contracting\n##### (a) Use of past performance\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Administrator shall issue guidance, including examples and templates where appropriate, on\u2014\n**(A)**\nwhen a wider range of projects, such as commercial or non-government, as well as Government projects, should be accepted as relevant past performance, in order to have increased competition among eligible firms with capability to perform a requirement, such as a requirement without much precedent;\n**(B)**\na means by which an agency may validate non-government past performance references, such as by requiring an official of an entity providing past performance references to attest to their authenticity and by providing verifiable contact information for the references; and\n**(C)**\nuse of alternative evaluation methods other than past performance that may be appropriate for a requirement without much precedent, such as demonstrations and testing of technologies as part of the proposal process.\n**(2) Supplement not supplant**\nThe guidance issued under paragraph (1) shall supplement existing Federal and agency policy and procedures for consideration of past performance and other evaluation factors and methods.\n##### (b) Enhancing competition in Federal procurement\n**(1) Council recommendations**\nNot later than 90 days after the date of the enactment of this Act, the Administrator shall convene the Chief Acquisition Officers Council (in this section referred to as the Council ), to make recommendations to identify and eliminate specific, unnecessary procedural barriers that disproportionately affect the ability of small businesses to compete for Federal contracts, with a focus on streamlining documentation and qualification requirements unrelated to the protection of privacy and civil liberties.\n**(2) Consultation**\nThe Council shall obtain input from the public, including from the APEX Accelerators program (formerly known as Procurement Technical Assistance Center network) and other contractor representatives, to identify Federal procurement policies and regulations that are obsolete, overly burdensome or restrictive, not adequately harmonized, or otherwise serve to create barriers to small business participation in Federal contracting or unnecessarily increase bid and proposal costs.\n**(3) Examination of actions**\nThe Council shall consider the input obtained under paragraph (2) and any other information determined to be relevant by the Council to identify legislative, regulatory, and other actions to increase competition and remove barriers to small business participation in the procurement process.\n**(4) Implementation**\nNot later than 2 years after the date of the enactment of this Act, the Administrator, in consultation with the Federal Acquisition Regulatory Council, the Chief Acquisition Officers Council, and other executive agencies as appropriate, shall implement the regulatory and other non-legislative actions identified under paragraph (3), as determined necessary by the Administrator, to remove barriers to entry for small businesses seeking to participate in Federal Government procurement.\n**(5) Briefing**\nNot later than 2 years after the date of the enactment of this Act, the Administrator shall brief the relevant committees of Congress on the legislative actions identified under paragraph (3), and the actions implemented under paragraph (4).\n##### (c) Consideration of cost-Efficiency and quality\nThe Administrator shall advocate for and prioritize contracting policies that ensure that cost-efficiency and quality of goods and services are key determining factors in awarding Federal contracts.\n#### 6. Comptroller general assessment of small business participation in Federal procurement\nNot later than 18 months after the date of the enactment of this Act, the Comptroller General of the United States shall submit to Congress and make publicly available a report that\u2014\n**(1)**\nassesses the current level of small business participation in Federal procurement, identifying barriers, opportunities, and the impact of existing policies on the ability of small businesses to compete in Federal procurement;\n**(2)**\ncatalogs and evaluates the effectiveness of programs intended to support small business participation in Federal procurement; and\n**(3)**\nanalyzes trends in small business involvement in Federal technology projects, including data on contract awards, the diversity of sectors represented, and the geographic distribution of small business contractors.\n#### 7. Conflict of interest procedures\nThe Federal Acquisition Regulatory Council and the Administrator shall update the Federal Acquisition Regulation as necessary to provide additional guidance to executive agencies to address personal and organizational conflicts of interest involving members of the acquisition workforce.\n#### 8. No additional funding\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act.",
      "versionDate": "2025-06-25",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-07-22T12:50:33Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4123ih.xml"
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
      "title": "FIT Procurement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T13:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FIT Procurement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T13:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Improvement in Technology Procurement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T13:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve Federal technology procurement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T13:48:24Z"
    }
  ]
}
```
