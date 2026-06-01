# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3378?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3378
- Title: Racehorse Health and Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3378
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2026-04-07T08:05:29Z
- Update date including text: 2026-04-07T08:05:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3378",
    "number": "3378",
    "originChamber": "House",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "H001077",
        "district": "3",
        "firstName": "Clay",
        "fullName": "Rep. Higgins, Clay [R-LA-3]",
        "lastName": "Higgins",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Racehorse Health and Safety Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:29Z",
    "updateDateIncludingText": "2026-04-07T08:05:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "NC"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "OK"
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
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3378ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3378\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Higgins of Louisiana (for himself, Mr. Davis of North Carolina , and Mr. Cole ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo protect the health and welfare of covered horses and improve the integrity and safety of horseracing by authorizing States to enter into an interstate compact to develop and enforce scientific medication control rules and racetrack safety rules that are uniform for each equine breed, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Racehorse Health and Safety Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nSec. 3. Repeal of the Horseracing Integrity and Safety Act of 2020.\nSec. 4. Authorization to enter into interstate compact.\nTitle I\u2014Racehorse Health and Safety Organization\nSec. 101. Racehorse Health and Safety Organization.\nSec. 102. Role of States and State racing commissions.\nSec. 103. Exemption from the Federal Advisory Committee Act.\nTitle II\u2014Horseracing scientific medication control\nSec. 201. Scientific medication control committees.\nSec. 202. Horseracing scientific medication control rules.\nTitle III\u2014Racetrack safety\nSec. 301. Definition of Committee.\nSec. 302. Racetrack Safety Committee.\nSec. 303. Racetrack safety rules.\nTitle IV\u2014Rule violations\nSec. 401. Prohibited acts.\nSec. 402. Results management and disciplinary process.\nSec. 403. Administrative sanctions.\nTitle V\u2014General provisions\nSec. 501. Effective dates.\n#### 2. Definitions\nIn this Act:\n**(1) Advance deposit wager**\nThe term advance deposit wager means a legal form of parimutuel wager in which an individual deposits money into an account and such funds are used to pay for parimutuel wagers made either on-track or off-track.\n**(2) Board**\nThe term Board means the board of directors of the Racehorse Health and Safety Organization established under section 101.\n**(3) Breed registry**\nThe term breed registry \u2014\n**(A)**\nmeans the organization with which an owner or breeder officially registers his or her horse for horseracing; and\n**(B)**\nincludes\u2014\n**(i)**\nin the case of Thoroughbreds, the Jockey Club;\n**(ii)**\nin the case of Standardbreds, the United States Trotting Association; and\n**(iii)**\nin the case of Quarter Horses, the American Quarter Horse Association.\n**(4) Covered horse**\nThe term covered horse means any Thoroughbred, Standardbred, or Quarter Horse during the period\u2014\n**(A)**\nbeginning on the date of the horse\u2019s first timed and reported workout at a racetrack that participates in covered horseraces or at a training facility; and\n**(B)**\nending on the earlier of\u2014\n**(i)**\nthe date on which the horse is permanently ineligible to be entered in a covered horserace; or\n**(ii)**\nthe date of the death of the horse.\n**(5) Covered horserace**\nThe term covered horserace means any horserace involving covered horses that has a substantial relation to interstate commerce, including any horserace that is the subject of interstate off-track wagers or advance deposit wagers.\n**(6) Covered person**\nThe term covered person means any trainer, owner, breeder, jockey, driver, racetrack, veterinarian, person (as defined in section 1, of title 1, United States Code) licensed by a State racing commission, any agent, assign, or employee of such a person, and any other horse support personnel engaged in the care, training, or racing of covered horses.\n**(7) Equine industry representative**\nThe term equine industry representative means an organization representing the interests of, and whose membership consists in whole or in part of, owners, breeders, trainers, racetracks, veterinarians, State racing commissions, jockeys, and drivers.\n**(8) Immediate family member**\nThe term immediate family member includes a spouse, domestic partner, mother, father, aunt, uncle, sibling, child, or member of the same household.\n**(9) Interstate compact**\nThe term interstate compact means the interstate compact entered into pursuant to this Act.\n**(10) Interstate off-track wager**\nThe term interstate off-track wager has the meaning given such term in section 3 of the Interstate Horseracing Act of 1978 ( 15 U.S.C. 3002 ).\n**(11) Jockey; driver**\nThe terms jockey and driver mean an individual who is a rider or driver of a covered horse in a covered horserace.\n**(12) Member State**\nThe term member State means a State that is a member of the interstate compact.\n**(13) Owner; breeder**\nThe terms owner and breeder mean an individual who\u2014\n**(A)**\nholds an ownership interest in a covered horse; or\n**(B)**\nis in the business of breeding covered horses.\n**(14) Racetrack**\nThe term racetrack means an organization or person licensed by a State racing commission to conduct covered horseraces.\n**(15) RHSO**\nThe term RHSO means the Racehorse Health and Safety Organization established under section 101.\n**(16) Scientific medication control committee**\nThe term scientific medication control committee means a committee established under section 201.\n**(17) State racing commission**\nThe term State racing commission means an entity designated by State law or regulation that has jurisdiction over the conduct of horseracing within the applicable State.\n**(18) Trainer**\nThe term trainer means an individual that is engaged in the training of covered horses and is the recipient of direct or indirect compensation or anything of value for such services or expertise.\n**(19) Training facility**\nThe term training facility means a location that\u2014\n**(A)**\nis not a racetrack recognized and designated by the Racehorse Health and Safety Organization; and\n**(B)**\noperates primarily to house covered horses or to conduct official timed workouts or qualifying races.\n**(20) Veterinarian**\nThe term veterinarian means a licensed veterinarian who provides veterinary services to covered horses.\n**(21) Workout**\nThe term workout means\u2014\n**(A)**\na timed running of a horse over a predetermined distance not associated with a purse race; or\n**(B)**\nthe competing of a horse in a harness qualifying race.\n#### 3. Repeal of the Horseracing Integrity and Safety Act of 2020\nThe Horseracing Integrity and Safety Act of 2020 ( 15 U.S.C. 3051 et seq. ) is repealed.\n#### 4. Authorization to enter into interstate compact\n##### (a) In general\nThe consent of Congress is given for States to enter into an interstate compact in accordance with this Act.\n##### (b) Consent of States\nA State may demonstrate consent to enter into the interstate compact through the enactment of a State law that contains a provision indicating such consent that is substantially similar to the following:\nThe State of _________ hereby consents to and enters into the interstate compact established in accordance with the Racehorse Health and Safety Act of 2025 . .\n##### (c) Prohibition on interstate off-Track wagers among non-Member States\n**(1) In general**\nSubject to, and in accordance with, the Interstate Horseracing Act of 1978 ( 15 U.S.C. 3001 et seq. ), a host State that is a member State of the interstate compact may allow the interstate transmission of any electronic signal for the purposes of allowing for the placement of interstate off-track wagers or advance deposit wagers pertaining to the covered horserace concerned.\n**(2) Exception**\nA host State that is not a member State of the interstate compact is prohibited from allowing interstate transmission of any electronic signal for the purposes described in paragraph (1).\n**(3) Host State defined**\nIn this subsection, the term host State means a State in which a horserace subject to an interstate wager takes place.\nI\nRacehorse Health and Safety Organization\n#### 101. Racehorse Health and Safety Organization\n##### (a) In general\nStates that are members of the interstate compact shall\u2014\n**(1)**\nestablish and participate in an organization, to be known as the Racehorse Health and Safety Organization or the RHSO , to coordinate the decision making and actions of the State racing commission of each member State; and\n**(2)**\ndevelop bylaws and rules governing the RHSO, including rules establishing the RHSO as an agency for purposes of subchapter II of chapter 5 of title 5, United States Code.\n##### (b) Board of directors\n**(1) In general**\nThe RHSO shall be governed by a board of directors composed of 9 members, of whom\u2014\n**(A)**\n5 shall be appointed by the State racing commission of each of the 5 member States that had the greatest number of racing days during the preceding 3-year period, with each such State racing commission appointing 1 member; and\n**(B)**\n4 shall be appointed by the State racing commissions of the remaining member States.\n**(2) Membership**\n**(A) Chairperson**\nThe chairperson of the Board shall be elected annually by majority vote from among the members of the Board.\n**(B) Term**\n**(i) In general**\nExcept as provided in clauses (ii) and (iii), the term of a member of the Board shall not exceed 3 years. No member shall serve more than 3 full terms.\n**(ii) Initial appointment**\nFor purposes of staggering terms of appointment, the initial members appointed by the State racing commissions in the 5 member States that had the greatest number of racing days during the prior 3-year period shall serve an initial term of 4 years.\n**(iii) Expansion in case of fewer than 9 member States**\nIf, as of the date described in section 502(a), fewer than 9 States have entered the interstate compact, the Board shall add a new member as each new State enters the interstate compact, up to a maximum of 9 members.\n**(iv) Vacancies**\nA vacancy on the Board shall be filled in the same manner as the position was appointed immediately prior to the vacancy. An individual appointed to fill a vacancy occurring before the expiration of the term for which the predecessor of that individual was appointed shall be appointed for the remainder of that term. When the term of office of a member ends, the member may continue to serve until a successor is appointed.\n**(C) Conflicts of interest**\n**(i) In general**\nEach member of the Board shall\u2014\n**(I)**\nbefore accepting appointment as a Board member, disclose any potential conflict of interest;\n**(II)**\nnotify the full Board immediately upon engaging in any activity that the RHSO determines may be perceived as a conflict of interest; and\n**(III)**\nnot less frequently than annually, certify in writing the information referred to in subclauses (I) and (II) and disclose any potential or perceived conflicts of interest.\n**(ii) Recusal required**\nA member of the Board shall recuse himself or herself from discussion of any item before the Board if such discussion\u2014\n**(I)**\nrelates to the direct financial interest of the member of the Board or an immediate family member of the member of the Board; and\n**(II)**\ndoes not apply to all covered horses within a breed.\n**(D) Removal and ethics**\nThe Board may remove by majority vote a member of the Board or the chairperson of the Board for\u2014\n**(i)**\nneglect of duty, unethical behavior, or malfeasance in office (including conduct determined by the Board to be injurious to the integrity of horseracing, such as contract violations or perjury); or\n**(ii)**\nconviction of a violation of a Federal or State civil or criminal law related to horseracing.\n**(E) Quorum**\nIn order to consider at a meeting any item requiring the approval of the Board, the Board shall have in attendance at such a meeting (either in person or remotely) a majority of members of the Board.\n##### (c) Duties of the Board\nThe duties of Board shall be\u2014\n**(1)**\n**(A)**\nto adopt rules with respect to scientific medication control recommended by each scientific medication control committee under section 202; or\n**(B)**\nto modify, or not adopt rules so recommended or adopt alternative rules if the Board determines, by a preponderance of evidence, that such recommendations do not meet the requirements specified in paragraph (4);\n**(2)**\n**(A)**\nto adopt rules with respect to racetrack safety recommended by the Racetrack Safety Committee under section 303; or\n**(B)**\nto modify, or not adopt rules so recommended or adopt alternative rules if the Board determines, by a preponderance of evidence, that such recommendations do not meet the requirements specified in paragraph (4);\n**(3)**\nto adopt rules with respect to rule violations, as described in sections 401, 402, and 403;\n**(4)**\nto ensure that any rule adopted under paragraph (1), (2), or (3) is based on generally accepted scientific principles and methods, and to the extent possible, on peer-reviewed scientific data and studies;\n**(5)**\nto hold open meetings with respect to proposed rules recommended under sections 202 and 303, at which the chairperson of the scientific medication control committee concerned or the chairperson of the Racetrack Safety Committee, as applicable, or the representative of such chairperson, shall present such proposed rules;\n**(6)**\nnot later than 45 days before any such meeting is to be held\u2014\n**(A)**\nto post on the internet website of the RHSO any proposed rule described in paragraph (1) or (2) (or modifications to such rules) under consideration at such meeting; and\n**(B)**\nto submit to each State racing commission (and to any other individual upon request) notification of such meeting;\n**(7)**\nto adopt any rule under paragraphs (1), (2), and (3) by a vote of not less than a two-thirds majority of the Board, determine the effective date of any such rule, and update any such rule in accordance with the process established under paragraphs (5) and (6);\n**(8)**\nafter notice and an opportunity for public comment, in consultation with the State racing commissions, to develop and maintain a nationwide database of racehorse safety, performance, health, and injury information for the purpose of conducting an epidemiological study;\n**(9)**\nin carrying out paragraph (8), to require covered persons and equine industry representatives to collect and submit for inclusion in such database such information as the RHSO considers necessary to further the goal of increased horse welfare;\n**(10)**\nwith respect to covered persons\u2014\n**(A)**\nsubject to section 102, to issue subpoenas and investigate rule violations; and\n**(B)**\nto refer to the appropriate State racing commission any such violation for enforcement action unless the State racing commission concerned agrees to give that enforcement authority to the RHSO;\n**(11)**\nin consultation with member States, to develop uniform standards for veterinarian\u2019s and steward\u2019s lists and uniform procedures for entering horses on, and removing horses from, such lists;\n**(12)**\nto establish, and conduct oversight activities with respect to, the scientific medication control committees under section 201 and the Racetrack Safety Committee under 302;\n**(13)**\nin carrying out paragraph (12), with respect to members of the committees referred to in that paragraph\u2014\n**(A)**\nto assess such members for potential conflicts on a case-by-case basis; and\n**(B)**\nto determine, in the sole discretion of the Board, whether the potential conflict requires removal from the committee or denial of the opportunity to vote on an item pending before the relevant committee;\n**(14)**\nto carry out activities described in subsection (e) relating to laboratory accreditation; and\n**(15)**\nto ensure that member States comply with the terms of this Act, the interstate compact, and the rules adopted by the Board under this section, including the prohibition on interstate off-track wagers among non-member States specified in section 4(c).\n##### (d) Funding\n**(1) Initial funding**\nThe RHSO, acting through the Board, shall assess an initial fee from each State racing commission of a member State in an amount determined by the Board to be sufficient to cover the startup costs of the racing commission for the first full year that begins after the effective date specified in section 502(a).\n**(2) Permanent funding**\n**(A) Assessment and collection of fees by States**\n**(i) In general**\nBeginning on a date determined by the RHSO, each State racing commission of a member State shall remit to the RHSO an amount of fees determined under subparagraph (B), in accordance with a schedule developed by the RHSO.\n**(ii) Determination of methods**\nEach State racing commission of a member State shall determine, subject to the applicable laws, regulations, and contracts of the State concerned, the method by which the amount of fees determined in accordance with subparagraph (B) shall be allocated, assessed, and collected.\n**(B) Annual calculation of amounts required**\n**(i) In general**\nFor the first year in which fees are collected under this subsection, not later than the date determined by the RHSO, and not later than November 1 each year thereafter, the RHSO shall determine and provide to each State racing commission the estimated amount required from each member State\u2014\n**(I)**\nto fund the member State\u2019s proportionate share of the expenditures incurred in administering the horseracing scientific medication control rules under subsection (c)(1) and the racetrack safety rules under section subsection (c)(2) for each breed of covered horses racing in covered horseraces in the State; and\n**(II)**\nto liquidate any loan undertaken or other debt incurred to cover a shortfall in fees assessed for the current calendar year and any preceding calendar year.\n**(ii) Basis of calculation**\nThe amounts calculated under clause (i) shall be based on the annual breed-specific budget of the RHSO for the breed in that State for the following year as approved by the Board of Directors after taking into account\u2014\n**(I)**\nthe projected number of racing starts for the year separately for each breed in that State; and\n**(II)**\nany other sources of RHSO income.\n**(C) State racing commission assessment**\n**(i) Sources**\nA State may fund the amount required under subparagraph (B)(i) from a variety of sources, including foal registration fees, sales contributions, starter fees, track fees, and other fees on covered persons.\n**(ii) Breed-specific assessments**\nIn assessing fees to meet the requirement under subparagraph (B), a State racing commission shall assess fees on a breed-specific basis, for the Standardbred, Thoroughbred, and the Quarter Horse industries operating within that State. Each such assessment shall be specifically earmarked for the development, refinement, and maintenance of\u2014\n**(I)**\nhorseracing scientific medication control rules consistent with subsection (c)(1) that are specific and limited to each breed\u2019s unique performance model and developed safety protocols; and\n**(II)**\nracetrack safety rules consistent with subsection (c)(2) that are specific and limited to each breed\u2019s unique performance model and developed safety protocols.\n**(iii) No commingling**\nA State racing commission of a member State shall ensure that funds assessed by the member State for a single breed of covered horses shall not be commingled for the use or subsidy of any other breed of covered horses.\n**(iv) Three-fourths majority vote required for rate increases**\nIn the case of a proposed increase in the amount required under clause (i) that exceeds 5 percent, such increase shall only become effective if the increase is approved by a vote of not less than a three-fourths majority of the Board.\n**(3) Borrowing**\nThe RHSO may incur debt to carry out the duties of the RHSO but may not accept loans from any covered person or equine industry representative.\n##### (e) Testing laboratories\n**(1) In general**\nThe RHSO shall review existing rules relating to laboratory accreditation and testing standards issued by the State racing commissions and the National Veterinary Services Laboratories of the Animal and Plant Health Inspection Service of the Department of Agriculture.\n**(2) Administration**\n**(A) In general**\nThe RHSO shall select an accreditation body to conduct the accreditation of laboratories and the audits of laboratories so accredited to ensure compliance with rules issued under subsection (c)(1).\n**(B) Authority**\nThe accreditation body selected under subparagraph (A) shall have the authority to require specific test samples to be directed to, and tested by, laboratories with special expertise in the required tests.\n**(C) Condition of accreditation**\nThe accreditation body so selected shall ensure that each laboratory seeking accreditation to conduct testing of covered horses has a relationship with a national laboratory, such as the National Veterinary Services Laboratories of the Animal and Plant Health Inspection Service.\n**(3) Selection of laboratories**\n**(A) In general**\nA State racing commission may select, for purposes of testing samples from covered horses racing in covered horseraces in the State concerned, a laboratory accredited by the accreditation body selected under paragraph (2).\n**(B) Selection by the RHSO**\nIf a State racing commission selects a laboratory that is not accredited by the accreditation body selected under paragraph (2), the RHSO shall select a laboratory accredited by the accreditation body selected under paragraph (2) to test samples taken in that State.\n#### 102. Role of States and State racing commissions\n##### (a) Enforcement authority\n**(1) State election To enforce**\nA State racing commission may elect to exercise enforcement authority with respect to the rules issued under paragraphs (1) and (2) of section 101(c) within the State concerned.\n**(2) RHSO rules**\nIf a State racing commission does not make the election described in paragraph (1), the RHSO shall enforce the rules issued under paragraphs (1) and (2) of section 101(c) within the State, pursuant to a memorandum of understanding entered into with the RHSO.\n##### (b) Preemption\nThe rules of the RHSO promulgated in accordance with this Act shall preempt any provision of State law or regulation of member States with respect to matters within the jurisdiction of the RHSO.\n##### (c) Unfair or deceptive acts or practices\nEach member State shall, as a condition of being a member of the interstate compact, have in effect a statute that treats as an unfair or deceptive act or practice the sale of a covered horse, or of any other horse in anticipation of its future participation in a covered race, if the seller\u2014\n**(1)**\nknows or has reason to know the horse has been administered\u2014\n**(A)**\na bisphosphonate prior to the horse\u2019s fourth birthday; or\n**(B)**\nany other substance or method the RHSO determines has a long-term degrading effect on the soundness of the covered horse; and\n**(2)**\nfails to disclose to the buyer the administration of the bisphosphonate or other such substance or method.\n#### 103. Exemption from the Federal Advisory Committee Act\nRHSO and any committee or subcommittee of RHSO are not subject to chapter 10 of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act).\nII\nHorseracing scientific medication control\n#### 201. Scientific medication control committees\n##### (a) In general\nFor purposes of developing, updating, and implementing a set of proposed rules with respect to horseracing scientific medication control for covered horses, covered persons, and covered horseraces, the RHSO shall establish a scientific medication control committee with respect to each breed of horses involved in covered horserace, as follows:\n**(1)**\nA Standardbred Racing Scientific Medication Control Committee.\n**(2)**\nA Quarter Horse Racing Scientific Medication Control Committee.\n**(3)**\nA Thoroughbred Racing Scientific Medication Control Committee.\n##### (b) Duties\nEach scientific medication control committee shall draft proposed rules regarding scientific medication control, in accordance with subsection (e), and shall recommend the proposed rules to the Board.\n##### (c) Meetings\nExcept as provided in subsection (e), meetings of a scientific medication control committee may be closed.\n##### (d) Membership\n**(1) Composition**\nEach scientific medication control committee shall be composed of 7 members, as follows:\n**(A) Regulatory members**\nThree members of each scientific medication control committee shall be appointed\u2014\n**(i)**\nby the Board from within the equine industry; and\n**(ii)**\nbased on their knowledge of equine exercise physiology, forensic toxicology, or equine pharmacology.\n**(B) Industry members**\nFour members of each scientific medication control committee shall be appointed as follows:\n**(i)**\nFor the Standardbred Racing Scientific Medication Control Committee, such appointments shall be made by the United States Trotting Association.\n**(ii)**\nFor the Quarter Horse Racing Scientific Medication Control Committee, such appointments shall be made by the American Quarter Horse Association.\n**(iii)**\nFor the Thoroughbred Racing Scientific Medication Control Committee, such appointments shall be made by the National Horsemen\u2019s Benevolent and Protective Association.\n**(2) Qualifications**\n**(A) In general**\nThe members of a scientific medication control committee appointed under paragraph (1)(B) shall\u2014\n**(i)**\nhave significant, recent experience in medication control or toxicology research; or\n**(ii)**\nhold a doctorate of philosophy or equivalent degree.\n**(B) Additional qualifications**\nOf the members appointed under paragraph (1)(B)\u2014\n**(i)**\nat least 1 member shall be a mathematician or statistician with experience in threshold determination;\n**(ii)**\nat least 1 member shall be an equine exercise physiologist;\n**(iii)**\nat least 1 member shall be an equine pharmacologist; and\n**(iv)**\nat least 1 member shall be an analytical chemist.\n**(3) Term**\n**(A) In general**\nExcept as provided in subparagraph (B), the term of each member of a scientific medication control committee shall not exceed 3 years. Such term is renewable for an indefinite number of terms.\n**(B) Initial term**\nFor purposes of staggering the terms of appointment, the members first appointed under paragraph (1)(A) shall serve an initial term of 4 years.\n**(C) Limitation**\nNo member of a scientific medication control committee may serve as a member on more than 2 scientific medication control committees.\n**(4) Chairperson**\nThe chairperson of each scientific medication control committee shall be elected annually from among the members of the scientific medication control committee by majority vote of the scientific medication control committee.\n**(5) Conflicts of interest**\nEach member appointed to a scientific medication control committee shall, before the beginning of any meeting of the scientific medication control committee, declare any conflicts of interest directly pertinent to the agenda of such meeting.\n**(6) Quorum**\nIn order to consider at a meeting any rule being proposed to the Board, each scientific medication control committee shall have in attendance at such a meeting (either in person or remotely) a majority of members of the scientific medication control committee.\n##### (e) Rules for scientific medical control\n**(1) Adoption of rules**\nNot later than 90 days before the consideration of a rule (or a modification to such a rule), each scientific medication control committee shall hold an open meeting at which covered persons or their representatives may provide input.\n**(2) Notice of meeting**\nNot less than 45 days before the date on which the meeting referred to in paragraph (1) is to be held, the agenda, location, and date of such meeting shall\u2014\n**(A)**\nbe posted on the internet website of the RHSO;\n**(B)**\nsubmitted to the Racing Medication and Testing Consortium, the Harness Racing Medication Collaborative, and the American Quarter Horse Association Medication Committee; and\n**(C)**\nprovided to any individual or entity requesting such information.\n**(3) Recording of input**\nIf any input from a covered person (or a representative of a covered person) is provided during a meeting referred to in paragraph (1), or provided in writing, such input shall be transcribed and recorded and made part of the record of the scientific medication control committee concerned.\n**(4) Review of medication and threshold rules**\n**(A) In general**\nEach scientific medication control committee shall review\u2014\n**(i)**\nall existing medication and threshold rules issued by State racing commissions with respect to covered horses; and\n**(ii)**\nall available research on medication thresholds for covered horses.\n**(B) Penalty recommendations**\nA scientific medication control committee may revise penalty recommendations with respect to each substance reviewed as part of the medication and threshold review under subparagraph (A).\n**(C) Medications**\nEach scientific medication control committee shall\u2014\n**(i)**\nreview the development of any new medication on an ongoing basis to determine whether such medication should be subject to the medication control rules issued pursuant to section 101(c); and\n**(ii)**\nif the scientific medication control committee determines that such a medication should be subject to such rules, the scientific medication control committee shall develop and submit to the Board for approval proposed modifications to such rules to include such medication.\n#### 202. Horseracing scientific medication control rules\n##### (a) Applicability\nScientific medication control rules issued under section 101(c)(1) for each breed of covered horse shall apply to\u2014\n**(1)**\ncovered horseraces, covered persons, and covered horses in member States; and\n**(2)**\nany covered horse or covered person from a State that is not a member State that seeks to race in a covered horserace in a member State.\n##### (b) Development of proposed rules\n**(1) In general**\nIn developing proposed scientific medication control rules with respect to a breed of covered horses, to the extent possible, a scientific medication control committee shall\u2014\n**(A)**\nuse scientific methods;\n**(B)**\naddress all topics set forth in subsection (c); and\n**(C)**\ntake into account the unique characteristics and needs of such breed and its racing performance model, including the varying number and nature of races each year for the breed.\n**(2) Transition**\nUntil the date on which rules issued by the RHSO pursuant to section 101(c) become effective, the rules of the State concerned shall apply with respect to the administration of medication to covered horses racing in covered horseraces.\n##### (c) Elements\nThe proposed rules referred to in subsection (b) shall provide\u2014\n**(1)**\nthat\u2014\n**(A)**\na covered horse may only compete in a covered horserace if the horse is\u2014\n**(i)**\nfree from the active pharmacological effect of medications, other foreign substances, and methods that enhance the natural performance of the covered horse; and\n**(ii)**\nunencumbered by\u2014\n**(I)**\nforeign substances; and\n**(II)**\ndiseases or conditions;\n**(B)**\na covered horse that is injured or determined by a veterinarian to be unsound may not train or participate in a covered horserace;\n**(C)**\nthe use of medications, other foreign substances, and treatment methods that mask pain in order to allow an injured or unsound covered horse to train or race in a covered horserace shall be prohibited;\n**(D)**\nwith respect to the uniformity of rules, standards, procedures, and protocols regulating medication and treatment methods for covered horses and covered horseraces, such rules, standards, procedures, and protocols\u2014\n**(i)**\nshall be uniform within each breed of covered horse; and\n**(ii)**\nshall not be imposed on all 3 breeds unless specifically adopted by the scientific medication control committee for each breed; and\n**(E)**\nbreed-specific rules, standards, procedures, and protocols shall include breed-specific permissible thresholds, medication withdrawal guidelines, and other breed-specific concerns with respect to the administration of medication; and\n**(2)**\nfor\u2014\n**(A)**\nthe development, in consultation with the State racing commissions and the National Veterinary Services Laboratories of the Animal and Plant Health Inspection Service, of a list of permitted and prohibited medications, methods, and substances, for each breed of covered horse;\n**(B)**\na process for the review by the scientific medication control committee concerned for the administration of any medication to a covered horse during the 24-hour period preceding the next racing start of the covered horse; and\n**(C)**\nthe performance and management of test distribution planning (including intelligence-based testing), the sample collection process, and in-competition and out-of-competition testing (including no-advance-notice testing).\nIII\nRacetrack safety\n#### 301. Definition of Committee\nIn this title, the term Committee means the Racetrack Safety Committee established under section 302.\n#### 302. Racetrack Safety Committee\n##### (a) In general\nFor the purposes of developing, updating, and implementing mandatory horseracing racetrack safety rules for covered horses, covered persons, and covered horseraces under this Act, the RHSO shall establish a Racetrack Safety Committee.\n##### (b) Duties\nThe Committee shall\u2014\n**(1)**\ndraft proposed rules with respect to racetrack safety for each horse breed competing in covered horseraces, in accordance with subsection (d);\n**(2)**\nrecommend such proposed rules to the Board; and\n**(3)**\nfor purposes of making such recommendations, obtain testimony or other documented comment from racetrack superintendents from each affected breed of covered horses.\n##### (c) Membership\nThe Committee shall be composed of 7 members as follows:\n**(1) Regulatory members**\nThree such members shall be representatives of the equine industry, selected by the Board for their knowledge of racetrack safety, management, and maintenance.\n**(2) Industry members**\nFour such members shall be appointed as follows:\n**(A)**\nOne member shall be appointed by the United States Trotting Association.\n**(B)**\nOne member shall be appointed by the American Quarter Horse Association.\n**(C)**\nOne member shall be appointed by the National Horsemen\u2019s Benevolent and Protective Association.\n**(D)**\nOne member shall be a racetrack superintendent appointed by the Association of Racing Commissioners International.\n**(3) Term**\n**(A) In general**\nExcept as provided in subparagraph (B), the term of each member of the Committee shall not exceed 3 years. Such term is renewable for an indefinite number of terms.\n**(B) Initial term**\nFor purposes of staggering the terms of appointment, the members first appointed under paragraph (1) shall serve an initial term of 4 years.\n**(4) Chairperson**\nThe chairperson of the Committee shall be elected annually from among the members of the Committee by majority vote of the Committee.\n**(5) Conflicts of interest**\n**(A) In general**\nEach member of the Committee shall\u2014\n**(i)**\nbefore accepting appointment as a member of the Committee, disclose any potential conflict of interest; and\n**(ii)**\nnotify the full Board immediately upon engaging in any activity that the RHSO determines may be perceived as a conflict.\n**(B) Recusal required**\nA member of the Committee shall recuse himself or herself from discussion of any item at a meeting of the Committee if such discussion\u2014\n**(i)**\nrelates to the direct financial interest of any member of the Committee; and\n**(ii)**\ndoes not apply to all covered horses within a breed.\n**(6) Removal and ethics**\nThe Board may remove by majority vote a member of the Committee for\u2014\n**(A)**\nneglect of duty, unethical behavior, or malfeasance in office (including conduct determined by the Board to be injurious to the integrity of horseracing, such as contract violations and perjury); or\n**(B)**\nconviction of a violation of a Federal or State civil or criminal law related to horseracing.\n**(7) Quorum**\nIn order to consider at a meeting any rule being proposed to the Board, the Committee shall have in attendance at such a meeting (either in person or remotely) a majority of members of the Committee.\n##### (d) Process for adoption of rules\n**(1) In general**\nNot later than 90 days before the consideration of a proposed rule (or a modification to such a rule), the Committee shall hold an open meeting at which covered persons or their representatives may provide input.\n**(2) Notice of meeting**\nNot less than 45 days before the date on which the meeting referred to in paragraph (1) is to be held, the agenda, location, and date of such meeting shall\u2014\n**(A)**\nbe posted on the internet website of the RHSO;\n**(B)**\nsubmitted to the Racing Medication and Testing Consortium, the Harness Racing Medication Collaborative, and the American Quarter Horse Association Medication; and\n**(C)**\nprovided to any individual or entity requesting such information.\n**(3) Recording of input**\nIf any input from a covered person (or a representative of a covered person) is provided during a meeting referred to in paragraph (1), or provided in writing, such input shall be transcribed and recorded and made part of the record of the Committee.\n#### 303. Racetrack safety rules\n##### (a) Applicability\nThe racetrack safety rules established pursuant to section 101(c)(2) shall apply with respect to covered horses, covered persons, and covered horseraces.\n##### (b) Development of proposed rules\nIn developing proposed racetrack safety rules, the Committee shall\u2014\n**(1)**\nconsult with the State racing commissions; and\n**(2)**\ntake into consideration safety standards in use as of the date of the enactment of this Act, including\u2014\n**(A)**\nthe National Thoroughbred Racing Association Safety and Integrity Alliance Code of Standards; and\n**(B)**\nthe Association of Racing Commissioners International Model Rules.\n##### (c) Elements\nThe proposed rules referred to in subsection (b) shall include the following:\n**(1)**\nTraining and racing safety standards and protocols that\u2014\n**(A)**\ntake into account regional differences and the character of different racing facilities that may cause variations based on geographical and environmental differences;\n**(B)**\nare otherwise uniform within each breed of covered horses and unique to the performance model of each such breed;\n**(C)**\nare consistent with the humane treatment of covered horses; and\n**(D)**\nmay include lists of permitted and prohibited practices, methods, and track surfaces that affect safety.\n**(2)**\nTrack safety standards and protocols, uniform within each breed of covered horses, which may include rules governing\u2014\n**(A)**\nhuman and equine injury reporting and prevention; and\n**(B)**\noversight and movement of covered horses.\n**(3)**\nWith respect to the accreditation by the RHSO of racetracks within each breed of covered horses racing in covered horseraces\u2014\n**(A)**\nsafety, training, and performance standards of such accreditation;\n**(B)**\nthe process by which a racetrack within each breed may achieve and maintain such accreditation; and\n**(C)**\nthe penalties to be imposed by the RHSO or a State racing commission, as applicable, in the case of a racetrack not complying with such standards.\n**(4)**\nIn the case of a racetrack that does not, as of the date on which the rules established pursuant to section 101(c)(2) become effective, meet the standards for accreditation issued pursuant to paragraph (2), a process for the extension of provisional or interim accreditation for a period not to exceed 1 year\u2014\n**(A)**\nto a racetrack accredited by the National Thoroughbred Racing Association Safety and Integrity Alliance; and\n**(B)**\nthat is\u2014\n**(i)**\ndetermined at a meeting that takes place on a date during such 1-year period; and\n**(ii)**\nsanctioned by the United States Trotting Association or any entity empowered to perform such function on behalf of the American Quarter Horse Association.\n**(5)**\nThe establishment and process for maintaining a racing surface quality maintenance system that\u2014\n**(A)**\ntakes into account regional environmental differences and the character of different racing facilities, including differences among breeds; and\n**(B)**\nmay include requirements for\u2014\n**(i)**\ntrack surface design and consistency; and\n**(ii)**\nstandard operating procedures related to track surface monitoring and maintenance, such as standardized seasonal assessment, daily tracking, and measurement.\n**(6)**\nA process for injury and fatality analysis, which may include\u2014\n**(A)**\npre-training and post-training and race inspections;\n**(B)**\nuse of a veterinarian\u2019s list or a steward\u2019s list that meet standards specified under section 101(c)(11); and\n**(C)**\njockey, exercise rider, and driver concussion protocols.\n**(7)**\nRequirements relating to the conduct of safety and performance research.\n**(8)**\nRules relating to the establishment of educational programs.\nIV\nRule violations\n#### 401. Prohibited acts\nIn enforcing the rules issued under section 101(c), the Board shall prohibit the following:\n**(1)**\nCertain nontherapeutic medications and substances, including\u2014\n**(A)**\nthe administration to a covered horse of such a medication or substance;\n**(B)**\nthe presence of such a medication or substance in a blood, urine, or hair sample of a covered horse;\n**(C)**\nthe use or attempted use of such a medication or substance on a covered horse;\n**(D)**\npossession or attempted possession of such a medication or substance;\n**(E)**\ntrafficking or attempted trafficking in any such medication or substance; and\n**(F)**\nmanufacturing, producing, or formulating such a medication or substance.\n**(2)**\nCertain therapeutic medications and substances in quantitative amounts that exceed the irrelevant concentration present in a covered horse during a prohibited timeframe before or after the covered horse races in a covered horserace, including\u2014\n**(A)**\nthe administration to a covered horse of such a medication or substance;\n**(B)**\nthe presence of such a medication or substance in a blood, urine, or hair sample of a covered horse; and\n**(C)**\nthe use or attempted use of such a medication or substance on a covered horse.\n**(3)**\nRefusal or failure\u2014\n**(A)**\nwithout compelling justification, to submit a covered horse for collection of a blood, urine, or hair sample;\n**(B)**\nto cooperate with the RHSO, a State racing commission, or an agent thereof during any investigation;\n**(C)**\nto respond truthfully, to the best of a covered person\u2019s knowledge, to a question of the RHSO, a State racing commission, or an agent thereof with respect to any matter under the jurisdiction of such entity; and\n**(D)**\nin the case of a racetrack, to be in compliance with track safety standards.\n**(4)**\nTampering or attempted tampering with the application of the rules issued by or process adopted by the RHSO under section 101(c), including\u2014\n**(A)**\nthe intentional interference, or an attempt to interfere, with the RHSO, a State racing commission, or an agent thereof;\n**(B)**\nthe procurement or the provision of fraudulent information to the RHSO, a State racing commission, or an agent thereof; and\n**(C)**\nthe intimidation of, or an attempt to intimidate, a potential witness.\n**(5)**\nAssisting, encouraging, aiding, abetting, conspiring, covering up, or any other type of intentional complicity involving a violation of a rule issued under section 101(c) or the violation of a period of suspension or eligibility imposed on a covered person, covered horse, or covered horserace.\n**(6)**\nThreatening or seeking to intimidate a person with the intent of discouraging the person from the good faith reporting to the RHSO, a State racing commission, or an agent thereof, of information that relates to\u2014\n**(A)**\nan alleged violation of a rule issued by the RHSO under section 101(c); or\n**(B)**\nalleged noncompliance with such a rule.\n#### 402. Results management and disciplinary process\n##### (a) In general\nThe Board shall issue rules with respect to the disciplinary process for safety, performance, and scientific medication control rule violations, which may include the existing Model Rules of the Association of Racing Commissioners International.\n##### (b) Elements\nThe rules and processes issued under subsection (a) shall include the following:\n**(1)**\nThe undertaking of investigations at racetrack and nonracetrack facilities related to safety violations. In performing investigations, the RHSO and State racing commissions shall seek assistance as needed.\n**(2)**\nProcedures for\u2014\n**(A)**\ninvestigating, charging, and adjudicating violations; and\n**(B)**\nthe enforcement of administrative sanctions.\n**(3)**\nA schedule of administrative sanctions for violations.\n**(4)**\nDisciplinary hearings, which may include binding arbitration, mediation, administrative sanctions, and research.\n**(5)**\nManagement of violation results.\n**(6)**\nReferral for criminal law enforcement investigation.\n**(7)**\nProvisions for notification of safety, performance, and scientific medication control rule violations.\n**(8)**\nA process by which a noncompliant member State may be removed by unanimous vote of the remaining member States.\n**(9)**\nHearing procedures.\n**(10)**\nStandards for burden of proof.\n**(11)**\nPresumptions, including a rebuttable presumption of liability for covered persons who are trainers for any violations of the scientific medication control rules under section 101(c)(1).\n**(12)**\nEvidentiary rules.\n**(13)**\nAppeals.\n**(14)**\nGuidelines for confidentiality and public reporting of decisions.\n##### (c) Due process\nThe rules established under subsection (a) shall provide for adequate due process, including\u2014\n**(1)**\nimpartial hearing officers or tribunals commensurate with the seriousness of the alleged safety, performance, or scientific medication control rule violation and the possible civil sanctions for such violation;\n**(2)**\nthe right to counsel, to confront witnesses, and to have a transcribed record of the proceedings; and\n**(3)**\nthe right to have a decision rendered not later than 60 days after the date on which the hearing closes.\n#### 403. Administrative sanctions\n##### (a) In general\nThe Board shall\u2014\n**(1)**\nreview existing Model Rules of the Association of Racing Commissioners International applicable to a specific breed, imposing administrative sanctions against covered persons or covered horses for safety, performance, and medication control rule violations; and\n**(2)**\nsubject to subsection (b), issue and update rules relating to administrative sanctions referred to in paragraph (1).\n##### (b) Requirements\nThe rules established under subsection (a) shall\u2014\n**(1)**\ntake into account the unique aspects of horseracing;\n**(2)**\nbe designed to ensure fair and transparent horseraces; and\n**(3)**\ndeter safety, performance, and scientific medication control rule violations.\n##### (c) Severity\nThe administrative sanctions under subsection (a) may include\u2014\n**(1)**\nlifetime bans from horseracing, disgorgement of purses, monetary fines and penalties, and changes to the order of finish in covered races; and\n**(2)**\nwith respect to scientific medication control rule violators, an opportunity to reduce the applicable administrative sanctions that is comparable to the opportunity provided by the Protocol for Olympic Movement Testing of the United States Medication Agency.\nV\nGeneral provisions\n#### 501. Effective dates\n##### (a) RHSO\nExcept as provided in subsections (b) and (c), the provisions of this Act shall take effect on the later of\u2014\n**(1)**\nthe date that is 2 years after the date of the enactment of this Act; or\n**(2)**\nthe date on which 2 or more States have entered into the interstate compact pursuant to section 4.\n##### (b) Exceptions\nSubsections (c), (d), and (e) of section 101, and titles II, III, and IV of this Act shall take effect 90 days after the date described in subsection (a).\n##### (c) Immediate upon enactment\nSections 1, 2, and 3 and subsections (a) and (b) of section 4 shall take effect immediately upon the date of the enactment of this Act.",
      "versionDate": "2025-05-14",
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
        "actionDate": "2025-05-14",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1770",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Racehorse Health and Safety Act of 2025",
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
            "name": "Advisory bodies",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "Athletes",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "Business ethics",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "Contracts and agency",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "Gambling",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "Mammals",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "Professional sports",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "Sports and recreation facilities",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-29T14:56:31Z"
          },
          {
            "name": "Veterinary medicine and animal diseases",
            "updateDate": "2025-07-29T14:56:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Sports and Recreation",
        "updateDate": "2025-06-03T19:12:55Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3378ih.xml"
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
      "title": "Racehorse Health and Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-23T10:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Racehorse Health and Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-23T10:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect the health and welfare of covered horses and improve the integrity and safety of horseracing by authorizing States to enter into an interstate compact to develop and enforce scientific medication control rules and racetrack safety rules that are uniform for each equine breed, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-23T10:18:16Z"
    }
  ]
}
```
