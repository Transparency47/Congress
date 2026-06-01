# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1756?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1756
- Title: Conscience Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1756
- Origin chamber: Senate
- Introduced date: 2025-05-14
- Update date: 2026-04-06T19:40:38Z
- Update date including text: 2026-04-06T19:40:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in Senate
- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-05-14: Introduced in Senate

## Actions

- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1756",
    "number": "1756",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Conscience Protection Act of 2025",
    "type": "S",
    "updateDate": "2026-04-06T19:40:38Z",
    "updateDateIncludingText": "2026-04-06T19:40:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-14",
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
      "actionDate": "2025-05-14",
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
        "item": [
          {
            "date": "2026-03-19T14:00:24Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-14T16:26:55Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-14T16:26:55Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "ND"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "SD"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "ID"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "WY"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MS"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "NC"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MO"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "IN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "NE"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "IA"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "NE"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "UT"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "IN"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "ID"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "LA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "TN"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "OK"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "AR"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "TX"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "ND"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "FL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1756is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1756\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mr. Lankford (for himself, Mr. Cramer , Mr. Rounds , Mr. Risch , Ms. Lummis , Mr. Daines , Mrs. Hyde-Smith , Mr. Budd , Mr. Hawley , Mr. Young , Mr. Ricketts , Ms. Ernst , Mrs. Fischer , Mr. Lee , Mr. Banks , and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to prohibit discrimination against health care entities that do not participate in abortion, and to strengthen implementation and enforcement of Federal conscience laws.\n#### 1. Short title\nThis Act may be cited as the Conscience Protection Act of 2025 .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nThomas Jefferson stated a conviction common to our Nation\u2019s founders when he declared in 1809 that [n]o provision in our Constitution ought to be dearer to man than that which protects the rights of conscience against the enterprises of the civil authority .\n**(2)**\nNo health care entity should have to choose between giving up their religious, moral, ethical, or medical convictions and abandoning a vital medical mission. Congress enacted more than two dozen provisions in Federal statutes to protect such rights in health care, which also protect States ability to operate in accordance with their laws to protect similar rights without fear of retaliation from the Federal Government. Such provisions of Federal statutes include\u2014\n**(A)**\nsubsections (b) through (e) of section 401 of the Health Programs Extension Act of 1973 ( 42 U.S.C. 300a\u20137 ) (commonly known, and referred to in this section, as the Church Amendments );\n**(B)**\nsection 245 of the Public Health Service Act ( 42 U.S.C. 238n ) (commonly known as the Coats-Snowe Amendment );\n**(C)**\nthe Weldon Amendment approved by Congresses and Presidents of both parties every year since 2004 (including section 507(d) of the Departments of Labor, Health and Human Services, and Education, and Related Agencies Appropriations Act, 2023 (division H of the Consolidated Appropriations Act, 2023 ( Public Law 117\u2013328 ))); and\n**(D)**\nother conscience protections, as outlined in the final rule issued by the Secretary of Health and Human Services entitled Protecting Statutory Conscience Rights in Health Care; Delegations of Authority (84 Fed. Reg. 23170; May 21, 2019), under the Patient Protection and Affordable Care Act, under the Social Security Act, and with respect to global health programs and advanced directives.\n**(3)**\nCourts have held that certain conscience protection statutes do not provide a private right of action for individuals or entities who have been discriminated against, thereby leaving victims of discrimination unable to defend their own conscience rights in court. At the same time, administrative implementation and enforcement of these laws by the Office for Civil Rights of the Department of Health and Human Services have been inconsistent and at times cases are allowed to languish for years or previously enacted enforcement measures are abandoned or reversed.\n**(4)**\nDefying the Weldon Amendment, the California Department of Managed Health Care has mandated coverage for elective abortions in all health plans under its jurisdiction. Other States, such as New York, Illinois, and Washington, have taken or considered similar action, and some States have required hospitals to provide or facilitate abortions. On June 21, 2016, the Office for Civil Rights of the Department of Health and Human Services, under the Obama Administration, concluded a nearly 2-year investigation of this matter by determining that the decision of California to require insurance plans under the California Department for Managed Health Care authority to cover abortion services did not violate the Weldon Amendment. At least 28,000 individuals and families subsequently lost abortion-free health plans as a result of this mandate in violation of their consciences and rights under the Weldon Amendment.\n**(5)**\nOn January 24, 2020, the Office for Civil Rights of the Department of Health and Human Services disavowed its prior findings and issued a notice of violation of the Weldon Amendment to California. After the State\u2019s continued noncompliance with the Weldon Amendment, the Centers for Medicare & Medicaid Services, on December 16, 2020, announced the disallowance of $200,000,000 per quarter in Federal funds to California beginning in the first quarter of 2021.\n**(6)**\nAlthough California had taken no action to come into compliance with the Weldon Amendment, on August 13, 2021, the Office for Civil Rights of the Department of Health and Human Services under the Biden Administration withdrew the notice of violation and closed the complaints filed with the Department. As a result, individuals continue to be coerced contrary to law into choosing between violating their consciences or forgoing health care coverage for themselves, their employees, and their families.\n**(7)**\n**(A)**\nOn August 28, 2019, the Office for Civil Rights of the Department of Health and Human Services under the Trump Administration issued a notice of violation against the University of Vermont Medical Center for violation of the Church Amendments after it was found to have scheduled approximately 10 nurses who had registered conscience objections to abortion to assist with approximately 20 abortion procedures and for maintaining policies that explicitly required employees with conscience objections to participate in procedures with which they disagreed to ensure that patient care is not negatively impacted . Such practices were found to be part of an ongoing pattern, practice, and policy of discriminating against health care providers who believe that the performance, or the assistance in the performance, of abortions is contrary to their religious beliefs or moral convictions .\n**(B)**\nAfter the University of Vermont Medical Center refused to come into compliance with the law, the Department of Justice brought an enforcement action in Federal court against the medical center on December 16, 2020.\n**(C)**\nOn July 30, 2021, the Department of Justice under the Biden Administration voluntarily dismissed the case, without any binding settlement or requirement that the University of Vermont Medical Center remedy its unlawful policies or make restitution to the employees whose rights it violated.\n**(8)**\nOn May 21, 2019, the Secretary of Health and Human Services issued the final rule entitled Protecting Statutory Conscience Rights in Health Care; Delegations of Authority (84 Fed. Reg. 23170; May 21, 2019) to implement 25 Federal conscience protection provisions governing programs funded under the Department of Health and Human Services and provide mechanisms to enforce conscience laws to ensure that the government and government-funded entities are not unlawfully discriminating against health care entities. Despite this regulation providing for enforcement of laws passed by Congress, the rule faced numerous legal challenges and was vacated.\n**(9)**\nOn January 11, 2024, the Department of Health and Human Services published a final rule that fails to equip the Department with the tools necessary for effective enforcement of Federal statutory protections of rights of conscience.\n**(10)**\nCongress has acted numerous times to expand access to health care and has also acted numerous times to provide unqualified statutorily protected rights of conscience to individuals and entities in certain circumstances. A health care entity\u2019s decision not to participate in an abortion, assisted suicide, procedures that can result in sterilization, or other interventions erects no barrier to those legally seeking to perform or undergo such interventions elsewhere.\n**(11)**\nThe vast majority of medical professionals do not perform abortions. Ninety-three percent of obstetricians/gynecologists in private practice report that they did not provide abortions (National Library of Medicine, April 2018) and the great majority of hospitals choose to do so only in rare cases or not at all.\n**(12)**\nIn the landmark 2022 decision, Dobbs v. Jackson Women\u2019s Health Organization, the Supreme Court held that the Constitution does not confer a right to abortion .\n**(13)**\nOn July 13, 2022, the Department of Health and Human Services issued guidance to retail pharmacies in the United States. Such guidance purported to address their obligations under Federal nondiscrimination laws, but in actuality orders pharmacies to stock and dispense abortion pills despite the fact that pharmacies and pharmacists have a right to not violate their conscience by participating in abortion under existing law.\n**(14)**\nConscience protections pose no conflict with other Federal laws, such as the law requiring stabilizing treatment for a pregnant woman \u2026 or her unborn child when either needs emergency care (Emergency Medical Treatment and Active Labor Act). As previous Administrations have said, these areas of law have operated side by side for many years and both should be fully enforced (76 Fed. Reg. 9968\u201377 (2011) at 9973).\n**(15)**\nReaffirming longstanding Federal policy on conscience rights and providing a private right of action in cases where it is violated allows longstanding and widely supported Federal laws to work as intended.\n#### 3. Prohibiting discrimination against health care entities that do not participate in abortion\nTitle II of the Public Health Service Act ( 42 U.S.C. 202 et seq. ) is amended by inserting after section 245 the following:\n245A. Prohibiting discrimination against health care entities that do not participate in abortion (a) In general Notwithstanding any other law, the Federal Government, and any individual or entity that receives Federal financial assistance, including any State or local government, may not penalize, retaliate against, or otherwise discriminate against a health care entity on the basis that such health care entity does not or declines to\u2014 (1) provide, perform, refer for, pay for, or otherwise participate in abortion; (2) provide or sponsor abortion coverage; or (3) facilitate or make arrangements for any of the activities specified in this subsection. (b) Rule of construction Nothing in this section shall be construed\u2014 (1) to prevent any health care entity from voluntarily electing to participate in abortions or abortion referrals where not prohibited by any other law; (2) to prevent any health care entity from voluntarily electing to provide or sponsor abortion coverage or health benefits coverage that includes abortion where not prohibited by any other law; (3) to prevent an accrediting agency, the Federal Government, or a State or local government from establishing standards of medical competency applicable only to those who have knowingly, voluntarily, and specifically elected to perform abortions, or from enforcing contractual obligations applicable only to those who, as part of such contract, knowingly, voluntarily, and specifically elect to provide abortions; (4) to affect, or be affected by, any Federal law that requires stabilizing treatment for a pregnant woman or her unborn child when either needs emergency care; or (5) to supersede any law enacted by any State for the purpose of regulating insurance, except as specified in subsection (a). (c) Definitions For purposes of this section: (1) Federal financial assistance The term Federal financial assistance means Federal payments to cover the cost of health care services or benefits, or other Federal payments, grants, or loans to promote or otherwise facilitate health-related activities. (2) Health care entity The term health care entity includes\u2014 (A) an individual physician, health care assistant, nurse, pharmacist, health researcher, or other health care personnel; (B) a hospital, laboratory, pharmacy, health system, or other health care or medical research facility or organization (including a party to a proposed merger or other collaborative arrangement relating to health services, and an entity resulting therefrom); (C) a provider-sponsored organization, an accountable care organization, or a health maintenance organization; (D) a social services provider that provides or authorizes referrals for health care services; (E) a program of training or education in the health professions or medical research, a participant in such a program, or any individual applying or otherwise aspiring to participate in such a program; (F) an issuer of health insurance coverage or of a health plan; (G) a health care sharing ministry; (H) a health insurance plan, including group, individual, or student health plans, or a sponsor or administrator thereof; or (I) any other health care organization, program, facility, or plan. (3) State or local government The term State or local government includes every agency and other governmental unit and subdivision of a State or local government, if such State or local government, or any agency or governmental unit or subdivision thereof, receives Federal financial assistance. .\n#### 4. Strengthening enforcement of Federal conscience laws\nTitle II of the Public Health Service Act ( 42 U.S.C. 202 et seq. ), as amended by section 3, is further amended by inserting after section 245A the following:\n245B. Administrative enforcement of Federal conscience laws (a) Regulations (1) In general Under this section, the Secretary may issue regulations under any provision of law described in paragraph (2). (2) Provisions of law The provisions of law described in this paragraph are each of the following: (A) Sections 245, 245A, 399M(d), and 520E(f) of this Act. (B) The Religious Freedom Restoration Act of 1993, with respect to any program or activity funded, administered, or conducted by the Department of Health and Human Services. (C) Any of subsections (b) through (e) of section 401 of the Health Programs Extension Act of 1973 (commonly known as the Church Amendments ), only with respect to an objection based on a religious belief or moral conviction. (D) Section 507(d) of the Departments of Labor, Health and Human Services, and Education, and Related Agencies Appropriations Act, 2023 (division H of the Consolidated Appropriations Act, 2023 ( Public Law 117\u2013328 )) (commonly known as the Weldon Amendment ) and any subsequent substantially similar provision in an appropriations Act, to the extent administered by the Secretary. (E) Section 209 of the Departments of Labor, Health and Human Services, and Education, and Related Agencies Appropriations Act, 2023 (division H of the Consolidated Appropriations Act, 2023 ( Public Law 117\u2013328 )) and any subsequent substantially similar provision in an appropriations Act, to the extent administered by the Secretary. (F) Clauses (i) and (ii) of paragraph (1)(A) of section 1303(b) of the Patient Protection and Affordable Care Act (only with respect to a determination not to provide coverage of abortion), and paragraph (4) of such section. (G) Section 1411(b)(5)(A) of the Patient Protection and Affordable Care Act (other than with respect to an exemption as an Indian or a hardship exemption) and section 5000A(d)(2)(A) of the Internal Revenue Code of 1986. (H) Section 1553 of the Patient Protection and Affordable Care Act. (I) Sections 1122(h), 1162, 1821, 1861(e), 1861(y)(1), and 1861(ss) of the Social Security Act, and the first paragraph of the matter following section 1902(a)(87)(D) of such Act, each of such provisions only with respect to protections for religious nonmedical health care institutions. (J) Sections 1852(j)(3)(B), 1866(f)(4), 1902(w)(3), 1902(w)(5), 1907, 1928(c)(2)(B)(ii) (with respect to a religious or other exemption), 1932(b)(3)(B), and 2012(b) of such Act. (K) Section 4206(c) of the Omnibus Budget Reconciliation Act of 1990. (L) Section 7 of the Assisted Suicide Funding Restriction Act of 1997. (M) Section 113(a) of the Child Abuse Prevention and Treatment Act. (N) Section 301(d) of the United States Leadership Against HIV/AIDS, Tuberculosis, and Malaria Act of 2003 to the extent administered by the Secretary. (O) The third sentence of section 20(a)(5) of the Occupational Safety and Health Act of 1970. (P) Section 104(f)(1) of the Foreign Assistance Act of 1961 (commonly known as the Helms Amendment ), and any provision of an appropriations Act or other Federal law that restates or incorporates by reference the protections of such section, to the extent administered by the Secretary. (Q) The ninth proviso under the heading Global Health Programs under the heading Funds Appropriated to the President under title III of the Department of State, Foreign Operations, and Related Programs Appropriations Act, 2023 (division K of the Consolidated Appropriations Act, 2023 ( Public Law 117\u2013328 )) and any subsequent substantially similar provision in an appropriations Act to the extent administered by the Secretary. (R) Any other provision of law protecting the exercise of conscience or religious freedom under programs or activities funded, administered, or conducted by the Department of Health and Human Services. (b) Office for Civil Rights The Secretary shall designate the Director of the Office for Civil Rights of the Department of Health and Human Services\u2014 (1) to receive complaints alleging a violation of any provision of law described in subsection (a)(2); and (2) to promptly investigate such complaints, issue findings, and require corrective action in cases of such a violation. (c) Enforcement (1) In general The Secretary shall, as permitted under law (including the Constitution of the United States), induce compliance of an individual or entity, including a State or local government, failing to comply with any provision of law described in subsection (a)(2), by terminating, in whole or in part, any Federal financial assistance provided by the Secretary to such individual or entity. (2) Referrals The Secretary shall, as the Secretary determines necessary for inducing compliance with a provision described in paragraph (1), refer a violation of such a provision to the Attorney General for a civil action in accordance with section 245C. 245C. Civil action for violations of Federal conscience laws (a) In general A qualified party may, in a civil action, obtain relief described in subsection (e) with respect to a designated violation. (b) Definitions For purposes of this section: (1) Designated violation The term designated violation means an actual or threatened violation of any provision of law described in section 245B(a)(2). (2) Qualified party The term qualified party means\u2014 (A) the Attorney General; or (B) any individual or entity adversely affected by the designated violation without regard to whether such individual or entity is a health care entity as defined in section 245A(c). (c) Administrative remedies not required An action under this section may be commenced, and relief may be granted, without regard to whether the party commencing the action has sought or exhausted any available administrative remedies. (d) Defendants in actions under this section may include governmental entities as well as others (1) In general An action under this section may be maintained against any individual or entity receiving Federal financial assistance (as defined in section 245A(c)), including a State governmental entity. Relief in an action under this section may include money damages even if the defendant is a governmental entity. (2) Definition For the purposes of this subsection, the term State governmental entity means a State, a local government within a State, and any agency or other governmental unit or subdivision of a State, or of such a local government. (e) Nature of relief In an action under this section, the court shall grant\u2014 (1) all appropriate relief, including injunctive relief, declaratory relief, and compensatory damages to prevent the occurrence, continuance, or repetition of the designated violation and to compensate for losses resulting from the designated violation; and (2) to a prevailing plaintiff, reasonable attorneys\u2019 fees and litigation costs. .\n#### 5. Severability\nIf any provision of this Act or an amendment made by this Act, or the application of such a provision or amendment to any individual, entity, government, or circumstance, is held to be unconstitutional, the remainder of this Act and the amendments made by this Act, and the application of such provision or amendment to any other individual, entity, government, or circumstance, shall not be affected.",
      "versionDate": "2025-05-14",
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
        "actionDate": "2025-05-14",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3411",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Conscience Protection Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Abortion",
            "updateDate": "2026-04-06T19:40:25Z"
          },
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-04-06T19:40:28Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-04-06T19:40:38Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2026-04-06T19:40:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-29T15:43:35Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1756is.xml"
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
      "title": "Conscience Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Conscience Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to prohibit discrimination against health care entities that do not participate in abortion, and to strengthen implementation and enforcement of Federal conscience laws.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:49Z"
    }
  ]
}
```
