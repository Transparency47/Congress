# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3547?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3547
- Title: Part-Time Worker Bill of Rights Act
- Congress: 119
- Bill type: S
- Bill number: 3547
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-03-11T14:10:16Z
- Update date including text: 2026-03-11T14:10:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3547",
    "number": "3547",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Part-Time Worker Bill of Rights Act",
    "type": "S",
    "updateDate": "2026-03-11T14:10:16Z",
    "updateDateIncludingText": "2026-03-11T14:10:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T21:54:05Z",
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
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "RI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-17",
      "state": "VT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "WA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3547is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3547\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Ms. Warren (for herself, Mr. Booker , Mr. Markey , Mr. Padilla , Mr. Whitehouse , Mr. Sanders , Mrs. Murray , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo extend protections to part-time workers in the areas of family and medical leave and to ensure equitable treatment in the workplace.\n#### 1. Short title\nThis Act may be cited as the Part-Time Worker Bill of Rights Act .\n#### 2. Table of contents\nThe table of contents is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nTITLE I\u2014Expanding Access to Benefits for Part-time Workers\nSec. 101. Elimination of hours of service requirement for FMLA leave.\nTITLE II\u2014Ensuring Fair Treatment for Part-Time and Temporary Workers\nSec. 201. Definitions.\nSec. 202. Elimination of discrimination on the basis of hours worked.\nSec. 203. Offer of work to existing employees.\nSec. 204. Prohibited acts.\nSec. 205. Remedies and enforcement.\nSec. 206. Regulations.\nI\nExpanding Access to Benefits for Part-time Workers\n#### 101. Elimination of hours of service requirement for FMLA leave\n##### (a) Amendment\nSection 101(2)(A) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611(2)(A) ) is amended to read as follows:\n(A) In general The term eligible employee means an employee who has been employed for at least 90 days by the employer with respect to whom leave is requested under section 102. .\n##### (b) Amendments to related statutes\n**(1) Congressional Accountability Act of 1995**\nSection 202(a)(2)(B) of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1312(a)(2)(B) ) is amended by striking 12 months and for at least 1,250 hours of employment during the previous 12 months and inserting at least 90 days .\n**(2) Title 3, United States Code**\nSection 412(a)(2)(B) of title 3, United States Code, is amended by striking 12 months and for at least 1,250 hours of employment during the previous 12 months and inserting at least 90 days .\n**(3) Title 5, United States Code**\nChapter 63 of title 5, United States Code, is amended\u2014\n**(A)**\nin section 6381(1)(B), by striking at least 12 months of service and inserting at least 90 days of service ; and\n**(B)**\nin section 6382(d)(2)(E), by striking at least 12 months of service and inserting at least 90 days of service .\n##### (c) Conforming amendments\n**(1)**\nSection 101(2) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611(2) ) is amended\u2014\n**(A)**\nby striking subparagraphs (C) and (D); and\n**(B)**\nby redesignating subparagraph (E) as subparagraph (C).\n**(2)**\nSection 102(a) of such Act ( 29 U.S.C. 2612(a) ) is amended by striking paragraph (5).\n##### (d) Effective date\nThe amendments made by subsections (a), (b), and (c) shall take effect beginning on the date that is 1 year after the date of enactment of this Act.\nII\nEnsuring Fair Treatment for Part-Time and Temporary Workers\n#### 201. Definitions\nIn this title:\n**(1) Employ**\nThe term employ has the meaning given the term in section 3(g) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(g) ).\n**(2) Employee**\nExcept as provided in section 205(e), the term employee means an individual who is\u2014\n**(A)**\nan employee, as defined in section 3(e) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(e) ), who is not covered under any of subparagraphs (B) through (F), except that a reference in such section to an employer shall be considered to be a reference to a person in commerce described in paragraph (3)(A);\n**(B)**\na State employee described in section 304(a) of the Government Employee Rights Act of 1991 (42 U.S.C. 2000e\u201316c(a));\n**(C)**\na covered employee, as defined in section 101 of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 ), except that such term shall not include an applicant for employment;\n**(D)**\na covered employee, as defined in section 411(c) of title 3, United States Code;\n**(E)**\na Federal officer or employee covered under subchapter V of chapter 63 of title 5, United States Code (without regard to the limitation in section 6381(1)(B) of that title), who is not covered under subparagraph (D); or\n**(F)**\nan employee of the Government Accountability Office.\n**(3) Employer**\nExcept as provided in section 205(e), the term employer \u2014\n**(A)**\n**(i)**\nmeans any person in commerce that is not otherwise described in any other subparagraph of this paragraph and\u2014\n**(I)**\nemploys more than 15 employees described in paragraph (2)(A), which shall be calculated by including all employees described in paragraph (2)(A) performing work for compensation on a full-time, part-time, or temporary basis, except that if the number of such employees who perform work for such a person for compensation fluctuates, the number may be determined for a calendar year based upon the average number of such employees who performed work for the person for compensation during the preceding calendar year; or\n**(II)**\nis part of an integrated enterprise, chain of businesses, group of franchises associated with a franchisor, or network of franchises that, in the aggregate, employs more than 15 such employees, calculated in accordance with subclause (I);\n**(ii)**\nincludes\u2014\n**(I)**\nany person who acts, directly or indirectly, in the interest of such an employer to any of the employees (described in clause (i)) of such employer; and\n**(II)**\nany successor in interest of such an employer; and\n**(iii)**\nincludes an agency described in subparagraph (A)(iii) of section 101(4) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611(4) );\n**(B)**\nis an entity employing a State employee described in section 304(a) of the Government Employee Rights Act of 1991 (42 U.S.C. 2000e\u201316c(a));\n**(C)**\nis an employing office, as defined in section 101 of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 );\n**(D)**\nis an employing office, as defined in section 411(c) of title 3, United States Code;\n**(E)**\nis an employing agency covered under subchapter V of chapter 63 of title 5, United States Code; or\n**(F)**\nis the Comptroller General of the United States.\n**(4) Person**\nThe term person , except as used with the term person in commerce , has the meaning given the term in section 3(a) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(a) ).\n**(5) Person in commerce**\n**(A) In general**\nThe term person in commerce means any person who is engaged in commerce, in any industry or activity affecting commerce, or in the production of goods for commerce.\n**(B) Commerce**\nIn subparagraph (A), the term commerce includes government.\n**(6) Secretary**\nThe term Secretary means the Secretary of Labor.\n#### 202. Elimination of discrimination on the basis of hours worked\n##### (a) Rule\n**(1) In general**\nAn employer shall not discriminate against an employee on the basis that such employee is scheduled to work fewer hours per week, or is employed for a shorter expected duration, than another employee of the employer if the jobs of such employees require substantially equal skill, effort, responsibility, and duties and such jobs are performed under similar working conditions.\n**(2) Examples**\nDiscrimination described in paragraph (1) shall include differential treatment with respect to\u2014\n**(A)**\nrate of compensation;\n**(B)**\nnotice of, and input into, work hours;\n**(C)**\neligibility to accrue, on a pro rata basis, employer-provided paid and unpaid time off and other benefits;\n**(D)**\npromotion opportunities; or\n**(E)**\nother terms, conditions, or privileges of employment.\n##### (b) Distinctions permitted\nThis section shall not be construed to prohibit differences in rate of compensation, or other conditions, terms, or privileges of employment, of employees of an employer for reasons other than the number of hours the employees are scheduled to work per week, or the expected duration of employment of the employees, including for reasons such as\u2014\n**(1)**\nthe date on which the employees are hired;\n**(2)**\na merit system; or\n**(3)**\na system that measures earnings by quantity per hour or quality of production.\n#### 203. Offer of work to existing employees\n##### (a) Written statements required\nUpon hiring an employee, an employer shall\u2014\n**(1)**\nobtain a written statement of the employee\u2019s desired number of weekly work hours and the days and times the employee is available to work;\n**(2)**\nnotify the employee that this written statement may be modified in writing at any time during employment; and\n**(3)**\nspecify the process to modify the written statement.\n##### (b) Offer of desired weekly work hours to existing employees\n**(1) In general**\nExcept as provided in paragraph (2), an employer shall schedule an employee to work the number of weekly hours identified by the employee as desired weekly hours in a written statement under subsection (a) prior to hiring any new employee from an external applicant pool, including hiring through the use of a temporary services or staffing agency, or contracting with a contractor or subcontractor, to work such hours.\n**(2) Exceptions**\nAn employer may hire an individual as a new employee, or engage a contractor or subcontractor, to perform work for the employer if\u2014\n**(A)**\nthe employer needs to fill hours for which no existing employees who have provided written statements under subsection (a) are available based on such written statements;\n**(B)**\nall existing employees who have provided written statements under subsection (a) lack, and cannot obtain with reasonable training, the qualifications necessary to perform the work; or\n**(C)**\nscheduling any such employee to perform the work would require providing such employee overtime compensation at a rate not less than one and one half times the regular rate at which the employee is employed, in accordance with section 7 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 207 ) or any State law.\n##### (c) Compensation required\n**(1) In general**\nExcept as provided in paragraph (2), an employee (referred to in this subsection as an existing employee ) who is not scheduled for the desired number of total weekly work hours identified by the employee in a written statement under subsection (a) shall be compensated for each hour worked by a newly hired employee, contractor, or subcontractor hired after the existing employee so identified such number of hours, during an hour that such existing employee identified in a written statement under such subsection as an hour for which the employee is available to work.\n**(2) Exception**\nAn employer shall not be required to compensate an existing employee under paragraph (1) for any hour of work for which\u2014\n**(A)**\nthe employee lacks, or cannot obtain with reasonable training, the qualifications necessary to perform the work;\n**(B)**\nscheduling such employee to perform the work would require providing the employee overtime compensation as described in subsection (b)(2)(C);\n**(C)**\nthe employer made a reasonable attempt to contact the employee to work such hour and was unable to reach the employee; or\n**(D)**\nthe employee was otherwise no longer available.\n##### (d) Definition\nFor purposes of this section, the terms written , with respect to a statement, and writing mean a printed or printable communication in physical or electronic form.\n#### 204. Prohibited acts\n##### (a) Interference with rights\nIt shall be unlawful for any employer to interfere with, restrain, or deny the exercise or the attempt to exercise, any rights set forth under this title.\n##### (b) Retaliation prohibited\nIt shall be unlawful for any employer to discharge, threaten to discharge, demote, suspend, reduce work hours of, or otherwise discriminate (including taking any other adverse employment action) against any person because of an employee of the employer exercising the rights of the employee under this title or opposing any practice made unlawful by this title.\n##### (c) Interference with Proceedings or Inquiries\nIt shall be unlawful for any person to discharge or in any other manner discriminate against an individual because such individual\u2014\n**(1)**\nhas filed any charge, or has instituted or caused to be instituted any proceeding, under or related to this title;\n**(2)**\nhas given, or is about to give, any information in connection with any inquiry or proceeding relating to any right provided under this title; or\n**(3)**\nhas testified, or is about to testify, in any inquiry or proceeding relating to any right provided under this title.\n#### 205. Remedies and enforcement\n##### (a) Investigative authority\n**(1) In general**\nTo ensure compliance with this title, including any regulation or order issued under this title, the Secretary shall have, subject to paragraph (3), the investigative authority provided under section 11(a) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 211(a) ).\n**(2) Obligation to keep and preserve records**\n**(A) In general**\nEach employer shall maintain for a period of not less than 3 years, or for the duration of any claim (including the duration of a related civil action or investigation) pending pursuant to this title, whichever is longer, all records necessary to demonstrate compliance with this title, including compliance with the requirements of regulations issued by the Secretary under section 206. Such records shall include documentation of offers of hours of work to employees and responses to such offers.\n**(B) Copies**\nEach employer shall, upon a reasonable request of an employee of the employer, provide the employee with a copy of the records described in subparagraph (A) relating to the employee.\n**(3) Required submissions generally limited to an annual basis**\nThe Secretary shall not require, under the authority of this subsection, any employer to submit to the Secretary any books or records more than once during any 12-month period, unless the Secretary has reasonable cause to believe there may exist a violation of this title, including any regulation or order issued pursuant to this title, or is investigating a charge pursuant to subsection (c).\n**(4) Subpoena powers**\nFor the purposes of any investigation provided for in this subsection, the Secretary shall have the subpoena authority provided for under section 9 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 209 ).\n##### (b) Civil action by employees\n**(1) Liability**\n**(A) In general**\nAny employer who violates section 202, 203, or 204 (each such provision referred to in this section as a covered provision ) shall be liable to any person affected for\u2014\n**(i)**\ndamages equal to the amount of\u2014\n**(I)**\nany wages, salary, employment benefits (as defined in section 101 of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611 )), or other compensation denied, lost, or owed to such employee by reason of the violation; or\n**(II)**\nin a case in which wages, salary, employment benefits (as so defined), or other compensation have not been denied, lost, or owed to the employee, any actual monetary losses sustained by the employee as a direct result of the violation;\n**(ii)**\ninterest on the amount described in clause (i) calculated at the prevailing rate;\n**(iii)**\nexcept as provided in subparagraph (B), an additional amount as liquidated damages equal to the sum of the amount described in clause (i) and the interest described in clause (ii); and\n**(iv)**\nsuch equitable relief as may be appropriate, including employment, reinstatement, and promotion.\n**(B) Exception for liquidated damages**\nIf an employer who has violated a covered provision proves to the satisfaction of the court that the act or omission which violated the covered provision was in good faith and that the employer had reasonable grounds for believing that the act or omission was not a violation of a covered provision, such court may, in the discretion of the court, reduce the amount of liability under subparagraph (A) to the amount, interest, and equitable relief determined under clauses (i), (ii), and (iv), respectively.\n**(2) Right of Action**\nAn action to recover the damages, interest, or equitable relief set forth in paragraph (1) may be maintained against any employer (including a public agency) in any Federal or State court of competent jurisdiction by any one or more employees for and on behalf of\u2014\n**(A)**\nsuch employees; or\n**(B)**\nsuch employees and any other employees similarly situated.\n**(3) Fees and Costs**\nThe court in such an action shall, in addition to any judgment awarded to the plaintiff, allow a reasonable attorney\u2019s fee, reasonable expert witness fees, and other costs of the action to be paid by the defendant.\n**(4) Limitations**\nThe right provided by paragraph (2) to bring an action by or on behalf of any employee shall terminate on the filing of a complaint by the Secretary in an action under subsection (c)(4) in which a recovery is sought of the damages, interest, or equitable relief described in paragraph (1)(A) owing to an employee by an employer liable under paragraph (1) unless the action is dismissed without prejudice on motion of the Secretary.\n##### (c) Actions by the Secretary\n**(1) Administrative Action**\nThe Secretary shall receive, investigate, and attempt to resolve complaints of violations of this title in the same manner that the Secretary receives, investigates, and attempts to resolve complaints of violations of sections 6 and 7 of the Fair Labor Standards Act of 1938 (29 U.S.C. 206 and 207), and may issue an order making determinations, and assessing a civil penalty described in paragraph (3) (in accordance with such paragraph), with respect to such an alleged violation.\n**(2) Administrative Review**\nAn affected person who takes exception to an order issued under paragraph (1) may request review of and a decision regarding such an order by an administrative law judge. In reviewing the order, the administrative law judge may hold an administrative hearing concerning the order, in accordance with the requirements of sections 554, 556, and 557 of title 5, United States Code. Such hearing shall be conducted expeditiously.\n**(3) Civil penalty**\n**(A) In general**\nAn employer who willfully and repeatedly violates\u2014\n**(i)**\nsection 204(a) shall be subject to a civil penalty in an amount to be determined by the Secretary, but not to be less than $500, or more than $1,000, per violation (subject to subparagraph (B)); or\n**(ii)**\nsubsection (b) or (c) of section 204 shall be subject to a civil penalty in an amount to be determined by the Secretary, but not to be less than $1,100, or more than $5,000, per violation (subject to subparagraph (B)).\n**(B) Inflation**\nThe Secretary shall, for each year beginning with calendar year 2024, increase the minimum and maximum amounts for the penalties described in clauses (i) and (ii) of subparagraph (A) by a percentage equal to the percentage increase in the Consumer Price Index for All Urban Consumers, published by the Department of Labor, between December 2023 and the December prior to the year for which the increase takes effect.\n**(C) Willful violation**\nFor purposes of this section, an employer willfully violates a provision of section 204 when, after taking into account all of the facts and circumstances surrounding the violation, it is determined that the employer\u2014\n**(i)**\nknew that its conduct was prohibited by such section; or\n**(ii)**\nshowed reckless disregard for the requirements of such section.\n**(4) Civil action**\n**(A) In general**\nThe Secretary may bring an action in any court of competent jurisdiction on behalf of aggrieved employees to\u2014\n**(i)**\nrestrain violations of this title;\n**(ii)**\nobtain such equitable relief as may be appropriate, including employment, reinstatement, and promotion; and\n**(iii)**\nin the case of a violation of a covered provision, recover the damages, interest, and equitable relief described in clauses (i) through (iv) of subsection (b)(1)(A).\n**(B) Recovery on behalf of employees**\nAny sums recovered by the Secretary under subparagraph (A) on behalf of an employee shall be held in a special deposit account and shall be paid, on order of the Secretary, directly to the employee affected. Any such sums not paid to an employee because of inability to do so within a period of 3 years shall be deposited in the Treasury and credited to miscellaneous receipts.\n##### (d) Limitation\n**(1) In general**\nExcept as provided in paragraph (2), an action may be brought under this section not later than 2 years after the date of the last event constituting the alleged violation for which the action is brought.\n**(2) Willful violation**\nIn the case of such action brought for a willful violation of section 204 (as described in subsection (c)(3)), such action may be brought within 3 years of the date of the last event constituting the alleged violation for which such action is brought.\n**(3) Commencement**\nIn determining when an action is commenced by the Secretary or by an employee under this section for the purposes of this subsection, it shall be considered to be commenced on the date when the complaint is filed.\n##### (e) Definition\nFor purposes of subsections (a) through (d)\u2014\n**(1)**\nthe term employee means an employee described in subparagraph (A) or (B) of section 201(2); and\n**(2)**\nthe term employer means an employer described in subparagraph (A) or (B) of section 201(3).\n##### (f) Other Administrative Officers\n**(1) Employees covered by Congressional Accountability Act of 1995**\nThe powers and procedures provided in the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. ) to the Board (as defined in section 101 of that Act ( 2 U.S.C. 1301 )), or any person, alleging a violation of section 202(a)(1) of that Act ( 2 U.S.C. 1312(a)(1) ) shall be the powers and procedures this title provides to that Board, or any person, alleging a violation of this title against an employee described in section 201(2)(C).\n**(2) Employees covered by chapter 5 of title 3, United States Code**\nThe powers and procedures provided in chapter 5 of title 3, United States Code, to the President, the Merit Systems Protection Board, or any person, alleging a violation of section 412(a)(1) of that title, shall be the powers and procedures this title provides to the President, that Board, or any person, respectively, alleging a violation of this title against an employee described in section 201(2)(D).\n**(3) Employees covered by chapter 63 of title 5, United States Code**\nThe powers and procedures provided in title 5, United States Code, to an employing agency, provided in chapter 12 of that title to the Merit Systems Protection Board, or provided in that title to any person, alleging a violation of chapter 63 of that title, shall be the powers and procedures this title provides to that agency, that Board, or any person, respectively, alleging a violation of this title against an employee described in section 201(2)(E).\n**(4) Comptroller General**\nIn the case of employees of the Government Accountability Office, the authority of the Secretary under this title shall be exercised by the Comptroller General of the United States.\n#### 206. Regulations\n##### (a) Secretary of Labor\nExcept as provided in subsections (b) through (e), not later than 180 days after the date of enactment of this Act, the Secretary shall issue such regulations as may be necessary to implement this title.\n##### (b) Board\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Board of Directors of the Office of Congressional Workplace Rights shall issue such regulations as may be necessary to implement this title with respect to employees described in section 201(2)(C). The procedures applicable to regulations of the Board issued for the implementation of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. ), prescribed in section 304 of that Act ( 2 U.S.C. 1384 ), shall be the procedures applicable to regulations issued under this subsection.\n**(2) Consideration**\nIn prescribing the regulations, the Board shall take into consideration the enforcement and remedies provisions concerning the Office and applicable to rights and protections under the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2601 et seq. ), under the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. ).\n**(3) Modifications**\nThe regulations issued under paragraph (1) to implement this title shall be the same as substantive regulations issued by the Secretary to implement this title, except to the extent that the Board may determine, for good cause shown and stated together with the regulations issued by the Board, that a modification of such substantive regulations would be more effective for the implementation of the rights and protections under this title.\n##### (c) President\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the President shall issue such regulations as may be necessary to implement this title with respect to employees described in section 201(2)(D).\n**(2) Consideration**\nIn prescribing the regulations, the President shall take into consideration the enforcement and remedies provisions concerning the President and the Merit Systems Protection Board, and applicable to rights and protections under the Family and Medical Leave Act of 1993, under chapter 5 of title 3, United States Code.\n**(3) Modifications**\nThe regulations issued under paragraph (1) to implement this title shall be the same as substantive regulations issued by the Secretary to implement this title, except to the extent that the President may determine, for good cause shown and stated together with the regulations issued by the President, that a modification of such substantive regulations would be more effective for the implementation of the rights and protections under this title.\n##### (d) Office of Personnel Management\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Office of Personnel Management shall issue such regulations as may be necessary to implement this title with respect to employees described in section 201(2)(E).\n**(2) Consideration**\nIn prescribing the regulations, the Office shall take into consideration the enforcement and remedies provisions concerning an employing agency and the Merit Systems Protection Board under subchapter V of chapter 63 of title 5, United States Code.\n**(3) Modifications**\nThe regulations issued under paragraph (1) to implement this title shall be the same as substantive regulations issued by the Secretary to implement this title, except to the extent that the Office may determine, for good cause shown and stated together with the regulations issued by the Office, that a modification of such substantive regulations would be more effective for the implementation of the rights and protections under this title.\n##### (e) Comptroller General\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Comptroller General of the United States shall issue such regulations as may be necessary to implement this title with respect to employees of the Government Accountability Office.\n**(2) Consideration**\nIn prescribing the regulations, the Comptroller General shall take into consideration the enforcement and remedies provisions concerning the Comptroller General under title I of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611 et seq. ).\n**(3) Modifications**\nThe regulations issued under paragraph (1) to implement this title shall be the same as substantive regulations issued by the Secretary to implement this title, except to the extent that the Comptroller General may determine, for good cause shown and stated together with the regulations issued by the Comptroller General, that a modification of such substantive regulations would be more effective for the implementation of the rights and protections under this title.",
      "versionDate": "2025-12-17",
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
        "actionDate": "2025-12-17",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on House Administration, Oversight and Government Reform, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6818",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Part-Time Worker Bill of Rights Act",
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
        "updateDate": "2026-01-22T15:38:04Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3547is.xml"
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
      "title": "Part-Time Worker Bill of Rights Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Part-Time Worker Bill of Rights Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to extend protections to part-time workers in the areas of family and medical leave and to ensure equitable treatment in the workplace.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:28Z"
    }
  ]
}
```
