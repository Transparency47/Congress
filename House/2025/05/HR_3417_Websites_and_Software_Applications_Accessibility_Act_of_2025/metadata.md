# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3417?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3417
- Title: Websites and Software Applications Accessibility Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3417
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2026-03-24T17:50:01Z
- Update date including text: 2026-03-24T17:50:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-14 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-14 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3417",
    "number": "3417",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "S000250",
        "district": "17",
        "firstName": "Pete",
        "fullName": "Rep. Sessions, Pete [R-TX-17]",
        "lastName": "Sessions",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Websites and Software Applications Accessibility Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-24T17:50:01Z",
    "updateDateIncludingText": "2026-03-24T17:50:01Z"
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
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:04:25Z",
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
          "date": "2025-05-14T14:04:20Z",
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
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "MD"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "FL"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "TX"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MI"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "OH"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "UT"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NY"
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
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3417ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3417\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Sessions (for himself and Mr. Hoyer ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish uniform accessibility standards for websites and applications of employers, employment agencies, labor organizations, joint labor-management committees, public entities, public accommodations, testing entities, and commercial providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Websites and Software Applications Accessibility Act of 2025 .\n#### 2. Findings and purposes\n##### (a) Findings\nCongress finds the following:\n**(1)**\nSection 2(b)(1) of the Americans with Disabilities Act of 1990 (ADA) states that the Act provides a clear and comprehensive national mandate for the elimination of discrimination against individuals with disabilities ( 42 U.S.C. 12101(b)(1) ).\n**(2)**\nIn 1990, websites and applications were essentially nonexistent, but Congress made clear that the ADA should keep pace with the rapidly changing technology of the times (H.R. Rep. No. 101\u2013485, pt. 2, at 381 (1990), as reprinted in 1990 U.S.C.C.A.N. 303, 391).\n**(3)**\nSection 102 of the ADA ( 42 U.S.C. 12112 ), section 202 of the ADA ( 42 U.S.C. 12132 ), and section 302 of the ADA ( 42 U.S.C. 12182 ) broadly prohibit discrimination on the basis of disability in regard to employment; services programs, or activities of public entities; and of goods, services, facilities, privileges, advantages, and accommodations of any place of public accommodation, respectively.\n**(4)**\nThe Department of Justice has promulgated regulations to address the intersection of the ADA and emerging technologies, including the obligation to ensure effective communication with and by individuals with disabilities by using technologies such as video remote interpreting, real-time computer-aided transcription, open and closed captioning, audio description, videophones, captioned telephones, screen reader software, optical readers, and telephone systems that interact properly with internet-based relay systems.\n**(5)**\nThe Department of Justice has also promulgated regulations implementing section 202 of the ADA to establish specific requirements, including the adoption of specific technical standards, for making accessible the services, programs, and activities offered by public entities to the public through the web and mobile applications.\n**(6)**\nThe activities of a vast number of ADA-covered entities now occur in whole or in part through websites and applications, a shift that was accelerated by a global pandemic. The digital economy accounts for nearly 10 percent of the United States gross domestic product, and 85 percent of United States adults visit the internet at least once per day.\n**(7)**\nDespite the ADA\u2019s clear language covering all terms, conditions, and privileges of employment and certain actions of employers; all services, programs, and activities of public entities; and all goods, services, facilities, privileges, advantages, and accommodations of public accommodations, including when conducted through websites and applications, most websites and applications of entities covered by the ADA contain significant barriers for individuals with disabilities.\n**(8)**\nConsistent with, Congress\u2019 intention for the ADA to keep pace with rapidly changing technology, the Department of Justice has rightly acknowledged that the ADA requires covered entities to ensure that their websites and mobile applications are accessible to individuals with disabilities.\n**(9)**\nSome courts have misconstrued section 302 of the ADA, despite the clear language of the ADA\u2019s provisions. 10 Some courts have said Section 302 only covers public accommodations that are physical places. In addition, some courts have said that section 302 only covers certain websites of public accommodations depending on the relationship between the website and a physical place. Section 302\u2019s coverage is not limited to physical places. Section 302 covers all websites and applications of public accommodations, regardless of whether the public accommodation is a physical place or regardless of the relationship between a website or application and a physical place.\n**(10)**\nWithout equal access to websites and applications, many individuals with disabilities are treated as second-class citizens and are excluded from equal participation in and equal access to all aspects of society.\n##### (b) Purpose\nIt is the purpose of this Act\u2014\n**(1)**\nto affirm that the ADA and this Act require that websites and applications used by any covered entity to communicate or interact with applicants, employees, participants, customers, or other members of the public be readily accessible to and useable by individuals with disabilities, whether the entity has a physical location or is digital only;\n**(2)**\nto require the Department of Justice and the Equal Employment Opportunity Commission to set and enforce additional standards for websites, electronic documents, and software applications and to periodically update such standards;\n**(3)**\nto address and remedy the systemic nationwide problem of inaccessible websites and applications that exclude individuals with disabilities from equal participation in and equal access to all aspects of society; and\n**(4)**\nto create effective mechanisms to respond to emerging technologies and to ensure that such technologies do not impair the rights and abilities of individuals with disabilities to participate in all aspects of society.\n#### 3. Definitions\nIn this Act:\n**(1) Accessible**\nThe term accessible or accessibility , used with respect to web content or an application, means a perceivable, operable, understandable, and robust web content or an application that enables individuals with disabilities to access the same information as, to engage in the same interactions as, to conduct the same transactions as, to communicate and to be understood as effectively as, and to enjoy the same services as are offered to, other individuals with the same privacy, same independence, and same ease of use as, individuals without disabilities.\n**(2) Accessibility regulations**\nThe term accessibility regulations means the regulations issued under section 5 in accordance with this Act.\n**(3) ADA**\nThe term ADA means the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ).\n**(4) Application**\nThe term application means software that is designed to run on a device, including a smartphone, tablet, self-service kiosk, wearable technology item, or laptop or desktop computer or another device, including a device devised after the date of enactment of this Act, and that is designed to perform, or to help the user perform, a specific task.\n**(5) Commercial provider**\nThe term commercial provider means any entity, including a public or private entity\u2014\n**(A)**\nwhose operations affect commerce; and\n**(B)**\nthat designs, develops, constructs, alters, modifies, or adds an application or web content for a covered entity (including a covered entity described in subparagraph (A) that takes such an action for the covered entity's product) for covered use.\n**(6) Commission**\nThe term Commission means the Equal Employment Opportunity Commission.\n**(7) Covered entity**\nThe term covered entity means an employment entity, public entity, public accommodation, or testing entity.\n**(8) Covered use**\nThe term covered use means\u2014\n**(A)**\nuse by an employment entity in determining or conducting job application procedures, hiring, advancement, or discharge of employees, employee compensation, job training, or other term, condition, or privilege of employment, for employees or applicants to become employees;\n**(B)**\nuse by a public entity to provide to an applicant, participant, or other member of the public a service, program, or activity covered under title II of the ADA ( 42 U.S.C. 12131 et seq. ), section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ), or section 1557 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 1811 ), including information related to such service, program, or activity; and\n**(C)**\nuse by a public accommodation or testing entity to provide to customers or other members of the public a good, service, facility, privilege, advantage, or accommodation, including information related to such good, service, facility, privilege, advantage, or accommodation, regardless of whether the public accommodation or testing entity owns, operates, or utilizes a physical location for covered use.\n**(9) Department**\nThe term Department means the Department of Justice.\n**(10) Disability**\nThe term disability has the meaning given the term in section 3 of the ADA ( 42 U.S.C. 12102 ).\n**(11) Employee**\nThe term employee has the meaning given the term in section 101 of the ADA ( 42 U.S.C. 12111 ).\n**(12) Employer**\nThe term employer has the meaning given the term in section 101 of the ADA ( 42 U.S.C. 12111 ).\n**(13) Employment agency**\nThe term employment agency has the meaning given the term in section 701 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e ).\n**(14) Employment entity**\nThe term employment entity means an employer, employment agency, labor organization, or joint labor-management committee.\n**(15) Information and communication technology**\nThe term information and communication technology \u2014\n**(A)**\nmeans\u2014\n**(i)**\nany equipment or interconnected system or subsystem of equipment, used in the automatic acquisition, storage, analysis, evaluation, manipulation, management, movement, control, display, switching, interchange, transmission, or reception of data or information; and\n**(ii)**\nother equipment or technology, or another system or process, for which the principal function is the creation, manipulation, storage, display, receipt, or transmission of electronic data and information, as well as any associated content; and\n**(B)**\nincludes computers and peripheral equipment, information kiosks and transaction machines, telecommunications equipment, customer premises equipment, multifunction office machines, software, applications, web content, videos, and electronic documents.\n**(16) Joint labor-management committee**\nThe term joint labor-management committee means a labor management committee established pursuant to section 205A of the Labor Management Relations Act, 1947 ( 29 U.S.C. 175a ) and engaged in commerce.\n**(17) Labor organization**\nThe term labor organization has the meaning given the term in section 701 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e ).\n**(18) Operable**\nThe term operable , used with respect to web content or an application, means that user interface components and navigation for the web content or application can be operated by individuals with disabilities.\n**(19) Perceivable**\nThe term perceivable , used with respect to web content or an application, means that information and user interface components for the web content or application are presentable in ways that individuals with disabilities can perceive.\n**(20) Public accommodation**\nThe term public accommodation means a private entity described in paragraph (7) of section 301 of the ADA ( 42 U.S.C. 12181 ) that owns, operates, or utilizes web content or an application for covered use.\n**(21) Public entity**\nThe term public entity has the meaning given the term public entity in section 201 of the ADA ( 42 U.S.C. 12131 ).\n**(22) Qualified individual**\nThe term qualified individual , used with respect to an employee or an applicant to become an employee, has the meaning given the term in section 101 of the ADA ( 42 U.S.C. 12111 ).\n**(23) Robust**\nThe term robust , used with respect to web content or an application, means web content or an application for which the content can be interpreted by and the interface can be accessed by a wide variety of tools, including assistive technology, used by individuals with disabilities.\n**(24) Small entity**\nThe term small entity means an entity or provider defined as a small entity in the regulations issued under subsection (a) or (b) of section 5.\n**(25) Software definitions**\n**(A) Platform software**\n**(i) In general**\nThe term platform software means software\u2014\n**(I)**\nthat interacts with hardware or provides services for other software;\n**(II)**\nthat may run or host other software, and may isolate the other software from underlying software or hardware layers; and\n**(III)**\na single component of which may have both platform and non-platform aspects.\n**(ii) Platform**\nFor purposes of clause (i), the term platform includes\u2014\n**(I)**\na desktop operating system;\n**(II)**\nan embedded operating system, including a mobile system;\n**(III)**\na web browser;\n**(IV)**\na plugin to a web browser that renders a particular media or format; and\n**(V)**\na set of components that allows another application to execute, such as an application which supports macros or scripting.\n**(B) Software**\nIn subparagraphs (A) and (C), the term software \u2014\n**(i)**\nmeans a program, a procedure, and a rule (any of which may include related data or documentation), that directs the use and operation of information and communication technology to perform a given task or function; and\n**(ii)**\nincludes applications, non-web software, platform software, and software tools.\n**(C) Software development tool**\n**(i) In general**\nThe term software tool means software\u2014\n**(I)**\nfor which the primary function is the development of other software; and\n**(II)**\nthat usually comes in the form of an Integrated Development Environment (IDE) and is an application suite of related products and utilities.\n**(ii) Integrated Development Environment**\nIn clause (i), the term Integrated Development Environment means an application such as\u2014\n**(I)**\nMicrosoft\u00ae Visual Studio Code\u00ae;\n**(II)**\nApple\u00ae Xcode\u00ae; and\n**(III)**\nEclipse Foundation Eclipse\u00ae.\n**(26) State**\nThe term State means each of the several States, the District of Columbia, and any territory or possession of the United States.\n**(27) Testing entity**\nThe term testing entity means any person whose operations affect commerce, as defined in section 301 of the ADA ( 42 U.S.C. 12181 ) and that offers examinations or courses related to, applying, licensing, certification, or credentialing for secondary or postsecondary education, professional, or trade purposes.\n**(28) Understandable**\nThe term understandable , used with respect to web content or an application, means that the components of the user interface for the web content or application, including any input fields, error messages, and correction opportunities, are predictable and can be understood and used by individuals with disabilities.\n**(29) Web content and related terms**\n**(A) Web content**\nThe term web content means information and sensory experience communicated to a user by means of a user agent, including code or markup that defines the content\u2019s structure, presentation, and interactions.\n**(B) Presentation**\nThe term presentation means the rendering of the content in a form to be perceived by users.\n**(C) Structure**\nThe term structure means the way in which the parts of a web page are organized in relation to each other and how a collection of web pages is organized.\n**(D) User agent**\nThe term user agent means any software that retrieves and presents web content for users.\n#### 4. Access to web content and applications\n##### (a) General rules for covered entities\n**(1) Employment entity**\nNo employment entity shall subject to discrimination, related to web content or an application owned, operated, or utilized for covered use by the employment entity, an individual with a disability in regard to an activity described in section 102 of the ADA ( 42 U.S.C. 12112 ).\n**(2) Public entity**\nNo individual with a disability shall, by reason of such disability\u2014\n**(A)**\nbe excluded from participation in or be denied the benefits of the services, programs, or activities, or information related to such services, programs, or activities, including information offered through web content or an application owned, operated, or utilized, for a covered use, by a public entity; or\n**(B)**\nbe otherwise subjected to discrimination related to web content or an application owned, operated, or utilized for covered use by a public entity.\n**(3) Public accommodation and testing entity**\nNo individual shall be discriminated against on the basis of disability in the full and equal enjoyment of the goods, services, facilities, privileges, advantages, or accommodations, or information related to such goods, services, facilities, privileges, advantages, or accommodations, including information offered through web content or an application owned, operated, or utilized for covered use by a public accommodation or testing entity.\n##### (b) Covered entities\nIn order to comply with subsection (a), a covered entity shall meet the following requirements:\n**(1) Accessibility**\nA covered entity that engages in an activity described in section 102 of the ADA ( 42 U.S.C. 12112 ), or that provides goods, services, facilities, privileges, advantages, accommodations, programs, activities, including information related to such goods, services, facilities, privileges, advantages, accommodations, programs, or activities, through web content or an application shall ensure that such content or application is accessible.\n**(2) Effective communications**\nA covered entity shall ensure that communications through web content and applications with applicants, employees, participants, customers, and other members of the public with disabilities are as effective as communications with individuals without disabilities.\n##### (c) Commercial providers\nNo commercial provider shall design, develop, construct, alter, modify, or add to an application or any web content for a covered entity for covered use in a manner that results in the content or application not being accessible, or otherwise provide web content or an application to a covered entity for covered use that is not accessible.\n##### (d) Defenses and exemptions\n**(1) Employment entities**\nWith respect to a claim that an employment entity violated this section, the entity shall not be considered to have violated this section if compliance with this section\u2014\n**(A)**\nwould impose an undue burden on the entity; or\n**(B)**\nwould fundamentally alter the nature of the employment provided by the entity.\n**(2) Public entities**\nWith respect to a claim that a public entity violated this section, the entity shall not be considered to have violated this section if compliance with this section\u2014\n**(A)**\nwould impose an undue burden on the entity; or\n**(B)**\nwould fundamentally alter the nature of the services, programs, or activities, including information provided by the entity.\n**(3) Public accommodations or testing entities**\nWith respect to a claim that a public accommodation or testing entity violated this section, the accommodation or entity shall not be considered to have violated this section if compliance with this section\u2014\n**(A)**\nwould impose an undue burden on the accommodation or entity; or\n**(B)**\nwould fundamentally alter the nature of the goods, services, facilities, privileges, advantages, accommodations, including information provided by the accommodation or entity.\n**(4) Commercial providers**\nWith respect to a claim that a commercial provider violated this section, the commercial provider shall not be considered to have violated this section if compliance with this section\u2014\n**(A)**\nwould impose an undue burden on the commercial provider; or\n**(B)**\nwould fundamentally alter the nature of the goods, services, facilities, privileges, advantages, accommodations, programs, activities, including information provided by the covered entity served.\n#### 5. Rulemaking\n##### (a) Public entities, public accommodations, and testing entities\n**(1) Notice of proposed rulemaking**\n**(A) Accessibility**\nNot later than 12 months after the date of enactment of this Act, the Attorney General shall issue, for purposes of section 4, a notice of proposed rulemaking regarding the accessibility of web content and applications applicable to covered entities that are public entities or public accommodations or testing entities, and the commercial providers for the three types of covered entities, for covered use. Such notice shall propose regulations to implement the accessibility obligations of this Act, and include standards for accessible web content and applications that offer equally effective experiences for users with disabilities and users without disabilities.\n**(B) Small entities**\nIn proposing the regulations described in subparagraph (A), the Attorney General shall\u2014\n**(i)**\ndetermine which covered entities and commercial providers should be considered small entities for the purposes of this Act; and\n**(ii)**\ntake into account the capabilities of small entities, such as small businesses, to comply with standards for accessible web content and applications.\n**(2) Final rule**\n**(A) In general**\nNot later than 24 months after the date of enactment of this Act, the Attorney General shall issue, for purposes of section 4, a final rule regarding the accessibility of web content and applications applicable to the covered entities, and the commercial providers, described in paragraph (1), for covered use. Such final rule shall implement the accessibility obligations of this Act, include standards for accessible web content and applications that offer equally effective experiences for users with disabilities and users without disabilities, and take into account the capabilities of small entities, as described in paragraph (1)(B)(ii).\n**(B) Effective date**\nThe final rule shall take effect\u2014\n**(i)**\nfor small entities, 3 years after the date of issuance of the final rule; and\n**(ii)**\nfor other entities, 30 days after that date of issuance.\n**(3) Public posting of enforcement actions**\nNot later than 6 months after such issuance, the Attorney General shall, to the extent permitted by law, post publicly on the Department website any and all settlement documents and documents specifying other resolutions, resulting from the initiation of enforcement actions, or filing of administrative or civil actions, by the Attorney General pursuant to this Act concerning the covered entities, and the commercial providers, described in paragraph (1).\n##### (b) Employment entities\n**(1) Notice of proposed rulemaking**\n**(A) Accessibility**\nNot later than 12 months after the date of enactment of this Act, the Commission shall issue, for purposes of section 4, a notice of proposed rulemaking regarding the accessibility of web content and applications applicable to employment entities, and the commercial providers for employment entities, for covered use. Such notice shall propose regulations to implement the accessibility obligations of this Act, and include standards for accessible web content and applications that offer equally effective experiences for users with disabilities and users without disabilities.\n**(B) Small entities**\nIn proposing the regulations described in subparagraph (A), the Commission shall\u2014\n**(i)**\ndetermine which covered entities and commercial providers should be considered small entities for the purposes of this Act; and\n**(ii)**\ntake into account the capabilities of small entities, such as small businesses, to comply with standards for accessible web content and applications.\n**(2) Final rule**\n**(A) In general**\nNot later than 24 months after the date of enactment of this Act, the Commission shall issue, for purposes of section 4, a final rule regarding the accessibility of web content and applications applicable to the employment entities, and the commercial providers, described in paragraph (1), for covered use. Such final rule shall implement the accessibility obligations of this Act, include standards for accessible web content and applications that offer equally effective experiences for users with disabilities and users without disabilities, and take into account the capabilities of small entities, as described in paragraph (1)(B)(ii).\n**(B) Effective date**\nThe final rule shall take effect\u2014\n**(i)**\nfor small entities, 2 years after the date of issuance of the final rule; and\n**(ii)**\nfor other entities, 30 days after that date of issuance.\n**(3) Public posting of enforcement actions**\nNot later than 6 months after such issuance, the Commission shall, to the extent permitted by law, post publicly on the Commission website any and all settlement documents, and documents specifying other resolutions, resulting from the initiation of enforcement actions, or filing of administrative or civil actions, by the Commission pursuant to this Act concerning the employment entities, and the commercial providers, described in paragraph (1).\n#### 6. Periodic review\n##### (a) Review\nFor each of the first 3 years after the date of enactment of this Act, and every 2 years thereafter, each Federal agency receiving complaints or engaging in enforcement (including compliance reviews and investigations), administrative (including administrative resolution of a claim of a violation), or civil actions under this Act shall submit a report on the complaints and activities to the Department and the Commission. The Attorney General and the Commission shall, for each of the first 3 years and every 2 years thereafter, review complaints received and enforcement, administrative, or civil actions taken under this Act, to determine whether the purpose of this Act is being achieved. In conducting such reviews, the Attorney General and the Commission may award grants, contracts, or cooperative agreements to entities that have documented experience and expertise in collecting and analyzing data associated with implementing reviews of complaints, and enforcement, administrative, and civil actions.\n##### (b) Report\nThe Attorney General and the Commission shall prepare a report containing the results of each such review of complaints and actions described in subsection (a), and shall submit the report to the Committee on Health, Education, Labor, and Pensions and the Committee on the Judiciary of the Senate and the Committee on Education and Workforce and the Committee on the Judiciary of the House of Representatives.\n##### (c) Updated regulations\nThe Attorney General and the Commission shall issue, in accordance with this Act, updated accessibility regulations every 3 years following the date of issuance of the initial accessibility regulations issued under this Act.\n#### 7. Enforcement and administrative action, and private right of action\n##### (a) Civil actions by Attorney General or Commissioner\n**(1) Civil action by Attorney General**\n**(A) In general**\n**(i) Investigation after a complaint**\nOn receiving a complaint filed by an individual with a disability, a class of individuals with disabilities, or an entity representing an individual with a disability or such a class, of a violation of paragraph (2) or (3) of subsection (a), as the case may be, or a complaint filed by a covered entity that is a public entity, public accommodation, or testing entity of a violation of subsection (c), of section 4 (including a related provision of the final rule issued under section 5(a)), the Attorney General may conduct an investigation. The investigation shall consist of a review of the corresponding web content or application owned, operated, or utilized for covered use by such a covered entity, or provided to such a covered entity by a commercial provider, to determine whether the covered entity or commercial provider has violated the corresponding provision of section 4.\n**(ii) Other investigation and review**\nIn addition, the Attorney General shall, on the Attorney General's own authority, investigate practices that may be violations of, and undertake periodic reviews of compliance of such covered entities and commercial providers with, the corresponding provision of section 4 (including a related provision of the final rule issued under section 5(a)).\n**(iii) Determination of violation**\nIf, after investigation or review under this subparagraph, the Attorney General determines that such a covered entity or commercial provider has violated the corresponding provision of section 4 (including a related provision of the final rule issued under section 5(a)), the Attorney General may take administrative action (including administrative resolution of a claim of such a violation) or bring a civil action in a district court of the United States.\n**(B) Intervention**\nIf the Attorney General brings such a civil action based on a complaint filed by an individual, class of individuals, or entity, described in subparagraph (A), including a covered entity described in subparagraph (A) alleging a violation by a commercial provider, such individual, class, or entity shall have the right to intervene in such civil action.\n**(2) Civil action by others**\nAn individual, class, or entity, described in paragraph (1)(A), including a covered entity described in paragraph (1)(A) alleging a violation by a commercial provider, may bring a civil action alleging a violation of paragraph (2) or (3) of subsection (a), or subsection (c), as the case may be, of section 4 (including a related provision of the final rule issued under section 5(a)) in an appropriate State or Federal court without first filing a complaint with the Department or exhausting any other administrative remedies.\n##### (b) Employment entities\n**(1) Civil action by Commissioner**\n**(A) In general**\n**(i) Investigation after a complaint**\nOn receiving a complaint filed by a qualified individual, a class of qualified individuals, or an entity representing a qualified individual or such a class, of a violation of subsection (a)(1), or a complaint filed by an employment entity of a violation of subsection (c), of section 4 (including a related provision of the final rule issued under section 5(b)), the Commission may conduct an investigation. The investigation shall consist of a review of the corresponding web content or application owned, operated, or utilized for covered use by an employment entity, or provided to an employment entity by a commercial provider, to determine whether the employment entity or commercial provider has violated the corresponding provision of section 4.\n**(ii) Other investigation and review**\nIn addition, the Commission shall, on the Commission's own authority, investigate practices that may be violations of, and undertake periodic reviews of compliance of employment entities and commercial providers with, the corresponding provision of section 4 (including a related provision of the final rule issued under section 5(b)).\n**(iii) Determination of violation**\nIf, after investigation or review described in this subparagraph, the Commission determines that an employment entity or commercial provider has violated the corresponding provision of section 4 (including a related provision of the final rule issued under section 5(b)), the Commission may take administrative action (including administrative resolution of a claim of such a violation) or bring a civil action in a district court of the United States.\n**(B) Intervention**\nIf the Commission brings such a civil action based on a complaint filed by a qualified individual, class of qualified individuals, or entity, described in subparagraph (A), including an employment entity alleging a violation by a commercial provider, such qualified individual, class, or entity shall have the right to intervene in such civil action.\n**(2) Civil action by others**\nA qualified individual, class, or entity, described in paragraph (1)(A), including an employee or employment entity alleging a violation by a commercial provider, may bring a civil action alleging a violation of subsection (a)(1) or subsection (c), as the case may be, of section 4 (including a related provision of the final rule issued under section 5(b)) in an appropriate State or Federal court without first filing a complaint with the Commission or exhausting any other administrative remedies.\n**(3) Functions of the Attorney General**\nThe Attorney General shall carry out any function of the Commission under this subsection that the Attorney General carries out under section 107 of the ADA ( 42 U.S.C. 12117 ).\n##### (c) Relief\n**(1) Civil action by Attorney General or Commissioner**\nIn a civil action brought under subsection (a)(1) or (b)(1), the Attorney General or Commissioner may seek\u2014\n**(A)**\na civil penalty and all appropriate injunctive relief to bring the affected web content or application into compliance with section 4; and\n**(B)**\non behalf of affected individuals, all economic and noneconomic damages including compensatory and punitive damages.\n**(2) Civil action by others**\nIn a civil action brought under subsection (a)(2) or (b)(2), the plaintiff may seek all appropriate injunctive relief described in paragraph (1)(A) and the damages described in paragraph (1)(B).\n**(3) Attorney\u2019s fees**\nThe prevailing plaintiff (other than the United States) shall also be awarded reasonable attorney\u2019s fees and costs.\n#### 8. Recommendations\n##### (a) Advisory committee\n**(1) In general**\nThe Attorney General and the Commission shall establish a standing advisory committee (referred to in this section as the Committee ) on accessible web content and applications. The Committee shall be operated and receive resources in accordance with the provisions of chapter 10 of title 5, United States Code (commonly known as the Federal Advisory Committee Act ), as an advisory committee under the authority of the Attorney General and Commission.\n**(2) Composition**\nIn establishing the Committee, the Attorney General and the Commission\u2014\n**(A)**\nshall include on the Committee\u2014\n**(i)**\nindividuals with disabilities (comprising a majority of the members of the Committee) who are\u2014\n**(I)**\nindividuals who are blind (including who have low vision), deaf, hard of hearing, or deafblind;\n**(II)**\nindividuals who have speech disabilities;\n**(III)**\nindividuals with physical disabilities including those with limited to no manual dexterity; and\n**(IV)**\nindividuals who have disabilities not specified in any of subclauses (I) through (III);\n**(ii)**\nexperts regarding accessible web content and applications for individuals with disabilities; and\n**(iii)**\nat least one representative from the United States Access Board; and\n**(B)**\nmay include on the Committee representatives of\u2014\n**(i)**\nState and local government;\n**(ii)**\ncovered entities, including such entities who are small entities;\n**(iii)**\ncommercial providers;\n**(iv)**\ntesting entities; and\n**(v)**\nother entities determined to be appropriate by the Attorney General and the Commission.\n**(3) Functions**\nThe Committee shall provide responsive advice and guidance to the Attorney General and the Commission, for purposes of carrying out this Act, by\u2014\n**(A)**\nconducting public meetings twice per year, at a minimum;\n**(B)**\nsubmitting reports and recommendations to the Attorney General and Commission, and making the reports and recommendations publicly available, every 2 years at a minimum; and\n**(C)**\notherwise assisting the Attorney General and Commission in identifying and understanding the impact and implications of innovations with regard to accessible web content and applications.\n##### (b) Conferring\nThe Attorney General and the Commission, in carrying out this Act, shall confer with the National Council on Disability, the Architectural and Transportation Barriers Compliance Board, or any other Federal department or agency that may have relevant expertise or experience.\n#### 9. Technical assistance\n##### (a) Purpose\nIt is the purpose of this section to establish a technical assistance center to provide, to covered entities, commercial providers, individuals with disabilities, and other members of the public, information, resources, training, and technical assistance regarding\u2014\n**(1)**\nthe design, development, construction, alteration, modification, or addition of accessible web content and applications in accordance with this Act; and\n**(2)**\nthe rights of individuals with disabilities, covered entities, and commercial providers to access web content and applications in accordance with the ADA ( 42 U.S.C. 12101 et seq. ) and this Act.\n##### (b) Support for training and technical assistance\nFrom amounts made available under section 13, the Attorney General, in coordination with the Commission, the Secretary of Education, the United States Access Board, and other heads of Federal agencies, as appropriate shall award, on a competitive basis, at least 1 grant, contract, or cooperative agreement to a qualified training and technical assistance provider to support the development, establishment, and procurement of accessible web content and applications.\n##### (c) Application\n**(1) In general**\nTo be eligible to receive a grant, contract, or cooperative agreement under this section, an entity shall submit an application to the Attorney General at such time, in such manner, and containing such information as the Attorney General may require.\n**(2) Input**\nIn awarding a grant, contract, or cooperative agreement under this section and in reviewing the activities proposed under the applications described in paragraph (1), the Attorney General, in coordination with the Commission, the Secretary of Education, and other heads of Federal agencies, as appropriate\u2014\n**(A)**\nshall consider the input of\u2014\n**(i)**\nindividuals with disabilities who are\u2014\n**(I)**\nindividuals who are blind (including individuals who have low vision), deaf, hard of hearing, or deafblind;\n**(II)**\nindividuals who have speech disabilities;\n**(III)**\nindividuals with physical disabilities, including individuals with limited to no manual dexterity; and\n**(IV)**\nindividuals who have disabilities not specified in any of subclauses (I) through (III);\n**(ii)**\nexperts regarding accessible web content and applications for use by individuals with disabilities; and\n**(iii)**\nthe United States Access Board; and\n**(B)**\nmay consider the input of\u2014\n**(i)**\nState and local government;\n**(ii)**\ncovered entities;\n**(iii)**\ncommercial providers;\n**(iv)**\ntesting entities; and\n**(v)**\nother entities determined to be appropriate by the Attorney General, in coordination with the Commission, the Secretary of Education, and other heads of Federal agencies, as appropriate.\n##### (d) Authorized activities\n**(1) Use of funds**\n**(A) Requests for information**\nAn entity receiving a grant, contract, or cooperative agreement under this section shall support a training and technical assistance program that addresses information requests, concerning accessible web content and applications, from covered entities and commercial providers, including requests for information regarding\u2014\n**(i)**\neffective approaches for developing, establishing, and procuring accessible web content and applications;\n**(ii)**\nstate-of-the-art, or model, Federal, State, and local laws, regulations, policies, practices, procedures, and organizational structures, that facilitate, and overcome barriers to, receipt of funding for, and access to, accessible web content and applications; and\n**(iii)**\nexamples of policies, practices, procedures, regulations, or judicial decisions that have enhanced or may enhance access to and receipt of funding for accessible web content and applications.\n**(B) Coordination**\nAn entity receiving a grant, contract, or cooperative agreement under this section may also provide technical assistance and training, concerning accessible web content and applications, for covered entities and commercial providers by\u2014\n**(i)**\nfacilitating onsite and electronic information sharing using state-of-the-art internet technologies such as real-time online discussions, multipoint video conferencing, and web-based audio or video broadcasts, on emerging topics regarding accessible web content and applications;\n**(ii)**\nconvening experts to discuss and make recommendations with regard to national emerging issues regarding accessible web content and applications;\n**(iii)**\nsharing best practices and evidence-based practices in developing, establishing, and procuring accessible web content and applications;\n**(iv)**\nsupporting and coordinating activities designed to reduce the financial costs of purchasing technology needed to access accessible web content and applications; and\n**(v)**\ncarrying out such other activities as the Attorney General, in coordination with the Commission, the Secretary of Education, the United States Access Board, and other heads of Federal agencies, as appropriate may require.\n**(C) Collaboration**\nIn developing and providing training and technical assistance under this section, an entity receiving a grant, contract, or cooperative agreement under this section shall collaborate with\u2014\n**(i)**\norganizations representing individuals with disabilities;\n**(ii)**\norganizations or entities that provide services for individuals with disabilities, such as centers for independent living, as defined in section 702 of the Rehabilitation Act of 1973 ( 29 U.S.C. 796a );\n**(iii)**\nentities, such as the World Wide Web Consortium and the National Institute of Standards and Technology, that develop international standards for accessible web content and applications;\n**(iv)**\nexisting (existing as of the date of the application for the award involved) technical assistance entities, such as the ADA National Network;\n**(v)**\nFederal, State, and territorial agencies that provide assistance to small businesses;\n**(vi)**\norganizations or entities representing State or local government, and educational web content and technology professionals;\n**(vii)**\nentities or individuals with expertise and experience in enforcing disability rights law; and\n**(viii)**\nother entities and technical assistance providers determined to be appropriate by the Attorney General, in coordination with the Commission, the Secretary of Education, the United States Access Board, and other heads of Federal agencies, as appropriate.\n**(D) Grant administration**\nAn entity receiving a grant, contract, or cooperative agreement under this section may use funds made available under section 13 to administer a program to make subgrants to small entities, pursuant to section 11.\n#### 10. Study and report on emerging technologies\n##### (a) Study and report\n**(1) In general**\nThe National Council on Disability (in this section referred to as the Council ) shall conduct a study and prepare a report on\u2014\n**(A)**\nthe effect that emerging technologies have on the ability of individuals with disabilities to participate in employment, education, government, health care, commerce, culture, and other aspects of society; and\n**(B)**\nthe effectiveness of this Act in achieving its purpose.\n**(2) Consideration of effect on individuals with particular barriers**\nIn conducting the study and preparing the report, the Council shall consider the effect of emerging technologies on individuals with disabilities who use those technologies and have particular barriers to such participation and communication, such as individuals with disabilities using those technologies\u2014\n**(A)**\nwho have limited language or limited English language;\n**(B)**\nwho have significant or targeted disabilities (including people who are blind, deaf, or deafblind);\n**(C)**\nwho have disabilities limiting communication;\n**(D)**\nwhose household income is at or below 200 percent of the poverty line, as defined by the Federal poverty guidelines of the Department of Health and Human Services;\n**(E)**\nwho lack access to broadband services and technology; or\n**(F)**\nwho are multiply marginalized due to race, ethnicity, national origin, age, sex, sexual orientation, gender identity, or socioeconomic status.\n##### (b) Submission of report\nFive years after the date of enactment of this Act, the Council shall submit the report required under subsection (a) to the appropriate committees of Congress, which shall at minimum include the Committee on Health, Education, Labor, and Pensions and the Committee on the Judiciary of the Senate and the Committee on Education and Workforce and the Committee on the Judiciary of the House of Representatives.\n#### 11. Grants to small entities\n##### (a) Purpose\nThe purpose of this section is to award grants to provide assistance to small entities to enable the entities to remediate or replace existing (as of the date of application for the award) web content and applications to enable the small entities to comply with the regulations established under this Act.\n##### (b) Support for remediation activities\n**(1) In general**\nFrom amounts made available under section 13, for each of the first 5 years after the date of issuance, the recipient of the award under section 9 (relating to a technical assistance center), in coordination with the Attorney General and the Commission, shall award grants, in amounts not to exceed $10,000, to small entities to support auditing, testing, and remediating inaccessible web content or applications or to support procurement of accessible web content and applications to replace inaccessible web content or applications, in accordance with this Act.\n**(2) Date of issuance**\nIn this subsection, the term date of issuance means the date that is the earlier of the first day on which a final rule is issued under section 5(a) and the first day on which a final rule is issued under section 5(b).\n##### (c) Application\nTo be eligible to receive a grant under this section, a small entity shall submit an application to the Attorney General and the Commission (or the recipient of the award under section 9) at such time, in such manner, and containing such information as the Attorney General and the Commission (or the recipient of the award under section 9) may require. At a minimum, the applicant shall demonstrate\u2014\n**(1)**\nthat the entity is a small entity;\n**(2)**\n**(A)**\nif the entity is a covered entity, that it owns, operates, or utilizes inaccessible web content or an application that requires remediation or replacement for the entity to comply with this Act; or\n**(B)**\nif the entity is a commercial provider, that it provides, to a covered entity, inaccessible web content or an application that requires remediation for the provider to comply with this Act; and\n**(3)**\nthat the small entity has a plan to remediate or replace, as appropriate, the inaccessible web content or application, so that the entity complies with this Act.\n##### (d) Authorized activities\nA small entity receiving a grant under this section\u2014\n**(1)**\nmay use the grant funds, directly or through a subgrant, to audit, test, or remediate the inaccessible web content or application or procure new accessible web content or an application to replace the inaccessible web content or application;\n**(2)**\nshall use the grant funds to demonstrate that the resulting web content or application is accessible; and\n**(3)**\nmay not use the grant funds to design, develop, or procure inaccessible web content or an inaccessible application.\n#### 12. Rules of construction\n##### (a) Other provisions of law\nNothing in this Act shall be construed to affect the scope of obligations imposed by any other provision of law, including\u2014\n**(1)**\nsection 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ), title I, II or III of the ADA ( 42 U.S.C. 12131 et seq. ), and section 1557 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18116 ); and\n**(2)**\nsection 508 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794d ) and section 255 of the Communications Act of 1934 ( 47 U.S.C. 255 ).\n##### (b) Relationship to other laws\nNothing in this Act shall be construed to invalidate or limit the remedies, rights, and procedures of any Federal law or law of any State or political subdivision of any State or jurisdiction, that provides greater or equal protection for the rights of individuals with disabilities than is afforded by this Act.\n##### (c) Consistent regulations\nRegulations promulgated under this Act shall be consistent with, and shall not contain a standard less protective of individuals with disabilities than, the standards contained in\u2014\n**(1)**\nany regulations issued by the Attorney General or the Commission pursuant to\u2014\n**(A)**\ntitle I of the ADA ( 42 U.S.C. 12111 et seq. ) for digital access to an item related to an activity described in section 102 of the ADA ( 42 U.S.C. 12112 ), by covered entities;\n**(B)**\ntitle II of the ADA ( 42 U.S.C. 12131 et seq. ) for digital access to services, programs, or activities, including information related to such services, programs, or activities of covered entities; or\n**(C)**\ntitle III of the ADA ( 42 U.S.C. 12181 et seq. ) for digital access to goods, services, facilities, privileges, advantages, accommodations, including information related to such goods, services, facilities, privileges, advantages, or accommodations of covered entities; and\n**(2)**\nthe regulations issued by the Federal Communications Commission for video programming and communications services provided via web content and applications.\n##### (d) Prohibition on notification requirement\nThe Attorney General and the Commission shall not include, in the accessibility regulations, any requirement that an individual shall notify a covered entity or commercial provider of an allegation of a violation of this Act prior to commencing a civil action under this Act.\n#### 13. Authorization of appropriations\nThere are authorized to be appropriated $35,150,000 for each of fiscal years 2026 through 2035 to carry out this Act.\n#### 14. Effective date\nThis Act shall take effect 6 months after the date of enactment of this Act, except that section 4 shall apply to covered entities and commercial providers 12 months after that date of enactment.",
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
        "actionDate": "2026-03-03",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3974",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Websites and Software Applications Accessibility Act of 2026",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-05-30T12:07:49Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3417ih.xml"
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
      "title": "Websites and Software Applications Accessibility Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Websites and Software Applications Accessibility Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish uniform accessibility standards for websites and applications of employers, employment agencies, labor organizations, joint labor-management committees, public entities, public accommodations, testing entities, and commercial providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T05:18:51Z"
    }
  ]
}
```
