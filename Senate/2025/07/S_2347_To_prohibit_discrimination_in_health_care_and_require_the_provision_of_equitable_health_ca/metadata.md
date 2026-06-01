# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2347?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2347
- Title: Equal Health Care for All Act
- Congress: 119
- Bill type: S
- Bill number: 2347
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2025-09-05T15:12:25Z
- Update date including text: 2025-09-05T15:12:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S4458: 3)
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S4458: 3)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2347",
    "number": "2347",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Equal Health Care for All Act",
    "type": "S",
    "updateDate": "2025-09-05T15:12:25Z",
    "updateDateIncludingText": "2025-09-05T15:12:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S4458: 3)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T20:20:05Z",
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
      "sponsorshipDate": "2025-07-17",
      "state": "NJ"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2347is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2347\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Padilla (for himself, Mr. Booker , Mr. Schiff , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit discrimination in health care and require the provision of equitable health care, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Equal Health Care for All Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 1966, Dr. Martin Luther King, Jr. said Of all the forms of inequality, injustice in health care is the most shocking and inhuman because it often results in physical death. .\n**(2)**\nInequity in health care remains a persistent and devastating reality for many communities, and, in particular, communities of color.\n**(3)**\nThe inequitable provision of health care has complex causes, many stemming from systemic inequality in access to health care, housing, nutrition, economic opportunity, education, and other factors.\n**(4)**\nHealth care outcomes for Black communities in particular lag far behind those of the population as a whole.\n**(5)**\nA contributing factor in health disparities is explicit and implicit bias in the delivery of health care, resulting in inferior care and poorer outcomes for some patients on the basis of factors that include race, national origin, sex (including sexual orientation or gender identity), disability, age, and religion.\n**(6)**\nThe National Academy of Medicine (formerly known as the Institute of Medicine ) issued a report in 2002 titled Unequal Treatment , finding that racial and ethnic minorities receive lower-quality health care than White individuals do, even when insurance status, income, age, and severity of condition is comparable.\n**(7)**\nJust as Congress has sought to eliminate bias, both explicit and implicit, in employment, housing, and other parts of our society, the elimination of bias and the legacy of structural racism in health care is of paramount importance.\n#### 3. Data collection and reporting\n##### (a) Required reporting\n**(1) In general**\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ), in consultation with the Director for Civil Rights and Health Equity, the Director of the National Institutes of Health, the Administrator of the Centers for Medicare & Medicaid Services, the Director of the Agency for Healthcare Research and Quality, the Deputy Assistant Secretary for Minority Health, and the Director of the Centers for Disease Control and Prevention, shall by regulation require all health care providers and facilities that are required under other provisions of law to report data on specific health outcomes to the Department of Health and Human Services in aggregate form, to disaggregate such data by demographic characteristics, including by race, national origin, sex (including sexual orientation and gender identity), disability, and age, as well as any other factor that the Secretary determines would be useful for determining a pattern of inequitable provision of health care.\n**(2) Proposed regulations**\nNot later than 90 days after the date of enactment of this Act, the Secretary shall issue proposed regulations to carry out paragraph (1).\n##### (b) Repository\nThe Secretary shall\u2014\n**(1)**\nnot later than 1 year after the date of enactment of this Act, establish a repository of the disaggregated data reported pursuant to subsection (a); and\n**(2)**\nensure that such repository does not contain any data that is individually identifiable.\n#### 4. Requiring equitable health care in the hospital value-based purchasing program\n##### (a) Equitable health care as value measurement\nSection 1886(b)(3)(B)(viii) of the Social Security Act ( 42 U.S.C. 1395ww(b)(3)(B)(viii) ) is amended by adding at the end the following new subclause:\n(XIII) (aa) Effective for payments beginning with fiscal year 2026, in expanding the number of measures under subclause (III), the Secretary shall adopt measures that relate to equitable health care furnished by hospitals in inpatient settings. (bb) In carrying out this subclause, the Secretary shall solicit input and recommendations from individuals and groups representing communities of color and other protected classes and ensure measures adopted pursuant to this subclause account for social determinants of health, as defined in section 7(e)(10) of the Equal Health Care for All Act , such that the social determinants of health do not adversely affect hospitals if any inequitable outcomes are not caused by that hospital\u2019s provision of care. (cc) For purposes of this subclause, the term equitable health care refers to the principle that high-quality care should be provided to all individuals and health care treatment and services should not vary on account of the real or perceived race, national origin, sex (including sexual orientation and gender identity), disability, or age of an individual, as well as any other factor that the Secretary determines would be useful for determining a pattern of inequitable provision of health care. .\n##### (b) Inclusion of equitable health care measures\nSection 1886(o)(2)(B) of the Social Security Act ( 42 U.S.C. 1395ww(o)(2)(B) ) is amended by adding at the end the following new clause:\n(iv) Inclusion of equitable health care measures Beginning in fiscal year 2026, measures selected under subparagraph (A) shall include the equitable health care measures described in subsection (b)(3)(B)(viii)(XIII). .\n#### 5. Inequitable provision of health care as a basis for permissive exclusion from Medicare and other Federal health care programs\nSection 1128(b) of the Social Security Act ( 42 U.S.C. 1320a\u20137(b) ) is amended by adding at the end the following new paragraph:\n(18) Inequitable provision of health care (A) In general Subject to subparagraph (B), any health care provider that the Secretary determines, under section 7(b)(2) of the Equal Health Care for All Act , has engaged in a pattern of inequitable provision of health care (as defined in subsection (e)(7) of such Act) on the basis of race, national origin, sex (including sexual orientation and gender identity), disability, or age of an individual. (B) Exception For purposes of carrying out subparagraph (A), the Secretary shall not exclude any health care provider from participation in the Medicare program under title XVIII or the Medicaid program under title XIX if the exclusion of such health care provider would result in increased difficulty in access to health care services for underserved or low-income communities. .\n#### 6. Office for Civil Rights and Health Equity of the Department of Health and Human Services\n##### (a) Name of office\nBeginning on the date of enactment of this Act, the Office for Civil Rights of the Department of Health and Human Services shall be known as the Office for Civil Rights and Health Equity of the Department of Health and Human Services. Any reference to the Office for Civil Rights of the Department of Health and Human Services in any law, regulation, map, document, record, or other paper of the United States shall be deemed to be a reference to the Office for Civil Rights and Health Equity.\n##### (b) Head of office\nThe head of the Office for Civil Rights and Health Equity shall be the Director for Civil Rights and Health Equity, to be appointed by the President. Any reference to the Director of the Office for Civil Rights of the Department of Health and Human Services in any law, regulation, map, document, record, or other paper of the United States shall be deemed to be a reference to the Director for Civil Rights and Health Equity.\n#### 7. Prohibiting discrimination in health care\n##### (a) Prohibiting discrimination\n**(1) In general**\nNo health care provider may, on the basis, in whole or in part, of race, sex (including sexual orientation and gender identity), disability, age, or religion, subject an individual to the inequitable provision of health care.\n**(2) Notice of patient rights**\nThe Secretary shall provide to each patient a notice of a patient\u2019s rights under this section.\n##### (b) Administrative complaint and conciliation process\n**(1) Complaints and answers**\n**(A) In general**\nAn aggrieved person may, not later than 1 year after an alleged violation of subsection (a) has occurred or concluded, file a complaint with the Director alleging inequitable provision of health care by a provider described in subsection (a).\n**(B) Complaint**\nA complaint submitted pursuant to subparagraph (A) shall be in writing and shall contain such information and be in such form as the Director requires.\n**(C) Oath or affirmation**\nThe complaint and any answer made under this subsection shall be made under oath or affirmation, and may be reasonably and fairly modified at any time.\n**(2) Response to complaints**\n**(A) In general**\nUpon the filing of a complaint under this subsection, the following procedures shall apply:\n**(i) Complainant notice**\nThe Director shall serve notice upon the complainant acknowledging receipt of such filing and advising the complainant of the time limits and procedures provided under this section.\n**(ii) Respondent notice**\nThe Director shall, not later than 30 days after receipt of such filing\u2014\n**(I)**\nserve on the respondent a notice of the complaint, together with a copy of the original complaint; and\n**(II)**\nadvise the respondent of the procedural rights and obligations of respondents under this section.\n**(iii) Answer**\nThe respondent may file, not later than 60 days after receipt of the notice from the Director, an answer to such complaint.\n**(iv) Investigative duties**\nThe Director shall\u2014\n**(I)**\nmake an investigation of the alleged inequitable provision of health care; and\n**(II)**\ncomplete such investigation within 180 days (unless it is impracticable to complete such investigation within 180 days) after the filing of the complaint.\n**(B) Investigations**\n**(i) Pattern or practice**\nIn the course of investigating the complaint, the Director may seek records of care provided to patients other than the complainant if necessary to demonstrate or disprove an allegation of inequitable provision of health care or to determine whether there is a pattern or practice of such care.\n**(ii) Accounting for social determinants of health**\nIn investigating the complaint and reaching a determination on the validity of the complaint, the Director shall account for social determinants of health and the effect of such social determinants on health care outcomes, so that the health care provider named in the complaint is not held accountable for a factor outside of the control of the provider's provision of health care.\n**(iii) Inability to complete investigation**\nIf the Director is unable to complete (or finds it is impracticable to complete) the investigation within 180 days after the filing of the complaint (or, if the Secretary takes further action under paragraph (6)(B) with respect to a complaint, within 180 days after the commencement of such further action), the Director shall notify the complainant and respondent in writing of the reasons involved.\n**(iv) Report to State licensing authorities**\nOn concluding each investigation under this subparagraph, the Director shall provide to each State licensing authority that is responsible for the licensing of the health care provider under investigation, information specifying the results of the investigation.\n**(C) Report**\n**(i) Final report**\nOn completing each investigation under this paragraph, the Director shall prepare a final investigative report.\n**(ii) Modification of report**\nA final report under this subparagraph may be modified if additional evidence is later discovered.\n**(3) Conciliation**\n**(A) In general**\nDuring the period beginning on the date on which a complaint is filed under this subsection and ending on the date of final disposition of such complaint (including during an investigation under paragraph (2)(B)), the Director shall, to the extent feasible, engage in conciliation with respect to such complaint.\n**(B) Conciliation agreement**\nA conciliation agreement arising out of such conciliation shall be an agreement between the respondent and the complainant, and shall be subject to approval by the Director.\n**(C) Rights protected**\nThe Director shall approve a conciliation agreement only if the agreement protects the rights of the complainant and other persons similarly situated.\n**(D) Reporting of agreement**\n**(i) In general**\nSubject to clause (ii), the Secretary shall make available to the State licensing authority described in paragraph (2)(B)(iv) a copy of a conciliation agreement entered into pursuant to this subsection unless the complainant and respondent otherwise agree, and the Secretary determines, that disclosure is not required to further the purposes of this subsection.\n**(ii) Limitation**\nA conciliation agreement that is made available to the State licensing authority pursuant to clause (i) may not disclose individually identifiable health information.\n**(4) Failure to comply with conciliation agreement**\nWhenever the Director has reasonable cause to believe that a respondent has breached a conciliation agreement, the Director shall refer the matter to the Attorney General to consider filing a civil action to enforce such agreement.\n**(5) Written consent for disclosure of information**\nNothing said or done in the course of conciliation under this subsection may be made public, or used as evidence in a subsequent proceeding under this subsection, without the written consent of the parties to the conciliation.\n**(6) Prompt judicial action**\n**(A) In general**\nIf the Director determines at any time following the filing of a complaint under this subsection that prompt judicial action is necessary to carry out the purposes of this subsection, the Director may recommend that the Attorney General promptly commence a civil action under subsection (d).\n**(B) Immediate suit**\nIf the Director determines at any time following the filing of a complaint under this subsection that the public interest would be served by allowing the complainant to bring a civil action under subsection (c) in a State or Federal court immediately, the Director shall certify that the administrative process has concluded and that the complainant may file such a suit immediately.\n**(7) Annual report**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Director shall make publicly available a report detailing the activities of the Office for Civil Rights and Health Equity under this subsection, including\u2014\n**(A)**\nthe number of complaints filed and the basis on which the complaints were filed;\n**(B)**\nthe number of investigations undertaken as a result of such complaints; and\n**(C)**\nthe disposition of all such investigations.\n##### (c) Enforcement by private persons\n**(1) In general**\n**(A) Civil action**\n**(i) In suit**\nA complainant under subsection (b) may commence a civil action to obtain appropriate relief with respect to an alleged violation of subsection (a), or for breach of a conciliation agreement under subsection (b), in an appropriate district court of the United States or State court\u2014\n**(I)**\nnot sooner than the earliest of\u2014\n**(aa)**\nthe date a conciliation agreement is reached under subsection (b);\n**(bb)**\nthe date of a final disposition of a complaint under subsection (b); or\n**(cc)**\n180 days after the first day of the alleged violation; and\n**(II)**\nnot later than 2 years after the final day of the alleged violation.\n**(ii) Statute of limitations**\nThe computation of such 2-year period shall not include any time during which an administrative proceeding (including investigation or conciliation) under subsection (b) was pending with respect to a complaint under such subsection.\n**(B) Barring suit**\nIf the Director has obtained a conciliation agreement under subsection (b) regarding an alleged violation of subsection (a), no action may be filed under this paragraph by the complainant involved with respect to the alleged violation except for the purpose of enforcing the terms of such an agreement.\n**(2) Relief which may be granted**\n**(A) In general**\nIn a civil action under paragraph (1), if the court finds that a violation of subsection (a) or breach of a conciliation agreement has occurred, the court may award to the plaintiff actual and punitive damages, and may grant as relief, as the court determines to be appropriate, any permanent or temporary injunction, temporary restraining order, or other order (including an order enjoining the defendant from engaging in a practice violating subsection (a) or ordering such affirmative action as may be appropriate).\n**(B) Fees and costs**\nIn a civil action under paragraph (1), the court, in its discretion, may allow the prevailing party, other than the United States, a reasonable attorney\u2019s fee and costs. The United States shall be liable for such fees and costs to the same extent as a private person.\n**(3) Intervention by Attorney General**\nUpon timely application, the Attorney General may intervene in a civil action under paragraph (1), if the Attorney General certifies that the case is of general public importance.\n##### (d) Enforcement by the Attorney General\n**(1) Commencement of actions**\n**(A) Pattern or practice cases**\nThe Attorney General may commence a civil action in any appropriate district court of the United States if the Attorney General has reasonable cause to believe that any health care provider covered by subsection (a)\u2014\n**(i)**\nis engaged in a pattern or practice that violates such subsection; or\n**(ii)**\nis engaged in a violation of such subsection that raises an issue of significant public importance.\n**(B) Cases by referral**\nThe Director may determine, based on a pattern of complaints, a pattern of violations, a review of data reported by a health care provider covered by subsection (a), or any other means, that there is reasonable cause to believe a health care provider is engaged in a pattern or practice that violates subsection (a). If the Director makes such a determination, the Director shall refer the related findings to the Attorney General. If the Attorney General finds that such reasonable cause exists, the Attorney General may commence a civil action in any appropriate district court of the United States.\n**(2) Enforcement of subpoenas**\nThe Attorney General, on behalf of the Director, or another party at whose request a subpoena is issued under this subsection, may enforce such subpoena in appropriate proceedings in the district court of the United States for the district in which the person to whom the subpoena was addressed resides, was served, or transacts business.\n**(3) Relief which may be granted in civil actions**\n**(A) In general**\nIn a civil action under paragraph (1), the court\u2014\n**(i)**\nmay award such preventive relief, including a permanent or temporary injunction, temporary restraining order, or other order against the person responsible for a violation of subsection (a) as is necessary to assure the full enjoyment of the rights granted by this subsection;\n**(ii)**\nmay award such other relief as the court determines to be appropriate, including monetary damages, to aggrieved persons; and\n**(iii)**\nmay, to vindicate the public interest, assess punitive damages against the respondent\u2014\n**(I)**\nin an amount not exceeding $500,000, for a first violation; and\n**(II)**\nin an amount not exceeding $1,000,000, for any subsequent violation.\n**(B) Fees and costs**\nIn a civil action under this subsection, the court, in its discretion, may allow the prevailing party, other than the United States, a reasonable attorney\u2019s fee and costs. The United States shall be liable for such fees and costs to the extent provided by section 2412 of title 28, United States Code.\n**(4) Intervention in civil actions**\nUpon timely application, any person may intervene in a civil action commenced by the Attorney General under paragraphs (1) and (2) if the action involves an alleged violation of subsection (a) with respect to which such person is an aggrieved person (including a person who is a complainant under subsection (b)) or a conciliation agreement to which such person is a party.\n##### (e) Definitions\nIn this section:\n**(1) Aggrieved person**\nThe term aggrieved person means\u2014\n**(A)**\na person who believes that the person was or will be injured in violation of subsection (a); or\n**(B)**\nthe personal representative or estate of a deceased person who was injured in violation of subsection (a).\n**(2) Director**\nThe term Director means the Director for Civil Rights and Health Equity of the Department of Health and Human Services.\n**(3) Disability**\nThe term disability has the meaning given such term in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 ).\n**(4) Conciliation**\nThe term conciliation means the attempted resolution of issues raised by a complaint, or by the investigation of such complaint, through informal negotiations involving the complainant, the respondent, and the Secretary.\n**(5) Conciliation agreement**\nThe term conciliation agreement means a written agreement setting forth the resolution of the issues in conciliation.\n**(6) Individually identifiable health information**\nThe term individually identifiable health information means any information, including demographic information collected from an individual\u2014\n**(A)**\nthat is created or received by a health care provider covered by subsection (a), health plan, employer, or health care clearinghouse;\n**(B)**\nthat relates to the past, present, or future physical or mental health or condition of, the provision of health care to, or the past, present, or future payment for the provision of health care to, the individual; and\n**(C)**\n**(i)**\nthat identifies the individual; or\n**(ii)**\nwith respect to which there is a reasonable basis to believe that the information can be used to identify the individual.\n**(7) Inequitable provision of health care**\nThe term inequitable provision of health care means the provision of any health care service, by a health care provider in a manner that\u2014\n**(A)**\nfails to meet a high-quality care standard, meaning the health care provider fails to\u2014\n**(i)**\navoid harm to patients as a result of the health services that are intended to help the patient;\n**(ii)**\nprovide health services based on scientific knowledge to all patients who benefit;\n**(iii)**\nrefrain from providing services to patients not likely to benefit;\n**(iv)**\nprovide care that is responsive to patient preferences, needs, and values; and\n**(v)**\navoids waits or delays in care; and\n**(B)**\nis discriminatory in intent or effect based at least in part on a basis specified in subsection (a).\n**(8) Respondent**\nThe term respondent means the person or other entity accused in a complaint of a violation of subsection (a).\n**(9) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(10) Social determinants of health**\nThe term social determinants of health means conditions in the environments in which individuals live, work, attend school, and worship, that affect a wide range of health, functioning, and quality-of-life outcomes and risks.\n##### (f) Rule of construction\nNothing in this section shall be construed as repealing or limiting the effect of title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ), section 1557 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18116 ), section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ), or the Age Discrimination Act of 1975 ( 42 U.S.C. 6101 et seq. ).\n#### 8. Federal Health Equity Commission\n##### (a) Establishment of Commission\n**(1) In general**\nThere is established the Federal Health Equity Commission (in this section referred to as the Commission ).\n**(2) Membership**\n**(A) In general**\nThe Commission shall be composed of\u2014\n**(i)**\n8 voting members appointed under subparagraph (B); and\n**(ii)**\nthe nonvoting, ex officio members described in subparagraph (C).\n**(B) Voting members**\nNot more than 4 of the members described in subparagraph (A)(i) shall at any one time be of the same political party. Such members shall have recognized expertise in and personal experience with racial and ethnic health inequities, health care needs of vulnerable and marginalized populations, and health equity as a vehicle for improving health status and health outcomes. Such members shall be appointed to the Commission as follows:\n**(i)**\n4 members of the Commission shall be appointed by the President.\n**(ii)**\n2 members of the Commission shall be appointed by the President pro tempore of the Senate, upon the recommendations of the majority leader and the minority leader of the Senate. Each member appointed to the Commission under this clause shall be appointed from a different political party.\n**(iii)**\n2 members of the Commission shall be appointed by the Speaker of the House of Representatives upon the recommendations of the majority leader and the minority leader of the House of Representatives. Each member appointed to the Commission under this clause shall be appointed from a different political party.\n**(C) Ex officio member**\nThe Commission shall have the following nonvoting, ex officio members:\n**(i)**\nThe Director for Civil Rights and Health Equity of the Department of Health and Human Services.\n**(ii)**\nThe Deputy Assistant Secretary for Minority Health of the Department of Health and Human Services.\n**(iii)**\nThe Director of the National Institute on Minority Health and Health Disparities.\n**(iv)**\nThe Chairperson of the Advisory Committee on Minority Health established under section 1707(c) of the Public Health Service Act ( 42 U.S.C. 300u\u20136(c) ).\n**(3) Terms**\nThe term of office of each member of the Commission appointed under paragraph (2)(B) shall be 6 years.\n**(4) Chairperson; Vice Chairperson**\n**(A) Chairperson**\nThe President shall, with the concurrence of a majority of the members of the Commission appointed under paragraph (2)(B), designate a Chairperson from among the members of the Commission appointed under such paragraph.\n**(B) Vice Chairperson**\n**(i) Designation**\nThe Speaker of the House of Representatives shall, in consultation with the majority leaders and the minority leaders of the Senate and the House of Representatives and with the concurrence of a majority of the members of the Commission appointed under paragraph (2)(B), designate a Vice Chairperson from among the members of the Commission appointed under such paragraph. The Vice Chairperson may not be a member of the same political party as the Chairperson.\n**(ii) Duty**\nThe Vice Chairperson shall act in place of the Chairperson in the absence of the Chairperson.\n**(5) Removal of members**\nThe President may remove a member of the Commission only for neglect of duty or malfeasance in office.\n**(6) Quorum**\nA majority of members of the Commission appointed under paragraph (2)(B) shall constitute a quorum of the Commission, but a lesser number of members may hold hearings.\n##### (b) Duties of the Commission\n**(1) In general**\nThe Commission shall\u2014\n**(A)**\nmonitor and report on the implementation of this Act; and\n**(B)**\ninvestigate, monitor, and report on progress towards health equity and the elimination of health disparities.\n**(2) Annual report**\nThe Commission shall\u2014\n**(A)**\nsubmit to the President and Congress at least one report annually on health equity and health disparities; and\n**(B)**\ninclude in such report\u2014\n**(i)**\na description of actions taken by the Department of Health and Human Services and any other Federal agency related to health equity or health disparities; and\n**(ii)**\nrecommendations on ensuring equitable health care and eliminating health disparities.\n##### (c) Powers\n**(1) Hearings**\n**(A) In general**\nThe Commission or, at the direction of the Commission, any subcommittee or member of the Commission, may, for the purpose of carrying out this section, as the Commission or the subcommittee or member considers advisable\u2014\n**(i)**\nhold such hearings, meet and act at such times and places, take such testimony, receive such evidence, and administer such oaths; and\n**(ii)**\nrequire, by subpoena or otherwise, the attendance and testimony of such witnesses and the production of such books, records, correspondence, memoranda, papers, documents, tapes, and materials.\n**(B) Limitation on hearings**\nThe Commission may hold a hearing under subparagraph (A)(i) only if the hearing is approved\u2014\n**(i)**\nby a majority of the members of the Commission appointed under subsection (a)(2)(B); or\n**(ii)**\nby a majority of such members present at a meeting when a quorum is present.\n**(2) Issuance and enforcement of subpoenas**\n**(A) Issuance**\nA subpoena issued under paragraph (1) shall\u2014\n**(i)**\nbear the signature of the Chairperson of the Commission; and\n**(ii)**\nbe served by any person or class of persons designated by the Chairperson for that purpose.\n**(B) Enforcement**\nIn the case of contumacy or failure to obey a subpoena issued under paragraph (1), the United States district court for the district in which the subpoenaed person resides, is served, or may be found may issue an order requiring the person to appear at any designated place to testify or to produce documentary or other evidence.\n**(C) Noncompliance**\nAny failure to obey the order of the court may be punished by the court as a contempt of court.\n**(3) Witness allowances and fees**\n**(A) In general**\nSection 1821 of title 28, United States Code, shall apply to a witness requested or subpoenaed to appear at a hearing of the Commission.\n**(B) Expenses**\nThe per diem and mileage allowances for a witness shall be paid from funds available to pay the expenses of the Commission.\n**(4) Postal services**\nThe Commission may use the United States mails in the same manner and under the same conditions as other agencies of the Federal Government.\n**(5) Gifts**\nThe Commission may accept, use, and dispose of gifts or donations of services or property.\n##### (d) Administrative Provisions\n**(1) Staff**\n**(A) Director**\nThere shall be a full-time staff director for the Commission who shall\u2014\n**(i)**\nserve as the administrative head of the Commission; and\n**(ii)**\nbe appointed by the Chairperson with the concurrence of the Vice Chairperson.\n**(B) Other personnel**\nThe Commission may\u2014\n**(i)**\nappoint such other personnel as it considers advisable, subject to the provisions of title 5, United States Code, governing appointments in the competitive service, and the provisions of chapter 51 and subchapter III of chapter 53 of that title relating to classification and General Schedule pay rates; and\n**(ii)**\nmay procure temporary and intermittent services under section 3109(b) of title 5, United States Code, at rates for individuals not in excess of the daily equivalent paid for positions at the maximum rate for GS\u201315 of the General Schedule under section 5332 of title 5, United States Code.\n**(2) Compensation of members**\n**(A) Non-Federal employees**\nEach member of the Commission who is not an officer or employee of the Federal Government shall be compensated at a rate equal to the daily equivalent of the annual rate of basic pay prescribed for level IV of the Executive Schedule under section 5315 of title 5, United States Code, for each day (including travel time) during which the member is engaged in the performance of the duties of the Commission.\n**(B) Federal employees**\nEach member of the Commission who is an officer or employee of the Federal Government shall serve without compensation in addition to the compensation received for the services of the member as an office or employee of the Federal Government.\n**(C) Travel expenses**\nA member of the Commission shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for an employee of an agency under subchapter I of chapter 57 of title 5, United States Code, while away from the home or regular place of business of the member in the performance of the duties of the Commission.\n**(3) Cooperation**\nThe Commission may secure directly from any Federal department or agency such information as the Commission considers necessary to carry out this Act. Upon request of the Chairman of the Commission, the head of such department or agency shall furnish such information to the Commission.\n##### (e) Permanent Commission\nSection 1013 of title 5, United States Code, shall not apply to the Commission.\n##### (f) Authorization of appropriations\nThere are authorized to be appropriated for fiscal year 2025 and each fiscal year thereafter such sums as may be necessary to carry out the duties of the Commission.\n#### 9. Grants for hospitals to promote equitable health care and outcomes\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Health and Human Services (in this section referred to as the Secretary ) shall award grants to hospitals to promote equitable health care treatment and services, and reduce disparities in care and outcomes.\n##### (b) Consultation\nIn establishing the criteria for grants under this section and evaluating applications for such grants, the Secretary shall consult with the Director for Civil Rights and Health Equity of the Department of Health and Human Services.\n##### (c) Use of funds\nA hospital shall use funds received from a grant under this section to establish or expand programs to provide equitable health care to all patients and to ensure equitable health care outcomes. Such uses may include\u2014\n**(1)**\nproviding explicit and implicit bias training to medical providers and staff;\n**(2)**\nproviding translation or interpretation services for patients;\n**(3)**\nrecruiting and training a diverse workforce;\n**(4)**\ntracking data related to care and outcomes; and\n**(5)**\ntraining on cultural sensitivity.\n##### (d) Priority\nIn awarding grants under this section, the Secretary shall give priority to hospitals that have received disproportionate share hospital payments under section 1886(r) of the Social Security Act ( 42 U.S.C. 1395ww(r) ) or section 1923 of such Act ( 42 U.S.C. 1396r\u20134 ) with respect to fiscal year 2025.\n##### (e) Supplement, not supplant\nGrants awarded under this section shall be used to supplement, not supplant, any nongovernment efforts, or other Federal, State, or local funds provided to a recipient.\n##### (f) Equitable health care defined\nThe term equitable health care has the meaning given such term in subclause (VIII)(cc) of section 1886(b)(3)(B)(viii) of the Social Security Act ( 42 U.S.C. 1395ww(b)(3)(B)(viii) ), as added by section 4(a).",
      "versionDate": "2025-07-17",
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
        "name": "Health",
        "updateDate": "2025-09-05T15:12:25Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2347is.xml"
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
      "title": "Equal Health Care for All Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Equal Health Care for All Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit discrimination in health care and require the provision of equitable health care, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:21Z"
    }
  ]
}
```
