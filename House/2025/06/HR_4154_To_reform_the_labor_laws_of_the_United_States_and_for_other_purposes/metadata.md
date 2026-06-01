# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4154?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4154
- Title: Employee Rights Act
- Congress: 119
- Bill type: HR
- Bill number: 4154
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2025-12-09T23:22:46Z
- Update date including text: 2025-12-09T23:22:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-26 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-26 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4154",
    "number": "4154",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "A000372",
        "district": "12",
        "firstName": "Rick",
        "fullName": "Rep. Allen, Rick W. [R-GA-12]",
        "lastName": "Allen",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Employee Rights Act",
    "type": "HR",
    "updateDate": "2025-12-09T23:22:46Z",
    "updateDateIncludingText": "2025-12-09T23:22:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-26T14:02:40Z",
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
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "SC"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "GA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "FL"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "SC"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "MO"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "GA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "MI"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "TN"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "LA"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "PA"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NC"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "NC"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4154ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4154\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Allen (for himself, Mr. Wilson of South Carolina , Mr. Carter of Georgia , Mr. Bean of Florida , Mr. Norman , Mr. Onder , Mr. Jack , Mr. Moolenaar , and Mr. Rose ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo reform the labor laws of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Employee Rights Act .\n#### 2. Enhanced employee rights for lawful workers\nSection 9(a) of the National Labor Relations Act ( 29 U.S.C. 159(a) ) is amended by striking designated or selected for the purposes of collective bargaining and inserting , for the purposes of collective bargaining selected by secret ballot of employees in an election conducted by the Board, .\n#### 3. Union voting for employees who do not have lawful status\n##### (a) National Labor Relations Act\nSection 9 of the National Labor Relations Act ( 29 U.S.C. 159 ) is amended by adding at the end the following:\n(f) Any employee who does not have lawful status under the immigration laws (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )) shall not\u2014 (1) be eligible to vote in any election (including an election by a secret ballot) conducted by the Board under this section, and any vote cast by such an employee in any such election shall not be valid; or (A) be considered an employee for the purposes of any petition described in subsection (c) or (e). .\n##### (b) Labor Management Relations Act\nSection 209(b) of the Labor Management Relations Act, 1947 ( 29 U.S.C. 179(b) ) is amended by adding at the end the following: Any such employee who does not have lawful status under the immigration laws (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )) shall not be entitled to vote in any such secret ballot. .\n##### (c) Labor-Management Reporting and Disclosure Act\nSection 401 of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 481 ) is amended by adding at the end the following:\n(j) Any employee who does not have lawful status under the immigration laws (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )) and who is a member of a labor organization shall not be entitled to vote in any election conducted by a labor organization under this section. .\n#### 4. Employee privacy\n##### (a) Notice of rights and protections; voter registration lists\nSection 8 of the National Labor Relations Act ( 29 U.S.C. 158 ) is amended by adding at the end the following:\n(h) (1) Whenever the Board directs an election under section 9(c) or approves an election agreement, the employer of employees in the bargaining unit shall, after the Board directs such election or approves such election agreement, provide a voter list to a labor organization that has petitioned to represent such employees. Such voter list shall include the names of all employees in the bargaining unit and not more than one additional form of personal contact information for the employee (such as a telephone number, an email address, or a mailing address) chosen by the employee in writing. The voter list shall be provided in a searchable electronic format generally approved by the Board unless the employer certifies that the employer does not possess the capacity to produce the list in the required form. Not later than nine months after the date of enactment of the Employee Rights Act, the Board shall promulgate regulations implementing the requirements of this paragraph. (2) It shall be an unfair labor practice for an employer to violate any requirement under this subsection. .\n##### (b) Labor organization use of personal information\nSection 8(b) of the National Labor Relations Act ( 29 U.S.C. 158(b) ) is amended\u2014\n**(1)**\nin paragraph (6), by striking and at the end;\n**(2)**\nin paragraph (7)(C), by striking services. and inserting services; ;\n**(3)**\nin the matter following paragraph (7)\u2014\n**(A)**\nby adjusting the margin two ems to the left; and\n**(B)**\nby striking Nothing in this paragraph and inserting Nothing in paragraph ; and\n**(4)**\nby inserting after subparagraph (C) of paragraph (7), as so amended, the following:\n(8) to fail to protect the personal information of an employee received for an organizing drive, to use such information for any reason other than a representation proceeding, or to use such information after the conclusion of a representation proceeding; .\n##### (c) Right not To subsidize labor organization nonrepresentational activities\nTitle I of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 411 et seq. ) is amended by adding at the end the following:\n106. Right not to subsidize labor organization nonrepresentational activities No employee\u2019s labor organization dues, fees, assessments, or other contributions shall be used or contributed to any person, organization, or entity for any purpose not directly related to the labor organization\u2019s collective bargaining or contract administration functions on behalf of the represented unit employee unless the employee member, or nonmember required to make such payments as a condition of employment, authorizes such expenditure in writing, after a notice period of not less than 35 days. An initial authorization provided by an employee under the preceding sentence shall expire not later than 1 year after the date on which such authorization is signed by the employee. There shall be no automatic renewal of an authorization under this section. .\n#### 5. Employment relationships\n##### (a) Criteria for determining employee status under the fair labor standards act\nSection 3(e) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(e) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (2), (3), and (4) as paragraphs (3), (4), and (5), respectively;\n**(2)**\nin paragraph (1), by striking paragraphs (2), (3), and (4) and inserting paragraphs (3), (4), and (5) ; and\n**(3)**\nby inserting after paragraph (1) the following:\n(2) (A) An individual shall be determined to be an independent contractor rather than an employee of another person if\u2014 (i) such other person does not exercise significant control over the details of the way the work is performed by the individual, without regard to any control the other person may exercise over the final result of the work performed; and (ii) while performing such work, the individual has the opportunities and risks inherent with entrepreneurship, such as the discretion to exercise managerial skill, business acumen, or professional judgment. (B) The following factors may not be used in determining that an individual is an employee of another person: (i) Whether such other person requires the individual to comply with legal, statutory, or regulatory requirements. (ii) Whether such other person requires the individual to comply with health and safety standards that are more stringent than otherwise applicable health and safety standards. (iii) Whether such other person requires the individual to carry insurance of any kind. (iv) Whether such other person requires the individual to meet contractually agreed-upon performance standards, such as deadlines. .\n##### (b)\nSection 2(3) of the National Labor Relations Act ( 29 U.S.C. 152(3) ) is amended\u2014\n**(1)**\nby striking (3) The term employee shall and inserting the following:\n(3) (A) The term employee shall ; and\n**(2)**\nby adding at the end the following:\n(B) Section 3(e)(2) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(e)(2) ) shall be used in determining whether an individual is an independent contractor or an employee of another person. .\n##### (c)\n**(1) National labor relations act**\nSection 2(2) of the National Labor Relations Act ( 29 U.S.C. 152(2) ) is amended\u2014\n**(A)**\nby striking The term employer and inserting (A) The term employer ; and\n**(B)**\nby adding at the end the following:\n(B) An employer may be considered a joint employer of the employees of another employer only if each employer directly, actually, and immediately, and not in a limited and routine manner, exercises significant control over the essential terms and conditions of employment of the employees of the other employer, such as hiring such employees, discharging such employees, determining the rate of pay and benefits of such employees, supervising such employees on a day-to-day basis, assigning such employees a work schedule, position, or task, or disciplining such employees. .\n**(2) Fair labor standards act of 1938**\nSection 3(d) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(d) ) is amended\u2014\n**(A)**\nby striking Employer includes and inserting (1) Employer includes ; and\n**(B)**\nby adding at the end the following:\n(2) An employer may be considered a joint employer of the employees of another employer for purposes of this Act only if each employer meets the criteria set forth in section 2(2)(B) of the National Labor Relations Act ( 29 U.S.C. 152(2)(B) ) except that, for purposes of determining joint-employer status under this Act, the terms employee and employer referenced in such section shall have the meanings given such terms in this section. .\n##### (d) Provision of technical assistance\nNotwithstanding any other provision of law, under the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ), the National Labor Relations Act ( 29 U.S.C. 151 et seq. ), or any other Federal law, none of the following may be construed, alone or in combination with any other factor, as establishing an employer and employee relationship between a franchisor (or any employee of the franchisor) and a franchisee (or any employee of the franchisee):\n**(1)**\nThe franchisor (or any employee of the franchisor) provides the franchisee (or any employee of the franchisee) with, or requires such franchisee (or any employee of the franchisee) to use, a handbook, or other training, on sexual harassment, human trafficking, workplace violence, discrimination, or opportunities for apprenticeships or scholarships.\n**(2)**\nThe franchisor (or any employee of the franchisor) requires the franchisee (or any employee of the franchisee) to adopt a policy on sexual harassment, human trafficking, workplace violence, discrimination, opportunities for apprenticeships or scholarships, child care, or paid leave, including a requirement for such franchisee (or any employee of the franchisee) to report to the franchisor (or any employee of the franchisor) any violations or suspected violations of such policy.\n#### 6. Tribal sovereignty\nSection 2 of the National Labor Relations Act ( 29 U.S.C. 152 ) is amended\u2014\n**(1)**\nin paragraph (2), by inserting or any Indian Tribe, or any enterprise or institution owned and operated by an Indian Tribe and located on its Indian lands, after subdivision thereof, ; and\n**(2)**\nby adding at the end the following:\n(15) The term Indian Tribe means any Indian Tribe, band, nation, pueblo, or other organized group or community which is recognized as eligible for the special programs and services provided by the United States to Indians because of their status as Indians. (16) The term Indian means any individual who is a member of an Indian Tribe. (17) The term Indian lands means\u2014 (A) all lands within the limits of any Indian reservation; (B) any lands title to which is either held in trust by the United States for the benefit of any Indian Tribe or Indian or held by any Indian Tribe or Indian subject to restriction by the United States against alienation; and (C) any lands in the State of Oklahoma that are within the boundaries of a former reservation (as defined by the Secretary of the Interior) of a Federally recognized Indian Tribe. .\n#### 7. Independent negotiating\n##### (a) Unfair labor practices\nSection 8 of the National Labor Relations Act ( 29 U.S.C. 158 ) is further amended\u2014\n**(1)**\nin subsection (a)(3)\u2014\n**(A)**\nby striking the or before (B) ; and\n**(B)**\nby striking membership; and inserting membership, or (C) if, in a covered State, the employee has ceased to be a member of a labor organization or pay an exclusive representative ; and\n**(2)**\nin subsection (b) by inserting after paragraph (8), as added by section 2(b)(2) of this Act, the following:\n(9) in a covered State, to represent or bargain on behalf of employees who have ceased to be a member of a labor organization or pay an exclusive representative; (10) in a covered State, to interfere with employees who have ceased to be a member of a labor organization or pay an exclusive representative engaged in independent negotiating; (11) in a covered State, to restrain or coerce employees who have ceased to be a member of a labor organization or pay an exclusive representative from engaging in independent negotiating; and .\n##### (b) Exclusion of workers engaged in independent negotiating from representation\nSection 9(a) of such Act ( 29 U.S.C. 159(a) ) is amended\u2014\n**(1)**\nby inserting (other than any employee who has elected to engage in independent negotiating) after all the employees ;\n**(2)**\nby inserting , in a State or Territory that is not a covered State, before any individual ; and\n**(3)**\nby inserting and, in a covered State, an individual employee shall engage in independent negotiating with their employer if such employee has ceased to be a member of a labor organization or pay an exclusive representative after in effect .\n##### (c) Independent negotiating and covered state defined\nSection 2 of such Act ( 29 U.S.C. 152 ) is further amended by adding at the end the following:\n(18) The term independent negotiating means, in a unit located in a covered State with an exclusive representative for the purposes of collective bargaining, negotiating between an employer and an individual employee as though such employee were not in such a unit and without regard to the existence of a collective-bargaining contract or agreement. (19) The term covered State means a State or Territory which prohibits the execution or application of agreements requiring membership in, or payment to, a labor organization as a condition of employment. .\n#### 8. Diversity, equity, or inclusion\nSection 8(b) of the National Labor Relations Act ( 29 U.S.C. 158(b) ) is further amended by inserting after paragraph (12), as added by section 7(a)(2) of this Act, the following:\n(12) to include any provision in a collective bargaining agreement that mandates or promotes diversity, equity, or inclusion initiatives, including preferences, mandates, policies, programs, activities, or guidance related to personal characteristics of an individual and is not related to the qualifications or performance required for a job, unless such initiatives are required by Federal, State, or local law. .\n#### 9. Freedom from union violence act\nSection 1951 of title 18, United States Code, is amended to read as follows:\n1951. Interference with commerce by threats or violence (a) Prohibition Except as provided in subsection (c), whoever in any way or degree obstructs, delays, or affects commerce or the movement of any article or commodity in commerce, by robbery or extortion, or attempts or conspires so to do, or commits or threatens physical violence to any person or property in furtherance of a plan or purpose to do anything in violation of this section, shall be fined not more than $100,000, imprisoned for a term of not more than 20 years, or both. (b) Definitions For purposes of this section\u2014 (1) the term commerce means any\u2014 (A) commerce within the District of Columbia, or any territory or possession of the United States; (B) commerce between any point in a State, territory, possession, or the District of Columbia and any point outside thereof; (C) commerce between points within the same State through any place outside that State; and (D) other commerce over which the United States has jurisdiction; (2) the term extortion means the obtaining of property from any person, with the consent of that person, if that consent is induced\u2014 (A) by actual or threatened use of force or violence, or fear thereof; (B) by wrongful use of fear not involving force or violence; or (C) under color of official right; (3) the term labor dispute has the same meaning as in section 2(9) of the National Labor Relations Act ( 29 U.S.C. 152(9) ); and (4) the term robbery means the unlawful taking or obtaining of personal property from the person or in the presence of another, against his or her will, by means of actual or threatened force or violence, or fear of injury, immediate or future\u2014 (A) to his or her person or property, or property in his or her custody or possession; or (B) to the person or property of a relative or member of his or her family, or of anyone in his or her company at the time of the taking or obtaining. (c) Exempted conduct (1) In general Subsection (a) does not apply to any conduct that\u2014 (A) is incidental to otherwise peaceful picketing during the course of a labor dispute; (B) consists solely of minor bodily injury, or minor damage to property, or threat or fear of such minor injury or damage; and (C) is not part of a pattern of violent conduct or of coordinated violent activity. (2) State and local jurisdiction Any violation of this section that involves any conduct described in paragraph (1) shall be subject to prosecution only by the appropriate State and local authorities. (d) Effect on other law Nothing in this section shall be construed\u2014 (1) to repeal, amend, or otherwise affect\u2014 (A) section 6 of the Clayton Act ( 15 U.S.C. 17 ); (B) section 20 of the Clayton Act ( 29 U.S.C. 52 ); (C) any provision of the Norris-LaGuardia Act ( 29 U.S.C. 101 et seq. ); (D) any provision of the National Labor Relations Act ( 29 U.S.C. 151 et seq. ); or (E) any provision of the Railway Labor Act ( 45 U.S.C. 151 et seq. ); or (2) to preclude Federal jurisdiction over any violation of this section, on the basis that the conduct at issue\u2014 (A) is also a violation of State or local law; or (B) occurred during the course of a labor dispute or in pursuit of a legitimate business or labor objective. .\n#### 10. Unlawful harassment\nSection 8(a)(3) of the National Labor Relations Act ( 29 U.S.C. 158(a)(3) ) is amended by adding after Provided, the following: that nothing in this section shall be construed to prevent an employer from taking action to protect employees from discriminatory, harassing, or demeaning language or conduct, including during organizing campaigns or strikes: Provided further, .",
      "versionDate": "2025-06-26",
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
        "actionDate": "2025-07-23",
        "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 19 - 16."
      },
      "number": "1319",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Fair Labor Standards Act of 1938 and the National Labor Relations Act to clarify the standard for determining whether an individual is an employee, and for other purposes.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-17",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 16."
      },
      "number": "1723",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Tribal Labor Sovereignty Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-03",
        "text": "Read twice and referred to the Committee on Indian Affairs."
      },
      "number": "1301",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Tribal Labor Sovereignty Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-26",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5054",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Freedom From Union Violence Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-08",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2984",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Employee Rights Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-09-19T15:51:50Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4154ih.xml"
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
      "title": "Employee Rights Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-22T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Employee Rights Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-22T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reform the labor laws of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-22T04:18:18Z"
    }
  ]
}
```
