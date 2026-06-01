# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3800?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3800
- Title: ePermit Act
- Congress: 119
- Bill type: S
- Bill number: 3800
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-04-08T15:30:57Z
- Update date including text: 2026-04-08T15:30:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-02-05: Introduced in Senate

## Actions

- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3800",
    "number": "3800",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "ePermit Act",
    "type": "S",
    "updateDate": "2026-04-08T15:30:57Z",
    "updateDateIncludingText": "2026-04-08T15:30:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T19:57:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NJ"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "AZ"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "MT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3800is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3800\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Mr. Curtis (for himself, Mr. Booker , Mr. Budd , Mr. Kelly , Mr. McCormick , Mr. Padilla , Mr. Daines , and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo improve environmental reviews and authorizations through the use of interactive, digital, and cloud-based platforms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ePermit Act .\n#### 2. Findings\nThe Congress finds that\u2014\n**(1)**\ncoordination between Federal, State, and local agencies and project sponsors is critical to ensuring the timely and effective completion of environmental reviews and authorizations, including through the sharing of relevant information, alignment of environmental review timelines, and integration of authorizations, while maintaining compliance with applicable statutory and regulatory requirements;\n**(2)**\ndigital strategies for environmental reviews have proven to make the community engagement process more accessible, available, and transparent to all stakeholders, especially the communities in which new projects are built;\n**(3)**\nestablishing robust data architectures will ensure data integrity, improve transparency, reduce costs, and enhance the ability of the Federal Government to serve the public;\n**(4)**\nFederal agency use of modern software that can track the full lifecycle of environmental reviews and authorizations is critical for\u2014\n**(A)**\neffective project management and process improvement;\n**(B)**\nenabling workflow automation, transparency, and tracking; and\n**(C)**\nsimplifying reporting requirements;\n**(5)**\nmodern business process management systems that track Federal agency workflows and produce vendor neutral, interoperable event, task, and other milestone data that can be shared with other Federal agency systems can reduce costs and improve performance for Federal agencies responsible for environmental reviews and authorizations;\n**(6)**\ncase and project management systems\u2014\n**(A)**\nare essential tools for managing the tasks and activities associated with environmental reviews and authorizations; and\n**(B)**\nprovide Federal agencies more data and insight into such environmental reviews and authorizations;\n**(7)**\nwell-defined business rules can enable process automation that allows Federal agencies responsible for environmental reviews or authorizations to expedite routine tasks and workflows, and improve transparency and accuracy of project timeline estimates, which in turn can help project sponsors better plan for application preparation and project delivery milestones;\n**(8)**\ntaking a standardized, digital-first perspective to environmental reviews and authorizations at Federal agencies responsible for environmental reviews or authorizations will improve document quality, lead to more concise reports, enable the reuse and accessibility of the data underpinning Federal agency analyses and decisions, and enable objective, technology-assisted evaluation of environmental impacts, analysis, and documentation, and accelerate future environmental reviews and authorizations;\n**(9)**\nFederal agencies responsible for environmental reviews or authorizations, project sponsors, and the public should have access to up-to-date information on accurate timelines and the status of environmental reviews and authorizations; and\n**(10)**\nallowing for seamless information exchange among Federal agencies and between Federal agencies and project sponsors will increase predictability and efficiency of environmental review and authorization schedules for project sponsors.\n#### 3. Establishment of data standards\n##### (a) In general\nNot later than 60 days after the date of enactment of this Act, the Chair of the Council on Environmental Quality, in consultation with the Federal Permitting Improvement Steering Council, the Chief Information Officers Council, the Office of Management and Budget, and other relevant stakeholders and Federal agencies, shall develop, publish, and iteratively update data standards for the collection and curation of authorization data by Federal agencies, which shall be used to\u2014\n**(1)**\nassist with environmental reviews and authorizations;\n**(2)**\norganize, define, and standardize various concepts, formats, and protocols that are included in environmental reviews and authorizations; and\n**(3)**\nreduce the need for redundant environmental reviews by creating a shared vocabulary and software systems that will support vendor neutrality, data interoperability, workflow automation, and automatic data exchange between Federal agencies.\n##### (b) Inclusions\nThe data standards developed, published, and iteratively updated under subsection (a) shall include the following:\n**(1)**\nA standardized taxonomy that allows Federal agencies to identify and track data types, relationships, and values.\n**(2)**\nComprehensive categories for data, such as\u2014\n**(A)**\nprojects;\n**(B)**\nprocesses;\n**(C)**\nenvironmental documents;\n**(D)**\npublic comments;\n**(E)**\ngeospatial information;\n**(F)**\npublic engagement events, as applicable by process or Federal agency;\n**(G)**\ncase events; and\n**(H)**\nmilestones to ensure clarity and uniformity.\n#### 4. Development of prototype tools\nThe Chair of the Council on Environmental Quality, in consultation with the Administrator of General Services, the Federal Permitting Improvement Steering Council, the Chief Information Officers Council, the Director of the Office of Management and Budget, and other relevant stakeholders and Federal agencies, shall design, test, and build prototype tools for environmental reviews and authorizations that will assist Federal agencies in implementing the minimum functional requirements described in section 5. The Chair of the Council on Environmental Quality shall prioritize designing, testing, and building tools under this section that\u2014\n**(1)**\nsupport authorization case or project management systems that manage tasks, milestones, and activities associated with environmental reviews and authorizations, and provide Federal agencies more data and insight into such reviews and authorizations;\n**(2)**\nenable\u2014\n**(A)**\napplication submission and tracking portals used by project sponsors, enabling greater transparency; and\n**(B)**\npublic comment opportunity tracking portals to increase transparency;\n**(3)**\nfacilitate automated applications, environmental reviews. and authorizations;\n**(4)**\nallow data exchange between Federal agency systems; and\n**(5)**\naccelerate complex environmental reviews.\n#### 5. Publication of guidance for implementation of data standards and minimum functional requirements\n##### (a) Publication\nNot later than 120 days after the date of enactment of this Act, the Chair of the Council on Environmental Quality shall publish guidance for how each Federal agency responsible for environmental reviews or authorizations implements\u2014\n**(1)**\nthe data standards published under section 3; and\n**(2)**\nthe following minimum functional requirements:\n**(A)**\nApplication data sharing that enables automated transfer of relevant environmental review and authorization data among Federal agencies.\n**(B)**\nAutomated project screening to assist frontline staff with reviewing project sponsor provided information for completeness and accuracy and determining if a categorical exclusion or other general authorization applies to an action. Automated project screening may not be used by the Council on Environmental Quality or a Federal agency to unlawfully restrict any activities on Federal lands.\n**(C)**\nPublic availability of screening criteria and related decision models.\n**(D)**\nAutomated case or project management tools which include a repository of relevant data and metadata that enable advanced tracking, reporting, and optimization to aid workflows.\n**(E)**\nIntegrated geographic information system analysis tools which incorporate geospatial data layers and models for each resource analyzed as part of an environmental review or authorization for a given study area.\n**(F)**\nDocument management tools that preserve metadata associated with geospatial analysis, modeling, and other analytic processes conducted during an environmental review or authorization, to support future reviews and enable Artificial Intelligence-assisted analysis of past decisions.\n**(G)**\nAutomated comment compilation and analysis tools, including services for comment categorization and response that handle the lifecycle of comment submission, analysis, categorization and response with Artificial Intelligence support where appropriate.\n**(H)**\nAdministrative record management tools that maintain both portable document formats and data-rich repositories accessible to both machine and human users.\n**(I)**\nCommon or interoperable Federal agency services that integrate shared services, shared applications, and common user experiences for Federal agency staff, project sponsors, and the public.\n##### (b) Inclusions\nThe guidance published under this section shall include the following:\n**(1)**\nGuidelines for cloud-based storage, data sharing protocols, and application programming interfaces to enable the Council on Environmental Quality to work with Federal agencies to use authorization data to aid Federal agencies in modernizing their environmental reviews and authorizations and for iterative development of the authorization portal.\n**(2)**\nProvisions that support scalability and adaptability of the minimum requirements to emerging technologies.\n#### 6. Implementation of data standards and minimum functional requirements\n##### (a) Implementation\nThe head of each Federal agency responsible for environmental reviews or authorizations shall\u2014\n**(1)**\nnot later than 90 days after the date of enactment of this Act\u2014\n**(A)**\ncompare existing Federal agency systems for environmental reviews and authorizations under their authority with the data standards published under section 3 and the minimum functional requirements described in section 5(a)(2) and report findings from such comparison to the Council on Environmental Quality;\n**(B)**\nassess whether existing Federal agency technological capabilities are consistent with the data standards published under section 3 and the minimum functional requirements described in section 5(a)(2);\n**(C)**\nsubmit to the Council on Environmental Quality a report that estimates the completion dates for implementing the data standards published under section 3 and the minimum functional requirements described in section 5(a)(2); and\n**(D)**\nsubmit to the Council on Environmental Quality, in consultation with the Council on Environmental Quality, an implementation plan that\u2014\n**(i)**\ndescribes how the Federal agency will implement the data standards published under section 3 and the minimum functional requirements described in section 5(a)(2); and\n**(ii)**\ndescribes how, to the extent the Federal agency determines necessary to meet relevant statutory requirements, the Federal agency will adopt or implement the prototype tools tested, designed, and built under section 4; and\n**(2)**\nnot later than 180 days after the date of enactment of this Act, begin implementing the data standards published under section 3 and the minimum functional requirements described in section 5(a)(2).\n##### (b) Report\nNot less frequently than twice each year, the Chief Information Officer of each Federal agency, in consultation with the Chief Environmental Review and Permitting Officer of each Federal agency, shall submit to the Council on Environmental Quality and the Director of the Office of Management and Budget a report on the progress of the Federal agency towards meeting the requirements of subsection (a).\n#### 7. Unified interagency data system\n##### (a) In general\n**(1) Unified interagency data system**\nTo the maximum extent practicable, the Chair of the Council of Environmental Quality and the head of each Federal agency responsible for environmental reviews or authorizations shall iteratively develop and maintain a unified interagency data system consisting of interconnected Federal agency systems and shared services for environmental reviews and authorizations.\n**(2) Authorization portal**\n**(A) In general**\nThe shared services developed and maintained under paragraph (1) shall include a common interactive, digital, cloud-based authorization portal, which shall\u2014\n**(i)**\nbe designed in a manner consistent with\u2014\n**(I)**\nthe recommendations of the Council on Environmental Quality included in the study submitted pursuant to section 110 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4336d ) titled Council on Environmental Quality Report to Congress on the Potential for Online and Digital Technologies to Address Delays in Reviews and Improve Public Accessibility and Transparency under 42 U.S.C. 4332(2)(C) ; and\n**(II)**\nthe minimum functional requirements described in section 5(a)(2);\n**(ii)**\nserve as a platform for tracking and displaying real-time data on environmental reviews and authorizations made available through application programming interfaces or other reporting mechanisms from Federal agency systems that are compliant with the data standards and data architecture described in this Act;\n**(iii)**\nbe supported by a decentralized, cross-network digital infrastructure software that ensures vendor neutrality and interoperability of data and models across Federal agencies;\n**(iv)**\ninclude a mechanism for the dissemination of relevant information (such as a notice of intent for public comment, public meetings, project statuses, or a notice of intent to begin an environmental review) to local communities, as applicable;\n**(v)**\nallow a project sponsor to submit all necessary documentation for environmental reviews and authorizations in one unified and secure portal;\n**(vi)**\nsupport interactive, digital, and cloud-based tools enabling applicants to edit documents and collaborate with relevant Federal agencies in real time;\n**(vii)**\nsupport visual features, including video, animation, geographic information system displays, interactive maps, and three-dimensional renderings;\n**(viii)**\nprovide for the exchange of information to and from Federal agency data systems via an application programming interface or another reporting mechanisms;\n**(ix)**\nallow for the submission of geospatial data associated with project location, footprint, and impact;\n**(x)**\nsupport automatic documentation of submission and process timelines; and\n**(xi)**\nallow the following metrics to be tracked over time\u2014\n**(I)**\nestimates of achieved efficiencies, such as reductions in the time between receipt of applications and final authorization decisions;\n**(II)**\ncomparisons of authorization timelines before and after the implementation of this Act;\n**(III)**\nusage of the authorization portal and other statistics from the Digital Analytics Program;\n**(IV)**\nmetrics on the number of public comments received, responses provided, and community meetings held;\n**(V)**\nthe number of projects subject to litigation based on authorization deficiencies or inefficiencies;\n**(VI)**\na list of Federal agencies that are not yet fully compliant with the data standards published under section 3 and the minimum functional requirements described in section 5(a)(2), along with their progress toward compliance; and\n**(VII)**\nexamples or repositories of Federal agency-developed digital workflows enabled by the implementation of this Act, including visualizations of data sharing, authorizations and decision logic, and environmental reviews.\n**(B) Administrative support**\nThe Administrator of General Services shall host the authorization portal as a shared service for Congress, Federal agencies, and the public.\n**(C) Accessability**\nThe authorization portal shall be accessible to Congress, Federal agencies, and the public, with appropriate safeguards to protect sensitive or classified information and information restricted by user type as appropriate.\n**(D) Public accessibility**\nTo the extent practicable and consistent with other law, the authorization portal shall provide public access to non-sensitive data, including authorization timelines, location, project type, environmental reviews, and mitigation measures.\n**(E) Congressional access and oversight**\n**(i) In general**\nThe authorization portal shall provide Congress with direct access to aggregated performance data and other analytics to enable real-time oversight of Federal agencies.\n**(ii) Artificial intelligence support systems and training materials**\nCongress shall have access to the data, fine-tuning procedures, and prompt configurations specifically created or adapted for Artificial Intelligence systems used to support environmental review or authorization activities, excluding proprietary or general pretraining materials unrelated to such agency-specific customization.\n**(iii) Technical assistance**\nThe Council on Environmental Quality shall provide to Congress technical assistance upon request to ensure effective use of the authorization portal and Artificial Intelligence systems for oversight purposes.\n**(3) Cybersecurity and compliance considerations**\nThe authorization portal shall be designed to promote vendor neutral interoperability, reduce redundancy, and ensure compliance and coordination with other laws, including\u2014\n**(A)**\nsection 552a of title 5, United States Code (commonly referred to as the Privacy Act of 1974), and subchapter II of chapter 35 of title 44, United States Code;\n**(B)**\nthe Federal Risk and Authorization Management Program established under section 3608 of title 44, United States Code; and\n**(C)**\nthe Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security, for a case in which the project is in coordination with a Federal agency with stringent security requirements.\n##### (b) Deadlines\n**(1) Shared services pilot**\nNot later than one year after the date of enactment of this Act, the Council on Environmental Quality shall oversee piloting of shared services for environmental reviews and authorizations, including the authorization portal under subsection (a)(2).\n**(2) Unified system development and implementation**\nTo the maximum extent practicable, not later than December 1, 2027, the Chair of the Council on Environmental Quality shall develop and implement the unified interagency data system required under subsection (a)(1).\n##### (c) Report\nNot less frequently than annually, the Chair of the Council on Environmental Quality, in consultation with the Federal Permitting Improvement Steering Council, the Chief Information Officers Council, and other relevant stakeholders and Federal agencies, shall submit to the Committee on Natural Resources of the House of Representatives and the Committee on Environment and Public Works of the Senate a report on the Council on Environmental Quality\u2019s progress on developing a unified interagency data system under subsection (a).\n#### 8. Authority to enter into contracts\nThe Council on Environmental Quality may enter into contracts and other arrangements for analyses, services, and products with Federal agencies, private organizations, and businesses, and make such payments as determined necessary by the Council on Environmental Quality to carry out the provisions of this Act.\n#### 9. Clarifying rulemaking authority\nNothing in this Act shall be construed to authorize the Council on Environmental Quality or a Federal agency to impose additional regulatory processes or requirements beyond those expressly stipulated under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) or any other law.\n#### 10. Savings clause\nTo the extent that a data system, technology, or tool developed or incorporated into a unified interagency data system under this Act is not limited by project type, the data system, technology, or tool shall not have its use be restricted by project type.\n#### 11. Definitions\nIn this Act:\n**(1) Authorization**\nThe term authorization means any license, permit, approval, finding, determination, or other administrative decision issued by an agency and any interagency consultation that is required or authorized under Federal law in order to site, construct, reconstruct, or commence operations of a project administered by a Federal agency.\n**(2) Authorization data**\nThe term authorization data means\u2014\n**(A)**\nany data relevant for a Federal agency to\u2014\n**(i)**\ndetermine the effect on the environment of an action for which an authorization is required by the Federal agency; and\n**(ii)**\ndetermine whether to issue such authorization; and\n**(B)**\nany community input or public comment on such determinations.\n**(3) Data architecture**\nThe term data architecture means the design and organization of data systems, including frameworks for data storage, processing, and exchange.\n**(4) Data standards**\nThe term data standards means agreed-upon specifications for data formats, structures, and definitions to ensure consistency and vendor neutral interoperability.\n**(5) Environmental review**\nThe term environmental review means any Federal agency procedures or processes for\u2014\n**(A)**\napplying a categorical exclusion; or\n**(B)**\npreparing an environmental assessment, an environmental impact statement, or another document required under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).\n**(6) Federal agency**\nThe term Federal agency has the meaning given the term agency in section 551 of title 5, United States Code.\n**(7) Federal Permitting Improvement Steering Council**\nThe term Federal Permitting Improvement Steering Council has the meaning given the term Council in section 41001 of the FAST Act ( 42 U.S.C. 4370m ).",
      "versionDate": "2026-02-05",
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
        "actionDate": "2025-12-10",
        "text": "Received in the Senate and Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "4503",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ePermit Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2026-02-27T18:56:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-05",
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
          "measure-id": "id119s3800",
          "measure-number": "3800",
          "measure-type": "s",
          "orig-publish-date": "2026-02-05",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3800v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2026-02-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>ePermit Act</strong></p><p>This bill establishes requirements related to digitizing environmental reviews conducted under the National Environmental Policy Act of 1969 (NEPA).</p><p>The Council on Environmental Quality (CEQ) must develop, publish, and iteratively update data standards for the collection and curation of certain data related to environmental reviews. CEQ must also design, test, and build prototype tools for environmental reviews.</p><p>Additionally, CEQ must publish guidance to assist relevant agencies in implementing such standards as well as certain minimum functional requirements, such as data sharing that enables automated transfer of relevant data among federal agencies. Federal agencies responsible for environmental reviews or authorizations must implement the data standards and such minimum functional requirements.</p><p>To the maximum extent practicable, CEQ and such agencies must iteratively develop and maintain a unified interagency data system consisting of interconnected federal agency systems and shared services for environmental reviews and authorizations, including a common interactive, digital, cloud-based authorization portal.</p><p>Within a year,\u00a0CEQ must oversee a pilot of shared services for environmental reviews and authorizations, including the portal. To the maximum extent practicable, CEQ must develop and implement the unified interagency data system by December 1, 2027.</p>"
        },
        "title": "ePermit Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3800.xml",
    "summary": {
      "actionDate": "2026-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>ePermit Act</strong></p><p>This bill establishes requirements related to digitizing environmental reviews conducted under the National Environmental Policy Act of 1969 (NEPA).</p><p>The Council on Environmental Quality (CEQ) must develop, publish, and iteratively update data standards for the collection and curation of certain data related to environmental reviews. CEQ must also design, test, and build prototype tools for environmental reviews.</p><p>Additionally, CEQ must publish guidance to assist relevant agencies in implementing such standards as well as certain minimum functional requirements, such as data sharing that enables automated transfer of relevant data among federal agencies. Federal agencies responsible for environmental reviews or authorizations must implement the data standards and such minimum functional requirements.</p><p>To the maximum extent practicable, CEQ and such agencies must iteratively develop and maintain a unified interagency data system consisting of interconnected federal agency systems and shared services for environmental reviews and authorizations, including a common interactive, digital, cloud-based authorization portal.</p><p>Within a year,\u00a0CEQ must oversee a pilot of shared services for environmental reviews and authorizations, including the portal. To the maximum extent practicable, CEQ must develop and implement the unified interagency data system by December 1, 2027.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3800"
    },
    "title": "ePermit Act"
  },
  "summaries": [
    {
      "actionDate": "2026-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>ePermit Act</strong></p><p>This bill establishes requirements related to digitizing environmental reviews conducted under the National Environmental Policy Act of 1969 (NEPA).</p><p>The Council on Environmental Quality (CEQ) must develop, publish, and iteratively update data standards for the collection and curation of certain data related to environmental reviews. CEQ must also design, test, and build prototype tools for environmental reviews.</p><p>Additionally, CEQ must publish guidance to assist relevant agencies in implementing such standards as well as certain minimum functional requirements, such as data sharing that enables automated transfer of relevant data among federal agencies. Federal agencies responsible for environmental reviews or authorizations must implement the data standards and such minimum functional requirements.</p><p>To the maximum extent practicable, CEQ and such agencies must iteratively develop and maintain a unified interagency data system consisting of interconnected federal agency systems and shared services for environmental reviews and authorizations, including a common interactive, digital, cloud-based authorization portal.</p><p>Within a year,\u00a0CEQ must oversee a pilot of shared services for environmental reviews and authorizations, including the portal. To the maximum extent practicable, CEQ must develop and implement the unified interagency data system by December 1, 2027.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3800"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3800is.xml"
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
      "title": "ePermit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T06:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ePermit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T06:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve environmental reviews and authorizations through the use of interactive, digital, and cloud-based platforms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T06:18:29Z"
    }
  ]
}
```
