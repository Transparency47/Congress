# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4540?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4540
- Title: Reproductive Health Care Accessibility Act
- Congress: 119
- Bill type: S
- Bill number: 4540
- Origin chamber: Senate
- Introduced date: 2026-05-14
- Update date: 2026-05-27T05:08:26Z
- Update date including text: 2026-05-27T05:08:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-14: Introduced in Senate
- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-05-14: Introduced in Senate

## Actions

- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4540",
    "number": "4540",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001111",
        "district": "",
        "firstName": "Patty",
        "fullName": "Sen. Murray, Patty [D-WA]",
        "lastName": "Murray",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Reproductive Health Care Accessibility Act",
    "type": "S",
    "updateDate": "2026-05-27T05:08:26Z",
    "updateDateIncludingText": "2026-05-27T05:08:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
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
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T17:33:01Z",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IL"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MD"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NJ"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NH"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "HI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "OR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-05-14",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "OR"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4540is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4540\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2026 Mrs. Murray (for herself, Ms. Duckworth , Ms. Alsobrooks , Mr. Blumenthal , Mr. Booker , Mr. Fetterman , Mrs. Gillibrand , Ms. Hassan , Ms. Hirono , Mr. Markey , Mr. Merkley , Mr. Padilla , Mr. Sanders , Mr. Schiff , Ms. Smith , Ms. Warren , Mr. Welch , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to improve reproductive health care of individuals with disabilities.\n#### 1. Short title\nThis Act may be cited as the Reproductive Health Care Accessibility Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn the United States, approximately 1 in 4 adults have some type of disability, more than 1 in 10 individuals with disabilities can become pregnant, and over 4,100,000 individuals are parents with disabilities.\n**(2)**\nAll people, including individuals with disabilities, have the right to decide if, when, and how to start and raise a family, as well as to have healthy pregnancies and postpartum periods.\n**(3)**\nTitles II and III of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12131 et seq. and 12181 et seq.), section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ), and section 1557 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18116 ) provide individuals with disabilities with the right to equitably access and receive health care.\n**(4)**\nDisabled individuals face unique barriers when accessing reproductive health care, including accessibility issues at health care facilities, lack of accessible medical diagnostic equipment, barriers to accessible travel, delay in receiving preventative services, and lack of health care providers with training and knowledge on the needs of individuals with disabilities receiving reproductive health care.\n**(5)**\nReproductive health care is critical to an individual's long-term health. Disabled individuals have higher mortality rates from reproductive related cancers often due to lack of access to reproductive health care, higher rates of maternal mortality and morbidity, and often experience earlier onset menopause.\n**(6)**\nThe United States Access Board has established standards for accessible medical diagnostic equipment that were adopted by the Department of Health and Human Services and the Department of Justice in 2024. Awareness about the standards remains low among providers. Greater provider education, implementation, and enforcement of the standards is necessary to ensure equally effective reproductive and sexual health care for individuals with disabilities.\n**(7)**\nDisabled individuals have an equal right to reproductive autonomy, but harmful stereotypes about individuals with disabilities create barriers to getting care that respects that autonomy.\n**(8)**\nLaws that restrict access to reproductive health care, including abortion care, disproportionally harm individuals who already face barriers to reproductive health care, which includes disabled individuals.\n**(9)**\nIndividuals with and without disabilities want children at the same frequency, but individuals with disabilities are less likely to receive contraception counseling and timely prenatal care, experience a higher rate of sterilization, and are at a greater risk for adverse pregnancy outcomes.\n**(10)**\nDiversity and inclusion in the health care workforce is a critical factor in the delivery of high-quality, culturally competent health care and improves patient outcomes. However, the rate of students and trainees with disabilities in medical and allied health education remains low compared to those without disabilities.\n#### 3. Program for training the workforce\nPart D of title VII of the Public Health Service Act ( 42 U.S.C. 294 et seq. ) is amended by adding at the end the following:\n760A. Program for training the workforce concerning reproductive health care for individuals with disabilities (a) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration and in consultation with the Administrator of the Administration for Community Living, shall award grants, contracts, or cooperative agreements to eligible entities to carry out training programs for health care professionals and trainees on providing equitable sexual and reproductive health care for individuals with disabilities. (b) Eligibility (1) In general To be eligible to receive an award under this section, an entity shall be a public or private nonprofit entity with demonstrated expertise in serving individuals with disabilities, which may include\u2014 (A) a multidisciplinary health care provider who provides sexual and reproductive health care, such as federally qualified health centers and Title X clinics; (B) institutions of higher education, as defined in section 101 of the Higher Education Act of 1965, with expertise in sexual and reproductive health care; (C) an entity primarily led by individuals with disabilities; (D) an entity with expertise in reproductive rights and justice; (E) an Indian Tribe, Tribal organization, or urban Indian organization; or (F) a consortium of entities described in any of subparagraphs (A) through (E). (2) Application To be eligible to receive an award under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, that includes\u2014 (A) a description of the eligible entity\u2019s or consortium of entities\u2019 expertise in providing technical assistance and training, including evidence such as\u2014 (i) knowledge of the rights afforded to individuals with a disability under relevant Federal and State law; (ii) knowledge of accessibility standards established by the United States Access Board; (iii) expertise in evidence-based or evidence-informed practices in providing trauma-informed sexual and reproductive health care, including preventive health care services and perinatal care, to individuals with disabilities and those facing compounded barriers to accessing care; (iv) experience working with health care providers, public or private nonprofit entities, or Federal, State, or local agencies focusing on sexual and reproductive health care services for individuals with disabilities; (v) experience working with individuals with disabilities and their families; (vi) expertise in providing, collecting, compiling, communicating, and disseminating sexual and reproductive health care information in culturally and linguistically appropriate manner especially in easily accessible formats; and (vii) experience improving coordination of services, such as mental health, substance use disorder prevention, treatment, and recovery support services, social services, other health care services, and transportation services for individuals with disabilities; (B) a description of the activities to be funded under the award and the goals of such activities, including a description of\u2014 (i) the training or education program to be implemented that meets the requirements of subsection (c); (ii) the process to be used to identify health care providers that will participate in the training program, including the process to increase diversity in the pool of participating providers; (iii) the process to be used to engage stakeholders in such training, including individuals with disabilities; and (iv) the eligible entity\u2019s evaluation plan to determine the scope and impact of the training program; (C) an assurance that the recipients of the training will receive ongoing and comprehensive training or professional development on the sexual and reproductive health care needs of individuals with disabilities; and (D) any other assurances that the Secretary may require. (3) Subawards An eligible entity or eligible consortium receiving an award under this section may, for contracting purposes, make subawards to individuals or entities with expertise in sexual and reproductive health care and serving individuals with disabilities. (c) Use of funds An entity or entities shall use amounts received under this section to carry out a training program for health care professionals providing sexual and reproductive health care that provides training concerning\u2014 (1) comprehensive disability clinical care curricula to inform health care professionals providing sexual and reproductive health care on how to provide effective, interprofessional team-based health care; (2) comprehensive clinical care curricula on how disability-based and intersectional discrimination shapes sexual and reproductive health care access and quality for disabled individuals, including historical and ongoing practices; (3) culturally and linguistically competent care for individuals with disabilities; (4) delivering sexual and reproductive health care for individuals with disabilities in a manner that emphasizes the independence, self-determination, and choices of individuals with disabilities with respect to their sexual and reproductive health through comprehensive disability clinical care curricula; (5) the rights afforded to individuals with disabilities under relevant Federal and State law; and (6) methods and evidence-based or evidence-informed practices for providing sexual and reproductive health care, including preventive health care services, to individuals with disabilities. (d) Evaluation and report (1) In general An entity or entities that receives an award under this section shall, at the end of the award period, carry out an evaluation of outcomes achieved through the program in training health care professionals providing sexual and reproductive health care, consistent with the purposes of this section. (2) Report Not later than 180 days after the end of the award period, an entity that receives an award under this section shall submit to the Secretary a report on the results of the evaluation conducted under paragraph (1). (3) Secretary The Secretary shall annually compile the reports submitted under paragraph (2) and submit such compilation to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives. Such compilations shall be posted on the internet website of the Department of Health and Human Services in an accessible format. (e) Definitions In this section: (1) Disability The terms disability and disabilities have the meaning given such terms for purposes of the Americans with Disabilities Act of 1990. (2) Indian Tribe; Tribal organization The terms Indian Tribe and Tribal organization have the meaning given such terms in section 4 of the Indian Self-Determination and Education Assistance Act. (3) Urban Indian organization The term Urban Indian organization has the meaning given such term in section 4 of the Indian Health Care Improvement Act. (f) Authorization of appropriations There is authorized to be appropriated to carry out this section, $10,000,000 for each of fiscal years 2027 through 2031. Funds provided to carry out this section shall supplement not supplant funds otherwise made available to carry out this title. .\n#### 4. Program for expanding the reproductive health care provider workforce\nPart B of title VII of the Public Health Service Act ( 42 U.S.C. 293 et seq. ) is amended by adding at the end the following:\n742. Program for expanding the reproductive health care provider workforce (a) Purpose It is the purpose of this section\u2014 (1) to establish and sustain a competitive health professions applicant pool of individuals with disabilities by increasing the total number of individuals with disabilities who pursue a career in sexual and reproductive health care, including abortion care and maternal health care; and (2) to develop a culturally and linguistically competent health care workforce providing sexual and reproductive health care that will serve unserved and underserved populations, including individuals with disabilities. (b) Awards To assist individuals with disabilities in undertaking education to enter into the sexual and reproductive health care workforce, the Secretary may award grants, contracts, or cooperative agreements to public or private nonprofit health or educational entities, including schools of medicine, schools of osteopathic medicine, schools of nursing, and other institutions of higher education, that offer programs, including graduate programs, in obstetrics and gynecology, comprehensive sexual and reproductive health care, or programs for the training of health care providers to enable such entities to carry out the activities described in subsection (d). (c) Application To be eligible to receive an award under subsection (b), an entity described in such subsection shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (d) Use of funds An entity shall use amounts received under an award under subsection (b) to\u2014 (1) conduct or support activities to develop a competitive applicant pool, through partnership with public or private nonprofit institutions of higher education, local educational agencies, health care providers, such as sexual and reproductive health care providers and primary care providers, or other community-based entities, and establish an education pipeline for individuals with disabilities entering the sexual and reproductive health care workforce; (2) establish, strengthen, or expand programs to support the academic performance of individuals with disabilities participating in activities funded under this section, including mentorship programs; (3) identify, recruit, enroll, and retain individuals with disabilities in education and training related to sexual and reproductive health care; (4) improve the capacity of the entity involved to train, recruit, and retain faculty with disabilities including the payment of such stipends and fellowships as the Secretary may determine appropriate; (5) carry out activities to improve the information resources, clinical education, curricula, and competencies of the graduates of the entity involved, as it relates to individuals with disabilities; (6) facilitate faculty and student research on health issues affecting individuals with disabilities, including research on issues relating to the delivery of sexual and reproductive health care to individuals with disabilities; (7) carry out programs, or offer experiences, to train students in providing sexual and reproductive health services to individuals with disabilities at community-based health facilities that provide sexual and reproductive health services; (8) provide stipends to individuals with disabilities participating in activities funded under this section as the Secretary determines appropriate, in amounts as the Secretary determines appropriate, with an assurance that such stipends shall not result in loss of an individual\u2019s Federal or State benefits; or (9) carry out any other activities that the Secretary may require. (e) Preference In awarding grants, contracts, or cooperative agreements under this section, the Secretary shall give preference to applications that have been approved for programs that involve a comprehensive approach through multiple entities described in subsection (b) to establish, enhance, and expand educational programs that will result in the development of a competitive applicant pool of individuals with disabilities who desire to pursue careers in sexual and reproductive health care services. (f) Consideration for awards In awarding grants, contracts, or cooperative agreements under this section, the Secretary shall\u2014 (1) consider current enrollment trends and the needs of certain populations, including individuals with disabilities; and (2) align and coordinate with other training programs administered by the Health Resources and Services Administration. (g) Effect on other programs Assistance or stipends provided to an individual under this section shall not be considered when applying asset or resource limitation provisions related to the eligibility of such individual for any benefit, assistance, or service provided under any Federal or State program. (h) Report Not later than 180 days after the end of the award period, the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives, a report concerning the activities carried out under this section to increase the representation of individuals with disabilities in the sexual and reproductive health profession and related training programs. (i) Authorization of appropriations There is authorized to be appropriated to carry out this section, $15,000,000 for each of fiscal years 2027 through 2031. Funds provided to carry out this section shall supplement not supplant funds otherwise made available to carry out this title. .\n#### 5. Expanding the reproductive health care nursing workforce\nSection 821 of the Public Health Service Act ( 42 U.S.C. 296m ) is amended by adding at the end the following:\n(d) Expanding the reproductive health care nursing workforce (1) Awards To assist individuals with disabilities in undertaking education to enter into the reproductive nursing workforce, the Secretary may award grants, contracts, or cooperative agreements under subsection (a)(1) to eligible entities to enable such entities to carry out the activities described in paragraph (3). (2) Application To be eligible to receive an award under paragraph (1), an entity described in such paragraph shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (3) Use of funds An entity shall use amounts received under an award under paragraph (1) to\u2014 (A) conduct activities to develop a competitive applicant pool, through partnership with public or private nonprofit institutions of higher education, local educational agencies, nurse-managed health clinics, health care providers, such as sexual and reproductive health care providers and nurses, or other community-based entities, and establish an education pipeline for individuals with disabilities entering the sexual and reproductive health care nursing workforce; (B) establish, strengthen, or expand programs to support the academic performance of individuals with disabilities participating in activities funded under this subsection, including mentorship programs; (C) identify, recruit, enroll, and retain individuals with disabilities in education and training related to sexual and reproductive health care; (D) improve the capacity of the entity involved to train, recruit, and retain faculty with disabilities, including the payment of such stipends and fellowships as the Secretary may determine appropriate; (E) carry out activities to improve the information resources, clinical education, curricula, and competencies of the graduates of the entity involved, as it relates to individuals with disabilities; (F) facilitate faculty and student research to include evidence-based practice and quality improvement projects focused on health issues affecting individuals with disabilities, including research on issues relating to the delivery of sexual and reproductive health care to individuals with disabilities; (G) carry out programs, or offer experiences, to train students in providing sexual and reproductive health services to individuals with disabilities at community-based health care facilities that provide sexual and reproductive health services; (H) provide stipends to individuals with disabilities participating in activities funded under this subsection as the Secretary determines appropriate, in amounts as the Secretary determines appropriate, with an assurance that such stipends shall not result in the loss of an individual\u2019s Federal or State benefits; or (I) carry out any other activities that the Secretary may require. (4) Preference In awarding grants, contracts, or cooperative agreements under this subsection, the Secretary shall give preference to applications that have been approved for programs that involve a comprehensive approach through multiple entities described in paragraph (1) to establish, enhance, and expand educational programs that will result in the development of a competitive applicant pool of individuals with disabilities who desire to pursue careers in sexual and reproductive health care services. (5) Consideration for awards In awarding grants, contracts, or cooperative agreements under this subsection, the Secretary shall\u2014 (A) consider current enrollment trends and the needs of certain populations, including individuals with disabilities; and (B) align and coordinate with other training programs administered by the Health Resources and Services Administration. (6) Effect on other programs Assistance or stipends provided to an individual under this subsection shall not be considered when applying asset or resource limitation provisions related to the eligibility of such individual for any benefit, assistance, or service provided under any Federal or State program. (7) Report Not later than 180 days after the end of the award period, the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives, a report concerning the activities carried out under this subsection to increase the representation of individuals with disabilities in the sexual and reproductive health profession and related training programs. (8) Authorization of appropriations There is authorized to be appropriated to carry out this subsection, $15,000,000 for each of fiscal years 2027 through 2031. Funds provided to carry out this subsection shall supplement not supplant funds otherwise made available to carry out this title. .\n#### 6. Program for reproductive health education\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ), acting through the Administrator of the Health Resources and Services Administration and in consultation with the Administrator of the Administration for Community Living, shall award grants, contracts, or cooperative agreements to eligible entities to provide funding for education programs focused on sexual and reproductive health needs for individuals with disabilities.\n##### (b) Eligibility\n**(1) In general**\nTo be eligible to receive an award under this section an entity shall be a public or private nonprofit entity with a demonstrated expertise in serving individuals with disabilities, which may include\u2014\n**(A)**\na multidisciplinary health care provider who provides sexual and reproductive health care services, such as a federally qualified health center or a Title X clinic;\n**(B)**\ninstitutions of higher education, as defined in section 101 of the Higher Education Act of 1965, with expertise in sexual and reproductive health care;\n**(C)**\nan entity primarily led by individuals with disabilities;\n**(D)**\nan entity with expertise in reproductive rights and justice;\n**(E)**\nan Indian Tribe, Tribal organization, or Urban Indian organization; and\n**(F)**\na consortium of entities described in any of subparagraphs (A) through (E).\n**(2) Application**\nTo be eligible to receive a grant, contract, or cooperative agreement under this section, an eligible entity or consortium of entities shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, that includes a description of the eligible entity\u2019s or entities\u2019 expertise in providing education programs including evidence that such entity has\u2014\n**(A)**\nknowledge of best practices in providing sexual and reproductive health care, including preventive health care services, to individuals with disabilities;\n**(B)**\nexperience working with individuals with disabilities and their families; and\n**(C)**\ndemonstrated expertise of developing materials in culturally and linguistically accessible formats including plain language.\n**(3) Subawards**\nAn eligible entity or eligible consortium receiving an award under this section may, for contracting purposes, make subawards to individuals or entities with expertise in sexual and reproductive health care and serving individuals with disabilities.\n##### (c) Use of funds\nAn entity shall use amounts received under subsection (a) to\u2014\n**(1)**\ncarry out evidence-based or evidence-informed sexual and reproductive health education programs for individuals with disabilities, including youth, in culturally and linguistically accessible formats;\n**(2)**\ndevelop sexual and reproductive health education programs in culturally and linguistically accessible formats to be used in carrying out paragraph (1);\n**(3)**\nprovide education to individuals with disabilities, including youth, concerning abortion care options and their sexual, reproductive, and perinatal health care needs;\n**(4)**\nprovide education to individuals with disabilities, including youth, concerning their rights under relevant Federal and State law;\n**(5)**\nprovide access to disability affirmative and supportive clinical resources that are accessible to individuals with disabilities;\n**(6)**\nbuild the entity\u2019s capacity and enhance their leadership of the entity within the community to promote community engagement in, and advancement of, evidence-based or evidence-informed sexual and reproductive health care education in easily accessible formats; and\n**(7)**\nsupport dissemination of newly developed sexual and reproductive health care education programs as described in paragraph (2) throughout the State, territorial, and Tribal communities.\n##### (d) Evaluation and report\n**(1) In general**\nAn entity that receives an award under this section shall, at the end of the award period, carry out an evaluation of success of the entity in achieving the goals of the program for which the award was made.\n**(2) Report**\nNot later than 180 days after the end of the award period, an entity that receives an award under this section shall submit to the Secretary a report on the results of the evaluation conducted under paragraph (1).\n**(3) Secretary**\nThe Secretary shall annually compile the reports submitted under paragraph (2) and submit such compilation to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives. Such compilations shall be posted on the website of the Department of Health and Human Services in an accessible format.\n##### (e) Definitions\nIn this section:\n**(1) Disability**\nThe terms disability and disabilities have the meaning given such terms for purposes of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ).\n**(2) Indian Tribe; Tribal organization**\nThe terms Indian Tribe and Tribal organization have the meaning given such terms in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(3) Urban indian organization**\nThe term Urban Indian organization has the meaning given such term in section 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 ).\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section, $10,000,000 for each of fiscal years 2027 through 2031.\n#### 7. National Technical Assistance Center\n##### (a) Establishment\nThe Secretary of Health and Human Services, acting through the Administration for Community Living, shall directly, or through a grant, contract, or cooperative agreement, establish a National Technical Assistance Center to\u2014\n**(1)**\nprovide recommendations and best practices to States, territories, Indian Tribes, Tribal organizations, and Urban Indian organizations concerning improving coordination of services including mental health and substance use disorder services, social services, health care, and transportation to increase access to quality, integrated systems of accessible, comprehensive disability clinical care, and services for individuals with disabilities;\n**(2)**\nprovide technical assistance to health care providers on culturally and linguistically accessible and appropriate sexual and reproductive health care, including before, during, and after pregnancy and perinatal care and family planning services;\n**(3)**\ndevelop resources and provide technical assistance to assist covered entities in complying with applicable Federal laws and regulations; and\n**(4)**\ndevelop resources for individuals with disabilities facing barriers to accessible care, including related to accessible medical diagnostic equipment and the Barrier-Free Health Care Initiative.\n##### (b) Definitions\nIn this section:\n**(1) Disability**\nThe terms disability and disabilities have the meaning given such terms for purposes of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ).\n**(2) Indian Tribe; Tribal organization**\nThe terms Indian Tribe and Tribal organization have the meaning given such terms in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(3) Urban indian organization**\nThe term Urban Indian organization has the meaning given such term in section 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 ).\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section, $10,000,000 for each of fiscal years 2027 through 2031.\n#### 8. Research study\n##### (a) In general\nThe Secretary of Health and Human Services, in consultation with the Administrator of the Administration for Community Living, shall carry out a study to\u2014\n**(1)**\nidentify the types of programs and services that have demonstrated effectiveness in providing sexual and reproductive health care services for individuals with disabilities;\n**(2)**\nanalyze the effectiveness of Federal, State, Tribal, and local partnerships to coordinate efforts to ensure an integrated system of accessible, comprehensive sexual and reproductive health care for individuals with disabilities; and\n**(3)**\nidentify necessary memoranda of understanding or interagency agreements that are needed to foster data and public health research focusing on sexual and reproductive health care barriers for individuals with disabilities.\n##### (b) Report\nNot later than 3 years after the date of enactment of this Act, the Secretary of Health and Human Services shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce and the Committee on Education and Workforce of the House of Representatives, a report on the results of the study conducted under subsection (a).\n##### (c) Definition\nIn this section the terms disability and disabilities have the meanings given such terms for purposes of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ).\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section, $15,000,000 for fiscal year 2027.",
      "versionDate": "2026-05-14",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4540is.xml"
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
      "title": "Reproductive Health Care Accessibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T05:08:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reproductive Health Care Accessibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-27T05:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to improve reproductive health care of individuals with disabilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T05:03:28Z"
    }
  ]
}
```
