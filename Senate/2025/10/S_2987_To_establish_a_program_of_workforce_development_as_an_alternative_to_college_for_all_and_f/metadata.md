# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2987?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2987
- Title: American Workforce Act
- Congress: 119
- Bill type: S
- Bill number: 2987
- Origin chamber: Senate
- Introduced date: 2025-10-08
- Update date: 2025-12-08T15:06:49Z
- Update date including text: 2025-12-08T15:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-08: Introduced in Senate
- 2025-10-08 - IntroReferral: Introduced in Senate
- 2025-10-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-10-08: Introduced in Senate

## Actions

- 2025-10-08 - IntroReferral: Introduced in Senate
- 2025-10-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-08",
    "latestAction": {
      "actionDate": "2025-10-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2987",
    "number": "2987",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "American Workforce Act",
    "type": "S",
    "updateDate": "2025-12-08T15:06:49Z",
    "updateDateIncludingText": "2025-12-08T15:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-08",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-08",
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
          "date": "2025-10-08T17:44:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2987is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2987\nIN THE SENATE OF THE UNITED STATES\nOctober 8, 2025 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish a program of workforce development as an alternative to college for all, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Workforce Act .\n#### 2. Definitions\nIn this Act:\n**(1) American workforce contract**\nThe term American workforce contract means a contract approved by the Director, and entered into by an employer and a prospective trainee under section 4(b)(6).\n**(2) American workforce program**\nThe term American workforce program means a program established under section 4(a) that provides, for each participating trainee, a paid, full-time position in which the trainee is engaged in\u2014\n**(A)**\nstructured on-the-job work, as specified by the American workforce contract involved; and\n**(B)**\neducational workforce training described in section 4(f), as specified by the American workforce contract.\n**(3) Competency-based credential**\nThe term competency-based credential means a credential awarded on the basis of a performance-based test that\u2014\n**(A)**\nis taken to demonstrate proficiency in knowledge and abilities essential to the industry or occupation; and\n**(B)**\ndoes not place restrictions on how, when, or where the test taker studied and acquired the knowledge and abilities.\n**(4) Director**\nThe term Director means the Director of the American Workforce Division, appointed under section 3(b).\n**(5) Employer**\nThe term employer means a for-profit employer, as defined in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ), other than a public agency, as defined in that section.\n**(6) Prospective trainee**\nThe term prospective trainee means an individual who\u2014\n**(A)**\napplies to an employer to enter into an American workforce contract; and\n**(B)**\non the date of application, meets the requirements of paragraph (8)(A).\n**(7) Secretary**\nThe term Secretary means the Secretary of Commerce.\n**(8) Trainee**\nThe term trainee means any individual who\u2014\n**(A)**\non the date of application to an employer to enter into an American workforce contract\u2014\n**(i)**\nis a United States citizen;\n**(ii)**\nhas a high school diploma or its generally recognized equivalent; and\n**(iii)**\nhas not earned a bachelor\u2019s or higher degree, such as a master\u2019s or doctoral degree; and\n**(B)**\nentered into an American workforce contract, which is still in effect, with the employer.\n**(9) Workforce project**\nThe term workforce project means a project carried out under an American workforce contract as part of the American workforce program.\n#### 3. Establishment of American Workforce Division\n##### (a) Establishment\nThere is established in the Economic Development Administration of the Department of Commerce an American Workforce Division that administers, subject to the availability of appropriations, the American workforce program established under section 4(a).\n##### (b) Director\n**(1) In general**\nThe American Workforce Division shall be headed and administered, in accordance with the provisions of this Act, by a Director. The Director shall be appointed by the President, by and with the advice and consent of the Senate. The Director shall report directly to the Secretary and shall perform, in addition to any functions specified in law for or required to be delegated to such officer, such additional functions as the Secretary may prescribe.\n**(2) Qualifications**\nThe Director shall have significant experience in the private sector.\n**(3) Authority before confirmation**\nUntil the initial appointment of an individual to the position of Director, by and with the advice and consent of the Senate, and, thereafter, if the individual serving as the Director dies, resigns, or is otherwise unable to perform the functions and duties of the office of the Director, the Secretary of Commerce shall designate an officer or employee of the Department of Commerce to perform the functions and duties of the Director under this Act temporarily in an acting capacity.\n##### (c) Responsibilities of the Director\nThe Director shall be responsible for each of the following:\n**(1)**\nReviewing, and approving or disapproving, each proposed American workforce contract received by the Director not later than 1 month after the date of receipt of the proposed contract.\n**(2)**\n**(A)**\nMaintaining records of American workforce contracts and ensuring compliance with the contracts.\n**(B)**\nPublishing a standardized template for American workforce contracts, which template shall not exceed 3 pages, and shall be used by prospective trainees and employers to draft a proposed American workforce contract to submit to the Director for review and approval.\n**(3)**\nIn accordance with subsection (d), receiving complaints, carrying out investigations, and taking disciplinary and corrective action.\n**(4)**\nIn accordance with subsection (e), making determinations and taking disciplinary and corrective action.\n**(5)**\nCoordinating activities with State governments and local governments to\u2014\n**(A)**\npublicize the opportunity to receive workforce education subsidies for workforce projects, with employers in high-wage, high-demand industries and occupations; and\n**(B)**\nencourage employers to recruit students from secondary schools to participate in the workforce projects.\n**(6)**\nDeveloping and maintaining a comprehensive, publicly accessible, and user-friendly website to allow employers from each State to simply indicate their demand for workers in their industry or occupation, post it online, and accept applications for training from prospective trainees and ensures prospective trainees can easily search and compare options.\n**(7)**\nPreparing 5- and 10-year reports under section 6, and submitting the reports to Congress.\n**(8)**\n**(A)**\nCollecting, on an ongoing basis, up-to-date contact information, including an email, phone number, and mailing address, for each employer participating in a workforce project in the American workforce program.\n**(B)**\nAnnually collecting the following information about the American workforce program:\n**(i)**\nThe total number of new and continuing trainees training in each workforce project under an American workforce contract.\n**(ii)**\nThe annual completion rate for trainees, calculated by comparing the number of trainees in a designated American workforce program cohort who successfully completed a workforce project with an employer and were hired as full-time regular employees by the same employer, with the number of trainees in that cohort who began participating in a workforce project.\n**(iii)**\nThe annual rate of trainees who successfully completed a workforce project with an employer but were not hired as full-time regular employees by the same employer compared with the number of trainees who began participating in a workforce project.\n**(iv)**\nThe median length of time for workforce project completion.\n**(v)**\nA survey conducted by the Director, based on a random sample and designed to generate statistically significant results, to estimate the post-American workforce program employment retention rate for former trainees, calculated 1 and 2 years after completion of a workforce project, broken down by\u2014\n**(I)**\nformer trainees who are employed by the employer with whom they completed their workforce project;\n**(II)**\nformer trainees employed in the same industry or occupation as the industry or occupation in which they completed that workforce project, but by a different employer; and\n**(III)**\nformer trainees who are employed, but in an industry or occupation that is not the industry or occupation described in subclause (II).\n**(vi)**\nThe credentials attained by trainees through the American workforce program, broken down by type (such as competency-based credentials, certifications, and licenses) and the number of such credentials attained.\n**(vii)**\nThe annualized average earnings of former trainees, calculated over a significant time period after completion of a workforce project.\n**(viii)**\nMedian and mean workforce education subsidy provided per trainee.\n**(ix)**\nBasic demographic information, such as age, sex, and area of residence, on trainees.\n##### (d) Whistleblower complaints\n**(1) Complaint**\nA trainee (including an employee participating as a trainee) in a workforce project may file a complaint with the Director alleging that the employer involved is not complying with the terms of the American workforce contract involved.\n**(2) Preliminary determination**\nThe Director shall begin an investigation into the complaint within 1 month after the date of receipt of the complaint. Not later than 90 days after the beginning of the investigation, if the Director determines that there is clear and convincing evidence that the complaint is valid, the Director shall make a preliminary determination on disciplinary or corrective action.\n**(3) Notice and opportunity to respond**\nIf the Director makes a preliminary determination under paragraph (2) of noncompliance, the Director shall provide the employer with reasonable notice and opportunity to respond to the preliminary determination.\n**(4) Disciplinary or corrective action**\nDisciplinary or corrective action under this subsection may consist of\u2014\n**(A)**\nissuing to the employer a warning or temporary suspension, of not more than 5 years, from participation in the American workforce program; and\n**(B)**\nassessing a civil penalty against the employer of not more than the amount of funds received by the employer through workforce education subsidies during the past 2 years.\n**(5) Appeal**\nIf the Director so determines that the appropriate disciplinary or corrective action includes a suspension, the employer shall have 90 days to appeal the validity of the disciplinary or corrective action to the Director, with mandatory review by the Secretary of Commerce.\n**(6) Final determination**\nAfter such mandatory review, the Director shall make a final determination on the validity and on the appropriate disciplinary or corrective action, contingent on approval from the Secretary of Commerce.\n##### (e) Noncompliance determinations\n**(1) Accountability**\nThe Director\u2014\n**(A)**\nmay, in order to make a preliminary determination about whether there is clear and convincing evidence that employers participating in workforce projects are complying with the terms of the American workforce contracts involved and meeting the requirements of the American workforce program\u2014\n**(i)**\ndemand and review relevant materials from the employers; and\n**(ii)**\nconduct random, periodic compliance reviews of workforce projects; and\n**(B)**\nshall review information in public disclosure documents submitted under section 4(g), including reviewing completion rates provided under section 4(g)(2)(A) to make a preliminary determination about whether there is clear and convincing evidence that employers are participating in a workforce project with a completion rate below 25 percent over 4 years.\n**(2) Notice and opportunity to respond**\nIf the Director makes a preliminary determination under paragraph (1) of noncompliance or participation in a workforce project described in paragraph (1)(B), the Director shall provide the employer with reasonable notice and opportunity to respond to the preliminary determination.\n**(3) Warning or civil penalty**\n**(A) In general**\nThe Director may, at the discretion of the Director, issue a warning to or assess a civil penalty against an employer if, after carrying out paragraph (2), the Director makes a final determination that there is clear and convincing evidence that\u2014\n**(i)**\nthe employer is participating in a workforce project described in paragraph (1)(B); or\n**(ii)**\nthe employer is violating the terms of an American workforce contract or the requirements of the American workforce program.\n**(B) Calculation of civil penalty**\nA civil penalty assessed under subparagraph (A) shall be in an amount that is not more than the amount of funds received by the employer through workforce education subsidies during the past 2 years.\n**(4) Suspension**\nThe Director may, at the discretion of the Director, temporarily suspend an employer from the American workforce program for not more than 5 years if, after carrying out paragraph (2), the Director makes a final determination that there is clear and convincing evidence that\u2014\n**(A)**\nthe employer is participating in a workforce project described in paragraph (1)(B); or\n**(B)**\nthe employer is consistently or egregiously violating the terms of an American workforce contract or the requirements of the American workforce program.\n##### (f) Interference with proceedings or inquiries\nIt shall be unlawful for any employer to discharge or in any other manner discriminate against any trainee because such trainee\u2014\n**(1)**\nhas filed any complaint under subsection (d);\n**(2)**\nhas given, or is about to give, any information in connection with any inquiry or proceeding under this Act (including any inquiry or proceeding under subsection (d) or (e)); or\n**(3)**\nhas testified, or is about to testify, in any such inquiry or proceeding under this Act.\n#### 4. American workforce program\n##### (a) In general\nThe Director shall establish, subject to the availability of appropriations, an American workforce program, and carry out the program by supporting workforce projects with American workforce contracts, distributing workforce education subsidies and bonuses for hiring, and providing technical and administrative support.\n##### (b) Contracts\n**(1) In general**\nTo be eligible to receive a workforce education subsidy, bonus for hiring, or technical support under this Act for a workforce project, an employer and prospective trainee shall prepare a proposed American workforce contract under this subsection, based on the standardized template created by the Director, and submit the proposed contract to the Director for approval. The page limitation placed on the Director\u2019s template under subsection (c)(2)(B) shall not apply to the proposed American workforce contract prepared by the trainee and employer or the final American workforce contract.\n**(2) Provisions**\nThe proposed contract between an individual who is a prospective trainee and the employer shall include each of the following:\n**(A) Parties involved**\nThe name of the individual, the employer participating in the workforce project, and any third-party entity with whom the employer is partnering to provide the educational workforce training component of the project (referred to in this Act as a third-party training entity ).\n**(B) Term**\nThe term, which shall not be shorter than 6 weeks, of the workforce project (including specifying total time to completion) and the amount of time the individual will spend in structured on-the-job work and in educational workforce training (including specifying hours per week, month, and year).\n**(C) Work and training plan**\nA detailed overview of the curriculum for the educational workforce training, a description of the structured on-the-job work, and a description of skills and competencies to be attained through the workforce project.\n**(D) Written workforce agreement**\nA proposed written workforce agreement for the individual that outlines each of the following:\n**(i)**\nThe terms and conditions of the individual\u2019s work and training.\n**(ii)**\nThe wage or salary an individual will receive as a trainee and the estimated starting wage or salary, in accordance with the requirements of subsection (e), for each position, described in subsection (e), that the individual is receiving training for and being considered for.\n**(iii)**\nThe technical and professional standards that will be met by the individual for successful completion of the workforce project.\n**(iv)**\n**(I)**\nExpected long-term and short-term outcomes for the individual, including qualifying positions of the type the individual is being trained for at the employer and third-party training entities (if applicable), and the estimated wage or salary range for the occupation the individual is being trained for.\n**(II)**\nThe projected growth of the relevant industry or occupation, if information on that growth is available to the employer or obtainable with such technical assistance as the Director may provide.\n**(v)**\nThe circumstances under which the individual's wage or salary will increase during the workforce project.\n**(vi)**\nA description of voluntary mentorship opportunities that may be available.\n**(vii)**\nA disclosure of the amount of the payment from a workforce education subsidy that the employer will receive per payment period from the Director and any costs or expenses that will be charged to the trainee or could reasonably be expected to be charged to the trainee.\n**(viii)**\nIf 1 or more competency-based credentials exist for the relevant industry or occupation, a description of the top 1 to 3 such credentials that the individual might earn on successful completion of the workforce project.\n**(ix)**\nIf no competency-based credential exists for the industry or occupation, a description of any other credential, such as a certification or license, that the individual might earn in the relevant industry or occupation due to experience in the workforce project.\n**(3) Review of credentials**\n**(A) In general**\nNot later than 1 month after receiving for review a proposed American workforce contract, the Director shall review the credentials specified in the contract under clause (viii) or (ix) of paragraph (2)(D) and may note any additional credentials the Director determines a trainee should consider earning. Any such credential noted by the Director shall be described in the contract.\n**(B) Rules of construction**\nNothing in this section shall be construed to\u2014\n**(i)**\npermit the Director to reject an entire proposed American workforce contract solely because of the Director\u2019s view of a credential described in the proposed contract; or\n**(ii)**\nrequire a trainee to agree to earn a competency-based credential or another credential specified in the American workforce contract, as a condition of using funding provided through a workforce education subsidy under this section.\n**(4) Review of contract**\n**(A) In general**\nNot later than 1 month after receiving a proposed American workforce contract, the Director shall review, and approve or disapprove, the proposed contract (including conducting the review under paragraph (3) and determining whether the employer has provided the appropriate written disclosure document under subsection (g)).\n**(B) Presumption of approval**\nThere shall be a presumption of approval for a proposed American workforce contract, in that such a contract that has not been disapproved by the Director shall be considered to be approved on the 32nd day after the date of that receipt. A proposed American workforce contract may only be disapproved for failing to meet the requirements of this Act. If such a proposed contract is disapproved, the Director shall describe the reason, with a citation to the requirement not met, and a recommendation for how the proposed contract shall be amended to comply with this Act.\n**(5) Review of resubmission**\nIf an employer and individual submit a proposed contract under paragraph (1) that is not approved under paragraph (4), the employer and individual may resubmit the amended proposed contract for review as described in paragraph (4). For purposes of paragraph (4)(B), the reference to the date of receipt shall be considered to be the date of receipt of the resubmitted proposed contract.\n**(6) Entry into contract**\nOnce a proposed contract has been approved under paragraph (4) or (5), the individual and employer involved may enter into the contract and initiate the workforce project.\n**(7) Current employees**\nA participating employer may enter into an American workforce contract with, and enroll into their workforce project, an employee who holds a position with the employer if the employer agrees to\u2014\n**(A)**\nmaintain employment for that employee at the employee's wage or salary on the date of enrollment, or a higher wage or salary; and\n**(B)**\nprovide an increase to the employee's annual wage or salary, if the employee successfully completes the workforce project, that is equal to not less than 25 percent of the value of the educational workforce subsidy provided for the project.\n##### (c) Workforce education subsidies\nNot earlier than the date on which an individual and employer enter into an American workforce contract approved by the Director, the Director shall provide an education workforce subsidy to the employer operating the workforce project. Each of the following rules shall apply to the workforce education subsidy and the trainee involved and employer:\n**(1)**\nThe workforce education subsidy may be used to subsidize the cost of educational workforce training (onsite or with an eligible third-party training entity), not the wage or salary of the trainee.\n**(2)**\nThe employer shall pay, at regular intervals, the trainee a wage or salary at a rate that is not less than the higher of\u2014\n**(A)**\nthe rate in effect under section 6(a)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(a)(1) ); or\n**(B)**\nthe rate in effect under a State or local minimum wage law that applies to the State or locality in which the trainee is engaged in labor or service for the employer.\n**(3)**\nThe employer shall provide a working environment for the trainee that meets all applicable Federal, State, and local safety laws and regulations.\n**(4)**\nNeither the Director or any other officer or employee of the executive branch of the Federal Government may make the workforce education subsidy contingent on any requirement not specified in this Act.\n**(5)**\nThe employer shall not currently be suspended from participating in workforce projects subsection (d) or (e) of section 3.\n**(6)**\nParticipation in the workforce project involved shall not make the employer subject to the jurisdiction of the Office of Federal Contract Compliance Programs of the Department of Labor as a Federal contractor, including not being subject to Executive Order 11246.\n**(7)**\nThe employer shall comply with all applicable Federal, State, and local statutory laws pertaining to nondiscrimination in employment.\n**(8)**\nThe workforce education subsidy may not be used for\u2014\n**(A)**\ndiversity, equity, and inclusion training, or culturally responsive training; or\n**(B)**\nany other training that may violate\u2014\n**(i)**\ntitle VII of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e et seq. ), by contributing to a hostile work environment; or\n**(ii)**\ntitle VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ), including its prohibition, on the grounds of race, color, or national origin, of discrimination under any program or activity receiving Federal financial assistance.\n**(9)**\nThe workforce education subsidy may not be used for political spending, electioneering, or any other purpose that is not directly related to educational workforce training.\n**(10)**\nThe Director shall make payments from the workforce education subsidy to the employer\u2014\n**(A)**\nin even installments, following the end of each financial quarter in which the training and on-the-job work specified in the American workforce contract have been completed by the trainee;\n**(B)**\nin sums of not more than $1,500 per month; and\n**(C)**\nfor a total amount of not more than $9,000, as determined on the basis of the American workforce contract.\n**(11)**\nA State government or locality may supplement the workforce education subsidy with additional funds, if the State government or locality does not make accepting such funds or any conditions attached to the funds a requirement of accepting Federal funding.\n**(12)**\nIf the trainee chooses to leave a workforce project after the halfway point of the term of the workforce project, the trainee will be considered to have used the entirety of one of the workforce education subsidies through which the trainee is eligible to receive educational workforce training.\n**(13)**\nIf the employer ceases operations, the trainee shall not be held at fault, meaning that the trainee may receive educational workforce training, funded with the full value of the workforce education subsidy, for a workforce project with a subsequent eligible employer, notwithstanding the time requirement of paragraph (15).\n**(14)**\nThe maximum period of time for which an employer (including a subsequent employer described in paragraph (13)) may receive payments, provided through the workforce education subsidy for education workforce training of a trainee, shall be 3 years.\n**(15)**\n**(A)**\nIn order for a trainee to enroll in a workforce project with a subsequent eligible employer through a second or third such subsidy, the trainee shall receive the related educational workforce training not less than 1 year after the conclusion of the trainee\u2019s most recent training through a workforce education subsidy.\n**(B)**\nThe time limit described in subparagraph (A) shall not apply to a trainee who\u2014\n**(i)**\ncompleted a workforce project with, but was not hired by, an employer; and\n**(ii)**\nseeks to receive such training through a workforce project with the trainee's next employer.\n**(16)**\nThe employer shall meet the applicable minimum ratios specified under section 5(d).\n**(17)**\nThe employer shall use E-Verify for each trainee enrolled and individual hired or employed during the period for which the employer accepts funds through a subsidy provided under this Act, regardless of whether the trainee or individual participated in a workforce project.\n**(18)**\nThe employer shall publish a public disclosure document, consistent with subsection (g).\n##### (d) Bonus for hiring\n**(1) In general**\nIf an trainee, on completion of a workforce project, is hired as a full-time, regular employee of the employer participating in the workforce project, with a wage or salary described in subsection (e)(1), the employer shall receive a bonus of $1,000 (in addition to any payment received through a workforce education subsidy). The Director shall pay the bonus not sooner than the date that is 6 months after the trainee is so hired.\n**(2) Rules**\nSubject to paragraph (3), each of the rules described in paragraphs (5), (6), (8), (9), (11), (16), (17), and (18) shall apply to the bonus, and the trainee hired and employer, except that a reference in those paragraphs\u2014\n**(A)**\nto a workforce educational subsidy shall be considered to be a reference to the bonus; and\n**(B)**\nto a trainee shall be considered to be a reference to the trainee hired.\n**(3) Use of bonus**\nAn employer who receives a bonus under this subsection may use the bonus funds to supplement the wage or salary of the trainee hired.\n##### (e) Position for the trainee\n**(1) Wages**\nAn employer participating in a workforce project shall be training each trainee and considering each trainee for a position that would have an annual wage or salary of not less than 80 percent of\u2014\n**(A)**\nthe annual median household income of the county in which the job involved is located (or an hourly wage based on that income and adjusted for a 2,080-hour annual work period), as determined by the 5-year estimates of the American Community Survey of the Bureau of the Census; or\n**(B)**\nif the county involved is not in a micropolitan or metropolitan area, the annual median household income for the nearest micropolitan or metropolitan area, as determined by the Bureau of the Census.\n**(2) Remote work**\nAn employer providing remote work for a trainee or employee (in a position referred to in paragraph (1)) shall use the trainee's or employee's location when determining an applicable wage or salary under this Act. Such a trainee or employee engaging in remote work shall live in the United States and file Federal income taxes in the United States.\n**(3) Work**\nAn employer participating in a workforce project shall provide structured on-the-job work for each trainee in a job that requires specialized knowledge and experience and involves the performance of complex tasks, to prepare the trainee for a position referred to in paragraph (1).\n##### (f) Educational workforce training\nIn providing for educational workforce training through a workforce project to a trainee, an employer shall meet each of the following requirements:\n**(1) Skills**\nThe employer shall ensure that the training is designed in a manner that enables trainees to obtain and demonstrate competency and obtain progressively advancing and portable skills that are necessary for the industry or occupation involved.\n**(2) Partners**\nThe employer may partner with any of the following eligible third-party training entities, and may pay such a third-party training entity with funds from a workforce education subsidy, in order to provide the training for trainees in the workforce project:\n**(A)**\nA trade, industry, or employer group or association.\n**(B)**\nA corporation or other related organized entity.\n**(C)**\nAn educational institution, such as an institution of higher education, including a community college, or a secondary school.\n**(D)**\nA State or local government agency or entity.\n**(E)**\nA nonprofit organization.\n**(F)**\nA union.\n**(G)**\nA joint labor-management organization.\n**(H)**\nA certification or accreditation body or entity for an industry or occupation.\n**(I)**\nA consortium or partnership of entities such as entities described in any of subparagraphs (A) through (H).\n**(3) Credentials**\nThe employer shall ensure that, in conjunction with that training, the trainee shall be made aware of any widely used competency-based credentials in the employer\u2019s industry or occupation. If a competency-based credential is described in the trainee\u2019s American workforce contract, the employer shall not forbid the trainee, or provide a disincentive to discourage the trainee, from taking a related competency-based credential exam.\n**(4) Definitions**\nIn this subsection:\n**(A) Community college**\nThe term community college means an institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )) at which the highest degree that is predominantly awarded to students is an associate degree.\n**(B) Institution of higher education**\nThe term institution of higher education has the meaning given that term in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ).\n##### (g) Public disclosure document\n**(1) In general**\nThe Director shall require each participating employer seeking approval for a proposed American workforce contract to provide a written disclosure document, about the employer\u2019s workforce project, that includes each of the following statistics and information:\n**(A)**\nThe total expected cost, if any, for a trainee during or at the completion of the workforce project, such as the cost of fees for a certification examination.\n**(B)**\nThe expected wage or salary for the position of the employer that the workforce project is designed to train for.\n**(C)**\nThe length of the workforce project.\n**(D)**\nThe total expected number of hours of structured on-the-job work per week, and of hours of educational workforce training per week, for a trainee during the workforce project.\n**(E)**\nThe total expected number of hours for which a trainee will be paid during the course of the workforce project.\n**(F)**\nThe hourly wage or salary for a trainee during the course of the workforce project.\n**(G)**\nInformation stating any certifications, licenses, or other credentials that trainees in the workforce project might earn on successful completion of the workforce project.\n**(2) Additional public disclosure for established workforce projects**\nThree years after an employer has completed a workforce project, the Director shall require the employer to include, in its written disclosure document, documentation that includes each of the following statistics:\n**(A)**\nThe completion rate for trainees in a workforce project with the employer, calculated over the previous 3 years.\n**(B)**\nThe percentage of trainees that completed a workforce project with, and were hired by, the employer participating in the project, calculated over the previous 2 years.\n**(C)**\nThe average wage or salary of currently employed (as of the date of collection of the wage or salary information) trainees who completed a workforce project, during the last 3 years, presented in a way that does not reveal individually identifiable wage or salary information.\n**(3) Availability**\nThe disclosure documents described in paragraphs (1) and (2) shall be made available to the general public by the Director.\n#### 5. General provisions\n##### (a) Workforce project after payment period\nNothing in this Act shall be construed to require a workforce project to end after 3 years, the maximum period of time for which an employer may receive payments through a workforce education subsidy for a trainee, if the employer pays for the cost of the associated educational workforce training for the portion of the project after that maximum period.\n##### (b) Relationship to other projects\nIndividuals who do not meet the criteria described in section 2(8)(A) may participate in projects, structured like workforce projects described in this Act, if the employer or an organization other than the Federal Government provides the necessary funding for wages or salaries, and educational workforce training.\n##### (c) Third-Party training entity\nThe Secretary may not pressure, or provide an incentive or disincentive to, an employer to choose 1 eligible entity over another as a third-party training entity. The choice of a third-party training entity shall be made entirely by an employer.\n##### (d) Regulations on Ratios\n**(1) Ratios**\nBeginning 5 years after the date of enactment of this Act, the Secretary may issue regulations that specify 1 or more ratios, based on categories of jobs as defined by the Secretary, between the number of job openings for a prospective position, as a full-time regular employee, related to a workforce project, and the number of trainees in that project.\n**(2) Objectives**\nIn issuing the regulations, the Secretary shall consider the following objectives:\n**(A)**\nAssuring that a trainee has a reasonable opportunity to be hired as a full-time, regular employee by the employer participating in the workforce project.\n**(B)**\nEnsuring that an employer\u2019s hiring discretion is not limited in a manner that would incentivize an employer to lower standards for a position that is particularly difficult or dangerous.\n##### (e) Criteria\nThe Secretary may establish criteria regarding technical matters and provide technical assistance for meeting the requirements of this Act.\n##### (f) Required regulations\nRegulations required under this Act shall be issued by the corresponding officer within 3 months after the date of enactment of this Act, except as otherwise specified.\n#### 6. Evaluation reports and sunset\n##### (a) 5-Year report\nNot later than 5 years after the date of enactment of this Act, the Secretary shall prepare and submit to Congress a report including each of the following information, analysis, and recommendations:\n**(1)**\nA comparison of the American workforce program to other major career and technical education or apprenticeship programs administered by the Federal Government, including the registered apprenticeship program carried out under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ), and to the workforce investment activity programs administered under the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ), on the basis of\u2014\n**(A)**\nthe completion rate of participants in each program;\n**(B)**\nthe average earnings of participants in each program, calculated during\u2014\n**(i)**\nthe related career and technical education, apprenticeship, workforce investment, or workforce project; and\n**(ii)**\nthe period beginning 3 years and ending 5 years after the participants complete the related career and technical education, apprenticeship, workforce investment, or workforce project;\n**(C)**\nthe percentages obtained by dividing\u2014\n**(i)**\nthe number of participants and rate of growth in participants for each program; by\n**(ii)**\nthe number of individuals in the labor force and the rate of growth of the labor force, respectively;\n**(D)**\nthe level of direct engagement by employers with, and satisfaction from employers in, each program; and\n**(E)**\nthe diversity of the industries and occupations of the employers who utilize each program.\n**(2)**\nThe overall completion rate for the American workforce program, the completion rate for workforce projects by industry and occupation, the number of trainees who dropped out of the program entirely, broken down by industry and occupation, and the number who left a workforce project for another workforce project.\n**(3)**\nThe results of a survey, based on a random sample and designed to generate statistically significant results, of trainees who have participated in the program.\n**(4)**\nThe results of a survey, based on a random sample and designed to generate statistically significant results, of employers who have participated in the program, including a breakdown by size of employer.\n**(5)**\nData collected under section 3(c)(8)(B).\n**(6)**\nInformation and technical criteria, other regulations, and guidance issued by the Secretary to administer the program.\n**(7)**\nInformation on the rate of uptake by individuals and employers that are eligible to participate in the program, and recommendations for ways in which this rate of uptake could be improved.\n**(8)**\nAnalysis on considerations for Congress about expanding the use of intermediary institutions, such as nonprofits, to better advertise the program.\n**(9)**\n**(A)**\nAnalysis on considerations for Congress in expanding eligibility of the program for United States citizens who do not have a high school diploma or its generally recognized equivalent.\n**(B)**\nAnalysis on considerations for Congress in encouraging trainees to obtain industry-recognized credentials that help to provide recognition of a portable skill.\n**(C)**\nAnalysis on considerations for Congress on the effect and necessity of regulations described in section 5(d).\n**(D)**\nRecommendations for Congress on encouraging participation in workforce projects by small businesses.\n**(10)**\nAnalysis on considerations for Congress about how to effectively engage high school students in a workforce project, including\u2014\n**(A)**\nhow coursework for a technical high school, or career and technical education in a high school, could qualify towards the completion of a workforce project; and\n**(B)**\nhow time spent in structured on-the-job work or educational workforce training for a workforce project could count towards high school graduation.\n**(11)**\nRecommendations for improvement and reauthorization of the American workforce program by Congress.\n##### (b) 10-Year report\nNot later than 10 years after the date of enactment of this Act, the Secretary shall prepare and submit to Congress a report containing the information, analysis, and recommendations described in subsection (a).\n##### (c) Sunset\nThe program authorized by section 4 and the position of the Director shall cease to exist on the earlier of\u2014\n**(1)**\nthe date on which the Director submits the report described in subsection (b) to Congress; or\n**(2)**\nthe day that is 11 years after the date of enactment of this Act.",
      "versionDate": "2025-10-08",
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
        "actionDate": "2025-10-17",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "5779",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "American Workforce Act",
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
        "name": "Labor and Employment",
        "updateDate": "2025-12-08T15:06:49Z"
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
      "date": "2025-10-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2987is.xml"
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
      "title": "American Workforce Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-21T11:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Workforce Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a program of workforce development as an alternative to college for all, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-21T11:18:14Z"
    }
  ]
}
```
