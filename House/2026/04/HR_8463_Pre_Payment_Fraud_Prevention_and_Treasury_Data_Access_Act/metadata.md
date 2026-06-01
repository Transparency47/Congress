# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8463?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8463
- Title: Pre-Payment Fraud Prevention and Treasury Data Access Act
- Congress: 119
- Bill type: HR
- Bill number: 8463
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-18T15:24:32Z
- Update date including text: 2026-05-18T15:24:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-23 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 35 - 1.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-23 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 35 - 1.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8463",
    "number": "8463",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001108",
        "district": "1",
        "firstName": "James",
        "fullName": "Rep. Comer, James [R-KY-1]",
        "lastName": "Comer",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Pre-Payment Fraud Prevention and Treasury Data Access Act",
    "type": "HR",
    "updateDate": "2026-05-18T15:24:32Z",
    "updateDateIncludingText": "2026-05-18T15:24:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 35 - 1.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-29",
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
      "actionDate": "2026-04-23",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
            "date": "2026-04-29T13:08:33Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-23T13:00:30Z",
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
          "date": "2026-04-23T13:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8463ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8463\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Comer (for himself and Mr. Arrington ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish governmentwide requirements for pre-payment fraud prevention actions, to provide the U.S. Treasury appropriate data resources, to facilitate participation in governmentwide anti-fraud data sharing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pre-Payment Fraud Prevention and Treasury Data Access Act .\n#### 2. Pre-payment fraud prevention requirements for agencies\n##### (a) Establishment of pre-Payment agency responsibilities\n**(1) Amendment**\nChapter 33 of title 31, United States Code, is amended by inserting after section 3325 the following:\n3325a. Agency duties for fraud and improper payment prevention before the issuance of a payment voucher request (a) Mandatory actions before issuing a payment voucher The head of an agency, or an officer or employee described in section 3325(a)(1)(B), may not certify a voucher under section 3325 until the following requirements are met: (1) Each pre-certification requirement described in subsection (b) for such payment request. (2) Confirmation is provided that the payment complies with any disbursement requirement and instruction, including any pre-certification requirement, published by the Secretary of the Treasury. (3) Confirmation is provided that any other appropriate payment, account, and payee validation program or service that the Secretary of the Treasury, in consultation with the Director, requires to reduce fraud and an improper payment resulting in financial loss to the Government, including any agency evaluation of the fraud-risk indicator of a program required under section 3352 and agency procedures required under section 3554(b)(1), have been conducted, in accordance with necessary exceptions for statutory, policy, or operational reasons. (b) Payment verification pre-Certification requirements Not later than 180 days after the date of the enactment of this section, and as needed thereafter, the Secretary of the Treasury shall, in consultation with the Director of the Office of Management and Budget, issue regulations, and guidance as necessary, for the pre-certification requirements of this section, for vouchers certified under section 3325, including any deadline for pre-certification information and related records to be submitted to the requisite Treasury official and disbursing official under subchapter IV of this chapter, before the date of disbursement in order to allow for sufficient time to meet the requirements of this section, including the following: (1) Funds are available at the time the obligation is incurred and if an obligation is incurred when funds are not available, then the agency may not certify the payment voucher. (2) The amount of the payment and the name of the payee on the payment voucher are correct, in conformance with the prescribed standard format. (3) A valid social security number, taxpayer identification number, employer identification number, individual taxpayer identification number, or payee ID number is provided for each payee on the voucher, if applicable. (4) The appropriation or fund from which the payment will be made is available for the purpose described in the voucher and indicated with the appropriate Treasury Account Symbol or Business Event Type Code. (5) A payee is not deceased, if the payment would be improperly made to a deceased payee. (6) The account number, if any, provided on the payment voucher is held at a financial institution and is open, valid, and belongs to the payee or a valid designee of the payee. (7) Any other identifier in conformance with the payment verification pre-certification requirements established by the Secretary of the Treasury, which may include the Procurement Instrument Identified and the Federal Award Identification Number. (c) Return of payment voucher The Secretary, in consultation with the Director, shall issue guidance and establish procedures to authorize the Chief Disbursing Officer of the Department of the Treasury, or an agency disbursing official, to return to the relevant agency certifying official, including a notification to the agency, any payment or payment voucher issued under section 3325 which does not comply with pre-certification verification requirements established under this section as determined by the Secretary. (d) Agency requests for exemptions The Secretary of the Treasury shall include in the guidance issued under subsection (b), or in other regulations or guidance issued under this chapter, a process for agencies to request exemptions from some or all of the payment verification requirements for specific payments or categories of payments under this section. Any approved exemption shall be documented in any related payment voucher certified under section 3325 for the duration of the exemption. .\n**(2) Technical and conforming amendment**\nThe table of sections for chapter 33 of title 31, United States Codes, is amended by inserting after the item for section 3325 the following:\n3325a. Agency duties for fraud and improper payment prevention prior to issuing a payment voucher request. .\n##### (b) Amendment to responsibilities of agency certifying official for payment vouchers\nSection 3528(a) of title 31, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by inserting after of this title the following: , including pre-certification requirement described in section 3325a ;\n**(2)**\nby redesignating paragraphs (4) and (5) as paragraphs (5) and (6), respectively; and\n**(3)**\nby inserting after paragraph (3) the following:\n(4) Ensuring that\u2014 (A) the agency has complied with the requirements of section 3325a and subchapter IV of this title; and (B) a covered recipient is in compliance with the reporting requirements under section 6107. .\n##### (c) Prepayment requirements of payment disbursing officials\nSection 3325 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (d) by striking taxpayer identifying number of each person and inserting information required to be submitted under section 3325a(b) of each payee ; and\n**(2)**\nby adding at the end the following:\n(e) (1) Before certifying a voucher to a disbursing official, the head of an agency or an officer or employee of an agency described in subparagraph (A) or (B) of subsection (a)(1), as applicable, shall take necessary actions to accurately disburse payments to the recipients of those payments, including by\u2014 (A) verifying the accuracy of the bank account information to which a payment is to be disbursed, to the extent practicable; and (B) comparing the bank account information of the proposed recipient to other payment records available to the agency, to the extent practicable. (2) The Secretary of the Treasury shall issue guidance to carry out this subsection, which may be carried out through any guidance issued for section 3325a(b). .\n##### (d) Requirements and authorities of payment disbursing officials\nParagraph (3) of section 3325(a) of title 31, United States Code, is amended\u2014\n**(1)**\nby inserting , compliance with an order to pause a payment pursuant to section 3337(b), after except for the correctness of computations on a voucher ; and\n**(2)**\nby striking ,, and inserting a comma.\n##### (e) Addition of fraud prevention indicators to agency improper payment risk assessments\n**(1) Definitions amendments**\nSection 3351 of title 31, United States Code is amended\u2014\n**(A)**\nin paragraph (3)\u2014\n**(i)**\nin the heading, by striking Initiative and inserting System ;\n**(ii)**\nby striking Initiative and inserting System ; and\n**(iii)**\nby striking initiative and inserting system ; and\n**(B)**\nby adding the following in the appropriate alphabetical order and redesignating the paragraphs accordingly:\n(9) Appropriate authorizing and appropriations committees of congress The term appropriate authorizing and appropriations committees of Congress means the following: (A) The Committees on Appropriations of the Senate and the House of Representatives. (B) The Committee on Homeland Security and Governmental Affairs of the Senate. (C) The Committee on Oversight and Government Reform of the House of Representatives. (D) The Budget Committee of the House of Representatives and the Committee on the Budget of the Senate. (D) Any other relevant congressional committee of jurisdiction. (10) Director The term Director means the Director of the Office of Management and Budget. (11) Fraud-risk indicator The term fraud-risk indicator means an objective data point or analytic signal that indicates an anomalous payment pattern or increase in the volume of a payment amount, a verified data mismatch, network or behavioral anomaly, or match identified by the Do Not Pay system and any other payment, account, and payee validation program or service provided by the Department of the Treasury that would result in financial loss to the Government. .\n**(2) Amendment**\nSection 3352(a)(1) of title 31, United States Code, is amended\u2014\n**(A)**\nin subparagraph (A), by striking ; and and inserting a semicolon;\n**(B)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(C) design and apply fraud-risk indicators to the programs identified under paragraph (A). .\n#### 3. Treasury do not pay system\n##### (a) Amendment\nSection 3354 of title 31, United States Code, is amended\u2014\n**(1)**\nin the heading, by striking Initiative and inserting System ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) In general The head of each executive agency shall establish and maintain appropriate preaward and prepayment procedures to prevent and recover improper payments, including payments resulting in financial loss to the Government, and to prevent financial fraud. Such procedures shall include, at a minimum\u2014 (A) screening all persons or entities that receive, or seek to receive, Federal awards or payments against all appropriate Do Not Pay system data assets, including data assets described in paragraph (2)(a), and risk tools before an award is made or a payment request is submitted to the disbursing officer in accordance with section 3325a; and (B) a periodic review of available data assets and notification to the Secretary of any data asset that the agency requires access to, either directly or through the Do Not Pay system. ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking At a minimum and before issuing any payment or award, each executive agency shall review as appropriate the following databases to verify eligibility of the payment and award: and inserting the following: Notwithstanding any other provision of law, including the Internal Revenue Code of 1986, the Social Security Act, and the Personal Responsibility and Work Opportunity Reconciliation Act, the Secretary shall have access to the following data assets and incorporate them in the Do Not Pay system, without the need to pursue designation under paragraph (3), for the sole purposes of improper payment prevention and detection: ; and\n**(ii)**\nby adding at the end the following:\n(G) The National Directory of New Hires pursuant to section 453(j) of the Social Security Act ( 42 U.S.C. 653(j) ). (H) Information made available to such head pursuant to a request made under section 6103(i)(9)(A) of the Internal Revenue Code of 1986. (I) Information made available to the Secretary of Treasury by the Commissioner of Social Security pursuant to section 235 of the Social Security Act. ; and\n**(C)**\nby adding at the end the following:\n(3) Additional data assets (A) Designation The Secretary may designate additional categories of data assets for inclusion in the Do Not Pay system to address risks of fraud and improper payments. (B) Privacy and notice In designating data assets that include personally identifiable information, law enforcement sensitive information, or information subject to section 552a of title 5, the Secretary shall\u2014 (i) act in coordination with the Director of the Office of Management and Budget; and (ii) provide public notice and an opportunity for comment for not less than 30 days prior to designation. (C) Database inclusion Following designation of a category of data assets under subparagraph (A), the Secretary shall provide public notice and an opportunity for comment for not less than 30 days before adding any specific data asset within such category. (D) Non-sensitive data Data assets that do not include personally identifiable or law enforcement sensitive information may be added at the discretion of the Secretary without designation if a list of such data sets is disclosed to the public on a public website maintained by the Department of the Treasury. (4) Treatment of data matching for purposes of agency use of do not pay system For purposes of section 552a of title 5, or any other provision of law, a computerized comparison of two or more automated Federal systems of records, or a computerized comparison of a Federal system of records with other records or non-Federal records, carried out by the Secretary to verify payments or identify or recover improper payments under this section shall not be considered a matching program. (5) Limitation on use Information obtained through the Do Not Pay system may be used solely for the purposes described in paragraph (1), or for Federal or State law enforcement or investigative purposes. Any officer, employee, contractor, subcontractor, or agent of a Federal or State entity may not publish, examine for a purpose not explicitly authorized under this section, or communicate such information furnished in such data assets other than in fulfillment of the purposes of this section. (6) Penalty for unlawful disclosure Any person described in paragraph (5) who knowingly and willfully discloses information in violation of that paragraph shall be fined not more than $5,000, imprisoned not more than 5 years, or both. (7) Exception when payment otherwise required under law The head of an executive agency may be exempt from the requirements of paragraph (1) if a Federal statute expressly requires that a payment or award be made notwithstanding potential ineligibility, and the agency head notifies the Secretary of the Treasury and the Director of the Office of Management and Budget prior to certification of the payment under section 3325. (8) Definition In this section, the term data asset has the meaning given that term in section 3502(17) of title 44. ; and\n**(3)**\nby striking subsections (b) through (e) and inserting the following:\n(b) Establishment of system The Secretary of the Treasury shall establish and maintain a Do Not Pay system, which shall be administered and operated by the Fiscal Service of the Department of the Treasury. The Do Not Pay system shall include\u2014 (1) the data assets described in subsection (a)(2); and (2) such other data assets as the Secretary of the Treasury may designate, in consultation with the Director of the Office of Management and Budget, to assist agencies in carrying out subsection (a)(1). (c) State and other governmental use (1) In general Each State and local government administering a federally funded program, and any contractor, subcontractor, or agent thereof, including State and local government auditors, shall establish and maintain appropriate preaward and prepayment procedures to prevent and recover improper payments, including payments resulting in financial loss to the Government, and to prevent financial fraud. Such procedures shall include, at a minimum\u2014 (A) screening all persons or entities that receive, or seek to receive, Federal awards or payments against all appropriate Do Not Pay system data assets, including data assets described in subsection (a)(2), and risk tools before an award is made or a payment request is submitted to the disbursing officer; and (B) periodic review of available data assets and notification to the Secretary of any data asset that the agency requires access to, either directly or through the Do Not Pay system. (2) Other governmental use The judicial and legislative branches of the United States (as defined in section 202(e) of title 18) shall have access to the Do Not Pay system for purposes of verifying eligibility for payments and preventing fraud and improper payments. (3) Privacy requirements The Secretary, in consultation with the Director of the Office of Management and Budget, shall issue guidance establishing privacy and other requirements applicable to such access, consistent with section 552a of title 5. (d) Annual report The Secretary shall submit to the appropriate authorizing and appropriations committees of Congress an annual report on the operation of the Do Not Pay system, which may be included as part of another report submitted to Congress by the Secretary, and which shall include the following: (1) An evaluation of the effectiveness of the system in reducing improper payments. (2) Information on the frequency of corrections and identification of erroneous data. (3) Recommendations for legislative or administrative action to enhance the operations of the system. (4) An assessment of agency compliance with the requirements of this section, including a listing of all memorandums established with the head of an agency under subsection (a)(4) that documents agency use of the Do Not Pay system. (e) Continuity and transition (1) Continuation of previous system if necessary The Do Not Pay initiative in effect on the day before the date of the enactment of this section shall continue as necessary to support implementation of the Do Not Pay system. (2) Guidance, rules, and procedures Guidance, rules, and procedures in effect before the date of the enactment of this section shall remain in effect until modified by the Secretary or the Director of the Office of Management and Budget. (3) Rules of construction Nothing in this subsection may be construed\u2014 (A) except as specifically provided in subsection (a)(4), to modify or supersede the requirements of section 552a of title 5, including the requirements for notice in section 552a(e)(12) and for due process rights of an individual under section 552a(p); or (B) to limit any authority of an Inspector General under applicable law. .\n##### (b) Technical and conforming amendment\nThe item relating to section 3354 in the table of sections for chapter 33 of title 31, United States Code, is amended, by striking Initiative and inserting Program .\n#### 4. Single report on first time use of funds by recipient\n##### (a) Establishment of post-Award single report requirement on first-Time use of funds by recipient of Federal award\nChapter 61 of title 31, United States Code, is amended by adding at the end the following:\n6107. Single report on first time use of funds by recipient (a) Federal award reporting requirement The head of each agency that administers a covered award shall require each covered recipient to, as a condition of receiving amounts under such award, submit to the head of the agency, not later than 180 days after the receipt of such award unless a deadline exception may be applied pursuant to pursuant to regulations promulgated under subsection (b), a one-time report on the use of such amounts that\u2014 (1) includes any content required to be included in such report pursuant to subsection (b); and (2) is in the format required under such subsection. (b) Governmentwide report regulations and guidance (1) Contents and format of report (A) Promulgation Not later than 1 year after the date of the enactment of this section, the Director, in coordination with the Secretary of the Treasury and the standard-setting agency designated under section 6402(a)(1), shall promulgate regulations, and any clarifying guidance as may be necessary, to establish governmentwide requirements for the content and format of the report described under subsection (a). (B) Updates Any guidance or regulation promulgated under subparagraph (A) shall be updated as necessary, but in any case, shall be updated not less often than once every 5 years. (2) Report minimum requirements The regulations and any clarifying guidance promulgated under paragraph (1), shall at a minimum\u2014 (A) enable the head of an awarding agency to determine whether amounts provided under a covered award are being used by the recipient required to submit the report, and any sub-recipient or sub-grantee thereof, for the intended purpose of the program, as set forth in statute, regulation, or policies and procedures of the agency; (B) enable fraud prevention, detection, investigation, and mitigation, in future awards of Federal funds to the recipient required to submit the report by identifying relevant fraud-risk indicators that would require a referral for investigation and criminal referral to the appropriate entity of the Federal Government, including any identified effort by a recipient to defraud the Federal Government or violate sections 3729 through 3731 of title 31, United States Code (commonly referred to as the False Claims Act ); (C) ensure that any sub-recipient or sub-grantee, at any level, of the recipient required to submit the report provide to such recipient such information as may be necessary to enable aggregate reporting on the covered award by the recipient; (D) require the heads of agencies to apply the governmentwide data standards established under chapter 64 with respect to the format and content of the report required to be submitted; (E) align with the Federal award reporting requirements and data standards under the Federal Funding Accountability and Transparency Act of 2006 ( Public Law 109\u2013282 ; 31 U.S.C. 6101 note), to the maximum extent practicable; (F) reduce recipient and agency reporting burdens by avoiding duplication in recipient reporting obligations, to the extent practicable; and (G) provide clarification for agencies to apply a reporting deadline exception under subsection (a)(1), which may be made for an entire program or type of covered award, beyond 180 days when the use of the covered funds by the covered recipient takes place more than 180 days after a receipt of such covered award. (c) Agency requirements In accordance with the regulations and any clarifying guidance promulgated under subsection (b), the head of an agency that administers a covered award shall\u2014 (1) update the terms and conditions of Federal awards in the agency programs to implement subsection (a) for covered recipients; (2) include a summary of the post-award reporting requirements established under subsection (a), including the required content and reporting format, in the Notice of Funding Opportunity (which has the meaning given the term in section 200.1 of title 2, Code of Federal Regulations) for Federal financial assistance (as defined under section 7501 of this title) in order to assist applicants for such assistance in understanding post-award reporting obligations; (3) to the maximum extent practicable\u2014 (A) provide user-friendly and plain language directives for covered recipients to fulfill their reporting obligation under subsection (a); and (B) use existing post-award reporting requirements to reduce the burden of cumulative post-award reporting; and (4) establish procedures within the agency to identify covered recipients that are not in compliance with the reporting requirement under subsection (a). (d) Noncompliance For a case in which a covered recipient does not submit the report required by subsection (a), the awarding agency shall\u2014 (1) provide a timely written notice of noncompliance to the recipient that\u2014 (A) clearly states the reason for noncompliance; (B) notifies the recipient of the obligation of the agency to cease further disbursements to the entity until the covered recipient is in compliance; and (C) provides clear instructions to the covered recipient on how to come back into compliance; and (2) prevent a payment voucher from being issued under section 3325 for a payment to such recipient, for any program funds, until such report is submitted. (e) Availability of report Each report submitted under subsection (a) shall be\u2014 (1) kept on file by the agency for a period of not less than 5 years after the date on the conclusion of the duration of the award; and (2) made available upon request to\u2014 (A) the Director; (B) the Secretary of the Treasury; (C) the Attorney General; (D) the Inspector General of the agency concerned; and (E) the appropriate congressional committees. (f) Use of information included in report Information included in the report required by subsection (a) shall be used by the agency in support of improper payment activities of the agency under section 3352 as appropriate and applicable. (g) Definitions In this section: (1) Appropriate congressional committees The term appropriate congressional committees means\u2014 (A) the Committees on Appropriations of the Senate and the House of Representatives; (B) the Committee on Homeland Security and Governmental Affairs of the Senate; (C) the Committee on Oversight and Government Reform of the House of Representatives; and (D) any other relevant congressional committee of jurisdiction. (2) Covered award The term covered award means a Federal award (as defined under section 7501) in an amount not less than $50,000 (based on fiscal year 2027 constant dollars). (3) Covered recipient The term covered recipient means any entity, including any State, the District of Columbia, and any territory or possession of the United States, including a pass-through entity (as defined under section 7501), that receives the covered award from a particular agency program for the first time in that program\u2019s existence. (4) Fraud-risk indicator The term fraud-risk indicator means an objective data point or analytic signal that indicates an anomalous payment pattern or increase in the volume of a payment amount, a verified data mismatch, network or behavioral anomaly, or match identified by the Do Not Pay system and any other payment, account, and payee validation program or service provided by the Department of the Treasury that would result in financial loss to the government. .\n##### (b) Clarification of application of first reporting deadline\nThe report required under subsection (a) of section 6107 of title 31, United States Code, as added by subsection (a), shall apply to a covered award made during the fiscal year following the promulgation of regulations or guidance by the Director under subsection (b)(1)(A) of such section.\n#### 5. U.S. treasury data access for purposes of program integrity\n##### (a) Access to the national directory of new hires\nSection 453(j) of the Social Security Act ( 42 U.S.C. 653(j) ) is amended by adding at the end the following:\n(12) Information to assist in the prevention of improper payments (A) In general The Secretary of the Treasury shall have access to the information in the National Directory of New Hires for the sole purpose of detecting, preventing, and recovering improper payments (as defined under section 3351 of title 31, United States Code), including for use in the Do Not Pay system established under section 3354 of title 31, United States Code. (B) Disclosure For the sole purpose of detecting, preventing, and recovering improper payments, the Secretary of the Treasury may disclose information in the National Directory of New Hires to\u2014 (i) agents and contractors of the Secretary of the Treasury; (ii) Federal and non-Federal individuals and entities authorized to receive information in the National Directory of New Hires directly from the Secretary; (iii) entities with access to the Do Not Pay system; and (iv) such additional individuals and entities as agreed to by the Secretary and the Secretary of the Treasury. .\n##### (b) Privacy-Preserving validation of select tax information\n**(1) In general**\nSection 6103(i) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(9) Disclosure of certain return information for use in the do not pay working system (A) In general Upon execution of a written intra agency agreement between the Internal Revenue Service and the office of the Department of the Treasury that operates the Do Not Pay system described in section 3354(c) of title 31, United States Code, the Secretary may disclose to any authorized person described in subparagraph (B) return information described in subparagraph (C) with respect to an individual taxpayer for the applicable period described in subparagraph (D) for the limited purpose described in subparagraph (E). The Secretary may further authorize the redisclosure of such return information by an authorized person described in subparagraph (B), subject to such terms, conditions, and safeguards as the Secretary determines appropriate, to other authorized persons described in subparagraph (B) solely for the limited purpose described in subparagraph (E). The Secretary shall disclose or permit the redisclosure of such return information only to the extent necessary and for the purpose of the Do Not Pay system assisting an authorized person to identify, prevent, and recover improper payments. (B) Authorized person For purposes of this paragraph, the term authorized person means\u2014 (i) an officer, employee, agent, or contractor of the Department of Treasury, whose official duties require access to the Do Not Pay system for the purpose of facilitating the identification, prevention, or recovery of improper payments, or (ii) an officer, employee, or contractor of an entity authorized to access the Do Not Pay system for the purposes described in subparagraph (E). (C) Return information The return information that may be disclosed under this paragraph is limited to\u2014 (i) taxpayer identity information, (ii) filing status, (iii) adjusted gross income, (iv) net profit or loss, as reported on Schedule C of Form 1040 (or successor form), (v) bank account and routing information, (vi) if applicable, the fact that there was no return filed, (vii) the taxable year with respect to which the preceding information relates, and (viii) any reported identity theft related to the taxpayer identification number. (D) Applicable period For purposes of this paragraph, the term applicable period means, with respect to any individual taxpayer, the period\u2014 (i) consisting of the number of taxable years specified in the agreement entered under subparagraph (A), except that such period shall not be fewer than 3 taxable years, and (ii) ending with the most recent taxable year for which the information described in subparagraph (C) is available. (E) Limitation on use of information Information disclosed under this subparagraph shall be solely for the use of the authorized persons to whom such information is disclosed and solely for the purpose of detecting, preventing, and recovering improper payments. .\n**(2) Conforming amendments**\n**(A)**\nSection 6103(a)(3) of the Internal Revenue Code of 1986 is amended by inserting subsection (i)(9), after subsection (e)(1)(D)(iii), .\n**(B)**\nSection 6103(p)(4) of such Code is amended\u2014\n**(i)**\nin the matter preceding subparagraph (A)\u2014\n**(I)**\nby striking or (7), and inserting (7), or (9), ; and\n**(II)**\nby striking or (7)(A)(ii), and inserting (7)(A)(ii), or (9), ;\n**(ii)**\nin subparagraph (F)(i), by inserting or (9) after (i)(3)(B)(i) ; and\n**(iii)**\nin the matter preceding subclause (I) of subparagraph (F)(ii), by striking (5) or (7), and inserting (5), (7), or (9), .\n**(C)**\nSection 7213(a)(2) of such Code is amended by striking or (7)(A)(ii), and inserting (7)(A)(ii), or (9), .\n**(3) Effective date**\nThe amendments made by this subsection shall apply to any disclosure made after the effective date of this Act.\n##### (c) Access to social security information\nTitle II of the Social Security Act ( 42 U.S.C. 401 et seq. ) is amended by adding at the end the following new section:\n235. Disclosure of information for do not pay system (a) The Commissioner of Social Security shall enter into an agreement with the Secretary of the Treasury (or his designee) under which\u2014 (1) the Commissioner establishes a reliable, secure method, which compares the name and social security account number provided in an inquiry against such information maintained by the Commissioner in order to confirm (or not confirm, including the reason for the nonconfirmation) the validity of the information provided; (2) appropriate safeguards are included to assure that the confirmation (or nonconfirmation) is used solely for the use of the authorized persons to whom such information is disclosed and solely for the purpose of using the Do No Pay system to identify, prevent, and recover improper payments, and any redisclosure shall be subject to the provisions of section 3354 of title 31, United States Code; and (3) the Secretary shall pay the Commissioner of Social Security the full costs (including systems and administrative costs) of providing the confirmation described in paragraph (1). (b) For purposes of this paragraph the term authorized person means\u2014 (1) an officer, employee, contractor, or agent of the Department of Treasury, whose official duties require access to the Do Not Pay system, or (2) an officer, employee, or contractor of another Federal agency, or a State agency that manages Federally funded State-administered programs, whose official duties require access to the Do Not Pay system. .\n#### 6. Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2026-04-23",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-05-18T15:24:10Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-18T15:23:59Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-05-18T15:23:35Z"
          },
          {
            "name": "Department of the Treasury",
            "updateDate": "2026-05-18T15:23:50Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-05-18T15:23:12Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-18T15:23:55Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-05-18T15:23:44Z"
          },
          {
            "name": "Office of Management and Budget (OMB)",
            "updateDate": "2026-05-18T15:24:05Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2026-05-18T15:24:23Z"
          },
          {
            "name": "Social security and elderly assistance",
            "updateDate": "2026-05-18T15:24:32Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-05-18T15:23:40Z"
          },
          {
            "name": "Tax administration and collection, taxpayers",
            "updateDate": "2026-05-18T15:24:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-07T02:45:06Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8463ih.xml"
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
      "title": "Pre-Payment Fraud Prevention and Treasury Data Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T06:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pre-Payment Fraud Prevention and Treasury Data Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T06:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish governmentwide requirements for pre-payment fraud prevention actions, to provide the U.S. Treasury appropriate data resources, to facilitate participation in governmentwide anti-fraud data sharing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T06:03:37Z"
    }
  ]
}
```
