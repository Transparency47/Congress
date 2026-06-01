# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2479?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2479
- Title: Homes for Young Adults Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2479
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-03-16T19:08:06Z
- Update date including text: 2026-03-16T19:08:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2479",
    "number": "2479",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Homes for Young Adults Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-16T19:08:06Z",
    "updateDateIncludingText": "2026-03-16T19:08:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2479ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2479\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mrs. Watson Coleman (for herself and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the United States Housing Act of 1937 to provide housing assistance for youth and young adults who are unstably housed.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Homes for Young Adults Act of 2025 .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Congressional findings.\nSec. 3. Definitions.\nSec. 4. Entitlement program for housing choice vouchers for youth.\nSec. 5. Promoting self-sufficiency.\nSec. 6. Enforcement of housing quality standards.\nSec. 7. Screening of applicants.\nSec. 8. Access to HUD programs for persons with limited English proficiency.\nSec. 9. Authorization of appropriations.\n#### 2. Congressional findings\nThe Congress finds that\u2014\n**(1)**\neach year an estimated 4.2 million youth and young adults experience homelessness in the United States;\n**(2)**\nhomelessness amongst youth and young adults is disproportionately represented among Black, Indigenous, other youth of color, and LGBTQ+ communities;\n**(3)**\nwhile there are effective programs that assist homeless youth and young adults, access to current resources are restricted due to a variety of systemic obstacles for homeless youth and young adults, forcing this population into congregate shelters, further perpetuating cycles of poverty and instability;\n**(4)**\nadequately removing barriers to housing assistance can\u2014\n**(A)**\nreduce crowding, housing instability, and homelessness;\n**(B)**\nreduce poverty;\n**(C)**\nimprove outcomes for children;\n**(D)**\nimprove overall adult well-being, reducing healthcare costs; and\n**(E)**\ncontribute to the prevention of homelessness;\n**(5)**\nthe housing choice voucher (HCV) program only reaches about a quarter of eligible households due to limited funding, yet extensive and inhibitive eligibility requirements presently make HCVs inaccessible to youth and young adults;\n**(6)**\nthe average wait time for youth and young adults from a coordinated entry assessment to being housed is between 132 and 140 days, depending on the program; and\n**(7)**\nFederal agencies, particularly the Department of Housing and Urban Development, the Department of Education, and the Department of Health and Human Services, should cooperate more fully to address the prevention and end of youth homelessness.\n#### 3. Definitions\nFor purposes of this Act, the following definitions shall apply:\n**(1) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(2) Youth and young adults**\nThe term youths and young adults means individuals who are\u2014\n**(A)**\n18 years old or older but are not older than 30 years old; or\n**(B)**\nemancipated minors under applicable State law.\n#### 4. Entitlement program for housing choice vouchers for youth\n##### (a) Entitlement\nDuring fiscal year 2027 and each fiscal year thereafter, any household that consists of or includes any youth or young adult and that is otherwise eligible for tenant-based rental assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) shall be entitled to such rental assistance in accordance with this section during such period the family remains so eligible.\n##### (b) Funding\nFor fiscal year 2027 and each fiscal year thereafter, there is appropriated out of any money in the Treasury not otherwise appropriated the amount necessary\u2014\n**(1)**\nto provide assistance under section 8(o) of the United States Housing Act of 1937 in accordance with the entitlement under subsection (a) of this section for each qualified household in the amount determined under subsection 8(o); and\n**(2)**\nto provide administrative fees under sections 8(q) and 23(h)(1) of such Act, as modified pursuant to this Act, in connection with each voucher for assistance provided pursuant to subsection (a) of this section.\n##### (c) Administering agencies\n**(1) Regional consortia**\nThe Secretary shall encourage and provide for public housing agencies to form regional consortia to administer the program for rental assistance under this section with respect to geographical areas.\n**(2) PHA designation**\nThe Secretary shall designate a public housing agency to administer assistance under this section in any area where no existing public housing agency has jurisdiction or where no agency with jurisdiction is adequately administering such assistance, subject to public comment and after consultation with States, public housing agencies, local government, Indian tribes, and tribally designated housing agencies.\n##### (d) Support services\n**(1) Requirements**\nEach public housing agency administering rental assistance provided pursuant to this section shall ensure that\u2014\n**(A)**\nsupport services described in paragraph (2) are made available to each youth and young adult provided such rental assistance by the administering agency, which may be accessed by such youth or young adult at any time; and\n**(B)**\neach such youth and young adult is provided clear information on how to access such services and the purposes, benefits, and any limitations involved with accessing such services.\n**(2) Included services**\nThe support services described in this paragraph are as follows:\n**(A)**\nAny services otherwise made available by the public housing agency to families provided rental assistance under section 8(o) of the United States Housing Act of 1937.\n**(B)**\nServices as the Secretary shall provide relating to housing navigation, job-skill training, assistance for pursuing higher education, relevant legal and tenant protection services, assistance in applying for other federally funded programs, and safety planning and services appropriate to address potential vulnerabilities and safety concerns of youths and young adults, including migrant youths and young adults.\n**(3) Availability**\nThis subsection may not be construed to require any youth or young adult provided rental assistance under this section to access or use such services.\n##### (e) Housing choice\nThe Secretary shall take such actions as necessary to ensure that the choice of a dwelling unit to be rented using assistance provided pursuant to this section shall be at the sole discretion of the assisted household and may be based upon such standards and factors as such household considers appropriate, including\u2014\n**(1)**\ngeographical considerations, including those affected by family or cultural factors;\n**(2)**\ncost of living;\n**(3)**\naccess to grocery stores, healthcare, transportation, or any need;\n**(4)**\npreference for individual or shared housing; and\n**(5)**\nany other considerations of importance to the household.\n##### (f) Mediation; appeal\nThe Secretary shall require each public housing agency administering rental assistance made available pursuant to this section to make available to households assisted under this section\u2014\n**(1)**\nan ombudsman to mediate any issues, including claims of discrimination, arising between the assisted household and the landlord of the dwelling unit rented by such household using such assistance; and\n**(2)**\nan appeal process for such assisted households to challenge any adverse decisions under the mediation process under paragraph (1).\n##### (g) Immigration status\nEligibility for assistance made available pursuant to this section may not be limited based on citizenship, immigration, or migratory status in any manner that is inconsistent with eligibility requirements otherwise applicable to assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) for households who are not youths or young adults.\n##### (h) Privacy\nThe Secretary shall take such actions as may be necessary to protect the privacy and confidentiality of households assisted pursuant to this section.\n##### (i) Studies and reports\nIn conducting any study or issuing any report relating to carrying out this Act, including the studies and reports under subsections (a)(4)(D) and (b), the Secretary shall ensure the appointment or inclusion of homeless youth and young adults.\n#### 5. Promoting self-sufficiency\nFor fiscal year 2027 and each fiscal year there after, the Secretary may\u2014\n**(1)**\nincrease the amount provided as administrative fees under section 23(h)(1) of the United States Housing Act of 1937 ( 42 U.S.C. 1437u(h)(1) ) for any public housing agency that meets such standards as the Secretary shall establish to assist and encourage\u2014\n**(A)**\ncoordinating the use of assistance under section 8(o) of such Act, including assistance pursuant to section 4 of this Act, for participation of youths and young adults, including youths and young adults who are single, parenting, or aging out of foster care or other youth-serving systems, in the family self-sufficiency program under such section 23; and\n**(B)**\nvoluntary participation of landlords in such self-sufficiency program to house youths and young adults holding vouchers for assistance under section 8(o) without discrimination based on credit history, income, criminal or legal history, or migratory status; and\n**(2)**\nprovide incentive awards under section 23(i) for public housing agencies who willingly participate in coordinating the use of assistance under section 8(o) for participation of youths and young adults in the family self-sufficiency program.\n#### 6. Enforcement of housing quality standards\nThe Secretary of Housing and Urban Development shall issue any regulations necessary to carry out subparagraph (G) of section 8(o)(8) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(8)(G) ) not later than the expiration of the 12-month period beginning upon the date of the enactment of this Act. Such regulations shall take effect not later than the expiration of the 90-day period beginning upon such issuance.\n#### 7. Screening of applicants\nSubparagraph (B) of section 8(o)(6) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(6)(B) ) is amended by inserting after the period at the end of the second sentence the following: A public housing agency\u2019s elective screening shall be limited to criteria that are directly related to an applicant\u2019s ability to fulfill the obligations of an assisted lease and shall consider mitigating circumstances related to such applicant, including discriminations against income, credit history, parental status, marital status, migratory status, or age. Any applicant or participant determined to be ineligible for admission or continued participation to the program shall be notified of the basis for such determination and provide, within a reasonable time after the determination, an opportunity for an informal hearing on such determination at which mitigating circumstances, including remedial conduct subsequent to the notice, shall be considered. .\n#### 8. Access to HUD programs for persons with limited English proficiency\n##### (a) HUD responsibilities\nTo allow the Department of Housing and Urban Development to better serve persons with limited proficiency in the English language by providing technical assistance to recipients of Federal funds, the Secretary of Housing and Urban Development shall take the following actions:\n**(1) Task Force**\nWithin 90 days after the enactment of this Act, convene a task force comprised of appropriate industry groups, recipients of funds from the Department of Housing and Urban Development (in this section referred to as the Department ), community-based organizations that serve individuals with limited English proficiency, civil rights groups, and stakeholders, which shall identify a list of vital documents, including Department and certain property and other documents, to be competently translated to improve access to federally conducted and federally assisted programs and activities for individuals with limited English proficiency. The task force shall meet not less frequently than twice per year.\n**(2) Translations**\nWithin 6 months after identification of documents pursuant to paragraph (1), produce translations of the documents identified in all necessary languages and make such translations available as part of the library of forms available on the website of the Department and as part of the clearinghouse developed pursuant to paragraph (4).\n**(3) Plan**\nDevelop and carry out a plan that includes providing resources of the Department to assist recipients of the Federal funds to improve access to programs and activities for individuals with limited English proficiency, which plan shall include the elements described in paragraph (4).\n**(4) Housing information resource center**\nDevelop and maintain a housing information resource center to facilitate the provision of language services by providers of housing services to individuals with limited English proficiency. Information provided by such center shall be made available in printed form and through the internet. The resources provided by the center shall include the following:\n**(A) Translation of written materials**\nThe center may provide, directly or through contract, vital documents from competent translation services for providers of housing services.\n**(B) Toll-free customer service telephone number**\nThe center shall provide a 24-hour toll-free interpretation service telephone line, by which recipients of funds of the Department and individuals with limited English proficiency may\u2014\n**(i)**\nobtain information about federally conducted or federally assisted housing programs of the Department;\n**(ii)**\nobtain assistance with applying for or accessing such housing programs and understanding Federal notices written in English; and\n**(iii)**\ncommunicate with housing providers and learn how to access additional language services.\nThe toll-free telephone service provided pursuant to this subparagraph shall supplement resources in the community identified by the plan developed pursuant to paragraph (3).\n**(C) Document clearinghouse**\nThe center shall collect and evaluate for accuracy or develop, and make available, templates and documents that are necessary for consumers, relevant industry representatives, and other stakeholders of the Department, to access, make educated decisions, and communicate effectively about their housing, including\u2014\n**(i)**\nadministrative and property documents;\n**(ii)**\nlegally binding documents;\n**(iii)**\nconsumer education and outreach materials;\n**(iv)**\ndocuments regarding rights and responsibilities of any party; and\n**(v)**\nremedies available to consumers.\n**(D) Study of language assistance programs**\nThe center shall conduct a study that evaluates best-practice models for all programs of the Department that promote language assistance and strategies to improve language services for individuals with limited English proficiency. Not later than 18 months after the date of the enactment of this Act, the center shall submit a report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate, which shall provide recommendations for implementation, specific to programs of the Department, and information and templates that could be made available to all recipients of grants from the Department.\n**(E) Cultural and linguistic competence materials**\nThe center shall provide information relating to culturally and linguistically competent housing services for populations with limited English proficiency.\n##### (b) Report\nNot later than the expiration of the 6-month period beginning on the date of the enactment of this Act, and annually thereafter, the Secretary of Housing and Urban Development shall submit a report regarding its compliance with the requirements under subsection (a) to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate.\n#### 9. Authorization of appropriations\nThere is authorized to be appropriated for fiscal year 2027 and each fiscal year thereafter such sums as may be necessary to carry out this Act.",
      "versionDate": "2025-03-27",
      "versionType": "Introduced in House"
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
            "name": "Community life and organization",
            "updateDate": "2026-03-16T19:07:36Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-16T19:08:05Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-03-16T19:07:59Z"
          },
          {
            "name": "Foreign language and bilingual programs",
            "updateDate": "2026-03-16T19:07:54Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-16T19:07:44Z"
          },
          {
            "name": "Homelessness and emergency shelter",
            "updateDate": "2026-03-16T19:07:21Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2026-03-16T19:07:15Z"
          },
          {
            "name": "Landlord and tenant",
            "updateDate": "2026-03-16T19:07:31Z"
          },
          {
            "name": "Public housing",
            "updateDate": "2026-03-16T19:07:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-04-07T13:48:09Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2479ih.xml"
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
      "title": "Homes for Young Adults Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Homes for Young Adults Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the United States Housing Act of 1937 to provide housing assistance for youth and young adults who are unstably housed.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:58Z"
    }
  ]
}
```
