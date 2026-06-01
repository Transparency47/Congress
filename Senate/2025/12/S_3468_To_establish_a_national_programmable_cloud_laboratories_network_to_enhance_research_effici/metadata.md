# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3468?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3468
- Title: National Programmable Cloud Laboratories Network Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3468
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-04-07T17:35:41Z
- Update date including text: 2026-04-07T17:35:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3468",
    "number": "3468",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "National Programmable Cloud Laboratories Network Act of 2025",
    "type": "S",
    "updateDate": "2026-04-07T17:35:41Z",
    "updateDateIncludingText": "2026-04-07T17:35:41Z"
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
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
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
            "date": "2025-12-11T20:59:27Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3468is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3468\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Fetterman (for himself and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish a national programmable cloud laboratories network to enhance research efficiency, innovation, and collaboration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Programmable Cloud Laboratories Network Act of 2025 .\n#### 2. Definitions\n##### (a) Definitions\nIn this Act:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given such term in section 5002 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 9401 ).\n**(2) Director**\nUnless otherwise provided, the term Director means the Director of the National Science Foundation.\n**(3) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(4) Network**\nThe term Network means the National Programmable Cloud Laboratories Network.\n**(5) Node**\nThe term node means a programmable cloud laboratory designated as part of the Network.\n**(6) Non-designated laboratory**\nThe term non-designated laboratory means any Federal, academic, nonprofit, or private industry programmable cloud laboratory not selected as a node under section 3.\n**(7) Programmable cloud laboratory**\nThe term programmable cloud laboratory means a physical laboratory that is equipped with research instrumentation and advanced manufacturing capabilities, including robotics and artificial intelligence, that can be securely and remotely programmed and controlled in order to conduct experiments and collect associated data.\n#### 3. National Programmable Cloud Laboratories Network\n##### (a) Purposes\nThe purposes of the Network established under this Act are\u2014\n**(1)**\nto maintain leadership by the United States in advanced experimentation, laboratory automation, and artificial intelligence for scientific research, advanced manufacturing, long-term economic competitiveness, and national security;\n**(2)**\nto reduce the cost of federally funded research through automation and reproducibility;\n**(3)**\nto accelerate national competitiveness by transferring government-funded research to private-sector commercial applications;\n**(4)**\nto improve collaboration among federally funded national laboratories, institutions of higher education, and private industry;\n**(5)**\nto ensure that investment in programmable cloud laboratories results in measurable cost savings, efficiencies, and long-term fiscal sustainability;\n**(6)**\nto incentivize private-sector cost-sharing in research infrastructure and equipment;\n**(7)**\nto support workforce development aligned with the technical needs of industry in the United States;\n**(8)**\nto advance the development of a domestic industrial base for scientific automation tools, artificial intelligence systems for experimentation, and robotics platforms for use in laboratory settings; and\n**(9)**\nto further programmable cloud laboratory research in areas such as materials science, biotechnology, chemistry, and other scientific or engineering disciplines where automation and cloud-enabled experimentation can deliver transformative results, including advanced materials synthesis and characterization, scalable biotechnology experimentation, and high-throughput chemical catalyst development.\n##### (b) Establishment\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Director, in consultation with the Director of the National Institute of Standards and Technology, shall designate and oversee a National Programmable Cloud Laboratories Network of not more than 6 nodes to support secure, standards-based, and cost-effective remote experimentation and automated research.\n**(2) Assessment sequencing**\nThe assessment required under section 5 shall be conducted only after the final designation of nodes under paragraph (1).\n**(3) Nodes**\nThe Network shall consist of nodes that\u2014\n**(A)**\nenable programmable workflows and automated science;\n**(B)**\nprovide access to advanced scientific and manufacturing instruments, including artificial intelligence-enabled tools;\n**(C)**\ncollaborate to establish and adopt common standards, protocols, and best practices; and\n**(D)**\nsupport interoperability across and between nodes.\n##### (c) Application and selection\n**(1) In general**\nThe Director shall issue a public solicitation for eligible entities to apply for node designation.\n**(2) Eligible entities**\nEligible entities that may apply for designation as a node include\u2014\n**(A)**\ninstitutions of higher education;\n**(B)**\nnonprofit research organizations;\n**(C)**\nprivate-sector research entities; and\n**(D)**\nconsortia or collaborations of the entities described in subparagraphs (A) through (C).\n##### (d) Applications for designation\nAn eligible entity that desires to apply for designation as a node in the Network shall submit an application to the Director at such time and in such manner as the Director may require. The application shall include\u2014\n**(1)**\na technical and programmatic plan for laboratory operations, automation capabilities, and data integration;\n**(2)**\na plan to achieve long-term self-sustainability, including metrics, interim milestones, and a timeline for reducing reliance on Federal funding; and\n**(3)**\nevidence of non-Federal cost share, private capital, or other third-party contributions demonstrating self-sustainability potential.\n##### (e) Evaluation of applicants\nThe Director shall ensure that the process for selecting eligible entities for designation in the Network shall be competitive, merit-reviewed, and transparent, evaluating\u2014\n**(1)**\npre-existing laboratory infrastructure and suitability for automated science;\n**(2)**\ncapacity to support distributed, cloud-enabled programmable workflows for multiple users;\n**(3)**\nlikelihood of achieving long-term sustainability without continued Federal funding;\n**(4)**\ndemonstrated ability to collaborate with other nodes, academic partners, industry partners, or other Federal research agencies (as defined in section 10002 of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 18901 ));\n**(5)**\nprotocols for research security, cybersecurity, and responsible access; and\n**(6)**\ndemonstration of user interest and research needs.\n##### (f) Designation\nIn designating nodes, the Director shall provide preference for applications demonstrating meaningful third-party cost share and pre-existing infrastructure.\n##### (g) Responsibilities\nEach node selected by the Director shall\u2014\n**(1)**\nsupport the purposes described in subsection (a)(9);\n**(2)**\nfacilitate collaboration among Network members to expand and integrate automated science capabilities and best practices;\n**(3)**\nactively participate with the Director of National Institute of Standards and Technology in developing network-wide interoperability, data-sharing, cybersecurity, and artificial intelligence-assisted experimentation standards;\n**(4)**\nsupport secure sharing of experimental data, models, and results across institutions of higher education participating in the Network, if applicable;\n**(5)**\nprovide a secure digital infrastructure to enable remote experimentation, artificial intelligence-assisted analysis, and reproducible science;\n**(6)**\nengage in public-private partnerships to streamline the transfer of technology developed using Network infrastructure;\n**(7)**\ndevelop and maintain a financial sustainability plan to reduce long-term reliance on Federal funds, including through user fees, licensing, consortia membership, or other revenue-generating models;\n**(8)**\nestablish performance metrics, including scientific output, cost-effectiveness, academic engagement, private-sector engagement, user satisfaction, and reproducibility of results; and\n**(9)**\nwhere practicable, leverage commercially available hardware and software solutions to minimize cost and accelerate deployment of automated science capabilities.\n#### 4. Interagency collaboration\nNot later than 180 days after all nodes of the Network are designated, the Director of the National Institute of Standards and Technology, in cooperation with the Director and participating eligible entities (including institutions of higher education), shall\u2014\n**(1)**\ndevelop and promulgate standards to ensure interoperability across Network nodes, including laboratory instrumentation, data infrastructure, communication protocols, and experiment execution systems;\n**(2)**\nestablish protocols for secure, seamless, and standardized data-sharing among all members of the Network aligned with node-level cybersecurity and research security protocols;\n**(3)**\ndefine minimum technical requirements and operating procedures to support remote experimentation, experiment reproducibility, and artificial intelligence-assisted workflows; and\n**(4)**\nperiodically update such standards in consultation with private-sector partners and nodes of the Network to reflect advancements in hardware, software, and automation technology.\n#### 5. Assessment of non-designated laboratories\n##### (a) Assessment requirement\nNot later than 180 days after the Director designates the final node of the Network under section 3, the Director, in consultation with the Secretary of Energy and the Director of the National Institute of Standards and Technology, shall conduct and submit to the appropriate committees of Congress, a comprehensive assessment of non-designated laboratories.\n##### (b) Scope\nThe assessment shall identify, to the extent practicable\u2014\n**(1)**\nFederal laboratories, institutions of higher education, nonprofit organizations, and private-sector laboratories that possess or are developing programmable, automated, or remotely accessible research infrastructure;\n**(2)**\nthe instrumentation, automation, and data capabilities of such laboratories;\n**(3)**\ncybersecurity and research security measures relevant to interoperability;\n**(4)**\nexisting or potential pathways for such laboratories to coordinate with Network nodes in areas such as data-sharing, standards adoption, or pilot interoperability projects; and\n**(5)**\nlegal, contractual, or intellectual property considerations that may affect participation.\n##### (c) Confidentiality and security\nProprietary information shall be protected from public disclosure consistent with applicable law. The Director shall publish a nonproprietary public summary of the assessment and may submit a proprietary annex to the congressional committees of jurisdiction.\n#### 6. Reporting and oversight\n##### (a) Annual Briefings\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Director shall brief the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives on the status of the Network.\n##### (b) Contents\nEach briefing required under subsection (a) shall include an assessment of\u2014\n**(1)**\nthe alignment of supported research with national scientific and economic priorities;\n**(2)**\nthe progress each node of the Network has made toward achieving self-sustainability as described in section 3(d)(2); and\n**(3)**\nthe performance metrics established in section 3(g)(8).\n#### 7. Sunset\nThe National Programmable Cloud Laboratories Network, including all authorities, programs, and funding provided under this Act, shall terminate on September 30, 2031.",
      "versionDate": "2025-12-11",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-02-17T19:11:05Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-02-17T19:13:46Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-02-17T19:10:56Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-07T17:35:41Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-02-17T19:11:39Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-02-17T19:13:34Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-02-17T19:16:13Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-02-17T19:11:53Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2026-02-17T19:11:23Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-02-17T19:13:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-07T15:37:05Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3468is.xml"
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
      "title": "National Programmable Cloud Laboratories Network Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "National Programmable Cloud Laboratories Network Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a national programmable cloud laboratories network to enhance research efficiency, innovation, and collaboration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:48:27Z"
    }
  ]
}
```
