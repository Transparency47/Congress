# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3461?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3461
- Title: RISE from Trauma Act
- Congress: 119
- Bill type: S
- Bill number: 3461
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-01-07T18:59:35Z
- Update date including text: 2026-01-07T18:59:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8672-8674)
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8672-8674)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3461",
    "number": "3461",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "RISE from Trauma Act",
    "type": "S",
    "updateDate": "2026-01-07T18:59:35Z",
    "updateDateIncludingText": "2026-01-07T18:59:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8672-8674)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T20:10:05Z",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "WV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3461is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3461\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Durbin (for himself and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo improve the identification and support of children and families who experience trauma.\n#### 1. Short title\nThis Act may be cited as the Resilience Investment, Support, and Expansion from Trauma Act or the RISE from Trauma Act .\nI\nCommunity programming\n#### 101. Trauma and resilience-related coordinating bodies\nTitle V of the Public Health Service Act is amended by inserting after section 520C ( 42 U.S.C. 290bb\u201334 ) the following:\n520D. Local coordinating bodies to address community trauma, prevention, and resilience (a) Grants (1) In general The Secretary, in coordination with the Director of the Centers for Disease Control and Prevention and the Assistant Secretary, shall award grants to State, county, local, or Indian tribe or tribal organizations (as such terms are defined in section 4 of the Indian Self-Determination Act and Education Assistance Act) or nonprofit private entities for demonstration projects to enable such entities to act as coordinating bodies to prevent or mitigate the impact of trauma and toxic stress in a community, or promote resilience by fostering protective factors. (2) Amount The Secretary shall award such grants in amounts of not more than $6,000,000. (3) Duration The Secretary shall award such grants for periods of 4 years. (b) Eligible entities (1) In general To be eligible to receive a grant under this section, an entity shall include 1 or more representatives from at least 5 of the categories described in paragraph (2). (2) Composition The categories referred to in paragraph (1) are\u2014 (A) governmental agencies, such as public health, mental health, human services, or child welfare agencies, that provide training related to covered services or conduct activities to screen, assess, provide services or referrals, prevent, or provide treatment to support infants, children, youth, and their families as appropriate, that have experienced or are at risk of experiencing trauma; (B) faculty or qualified staff at an institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965) or representatives of a local member of the National Child Traumatic Stress Network, in an area related to screening, assessment, service provision or referral, prevention, or treatment to support infants, children, youth, and their families, as appropriate, that have experienced or are at risk of experiencing trauma; (C) hospitals, health care clinics, or other health care institutions, such as mental health and substance use disorder treatment facilities; (D) criminal justice representatives related to adults and juveniles, which may include law enforcement or judicial or court employees; (E) local educational agencies (as defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )) or agencies responsible for early childhood education programs, which may include Head Start and Early Head Start agencies; (F) workforce development, job training, or business associations; (G) nonprofit, community-based faith, human services, civic, or social services organizations, including participants in a national or community service program (as described in section 122 of the National and Community Service Act of 1990 ( 42 U.S.C. 12572 )), providers of after-school programs, home visiting programs, family resource centers, agencies that serve victims of domestic and family violence or child abuse, or programs to prevent or address the impact of violence and addiction; and (H) the general public, including individuals who have experienced trauma who can appropriately represent populations and activities relevant to the community that will be served by the entity. (3) Qualifications In order for an entity to be eligible to receive the grant under this section, the representatives included in the entity shall, collectively, have training and expertise concerning childhood trauma, resilience, and covered services. (c) Application To be eligible to receive a grant under this section, an entity shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require. (d) Priority In awarding grants under this section, the Secretary shall give priority to entities proposing to serve communities or populations that have faced or currently face high rates of community trauma, including from intergenerational poverty, civil unrest, discrimination, or oppression, which may include an evaluation of\u2014 (1) an age-adjusted rate of drug overdose deaths that is above the national overdose mortality rate, as determined by the Director of the Centers for Disease Control and Prevention; (2) an age-adjusted rate of violence-related (or intentional) injury deaths that is above the national average, as determined by the Director of the Centers for Disease Control and Prevention; and (3) a rate of involvement in the child welfare or juvenile justice systems that is above the national average, as determined by the Secretary. (e) Use of funds An entity that receives a grant under this section to act as a coordinating body may use the grant funds to\u2014 (1) bring together stakeholders who provide or use services in, or have expertise concerning, covered settings to identify community needs and resources related to covered services, and to build on any needs assessments conducted by organizations or groups represented on the coordinating body; (2) (A) collect data, on indicators to reflect local priority issues, including across multiple covered settings and disaggregated by age, race, and any other appropriate metrics; and (B) use the data to identify unique community challenges and barriers, community strengths and assets, gaps in services, and high-need areas, related to covered services; (3) build awareness, skills, and leadership (including through trauma-informed and resilience-focused training and public outreach campaigns) on covered services in covered settings; (4) develop a strategic plan, in partnership with members of the served community or population, that identifies\u2014 (A) policy goals and coordination opportunities to address community needs and local priority issues (including coordination in applying for or utilizing existing grants, insurance coverage, or other government programs), including for communities of color and relating to delivering and implementing covered services; and (B) a comprehensive, integrated approach for the entity and its members to prevent and mitigate the impact of exposure to trauma or toxic stress in the community, and to assist the community in healing from existing and prior exposure to trauma through promotion of resilience and fostering protective factors; (5) implement such strategic plans in the local community, including through the delivery of covered services in covered settings; and (6) identify funding sources and partner with community stakeholders to sustainably continue activities after the end of the grant period. (f) Supplement not supplant Amounts made available under this section shall be used to supplement and not supplant other Federal, State, and local public funds and private funds expended to provide trauma-related coordination activities. (g) Evaluation At the end of the period for which grants are awarded under this section, the Secretary shall conduct an evaluation of the activities carried out under each grant under this section. In conducting the evaluation, the Secretary shall assess the outcomes of the grant activities carried out by each grant recipient, including outcomes related to health, education, child welfare, criminal justice involvement, or other measurable outcomes pertaining to wellbeing and societal impact. (h) Authorization of appropriations There is authorized to be appropriated to carry out this section $600,000,000 for each of fiscal years 2026 through 2033. (i) Definitions In this section: (1) Covered services The term covered services means culturally responsive services, programs, models, or interventions that are evidence-based, evidence-informed, or promising best practices to support infants, children, youth, and their families as appropriate by preventing or mitigating the impact of trauma and toxic stress or promoting resilience by fostering protective factors, which may include the best practices developed under section 7132(d) of the SUPPORT for Patients and Communities Act ( Public Law 115\u2013271 ). (2) Covered setting The term covered setting means the settings in which individuals may come into contact with infants, children, youth, and their families, as appropriate, who have experienced or are at risk of experiencing trauma, including schools, hospitals, settings where health care providers, including primary care and pediatric providers, provide services, early childhood education and care settings, home visiting settings, after-school program facilities, child welfare agency facilities, public health agency facilities, mental health treatment facilities, substance use disorder treatment facilities, faith-based institutions, domestic violence agencies, violence intervention organizations, child advocacy centers, homeless services system facilities, refugee services system facilities, juvenile justice system facilities, law enforcement agency facilities, Healthy Marriage Promotion or Responsible Fatherhood service settings, child support service settings, and service settings focused on individuals eligible for Temporary Assistance for Needy Families; and .\n#### 102. Expansion of performance partnership pilot for children who have experienced or are at risk of experiencing trauma\n##### (a) In general\nSection 526 of the Departments of Labor, Health and Human Services, and Education, and Related Agencies Appropriations Act, 2014 ( 42 U.S.C. 12301 note) is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following:\n(4) To improve outcomes for infants, children, and youth, and their families as appropriate, who have experienced or are at risk of experiencing trauma means to increase the rate at which individuals who have experienced or are at risk of experiencing trauma, including those who are low-income, homeless, involved with the child welfare system, involved in the juvenile justice system, have been victims of violence (including community, family, or sexual violence), unemployed, or not enrolled in or at risk of dropping out of an educational institution and live in a community that has faced acute or long-term exposure to substantial discrimination, historical oppression, intergenerational poverty, civil unrest, a high rate of violence or drug overdose deaths, achieve success in meeting educational, employment, health, developmental, community reentry, permanency from foster care, or other key goals. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin the subsection heading, by striking Fiscal Year 2014 and inserting Fiscal Years 2026 Through 2030 ;\n**(B)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively, and by moving such subparagraphs, as so redesignated, 2 ems to the right;\n**(C)**\nby striking Federal agencies and inserting the following:\n(1) Disconnected youth pilots Federal agencies ; and\n**(D)**\nby adding at the end the following:\n(2) Trauma-informed care pilots Federal agencies may use Federal discretionary funds that are made available in this Act or any appropriations Act, including across different or multiple years, for any of fiscal years 2026 through 2030 to carry out up to 10 Performance Partnership Pilots. Such Pilots shall\u2014 (A) be designed to improve outcomes for infants, children, and youth, and their families as appropriate, who have experienced or are at risk of experiencing trauma; and (B) involve Federal programs targeted on infants, children, and youth, and their families as appropriate, who have experienced or are at risk of experiencing trauma. ;\n**(3)**\nin subsection (c)(2)\u2014\n**(A)**\nin subparagraph (A), by striking 2018 and inserting 2029 ; and\n**(B)**\nin subparagraph (F), by inserting before the semicolon , including the age range for such population ; and\n**(4)**\nin subsection (e), by striking 2018 and inserting 2029 .\n##### (b) Requirement\nNot later than 9 months after the date of enactment of this Act, the Director of the Office of Management and Budget, working with the Attorney General and the Secretary of Labor, Secretary of Health and Human Services, Secretary of Education, and Secretary of Housing and Urban Development, and any other appropriate agency representative, shall, with respect to carrying out this section\u2014\n**(1)**\nexplore authorities to enable the issuance of appropriate start-up funding;\n**(2)**\nissue guidance documents, template waivers and performance measurements, best practices and lessons learned from prior pilot programs, recommendations for how to sustain projects after award periods, and other technical assistance documents as needed; and\n**(3)**\nalign application timing periods to provide maximum flexibility, which may include the availability of initial planning periods for awardees.\n#### 103. Hospital-based interventions to reduce readmissions\nSection 393 of the Public Health Service Act ( 42 U.S.C. 280b\u20131a ) is amended by adding at the end the following:\n(c) Hospital-Based interventions To reduce readmissions (1) Grants The Secretary shall award grants to eligible entities to deliver and evaluate hospital-based interventions to improve outcomes and reduce subsequent reinjury or readmissions of patients that present at a hospital after overdosing, attempting suicide, or suffering violent injury or abuse. (2) Eligible entities To be eligible to receive a grant under this subsection and entity shall\u2014 (A) be a hospital or health system (including health systems operated by Indian tribes or tribal organizations as such terms are defined in section 4 of the Indian Self-Determination Act and Education Assistance Act); and (B) submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, which shall include demonstrated experience furnishing successful hospital-based trauma interventions to improve outcomes and prevent reinjury or readmission for patients presenting after overdosing, attempting suicide, or suffering violent injury or abuse. (3) Use of funds An entity shall use amounts received under a grant under this subsection to deliver, test, and evaluate hospital-based trauma-informed interventions for patients who present at hospitals with drug overdoses, suicide attempts, or violent injuries (such as domestic violence or intentional penetrating wounds, including gunshots and stabbings), or other presenting symptoms associated with exposure to trauma, violence, substance misuse, or suicidal ideation, to provide comprehensive education, screening, counseling, discharge planning, skills building, and long-term case management services to such individuals, and their guardians or caregivers as appropriate, to prevent hospital readmission, injury, and improve health, wellness, and safety outcomes. Such interventions may be furnished in coordination or partnership with qualified community-based organizations and may include or incorporate the best practices developed under section 7132(d) of the SUPPORT for Patients and Communities Act ( Public Law 115\u2013271 ). (4) Quality measures An entity that receive a grant under this section shall submit to the Secretary a report on the data and outcomes developed under the grant, including any quality measures developed, evaluated, and validated to prevent hospital readmissions for the patients served under the program involved. (5) Sustainable coverage The Secretary, acting through the Administrator of the Centers for Medicare & Medicaid Services, shall evaluate existing authorities, flexibilities, and policies and disseminate appropriate and relevant information to eligible entities on the opportunities for health insurance coverage and reimbursement for the activities described in paragraph (3). .\n#### 104. Reauthorizing the national child traumatic stress network\nSection 582 of the Public Health Service Act ( 42 U.S.C. 290hh\u20131 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking and at the end;\n**(B)**\nin paragraph (2), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(3) collaboration among all NCTSI grantees for purposes of developing evidence-based resources, training, interventions, practices, and other information, as an integral part of required grant activities. ;\n**(2)**\nin subsection (d), by adding at the end the following: In carrying out this subsection, the Secretary shall permit all grantees to deliver both training and services, as appropriate. ; and\n**(3)**\nin subsection (j), to read as follows:\n(j) Authorization of appropriations There is authorized to be appropriated to carry out this section, $93,887,000 for each of fiscal years 2026 through 2030. .\n#### 105. Reauthorizing the trauma support services in schools grant program\nSection 7134(l) of the SUPPORT for Patients and Communities Act ( Public Law 115\u2013271 ) is amended by striking fiscal years 2019 through 2023 and inserting fiscal years 2026 through 2030 .\n#### 106. Reauthorizing CDC surveillance and data collection activities\nSection 7131(e) of the SUPPORT for Patients and Communities Act ( Public Law 115\u2013271 ) is amended by striking $2,000,000 for each of fiscal years 2019 through 2023 and inserting $9,000,000 for each of fiscal years 2026 through 2030 .\nII\nWorkforce development\n#### 201. Reauthorizing the interagency task force on trauma-informed care\nSection 7132(i) of the SUPPORT for Patients and Communities Act ( Public Law 115\u2013271 ) is amended by striking 2030 and inserting 2031 .\n#### 202. Training and recruitment of individuals from communities that have experienced high levels of trauma, violence, or addiction\nPart B of title VII of the Public Health Service Act ( 42 U.S.C. 293 et seq. ) is amended by adding at the end the following:\n742. Individuals from communities that have experienced high levels of trauma, violence, or addiction In carrying out activities under this part, the Secretary shall ensure that emphasis is provided on the recruitment of individuals from communities that have experienced high levels of trauma, violence, or addiction and that appropriate activities under this part are carried out in partnership with community-based organizations that have expertise in addressing such challenges to enhance service delivery. .\n#### 203. Funding for the National Health Service Corps\nSection 10503(b)(2) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 254b\u20132(b)(2) ) is amended\u2014\n**(1)**\nin subparagraph (G), by striking and at the end;\n**(2)**\nin subparagraph (H), by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(I) in addition to the amounts provided for under subparagraph (H) for fiscal year 2023, $50,000,000 for each of fiscal years 2026 through 2030, to be allocated in each such fiscal year for awards to eligible individuals whose obligated service locations are in schools or community-based settings as described in section 338N of the Public Health Service Act. .\n#### 204. Infant and early childhood clinical workforce\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g ) is amended by adding at the end the following:\n399V\u20138. Infant and early childhood clinical workforce (a) In general The Secretary, acting through the Associate Administrator of the Maternal and Child Health Bureau, shall establish an Infant and Early Childhood Mental Health Clinical Leadership Program to award grants to eligible entities to establish a national network of training institutes for infant and early childhood clinical mental health. (b) Eligible entities To be eligible to receive a grant under this section, an entity shall\u2014 (1) be\u2014 (A) an institution of higher education as defined in section 101(a) of the Higher Education Act of 1965, including historically Black colleges and universities (as defined for purposes of section 322 of the Higher Education Act of 1965 ( 20 U.S.C. 1061 )), and Tribal colleges (as defined for purposes of section 316(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059c )); or (B) be a hospital with affiliation with such an institution of higher education, or a State professional medical society or association of infant mental health demonstrating an affiliation or partnership with such an institution of higher education; and (2) submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (c) Use of grant An entity shall use amounts received under a grant under this section to establish training institutes to\u2014 (1) equip aspiring and current mental health professionals, including clinical social workers, professional counselors, marriage and family therapists, clinical psychologists, child psychiatrists, school psychologists, school counselors, school social workers, nurses, home visitors, community health workers, and developmental and behavioral pediatricians with specialization in infant and early childhood clinical mental health, and those pursuing certification or licensure in such professions; and (2) emphasize equipping trainees with culturally responsive skills in prevention, mental health consultation, screening, assessment, diagnosis, and treatment for infants and children, and their parents as appropriate, who have experienced or are at risk of experiencing trauma, including from intergenerational poverty, civil unrest, discrimination, or oppression, exposure to violence or overdose, as well as prevention of secondary trauma, through\u2014 (A) the provision of community-based training and supervision in evidence-based assessment, diagnosis, and treatment, which may be conducted through partnership with qualified community-based organizations; (B) the development of graduate education training tracks; (C) the provision of scholarships, stipends, and trainee supports, including to enhance recruitment, retention, and career placement of students from populations under-represented populations in the mental health workforce; and (D) the provision of mid-career training to develop the capacity of existing health practitioners. (d) Authorization of appropriations There is authorized to be appropriated to carry out this section, $25,000,000 for each of fiscal years 2026 through 2030. .\n#### 205. Trauma-informed teaching and school leadership\n##### (a) Partnership grants\nSection 202 of the Higher Education Act of 1965 ( 20 U.S.C. 1022a ) is amended\u2014\n**(1)**\nin subsection (b)(6)\u2014\n**(A)**\nby redesignating subparagraphs (H) through (K) as subparagraphs (I) through (L), respectively; and\n**(B)**\nby inserting after subparagraph (G) the following:\n(H) how the partnership will prepare general education and special education teachers and, as applicable, early childhood educators, to support positive learning outcomes and social and emotional development for students\u2014 (i) who have experienced trauma (including students who are involved in the foster care or juvenile justice system or runaway or homeless youth); and (ii) in alternative education settings in which high populations of youth with trauma exposure may learn (including settings for correctional education, juvenile justice, pregnant, expecting, and parenting students, or youth who have re-entered school after a period of absence due to dropping out); ;\n**(2)**\nin subsection (d)(1)(A)(i)\u2014\n**(A)**\nin subclause (II), by striking and after the semicolon;\n**(B)**\nby redesignating subclause (III) as subclause (IV); and\n**(C)**\nby inserting after subclause (II) the following:\n(III) such teachers and, as applicable, early childhood educators, to adopt evidence-based approaches for\u2014 (aa) improving behavior (such as positive behavior interventions and supports and restorative justice practices); (bb) supporting social and emotional learning; (cc) mitigating the effects of trauma; (dd) improving the learning environment in the school; (ee) preventing secondary trauma, compassion fatigue, and burnout; and (ff) alternatives to punitive discipline practices, including suspensions, expulsions, corporal punishment, referrals to law enforcement, and other actions that remove students from the learning environment; and ; and\n**(3)**\nin subsection (d), by adding at the end the following:\n(7) Trauma-informed and resilience-focused practice and work in alternative education settings Developing the teaching skills of prospective and, as applicable, new, early childhood educators and elementary school and secondary school teachers to adopt evidence-based trauma-informed and resilience-focused teaching strategies\u2014 (A) to\u2014 (i) recognize the signs of trauma and its impact on learning; (ii) maximize student engagement and promote the social and emotional development of students; (iii) implement alternative practices to suspension and expulsion that do not remove students from the learning environment; and (iv) engage with other school personnel, including administrators and nonteaching staff, to foster a shared understanding of the items described in clauses (i), (ii), and (iii); and (B) including programs training teachers and, as applicable, early childhood educators to work with students\u2014 (i) with exposure to traumatic events (including students involved in the foster care or juvenile justice system or runaway and homeless youth); and (ii) in alternative academic settings for youth unable to participate in a traditional public school program in which high populations of students with trauma exposure may learn (such as students involved in the foster care or juvenile justice system, pregnant, expecting, and parenting students, runaway and homeless students, students exposed to family violence or trafficking, and other youth who have re-entered school after a period of absence due to dropping out). .\n##### (b) Administrative provisions\nSection 203(b)(2) of the Higher Education Act of 1965 ( 20 U.S.C. 1022b(b)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking and after the semicolon;\n**(2)**\nin subparagraph (B)(ii), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(C) to eligible partnerships that have a high-quality proposal for trauma-informed and resilience-focused training programs for general education and special education teachers and, as applicable, early childhood educators. .\n##### (c) Grants for the development of leadership programs\nSection 202(f)(1)(B) of the Higher Education Act of 1965 ( 20 U.S.C. 1022a(f)(1)(B) ) is amended\u2014\n**(1)**\nin clause (v), by striking and after the semicolon;\n**(2)**\nin clause (vi), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(vii) identify students who have experienced trauma and connect those students with appropriate school-based or community-based interventions and services. .\n#### 206. Tools for front-line providers\nNot later than 18 months after the date of enactment of this Act, the Secretary of Health and Human Services, in coordination with appropriate stakeholders with subject matter expertise which may include the National Child Traumatic Stress Network or other resource centers funded by the Department of Health and Human Services, shall carry out activities to develop accessible and easily understandable toolkits for use by front-line service providers (including teachers, early childhood educators, school and out-of-school program leaders, paraeducators and school support staff, home visitors, mentors, social workers, counselors, health care providers, child welfare agency staff, individuals in juvenile justice settings, faith leaders, first responders, kinship caregivers, domestic violence agencies, child advocacy centers, homeless services personnel, and youth development and community-based organization personnel) for appropriately identifying, responding to, and supporting infants, children, and youth, and their families, as appropriate, who have experienced or are at risk of experiencing trauma or toxic stress. Such toolkits shall incorporate best practices developed under section 7132(d) of the SUPPORT for Patients and Communities Act ( Public Law 115\u2013271 ), and include actions to build a safe, stable, and nurturing environment for the infants, children, and youth served in those settings, capacity building, and strategies for addressing the impact of secondary trauma, compassion fatigue, and burnout among such front-line service providers and other caregivers.\n#### 207. Children exposed to violence initiative\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 ) is amended by adding at the end the following:\nPP Children exposed to violence and addiction initiative 3061. Grants to support children exposed to violence and substance use (a) In general The Attorney General may make grants to States, units of local government, Indian tribes and tribal organizations (as such terms are defined in section 4 of the Indian Self-Determination Act and Education Assistance Act), and nonprofit organizations to reduce violence and substance use by preventing children\u2019s trauma from exposure to violence or substance use and supporting infants, children, and youth, and their families, who have been harmed by violence, trauma, or substance use to heal. (b) Use of funds (1) In general A grant under subsection (a) may be used to implement trauma-informed policies and practices that support infants, children, youth, and their families, as appropriate, by\u2014 (A) building public awareness and education about the importance of addressing childhood trauma as a means to reduce violence and substance use and improve educational, economic, developmental, and societal outcomes for infants, children, and youth; (B) providing training, tools, and resources to develop the skills and capacity of parents (including foster parents), adult guardians, and professionals who interact directly with infants, children, and youth, in an organized or professional setting, to reduce the impact of trauma, grief, and exposure to violence on children, including through the best practices developed under section 7132(d) of the SUPPORT for Patients and Communities Act ( Public Law 115\u2013271 ); and (C) supporting community collaborations and providing technical assistance to communities, organizations, and public agencies on how they can coordinate to prevent and mitigate the impact of trauma from exposure to violence and substance use on children in their homes, schools, and communities. (2) Priority Priority in awarding grants under this section shall be given to communities that seek to address multiple types of violence and serve children who have experienced poly-victimization. (c) Authorization of appropriations There are authorized to be appropriated to carry out this section $11,000,000 for each of fiscal years 2026 through 2030. .\n#### 208. Establishment of law enforcement child and youth trauma coordinating center\n##### (a) Establishment of center\n**(1) In general**\nThe Attorney General, in coordination with the Civil Rights Division, shall establish a National Law Enforcement Child and Youth Trauma Coordinating Center (referred to in this section as the Center ) to provide assistance to adult- and juvenile-serving State, local, and tribal law enforcement agencies (including those operated by Indian tribes and tribal organizations as such terms are defined in section 4 of the Indian Self-Determination Act and Education Assistance Act) in interacting with infants, children, and youth who have been exposed to violence or other trauma, and their families as appropriate.\n**(2) Age range**\nThe Center shall determine the age range of infants, children, and youth to be covered by the activities of the Center.\n##### (b) Duties\nThe Center shall provide assistance to adult- and juvenile-serving State, local, and tribal law enforcement agencies by\u2014\n**(1)**\ndisseminating information on the best practices for law enforcement officers, which may include best practices based on evidence-based and evidence-informed models from programs of the Department of Justice and the Office of Justice Services of the Bureau of Indian Affairs or the best practices developed under section 7132(d) of the SUPPORT for Patients and Communities Act ( Public Law 115\u2013271 ), such as\u2014\n**(A)**\nmodels developed in partnership with national law enforcement organizations, Indian tribes, or clinical researchers; and\n**(B)**\nmodels that include\u2014\n**(i)**\ntrauma-informed approaches to conflict resolution, information gathering, forensic interviewing, de-escalation, and crisis intervention training;\n**(ii)**\nearly interventions that link child and youth witnesses and victims, and their families as appropriate, to age-appropriate trauma-informed services; and\n**(iii)**\npreventing and supporting officers who experience secondary trauma;\n**(2)**\nproviding professional training and technical assistance; and\n**(3)**\nawarding grants under subsection (c).\n##### (c) Grant program\n**(1) In general**\nThe Attorney General, acting through the Center, may award grants to State, local, and tribal law enforcement agencies or to multi-disciplinary consortia to\u2014\n**(A)**\nenhance the awareness of best practices for trauma-informed responses to infants, children, and youth who have been exposed to violence or other trauma, and their families as appropriate; and\n**(B)**\nprovide professional training and technical assistance in implementing the best practices described in subparagraph (A).\n**(2) Application**\nAny State, local, or tribal law enforcement agency seeking a grant under this subsection shall submit an application to the Attorney General at such time, in such manner, and containing such information as the Attorney General may require.\n**(3) Use of funds**\nA grant awarded under this subsection may be used to\u2014\n**(A)**\nprovide training to law enforcement officers on best practices, including how to identify and appropriately respond to early signs of trauma and violence exposure when interacting with infants, children, and youth, and their families, as appropriate; and\n**(B)**\nestablish, operate, and evaluate a referral and partnership program with trauma-informed clinical mental health, substance use, health care, or social service professionals in the community in which the law enforcement agency serves.\n##### (d) Authorization of appropriations\nThere are authorized to be appropriated to the Attorney General\u2014\n**(1)**\n$6,000,000 for each of fiscal years 2026 through 2030 to award grants under subsection (c); and\n**(2)**\n$2,000,000 for each of fiscal years 2026 through 2030 for other activities of the Center.",
      "versionDate": "2025-12-11",
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
        "actionDate": "2025-12-11",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on Energy and Commerce, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6625",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "RISE from Trauma Act",
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
        "name": "Health",
        "updateDate": "2026-01-07T18:59:35Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3461is.xml"
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
      "title": "RISE from Trauma Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RISE from Trauma Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Resilience Investment, Support, and Expansion from Trauma Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the identification and support of children and families who experience trauma.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:26Z"
    }
  ]
}
```
