# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8256?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8256
- Title: Senior Hunger Prevention Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8256
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-04-29T15:12:31Z
- Update date including text: 2026-04-29T15:12:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-04-14: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-04-14: Introduced in House

## Actions

- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8256",
    "number": "8256",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
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
    "title": "Senior Hunger Prevention Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-29T15:12:31Z",
    "updateDateIncludingText": "2026-04-29T15:12:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-14",
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
          "date": "2026-04-14T16:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "OR"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "VT"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "TN"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MI"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "FL"
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
      "sponsorshipDate": "2026-04-14",
      "state": "NY"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "IL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "RI"
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
      "sponsorshipDate": "2026-04-14",
      "state": "VA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "KY"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-14",
      "state": "DC"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NV"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "PA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8256ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8256\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Ms. Bonamici (for herself, Ms. Salinas , Ms. Balint , Ms. Barrag\u00e1n , Ms. Brownley , Mr. Cohen , Mrs. Dingell , Ms. Lois Frankel of Florida , Mr. Goldman of New York , Mr. Jackson of Illinois , Ms. Lee of Pennsylvania , Mr. Magaziner , Ms. McClellan , Mr. McGarvey , Mr. Morelle , Ms. Norton , Ms. Scanlon , and Ms. Simon ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to streamline nutrition access for older adults and adults with disabilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Senior Hunger Prevention Act of 2026 .\n#### 2. Improving efficacy of the supplemental nutrition assistance program\n##### (a) Certification period\nSection 3(f) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(f) ) is amended, in the second sentence, by striking 24 and inserting 36 .\n##### (b) Standard medical expense deduction\nSection 5(e)(5) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014(e)(5) ) is amended\u2014\n**(1)**\nin the paragraph heading, by striking Excess medical and inserting Medical ;\n**(2)**\nin subparagraph (A), by striking an excess medical and all that follows through the period at the end and inserting a standard medical deduction or a medical expense deduction of actual costs for the allowable medical expenses incurred by the elderly or disabled member, exclusive of special diets. ;\n**(3)**\nin subparagraph (B)(i), by striking excess ; and\n**(4)**\nby adding at the end the following:\n(D) Standard medical expense deduction amount (i) In general Except as provided in clause (ii), the standard medical expense deduction shall be equal to\u2014 (I) for fiscal year 2027, $155; and (II) for each subsequent fiscal year, the applicable amount for the immediately preceding fiscal year, as adjusted to reflect changes for the 12-month period ending the preceding June 30 in the Consumer Price Index for All Urban Consumers: Medical Care published by the Bureau of Labor Statistics of the Department of Labor. (ii) Exception For any fiscal year, a State agency may establish a greater standard medical expense deduction than the deduction described in clause (i) if the greater deduction satisfies the applicable cost-neutrality standards established by the Secretary for that fiscal year. .\n##### (c) Value of allotment\nSection 8(a) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2017(a) ) is amended, in the proviso, by striking 8 percent and inserting 1/3 .\n#### 3. Streamlining nutrition access for older adults and adults with disabilities\n##### (a) Definition of elderly and disabled\nSection 3(j)(2)(B) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(j)(2)(B) ) is amended by inserting (which includes medical assistance provided to an individual described in section 1902(e)(14)(D)(i)(III) of the Social Security Act ( 42 U.S.C. 1396a(e)(14)(D)(i)(III) )) after ( 42 U.S.C. 1396 et seq. ) .\n##### (b) Elderly Simplified Application Program\nThe Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) is amended by adding at the end the following:\n31. Elderly Simplified Application Program (a) In general Not later than 180 days after the date of enactment of this section, the Secretary shall establish a program, to be known as the elderly simplified application program (referred to in this section as ESAP ), under which a State, in carrying out the supplemental nutrition assistance program, may elect to implement a streamlined application and certification process for households in which all adult members\u2014 (1) are elderly or disabled members; and (2) have no earned income. (b) Certification period The certification period for participants in ESAP shall be 36 months. (c) Income and other data verification (1) In general A State agency determining the eligibility for an applicant household under ESAP shall, notwithstanding section 11(e)(3)\u2014 (A) to the maximum extent practicable, use data matching for income verification and household size; and (B) (i) allow self-declaration by the applicant of the information required under section 273.2(f) of title 7, Code of Federal Regulations (or a successor regulation); but (ii) verify, prior to certification of the household, factors of eligibility provided by the applicant that the State agency determines are questionable. (2) Accountability and fraud prevention In carrying out paragraph (1), a State agency shall establish accountability and fraud protection measures to deter fraud and ensure the integrity of ESAP and the supplemental nutrition assistance program. (d) Interviews Notwithstanding section 11(e)(6)(A), for recertification of a household under ESAP, a State agency shall not require an interview unless requested by the household, which may be conducted virtually. (e) Guidance Prior to the establishment of ESAP under subsection (a), the Administrator of the Food and Nutrition Service shall develop guidance for States, including by consulting with States, to carry out ESAP, which shall include\u2014 (1) general implementation guidelines; (2) reporting requirements; (3) quality control requirements; and (4) best practices. .\n##### (c) Combined Application Program\nThe Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) (as amended by subsection (b)) is amended by adding at the end the following:\n32. Combined application program (a) In general Not later than 180 days after the date of enactment of this section, the Secretary, in coordination with the Commissioner of Social Security, shall establish a program, to be known as the \u2018combined application program\u2019 (referred to in this section as CAP ), under which a State, in carrying out the supplemental nutrition assistance program, may elect to implement a streamlined application process for households in which all adult members are applicants for or recipients of benefits under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ) on the basis of a disability or supplemental security income under title XVI of that Act ( 42 U.S.C. 1381 et seq. ). (b) Purposes The purposes of CAP are\u2014 (1) to reduce the need for households described in subsection (a) to have in-person interviews with State offices administering the supplemental nutrition assistance program; and (2) to increase participation in the supplemental nutrition assistance program by simplifying the application process for that program through increased automation and simplified calculation of benefits. (c) CAP models The Secretary, in coordination with the Commissioner of the Social Security Administration, shall offer, at a minimum, each of the following models for States to implement CAP: (1) Standard model (A) In general Under the standard model, the Commissioner of the Social Security Administration and the State agency administering the supplemental nutrition assistance program shall coordinate\u2014 (i) to develop a simplified joint application process for the supplemental nutrition assistance program that uses standardized benefit amounts or standardized shelter expenses, in accordance with this paragraph; and (ii) to conduct outreach to adult members receiving supplemental security income under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ) that are not receiving benefits under the supplemental nutrition assistance program. (B) Standardized benefit amounts (i) In general Under the standardized model described in subparagraph (A), applicants shall receive a standardized or automated benefit level under the supplemental nutrition assistance program based on the shelter expenses and other income of the applicants. (ii) Minimum standardized benefit levels At a minimum, there shall be 2 standardized benefit levels under clause (i), including, as determined by the State\u2014 (I) a level for participants with low shelter expenses; and (II) a level for participants with high shelter expenses. (iii) Comparable amount A State shall ensure that the amount provided under a standardized benefit level under clause (i) is comparable to an amount that a participant would otherwise receive under the supplemental nutrition assistance program. (iv) Referral A State shall refer a household described in subsection (a) to the supplemental nutrition assistance program instead of enrolling that household in CAP if the standardized amount that the household would receive under CAP would be significantly less than the amount of benefits that the household would receive under the supplemental nutrition assistance program. (C) Standardized shelter expenses In computing an excess shelter expense deduction under section 5(e)(6), a State agency may use a standard utility allowance in accordance with regulations promulgated by the Secretary. (2) Modified model Under the modified model, a State agency administering the supplemental nutrition assistance program shall\u2014 (A) conduct outreach to prospective participants in the supplemental nutrition assistance program using information from the Social Security Administration to identify households described in subsection (a) that are not participants in the supplemental nutrition assistance program; and (B) send to those households simplified application forms for the supplemental nutrition assistance program. .\n#### 4. Enrollment and outreach pilot program for older adults, kinship families, and adults with disabilities\nThe Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) (as amended by section 3(c)) is amended by adding at the end the following:\n33. Enrollment and outreach pilot program for older adults, kinship families, and adults with disabilities (a) Definitions In this section: (1) Disability The term disability has the meaning given the term in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 ). (2) Eligible entity The term eligible entity means\u2014 (A) a State or local government agency; (B) an Indian tribe or Tribal organization; (C) a nonprofit organization, including a public or nonprofit provider of services; (D) a community-based organization; and (E) an educational provider. (3) Kinship family The term kinship family means a family in which a child resides with, and is being raised by, a grandparent, another extended family member, or an adult with whom the child has a close family-like relationship, such as a godparent or a close family friend. (4) Older adult The term older adult has the meaning given the term older individual in section 102 of the Older Americans Act of 1965 ( 42 U.S.C. 3002 ). (5) Pilot program The term pilot program means the Enrollment and Outreach Pilot Program for Older Adults, Kinship Families, and Adults with Disabilities established under subsection (b). (b) Establishment Not later than 180 days after the date of enactment of this section, the Secretary shall establish a pilot program, to be known as the Enrollment and Outreach Pilot Program for Older Adults, Kinship Families, and Adults with Disabilities , under which the Secretary shall award grants to eligible entities\u2014 (1) to raise awareness among older adults, kinship families, and adults with disabilities of the availability, eligibility requirements, application procedures, and benefits of the supplemental nutrition assistance program; and (2) to support older adults, kinship families, and adults with disabilities in enrolling in the supplemental nutrition assistance program. (c) Priority In awarding grants under the pilot program, the Secretary shall give priority to\u2014 (1) eligible entities that\u2014 (A) provide services to older adults or adults with disabilities; (B) provide services to kinship families, including kinship navigator programs; (C) have experience implementing programs that receive funding under the Older Americans Act of 1965 ( 42 U.S.C. 3001 et seq. ); (D) have experience implementing programs administered by the Food and Nutrition Service; or (E) receive, plan to receive, or demonstrate an ability to partner with a program that receives, funding under\u2014 (i) the Older Americans Act of 1965 ( 42 U.S.C. 3001 et seq. ); (ii) the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ); or (iii) 1 or more nutrition programs administered by the Secretary; and (2) projects that will\u2014 (A) serve communities with high rates of food insecurity, malnutrition, or low food access; (B) serve rural communities, indigenous communities, or communities of color; (C) serve members of the lesbian, gay, bisexual, transgender, and queer community; (D) serve adults with limited English proficiency; (E) serve veterans; (F) serve residents in federally subsidized housing, including federally subsidized housing units for older adults and adults with disabilities; (G) serve residents living in housing serving kinship families; and (H) incorporate nutrition education activities that promote healthy eating and active lifestyles. (d) Eligible activities An eligible entity receiving a grant under the pilot program shall use the grant to carry out 1 or more of the following activities: (1) Application assistance, including\u2014 (A) eligibility prescreening; (B) assistance in completing an application for the supplemental nutrition assistance program; (C) assistance in obtaining application verification documents; (D) medical expense deduction counseling; and (E) translation of materials and bilingual accommodation. (2) Tailored dissemination of information relating to the supplemental nutrition assistance program, including through\u2014 (A) community-based outreach workshops and events; (B) a toll-free hotline to provide information about Federal, State, and local food resources; (C) informational websites and other social media sites; and (D) printed or digital informational content. (3) Transportation, including\u2014 (A) transportation to or from a local office of the supplemental nutrition assistance program; and (B) administration of vouchers or similar items for the transportation described in subparagraph (A). (4) Identification, implementation, analysis, and dissemination of replicable and scalable models for increasing enrollment in the supplemental nutrition assistance program among older adults, kinship families, and adults with disabilities. (e) Grants (1) Maximum amount A grant awarded under the pilot program to an eligible entity for a fiscal year shall be not less than $50,000, but not more than $250,000. (2) Duration An eligible entity may be awarded a grant under the pilot program for not more than 5 years. (f) Evaluation Not later than 2 years after the date of establishment of the pilot program, the Secretary shall conduct an evaluation of the pilot program. (g) Funding (1) In general In addition to amounts otherwise available, there is appropriated, out of any funds in the Treasury not otherwise appropriated, $12,250,000, to remain available until expended, to carry out the pilot program, of which not more than $250,000 shall be used to carry out the evaluation under subsection (f). (2) Administrative costs Of the amounts made available under paragraph (1) (excluding the amount made available to carry out subsection (f)), not more than 3 percent may be used by the Secretary for administrative costs. .\n#### 5. Food delivery under supplemental nutrition assistance program\nThe Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) (as amended by section 4) is amended by adding at the end the following:\n34. Food delivery (a) Definitions In this section: (1) Covered retail food store The term covered retail food store means a retail food store, a public or private nonprofit meal delivery service, or a public or nonprofit meal delivery provider participating in the supplemental nutrition assistance program that is unable to cover the cost of food delivery for participants of that program. (2) Employee The term employee has the meaning given the term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ). (b) Program modifications (1) In general In carrying out the supplemental nutrition assistance program, the Secretary shall\u2014 (A) notify retail food stores participating in the supplemental nutrition assistance program of existing opportunities through which the retail food stores can deliver food to program participants, including by\u2014 (i) allowing an EBT card to be swiped on delivery of food to the home (with a mobile device); and (ii) preparing food for pick-up; (B) authorize public-private partnerships between the Department of Agriculture, retail food stores participating in the supplemental nutrition assistance program, and community-based organizations to provide free or low-cost food delivery, including through the use of private funds; (C) in the case of a covered retail food store, use funds made available under subparagraph (E) of paragraph (3) to provide, in accordance with that paragraph, free grocery delivery for program participants who are older adults or adults with disabilities (as those terms are defined in section 33(a)) who are unable to shop for food or lack safe and accessible transportation options to the covered retail food store; and (D) require each State to submit to the Secretary a State plan that describes how the State will\u2014 (i) work with retail food stores participating in the supplemental nutrition assistance program and other community-based partners to establish a process for food delivery for program participants; (ii) administer the reimbursements described in paragraph (3), including timing, eligibility, and distribution processes; and (iii) ensure that retail food stores participating in the supplemental nutrition assistance program that are reimbursed for delivery costs under paragraph (3) adhere to the requirements described in subparagraph (B) of that paragraph. (2) State plans Not later than 10 days after the date on which the Secretary receives a State plan under paragraph (1)(D), the Secretary shall\u2014 (A) approve or deny the State plan; and (B) make publicly available on the website of the Department of Agriculture\u2014 (i) the State plan; (ii) the determination made under subparagraph (A) with respect to that plan; and (iii) any guidance issued to the State with respect to that plan. (3) Reimbursement of covered retail food stores (A) In general Notwithstanding any other provision of law (including sections 274.7(f) and 278.2(b) of title 7, Code of Federal Regulations (or successor regulations), and any other regulations), subject to the availability of funds, a State agency shall reimburse a covered retail food store for the cost of food delivery to participants described in paragraph (1)(C) if\u2014 (i) the covered retail food store meets the requirements under subparagraph (B); and (ii) the majority of the number of food items delivered by the covered retail food store are eligible for redemption using benefits under the supplemental nutrition assistance program, regardless of whether the delivery includes nonfood items, subject to the condition that those nonfood items are of de minimis value. (B) Requirements A covered retail food store may receive reimbursement for the cost of food delivery to participants described in paragraph (1)(C) if the following requirements are met: (i) Food delivery is performed by employees of the covered retail food store or employees of an entity contracted by the covered retail food store to perform deliveries. (ii) Before any employee described in clause (i) begins making food deliveries, that employee receives employer-provided health and safety training that reflects the most recent guidelines of the Centers for Disease Control and Prevention. (iii) All employees described in clause (i) performing deliveries are paid at a rate that is not less than the greater of\u2014 (I) the minimum wage rate established under section 6(a)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(a)(1) ); and (II) the minimum wage rate established by the applicable State or locality in which the employee works. (iv) The covered retail food store meets the size standard determined by the Small Business Administration for a supermarket or other grocery retailer or a convenience retailer under section 121.201 of title 13, Code of Federal Regulations (or a successor regulation). (v) The covered retail food store does not\u2014 (I) charge the supplemental nutrition assistance program participant for delivery costs for which the covered retail food store will be reimbursed; (II) require minimum purchase thresholds in order to provide free delivery; (III) restrict delivery times to least-favorable windows for supplemental nutrition assistance program participants; or (IV) charge surge pricing. (C) Reimbursable costs Reimbursable costs under subparagraph (A) include costs associated with purchasing point-of-sale devices or receiving technical assistance relating to point-of-sale devices. (D) Maximum reimbursement per delivery The maximum amount of reimbursement under subparagraph (A) for a food delivery fee shall be $10 per delivery, which may be adjusted by the Secretary for inflation. (E) Authorization of appropriations There is authorized to be appropriated to the Secretary $500,000,000 for fiscal year 2027, and each fiscal year thereafter, to remain available until expended, to cover the cost of food delivery described in paragraph (1)(C), to be distributed among States to fund reimbursements by States under subparagraph (A). (4) Report Not later than April 30, 2028, and April 30 of each year thereafter, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry and the Special Committee on Aging of the Senate, and the Committee on Agriculture of the House of Representatives, a report that describes, for the period covered by the report, as applicable\u2014 (A) the number of supplemental nutrition assistance program participants using food delivery services, including the percentage of those participants that are older adults and adults with disabilities (as those terms are defined in section 33(a)); (B) the covered retail food stores that were reimbursed under paragraph (3), including the amount of each reimbursement; (C) any complications or difficulties experienced by States in administering reimbursements under paragraph (3); and (D) recommendations or best practices to assist States in implementing food delivery programs. .\n#### 6. Commodity supplemental food program\n##### (a) Funds\nSection 4 of the Agriculture and Consumer Protection Act of 1973 ( 7 U.S.C. 612c note; Public Law 93\u201386 ) is amended\u2014\n**(1)**\nin subsection (a), in the first sentence, by striking 2023 and inserting 2031 ; and\n**(2)**\nby adding at the end the following:\n(d) Funds In addition to amounts otherwise available, there is appropriated, out of any funds in the Treasury not otherwise appropriated, to carry out the program under this section $10,000,000 for each of fiscal years 2027 through 2031. .\n##### (b) Adults with disabilities\nSection 5 of the Agriculture and Consumer Protection Act of 1973 ( 7 U.S.C. 612c note; Public Law 93\u201386 ) is amended\u2014\n**(1)**\nby striking 2023 each place it appears and inserting 2031 ;\n**(2)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1), by striking to low-income persons aged 60 and older. and inserting the following:\nto\u2014 (A) low-income persons aged 60 and older; and (B) low-income adults with disabilities (as defined in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 )). ;\n**(B)**\nby redesignating paragraph (2) as paragraph (3);\n**(C)**\nby inserting after paragraph (1) the following:\n(2) Income eligibility For purposes of paragraph (1), a low-income individual described in subparagraph (A) or (B) of that paragraph shall have a gross income level that is less than 185 percent of the Federal poverty line. ; and\n**(D)**\nin subparagraph (B) of paragraph (3) (as so redesignated), in the matter preceding clause (i), by striking of\u2014 and all that follows through the period at the end of clause (ii) and inserting of 36 months. ; and\n**(3)**\nin subsection (i), in the matter preceding paragraph (1)\u2014\n**(A)**\nby inserting or low-income adults with disabilities described in subsection (g)(1)(B) after elderly persons ; and\n**(B)**\nby striking to each elderly participant in, or applicant for, the commodity supplemental food program for the elderly and inserting to each participant in, or applicant for, such a program .\n#### 7. Seniors farmers' market nutrition program\n##### (a) In general\nSection 4402 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 3007 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking Of the funds and inserting the following:\n(1) Mandatory funding Of the funds ;\n**(B)**\nin paragraph (1) (as so designated), by inserting (referred to in this section as the Secretary ) after Agriculture ; and\n**(C)**\nby adding at the end the following:\n(2) Authorization of appropriations There are authorized to be appropriated to the Secretary to carry out and expand the seniors farmers' market nutrition program\u2014 (A) not less than $60,000,000 for fiscal year 2027; (B) not less than $70,000,000 for fiscal year 2028; and (C) not less than $100,000,000 for each of fiscal years 2029 through 2031. ;\n**(2)**\nin subsection (b)(1), by inserting and adults with disabilities (as defined in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 )) before the semicolon at the end;\n**(3)**\nby redesignating subsections (c) through (f) as subsections (f) through (i), respectively; and\n**(4)**\nby inserting after subsection (b) the following:\n(c) Benefit amounts Under the seniors farmers' market nutrition program\u2014 (1) the minimum individual benefit shall be $35; and (2) the maximum individual benefit shall be $80. (d) Certification period The certification period for participants in the seniors farmers' market nutrition program shall be 36 months. (e) Modernization grants (1) In general Not later than 180 days after the date of enactment of the Senior Hunger Prevention Act of 2026 , the Secretary shall establish a grant program under which the Secretary shall award grants to State agencies, including Tribal organizations (as defined in section 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 )) and territories, that administer the senior farmers\u2019 market nutrition program to modernize program operations, including\u2014 (A) by transitioning from paper-based coupons to an electronic transaction technology, such as a web-based service or installable software; and (B) by increasing benefit use at farmers\u2019 markets. (2) Grant amount (A) In general The amount of a grant awarded under paragraph (1) shall not exceed $350,000. (B) Supplies Not more than $25,000 may be used to carry out subparagraph (F) of paragraph (3). (3) Eligible expenses An entity receiving a grant under paragraph (1) may use the grant for\u2014 (A) costs associated with the procurement of electronic transaction technology; (B) planning costs, including personnel costs, relating to electronic transaction technology procurement and implementation; (C) costs associated with evaluating the impact of transitioning from coupon-based operations to an electronic transaction technology; (D) training, outreach, and promotional material costs, including the costs associated with translating materials; (E) maintenance and operation of electronic transaction technology procured using the grant during the period of performance of the grant; (F) the purchase of supplies needed to perform electronic transactions onsite; and (G) additional costs associated with modernizing program operations, as determined appropriate by the Secretary. (4) Reports Each entity that receives a grant under paragraph (1) shall submit to the Secretary and the Administrator of the Food and Nutrition Service quarterly performance progress reports on the use of the grant. (5) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this subsection $15,000,000 for fiscal year 2027 and each fiscal year thereafter. .\n##### (b) Income guidelines\nThe Secretary of Agriculture shall revise section 249.6(a)(3) of title 7, Code of Federal Regulations (or a successor regulation), to ensure that income eligibility under that section is at or below 200 percent of the poverty income guidelines.\n#### 8. Infrastructure funding for farmers' markets; local procurement pilot program\nThe Farm Security and Rural Investment Act of 2002 is amended by inserting after section 4402 ( 7 U.S.C. 3007 ) the following:\n4403. Infrastructure funding for farmers' markets; local procurement pilot program (a) Definitions In this section: (1) Disability The term disability has the meaning given the term in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 ). (2) Financial assistance The term financial assistance means\u2014 (A) a loan; (B) a loan guarantee; and (C) a grant. (3) Older adult The term older adult has the meaning given the term older individual in section 102 of the Older Americans Act of 1965 ( 42 U.S.C. 3002 ). (4) Program The term program means the program established under subsection (b)(2). (5) Secretary The term Secretary means the Secretary of Agriculture. (b) Infrastructure funding for farmers' markets (1) Definition of eligible entity In this subsection, the term eligible entity means an entity that\u2014 (A) is\u2014 (i) an agricultural cooperative or other agricultural business entity or a producer network or association, including a community-supported agriculture network or association; (ii) a local or Tribal government; (iii) a nonprofit corporation; (iv) a public benefit corporation; (v) an economic development corporation; (vi) a regional farmers' market authority; (vii) a food council; or (viii) any other entity as determined by the Secretary; and (B) can demonstrate financial need, as determined by the Secretary. (2) Establishment Not later than 180 days after the date of enactment of the Senior Hunger Prevention Act of 2026 , the Secretary shall establish a program under which the Secretary shall provide financial assistance to eligible entities for\u2014 (A) the establishment of new farmers' markets; (B) the improvement or rehabilitation of existing farmers' markets, including by adding or improving payment technologies used in those farmers' markets; and (C) the expansion of community supported agriculture to serve older adults and adults with disabilities. (3) Requirements An eligible entity that receives financial assistance under the program shall be required\u2014 (A) to host farmers\u2019 markets or related activities at locations accessible\u2014 (i) by public transportation; (ii) by paratransit; or (iii) through transportation services provided under the Older Americans Act of 1965 ( 42 U.S.C. 3001 et seq. ); and (B) to reserve not less than 50 percent of the floor area of an applicable farmers' market for the sale of products that are produced locally, as determined by the Secretary, by\u2014 (i) farmers, ranchers, or aquaculture, mariculture, or fisheries operators; or (ii) associations of farmers, ranchers, or aquaculture, mariculture, or fisheries operators. (4) Cost sharing The non-Federal share of a grant provided under the program shall be 20 percent of the amount of the grant, which may comprise transportation costs, volunteer contributions, and in-kind staffing. (5) Funding Of the funds of the Commodity Credit Corporation, the Secretary shall use to carry out the program $50,000,000 for each of fiscal years 2027 through 2031. (c) Local procurement pilot program (1) Definitions In this subsection: (A) Agricultural producer The term agricultural producer includes\u2014 (i) an agricultural cooperative; (ii) a person engaged in farming, ranching, or aquaculture; (iii) a person engaged in the packing of a food product; and (iv) a person engaged in the minimal processing of a food product, as determined by the Secretary. (B) Eligible entity The term eligible entity means an entity that\u2014 (i) (I) coordinates enrollment in, and distribution of, benefits under the seniors farmers\u2019 market nutrition program; or (II) demonstrates an ability to partner with an entity that coordinates enrollment in and distribution of benefits under the seniors farmers\u2019 market nutrition program; and (ii) is\u2014 (I) a public or nonprofit provider of nutrition services or support to older adults or adults with disabilities, including\u2014 (aa) an Aging and Disability Resource Center (as defined in section 102 of the Older Americans Act of 1965 ( 42 U.S.C. 3002 )); (bb) an area agency on aging (as defined in that section); (cc) a State health insurance program; (dd) a State unit on aging; (ee) a center for independent living; (ff) a community health center; (gg) a multipurpose senior center; and (hh) federally subsidized housing, including federally subsidized housing units for older adults and adults with disabilities; or (II) a local, State, or national parks and recreation department. (2) Establishment Not later than 180 days after the date of enactment of the Senior Hunger Prevention Act of 2026 , the Secretary shall establish a pilot program under which the Secretary shall award grants to eligible entities to contract with agricultural producers that will grow produce to support the local procurement and contracting of produce for eligible entities. (3) Priority In awarding grants under paragraph (2), the Secretary shall give priority to an eligible entity that will use the grant funds to benefit underserved communities, including communities that are located in areas of concentrated poverty with limited access to fresh locally or regionally grown food. (4) Methods Under a contract described in paragraph (2), an agricultural producer may grow produce through traditional or controlled environmental agriculture farming. (5) Evaluation Not later than 2 years after the date of establishment of the pilot program under paragraph (2), the Secretary shall conduct an evaluation of the pilot program. (6) Funding (A) In general Of the funds of the Commodity Credit Corporation, the Secretary shall use to carry out this subsection $350,000 for each of fiscal years 2027 through 2031. (B) Administrative costs Of the amounts made available under subparagraph (A) for a fiscal year, not more than 5 percent may be used for administrative costs. (C) Evaluation In addition to amounts made available under subparagraph (A), there is appropriated to the Secretary, out of any funds in the Treasury not otherwise appropriated, $25,000 to carry out paragraph (5). .",
      "versionDate": "2026-04-14",
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
        "actionDate": "2026-04-14",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "4286",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Senior Hunger Prevention Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-21T02:37:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-14",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr8256",
          "measure-number": "8256",
          "measure-type": "hr",
          "orig-publish-date": "2026-04-14",
          "originChamber": "HOUSE",
          "update-date": "2026-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr8256v00",
            "update-date": "2026-04-29"
          },
          "action-date": "2026-04-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Senior Hunger Prevention Act of 2026</strong></p><p>This bill expands and modifies nutrition programs for older adults and adults with disabilities, including the Supplemental Nutrition Assistance Program (SNAP) and the Commodity Supplemental Food Program (CSFP).</p><p>Under the bill, a household's eligibility for SNAP benefits may be certified for 36 months\u00a0if all adult household members are elderly or disabled, an increase from 24 months. The bill also expands the SNAP medical expense deduction and increases the minimum allotment for households with one and two persons.</p><p>The Department of Agriculture (USDA) must establish an elderly simplified application program that\u00a0allows a state to implement a streamlined SNAP application and certification process for households where all adult household members are elderly or disabled and have no earned income.</p><p>The bill also directs USDA to authorize public-private partnerships between USDA, retail food stores participating in SNAP, and community-based organizations to provide free or low-cost food delivery under SNAP, including through the use of private funds.</p><p>Further, the bill reauthorizes CSFP, provides additional funding for the program, and expands eligibility to include low-income adults with disabilities. CSFP benefits may also be certified for 36 months. Currently, benefits may be certified for not less than one year, but not more than three years.</p><p>The bill also expands eligibility for the Seniors Farmers Market Nutrition Program to include adults with disabilities, provide a 36-month certification period, and include minimum and maximum benefit amounts.</p><p>Under the bill, USDA must also establish various related grant programs.</p>"
        },
        "title": "Senior Hunger Prevention Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr8256.xml",
    "summary": {
      "actionDate": "2026-04-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Senior Hunger Prevention Act of 2026</strong></p><p>This bill expands and modifies nutrition programs for older adults and adults with disabilities, including the Supplemental Nutrition Assistance Program (SNAP) and the Commodity Supplemental Food Program (CSFP).</p><p>Under the bill, a household's eligibility for SNAP benefits may be certified for 36 months\u00a0if all adult household members are elderly or disabled, an increase from 24 months. The bill also expands the SNAP medical expense deduction and increases the minimum allotment for households with one and two persons.</p><p>The Department of Agriculture (USDA) must establish an elderly simplified application program that\u00a0allows a state to implement a streamlined SNAP application and certification process for households where all adult household members are elderly or disabled and have no earned income.</p><p>The bill also directs USDA to authorize public-private partnerships between USDA, retail food stores participating in SNAP, and community-based organizations to provide free or low-cost food delivery under SNAP, including through the use of private funds.</p><p>Further, the bill reauthorizes CSFP, provides additional funding for the program, and expands eligibility to include low-income adults with disabilities. CSFP benefits may also be certified for 36 months. Currently, benefits may be certified for not less than one year, but not more than three years.</p><p>The bill also expands eligibility for the Seniors Farmers Market Nutrition Program to include adults with disabilities, provide a 36-month certification period, and include minimum and maximum benefit amounts.</p><p>Under the bill, USDA must also establish various related grant programs.</p>",
      "updateDate": "2026-04-29",
      "versionCode": "id119hr8256"
    },
    "title": "Senior Hunger Prevention Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-04-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Senior Hunger Prevention Act of 2026</strong></p><p>This bill expands and modifies nutrition programs for older adults and adults with disabilities, including the Supplemental Nutrition Assistance Program (SNAP) and the Commodity Supplemental Food Program (CSFP).</p><p>Under the bill, a household's eligibility for SNAP benefits may be certified for 36 months\u00a0if all adult household members are elderly or disabled, an increase from 24 months. The bill also expands the SNAP medical expense deduction and increases the minimum allotment for households with one and two persons.</p><p>The Department of Agriculture (USDA) must establish an elderly simplified application program that\u00a0allows a state to implement a streamlined SNAP application and certification process for households where all adult household members are elderly or disabled and have no earned income.</p><p>The bill also directs USDA to authorize public-private partnerships between USDA, retail food stores participating in SNAP, and community-based organizations to provide free or low-cost food delivery under SNAP, including through the use of private funds.</p><p>Further, the bill reauthorizes CSFP, provides additional funding for the program, and expands eligibility to include low-income adults with disabilities. CSFP benefits may also be certified for 36 months. Currently, benefits may be certified for not less than one year, but not more than three years.</p><p>The bill also expands eligibility for the Seniors Farmers Market Nutrition Program to include adults with disabilities, provide a 36-month certification period, and include minimum and maximum benefit amounts.</p><p>Under the bill, USDA must also establish various related grant programs.</p>",
      "updateDate": "2026-04-29",
      "versionCode": "id119hr8256"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8256ih.xml"
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
      "title": "Senior Hunger Prevention Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-18T09:53:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Senior Hunger Prevention Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-18T09:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to streamline nutrition access for older adults and adults with disabilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-18T09:48:25Z"
    }
  ]
}
```
