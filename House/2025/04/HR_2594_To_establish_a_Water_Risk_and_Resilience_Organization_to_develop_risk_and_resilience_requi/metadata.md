# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2594?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2594
- Title: To establish a Water Risk and Resilience Organization to develop risk and resilience requirements for the water sector.
- Congress: 119
- Bill type: HR
- Bill number: 2594
- Origin chamber: House
- Introduced date: 2025-04-02
- Update date: 2025-09-05T08:06:09Z
- Update date including text: 2025-09-05T08:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-02 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-02 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-04-02: Introduced in House

## Actions

- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-02 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-02 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2594",
    "number": "2594",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001087",
        "district": "1",
        "firstName": "Eric",
        "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
        "lastName": "Crawford",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "To establish a Water Risk and Resilience Organization to develop risk and resilience requirements for the water sector.",
    "type": "HR",
    "updateDate": "2025-09-05T08:06:09Z",
    "updateDateIncludingText": "2025-09-05T08:06:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-02",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T22:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-02T22:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-02T21:24:25Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "MN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2594ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2594\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Mr. Crawford introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a Water Risk and Resilience Organization to develop risk and resilience requirements for the water sector.\n#### 1. Water risk and resilience organization\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Covered water system**\nThe term covered water system means\u2014\n**(A)**\na community water system (as defined in section 1401 of the Safe Drinking Water Act ( 42 U.S.C. 300f )) that serves a population of 3,300 or more persons; or\n**(B)**\na treatment works (as defined in section 212 of the Federal Water Pollution Control Act ( 33 U.S.C. 1292 )) that serves a population of 3,300 or more persons.\n**(3) Cyber resilient**\n**(A) In general**\nThe term cyber resilient means the ability of a covered water system to withstand or reduce the magnitude or duration of cybersecurity incidents that disrupt the ability of the covered water system to function normally.\n**(B) Inclusion**\nThe term cyber resilient includes the ability of a covered water system to anticipate, absorb, adapt to, or rapidly recover from cybersecurity incidents.\n**(4) Cybersecurity incident**\nThe term cybersecurity incident means a malicious act or suspicious event that disrupts, or attempts to disrupt, the operation of programmable electronic devices and communication networks, including hardware, software, and data that are essential to the cyber resilient operation of a covered water system.\n**(5) Cybersecurity risk and resilience requirement**\nThe term cybersecurity risk and resilience requirement means a requirement that provides for the cyber resilient operation of a covered water system and the cyber resilient design of planned additions or modifications to a covered water system.\n**(6) Water risk and resilience organization; wrro**\nThe terms Water Risk and Resilience Organization and WRRO mean the organization certified by the Administrator under subsection (c).\n##### (b) Applicability\nNot later than 270 days after the date of enactment of this Act, the Administrator shall issue a final rule to carry out this section, including regulations for the selection and certification of the WRRO under subsection (c).\n##### (c) Certification\n**(1) In general**\nFollowing the issuance of the final rule under subsection (b)(1), any organization may submit an application to the Administrator, at such time, in such manner, and containing such information as the Administrator may require, for certification as the Water Risk and Resilience Organization.\n**(2) Requirements**\nThe Administrator shall certify not more than 1 organization that submitted an application under paragraph (1) as the Water Risk and Resilience Organization if the Administrator determines that the organization\u2014\n**(A)**\ndemonstrates advanced technical knowledge and expertise in the operations of covered water systems;\n**(B)**\nis comprised of 1 or more members with relevant experience as owners or operators of covered water systems;\n**(C)**\nhas demonstrated the ability to develop and implement cybersecurity risk and resilience requirements that provide for an adequate level of cybersecurity risk and resilience for a covered water system;\n**(D)**\nis capable of establishing measures, in line with prevailing best practices, to secure sensitive information and to protect sensitive security information from public disclosure; and\n**(E)**\nhas established rules that\u2014\n**(i)**\nrequire that the organization be independent of the users, owners, and operators of a covered water system, with balanced and objective stakeholder representation in the selection of directors of the organization and balanced decision making in any committee or subordinate organizational structure;\n**(ii)**\nrequire that the organization allocate reasonable dues, fees, and other charges among end-users for all activities under this section;\n**(iii)**\nprovide just and reasonable procedures for enforcement of cybersecurity risk and resilience requirements and the imposition of penalties in accordance with subsection (f), including limitations on activities, functions, or operations, or other appropriate sanctions; and\n**(iv)**\nprovides for reasonable notice and opportunity for public comment, due process, openness, and balancing of interests in developing cybersecurity risk and resilience requirements and otherwise exercising duties described in this section.\n##### (d) Cybersecurity risk and resilience requirements\n**(1) In general**\n**(A) Proposed requirements**\nThe WRRO shall file with the Administrator each cybersecurity risk and resilience requirement or modification to such a requirement that the WRRO proposes to be made effective under this section.\n**(B) Implementation plan**\n**(i) In general**\nFor each proposed cybersecurity risk and resilience requirement or modification to such a requirement filed pursuant to subparagraph (A), the WRRO shall file an implementation plan, including the schedule for implementation, which may include a specified date, by which covered water systems shall achieve compliance with all of the cybersecurity risk and resilience requirement or modification to such a requirement. The implementation schedule may account for a phased rollout of the requirement, recognizing that the requirement may not apply, in totality, to all covered water systems.\n**(ii) Reasonable deadlines**\nThe enforcement date proposed by the WRRO in the implementation plan under clause (i) shall provide a reasonable implementation period for covered water systems to meet the requirements under the implementation plan.\n**(2) Approval**\n**(A) In general**\nNotwithstanding paragraph (3)(A), the Administrator shall approve a proposed cybersecurity risk and resilience requirement or modification to such a requirement, including the accompanying implementation plan filed under paragraph (1), if the Administrator determines that the requirement is just, reasonable, and not unduly discriminatory or preferential.\n**(B) Deference to wrro**\nThe Administrator shall defer to the technical expertise of the WRRO with respect to the content of a proposed cybersecurity risk and resilience requirement or modification to such a requirement.\n**(3) Disapproval of requirement**\n**(A) In general**\nNotwithstanding paragraph (2)(A), if the Administrator disapproves, in whole or in part, a filed cybersecurity risk and resilience requirement or modification to such a requirement, the Administrator shall remand such requirement to the WRRO and provide to the WRRO specific recommendations that would lead to the approval of the cybersecurity risk and resilience requirement or modification to such requirement under paragraph (2).\n**(B) Timeline**\nThe Administrator shall remand to the WRRO a proposed cybersecurity risk and resilience requirement or modification to such a requirement disapproved under subparagraph (A), including the submission of the specific recommendations required under that subparagraph, not later than 90 days after the date on which the WRRO filed the requirement or modification with the Administrator under paragraph (1)(A).\n**(C) Response and approval**\n**(i) In general**\nOn receipt of the remand of a proposed cybersecurity risk and resilience requirement or modification to such a requirement and receipt of the specific recommendations of the Administrator pursuant to subparagraph (A), the WRRO shall\u2014\n**(I)**\naccept the recommendations of the Administrator and resubmit an amended proposed cybersecurity risk and resilience requirement or modification to such a requirement consistent with those recommendations;\n**(II)**\nprovide to the Administrator and a reason why the recommendation was not accepted; or\n**(III)**\nwithdraw the proposed cybersecurity risk and resilience requirement or modification to such a requirement.\n**(ii) Amended requirement**\nIf the WRRO files an amended proposed cybersecurity risk and resilience requirement or modification to such a requirement under clause (i)(I) the Administrator shall review such proposed requirement or modification and determine whether to approve such amended requirement or modification in accordance with paragraph (2)(A).\n**(iii) Response by WRRO**\nOn receipt of a response from the WRRO pursuant to clause (i)(II), the Administrator shall\u2014\n**(I)**\napprove the proposed cybersecurity risk and resilience requirement or modification to such a requirement; or\n**(II)**\ninvite the WRRO to engage in negotiations with the Administrator to reach consensus to address the specific recommendation made by the Administrator under subparagraph (A).\n**(4) Effective date**\nThe effective date of an approved cybersecurity risk and resilience requirement or modification to such a requirement proposed under this subsection shall be set by the Administrator in accordance with the proposed implementation plan submitted by the WRRO under paragraph (1).\n**(5) Submission of specific requirement**\nThe Administrator, on the motion of the Administrator or on complaint may, following consultation with the WRRO, order the WRRO to file with the Administrator under paragraph (1) a proposed cybersecurity risk and resilience requirement or modification to such as requirement that addresses a specific matter if the Administrator determines there is a reasonable basis to conclude the existing cybersecurity risk and resilience requirements are insufficient, when implemented by covered water systems, to protect, defend, or recover from or mitigate a cybersecurity incident.\n**(6) Conflict**\n**(A) In general**\nThe final rule adopted under subsection (b)(2) shall include specific processes for the identification and timely resolution of any conflict between a cybersecurity risk and resilience requirement and any function, rule, order, tariff, or agreement accepted, approved, or ordered by the Administrator that is applicable to a covered water system.\n**(B) Compliance**\nA covered water system shall continue to comply with a function, rule, order, tariff, or agreement described in subparagraph (A) unless\u2014\n**(i)**\nthe Administrator finds a conflict exists between a cybersecurity risk and resilience requirement and any function, rule, order, tariff, or agreement approved or otherwise accepted or ordered by the Administrator;\n**(ii)**\nthe Administrator orders a change to that function, rule, order, tariff, or agreement; and\n**(iii)**\nthe ordered change becomes effective.\n**(C) Modification**\nIf the Administrator determines that a cybersecurity risk and resilience requirement needs to be changed as a result of a conflict identified under this paragraph, the Administrator shall direct the WRRO to propose and file with the Administrator a modified cybersecurity risk and resilience requirement pursuant to paragraphs (1) through (4) of this section.\n##### (e) Water system monitoring and assessment\nTo aid in the development and adoption of appropriate and necessary cybersecurity risk and resilience requirements and modifications to such requirements, the WRRO shall\u2014\n**(1)**\nroutinely monitor and conduct periodic assessments of the implementation of cybersecurity risk and resilience requirements approved by the Administrator under subsection (d) and the effectiveness of cybersecurity risk and resilience requirements for covered systems, including by requiring\u2014\n**(A)**\nannual self-attestations of compliance with such cybersecurity risk and resilience requirements by covered water systems; and\n**(B)**\nassessments of the covered water system by the WRRO or by a third party designated by the WRRO not less frequently than every 5 years of compliance by covered water systems with such cybersecurity risk and resilience requirements; and\n**(2)**\nannually submit to the Administrator a report describing the implementation of cybersecurity risk and resilience requirements approved by the Administrator under subsection (d) and the effectiveness of cybersecurity risk and resilience requirements for covered water systems subject to the requirements that reports under this paragraph\u2014\n**(A)**\nshall only include aggregated or anonymized findings, observations, and data; and\n**(B)**\nshall not contain any sensitive security information.\n##### (f) Enforcement\n**(1) In general**\nThe WRRO may, subject to paragraphs (2) through (5), impose a penalty on the owner or operator of a covered water system for a violation of a cybersecurity risk and resilience requirement if the WRRO, after notice and an opportunity for a consultation and a hearing\u2014\n**(A)**\nfinds that the owner or operator of a covered system has violated or failed to comply with the cybersecurity risk and resilience requirement; and\n**(B)**\nfiles notice of the finding under subparagraph (A) and the record of the proceeding with the Administrator.\n**(2) Notice**\n**(A) In general**\nThe WRRO may not impose a penalty on the owner or operator of a covered water system under paragraph (1) unless the WRRO provides the owner or operator with\u2014\n**(i)**\nnotice of the alleged violation of or failure to comply with a cybersecurity risk and resilience requirement; and\n**(ii)**\nan opportunity for a consultation and a hearing prior to finding that the owner or operator has violated or failed to comply with the applicable cybersecurity risk and resilience requirement under paragraph (1)(A).\n**(B) Access to counsel**\nThe owner or operator of a covered water system may engage legal counsel to take part in the consultation and hearing described in subparagraph (A)(ii).\n**(3) Effective date of penalty**\nA penalty imposed under paragraph (1) may take effect not earlier than 31 days after the date on which the WRRO files with the Administrator notice of the penalty and the record of proceedings under subparagraph (B) of that paragraph.\n**(4) Imposition of penalty**\n**(A) Maximum amount**\nA penalty imposed under paragraph (1) shall not exceed $25,000 per day the applicable owner or operator is in violation of a cybersecurity risk and resilience requirement approved by the Administrator under subsection (d).\n**(B) Limitation**\nNo penalty may be imposed on a covered water system under any other provision of law for a violation of a cybersecurity risk and resilience requirement approved by the Administrator under subsection (d).\n**(C) Use of penalty funds**\nAny penalties collected under this subsection shall be returned to the WRRO to support training initiatives and other resource capabilities of the WRRO in carrying out the duties of the WRRO under this section.\n**(5) Review by administrator**\n**(A) In general**\nThe Administrator may review a penalty imposed under paragraph (1).\n**(B) Application for review**\nThe Administrator may conduct a review under subparagraph (A) on the motion of the Administrator or on application by an owner or operator of a covered water system that is the subject of a penalty imposed under paragraph (1), if such application is filed not later than 30 days after the date on which the notice of that penalty is filed with the Administrator.\n**(C) Stay of penalty**\nA penalty under review by the Administrator under this paragraph may only be stayed if, on the motion of the Administrator or on application by the owner or operator of the covered water system that is the subject of the penalty, the Administrator separately orders the stay of the penalty.\n**(D) Proceedings**\n**(i) In general**\nIn any proceeding to review a penalty imposed under paragraph (1), the Administrator, after notice and, subject to clause (ii), opportunity for a hearing, shall by order affirm, set aside, reinstate, or modify the penalty, and, if appropriate, remand to the WRRO for further proceedings.\n**(ii) Record below**\nA hearing under clause (i) may consist solely of the record before the WRRO and an opportunity for the presentation of supporting reasons to affirm, modify, or set aside the applicable penalty.\n**(iii) Expedited procedures**\nThe Administrator shall act expeditiously in administering all proceedings under this paragraph.\n##### (g) Savings provisions\n**(1) Authority**\nNothing in this section authorizes the WRRO or the Administrator to develop binding cybersecurity risk and resilience requirements for covered water systems, except as specifically provided for in this Act.\n**(2) Rule of construction**\nNothing in this section preempts any authority of any State to take action to ensure the safety, adequacy, and resilience of water service within that State, as long as such action is not inconsistent with or in conflict with any cybersecurity risk and resilience requirement.\n##### (h) Status of WRRO\nThe WRRO is not a department, agency, or instrumentality of the United States Government.\n##### (i) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $10,000,000 to remain available to the WRRO until expended.",
      "versionDate": "2025-04-02",
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
        "name": "Environmental Protection",
        "updateDate": "2025-04-09T14:21:44Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2594ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a Water Risk and Resilience Organization to develop risk and resilience requirements for the water sector.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:48:21Z"
    },
    {
      "title": "To establish a Water Risk and Resilience Organization to develop risk and resilience requirements for the water sector.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:29Z"
    }
  ]
}
```
