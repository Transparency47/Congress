# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3235?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3235
- Title: MOMS Act
- Congress: 119
- Bill type: HR
- Bill number: 3235
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2026-05-21T08:08:16Z
- Update date including text: 2026-05-21T08:08:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-07 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-07 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3235",
    "number": "3235",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000470",
        "district": "7",
        "firstName": "Michelle",
        "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
        "lastName": "Fischbach",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "MOMS Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:16Z",
    "updateDateIncludingText": "2026-05-21T08:08:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T14:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-07T14:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "MN"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "MN"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "IL"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "WV"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "FL"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "TN"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "MS"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "FL"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "IA"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "VA"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "NC"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "WV"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "NJ"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "IA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "FL"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "SC"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "TN"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "MD"
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
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NC"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "VA"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "ND"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3235ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3235\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Mrs. Fischbach (for herself, Mr. Finstad , Mr. Stauber , Mrs. Miller of Illinois , Mrs. Miller of West Virginia , Ms. Tenney , Mr. Webster of Florida , Mrs. Harshbarger , Mr. Guest , Mrs. Cammack , Mrs. Hinson , Mr. McGuire , Mr. McDowell , Mr. Moore of West Virginia , and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Public Health Service Act to provide more opportunities for mothers to succeed, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the More Opportunities for Moms to Succeed Act or the MOMS Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Federal clearinghouse of resources for expecting moms\nSec. 101. Pregnancy.gov.\nSec. 102. National list of licensed child placement agencies.\nSec. 103. List of funding opportunities available to pregnancy support centers.\nTITLE II\u2014Improving access to prenatal and postnatal resources\nSec. 201. Positive alternatives for women.\nSec. 202. Improving access to prenatal and postnatal telehealth care.\nTITLE III\u2014Unborn child support\nSec. 301. Child support enforcement on behalf of unborn children.\nI\nFederal clearinghouse of resources for expecting moms\n#### 101. Pregnancy.gov\nThe Public Health Service Act ( 42 U.S.C. 201 et seq. ) is amended by adding at the end the following:\nXXXIV Resource directory for moms 3401. Establishment of pregnancy.gov website (a) Website Not later than 1 year after the date of enactment of this section, the Secretary shall publish a public website entitled pregnancy.gov . The Secretary may not delegate implementation or administration of the website below the level of the Office of the Secretary. The website shall include the following: (1) A clearinghouse of relevant resources available for pregnant and postpartum women, and women parenting young children. (2) A series of questions through which a user is able to generate a list of relevant resources of interest within the user\u2019s ZIP Code. (3) A means to direct the user to identify whether to list the relevant resources of interest that are available online or within 1, 5, 10, 50, and 100 miles of the user. (4) A mechanism for users to take an assessment through the website and provide consent to use the user\u2019s contact information, which the Secretary may use to conduct outreach via phone or email to follow up with users on additional resources that would be helpful for the users to review. (b) Resource list aggregation (1) In general The Secretary shall invite each State to provide recommendations of relevant resources referred to in subsection (a)(3) for such State. (2) Criteria for making recommendations The Secretary shall develop criteria to provide to the States to determine whether resources recommended as described in paragraph (1) should appear on the website. Such criteria shall include the requirement that the relevant resource is not a prohibited entity. (3) Grant program (A) In general The Secretary shall provide grants to States to establish or support a system that\u2014 (i) aggregates relevant resources referred to in subsection (a)(3), in accordance with the criteria developed under paragraph (2); and (ii) may be coordinated, to the extent determined appropriate by the State, by a statewide, regionally-based, or community-based public or private entity. (B) Applications To be eligible to receive a grant under subparagraph (A), a State shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including a plan for outreach and awareness activities, and a list of relevant resources that would be included in the State system supported by the grant. (c) Prohibition regarding certain entities Relevant resources listed on the website, and any additional resources promoted by the Secretary, may not include any resource offered by a prohibited entity. No prohibited entity may receive a grant provided under subsection (b)(3). (d) Services in different languages The Secretary shall ensure that the website provides the widest possible access to services for families who speak languages other than English. (e) Reporting requirements (1) In general Not later than 180 days after the date on which the website is established under this section, the Secretary shall submit to Congress a report on\u2014 (A) the traffic of the website; (B) user feedback on the accessibility and helpfulness of the website in tailoring to the user\u2019s needs; (C) insights on gaps in relevant resources with respect to services for pregnant and postpartum women, or women parenting young children; (D) suggestions on how to improve user experience and accessibility based on user feedback and missing resources that would be helpful to include in future updates; and (E) certification that no prohibited entities are listed as a relevant resource or are in receipt of a grant under subsection (b)(3). (2) Confidentiality The report under paragraph (1) shall not include any personal identifying information regarding individuals who have used the website. (f) Authorization of appropriations To carry out this section, there are authorized to be appropriated such sums as may be necessary for each of fiscal years 2025 through 2030. (g) Definitions In this section: (1) Abortion The term abortion means the use or prescription of any instrument, medicine, drug, or any other substance or device to intentionally\u2014 (A) kill the unborn child of a woman known to be pregnant; or (B) terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) after viability, to produce a live birth and preserve the life and health of the child born alive; (ii) to remove a dead unborn child; or (iii) to treat an ectopic pregnancy. (2) Born alive The term born alive has the meaning given such term in section 8(b) of title 1, United States Code. (3) Prohibited entity The term prohibited entity means an entity, including its affiliates, subsidiaries, successors, and clinics, that performs, induces, refers for, or counsels in favor of abortions, or provides financial support to any other organization that conducts such activities. (4) Relevant resources The term relevant resources means the Federal, State, local governmental, and private resources that serve pregnant and postpartum women, or women parenting young children in the categories of the following topics: (A) Mentorship opportunities, including pregnancy and parenting help and case management resources. (B) Health and well-being services, including women\u2019s medical services such as obstetrical and gynecological support services for women, abortion pill reversal, breastfeeding, general health services, primary care, and dental care. (C) Financial assistance, work opportunities, nutrition assistance, childcare, and education opportunities for parents. (D) Material or legal support, including transportation, food, nutrition, clothing, household goods, baby supplies, housing, shelters, maternity homes, tax preparation, legal support for child support, family leave, breastfeeding protections, and custody issues. (E) Recovery and mental health services, including services with respect to addiction or suicide intervention, intimate partner violence, sexual assault, rape, sex trafficking, and counseling for women and families surrounding unexpected loss of a child. (F) Prenatal diagnostic services, including disability support organizations, medical interventions for a baby, perinatal hospice resources, pregnancy and infant loss support, and literature on pregnancy wellness. (G) Healing and support services for abortion survivors and their families. (H) Services providing childcare, adoption, foster care, and short term childcare services and resources. (I) Comprehensive information on alternatives to abortion. (J) Information about abortion risks, including complications and failures. (K) Links to information on child development from moment of conception. (5) Unborn child The term unborn child has the meaning given such term in section 1841(d) of title 18, United States Code. (6) Website The term website means the public website entitled pregnancy.gov required to be established under subsection (a). .\n#### 102. National list of licensed child placement agencies\n##### (a) In general\nSection 474 of the Social Security Act ( 42 U.S.C. 674 ) is amended by adding at the end the following:\n(h) National list of licensed child placement agencies (1) State reporting (A) In general Not later than January 1 of each fiscal year, a State with a plan approved under this part for the fiscal year shall submit to the Secretary a list of private child placement agencies that, as of the end of the preceding fiscal year, were licensed or accredited by, and in good standing with, the State and exempt from Federal income tax by reason of section 501(c)(3) of the Internal Revenue Code of 1986. (B) Child placement agency In subparagraph (A), the term child placement agency means an agency that places children in prospective adoptive homes. (2) National list The Secretary, through the United States Children\u2019s Bureau, shall compile and maintain on the public website entitled pregnancy.gov required to be established under title XXXIV of the Public Health Service Act, a publicly available list consisting of each list most recently submitted by a State under paragraph (1). (3) Annual reports to congress Not later than the 2nd December 31 after the date of the enactment of this subsection, and annually thereafter, the Secretary shall submit to the Congress a written report that contains the list maintained under paragraph (2) and identifies any child placement agency that is licensed by a State and is not on the list, and a specification of any disciplinary actions that a State has taken against a private child placement agency. .\n##### (b) Loss of eligibility for adoption and legal guardianship incentive payments for failure of state To comply with list submission requirement\nSection 473A(b) of such Act ( 42 U.S.C. 673b(b) ) is amended\u2014\n**(1)**\nby striking and at the end of paragraph (3);\n**(2)**\nby striking the period at the end of paragraph (4) and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(5) the State has complied with section 474(h)(1) with respect to the preceding fiscal year. .\n#### 103. List of funding opportunities available to pregnancy support centers\nTitle XXXIV of the Public Health Service Act (as added by section 101) is amended by adding at the end the following:\n3402. List of funding opportunities available to pregnancy support centers The Secretary shall compile and maintain on the public website entitled pregnancy.gov required to be established under section 3401, a publicly available list of Federal funding opportunities available to nonprofit and health care entities for pregnancy support services that offer or provide the relevant resources (as defined in subsection (g) of such section). .\nII\nImproving access to prenatal and postnatal resources\n#### 201. Positive alternatives for women\n##### (a) Program authority\n**(1) Purpose**\nThe purpose of grants under this section shall be to support, encourage, and assist women\u2014\n**(A)**\nto carry their pregnancies to term; and\n**(B)**\nto care for themselves and their babies after birth.\n**(2) Grants**\nFor the purpose described in paragraph (1), the Secretary shall award grants to eligible entities described in subsection (b) to provide information on, referral to, and direct services as described in subsection (c).\n##### (b) Eligibility\n**(1) Eligible entities**\nTo be eligible for a grant under this section, an entity shall\u2014\n**(A)**\nbe a nonprofit organization;\n**(B)**\nsupport, encourage, and assist women as described in subsection (a)(1);\n**(C)**\nagree to be subject to such monitoring and review as the Secretary may require under subsection (g);\n**(D)**\nagree to not charge women for services provided through the grant;\n**(E)**\nprovide each pregnant woman counseled through the grant with accurate information on the developmental characteristics of babies and of unborn children, including offering printed information; and\n**(F)**\nhave a privacy policy and procedures in place to ensure that\u2014\n**(i)**\nthe name, address, telephone number, or any other information that might identify any woman seeking services supported through the grant is not made public or shared with any other entity without the written consent of the woman; and\n**(ii)**\nthe grantee adheres to requirements comparable to those applicable under the HIPAA privacy regulation (as defined in section 1180(b)(3) of the Social Security Act ( 42 U.S.C. 1320d\u20139(b)(3) )) to covered entities (as defined for purposes of such regulation).\n**(2) Ineligible entities**\nAn entity shall be ineligible to receive a grant under this section if the entity or any affiliate, subsidiary, successor, or clinic thereof\u2014\n**(A)**\nperforms, induces, refers for, or counsels in favor of abortions; or\n**(B)**\nprovides financial support to any other entity that conducts any activity described in subparagraph (A).\n**(3) Financial records**\nAs a condition on receipt of a grant under this section, an eligible entity shall agree to maintain and make available to the Secretary records, including financial records, that demonstrate that the entity satisfies the requirements of paragraph (1) and is not ineligible by operation of paragraph (2).\n##### (c) Covered services\n**(1) Required information and referral**\nFor the purpose described in subsection (a)(1), an eligible entity receiving a grant under this section shall use the grant to provide to pregnant and postpartum women, or women parenting young children, information on, and referral to, each of the following services:\n**(A)**\nMedical care.\n**(B)**\nNutritional services.\n**(C)**\nHousing assistance.\n**(D)**\nAdoption services.\n**(E)**\nEducation and employment assistance, including services that support the continuation and completion of high school.\n**(F)**\nChild care assistance.\n**(G)**\nParenting education and support services.\n**(H)**\nVoluntary substance abuse counseling and treatment.\n**(2) Permissible direct provision of services**\nFor the purpose described in subsection (a)(1), in addition to using a grant under this section as described in paragraph (1), an eligible entity receiving a grant under this section may use the grant for the direct provision of one or more services listed in paragraph (1).\n##### (d) Prohibited uses of funds\nNone of the funds made available under this section shall be used\u2014\n**(1)**\nfor health benefits coverage that includes coverage of abortion;\n**(2)**\nfor providing or assisting a woman to obtain adoption services from a provider of adoption services that is not licensed; and\n**(3)**\nfor any of the activities described in subsection (b)(2).\n##### (e) Consideration\nIn selecting the recipients of grants under this section, the Secretary shall consider each applicant\u2019s demonstrated capacity in providing services to assist a pregnant woman in carrying her pregnancy to term.\n##### (f) Monitoring and review\nThe Secretary shall\u2014\n**(1)**\nmonitor and review each program funded through a grant under this section to ensure that the grantee carefully adheres to\u2014\n**(A)**\nthe purpose described in subsection (a)(1); and\n**(B)**\nthe requirements of this section; and\n**(2)**\ncease to fund a program under this section if the grantee fails to adhere to such purpose and requirements.\n##### (g) Definitions\nIn this section:\n**(1) Abortion**\nThe term abortion means the use or prescription of any instrument, medicine, drug, or any other substance or device to intentionally\u2014\n**(A)**\nkill the unborn child of a woman known to be pregnant; or\n**(B)**\nterminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014\n**(i)**\nafter viability, to produce a live birth and preserve the life and health of the child born alive;\n**(ii)**\nto remove a dead unborn child; or\n**(iii)**\nto treat an ectopic pregnancy.\n**(2) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n##### (h) Authorization of appropriations\nTo carry out this section, there are authorized to be appropriated such sums as may be necessary for each of fiscal years 2025 through 2030.\n#### 202. Improving access to prenatal and postnatal telehealth care\n##### (a) In general\nThe Secretary shall award grants to, or enter into cooperative agreements with, eligible entities to purchase equipment necessary for carrying out at-home telehealth visits for screening, monitoring, and management of prenatal and postnatal care for the purpose of improving maternal and infant health outcomes, and reducing maternal mortality, by improving access to care in rural areas, frontier counties, medically underserved areas, or jurisdictions of Indian Tribes and Tribal organizations.\n##### (b) Ineligible entities\nAn entity shall be ineligible to receive a grant or enter into a cooperative agreement under this section if the entity or any affiliate, subsidiary, successor, or clinic thereof\u2014\n**(1)**\nperforms, induces, refers for, or counsels in favor of abortions; or\n**(2)**\nprovides financial support to any other entity that conducts any activity described in paragraph (1).\n##### (c) Use of funds\nA recipient of a grant or cooperative agreement under this section shall use the award funds as described in subsection (a), which may include purchasing or providing equipment necessary for carrying out at-home telehealth visits (such as remote physiologic devices and related services, including pulse oximeters, blood pressure cuffs, scales, and blood glucose monitors) to screen, monitor, and manage prenatal and postnatal care at home by means of telehealth visits and services for the purpose described in subsection (a).\n##### (d) Report to Congress\nNot later than September 30, 2029, the Secretary shall submit to Congress a report on activities supported through grants and cooperative agreements under this section, including\u2014\n**(1)**\na description of the activities conducted pursuant to such grants and cooperative agreements; and\n**(2)**\nan analysis of the effects of such grants and cooperative agreements on improving prenatal and postnatal care in areas and jurisdictions described in subsection (a).\n##### (e) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means an entity that provides prenatal care, labor care, birthing, or postpartum care services in a rural area, a frontier county, a medically underserved area, or the jurisdiction of an Indian Tribe or Tribal organization.\n**(2) Frontier county**\nThe term frontier county has the meaning given such term in section 1886(d)(3)(E)(iii)(III) of the Social Security Act ( 42 U.S.C. 1395ww(d)(3)(E)(iii)(III) ).\n**(3) Indian tribe; tribal organization**\nThe terms Indian Tribe and Tribal organization have the meanings given such terms in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(4) Medically underserved area**\nThe term medically underserved area means a health professional shortage area designated under section 332 of the Public Health Service Act ( 42 U.S.C. 254e ).\n**(5) Rural area**\nThe term rural area has the meaning given such term in section 330J(e) of the Public Health Service Act ( 42 U.S.C. 254c\u201315(e) ).\n**(6) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n##### (f) Authorization of appropriations\nTo carry out this section, there are authorized to be appropriated such sums as may be necessary for each of fiscal years 2025 through 2030.\nIII\nUnborn child support\n#### 301. Child support enforcement on behalf of unborn children\n##### (a) State plan amendment\nSection 454 of the Social Security Act ( 42 U.S.C. 654 ) is amended\u2014\n**(1)**\nin paragraph (4)(A)\u2014\n**(A)**\nin clause (i)\u2014\n**(i)**\nby inserting , including an unborn child, after child ; and\n**(ii)**\nby inserting and after the semicolon; and\n**(B)**\nin clause (ii), by inserting , including an unborn child after other child ;\n**(2)**\nin paragraph (33), by striking and after the semicolon;\n**(3)**\nin paragraph (34), by striking the period and inserting ; and ;\n**(4)**\nby inserting after paragraph (34), the following:\n(35) provide that the State will establish and enforce child support obligations of the biological father of an unborn child (and subsequent to the birth of the child) to the mother of such child provided that\u2014 (A) the mother has requested payment of such child support obligations; (B) the start date for such obligations may begin with the first month in which the child was conceived, as determined by a physician (and shall begin with that month if the mother so requests); (C) payments for such obligations may be retroactively collected or awarded, including in the case where paternity is established subsequent to the birth of the child; (D) the payment amount for such obligations shall be determined by a court, in consultation with the mother, taking into account the best interests of the mother and child; (E) any measure to establish the paternity of a child (born or unborn) shall not be required without the consent of the mother; and (F) any measure to establish the paternity of an unborn child shall not be taken if the measure poses any risk of harm to the child if unborn. ; and\n**(5)**\nby adding at the end the following: For purposes of paragraphs (4) and (35), the term unborn child means a member of the species homo sapiens, at any stage of development, who is carried in the womb. .\n##### (b) Limitation of waiver authority\nSection 1115 of the Social Security Act ( 42 U.S.C. 1315 ) is amended\u2014\n**(1)**\nin subsection (a), in the matter preceding paragraph (1), by striking In the case of and inserting Except as provided in subsection (c), in the case of ;\n**(2)**\nin subsection (b)(1), in the matter preceding subparagraph (A), by striking In the case of and inserting Except as provided in subsection (c), in the case of ; and\n**(3)**\nby striking subsection (c) and inserting the following:\n(c) No experimental, pilot, or demonstration project undertaken under subsection (a) to assist in promoting the objectives of part D of title IV, may permit modifications of paragraphs (4)(A)(ii) and (35) of section 454 to establish and enforce child support obligations of the biological father of an unborn child. For purposes of the preceding sentence, the term unborn child means a member of the species homo sapiens, at any stage of development, who is carried in the womb. .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date that is 2 years after the date of enactment of this Act and shall apply to payments under part D of title IV of the Social Security Act ( 42 U.S.C. 651 et seq. ) for calendar quarters beginning on or after such date.",
      "versionDate": "2025-05-07",
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
        "actionDate": "2026-01-23",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7236",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "In Good Standing Adoption Agencies Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-23",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "230",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Unborn Child Support Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-06",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1104",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Unborn Child Support Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-06",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1630",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "MOMS Act",
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
        "name": "Health",
        "updateDate": "2025-05-22T17:19:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-07",
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
          "measure-id": "id119hr3235",
          "measure-number": "3235",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-07",
          "originChamber": "HOUSE",
          "update-date": "2026-03-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3235v00",
            "update-date": "2026-03-05"
          },
          "action-date": "2025-05-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>More Opportunities for Moms to Succeed Act or the MOMS Act</strong></p><p>This bill establishes requirements to enable the collection of certain child support\u00a0during pregnancy, establishes grants for supportive services for women\u00a0that promote alternatives to abortions, and requires the Department of Health and Human Services (HHS) to establish a website with pregnancy resources other than those about abortions.</p><p>Specifically, the bill requires states to apply child support obligations to the time period during pregnancy under the Child Support Enforcement program. (The program enables states to receive federal matching funds for expenses related to child support enforcement activities and related services.)\u00a0Such child support applies at the request of the mother and may be applied retroactively. </p><p>Also, HHS must award grants to nonprofits to provide pregnant and postpartum women, and women parenting young children, with services or information on topics including health care (excluding abortions), child care, and employment assistance. It also requires\u00a0HHS to provide grants to health care providers in rural or medically underserved areas, as well as tribal areas,\u00a0to purchase equipment enabling telehealth visits for prenatal and postnatal care (e.g., monitoring devices).</p><p>Additionally, the bill requires HHS to establish a public website <em></em>to inform pregnant and postpartum women, and women parenting young children, of nearby services and resources on topics including health care, material or legal support, and alternatives to abortion. States must, as a condition of receiving certain federal funds,\u00a0provide\u00a0lists of nonprofit child placement agencies for potential inclusion on the site. </p>"
        },
        "title": "MOMS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3235.xml",
    "summary": {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>More Opportunities for Moms to Succeed Act or the MOMS Act</strong></p><p>This bill establishes requirements to enable the collection of certain child support\u00a0during pregnancy, establishes grants for supportive services for women\u00a0that promote alternatives to abortions, and requires the Department of Health and Human Services (HHS) to establish a website with pregnancy resources other than those about abortions.</p><p>Specifically, the bill requires states to apply child support obligations to the time period during pregnancy under the Child Support Enforcement program. (The program enables states to receive federal matching funds for expenses related to child support enforcement activities and related services.)\u00a0Such child support applies at the request of the mother and may be applied retroactively. </p><p>Also, HHS must award grants to nonprofits to provide pregnant and postpartum women, and women parenting young children, with services or information on topics including health care (excluding abortions), child care, and employment assistance. It also requires\u00a0HHS to provide grants to health care providers in rural or medically underserved areas, as well as tribal areas,\u00a0to purchase equipment enabling telehealth visits for prenatal and postnatal care (e.g., monitoring devices).</p><p>Additionally, the bill requires HHS to establish a public website <em></em>to inform pregnant and postpartum women, and women parenting young children, of nearby services and resources on topics including health care, material or legal support, and alternatives to abortion. States must, as a condition of receiving certain federal funds,\u00a0provide\u00a0lists of nonprofit child placement agencies for potential inclusion on the site. </p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119hr3235"
    },
    "title": "MOMS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>More Opportunities for Moms to Succeed Act or the MOMS Act</strong></p><p>This bill establishes requirements to enable the collection of certain child support\u00a0during pregnancy, establishes grants for supportive services for women\u00a0that promote alternatives to abortions, and requires the Department of Health and Human Services (HHS) to establish a website with pregnancy resources other than those about abortions.</p><p>Specifically, the bill requires states to apply child support obligations to the time period during pregnancy under the Child Support Enforcement program. (The program enables states to receive federal matching funds for expenses related to child support enforcement activities and related services.)\u00a0Such child support applies at the request of the mother and may be applied retroactively. </p><p>Also, HHS must award grants to nonprofits to provide pregnant and postpartum women, and women parenting young children, with services or information on topics including health care (excluding abortions), child care, and employment assistance. It also requires\u00a0HHS to provide grants to health care providers in rural or medically underserved areas, as well as tribal areas,\u00a0to purchase equipment enabling telehealth visits for prenatal and postnatal care (e.g., monitoring devices).</p><p>Additionally, the bill requires HHS to establish a public website <em></em>to inform pregnant and postpartum women, and women parenting young children, of nearby services and resources on topics including health care, material or legal support, and alternatives to abortion. States must, as a condition of receiving certain federal funds,\u00a0provide\u00a0lists of nonprofit child placement agencies for potential inclusion on the site. </p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119hr3235"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3235ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to provide more opportunities for mothers to succeed, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T06:12:52Z"
    },
    {
      "title": "MOMS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T06:09:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MOMS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T06:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "More Opportunities for Moms to Succeed Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T06:08:15Z"
    }
  ]
}
```
