# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2417?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2417
- Title: Strengthening Agency Management and Oversight of Software Assets Act
- Congress: 119
- Bill type: HR
- Bill number: 2417
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-03-03T01:54:09Z
- Update date including text: 2026-03-03T01:54:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2417",
    "number": "2417",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001078",
        "district": "11",
        "firstName": "Gerald",
        "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
        "lastName": "Connolly",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Strengthening Agency Management and Oversight of Software Assets Act",
    "type": "HR",
    "updateDate": "2026-03-03T01:54:09Z",
    "updateDateIncludingText": "2026-03-03T01:54:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MD"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2417ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2417\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Connolly (for himself, Mr. Fallon , Mrs. McClain Delaney , and Ms. Mace ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo improve the visibility, accountability, and oversight of agency software asset management practices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Agency Management and Oversight of Software Assets Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of General Services.\n**(2) Agency**\nThe term agency has the meaning given that term in section 3502 of title 44, United States Code, except that such term does not include an element of the intelligence community.\n**(3) Cloud computing**\nThe term cloud computing has the meaning given the term in Special Publication 800\u2013145 of the National Institute of Standards and Technology, or any successor document.\n**(4) Cloud service provider**\nThe term cloud service provider has the meaning given the term in section 3607(b) of title 44, United States Code.\n**(5) Comprehensive assessment**\nThe term comprehensive assessment means a comprehensive assessment conducted pursuant to section 3(a).\n**(6) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(7) Intelligence community**\nThe term intelligence community has the meaning given the term in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 ).\n**(8) Plan**\nThe term plan means the plan developed by a Chief Information Officer, or equivalent official, pursuant to section 4(a).\n**(9) Software entitlement**\nThe term software entitlement means any software that\u2014\n**(A)**\nhas been purchased, leased, or licensed by or billed to an agency under any contract or other business arrangement; and\n**(B)**\nis subject to use limitations.\n**(10) Software inventory**\nThe term software inventory means the software inventory of an agency required pursuant to\u2014\n**(A)**\nsection 2(b)(2)(A) of the Making Electronic Government Accountable By Yielding Tangible Efficiencies Act of 2016 ( 40 U.S.C. 11302 note; Public Law 114\u2013210 ); or\n**(B)**\nsubsequent guidance issued by the Director pursuant to that Act.\n#### 3. Software inventory update and expansion\n##### (a) In general\nAs soon as practicable, and not later than 18 months after the date of enactment of this Act, the Chief Information Officer of each agency, in consultation with the Chief Financial Officer, the Chief Acquisition Officer, the Chief Data Officer, and General Counsel of the agency, or the equivalent officials of the agency, shall complete a comprehensive assessment of the software paid for by, in use at, or deployed throughout the agency, which shall include\u2014\n**(1)**\nthe current software inventory of the agency, including software entitlements, contracts and other agreements or arrangements of the agency, and a list of the largest software entitlements of the agency separated by provider and category of software;\n**(2)**\na comprehensive, detailed accounting of\u2014\n**(A)**\nany software used by or deployed within the agency, including software developed or built by the agency, or by another agency for use by the agency, including shared services, as of the date of the comprehensive assessment, including, to the extent identifiable, the contracts and other agreements or arrangements used by the agency to acquire, build, deploy, or use such software;\n**(B)**\ninformation and data on software entitlements, which shall include information on any additional fees or costs, including fees or costs for the use of cloud services, that are not included in the initial costs of the contract, agreement, or arrangement\u2014\n**(i)**\nfor which the agency pays;\n**(ii)**\nthat are not deployed or in use by the agency; and\n**(iii)**\nthat are billed to the agency under any contract or business arrangement that creates duplication, or are otherwise determined to be unnecessary by the Chief Information Officer of the agency, or the equivalent official, in the deployment or use by the agency; and\n**(C)**\nthe extent\u2014\n**(i)**\nto which any software paid for, in use, or deployed throughout the agency is interoperable; and\n**(ii)**\nof the efforts of the agency to improve interoperability of software assets throughout the agency enterprise;\n**(3)**\na categorization of software entitlements of the agency by cost, volume, and type of software;\n**(4)**\na list of any provisions in the software entitlements of the agency that may restrict how the software can be deployed, accessed, or used, including any such restrictions on desktop or server hardware, through a cloud service provider, or on data ownership or access; and\n**(5)**\nan analysis addressing\u2014\n**(A)**\nthe accuracy and completeness of the comprehensive assessment;\n**(B)**\nagency management of and compliance with all contracts or other agreements or arrangements that include or reference software entitlements or software management within the agency;\n**(C)**\nthe extent to which the agency accurately captures the total cost of software entitlements and related costs, including the total cost of upgrades over the life of a contract, cloud usage costs, and any other cost associated with the maintenance or servicing of contracts; and\n**(D)**\ncompliance with software license management policies of the agency.\n##### (b) Contract support\n**(1) Authority**\nThe head of an agency may enter into 1 or more contracts to support the requirements of subsection (a).\n**(2) No conflict of interest**\nContracts under paragraph (1) shall not include contractors with organizational conflicts of interest, within the meaning given that term under subpart 9.5 of the Federal Acquisition Regulation.\n**(3) Operational independence**\nOver the course of a comprehensive assessment, contractors hired pursuant to paragraph (1) shall maintain operational independence from the integration, management, and operations of the software inventory and software entitlements of the agency.\n##### (c) Submission\nOn the date on which the Chief Information Officer, Chief Financial Officer, Chief Acquisition Officer, the Chief Data Officer, and General Counsel of an agency, or the equivalent officials of the agency, complete the comprehensive assessment, the Chief Information Officer shall submit the comprehensive assessment to the head of the agency.\n##### (d) Subsequent submission\nNot later than 30 days after the date on which the head of an agency receives the comprehensive assessment under subsection (c), the head of the agency shall submit the comprehensive assessment to\u2014\n**(1)**\nthe Director;\n**(2)**\nthe Administrator;\n**(3)**\nthe Comptroller General of the United States;\n**(4)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(5)**\nthe Committee on Oversight and Accountability of the House of Representatives.\n##### (e) Consultation\nIn order to ensure the utility and standardization of the comprehensive assessment of each agency, including to support the development of each plan and the report required under section 4(e)(2), the Director, in consultation with the Administrator, shall share information, best practices, and recommendations relating to the activities performed in the course of a comprehensive assessment of an agency.\n##### (f) Intelligence community\nFor each element of the intelligence community, a comprehensive assessment described under subsection (a) shall be\u2014\n**(1)**\nconducted separately;\n**(2)**\nperformed only by an entity designated by the head of the element of the intelligence community, in accordance with appropriate applicable laws;\n**(3)**\nperformed in such a manner as to ensure appropriate protection of information which, if disclosed, may adversely affect national security; and\n**(4)**\nsubmitted in summary form, not later than 30 days after the date on which the head of the element of the intelligence community receives the assessment, by the head of the element of the intelligence community to\u2014\n**(A)**\nthe Director;\n**(B)**\nthe Select Committee on Intelligence of the Senate; and\n**(C)**\nthe Permanent Select Committee on Intelligence of the House of Representatives.\n#### 4. Software modernization planning at agencies\n##### (a) In general\nThe Chief Information Officer of each agency, in consultation with the Chief Financial Officer, the Chief Acquisition Officer, the Chief Data Officer, and the General Counsel of the agency, or the equivalent officials of the agency, shall use the information developed pursuant to the comprehensive assessment of the agency to develop a plan for the agency\u2014\n**(1)**\nto consolidate software entitlements of the agency;\n**(2)**\nto ensure that, in order to improve the performance of, and reduce unnecessary costs to, the agency, the Chief Information Officer, Chief Data Officer, and Chief Acquisition Officer of the agency, or the equivalent officers, develop criteria and procedures for how the agency will adopt cost-effective acquisition strategies, including enterprise licensing, across the agency that reduce costs, eliminate excess licenses, and improve performance; and\n**(3)**\nto restrict the ability of a bureau, program, component, or operational entity within the agency to acquire, use, develop, or otherwise leverage any software entitlement (or portion thereof) without the approval of the Chief Information Officer of the agency, in consultation with the Chief Acquisition Officer of the agency, or the equivalent officers of the agency.\n##### (b) Plan requirements\nThe plan of an agency shall\u2014\n**(1)**\ninclude a detailed strategy for\u2014\n**(A)**\nthe remediation of any software asset management deficiencies found during the comprehensive assessment of the agency;\n**(B)**\nthe ongoing maintenance of software asset management upon the completion of the remediation;\n**(C)**\nautomation of software license management processes and incorporation of discovery tools across the agency;\n**(D)**\nensuring that officers and employees of the agency are adequately trained in the policies, procedures, rules, regulations, and guidance relating to the software acquisition and development of the agency before entering into any agreement relating to any software entitlement (or portion thereof) for the agency, including training on\u2014\n**(i)**\nnegotiating options within contracts to address and minimize provisions that restrict how the agency may deploy, access, or use the software, including restrictions on deployment, access, or use on desktop or server hardware and restrictions on data ownership or access;\n**(ii)**\nthe differences between acquiring commercial software products and services and acquiring or building custom software; and\n**(iii)**\ndetermining the costs of different types of licenses and options for adjusting licenses to meet increasing or decreasing demand; and\n**(E)**\nmaximizing the effectiveness of software deployed by the agency, including, to the extent practicable, leveraging technologies that\u2014\n**(i)**\nmeasure actual software usage via analytics that can identify inefficiencies to assist in rationalizing software spending;\n**(ii)**\nallow for segmentation of the user base;\n**(iii)**\nsupport effective governance and compliance in the use of software; and\n**(iv)**\nsupport interoperable capabilities between software;\n**(2)**\nidentify categories of software the agency could prioritize for conversion to more cost-effective software licenses, including enterprise licenses, as the software entitlements, contracts, and other agreements or arrangements come up for renewal or renegotiation;\n**(3)**\nprovide an estimate of the costs to move toward more enterprise, open-source, or other licenses that do not restrict the use of software by the agency, and the projected cost savings, efficiency measures, and improvements to agency performance throughout the total software lifecycle;\n**(4)**\nidentify potential mitigations to minimize software license restrictions on how such software can be deployed, accessed, or used, including any mitigations that would minimize any such restrictions on desktop or server hardware, through a cloud service provider, or on data ownership or access;\n**(5)**\nensure that the purchase by the agency of any software is based on publicly available criteria that are not unduly structured to favor any specific vendor, unless prohibited by law (including regulation);\n**(6)**\ninclude any estimates for additional resources, services, or support the agency may need to implement the plan;\n**(7)**\nprovide information on the prevalence of software products in use across multiple software categories; and\n**(8)**\ninclude any additional information, data, or analysis determined necessary by the Chief Information Officer, or other equivalent official, of the agency.\n##### (c) Support\nThe Chief Information Officer, or other equivalent official, of an agency may request support from the Director and the Administrator for any analysis or developmental needs to create the plan of the agency.\n##### (d) Agency submission\n**(1) In general**\nNot later than 1 year after the date on which the head of an agency submits the comprehensive assessment pursuant to section 3(d), the head of the agency shall submit to the Director, the Committee on Homeland Security and Governmental Affairs of the Senate, and the Committee on Oversight and Accountability of the House of Representatives the plan of the agency.\n**(2) Intelligence community**\nNot later than 1 year after the date on which the head of an element of the intelligence community submits the summary assessment pursuant to section 3(f)(4), the head of the element shall separately submit the plan of the element to the Director, the Select Committee on Intelligence of the Senate, and the Permanent Select Committee on Intelligence of the House of Representatives.\n##### (e) Consultation and coordination\nThe Director\u2014\n**(1)**\nin coordination with the Administrator, the Chief Information Officers Council, the Chief Acquisition Officers Council, the Chief Data Officers Council, the Chief Financial Officers Council, and other government and industry representatives identified by the Director, shall establish processes, using existing reporting functions, as appropriate, to identify, define, and harmonize common definitions, terms and conditions, standardized requirements, and other information and criteria to support agency heads in developing and implementing the plans required by this section; and\n**(2)**\nin coordination with the Administrator, and not later than 2 years after the date of enactment of this Act, submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Accountability of the House of Representatives a report detailing recommendations to leverage Government procurement policies and practices with respect to software acquired by, developed by, deployed within, or in use at 1 or more agencies to\u2014\n**(A)**\nincrease the interoperability of software licenses, including software entitlements and software built by Government agencies;\n**(B)**\nconsolidate licenses, as appropriate;\n**(C)**\nreduce costs;\n**(D)**\nimprove performance; and\n**(E)**\nmodernize the management and oversight of software entitlements and software built by Government agencies, as identified through an analysis of agency plans.\n#### 5. GAO report\nNot later than 3 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Accountability of the House of Representatives a report on\u2014\n**(1)**\nGovernment-wide trends in agency software asset management practices;\n**(2)**\ncomparisons of software asset management practices among agencies;\n**(3)**\nthe establishment by the Director of processes to identify, define, and harmonize common definitions, terms, and conditions under section 4(e);\n**(4)**\nagency compliance with the restrictions on contract support under section 3(b); and\n**(5)**\nother analyses of and findings regarding the plans of agencies, as determined by the Comptroller General of the United States.\n#### 6. No additional funds\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-12-16",
        "text": "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "5457",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Strengthening Agency Management and Oversight of Software Assets Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-04",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "1956",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Strengthening Agency Management and Oversight of Software Assets Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Accounting and auditing",
            "updateDate": "2025-12-17T19:22:21Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-12-17T19:22:21Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-12-17T19:22:21Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-17T19:22:21Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-12-17T19:22:21Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-12-17T19:22:21Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-12-17T19:22:21Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-12-17T19:22:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-20T18:10:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119hr2417",
          "measure-number": "2417",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-27",
          "originChamber": "HOUSE",
          "update-date": "2026-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2417v00",
            "update-date": "2026-03-03"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Strengthening Agency Management and Oversight of Software Assets Act</strong></p><p>This bill requires federal agencies and Intelligence Community (IC) elements to assess their software inventory and develop software management plans.</p><p>The bill requires each agency and each IC element to complete a comprehensive assessment of the software paid for by, in use at, or deployed throughout the agency or element. The assessment must include information such as (1) the current inventory of software; (2) contracts and other arrangements used to acquire, build, deploy, or use the software; (3) costs and fees not included in the initial contract or agreement; and (4) the interoperability of the software and restrictions on its use.</p><p>Each agency and IC element must use their assessment to develop a plan to consolidate software entitlements, develop procedures for cost-effective acquisition strategies, and restrict subordinate entities from using any software entitlement without approval.\u00a0(A software entitlement is software that has been purchased, leased, or licensed by or billed to an agency and that is subject to use limitations.)\u00a0Such plans must be submitted to\u00a0the Office of Management and Budget (OMB) and Congress.\u00a0</p><p>Within two years of enactment, OMB must submit recommendations to Congress regarding government software procurement policies and practices to</p><p>\u00a0 \u00a0 \u2022 increase the interoperability of software licenses;<br/>\u00a0 \u00a0 \u2022 consolidate licenses when appropriate;<br/>\u00a0 \u00a0 \u2022 reduce costs;<br/>\u00a0 \u00a0 \u2022 improve performance; and<br/>\u00a0 \u00a0 \u2022 modernize the management and oversight of agency software.<br/>\u00a0 \u00a0\u00a0<br/>The GAO must report on certain related topics, including governmentwide trends in agency software asset management practices and comparisons of such practices among agencies.</p>"
        },
        "title": "Strengthening Agency Management and Oversight of Software Assets Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2417.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strengthening Agency Management and Oversight of Software Assets Act</strong></p><p>This bill requires federal agencies and Intelligence Community (IC) elements to assess their software inventory and develop software management plans.</p><p>The bill requires each agency and each IC element to complete a comprehensive assessment of the software paid for by, in use at, or deployed throughout the agency or element. The assessment must include information such as (1) the current inventory of software; (2) contracts and other arrangements used to acquire, build, deploy, or use the software; (3) costs and fees not included in the initial contract or agreement; and (4) the interoperability of the software and restrictions on its use.</p><p>Each agency and IC element must use their assessment to develop a plan to consolidate software entitlements, develop procedures for cost-effective acquisition strategies, and restrict subordinate entities from using any software entitlement without approval.\u00a0(A software entitlement is software that has been purchased, leased, or licensed by or billed to an agency and that is subject to use limitations.)\u00a0Such plans must be submitted to\u00a0the Office of Management and Budget (OMB) and Congress.\u00a0</p><p>Within two years of enactment, OMB must submit recommendations to Congress regarding government software procurement policies and practices to</p><p>\u00a0 \u00a0 \u2022 increase the interoperability of software licenses;<br/>\u00a0 \u00a0 \u2022 consolidate licenses when appropriate;<br/>\u00a0 \u00a0 \u2022 reduce costs;<br/>\u00a0 \u00a0 \u2022 improve performance; and<br/>\u00a0 \u00a0 \u2022 modernize the management and oversight of agency software.<br/>\u00a0 \u00a0\u00a0<br/>The GAO must report on certain related topics, including governmentwide trends in agency software asset management practices and comparisons of such practices among agencies.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119hr2417"
    },
    "title": "Strengthening Agency Management and Oversight of Software Assets Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strengthening Agency Management and Oversight of Software Assets Act</strong></p><p>This bill requires federal agencies and Intelligence Community (IC) elements to assess their software inventory and develop software management plans.</p><p>The bill requires each agency and each IC element to complete a comprehensive assessment of the software paid for by, in use at, or deployed throughout the agency or element. The assessment must include information such as (1) the current inventory of software; (2) contracts and other arrangements used to acquire, build, deploy, or use the software; (3) costs and fees not included in the initial contract or agreement; and (4) the interoperability of the software and restrictions on its use.</p><p>Each agency and IC element must use their assessment to develop a plan to consolidate software entitlements, develop procedures for cost-effective acquisition strategies, and restrict subordinate entities from using any software entitlement without approval.\u00a0(A software entitlement is software that has been purchased, leased, or licensed by or billed to an agency and that is subject to use limitations.)\u00a0Such plans must be submitted to\u00a0the Office of Management and Budget (OMB) and Congress.\u00a0</p><p>Within two years of enactment, OMB must submit recommendations to Congress regarding government software procurement policies and practices to</p><p>\u00a0 \u00a0 \u2022 increase the interoperability of software licenses;<br/>\u00a0 \u00a0 \u2022 consolidate licenses when appropriate;<br/>\u00a0 \u00a0 \u2022 reduce costs;<br/>\u00a0 \u00a0 \u2022 improve performance; and<br/>\u00a0 \u00a0 \u2022 modernize the management and oversight of agency software.<br/>\u00a0 \u00a0\u00a0<br/>The GAO must report on certain related topics, including governmentwide trends in agency software asset management practices and comparisons of such practices among agencies.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119hr2417"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2417ih.xml"
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
      "title": "Strengthening Agency Management and Oversight of Software Assets Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Agency Management and Oversight of Software Assets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve the visibility, accountability, and oversight of agency software asset management practices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:27Z"
    }
  ]
}
```
