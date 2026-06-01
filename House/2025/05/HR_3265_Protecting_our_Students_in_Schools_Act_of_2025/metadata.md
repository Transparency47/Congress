# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3265?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3265
- Title: Protecting our Students in Schools Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3265
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-08 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-08 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3265",
    "number": "3265",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Protecting our Students in Schools Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-08T13:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "GA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "WI"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "ME"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "VA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "IL"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "FL"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "VA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "FL"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CT"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MA"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CT"
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
      "sponsorshipDate": "2025-05-08",
      "state": "MA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "PA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "WI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NJ"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "WA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "HI"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3265ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3265\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Ms. Bonamici (for herself, Mrs. McBath , Ms. Moore of Wisconsin , Ms. Pingree , Mr. Beyer , Mr. Davis of Illinois , Mr. Takano , Mr. Soto , Ms. McClellan , Mrs. Cherfilus-McCormick , Mr. DeSaulnier , Mrs. Hayes , Mr. Keating , Mr. Courtney , Mr. Lynch , Ms. Scanlon , Mr. Pocan , Mrs. Watson Coleman , Ms. Jayapal , and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the use of corporal punishment in schools, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Protecting our Students in Schools Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act are as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Purposes.\nSec. 3. Definitions.\nTitle I\u2014Prohibition of Corporal Punishment\nSec. 101. Prohibition of corporal punishment.\nSec. 102. Civil actions by the Attorney General.\nSec. 103. Enforcement by the Office for Civil Rights.\nSec. 104. Parent notification and protection and advocacy systems.\nTitle II\u2014State Activities and Grant Program\nSec. 201. State plan and enforcement.\nSec. 202. Grant authority.\nTitle III\u2014Additional Provisions\nSec. 301. Federal regulations.\nSec. 302. Other schools.\nSec. 303. Limitation of authority.\nSec. 304. Applicability to private schools and home schools.\nSec. 305. Severability.\nSec. 306. Authorization of appropriations.\n#### 2. Purposes\nThe purposes of this Act are to\u2014\n**(1)**\neliminate the use of corporal punishment in schools;\n**(2)**\nensure, regardless of sexual orientation, gender identity or expression, sex, race, color, national origin, disability, or religion, the health and safety of all students and program personnel in schools and promote a positive school climate and culture;\n**(3)**\nassist States, local educational agencies, and schools in improving school climate and culture by implementing positive behavioral interventions and supports, and other models (including models such as restorative justice interventions, trauma-informed care, multi-tiered system of supports, crisis and de-escalation interventions, implicit bias training, and culturally responsive teaching), to address student behavior and work to eliminate the use of exclusionary and aversive discipline practices or interventions;\n**(4)**\nensure all program personnel have the supports and training necessary to implement positive behavioral interventions and supports and other models to address student behavior and improve school climate and culture; and\n**(5)**\ncollect and analyze data on exclusionary and aversive discipline practices or interventions in schools.\n#### 3. Definitions\nIn this Act:\n**(1) Corporal punishment**\nThe term corporal punishment means, with respect to a student, a deliberate act which causes the student to feel physical pain for the purpose of discipline, including an act of physical force, such as striking, spanking, or paddling, inflicted on a student\u2019s body, requiring a student to assume a painful physical position, or the use of chemical sprays, electroshock weapons, or stun guns on a student\u2019s body.\n**(2) ESEA terms**\nThe terms elementary school , evidence-based , local educational agency , outlying area , parent , secondary school , Secretary , State , and State educational agency have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(3) Exclusionary discipline**\nThe term exclusionary discipline means any type of disciplinary action that removes or excludes a student from the student\u2019s usual educational setting, or from access to education services, including such disciplinary actions as in-school suspensions, out-of-school suspensions, expulsions, or any other removal, however labeled, that results in lost instructional time for the student.\n**(4) Model**\nThe term model means an activity, strategy, framework, or intervention that is evidence-based, to the extent practicable.\n**(5) Positive behavioral interventions and supports**\nThe term positive behavioral interventions and supports \u2014\n**(A)**\nmeans a schoolwide, systematic approach that embeds evidence-based practices and data-driven decision making to improve school climate and culture in order to achieve improved academic and social outcomes and increase learning for all students (including students with the most complex and intensive behavioral needs); and\n**(B)**\nencompasses a range of systemic and individualized positive strategies to teach and reinforce school-expected behaviors, while discouraging and diminishing undesirable behaviors.\n**(6) Program**\nThe term program means\u2014\n**(A)**\nall of the operations of a local educational agency, system of vocational education, or other school system;\n**(B)**\na program that serves children who receive services for which financial assistance is provided in accordance with the Head Start Act ( 42 U.S.C. 9831 et seq. ); or\n**(C)**\nan elementary school or secondary school that is not a public school that enrolls a student who receives special education and related services under the Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ).\n**(7) Program personnel**\n**(A) In General**\nSubject to subparagraph (B), the term program personnel means any agent of a program, including an individual who is employed by a program, or who performs services for a program on a contractual basis, including\u2014\n**(i)**\nschool leaders;\n**(ii)**\nteachers;\n**(iii)**\nspecialized instructional support personnel;\n**(iv)**\nparaprofessionals; or\n**(v)**\nother staff.\n**(B) Exclusion**\nNotwithstanding subparagraph (A), program personnel shall not include a law enforcement officer or a school security guard.\n**(8) Protection and advocacy system**\nThe term protection and advocacy system means a protection and advocacy system established under section 143 of the Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15043 ).\n**(9) Law enforcement officer**\nThe term law enforcement officer \u2014\n**(A)**\nmeans any person who\u2014\n**(i)**\nis a State, Tribal, or local law enforcement officer (as defined in section 1204 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284 )); and\n**(ii)**\nis assigned by the employing law enforcement agency to a program, who is contracting with a program, or who is employed by a program; and\n**(B)**\nincludes an individual referred to as a school resource officer if that individual meets the definition in subparagraph (A).\n**(10) School security guard**\nThe term school security guard means an individual who is not a sworn law enforcement officer and who is responsible for addressing one or more of the following safety and crime prevention activities in and around a program:\n**(A)**\nAssisting program personnel in safety incidents.\n**(B)**\nEducating students in crime and illegal drug use prevention and safety.\n**(C)**\nDeveloping or expanding community justice initiatives for students.\n**(D)**\nTraining students in conflict resolution and supporting restorative justice programs.\n**(E)**\nServing as a liaison between the program and outside agencies, including other law enforcement agencies.\n**(F)**\nScreening students or visitors to the program for prohibited items.\n**(11) Student**\nThe term student means an individual enrolled in a program.\nI\nProhibition of Corporal Punishment\n#### 101. Prohibition of corporal punishment\n##### (a) Prohibition\nNo student shall be subjected to corporal punishment by program personnel, a law enforcement officer, or a school security guard under any program which receives Federal financial assistance.\n##### (b) Private right of action\nA student who has been subjected to corporal punishment by program personnel, a law enforcement officer, or a school security guard in violation of subsection (a), or the parent of such student, may file a civil action in any Federal or State court of competent jurisdiction against the program under which the violation is alleged to have occurred for attorneys\u2019 fees, expert fees, injunctive relief, and compensatory damages.\n#### 102. Civil actions by the Attorney General\nWhenever the Attorney General receives a complaint in writing signed by a parent (including a legal guardian) or a group of parents (including legal guardians) to the effect that the minor children of such a parent or parents are being deprived by a program of the right under this Act to not be subject to corporal punishment by program personnel, law enforcement officers, or school security guards and the Attorney General believes the complaint is meritorious, the Attorney General is authorized, after giving notice of such complaint to the appropriate program and after certifying that the Attorney General is satisfied that such program has had a reasonable time to adjust the conditions alleged in such complaint, to institute for or in the name of the United States a civil action in any appropriate district court of the United States against such parties and for such relief as may be appropriate, and such court shall have and shall exercise jurisdiction of proceedings instituted pursuant to this section. The Attorney General may implead as defendants such additional parties as are or become necessary to the grant of effective relief hereunder.\n#### 103. Enforcement by the Office for Civil Rights\n##### (a) Referral to Office for Civil Rights\nThe Secretary shall refer any complaint alleging a violation of section 101(a) to the Office for Civil Rights of the Department of Education for an investigation.\n##### (b) Process for referral\nNot later than 90 days after the date of the enactment of this Act, the Secretary shall develop and implement a procedure for receiving a complaint alleging a violation of section 101(a).\n##### (c) Failure To comply\nIn the event that a program has failed to comply with section 101(a), the Secretary shall carry out at least one of the following:\n**(1)**\nWithhold from such program, in whole or in part, further payments (including payments for administrative costs) under an applicable program (as such term is defined in section 400(c) of the General Education Provisions Act ( 20 U.S.C. 1221(c) )) in accordance with section 455 of such Act ( 20 U.S.C. 1234d ).\n**(2)**\nEnter into a compliance agreement in accordance with section 457 of the General Education Provisions Act ( 20 U.S.C. 1234f ).\n**(3)**\nIssue a complaint to compel compliance of such program through a cease and desist order, in the same manner the Secretary is authorized to take such action under section 456 of the General Education Provisions Act ( 20 U.S.C. 1234c ).\n##### (d) Cessation of withholding of funds\nIf the Secretary determines (whether by certification or other appropriate evidence) that a program that is subject to the withholding of payments under subsection (c)(1) of this section has cured the failure providing the basis for the withholding of payments on a date that is within one year from the date on which such payments were first withheld, the Secretary shall\u2014\n**(1)**\ncease the withholding of payments with respect to that program under such subsection; and\n**(2)**\nreimburse all the withheld payments under such subsection to such program.\n##### (e) Withheld funds\nThe funds appropriated or made available for the payments that were withheld under subsection (c)(1) shall be available for expenditure to that program pursuant to this subsection for up to one year from the date upon which the determination in subsection (d) was made.\n##### (f) Rule of construction\nNothing in this section shall be construed to limit the Secretary\u2019s authority under the General Education Provisions Act ( 20 U.S.C. 1221 et seq. ).\n#### 104. Parent notification and protection and advocacy systems\n##### (a) Notification\nIf a student is subject to corporal punishment committed by program personnel, a law enforcement officer, or a school security guard at a program, the program serving such student shall notify, in writing, not later than 24 hours after such use of force occurs, the facts of such use of force to\u2014\n**(1)**\nthe parent or parents of such student;\n**(2)**\nthe State educational agency; and\n**(3)**\nthe local law enforcement agency.\n##### (b) Notification for students with disabilities\nIn the case of a student described in subsection (a) who is an individual with a disability (as defined in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 )) the program serving such student shall\u2014\n**(1)**\nin addition to the notification described in such subsection, notify, in writing, not later than 24 hours after the use of force described in such subsection occurs, the facts of such use of force to the relevant protection and advocacy system; and\n**(2)**\nprovide any information to the relevant protection and advocacy system that the protection and advocacy system may require.\n##### (c) Restatement of authority\nProtection and advocacy systems shall have the same authorities and rights provided under subtitle C of title I of the Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15041 et seq. ) with respect to protections provided for students under this Act when such students are otherwise eligible to be clients of the protection and advocacy system, including investigating, monitoring, and enforcing such protections.\nII\nState Activities and Grant Program\n#### 201. State plan and enforcement\n##### (a) State requirements\nIn accordance with the schedule specified in subsection (c), each State educational agency that receives Federal financial assistance shall provide to the Secretary\u2014\n**(1)**\nin the case of a State that did not prohibit corporal punishment in schools before the date of enactment of this Act, a written assurance that\u2014\n**(A)**\nall programs located in such State have been notified of the requirements of this Act;\n**(B)**\nall program personnel of such State educational agency have received training with respect to such requirements;\n**(C)**\nparents of students served by such State educational agency have been notified of the requirements, rights, and remedies available under this Act; and\n**(D)**\nthe notification required under subparagraph (C) is publicly available on the website of the State educational agency;\n**(2)**\nin the case of a State that prohibited corporal punishment in schools before the date of enactment of this Act, a written assurance that all programs located in such State have been notified of the requirements of this Act; and\n**(3)**\na school climate report that includes a description of\u2014\n**(A)**\nthe policies and procedures of the State educational agency with respect to exclusionary and aversive discipline practices or interventions in such schools;\n**(B)**\nhow the State educational agency plans to implement, is implementing, or has implemented positive behavioral interventions and supports and other models to address student behavior and reduce the use of exclusionary and aversive discipline practices or interventions in the public elementary and secondary schools of such State as required under section 1111(g)(1)(C) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(g)(1)(C) ); and\n**(C)**\nefforts of the State educational agency to ensure program personnel receive the supports and training necessary to implement the interventions, supports, and other models described in subparagraph (B).\n##### (b) Local educational agency requirements\nIn accordance with the schedule specified in subsection (c), each local educational agency shall submit to the State educational agency a report that includes the information the State educational agency determines necessary to comply with the requirements of subsection (a).\n##### (c) Submission schedule\nStates and local educational agencies shall make the submissions required under subsections (a) and (b) as follows:\n**(1)**\nThe initial submissions shall be made not later than one year after the date of enactment of this Act and on an annual basis during each of the 3 years following the year of the first submission.\n**(2)**\nAfter the expiration of the 3-year period described in paragraph (1), subsequent submissions shall be made not less frequently than once every two years.\n##### (d) Report\nFor each year in which the Secretary receives submissions from States in accordance with the schedule specified in subsection (c), the Secretary shall\u2014\n**(1)**\nsubmit to the Committee on Education and Labor of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate a report summarizing the findings of the school climate reports received from States for such year; and\n**(2)**\nmake the school climate reports publicly available.\n##### (e) Enforcement\n**(1) In general**\n**(A) Use of remedies**\nIf a State educational agency fails to comply with subsection (a), the Secretary shall carry out at least one of the following:\n**(i)**\nWithhold, in whole or in part, further payments under an applicable program (as such term is defined in section 400(c) of the General Education Provisions Act ( 20 U.S.C. 1221(c) )) in accordance with section 455 of such Act ( 20 U.S.C. 1234d ).\n**(ii)**\nEnter into a compliance agreement in accordance with section 457 of the General Education Provisions Act ( 20 U.S.C. 1234f ).\n**(iii)**\nIssue a complaint to compel compliance of the State educational agency through a cease and desist order, in the same manner the Secretary is authorized to take such action under section 456 of the General Education Provisions Act ( 20 U.S.C. 1234e ).\n**(B) Cessation of withholding of funds**\nIf the Secretary determines (whether by certification or other appropriate evidence) that a State educational agency that is subject to the withholding of payments under subparagraph (A)(i) has cured the failure providing the basis for the withholding of payments within one year from the date on which such payments were first withheld, the Secretary shall\u2014\n**(i)**\ncease the withholding of payments with respect to the State educational agency under such subparagraph; and\n**(ii)**\nreimburse all the withheld payments under such subparagraph to such State educational agency.\n**(2) Withheld funds**\nThe funds appropriated or made available for the payments that were withheld under paragraph (1)(A)(i) shall be available for expenditure to that program pursuant to this paragraph for up to one year from the date upon which the determination in paragraph (1)(B) was made.\n**(3) Rule of construction**\nNothing in this subsection shall be construed to limit the Secretary\u2019s authority under the General Education Provisions Act ( 20 U.S.C. 1221 et seq. ).\n#### 202. Grant authority\n##### (a) In general\nFrom the amount appropriated under section 306, the Secretary may award grants to State educational agencies to improve school climate and culture by implementing positive behavioral interventions and supports and other models to address student behavior and reduce the use of exclusionary and aversive discipline practices or interventions in public elementary schools and secondary schools.\n##### (b) Duration of grant\n**(1) In general**\nA grant under this section shall be awarded to a State educational agency for a three-year period.\n**(2) Reapplication**\nAt the end of a grant period described in paragraph (1), a State educational agency desiring a subsequent grant under this section may be eligible for such grant if such State educational agency\u2014\n**(A)**\nsubmits an application under subsection (c); and\n**(B)**\ndemonstrates\u2014\n**(i)**\nthat such State educational agency effectively used grant funds to carry out the required activities under subsection (e) during the previous grant period; and\n**(ii)**\nwith respect to such State educational agency, a decrease in at least one of the following:\n**(I)**\nExclusionary and aversive discipline practices or interventions, including in-school suspensions, out-of-school suspensions, and expulsions.\n**(II)**\nSchool-related arrests.\n**(III)**\nReferrals of students to law enforcement.\n**(3) Data**\nA State educational agency shall, with respect to the data used under paragraph (2)(B)(ii)\u2014\n**(A)**\ncross-tabulate such data and disaggregate by race, gender, disability, and English learner status; and\n**(B)**\nredact all personally identifiable information from such data.\n##### (c) Application\n**(1) In general**\nEach State educational agency desiring a grant under this section shall submit an application to the Secretary at such time, in such manner, and accompanied by such information as the Secretary may require, including\u2014\n**(A)**\ninformation on how the State educational agency will carry out the required activities specified in subsection (e);\n**(B)**\na description of how the State educational agency will improve school climate and culture by reducing the use of exclusionary and aversive discipline practices or interventions;\n**(C)**\na description of how the State educational agency will implement positive behavioral interventions and supports, and other models (including models such as restorative justice interventions, trauma-informed care, multi-tiered system of supports, crisis and de-escalation interventions, implicit bias training, and culturally responsive teaching), to address student behavior and work to eliminate the use of exclusionary and aversive discipline practices or interventions; and\n**(D)**\na description of how the State educational agency will develop and implement high-quality training for program personnel designed to improve school climate and culture and increase the use of positive behavioral interventions and supports and other models to address student behavior and reduce the use of exclusionary and aversive discipline practices or interventions.\n**(2) Priority**\nIn awarding grants under this section, the Secretary shall give priority to State educational agencies\u2014\n**(A)**\nwith a high percentage of in-school suspensions, out-of-school suspensions, expulsions, school-related arrests, and referrals of students to law enforcement;\n**(B)**\nthat lack positive behavioral interventions and supports and other models to improve school climate and culture; or\n**(C)**\nthat are in most need of assistance relating to improving school climate and culture by reducing the use of exclusionary and aversive discipline practices or interventions, as determined by the Secretary.\n##### (d) Authority To make subgrants\n**(1) In general**\nA State educational agency receiving a grant under this section may use such grant funds to award subgrants, on a competitive basis in accordance with subsection (e)(2), to local educational agencies.\n**(2) Application**\nA local educational agency desiring to receive a subgrant under this section shall submit an application to the applicable State educational agency at such time, in such manner, and containing such information as the State educational agency may require, including the information described in subparagraphs (A) through (D) of subsection (c)(1) with respect to the local educational agency.\n##### (e) Required activities\n**(1) In general**\nA State educational agency receiving a grant, or a local educational agency receiving a subgrant, under this section shall use such grant or subgrant funds to carry out the following:\n**(A)**\nDeveloping and implementing high-quality training for program personnel designed to\u2014\n**(i)**\nimprove school climate and culture;\n**(ii)**\nincrease use of positive behavioral interventions and supports and other models to address student behavior; and\n**(iii)**\nreduce the use of exclusionary and aversive discipline practices or interventions and the discriminatory and disproportionate impact such practices have on students based on their race, ethnicity, gender, or disability.\n**(B)**\nProviding technical assistance to improve school climate and culture by implementing positive behavioral interventions and supports, and other models (including models such as restorative justice interventions, trauma-informed care, multi-tiered system of supports, crisis and de-escalation interventions, implicit bias training, and culturally responsive teaching), to address student behavior and work to eliminate the use of exclusionary and aversive discipline practices or interventions.\n**(C)**\nResearching, developing, implementing, and evaluating models, policies, and procedures to reduce the use of exclusionary and aversive discipline practices or interventions in public elementary schools and secondary schools.\n**(2) Priority**\nA State educational agency or local educational agency shall prioritize carrying out the activities specified in subparagraphs (A) through (C) of paragraph (1) in public elementary schools and secondary schools\u2014\n**(A)**\nin which a disproportionately high percentage of students who have been subjected to disciplinary proceedings or have otherwise experienced the application of such a school\u2019s discipline policies, practices, and procedures, relative to such school\u2019s total student population, are students of color or students with disabilities (as defined in section 602 of the Individuals with Disabilities Education Act ( 20 U.S.C. 1401 ));\n**(B)**\nwith a high percentage of in-school suspensions, out-of-school suspensions, expulsions, school-related arrests, and referrals of students to law enforcement;\n**(C)**\nthat lack positive behavioral interventions and supports and other models to improve school climate and culture; or\n**(D)**\nthat have demonstrated meaningful community engagement in selecting models to improve school climate and culture.\n##### (f) Evaluation and report\n**(1) Local educational agency reports**\nEach local educational agency receiving a subgrant under this section shall, at the end of the grant period for such subgrant, prepare and submit to the State educational agency a report that\u2014\n**(A)**\nevaluates the progress of the local educational agency toward carrying out the required activities under subsection (e); and\n**(B)**\nincludes any additional information the State educational agency determines necessary to complete the report required under paragraph (2).\n**(2) State educational agency reports**\nEach State educational agency receiving a grant under this section shall, at the end of the three-year grant period for such grant, prepare and submit to the Secretary a report that\u2014\n**(A)**\nevaluates the State\u2019s progress toward carrying out the required activities under subsection (e);\n**(B)**\nincludes data on the impact of the grant program on school climate and culture during such grant period, including, with respect to the State educational agency, data on the prevalence of, and increase or decrease in\u2014\n**(i)**\nexclusionary and aversive discipline practices or interventions, including in-school suspensions, out-of-school suspensions, and expulsions;\n**(ii)**\nschool-related arrests; and\n**(iii)**\nstudent referrals to law enforcement;\n**(C)**\nincludes the number of high-quality school climate and culture trainings conducted for program personnel during such grant period;\n**(D)**\ndescribes the models implemented to improve school climate and culture during such grant period;\n**(E)**\nspecifies the number of subgrants made under subsection (d) and the local educational agencies that were awarded such subgrants; and\n**(F)**\nincludes such information as the Secretary may require.\n**(3) Data**\nA State educational agency shall, with respect to the data described in paragraph (2)(B)\u2014\n**(A)**\ncross-tabulate and disaggregate the data in the same manner as under subsection (b)(3)(A); and\n**(B)**\nredact all personally identifiable information from such data.\n**(4) Publication**\nNot later than one year after receiving a report under paragraph (2), the Secretary shall make the report publicly available on the website of the Department of Education.\n##### (g) Funds available for the Department of the Interior\nFrom the amount appropriated under section 306, the Secretary shall allocate\u2014\n**(1)**\n0.5 percent of such funds to the Secretary of the Interior for activities under this section with respect to schools operated or funded by the Department of the Interior, under such terms and conditions as the Secretary may prescribe; and\n**(2)**\n0.5 percent of such funds for activities under this section with respect to schools operated in the outlying areas, under such terms and conditions as the Secretary may prescribe.\nIII\nAdditional Provisions\n#### 301. Federal regulations\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall issue such regulations as are necessary to reasonably ensure compliance with this Act.\n##### (b) Negotiated rulemaking process\nIn carrying out subsection (a), the Secretary shall use a negotiated rulemaking process described in section 1601 and section 1602 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6571 ; 6572) except subparagraph (A) of subsection (b)(3) of such section 1601 shall apply by substituting establish a negotiated rulemaking process; for the text of such subparagraph.\n#### 302. Other schools\n##### (a) Department of Defense\nThe Secretary of Defense shall ensure that schools operated or funded by the Department of Defense Education Activity or otherwise operated or funded by the Department of Defense for the education of military-connected dependents comply with the regulations promulgated by the Secretary pursuant to this Act.\n##### (b) Department of Interior\nThe Secretary of the Interior shall ensure that schools operated or funded by the Department of the Interior comply with the regulations promulgated by the Secretary pursuant to this Act.\n#### 303. Limitation of authority\n##### (a) In general\nNothing in this Act shall be construed\u2014\n**(1)**\nto restrict or limit, or allow the Secretary to restrict or limit, any other rights or remedies otherwise available to students or parents under Federal, State, or local law or regulation; or\n**(2)**\nto restrict or limit Federal, State, or local laws, regulations, or polices that provide for more stringent prohibitions or limitations on the use of corporal punishment than the prohibitions or limitations that are provided for in this Act.\n##### (b) Law enforcement officer duties\nNothing in this Act shall be construed to prevent a sworn law enforcement officer from carrying out the lawful duties of the officer under otherwise applicable law.\n##### (c) Rule of construction on enforcement\nNothing in this Act shall be construed to affect the enforcement of title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ), title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ), section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ), or the Department of Education Organization Act ( 20 U.S.C. 3401 et seq. ) and their enforcing regulations.\n#### 304. Applicability to private schools and home schools\n##### (a) Private schools\nNothing in this Act shall be construed to affect any private school that does not receive, or does not serve students who receive, support in any form from any program or activity supported, in whole or in part, with Federal funds.\n##### (b) Home schools\nNothing in this Act shall be construed to\u2014\n**(1)**\naffect a home school, whether or not a home school is treated as a private school or home school under State law; or\n**(2)**\nconsider parents who are schooling a child at home as program personnel.\n#### 305. Severability\nIf any provision of this Act or the application of such provision to any person or circumstance is held to be unconstitutional, the remaining provisions of this Act and the application of such provisions to any person or circumstance shall not be affected thereby.\n#### 306. Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out this Act for fiscal year 2025 and each fiscal year thereafter.",
      "versionDate": "2025-05-08",
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
        "name": "Education",
        "updateDate": "2025-05-22T17:36:05Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3265ih.xml"
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
      "title": "Protecting our Students in Schools Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-16T09:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting our Students in Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-16T09:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of corporal punishment in schools, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T09:03:20Z"
    }
  ]
}
```
