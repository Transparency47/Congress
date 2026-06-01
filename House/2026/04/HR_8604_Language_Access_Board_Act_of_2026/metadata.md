# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8604?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8604
- Title: Language Access Board Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8604
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-27T15:05:42Z
- Update date including text: 2026-05-27T15:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8604",
    "number": "8604",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001080",
        "district": "28",
        "firstName": "Judy",
        "fullName": "Rep. Chu, Judy [D-CA-28]",
        "lastName": "Chu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Language Access Board Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-27T15:05:42Z",
    "updateDateIncludingText": "2026-05-27T15:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:03:10Z",
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
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "DC"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MI"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "TX"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "FL"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "CA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8604ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8604\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Ms. Chu (for herself, Ms. Meng , Mr. Vargas , Mr. Goldman of New York , Ms. Wilson of Florida , Ms. Norton , Mr. Lieu , Ms. Tlaib , Mr. Green of Texas , Mr. Soto , Mr. Kennedy of New York , and Mr. Correa ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo establish the Language Access Board, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Language Access Board Act of 2026 .\n#### 2. Language Access Board\n##### (a) Board established\nThere is established within the Federal Government the Language Access Board (referred to in this Act as the Board ) which shall be composed of 32 members as follows:\n**(1)**\n16 members shall be appointed by the President, in accordance with the appointment requirements under subsection (b), from among members of the public who are not Federal employees, and one whom has been appointed under subparagraph (A) of section 502 of the Rehabilitation Act of 1973 ( 29 U.S.C. 792 ) to serve as a public member of the Access Board established under such section 502, and each of whom have expertise in\u2014\n**(A)**\ndeveloping or implementing policies or programs related to language access issues;\n**(B)**\nworking with individuals with limited English proficiency; or\n**(C)**\ntranslation or interpretation services.\n**(2)**\nThe remaining 16 members shall be the heads of each of the following departments, agencies, or bureaus (or their designees whose positions are executive level IV or higher):\n**(A)**\nDepartment of Health and Human Services.\n**(B)**\nDepartment of Transportation.\n**(C)**\nDepartment of Housing and Urban Development.\n**(D)**\nDepartment of Labor.\n**(E)**\nDepartment of the Interior.\n**(F)**\nDepartment of Agriculture.\n**(G)**\nDepartment of Justice.\n**(H)**\nDepartment of Veterans Affairs.\n**(I)**\nDepartment of Homeland Security.\n**(J)**\nDepartment of Education.\n**(K)**\nDepartment of Commerce.\n**(L)**\nInternal Revenue Service.\n**(M)**\nOffice of Management and Budget.\n**(N)**\nSmall Business Administration.\n**(O)**\nSocial Security Administration.\n**(P)**\nDepartment of the Treasury.\n##### (b) Appointment requirements\nMembers described in subsection (a)(1) shall be appointed solely on the basis of their professional qualifications, achievements, public stature, and relevant expertise and experience, and without regard to political affiliation, but in no event shall more than 8 such members be members of the same political party.\n##### (c) Duties\nThe duties of the Board shall be to\u2014\n**(1)**\nenforce, issue requirements for, and investigate violations of standards under, or prescribed pursuant to, language access guidelines required in section 4(a), as applicable;\n**(2)**\nestablish, maintain, and provide technical assistance and training on\u2014\n**(A)**\nlanguage access standards for public-facing resources or materials for federally conducted programs or initiatives issued pursuant to section 4; and\n**(B)**\nlanguage access provisions of law identified in the review required under section 3(b);\n**(3)**\ndevelop advisory information for, and provide appropriate technical assistance to, Federal departments and agencies, including\u2014\n**(A)**\na duty to provide services for individuals with limited English proficiency; or\n**(B)**\na duty to provide multilingual or non-English resources, programs, or materials to individuals with limited English proficiency;\n**(4)**\nstudy practices and approaches that help individuals with limited English proficiency access Federal resources and programs;\n**(5)**\nhelp connect individuals with limited English proficiency with Federal resources and programs; and\n**(6)**\npromote language access for individuals with limited English proficiency throughout all segments of society.\n##### (d) Term of office\n**(1) In general**\nEach member described in subsection (a)(1) shall be appointed for a term of 5 years, except as provided in paragraph 2.\n**(2) Terms of initial appointees**\nAs designated by the President at the time of appointment, of the members described in subsection (a)(1) first appointed\u2014\n**(A)**\n6 shall be appointed for a term of 5 years;\n**(B)**\n5 shall be appointed for a term of 4 years; and\n**(C)**\n5 shall be appointed for a term of 3 years.\n##### (e) Chairperson; vice-Chairperson\nThe chairperson and vice-chairperson of the Board shall be subject to the following requirements:\n**(1)**\nThe chairperson and vice-chairperson of the Board shall each be elected by majority vote of the members of the Board.\n**(2)**\nThe chairperson and vice-chairperson of the Board shall each serve for a term of 1 year.\n**(3)**\nThe chairperson elected by the Board shall alternate, on a term-by-term basis, between being a member described in subsection (a)(1) or a member described in subsection (a)(2).\n**(4)**\nThe chairperson and vice-chairperson of the Board may not both be members described in subsection (a)(1) or both be members described in subsection (a)(2).\n**(5)**\nThe chairperson and vice-chairperson may not be members of the same political party.\n##### (f) Vacancies\n**(1) In general**\nA member described in subsection (a)(1) appointed to fill a vacancy shall serve for the remainder of the term to which that member\u2019s predecessor was appointed.\n**(2) Change in status**\nIf any member described in subsection (a)(1) becomes a Federal employee or employee of a contractor of a Federal department or agency, such member may continue as a member of the Board for not longer than the 60-day period beginning on the date the member becomes such an employee.\n##### (g) Reappointment\nNo member described in subsection (a)(1) may be reappointed to the Board more than once unless such individual has not served on the Board for a period of 30 months prior to the effective date of such individual\u2019s appointment.\n##### (h) Basic pay\n**(1) Appointed members**\nMembers described in subsection (a)(1) shall be entitled to receive compensation at rates fixed by the President, but not to exceed the daily equivalent of the annual rate of basic pay for level IV of the Executive Schedule under section 5315 of title 5, United States Code, including travel time, for each day (including travel time) during which they are engaged in the actual performance of their duties as members of the Board.\n**(2) Prohibition on compensation of Federal employees**\nMembers described in subsection (a)(2) shall serve without compensation.\n##### (i) Travel expenses\nEach member shall receive travel expenses, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter I of chapter 57 of title 5, United States Code.\n##### (j) Bylaws\n**(1) In general**\nThe Board shall establish such bylaws and other rules as may be appropriate to enable the Board to carry out its functions under this Act.\n**(2) Quorum**\nThe bylaws described in paragraph (1) shall include quorum requirements that meet the following requirements:\n**(A)**\nA proxy may not be counted for purposes of establishing a quorum.\n**(B)**\nNot less than half the members required for a quorum shall be members described under subsection (a)(1).\n##### (k) Staff\n**(1) In general**\nThe heads of each department and agency described in subsection (a)(2) shall make available to the Board such technical, administrative, or other assistance as it may require to carry out its functions under this section, and the Board may hire such other advisers, technical experts, and consultants as it deems necessary to assist it in carrying out its functions under this section. Special advisory and technical experts and consultants hired pursuant to this paragraph shall, while performing their functions under this section, be entitled to receive compensation at rates fixed by the Chairperson, but not exceeding the daily equivalent of the rate of pay for level 4 of the Senior Executive Service Schedule under section 5382 of title 5, United States Code, including travel time, and while serving away from their homes or regular places of business they may be allowed travel expenses, including per diem in lieu of subsistence, as authorized by section 5703 of such title for persons in the Government service employed intermittently.\n**(2) Required staff**\nThe Board shall hire an Executive Director, hearing examiners, and such other professional and clerical personnel as are necessary to carry out its functions under this Act.\n**(3) Role of Executive Director**\nThe Executive Director shall exercise general supervision over all personnel employed by the Board (other than hearing examiners and their assistants). The Executive Director shall have final authority on behalf of the Board, with respect to the investigation of alleged noncompliance and in the issuance of formal complaints before the Board, and shall have such other duties as the Board may prescribe.\n**(4) Role of hearing examiners**\nThe Board is authorized to appoint as many hearing examiners as are necessary for proceedings required to be conducted under this section. The provisions applicable to hearing examiners appointed under section 3105 of title 5, United States Code, shall apply to hearing examiners appointed under this subsection. An order of compliance issued by a hearing examiner shall be deemed to be an order of the Board.\n##### (l) Powers of Board\n**(1) In general**\nThe Board shall conduct investigations, hold public hearings, and issue orders of compliance in accordance with the requirements under this section as the Board deems necessary to carry out its responsibilities under this section.\n**(2) Orders of compliance**\n**(A) In general**\nThe provisions of subchapter II of chapter 5, and chapter 7 of title 5, United States Code, shall apply to procedures under this subsection, and an order of compliance issued by the Board in accordance with subparagraph (B) shall be a final order for purposes of judicial review. Any such order affecting any Federal department, agency, or instrumentality of the United States shall be final and binding on such department, agency, or instrumentality. Pursuant to chapter 7 of title 5, United States Code, any complainant or participant in a proceeding under this subsection may obtain review of a final order issued in such proceeding.\n**(B) Approval process**\n**(i) In general**\nBefore the Board issues an order of compliance, the Board shall submit such order to the Director of the Office of Management and Budget for review. The Board may not issue an order of compliance that has not been approved by the Director.\n**(ii) Deadline**\nNot later than 14 days after receiving an order of compliance from the Board for review under clause (i), the Director of the Office of Management and Budget shall approve or suggest a modification to such order. In the case that the Director does not act to approve or suggest a modification to such order before the expiration of such period, such inaction shall be deemed to be an approval of such order by the Director. In the event that the Director suggests a modification of the order, the Board may review and revise such modifications and shall resubmit the order to the Director for review within 30 days.\n**(C) Assistance**\nThe Board or the Director of the Office of Management and Budget may request the Inspector General of a Federal department or agency subject to an order of compliance issued by the Board (or an equivalent official, as applicable) to assist with investigating, monitoring, or enforcing such Federal department or agency\u2019s compliance with such order of compliance.\n**(3) Powers of Executive Director**\n**(A) In general**\nThe Executive Director is authorized, at the direction of the Board\u2014\n**(i)**\nin accordance with subparagraph (B), to bring a civil action in any appropriate United States district court to enforce, in whole or in part, any final order of the Board under this section;\n**(ii)**\nto appear as amicus curiae, in any court of the United States or in any court of a State in civil actions that relate to this section; and\n**(iii)**\nexcept as provided in section 518(a) of title 28, United States Code (relating to litigation before the Supreme Court), to appear for and represent the Board in any civil litigation brought under this section.\n**(B) Approval process**\n**(i) In general**\nBefore the Executive Director may bring a civil action under subparagraph (A)(i), the Executive Director shall submit the applicable complaint to the Director of the Office of Management and Budget for review. The Executive Director may not file such complaint and bring such civil action without approval by the Director of the Office of Management and Budget.\n**(ii) Deadline**\nNot later than 14 days after receiving a complaint described in subparagraph (A) from the Executive Director for review under clause (i), the Director of the Office of Management and Budget shall approve of filing or suggest a modification to the complaint. In the case that the Director of the Office of Management and Budget does not act to approve, or suggest a modification to, such complaint before the expiration of such period, such inaction shall be deemed to be an approval to file such complaint by the Director of the Office of Management and Budget. In the event that the Director suggests a modification of the complaint the Board may review and revise such modification and shall resubmit the complaint to the Director for review within 30 days.\n##### (m) Contract authority\nThe Board may make grants to, or enter into contracts with, public or private organizations to carry out its duties under subsection (c).\n##### (n) Gifts, Bequests, and Devises\n**(1) In general**\nThe Board may accept, hold, administer, and utilize gifts, devises, and bequests of property, both real and personal, for the purpose of aiding and facilitating the functions of the Board under subsection (c). Gifts and bequests of money and proceeds from sales of other property received as gifts, devises, or bequests shall be deposited in the Treasury and shall be disbursed upon the order of the Chairperson. Property accepted pursuant to this section, and the proceeds thereof, shall be used as nearly as possible in accordance with the terms of the gifts, devises, or bequests. For purposes of Federal income, estate, or gift taxes, property accepted under this section shall be considered as a gift, devise, or bequest to the United States.\n**(2) Regulations**\nThe Board shall publish regulations setting forth the criteria the Board will use in determining whether the acceptance of gifts, devises, and bequests of property, both real and personal, would reflect unfavorably upon the ability of the Board or any employee to carry out the responsibilities or official duties of the Board in a fair and objective manner, or would compromise the integrity of or the appearance of the integrity of a Government program or any official involved in that program.\n##### (o) Report\nNot later than 4 years after the date of enactment of this Act, and every 2 years thereafter, the Board shall submit to Congress and the President, and publish on a publicly accessible website, a report that includes\u2014\n**(1)**\ninformation and recommendations regarding\u2014\n**(A)**\nthe extent to which public-facing resources and materials for federally conducted programs and initiatives are accessible to individuals with limited English proficiency, including any adjustments made to improve such access since the last report was submitted under this subsection; and\n**(B)**\nthe state of compliance with the language access standards issued pursuant to section 4 and language access provisions of law;\n**(2)**\na description and analysis of any investigations made (other than investigations made pursuant to a complaint filed under section 4(d)), and actions taken pursuant to such investigations, by the Board since the last report was submitted under this subsection as applicable; and\n**(3)**\na description and analysis of any complaints filed under section 4(d) with the Board, including the number of complaints, the topics of such complaints, the current status or resolution of such complaints, and actions taken pursuant to such complaints (including any investigations), since the last report was submitted under this subsection as applicable.\n#### 3. Review of language access provisions of law\n##### (a) Study\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, the Board shall complete a study of\u2014\n**(A)**\nlanguage access requirements, including statutory provisions, regulatory provisions, and Executive orders, that Federal departments and agencies must follow, including any adjustments that have been made to such language access requirements over time;\n**(B)**\nbarriers that prevent individuals with limited English proficiency from connecting with, accessing, participating in, or receiving outreach related to Federal programs and initiatives, including measures to reduce such barriers;\n**(C)**\nthe effect that failures to provide accessible services has on individuals with limited English proficiency, including\u2014\n**(i)**\nany costs borne by such individuals and the Federal Government as a result of such failures;\n**(ii)**\nreduced use of services by such individuals; and\n**(iii)**\nsevere or adverse risks of critical delays in receiving such services;\n**(D)**\nFederal department and agency standards and best practices regarding the qualifications and usage of interpreters and translators, including the use of machine translation and artificial intelligence, in translating resources or materials for federally conducted programs or initiatives; and\n**(E)**\nthe effect that failing to translate resources or materials for federally conducted programs or initiatives, including inaccurate or incomplete translation of such resources or materials, has on the ability of Federal departments and agencies to carry out their responsibilities.\n**(2) Results**\nNot later than 2 years after the date of enactment of this Act, the Board shall\u2014\n**(A)**\nsubmit the results of the study required under paragraph (1) to Congress and the President; and\n**(B)**\npublish such results on a publicly accessible website.\n##### (b) Review\nNot later than 2 years after the date of enactment of this Act, the Board shall conduct a review of language access provisions of law and publish such results on a publicly accessible website.\n#### 4. Language access requirements and standards for program materials\n##### (a) Federal departments and agencies\n**(1) Requirements**\n**(A) In general**\nWhen developing public-facing resources or materials for programs or initiatives (including vital documents and websites), each Federal department or agency shall ensure, unless an undue burden would be imposed on the Federal department or agency, that such resources or materials are accessible to individuals with limited English proficiency in a format and manner that is comparable to the accessibility of such resources or materials to members of the public who are not individuals with limited English proficiency.\n**(B) Alternative means efforts**\nIn accordance with paragraph (4), when the development of public-facing resources or materials for programs or initiatives in accordance with the standards published by the Board under paragraph (2) would impose an undue burden, the Federal department or agency shall provide individuals with limited English proficiency covered by this paragraph with such resources or materials in a format and manner that allows such individuals to access such resources or materials.\n**(2) Standards**\n**(A) Initial standards**\n**(i) In general**\nNot later than 2 years after the date of enactment of this Act and in accordance with the requirements under subparagraph (C), the Board, after consultation with the heads of any Federal departments or agencies that the Board determines to be appropriate (including about relevant research findings) and consultation with appropriate public or nonprofit agencies or organizations, including organizations representing individuals with limited English proficiency, shall issue and publish in the Federal Register, standards setting forth the language access criteria necessary to implement the requirements set forth in paragraph (1).\n**(ii) Public comment period**\nThe Board shall publish such standards in the Federal Register for a 60-day public comment period to ensure that stakeholders, including individuals with limited English proficiency and organizations representing such individuals, have an adequate opportunity to provide input on these standards. Not later than 30 days after such 60-day public comment period, the Board shall review and consider all timely submitted comments and may revise the standards as appropriate before submitting such standards to the Director for review pursuant to subparagraph (C).\n**(B) Review and amendment**\nIn accordance with the requirements under subparagraph (C), beginning not later than 5 years after the date of enactment of this Act, and every 5 years thereafter, the Board shall review and, as appropriate, amend such standards published in subparagraph (A) to reflect\u2014\n**(i)**\ntechnological advances or changes in electronic and information technology;\n**(ii)**\nchanges in Federal department and agency programs and initiatives;\n**(iii)**\nchanges in the demographic data of individuals with limited English proficiency and of the communities such individuals belong to; and\n**(iv)**\nchanges in the language access needs of such individuals and communities.\n**(C) Approval process**\n**(i) In general**\nBefore the Board issues or amends the standards in accordance with subparagraph (A) or (B), the Board shall submit such standards to the Director of the Office of Management and Budget for review. The Board may not issue or amend such standards without approval by the Director.\n**(ii) Deadlines**\n**(I) In general**\nNot later than 30 days after receiving the standards (including amendments to such standards) from the Board for review under clause (i), the Director of the Office of Management and Budget shall approve or suggest a modification to such standards. In the case that the Director does not act to approve, or suggest a modification to, such standards before the expiration of such period, such inaction shall be deemed to be an approval of such standards by the Director.\n**(II) Submission of revised standards**\nIn the event that the Director suggests a modification of the standards, not later than 30 days after receiving such modification, the Board may review and revise such modification, and submit to the Director revised standards that incorporate such revised modification.\n**(3) Incorporation of standards**\n**(A) In general**\nNot later than 6 months after the Board publishes the standards required under paragraph (2), each Federal department or agency shall revise their language access policies and directives to incorporate those standards.\n**(B) Revision**\nNot later than 6 months after the Board revises any standards required under paragraph (2), each appropriate Federal department or agency shall revise their language access policies and directives, as necessary, to incorporate the revisions.\n**(4) Undue burden**\n**(A) Request for waiver**\nIn the event that a Federal department or agency determines that compliance with a standard issued by the Board under paragraph (2) imposes an undue burden related to a specific program, initiative, or other activity of the Federal department or agency, such Federal department or agency may request a waiver for compliance with such standard and provide the Board with documentation explaining why such compliance would create an undue burden, which shall\u2014\n**(i)**\nidentify the standard creating the undue burden;\n**(ii)**\ndescribe the nature of the undue burden; and\n**(iii)**\neither\u2014\n**(I)**\npropose an alternative standard to apply; or\n**(II)**\nexplain why applying an alternative standard is not feasible.\n**(B) Review**\n**(i) In general**\nNot later than 30 days after receiving a waiver request described in subparagraph (A), the Board shall\u2014\n**(I)**\ngrant or deny the waiver request in accordance with clause (ii); or\n**(II)**\nrequest the Federal department or agency that submitted the waiver request to provide further information by not later than 30 days after receiving such request for further information.\n**(ii) Criteria**\nIn determining whether to grant or deny a waiver request described in subparagraph (A), the Board shall consider\u2014\n**(I)**\nwhether an individual with limited English proficiency is likely to interact with the Federal department or agency that submitted the waiver request, including an analysis of the number or proportion of such individuals served by such Federal department or agency and the frequency of contact with such department or agency by such individuals;\n**(II)**\nwhether a failure to comply with the applicable standard is likely to result in significant harm, including a denial of benefits or diminished civil rights protections;\n**(III)**\nthe costs borne by such Federal department or agency due to compliance with the applicable standard, including the resources available to the Federal department or agency; and\n**(IV)**\nwhether an alternative standard can be applied that would avoid causing such significant harm.\n**(iii) Duration**\nA waiver granted under this subparagraph shall be for a period of not more than 2 years.\n**(iv) Record**\nThe Board shall maintain a publicly accessible record of all waiver requests described in subparagraph (A).\n**(C) Requirement**\nThe Board shall ensure that a waiver granted under subparagraph (B) does not\u2014\n**(i)**\nresult in the denial of meaningful access to a federally conducted program or initiative; or\n**(ii)**\nrelieve a Federal department or agency of the obligation to take reasonable steps to provide language assistance services.\n##### (b) Technical Assistance\nThe Board shall provide technical assistance to individuals and Federal departments and agencies concerning the requirements under this section.\n##### (c) Evaluations\n**(1) In general**\nNot later than 18 months after the date of enactment of this Act, and every 2 years thereafter, the head of each Federal department or agency shall, in accordance with paragraph (2)\u2014\n**(A)**\nevaluate the extent to which the public-facing resources and materials for programs and initiatives of the department or agency are accessible to individuals with limited English proficiency described in subsection (a)(1), compared to the access to the resources and materials by individuals described in such subsection who are not individuals with limited English proficiency;\n**(B)**\nsubmit a report containing the evaluation to Congress, the President, and the Board; and\n**(C)**\nnot later than 60 days after completing such evaluation, take appropriate steps, based on such evaluation, to update, modify, or amend the programs, initiatives, and public-facing resources and materials of the department or agency to improve accessibility for individuals with limited English proficiency, consistent with the most recent applicable standards issued by the Board.\n**(2) Requirements**\nAn evaluation described in paragraph (1) shall take into account the following:\n**(A)**\nLanguage access compliance measures.\n**(B)**\nQuality assurance standards.\n**(C)**\nFederal program and initiative participant outcomes.\n**(D)**\nThe use of qualified or certified interpreters and translators.\n**(E)**\nTraining requirements for staff and contractors.\n**(F)**\nStakeholder feedback.\n**(G)**\nThe impact of failing to provide accessible programs and initiatives.\n**(H)**\nAny other standards, activities, or information related to programs or initiatives of the Federal department or agency, as determined relevant by the department or agency.\n##### (d) Complaints\n**(1) In general**\n**(A) Process**\nEffective 6 months after the date of publication by the Board of final standards described in subsection (a)(2), any individual with limited English proficiency (or an organization acting on behalf of such an individual) may file a complaint with the Board alleging that a Federal department or agency fails to comply with the requirements under subsection (a)(1).\n**(B) Application**\nThis subsection shall apply only to public-facing resources or materials for programs or initiatives of a Federal department or agency that are produced by a Federal department or agency not less than 6 months after the date of publication by the Board of final standards described in subsection (a)(2).\n**(C) Complaints submitted to the Board**\nIn the case that the Board determines that a complaint filed with the Board is outside the jurisdiction of the Board, the Board shall notify the individual who filed such complaint of such determination and refer the individual to the appropriate entity to investigate such complaint as applicable.\n**(D) Complaints submitted to Federal department or agency**\nIn the case that a Federal department or agency receives a complaint that falls under the jurisdiction of the Board, the Federal department or agency shall forward such complaint to the Board and consult with the Board regarding how such complaint should be investigated.\n**(E) Confidentiality**\nAny information provided by an individual under this subsection, including personally identifying information, shall only be utilized for the purposes of, and to the extent necessary in, ensuring the efficient investigation of their complaint. Any person or agency receiving information from the Board shall use it only for the purposes of ensuring efficient investigation of the complaint.\n**(2) Corrective action plan**\n**(A) In general**\nIn the case that the Board investigates a complaint and determines that the Federal department or agency implicated in the complaint is not in compliance with the requirements under subsection (a)(1), the Board shall collaborate with the Federal department or agency to develop a corrective action plan, which shall include\u2014\n**(i)**\nif determined appropriate by the Board, a joint investigation by the Board and the Federal department or agency of the language access requirements and procedures of such department or agency;\n**(ii)**\nsteps for the Federal department or agency to take in order to make progress on satisfying such requirements; and\n**(iii)**\na timeline for achieving compliance with such requirements.\n**(B) Approval process**\n**(i) In general**\nBefore a corrective action plan developed pursuant to subparagraph (A) may be entered into by the Board, the Board shall submit such corrective action plan to the Director of the Office of Management and Budget for review. The Board may not enter into such corrective action plan without approval by the Director.\n**(ii) Deadlines**\n**(I) In general**\nNot later than 14 days after receiving a corrective action plan described in subparagraph (A) from the Board for review under clause (i), the Director of the Office of Management and Budget shall approve or suggest a modification to such corrective action plan. In the case that the Director does not act to approve, or suggest a modification to, such corrective action plan before the expiration of such period, such inaction shall be deemed to be an approval of such corrective action plan by the Director.\n**(II) Submission of revised corrective plan**\nIn the event that the Director suggests a modification of the corrective plan, not later than 30 days after receiving such modification, Board may review and revise such modification, and submit to the Director a revised corrective plan that incorporates such revised modification.\n**(C) Monitoring**\nThe Board shall monitor the progress of a Federal department or agency that implements a corrective action plan described in paragraph (A).\n**(D) Notice**\nIn the case that a corrective action plan is developed under subparagraph (A) due to a complaint received pursuant to paragraph (1)(A), not later than 60 days after such plan is completed, the Board shall notify the individual who submitted such complaint in writing of whether the Federal department or agency is now in compliance with the requirements under subsection (a)(1) and of any additional steps the Board plans to take regarding the complaint.\n**(E) Record**\nThe Board shall maintain a publicly accessible record of all corrective action plans described in subparagraph (A).\n**(3) Application to other Federal laws**\nThis subsection shall not be construed to limit any right, remedy, or procedure otherwise available under any provision of Federal law (including under title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. )) that provides protection for the rights of individuals with limited English proficiency, including the ability to file a complaint pertaining to language access with an entity other than the Board.\n#### 5. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given that term in section 551 of title 5, United States Code.\n**(2) Federally conducted program or initiative**\n**(A) In general**\nThe term federally conducted program or initiative means any program, activity, or operation that is directly administered by a Federal agency including through its officers, employees, or contractors acting on its behalf, in which the Federal agency exercises day-to-day operational control over program implementation, and that involves contact with the public, the administration of Federal benefits, or communication with members of the public or program participants.\n**(B) Exclusions**\nThe term federally conducted program or initiative does not include programs or activities that are administered by a non-Federal entity, including a State, local, Tribal, or territorial government, or a private entity, even if funded in part by the Federal Government but administered by non-Federal entities, unless the Federal Government exercises day-to-day direct operational control (except that for purposes of this paragraph Federal funding, rulemaking, approval of plans or applications, or regulatory oversight shall not, standing alone, constitute day-to-day operational control).\n**(3) Individual with limited English proficiency**\nThe term individual with limited English proficiency means an individual who\u2014\n**(A)**\nuses a primary language other than English; and\n**(B)**\nhas a limited ability to read, speak, write, or understand English.\n**(4) Language access**\nThe term language access means the ability of individuals with limited English proficiency to meaningfully access and participate in programs, initiatives, services, and activities, including the ability for such individuals to engage in equitable and effective communication regarding such programs, initiatives, services, and activities through interpretation, translation, and other language assistance services.\n**(5) Language access provision of law**\nThe term language access provision of law means any provision of a Federal statute, regulation, or Executive order, or a policy established by a Federal department or agency to carry out or comply with such a provision, that requires a Federal department or agency to provide or ensure access to a federally conducted program or initiative by individuals with limited English proficiency and includes, with respect to a Federal department or agency, a legal obligation (including a requirement established by Federal statute, regulation, or Executive order)\u2014\n**(A)**\nto provide language assistance or remove language barriers in a specific programmatic context, including in education, voting, health care, housing, taxation, emergency response, nutrition assistance, and the administration of justice;\n**(B)**\nto ensure language access, including through establishing standards for meaningful access to a federally conducted program or initiative;\n**(C)**\nrelated to the translation of public-facing resources or materials for the programs or initiatives of the Federal department or agency, including vital documents and websites;\n**(D)**\nrelated to the development and implementation of a language access plan, including an obligation to update such a plan;\n**(E)**\nrelated to the quality, accuracy, and confidentiality of interpretation and translation services, including the use of qualified personnel and artificial intelligence;\n**(F)**\nto train staff and relevant personnel on language access obligations and procedures;\n**(G)**\nrelated to the collection and analysis of data to assess language access needs and evaluate the effectiveness of language access services; or\n**(H)**\nrelated to monitoring, compliance, and accountability mechanisms designed to ensure adherence to language access requirements.\n**(6) Language assistance services**\nThe term language assistance services means oral and written services used to assist individuals with limited English proficiency meaningful access to, and an equal opportunity to participate fully in, the services, activities, and other programs administered by the Federal Government.\n**(7) Meaningful access**\nThe term meaningful access means access that\u2014\n**(A)**\nresults in accurate, timely, and effective communication at no cost to the individual with limited English proficiency; and\n**(B)**\nis comparable to the access provided to individuals who are proficient in English.\n**(8) Public-facing resources or materials**\n**(A) In general**\nThe term public-facing resources or materials means any information, communication, or service produced or provided by a Federal agency or department that is intended for routine access or use by the general public to obtain general information about, or assistance in accessing, Federal programs, benefits, or services. Such term includes\u2014\n**(i)**\nwritten or printed materials commonly required to be completed by members of the public, including forms, applications, and notices;\n**(ii)**\ndigital or online content designed for general public use, including primary public websites and commonly accessed web pages; and\n**(iii)**\npublic-facing service channels through which individuals may obtain general information or assistance, including telephone hotlines, call centers, and in-person or virtual assistance services.\n**(B) Exclusions**\nThe term public-facing resources or materials does not include\u2014\n**(i)**\ntechnical, scientific, legal, or policy materials primarily intended for specialized or expert audiences; or\n**(ii)**\nmaterials that are not routinely accessed by or necessary for a reasonable member of the general public to obtain information or services from a Federal agency or department.\n**(9) Vital document**\nThe term vital document means any physical or digital material\u2014\n**(A)**\nrequired to be submitted by an individual before such individual may obtain any aid, benefit, service, or training provided under a federally conducted program or initiative, including an application related to such a program or initiative;\n**(B)**\nrequired to be provided by Federal law, including a notice of rights and responsibilities; or\n**(C)**\ncontaining information critical for fully participating in or understanding a federally conducted program or initiative, including\u2014\n**(i)**\na letter or notice that requires a response from a beneficiary, applicant, participant, or employee;\n**(ii)**\na consent form; or\n**(iii)**\na complaint form.",
      "versionDate": "2026-04-30",
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
        "updateDate": "2026-05-27T15:05:41Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8604ih.xml"
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
      "title": "Language Access Board Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T12:53:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Language Access Board Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Language Access Board, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T12:48:44Z"
    }
  ]
}
```
