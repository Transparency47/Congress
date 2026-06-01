# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2308?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2308
- Title: FEMA Independence Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2308
- Origin chamber: House
- Introduced date: 2025-03-24
- Update date: 2026-01-13T01:07:04Z
- Update date including text: 2026-01-13T01:07:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-24 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-24 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- 2025-03-24 - Committee: Referred to the Subcommittee on Emergency Management and Technology.
- Latest action: 2025-03-24: Introduced in House

## Actions

- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-24 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-24 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- 2025-03-24 - Committee: Referred to the Subcommittee on Emergency Management and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2308",
    "number": "2308",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "FEMA Independence Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-13T01:07:04Z",
    "updateDateIncludingText": "2026-01-13T01:07:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-24",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-24",
      "committees": {
        "item": {
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Emergency Management and Technology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T16:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-24T20:44:39Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-24T16:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-24T17:51:25Z",
              "name": "Referred to"
            }
          },
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
        }
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
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "FL"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2308ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2308\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2025 Mr. Moskowitz (for himself and Mr. Donalds ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish the Federal Emergency Management Agency as a cabinet-level independent agency, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the FEMA Independence Act of 2025 .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Establishment of FEMA as cabinet-level independent agency.\nSec. 3. Director; deputy directors; regional offices.\nSec. 4. Authority and responsibilities.\nSec. 5. Office of the Inspector General.\nSec. 6. Transfer of functions.\nSec. 7. Personnel and other transfers.\nSec. 8. Savings provisions.\nSec. 9. References.\nSec. 10. Offices and functions of Department of Homeland Security.\nSec. 11. Homeland security grants.\nSec. 12. Conforming amendments to other laws.\nSec. 13. Report on recommended legislation.\nSec. 14. Definitions.\n#### 2. Establishment of FEMA as cabinet-level independent agency\n##### (a) In general\nThe Federal Emergency Management Agency is established as a cabinet-level independent establishment in the executive branch.\n##### (b) Mission\nThe primary mission of the Agency is to reduce the loss of life and property and protect the Nation from all hazards, including natural disasters, acts of terrorism, and other man-made disasters, by leading and supporting the Nation in a risk-based, comprehensive emergency management system of preparedness, protection, response, recovery, and mitigation.\n#### 3. Director; deputy directors; regional offices\n##### (a) Director\n**(1) In general**\nThe Agency shall be headed by a Director, who shall be appointed by the President, by and with the advice and consent of the Senate, and who shall report directly to the President.\n**(2) Qualifications**\nThe Director shall be appointed from among individuals who have\u2014\n**(A)**\na demonstrated ability in and knowledge of emergency management and homeland security; and\n**(B)**\nnot less than 5 years of executive leadership and management experience in the public sector and 5 years of such experience in the private sector.\n**(3) Executive schedule**\nTitle 5, United States Code, is amended\u2014\n**(A)**\nin section 5312 by adding at the end the following:\nDirector of the Federal Emergency Management Agency. ; and\n**(B)**\nin section 5313 by striking the item relating to Administrator of the Federal Emergency Management Agency. .\n##### (b) Deputy directors\n**(1) In general**\nThe President may appoint, by and with the advice and consent of the Senate, not more than 4 Deputy Directors to assist the Director in carrying out the functions and authorities of the Director.\n**(2) Executive schedule**\nSection 5314 of title 5, United States Code, is amended by striking Deputy Administrators, Federal Emergency Management Agency and inserting Deputy Directors, Federal Emergency Management Agency .\n##### (c) Regional offices\n**(1) In general**\nThere shall be in the Agency 10 Regional Offices, as identified by the Director.\n**(2) Regional Directors**\nEach Regional Office shall be headed by a Regional Director who shall be chosen by the Director.\n#### 4. Authority and responsibilities\n##### (a) In general\nThe Director shall provide the Federal leadership necessary to prepare for, respond to, recover from, and mitigate hazards.\n##### (b) Stafford Act\nThe Director shall assist the President in carrying out the functions under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ) and carrying out all functions and authorities given to the Administrator of the Federal Emergency Management Agency under that Act.\n##### (c) Mission\nThe responsibilities of the Director shall include carrying out the mission of the Agency by leading and supporting the Nation in a comprehensive emergency management system of\u2014\n**(1)**\nmitigation, by taking sustained actions to reduce or eliminate long-term risks to people and property from hazards and their effects;\n**(2)**\npreparedness, by planning, training, conducting exercises, and building the emergency management profession to prepare effectively for mitigating, responding to, and recovering from any hazard;\n**(3)**\nresponse, by conducting emergency operations to save lives and property through positioning emergency equipment, personnel, and supplies, through evacuating potential victims, through providing food, water, shelter, and medical care to those in need, and through restoring critical public services; and\n**(4)**\nrecovery, by rebuilding communities so individuals, businesses, and governments can function on their own, return to normal life, and protect against future hazards.\n##### (d) Response duties\nIn carrying out subsection (c)(3), the Director, at a minimum, shall\u2014\n**(1)**\nhelp to ensure the effectiveness of emergency response providers in responding to a hazard;\n**(2)**\ncoordinate and provide the Federal Government\u2019s response to hazards;\n**(3)**\nbuild a comprehensive national incident management system with Federal, State, and local government personnel, agencies, and authorities to respond to hazards;\n**(4)**\nconsolidate existing Federal Government emergency response plans into a single, coordinated plan to be known as the National Response Plan;\n**(5)**\nadminister and ensure the implementation of the National Response Plan, including coordinating and ensuring the readiness of each emergency support function under the National Response Plan; and\n**(6)**\nhelp ensure the acquisition of operable and interoperable communications capabilities by Federal, State, local, and tribal governments and emergency response providers.\n##### (e) Continuity of Government\nThe Director shall prepare and implement the plans and programs of the Federal Government for\u2014\n**(1)**\ncontinuity of operations;\n**(2)**\ncontinuity of Government; and\n**(3)**\ncontinuity of plans.\n##### (f) Other duties\nThe Director shall\u2014\n**(1)**\ncoordinate the National Advisory Council;\n**(2)**\nmaintain and operate within the Agency the National Response Coordination Center (or its successor);\n**(3)**\ndevelop and maintain a national emergency management system that is capable of preparing for, responding to, recovering from, and mitigating hazards of all magnitudes, including catastrophic disasters; and\n**(4)**\nsupervise grant programs administered by the Agency.\n##### (g) All-Hazards approach\nIn carrying out the responsibilities under this section, the Director shall coordinate the implementation of an all-hazards strategy that builds those common capabilities necessary to prepare for, respond to, recover from, and mitigate hazards.\n#### 5. Office of the Inspector General\nThe Agency shall have an Office of the Inspector General, headed by an Inspector General, in accordance with chapter 4 of title 5, United States Code (commonly known as the Inspector General Act of 1978 ).\n#### 6. Transfer of functions\n##### (a) In general\nThere shall be transferred to the Director all functions of the Federal Emergency Management Agency, as such Agency was constituted on the day before the date of enactment of this Act.\n##### (b) Inspector General\nThere shall be transferred to the Inspector General all functions relating to the Inspector General that were transferred from the Federal Emergency Management Agency to the Department of Homeland Security on or after January 1, 2003.\n##### (c) Transition period\nThe transfers under this section shall be carried out not later than 365 days following the date of enactment of this Act. During the transition period, the Secretary of Homeland Security shall provide to the Director such assistance, including the use of personnel and assets, as the Director may request in preparing for the transfer.\n#### 7. Personnel and other transfers\n##### (a) Personnel appointments\nThe Director may appoint and fix the compensation of such officers and employees as may be necessary to carry out the respective functions transferred by section 6.\n##### (b) Transfer and allocations of appropriations and personnel\nExcept as otherwise provided in this Act, the personnel employed in connection with, and the assets, liabilities, contracts, property, records, and unexpended balances of appropriations, authorizations, allocations, and other funds employed, used, held, arising from, available to, or to be made available in connection with the functions transferred by section 6, subject to section 1531 of title 31, United States Code, shall be transferred to the Agency. Unexpended funds transferred pursuant to this subsection shall be used only for the purposes for which the funds were originally authorized and appropriated.\n##### (c) Incidental transfers\nThe Director of the Office of Management and Budget, in consultation with the Director of the Federal Emergency Management Agency, may make such determinations as may be necessary with regard to the functions transferred by section 6, and may make such additional incidental dispositions of personnel, assets, liabilities, grants, contracts, property, records, and unexpended balances of appropriations, authorizations, allocations, and other funds held, used, arising from, available to, or to be made available in connection with such functions, as may be necessary to carry out the provisions of this Act. The Director of the Office of Management and Budget shall provide for the termination of the affairs of all entities terminated by this Act and for such further measures and dispositions as may be necessary to effectuate the purposes of this Act.\n##### (d) Effect on personnel\n**(1) In general**\nExcept as otherwise provided by this Act, the transfer pursuant to this Act of full-time personnel (except special Government employees) and part-time personnel holding permanent positions shall not cause any such employee to be separated or reduced in grade or compensation for 1 year after the date of transfer of such employee under this Act.\n**(2) Executive schedule positions**\nExcept as otherwise provided in this Act, any person who, on the day preceding the date of the transfers of functions by section 6, held a position compensated in accordance with the Executive Schedule prescribed in chapter 53 of title 5, United States Code, and who, without a break in service, is appointed in the Agency to a position having duties comparable to the duties performed immediately preceding such appointment shall continue to be compensated in such new position at not less than the rate provided for such previous position, for the duration of the service of such person in such new position.\n#### 8. Savings provisions\n##### (a) Continuing effect of legal documents and actions\n**(1) In general**\nThe legal documents and actions described in paragraph (2) shall continue in effect according to their terms until modified, terminated, superseded, set aside, or revoked in accordance with law by the President, the Director, other authorized official, a court of competent jurisdiction, or by operation of law.\n**(2) Legal documents and actions described**\nThe legal documents and actions described in this paragraph are all orders, determinations, rules, regulations, permits, agreements, grants, contracts, certificates, licenses, registrations, privileges, and other administrative actions that both\u2014\n**(A)**\nhave been issued, made, granted, or allowed to become effective by the President, any Federal agency or official thereof, or by a court of competent jurisdiction, in the performance of functions that are transferred by section 6; and\n**(B)**\nare in effect on the date of the transfers of functions by section 6, or were final before such date and are to become effective on or after such date.\n##### (b) Proceedings not affected\nThe provisions of this Act shall not affect any proceedings, including notices of proposed rulemaking, or any application for any license, permit, certificate, or financial assistance pending before the Agency on the date of the transfers of functions by section 6, with respect to functions transferred by section 6, but such proceedings and applications shall continue. Orders shall be issued in such proceedings, appeals shall be taken therefrom, and payments shall be made pursuant to such orders, as if this Act had not been enacted, and orders issued in any such proceedings shall continue in effect until modified, terminated, superseded, or revoked by a duly authorized official, by a court of competent jurisdiction, or by operation of law. Nothing in this paragraph shall be considered to prohibit the discontinuance or modification of any such proceeding under the same terms and conditions and to the same extent that such proceeding could have been discontinued or modified if this Act had not been enacted.\n##### (c) Causes of action not affected\nThe provisions of this Act shall not affect any cause of action commenced before the date of the transfers of functions by section 6, and in all such causes of action, proceedings shall be had, appeals taken, and judgments rendered in the same manner and with the same effect as if this Act had not been enacted.\n##### (d) Nonabatement of causes of action\nNo cause of action commenced by or against the Agency, or by or against any individual in the official capacity of such individual as an officer of the Agency, shall abate by reason of the enactment of this Act.\n##### (e) Administrative actions relating to promulgation of regulations\nAny administrative action relating to the preparation or promulgation of a regulation by the Agency relating to a function transferred by section 6 may be continued by the Agency with the same effect as if this Act had not been enacted.\n#### 9. References\n##### (a) References to FEMA\nAny reference to the Federal Emergency Management Agency in any law, Executive order, rule, regulation, certificate, directive, instruction, delegation of authority, or other official paper shall be considered to refer and apply to the Agency established by section 2.\n##### (b) References to Director or Administrator of FEMA\nAny reference to the Director or the Administrator of the Federal Emergency Management Agency in any law, Executive order, rule, regulation, certificate, directive, instruction, delegation of authority, or other official paper shall be considered to refer and apply to the Director established by section 3(a)(1).\n##### (c) References to Inspector General\nAny reference to the Inspector General of the Federal Emergency Management Agency or to the functions relating to such office that were transferred from the Federal Emergency Management Agency to the Department of Homeland Security on or after January 1, 2003, in any law, Executive order, rule, regulation, certificate, directive, instruction, delegation of authority, or other official paper shall be considered to refer and apply to the Inspector General established by section 5 or to the functions related to such office.\n#### 10. Offices and functions of Department of Homeland Security\n##### (a) Repeals\nThe following provisions of the Homeland Security Act of 2002 ( 6 U.S.C. 101 et seq. ) are repealed:\n**(1)**\nSection 501 ( 6 U.S.C. 311 ).\n**(2)**\nSection 503 ( 6 U.S.C. 313 ).\n**(3)**\nSection 504 ( 6 U.S.C. 314 ).\n**(4)**\nSection 505 ( 6 U.S.C. 315 ).\n**(5)**\nSection 506 ( 6 U.S.C. 316 ).\n**(6)**\nSection 507 ( 6 U.S.C. 317 ).\n**(7)**\nSection 508 ( 6 U.S.C. 318 ).\n**(8)**\nSection 509 ( 6 U.S.C. 319 ).\n**(9)**\nSection 510 ( 6 U.S.C. 320 ).\n**(10)**\nSection 513 ( 6 U.S.C. 321b ).\n**(11)**\nSection 514 ( 6 U.S.C. 321c ).\n**(12)**\nSection 519 ( 6 U.S.C. 321h ).\n##### (b) Redesignations\nSections 502, 511, 512, 515, 517, 518, 520, 521, 522, 523, 524, 525, 526, 527, 528, and 529 of such Act ( 6 U.S.C. 312 , 321, 321a, 321d, 321f, 321g, 321i, 321j, 321k, 321l, 321m, 321n, 321o, 321p, 321q, and 321r) are redesignated as sections 501 through 516, respectively.\n##### (c) Title heading\nThe heading for title V of such Act is amended by striking National Emergency Management and inserting Other Offices and Functions .\n##### (d) Table of contents\nThe table of contents contained in section 1(b) of such Act is amended by striking the items relating to title V and inserting the following:\nTITLE V\u2014OTHER OFFICES AND FUNCTIONS Sec. 501. Definition. Sec. 502. The National Infrastructure Simulation and Analysis Center. Sec. 503. Evacuation plans and exercises. Sec. 504. National Operations Center. Sec. 505. Nuclear incident response. Sec. 506. Conduct of certain public health-related activities. Sec. 507. Use of commercially available technology, goods, and services. Sec. 508. Procurement of security countermeasures for strategic national stockpile. Sec. 509. Model standards and guidelines for critical infrastructure workers. Sec. 510. Guidance and recommendations. Sec. 511. Voluntary private sector preparedness accreditation and certification program. Sec. 512. Acceptance of gifts. Sec. 513. Integrated public alert and warning system modernization. Sec. 514. National planning and education. Sec. 515. Coordination of Department of Homeland Security efforts related to food, agriculture, and veterinary defense against terrorism. Sec. 516. Transfer of equipment during a public health emergency. .\n##### (e) Effective date\nThe amendments made by this section shall take effect on the date on which the transfers of functions by section 6 are carried out.\n#### 11. Homeland security grants\n##### (a) References to Administrator\nTitle XX of the Homeland Security Act of 2002 ( 6 U.S.C. 601 et seq. ) is amended\u2014\n**(1)**\nin section 2002(a) ( 6 U.S.C. 603(a) ) by striking , through the Administrator, ;\n**(2)**\nin section 2009(a) ( 6 U.S.C. 609a(a) ) by striking , acting through the Administrator, ;\n**(3)**\nin the subsection heading for section 2022(c) ( 6 U.S.C. 612(c) ) by striking by the Administrator ; and\n**(4)**\nby striking Administrator each place it appears and inserting Secretary .\n##### (b) Exceptions\nTitle XX of the Homeland Security Act of 2002 ( 6 U.S.C. 601 et seq. ), as amended by subsection (a), is further amended\u2014\n**(1)**\nin section 2001(1) ( 6 U.S.C. 601(1) ) by striking Secretary each place it appears and inserting Director ;\n**(2)**\nin section 2006(b)(4)(F) ( 6 U.S.C. 607(b)(4)(F) ) by striking Secretary and inserting Director ; and\n**(3)**\nin section 2006(b)(5) ( 6 U.S.C. 607(b)(5) ) by striking Secretary and inserting Director .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date on which the transfers of functions by section 6 are carried out.\n#### 12. Conforming amendments to other laws\n##### (a) Improvements to information technology\nSection 640(a) of the Post-Katrina Emergency Management Reform Act of 2006 ( 6 U.S.C. 727(a) ) is amended by striking , in coordination with the Chief Information Officer of the Department, .\n##### (b) Chief Financial Officer\nSection 901(b)(2) of title 31, United States Code, is amended by adding at the end the following:\n(H) The Federal Emergency Management Agency. .\n##### (c) References\nSubsection (c) of section 612 of the Post-Katrina Emergency Management Reform Act of 2006 ( 6 U.S.C. 313 note) is repealed.\n##### (d) Effective date\nThe amendments made by this section shall take effect on the date on which the transfers of functions by section 6 are carried out.\n#### 13. Report on recommended legislation\n##### (a) In general\nAfter consultation with Congress, the Director shall prepare a report describing recommended legislation for additional technical and conforming amendments to reflect the changes made by this Act.\n##### (b) Submission to Congress\nNot later than 90 days after the last day of the transition period referred to in section 6(c), the Director shall submit to Congress the report referred to in subsection (a).\n#### 14. Definitions\nIn this Act:\n**(1) Agency**\nThe term Agency means the Federal Emergency Management Agency established by section 2.\n**(2) Director**\nThe term Director means the Director of the Federal Emergency Management Agency established by section 3(a).\n**(3) Hazard**\nThe term hazard has the meaning given that term in section 602(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5195a(a) ) and includes any major disaster or emergency.\n**(4) Inspector General**\nThe term Inspector General means the Inspector General of the Federal Emergency Management Agency established by section 5.",
      "versionDate": "2025-03-24",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-13T21:17:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
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
          "measure-id": "id119hr2308",
          "measure-number": "2308",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-24",
          "originChamber": "HOUSE",
          "update-date": "2026-01-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2308v00",
            "update-date": "2026-01-13"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>FEMA Independence Act of 2025</strong></p><p>This bill establishes the Federal Emergency Management Agency (FEMA) as an independent, cabinet-level agency in the executive branch. It also transfers from FEMA to the Department of Homeland Security (DHS) certain grant programs for protecting communities and nonprofits from terrorist attacks.</p><p>The bill removes FEMA from DHS. FEMA\u2019s existing functions as a DHS component must transfer to FEMA as an independent agency within one year after the bill\u2019s enactment. The independent\u00a0FEMA generally retains its existing mission, authorities, and functions. FEMA continues to have 10 regional offices.</p><p>The bill requires\u00a0FEMA to be headed by a Director who is appointed by the President and confirmed by the Senate and reports directly to the President as a Cabinet member. (Under current law, the President may designate the\u00a0FEMA Administrator as a Cabinet member in the event of a disaster.) The Director must have knowledge of emergency management and homeland security and five years of leadership experience in each the public sector and the private sector. The President may appoint up to four Deputy Directors.</p><p>The bill also establishes within FEMA an Office of the Inspector General.</p><p>Also, the bill transfers from FEMA to DHS the authority to administer the Homeland Security Grant Program, Urban Area Security Initiative, and Nonprofit Security Grant Program.\u00a0</p>"
        },
        "title": "FEMA Independence Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2308.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>FEMA Independence Act of 2025</strong></p><p>This bill establishes the Federal Emergency Management Agency (FEMA) as an independent, cabinet-level agency in the executive branch. It also transfers from FEMA to the Department of Homeland Security (DHS) certain grant programs for protecting communities and nonprofits from terrorist attacks.</p><p>The bill removes FEMA from DHS. FEMA\u2019s existing functions as a DHS component must transfer to FEMA as an independent agency within one year after the bill\u2019s enactment. The independent\u00a0FEMA generally retains its existing mission, authorities, and functions. FEMA continues to have 10 regional offices.</p><p>The bill requires\u00a0FEMA to be headed by a Director who is appointed by the President and confirmed by the Senate and reports directly to the President as a Cabinet member. (Under current law, the President may designate the\u00a0FEMA Administrator as a Cabinet member in the event of a disaster.) The Director must have knowledge of emergency management and homeland security and five years of leadership experience in each the public sector and the private sector. The President may appoint up to four Deputy Directors.</p><p>The bill also establishes within FEMA an Office of the Inspector General.</p><p>Also, the bill transfers from FEMA to DHS the authority to administer the Homeland Security Grant Program, Urban Area Security Initiative, and Nonprofit Security Grant Program.\u00a0</p>",
      "updateDate": "2026-01-13",
      "versionCode": "id119hr2308"
    },
    "title": "FEMA Independence Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>FEMA Independence Act of 2025</strong></p><p>This bill establishes the Federal Emergency Management Agency (FEMA) as an independent, cabinet-level agency in the executive branch. It also transfers from FEMA to the Department of Homeland Security (DHS) certain grant programs for protecting communities and nonprofits from terrorist attacks.</p><p>The bill removes FEMA from DHS. FEMA\u2019s existing functions as a DHS component must transfer to FEMA as an independent agency within one year after the bill\u2019s enactment. The independent\u00a0FEMA generally retains its existing mission, authorities, and functions. FEMA continues to have 10 regional offices.</p><p>The bill requires\u00a0FEMA to be headed by a Director who is appointed by the President and confirmed by the Senate and reports directly to the President as a Cabinet member. (Under current law, the President may designate the\u00a0FEMA Administrator as a Cabinet member in the event of a disaster.) The Director must have knowledge of emergency management and homeland security and five years of leadership experience in each the public sector and the private sector. The President may appoint up to four Deputy Directors.</p><p>The bill also establishes within FEMA an Office of the Inspector General.</p><p>Also, the bill transfers from FEMA to DHS the authority to administer the Homeland Security Grant Program, Urban Area Security Initiative, and Nonprofit Security Grant Program.\u00a0</p>",
      "updateDate": "2026-01-13",
      "versionCode": "id119hr2308"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2308ih.xml"
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
      "title": "FEMA Independence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FEMA Independence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Federal Emergency Management Agency as a cabinet-level independent agency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:35Z"
    }
  ]
}
```
