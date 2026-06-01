# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4247?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4247
- Title: Guardianship Bill of Rights Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4247
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-20T19:06:06Z
- Update date including text: 2026-04-20T19:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4247",
    "number": "4247",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Guardianship Bill of Rights Act of 2026",
    "type": "S",
    "updateDate": "2026-04-20T19:06:06Z",
    "updateDateIncludingText": "2026-04-20T19:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T19:42:28Z",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-03-26",
      "state": "VT"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4247is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4247\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Ms. Duckworth (for herself, Mr. Sanders , and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish rights for people being considered for and in protective arrangements, including guardianships and conservatorships, or other arrangements, to provide decision supports.\n#### 1. Short title\nThis Act may be cited as the Guardianship Bill of Rights Act of 2026 .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nAt least 1,300,000 people in the United States are in some type of guardianship or other protective arrangement.\n**(2)**\nA majority of guardianships are plenary and strip almost all rights from individuals, with the restoration of rights being very rare.\n**(3)**\nGuardianship can have grave implications limiting the liberty of people in such an arrangement.\n**(4)**\nOverbroad, restrictive, and unnecessary guardianships, conservatorships, and other protective arrangements can dramatically curtail the rights of older adults and persons with disabilities.\n**(5)**\nA person who is being considered for a protective arrangement, or is in a protective arrangement, including an individual in a guardianship or conservatorship, has a set of fundamental rights including\u2014\n**(A)**\na right, prior to the imposition of a protective arrangement, to exhaust less restrictive alternative arrangements for supports;\n**(B)**\n**(i)**\na right to an alternative arrangement, for anyone who needs decision supports but does not need a guardianship or conservatorship; and\n**(ii)**\na right to a supported decisionmaking arrangement for anyone who needs decision supports, whether being considered for or in a protective arrangement;\n**(C)**\na right to an independent, qualified lawyer who\u2014\n**(i)**\nspeaks solely for the person who is being considered for a guardianship or other protective arrangement, or who is in a protective arrangement;\n**(ii)**\nis free of a conflict of interest with the person\u2019s family members, and the corresponding governmental entities, social service agencies, and courts;\n**(iii)**\nrepresents the expressed wishes of the person who is being considered for or who is in a protective arrangement;\n**(iv)**\nis compensated at a reasonable fee through the use of public funds, if the person is not able to pay; and\n**(v)**\nis appointed by the court involved, if the person does not prefer to have a lawyer of the person\u2019s own choosing;\n**(D)**\nthe right to significant input and full participation into decisions about their life, including their health, education, finances, employment, housing, relationships, parenthood, politics, religious activities, and social activities, and other basic decisions affecting their life;\n**(E)**\nif in a protective arrangement, the right to a reasonable, timely method and information for reviewing, modifying, and discontinuing the protective arrangement;\n**(F)**\nif in a protective arrangement, the right to, at a minimum, an annual meaningful review of their protective arrangement that includes representation by a lawyer described in subparagraph (C); and\n**(G)**\na right to the least restrictive arrangement to provide support to a covered individual needing decision supports.\n##### (b) Purpose\nThe purpose of this Act is to create a process to establish a bill of rights for covered individuals who are being considered for or who are in a guardianship, conservatorship, supported decisionmaking arrangement, or other alternative arrangement, regarding the decisions of the individuals to ensure the fundamental rights of each such individual are protected and the individual has significant input into arrangements of the types described in this subsection.\n#### 3. Definitions\nIn this Act:\n**(1) Alternative arrangement**\nThe term alternative arrangement means an arrangement with key support personnel who may include family members, friends, and professionals, with an approach to meeting the needs of an individual to make decisions that restricts fewer rights of the individual than would the appointment of a guardian or conservator.\n**(2) Assistive technology device**\nThe term assistive technology device has the meaning given the term in section 3 of the Assistive Technology Act of 1998 ( 29 U.S.C. 3002 ).\n**(3) Covered individual**\nThe term covered individual means\u2014\n**(A)**\nan older adult; and\n**(B)**\na person with a disability.\n**(4) Developmental disability**\nThe term developmental disability has the meaning given the term in section 102 of the Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15002 ).\n**(5) Disability**\nThe term disability means a disability as defined in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 ).\n**(6) Guardianship**\nThe term guardianship means a legal relationship established by a court if an individual is determined to lack the ability to meet essential requirements for physical health, safety, or self-care because the person is unable to receive and evaluate information, or make or communicate decisions, about their person or property, even with appropriate supportive services, assistive technology devices, supported decisionmaking, or other less restrictive alternative arrangements.\n**(7) Indian Tribe**\nThe term Indian Tribe means an entity that\u2014\n**(A)**\nis eligible for funding as an Indian tribe under subpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ); and\n**(B)**\nis\u2014\n**(i)**\neligible for funding as an Indian tribe under title I of the Rehabilitation Act of 1973 ( 29 U.S.C. 720 et seq. ); or\n**(ii)**\neligible for funding through an American Indian consortium under subtitle C of title I of the Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15041 et seq. ).\n**(8) Limited guardianship**\nThe term limited guardianship means a guardianship in which a court-appointed fiduciary has the power to make decisions for an individual, with that power defined by the court and for the duration determined by the court.\n**(9) Local educational agency; State educational agency**\nThe terms local educational agency and State educational agency have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(10) Older adult**\nThe term older adult means an individual who is 60 years of age or older.\n**(11) Person with a disability**\nThe term person with a disability means any person who has a disability (including a sensory disability).\n**(12) Plenary guardianship**\nThe term plenary guardianship means a guardianship in which a court-appointed fiduciary has the power to make all decisions allowed by State law for an individual, often due to a finding that the individual is incapacitated.\n**(13) Protection and advocacy system**\nThe term protection and advocacy system means a protection and advocacy system established in accordance with section 143 of the Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15043 ).\n**(14) Protective arrangement**\nThe term protective arrangement means\u2014\n**(A)**\nan arrangement in which a person, acting under a limited court order authorizing support for an individual who the court has determined is in need of decision supports, has the power, for a duration specified in the order, to make such decisions for the individual, without a finding of incapacity or the appointment of a guardian or conservator; or\n**(B)**\na guardianship or conservatorship.\n**(15) Secretary**\nThe term Secretary refers to the Secretary of Health and Human Services or the designee of that Secretary.\n**(16) Standard**\nThe term standard means a requirement.\n**(17) State**\nThe term State means any of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, Guam, the Commonwealth of the Northern Mariana Islands, American Samoa, and any Indian Tribe.\n**(18) Supported decisionmaking arrangement**\nThe term supported decisionmaking arrangement means an agreement or other arrangement, resulting from a series of relationships, practices, and shorter arrangements, of greater or lesser formality and intensity, designed to assist an individual in understanding, making, and communicating the individual\u2019s own decisions in a way that does not impede the individual\u2019s self-determination, including deciding\u2014\n**(A)**\nwho provides the individual with supports for the decisions;\n**(B)**\nin which areas of life the individual receives supports, including decisions about health, services received, finances, property, living arrangements, and work; and\n**(C)**\nwith whom to associate through the support of people, technology, and other decisionmaking aids.\n#### 4. Guardianship and other protective arrangements and supported decisionmaking council\n##### (a) Establishment of a guardianship and other protective arrangements and supported decisionmaking council\n**(1) Establishment**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish in the Department of Health and Human Services a Guardianship and Other Protective Arrangements and Supported Decisionmaking Council (referred to in this Act as the Council ).\n**(2) Duties of the Council**\nThe Council shall advise the Secretary on the development of standards under section 5 related to guardianships, conservatorships, supported decisionmaking arrangements, and other alternative arrangements, including recommending standards on the fundamental rights (including the implementation of those rights) of a covered individual in a guardianship, conservatorship, supported decisionmaking arrangement, or other alternative arrangement.\n**(3) Guardianship bill of rights**\nThe Council's recommendations for those standards on the fundamental rights of a covered individual in a guardianship, conservatorship, supported decisionmaking arrangement, or other alternative arrangement (commonly known as the Guardianship Bill of Rights ) shall address, at minimum\u2014\n**(A)**\nthe scope of the fundamental rights, including the fundamental rights described in section 2(a)(5);\n**(B)**\nwhich fundamental rights cannot be restricted, which can be restricted but not delegated, and which can be restricted but only with further due process protections;\n**(C)**\ndue process protections to be provided, during consideration of an arrangement, to protect the fundamental rights;\n**(D)**\nthe fundamental rights related to\u2014\n**(i)**\nvoting access and decisionmaking;\n**(ii)**\ndecisionmaking concerning marriage and other relationships, including romantic, friendship, and family relationships;\n**(iii)**\nreproductive decisionmaking;\n**(iv)**\nfinancial decisionmaking on matters that do not jeopardize long-term security;\n**(v)**\neducational decisionmaking;\n**(vi)**\nhealth and medical decisionmaking, including the right to private communication between an individual and the individual\u2019s health care provider;\n**(vii)**\ndecisionmaking for religious observation and activities;\n**(viii)**\ndecisionmaking concerning a place of residency;\n**(ix)**\ndecisionmaking for visitation and association;\n**(x)**\ndecisionmaking for travel;\n**(xi)**\ncommunication; and\n**(xii)**\ndecisionmaking for daily decisions; and\n**(E)**\nmaintenance of a covered individual\u2019s fundamental rights in their decisionmaking.\n**(4) Membership**\n**(A) Background**\nThe Secretary shall appoint members to the Council. The Council shall be composed of 30 members that include\u2014\n**(i)**\nfive covered individuals currently (as of the date of appointment) using a supported decisionmaking arrangement;\n**(ii)**\nfour covered individuals currently (as of the date of appointment) in a protective arrangement;\n**(iii)**\nthree family members of covered individuals who are at risk of being in, or are in, protective arrangements;\n**(iv)**\ntwo lawyers, including at least 1 of whom\u2014\n**(I)**\nis a lawyer who has served a protection and advocacy system or legal services organization;\n**(II)**\nhas experience in representation of covered individuals in contesting or limiting guardianships; and\n**(III)**\nhas experience in supported decisionmaking arrangements, other alternative arrangements, and protective arrangements;\n**(v)**\ntwo judges with experience managing contested and uncontested guardianships;\n**(vi)**\ntwo teachers or special education personnel from an elementary school or secondary school;\n**(vii)**\ntwo behavioral health care professionals;\n**(viii)**\none independent living specialist;\n**(ix)**\ntwo other professionals with extensive knowledge of supported decisionmaking arrangements;\n**(x)**\ntwo representatives of disability-led organizations, meaning organizations for which at least 50 percent of the staff have a disability, or 50 percent of the members of the governing body have a disability;\n**(xi)**\ntwo representatives of organizations representing older adults;\n**(xii)**\none guardian, who shall be a certified guardian if the State involved provides for such certifications;\n**(xiii)**\none guardianship investigator; and\n**(xiv)**\none representative of a State developmental disability agency, State agency on aging, or State adult protective services agency.\n**(B) Diversity**\nMembers of the Council shall represent diverse racial, ethnic, religious, gender, geographic, socioeconomic, religious, age, and disability categories.\n**(C) Period of appointment; vacancies**\n**(i) Term**\nMembers shall be appointed for a 3-year term and may be reappointed for one additional term.\n**(ii) Vacancies**\nAny vacancy in the Council shall not affect its powers, but shall be expeditiously filled by the Secretary.\n**(D) Chair; Vice Chair**\nAt the first meeting of the Council, the Council shall select a Chair and Vice Chair from among its members. The Council shall select a member with the characteristics described in clause (i) or (ii) of subparagraph (A) to fill at least one of those positions.\n**(5) Council reports**\n**(A) Initial report**\nThe Council shall prepare a report in which it makes its initial recommendations on the standards described in section 5, not later than 2 years after the date of the Council's establishment.\n**(B) Subsequent reports**\nFor the 10-year period beginning on that date of establishment, not later than 4 years after that date and not later than every 2 years thereafter, the Council will review the standards established under section 5 and prepare a report in which it makes its subsequent recommendations on the standards.\n**(C) Submission**\nThe Council shall make the reports described in this paragraph publicly available and submit the reports to\u2014\n**(i)**\nthe Secretary;\n**(ii)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate;\n**(iii)**\nthe Special Committee on Aging of the Senate;\n**(iv)**\nthe Committee on the Judiciary of the Senate;\n**(v)**\nthe Committee on Education and Workforce of the House of Representatives;\n**(vi)**\nthe Committee on Energy and Commerce of the House of Representatives; and\n**(vii)**\nthe Committee on the Judiciary of the House of Representatives.\n**(6) Personnel matters**\n**(A) No additional compensation**\nMembers of the Council who are officers or employees of the United States shall serve without compensation in addition to that received for their services as officers or employees of the United States. Other members of the Council shall serve without compensation for the performance of services for the Council. Notwithstanding section 1342 of title 31, United States Code, the Secretary may accept the voluntary and uncompensated services of members of the Council.\n**(B) Travel expenses**\nThe members of the Council shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies in subchapter I of chapter 57 of title 5, United States Code, while away from their homes or regular places of business in the performance of services for the Council.\n**(C) Detail of government employees**\nAny Federal Government employee may be detailed to the Council without reimbursement, and such detail shall be without interruption or loss of civil service status or privilege.\n##### (b) Termination\nThe Council shall terminate 10 years after the date of the establishment of the Council.\n#### 5. Standards for guardianships, conservatorships, and alternative arrangements\n##### (a) Standards for establishing, reviewing, modifying, and discontinuing guardianships, conservatorships, or other protective arrangements\nThe Secretary, through the Administrator of the Administration for Community Living, with significant input from the Council, shall develop standards for establishing, reviewing, modifying, and discontinuing any protective arrangement for a covered individual, including guardianships and conservatorships, including standards for each of the following:\n**(1)**\nEstablishing protective arrangements.\n**(2)**\nEstablishing frequencies, of not more than 1 year, for regular review of protective arrangements by the court of jurisdiction.\n**(3)**\nGuaranteed procedures for modification or discontinuation of protective arrangements.\n**(4)**\nGuaranteed representation by an independent, qualified, and compensated lawyer described in section 2(a)(5)(C) for the covered individual being considered for a protective arrangement or in a protective arrangement.\n**(5)**\nAccess to due process while the individual is being considered for a protective arrangement and while in a protective arrangement.\n**(6)**\nOptions for full restoration of rights for a covered individual in a protective arrangement.\n**(7)**\nOrdering limited protective arrangements when less restrictive arrangements, such as supported decisionmaking arrangements, are not appropriate.\n**(8)**\n**(A)**\nCollecting detailed data at the national and State levels on the use of guardianships and other protective arrangements, supported decisionmaking arrangements, and other alternative arrangements.\n**(B)**\nReporting that data, taken as a whole and disaggregated by gender identity, race, ethnicity, sexual orientation, income level, living situation, age, disability type, and reason for guardianship or other protective arrangement.\n##### (b) Standards for establishing supported decisionmaking and other alternative arrangements\nThe Secretary, through the Administrator of the Administration for Community Living, with significant input from the Council, shall develop system standards and other standards for establishing supported decisionmaking arrangements and other alternative arrangements as the default decision support options for covered individuals to avert the use of guardianship or a more restrictive protective arrangement, including\u2014\n**(1)**\nsystem standards that promote supported decisionmaking arrangements and other alternative arrangements for decisionmaking arrangements, including decisionmaking arrangements within local educational agencies, health care systems, disability and aging services systems, financial institutions, and court systems;\n**(2)**\nstandards for the areas (such as education, finance, and health) in which a covered individual requires decisionmaking supports;\n**(3)**\nstandards for how a covered individual using a supported decisionmaking arrangement will select the persons to serve on the supported decisionmaking team;\n**(4)**\nstandards for additional supports, such as assistive technology devices, required to ensure maximum participation by covered individuals in their decisionmaking; and\n**(5)**\nstandards for interrupting the processes that lead to guardianship or conservatorship through retraining key decisionmakers, such as court personnel and administrators, to recognize overbroad petitions for guardianships or conservatorships.\n##### (c) Standards for transitioning from guardianships to alternative arrangements\nThe Secretary, with significant input from the Council and a stakeholder group process, shall\u2014\n**(1)**\nestablish standards, for transitioning covered individuals from guardianship or conservatorship arrangements into supported decisionmaking arrangements or other alternative arrangements, that restore the rights of individuals in appropriate circumstances; and\n**(2)**\nestablish standards that\u2014\n**(A)**\nrequire a periodic review of guardianships and conservatorships, to transition covered individuals in either type of arrangement to a supported decisionmaking arrangement or another alternative arrangement;\n**(B)**\nprovide for such a review at least once a year for such covered individuals; and\n**(C)**\nrequire that a review of a guardianship or conservatorship occurs if such a covered individual requests that review.\n##### (d) Minimum standards for establishment and review of protective arrangements\nThe Secretary, with significant input from the Council, shall\u2014\n**(1)**\nestablish standards for establishing guardianships or other protective arrangements, including in the case of a plenary guardianship, standards for health, medical, and financial well-being reviews by the corresponding members serving on a guardianship review panel before the guardianship is established and during reviews described in paragraph (4);\n**(2)**\ncreate standards for individuals eligible to serve on such a review panel, which shall include lawyers, and advocates, with experience protecting the civil rights described in subsection (a), other professionals with experience in protective arrangements (such as doctors, psychologists, and certified financial planners), and covered individuals;\n**(3)**\nestablish standards requiring background checks of individuals seeking to serve on guardianship review panels; and\n**(4)**\nestablish standards for reviews of protective arrangements described in section 2(a)(5)(F).\n##### (e) Availability and accessibility\nThe Secretary shall make the standards described in this section, and information on the standards, available and accessible to covered individuals, family members and guardians of covered individuals, judges and court personnel, school personnel, minority language communities, and additional appropriate entities and individuals.\n##### (f) Relation to other law\nA State that seeks funding under\u2014\n**(1)**\ntitle I of the Rehabilitation Act of 1973 ( 29 U.S.C. 720 et seq. ) shall include, in the State plan submitted under section 101 of that Act ( 29 U.S.C. 721 ) or the application submitted under section 121 of that Act ( 29 U.S.C. 741 ), as the case may be, an assurance that the State is implementing and enforcing the standards described in this section and issued by the Secretary, other than subsection (c); and\n**(2)**\nsubtitle B or C of the Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15021 et seq. , 15041 et seq.) shall include, in the State plan submitted under section 124 of that Act ( 42 U.S.C. 15024 ) or the materials demonstrating eligibility under section 143 of that Act ( 42 U.S.C. 15043 ), as the case may be, the assurance described in paragraph (1).\n#### 6. Protection and advocacy program for oversight of protective arrangements\nTitle I of the Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15001 et seq. ) is amended by adding at the end the following:\nF Protective Arrangements Oversight 171. Protection and advocacy program for oversight of protective arrangements (a) Definitions In this section: (1) American Indian Consortium; State The terms American Indian Consortium and State have the meanings given the terms in section 102. (2) Guardianship Bill of Rights definitions Except as provided in paragraphs (1) and (3), the terms used in this section have the meanings given the terms in section 3 of the Guardianship Bill of Rights Act of 2026. (3) Protection and advocacy system The term protection and advocacy system means\u2014 (A) a protection and advocacy system established in accordance with section 143; and (B) an American Indian Consortium that provides protection and advocacy services under section 142. (b) Establishment The Secretary, acting through the Administrator for the Administration for Community Living, shall establish a Protection and Advocacy Program, for oversight and monitoring of State and local guardianships, conservatorships, and other protective arrangements. (c) Grants The Secretary shall make a grant to each protection and advocacy system to establish or expand a Protection and Advocacy Program for Oversight of Protective Arrangements. (d) Authority In order for a protection and advocacy system for a State or serving an American Indian tribe to receive a grant under this section\u2014 (1) the State or tribe shall have in effect a protective arrangement oversight system to protect and advocate for the rights of covered individuals concerning protective arrangements; and (2) the protective arrangement oversight system shall have the authority to\u2014 (A) pursue legal, administrative, and other appropriate remedies or approaches to ensure the protection of, and advocacy for, the rights of covered individuals within the State or American Indian tribe who are being considered for or in a protective arrangement; (B) provide legal representation to covered individuals who\u2014 (i) are facing a proceeding to establish a protective arrangement; or (ii) who desire to modify or discontinue a protective arrangement; (C) provide information, referrals, training, and legal representation to enable a covered individual to establish or defend a supported decisionmaking arrangement or another alternative arrangement, including providing such services in plain language, American Sign Language, and other minority languages; and (D) investigate incidents of abuse of guardianships and other protective arrangements. (e) Use of funds (1) In general An entity that receives a grant under this section for a protective arrangement oversight system shall carry out the activities described in subsection (d) or (f). (2) Limitation The protective arrangement oversight system may not use the grant funds to provide legal representation, or other services, to persons seeking to establish or maintain (with or without modification) a guardianship or conservatorship. (f) Reports Each entity that receives a grant under this section for a protective arrangement oversight system shall prepare and submit to the Secretary, in accordance with such requirements as the Secretary may specify, information on activities carried out through the corresponding program described in subsection (c). (g) Authorization of appropriations There is authorized to be appropriated to carry out this section $50,000,000 for fiscal year 2027 and each succeeding fiscal year. .",
      "versionDate": "2026-03-26",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-04-20T19:06:06Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4247is.xml"
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
      "title": "Guardianship Bill of Rights Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T03:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guardianship Bill of Rights Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T03:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish rights for people being considered for and in protective arrangements, including guardianships and conservatorships, or other arrangements, to provide decision supports.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T03:33:29Z"
    }
  ]
}
```
