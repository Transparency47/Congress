# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2576?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2576
- Title: Servicemembers and Veterans Empowerment and Support Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2576
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-04-28T08:06:27Z
- Update date including text: 2026-04-28T08:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-09 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-09 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2576",
    "number": "2576",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000597",
        "district": "1",
        "firstName": "Chellie",
        "fullName": "Rep. Pingree, Chellie [D-ME-1]",
        "lastName": "Pingree",
        "party": "D",
        "state": "ME"
      }
    ],
    "title": "Servicemembers and Veterans Empowerment and Support Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:27Z",
    "updateDateIncludingText": "2026-04-28T08:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-09T15:34:17Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "HI"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "FL"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "IL"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MI"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "IN"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "IN"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "CA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "LA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "KY"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2576ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2576\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Ms. Pingree (for herself, Ms. Tokuda , Mrs. Cherfilus-McCormick , Mrs. Ramirez , Mrs. Dingell , and Mr. Mrvan ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to expand health care and benefits from the Department of Veterans Affairs for military sexual trauma, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Servicemembers and Veterans Empowerment and Support Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Defining military sexual trauma\nSec. 101. Report on military sexual trauma in the digital age.\nTITLE II\u2014Disability compensation and claims processing\nSec. 201. Definition of military sexual trauma.\nSec. 202. Conforming changes relating to specialized teams to evaluate claims involving military sexual trauma.\nSec. 203. Evaluation of claims involving military sexual trauma.\nSec. 204. Choice of location of Department of Veterans Affairs medical examination for assessment of claims for compensation relating to disability resulting from military sexual trauma.\nSec. 205. Communications from the Department of Veterans Affairs to individuals who have experienced military sexual trauma.\nSec. 206. Study on training and processing relating to claims for disability compensation relating to military sexual trauma.\nSec. 207. Annual special focus review of claims for disability compensation for disabilities relating to military sexual trauma.\nSec. 208. Workgroup on medical examinations for claims for disability compensation for disabilities relating to military sexual trauma.\nTITLE III\u2014Access to health care\nSec. 301. Expansion of eligibility for counseling and treatment for military sexual trauma to include all former members of the reserve components of the armed forces.\nSec. 302. Connection to veterans health administration when a disability claim related to military sexual trauma is submitted to veterans benefits administration.\nSec. 303. Care relating to military sexual trauma for individuals who withdraw from or otherwise do not complete service at service academies.\nI\nDefining military sexual trauma\n#### 101. Report on military sexual trauma in the digital age\n##### (a) Report required\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on military sexual trauma in the digital age.\n##### (b) Requirements\nThe report required under subsection (a) shall include the following:\n**(1)**\nA comprehensive evaluation and assessment of current Department of Veterans Affairs statutes, regulations, and agency guidance relating to military sexual trauma for the purposes of access to health care under chapter 17 of title 38, United States Code, and compensation under chapter 11 of such title to identify\u2014\n**(A)**\ngaps in coverage for health care and compensation eligibility relating to military sexual trauma involving online or other technological communications; and\n**(B)**\nthe feasibility and advisability of expanding health care and compensation for trauma that is nonsexual in nature involving online or other technological communications.\n**(2)**\nRecommendations for revising statutes, regulations, and agency guidance in response to the evaluation and assessment under paragraph (1).\n##### (c) Consultation\n**(1) In general**\nIn carrying out subsection (a), the Secretary of Veterans Affairs shall consult veterans service organizations and such other stakeholders as the Secretary considers relevant and appropriate.\n**(2) Relation to FACA**\nChapter 10 of title 5, United States Code, shall not apply to paragraph (1).\n##### (d) Military sexual trauma defined\nIn this section, the term military sexual trauma \u2014\n**(1)**\nwith respect to eligibility for health care, has the meaning given such term in section 1720D(f) of title 38, United States Code, as added by section 301; and\n**(2)**\nwith respect to eligibility for compensation, has the meaning given such term in section 1166A(i) of title 38, United States Code, as added by section 203(a).\nII\nDisability compensation and claims processing\n#### 201. Definition of military sexual trauma\nIn this title, the term military sexual trauma has the meaning given such term in section 1166A(i) of title 38, United States Code, as added by section 203(a).\n#### 202. Conforming changes relating to specialized teams to evaluate claims involving military sexual trauma\nSection 1166 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(1), by striking for compensation for a covered mental health condition and inserting for compensation for a condition, which may include a covered mental health condition, ; and\n**(2)**\nby amending subsection (d) to read as follows:\n(d) Definitions In this section, the terms covered mental health condition and military sexual trauma have the meanings given those terms in section 1166A(i) of this title. .\n#### 203. Evaluation of claims involving military sexual trauma\n##### (a) In general\nSubchapter VI of chapter 11 of such title is amended by inserting after section 1166 the following new section:\n1166A. Evaluation of claims involving military sexual trauma (a) In general (1) In the case of any veteran who claims that a covered mental health condition based on military sexual trauma was incurred in or aggravated by active military, naval, air, or space service, the Secretary shall consider the following: (A) A diagnosis of such mental health condition by a mental health professional. (B) A link, established by medical evidence, between current symptoms and a military sexual trauma. (C) Credible corroborating evidence, in accordance with subsections (b) and (c), that the claimed military sexual trauma occurred. (2) The reasons for granting or denying service-connection in each case described in paragraph (1) shall be recorded in full. (b) Nonmilitary sources of evidence (1) For purposes of subsection (a), evidence from sources other than official records of the Department of Defense regarding the veteran's active military, naval, air, or space service may corroborate the veteran's account of the trauma. (2) Examples of evidence described in paragraph (1) include the following: (A) Records from law enforcement authorities, rape crisis centers, mental health counseling centers, hospitals, and physicians. (B) Pregnancy tests and tests for sexually transmitted diseases. (C) Statements from family members, roommates, other members of the Armed Forces or veterans, and clergy. (c) Evidence of behavior changes (1) For purposes of subsection (a), evidence of a behavior change following military sexual trauma is one type of relevant evidence that may be found in sources described in such subsection. (2) Examples of behavior changes that may be relevant evidence of military sexual trauma include the following: (A) A request for a transfer to another military duty assignment. (B) Deterioration in work performance. (C) Substance abuse or substance use disorder. (D) Episodes of depression, panic attacks, or anxiety without an identifiable cause. (E) Unexplained economic or social behavior changes. (d) Notice and opportunity To supply evidence The Secretary may not deny a claim of a veteran for compensation under this chapter for a covered mental health condition that is based on military sexual trauma without first\u2014 (1) advising the veteran that evidence described in subsections (b) and (c) may constitute credible corroborating evidence of the military sexual trauma; and (2) allowing the veteran an opportunity to furnish such corroborating evidence or advise the Secretary of potential sources of such evidence. (e) Review of evidence In reviewing a claim for compensation described in subsection (a)(1), for any evidence identified as part of such claim that is described in subsection (b) or (c), the Secretary shall submit such evidence to such medical or mental health professional as the Secretary considers appropriate, including clinical and counseling experts employed by the Department, to obtain an opinion as to whether the evidence indicates that a military sexual trauma occurred. (f) Point of contact The Secretary shall ensure that each document provided to a veteran relating to a claim for compensation described in subsection (a)(1) includes contact information for an appropriate point of contact with the Department. (g) Specialized teams The Secretary shall ensure that all claims for compensation described in subsection (a)(1) are reviewed and processed by a specialized team established under section 1166 of this title. (h) Rule of construction regarding application to nonsexual personal assault The Secretary shall not construe this section as supplanting the standard of proof or evidence required for claims for post-traumatic stress disorder based on nonsexual personal assault, which the Secretary shall continue to define in regulation. (i) Definitions In this section: (1) The term covered mental health condition means post-traumatic stress disorder, anxiety, depression, or other mental health diagnosis that the Secretary determines to be related to military sexual trauma and which may be service-connected under section 1110 of this title. (2) The term mental health professional means a provider in the field of mental health who meets the credential, licensure, education, and training requirements established by the Secretary. (3) The term military sexual trauma means, with respect to a veteran, a physical assault of a sexual nature, battery of a sexual nature, or sexual harassment that occurred while the veteran was serving in the active military, naval, air, or space service. .\n##### (b) Outreach\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall implement, with input from the veteran community, an informative outreach program for veterans regarding the standard of proof for evaluation of claims relating to military sexual trauma, including requirements for a medical examination and opinion.\n**(2) Targeted outreach**\nIn implementing the program under paragraph (1), the Secretary shall, to the extent practicable, target outreach to veterans who submitted a claim relating to military sexual trauma that was denied.\n##### (c) Clerical amendment\nThe table of sections at the beginning of chapter 11 of such title is amended by inserting after the item relating to section 1166 the following new item:\n1166A. Evaluation of claims involving military sexual trauma. .\n#### 204. Choice of location of Department of Veterans Affairs medical examination for assessment of claims for compensation relating to disability resulting from military sexual trauma\n##### (a) In general\nSection 1165 of title 38, United States Code, is amended\u2014\n**(1)**\nin the section heading, by inserting and location of medical examination after examiner ;\n**(2)**\nin subsection (a), by striking a physical assault of a sexual nature, battery of a sexual nature, or sexual harassment and inserting military sexual trauma (as defined in section 1166A(i) of this title) ;\n**(3)**\nby redesignating subsection (c) as subsection (d); and\n**(4)**\nby inserting after subsection (b) the following new subsection (c):\n(c) Choice of examination location The Secretary shall ensure that a veteran who requires a medical examination in support of a claim described in subsection (a) may request that the medical examination take place at a medical facility of the Department by a qualified employee of the Department rather than at a location designated by a contractor of the Department that performs such examinations on behalf of the Department. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 11 of such title is amended by striking the item relating to section 1165 and inserting the following new item:\n1165. Choice of sex of medical examiner and location of medical examination for certain disabilities. .\n#### 205. Communications from the Department of Veterans Affairs to individuals who have experienced military sexual trauma\n##### (a) Review workgroup\n**(1) In general**\nThe Secretary of Veterans Affairs shall establish a workgroup to review correspondence relating to military sexual trauma.\n**(2) Membership**\nThe workgroup established under paragraph (1) shall be composed of members who shall be appointed by the Secretary from among employees of the Department of Veterans Affairs who are experts in military sexual trauma and mental health, of whom\u2014\n**(A)**\none or more shall be appointed from among mental health providers of the Veterans Health Administration;\n**(B)**\none or more shall be appointed from among experts on sexual assault and sexual harassment of the Veterans Benefits Administration; and\n**(C)**\none or more shall be appointed from among experts on sexual assault and sexual harassment of the Board of Veterans\u2019 Appeals.\n**(3) Duties**\nThe workgroup established under paragraph (1) shall\u2014\n**(A)**\nreview standard correspondence, which may include templates for notices under sections 5103, 5104, 5104B, and 7104 of title 38, United States Code, from the Department to individuals who have experienced military sexual trauma for sensitivity; and\n**(B)**\nensure that the correspondence\u2014\n**(i)**\ntreats such individuals with dignity and respect; and\n**(ii)**\ndoes not re-traumatize such individuals.\n**(4) Individual who has experienced military sexual trauma defined**\nIn this subsection, the term individual who has experienced military sexual trauma means\u2014\n**(A)**\nan individual who has filed a claim for compensation under chapter 11 of title 38, United States Code, relating to military sexual trauma;\n**(B)**\na veteran who has been awarded compensation under such chapter relating to military sexual trauma; or\n**(C)**\na member of the Armed Forces (including a member of the National Guard or Reserves), a former member of the Armed Forces, or a veteran who is receiving care from the Department relating to military sexual trauma.\n##### (b) Contents of certain written communications to individuals who have experienced military sexual trauma\n**(1) Notice to claimants of required information and evidence**\nSection 5103 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(c) Written communications to individuals who have experienced military sexual trauma (1) The Secretary shall ensure that any written communication under this section from the Department to an individual who has experienced military sexual trauma includes each of the following: (A) Contact information for each of the following: (i) The military sexual trauma coordinator of the Veterans Benefits Administration. (ii) The military sexual trauma coordinator of the Veterans Health Administration. (iii) The Veterans Crisis Line. (iv) The facility of the Veterans Health Administration closest to where the individual resides. (v) The Vet Center closest to where the individual resides. (B) Information on the eligibility of the individual for services provided through the Vet Center described in subparagraph (A)(v). (2) In this subsection: (A) The term individual who has experienced military sexual trauma means\u2014 (i) an individual who has filed a claim for compensation under chapter 11 of this title relating to military sexual trauma; (ii) a veteran who has been awarded compensation under such chapter relating to military sexual trauma; or (iii) a member of the Armed Forces (including a member of the National Guard or Reserves), a former member of the Armed Forces, or a veteran who is receiving care from the Department relating to military sexual trauma. (B) The term military sexual trauma has the meaning given that term in section 1166A(i) of this title. (C) The term Vet Center has the meaning given that term in section 1712A(h) of this title. (D) The term Veterans Crisis Line means the toll-free hotline for veterans established under section 1720F(h) of this title. .\n**(2) Decisions and notices of decisions**\nSection 5104 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(e) (1) The Secretary shall ensure that any written communication under this section from the Department to an individual who has experienced military sexual trauma includes each of the following: (A) Contact information for each of the following: (i) The military sexual trauma coordinator of the Veterans Health Administration. (ii) The Veterans Crisis Line. (iii) The facility of the Veterans Health Administration closest to where the individual resides. (iv) The Vet Center closest to where the individual resides. (B) Information on the eligibility of the individual for services provided through the Vet Center described in subparagraph (A)(iv). (2) The Secretary shall ensure that any written communication under this section from the Department to an individual who has experienced military sexual trauma that includes notification of an award of compensation under chapter 11 of this title relating to military sexual trauma includes\u2014 (A) the contact information described in paragraph (1); and (B) the contact information for the military sexual trauma coordinator of the Veterans Benefits Administration. (3) In this subsection: (A) The term individual who has experienced military sexual trauma means\u2014 (i) an individual who has filed a claim for compensation under chapter 11 of this title relating to military sexual trauma; (ii) a veteran who has been awarded compensation under such chapter relating to military sexual trauma; or (iii) a member of the Armed Forces (including a member of the National Guard or Reserves), a former member of the Armed Forces, or a veteran who is receiving care from the Department relating to military sexual trauma. (B) The term military sexual trauma has the meaning given that term in section 1166A(i) of this title. (C) The term Vet Center has the meaning given that term in section 1712A(h) of this title. (D) The term Veterans Crisis Line means the toll-free hotline for veterans established under section 1720F(h) of this title. .\n**(3) Higher-level review by the agency of original jurisdiction**\nSection 5104B of title 38, United States Code, is amended by adding at the end the following new subsection:\n(f) Written communications to individuals who have experienced military sexual trauma (1) The Secretary shall ensure that any written communication under this section from the Department to an individual who has experienced military sexual trauma includes each of the following: (A) Contact information for each of the following: (i) The military sexual trauma coordinator of the Veterans Health Administration. (ii) The Veterans Crisis Line. (iii) The facility of the Veterans Health Administration closest to where the individual resides. (iv) The Vet Center closest to where the individual resides. (B) Information on the eligibility of the individual for services provided through the Vet Center described in subparagraph (A)(iv). (2) The Secretary shall ensure that any written communication under this section from the Department to an individual who has experienced military sexual trauma that includes notification of an award of compensation under chapter 11 of this title relating to military sexual trauma includes\u2014 (A) the contact information described in paragraph (1); and (B) the contact information for the military sexual trauma coordinator of the Veterans Benefits Administration. (3) In this subsection: (A) The term individual who has experienced military sexual trauma means\u2014 (i) an individual who has filed a claim for compensation under chapter 11 of this title relating to military sexual trauma; (ii) a veteran who has been awarded compensation under such chapter relating to military sexual trauma; or (iii) a member of the Armed Forces (including a member of the National Guard or Reserves), a former member of the Armed Forces, or a veteran who is receiving care from the Department relating to military sexual trauma. (B) The term military sexual trauma has the meaning given that term in section 1166A(i) of this title. (C) The term Vet Center has the meaning given that term in section 1712A(h) of this title. (D) The term Veterans Crisis Line means the toll-free hotline for veterans established under section 1720F(h) of this title. .\n**(4) Board of Veterans\u2019 Appeals**\nSection 7104 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(g) (1) The Secretary shall ensure that any written communication under this section from the Department to an individual who has experienced military sexual trauma include each of the following: (A) Contact information for each of the following: (i) The military sexual trauma coordinator of the Veterans Health Administration. (ii) The Veterans Crisis Line. (iii) The facility of the Veterans Health Administration closest to where the individual resides. (iv) The Vet Center closest to where the individual resides. (B) Information on the eligibility of the individual for services provided through the Vet Center described in subparagraph (A)(iv). (2) The Secretary shall ensure that any written communication under this section from the Department to an individual who has experienced military sexual trauma that includes notification of an award of compensation under chapter 11 of this title relating to military sexual trauma includes\u2014 (A) the contact information described in paragraph (1); and (B) the contact information for the military sexual trauma coordinator of the Veterans Benefits Administration. (3) In this subsection: (A) The term individual who has experienced military sexual trauma means\u2014 (i) an individual who has filed a claim for compensation under chapter 11 of this title relating to military sexual trauma; (ii) a veteran who has been awarded compensation under such chapter relating to military sexual trauma; or (iii) a member of the Armed Forces (including a member of the National Guard or Reserves), a former member of the Armed Forces, or a veteran who is receiving care from the Department relating to military sexual trauma. (B) The term military sexual trauma has the meaning given that term in section 1166A(i) of this title. (C) The term Vet Center has the meaning given that term in section 1712A(h) of this title. (D) The term Veterans Crisis Line means the toll-free hotline for veterans established under section 1720F(h) of this title. .\n#### 206. Study on training and processing relating to claims for disability compensation relating to military sexual trauma\n##### (a) Study required\nThe Secretary of Veterans Affairs shall conduct a study on\u2014\n**(1)**\nthe quality of training provided to personnel of the Department of Veterans Affairs who review claims for disability compensation under chapter 11 of title 38, United States Code, for disabilities relating to military sexual trauma; and\n**(2)**\nthe quality of the procedures of the Department for reviewing the accuracy of the processing of such claims.\n##### (b) Elements\nThe study required by subsection (a) shall include the following:\n**(1)**\nWith respect to the quality of training described in paragraph (1) of such subsection:\n**(A)**\nWhether the Department ensures personnel complete such training on time.\n**(B)**\nWhether the training has resulted in improvements to the processing of claims described in such subsection and issue-based accuracy.\n**(C)**\nSuch recommendations as the Secretary may have for improving the training.\n**(2)**\nWith respect to the quality of procedures described in paragraph (2) of such subsection:\n**(A)**\nWhether the procedures of the Department for reviewing the accuracy of the processing of claims described in such subsection comport with generally accepted statistical methodologies to ensure reasonable accuracy of such reviews.\n**(B)**\nWhether such procedures adequately include mechanisms to correct errors found in such reviews.\n**(C)**\nA summary of quality assurance reviews and reports conducted as part of such procedures.\n**(D)**\nSuch recommendations as the Secretary may have for improving such procedures.\n##### (c) Report required\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to the Committee on Veterans' Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report detailing the findings of the Secretary with respect to the study conducted under subsection (a).\n#### 207. Annual special focus review of claims for disability compensation for disabilities relating to military sexual trauma\n##### (a) Annual special focus review\n**(1) In general**\nEach year, the Under Secretary for Benefits of the Department of Veterans Affairs shall conduct a special focus review on the accuracy of the processing of claims for disability compensation under chapter 11 of title 38, United States Code, for disabilities relating to military sexual trauma.\n**(2) Elements**\nEach review conducted under paragraph (1) shall include a review of the following:\n**(A)**\nA statistically significant, nationally representative sample of all claims for benefits under the laws administered by the Secretary of Veterans Affairs relating to military sexual trauma filed during the fiscal year preceding the fiscal year in which the report is submitted.\n**(B)**\nThe accuracy of each decision made with respect to each claim described in subparagraph (A).\n**(C)**\nThe types of benefit entitlement errors found, disaggregated by category.\n**(D)**\nTrends from year to year.\n**(E)**\nTraining completion rates for personnel of the Department who process claims described in paragraph (1).\n##### (b) Reprocessing of claims\nIf the Under Secretary finds, pursuant to a special focus review conducted under subsection (a)(1), that an error was made with respect to the entitlement of a veteran to a benefit under the laws administered by the Secretary, the Secretary shall return the relevant claim of the veteran to the appropriate office of the Department for reprocessing to ensure that the veteran receives an accurate decision with respect to the claim.\n##### (c) Report\nSection 5501(b) of the Johnny Isakson and David P. Roe, M.D. Veterans Health Care and Benefits Improvement Act of 2020 ( Public Law 116\u2013315 ; 134 Stat. 5048) is amended\u2014\n**(1)**\nin paragraph (1), by striking through 2027 and inserting until the date described in section 207(d) of the Servicemembers and Veterans Empowerment and Support Act of 2025 ; and\n**(2)**\nin paragraph (2), by adding at the end the following new subparagraph:\n(I) The findings of the most recent special focus review conducted under subsection (a)(1) of section 207 of the Servicemembers and Veterans Empowerment and Support Act of 2025 , including\u2014 (i) the elements under subsection (a)(2) of such section; (ii) the number of claims returned for reprocessing under subsection (b) of such section; and (iii) the number of claims described in clause (ii) for which the decision relating to service-connection or entitlement to compensation changed as a result of reprocessing the claim. .\n##### (d) Sunset\nOn the date that the Under Secretary determines, pursuant to special focus reviews conducted under paragraph (1) of subsection (a), that the accuracy rates under paragraph (2)(B) of such subsection have been 95 percent or greater for five consecutive years, subsection (a)(1) shall cease to be in effect.\n#### 208. Workgroup on medical examinations for claims for disability compensation for disabilities relating to military sexual trauma\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall establish a workgroup on medical examinations for claims for disability compensation under chapter 11 of title 38, United States Code, for disabilities relating to military sexual trauma (in this section referred to as the workgroup ).\n##### (b) Membership\nThe workgroup shall be composed of the following:\n**(1)**\nStaff of the operations center for military sexual trauma of the Department of Veterans Affairs who have experience reviewing the quality of medical examinations in support of claims for disability compensation under chapter 11 of title 38, United States Code.\n**(2)**\nStaff of the Medical Disability Examination Office of the Department.\n**(3)**\nVeterans service officers who have experience with claims described in subsection (a).\n**(4)**\nMedical examiners who have experience with such claims.\n**(5)**\nStaff of the Veterans Experience Office of the Department.\n**(6)**\nSuch other individuals as the Secretary considers appropriate.\n##### (c) Duties\nNot later than 180 days after the date of the enactment of this Act, the Workgroup shall\u2014\n**(1)**\nreview the quality of medical examinations described in subsection (a);\n**(2)**\nreview the feasibility of minimizing re-examinations for conditions relating to military sexual trauma; and\n**(3)**\nsubmit to the Under Secretary for Benefits of the Department and the Secretary recommendations on how to\u2014\n**(A)**\neliminate re-traumatization of individuals who file claims described in subsection (a); and\n**(B)**\nreduce the overdevelopment of such claims.\n##### (d) Report\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to Congress a report that includes the following:\n**(1)**\nThe views of the workgroup on efforts by the Department to eliminate re-traumatization of individuals who file claims described in subsection (a).\n**(2)**\nLegislative proposals to improve the experience of such individuals in pursuing such claims.\n**(3)**\nThe recommendations submitted under subsection (c)(3).\n**(4)**\nThe plan of the Under Secretary for Benefits of the Department and the Secretary to implement such recommendations.\n##### (e) Review and implementation\nNot later than one year after the date of the enactment of this Act, the Under Secretary for Benefits of the Department and the Secretary shall\u2014\n**(1)**\nreview the recommendations submitted under subsection (c)(3); and\n**(2)**\nimplement the recommendations that, as determined by the Under Secretary and the Secretary, would improve the claims process for individuals who file claims described in subsection (a).\nIII\nAccess to health care\n#### 301. Expansion of eligibility for counseling and treatment for military sexual trauma to include all former members of the reserve components of the armed forces\nSection 1720D of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking a physical assault and all that follows through the period at the end and inserting military sexual trauma. ; and\n**(B)**\nin paragraph (2)(A), by striking was suffered and all that follows through the period at the end and inserting resulted from military sexual trauma. ; and\n**(2)**\nby striking subsections (f) and (g) and inserting the following new subsection (f):\n(f) In this section: (1) The term former member of the Armed Forces means a person who served on active duty, active duty for training, or inactive duty training, and who was discharged or released therefrom under any condition that is not\u2014 (A) a discharge by court-martial, unless the Secretary determines an exception to the bar to benefits applies; or (B) a discharge subject to a bar to benefits under section 5303 of this title. (2) The term military sexual trauma means, with respect to a member of the Armed Forces or former member of the Armed Forces, a physical assault of a sexual nature, battery of a sexual nature, or sexual harassment which occurred while the member or former member was serving on duty, regardless of duty status or line of duty determination (as that term is used in section 12323 of title 10). (3) The term sexual harassment means unsolicited verbal or physical contact of a sexual nature which is threatening in character. .\n#### 302. Connection to veterans health administration when a disability claim related to military sexual trauma is submitted to veterans benefits administration\n##### (a) In general\nNot later than 14 days after the date on which a veteran submits a claim for disability compensation to the Veterans Benefits Administration for a disability related to military sexual trauma, the Secretary of Veterans Affairs shall send a communication to the veteran with the following information:\n**(1)**\nThe contact information for the nearest military sexual trauma coordinator for the veteran at the Veterans Benefits Administration and a description of the assistance such coordinator can provide.\n**(2)**\nThe contact information for the nearest military sexual trauma coordinator for the veteran at the Veterans Health Administration and a description of the assistance such coordinator can provide.\n**(3)**\nThe types of services that individuals who have experienced military sexual trauma are eligible to receive from the Department of Veterans Affairs, including the nearest locations, including the nearest Vet Center, and the contact information for such services.\n**(4)**\nThe contact information for the Veterans Crisis Line established under section 1720F(h) of title 38, United States Code.\n**(5)**\nSuch other information on services, care, or resources for military sexual trauma as the Secretary determines appropriate.\n##### (b) Definitions\nIn this section:\n**(1) Military sexual trauma**\nThe term military sexual trauma \u2014\n**(A)**\nwith respect to eligibility for health care, has the meaning given such term in section 1720D(f) of title 38, United States Code, as added by section 301; and\n**(B)**\nwith respect to eligibility for compensation, has the meaning given such term in section 1166A(i) of title 38, United States Code, as added by section 203(a).\n**(2) Vet center**\nThe term Vet Center has the meaning given that term in section 1712A(h) of title 38, United States Code.\n#### 303. Care relating to military sexual trauma for individuals who withdraw from or otherwise do not complete service at service academies\n##### (a) In general\nThe Secretary of Veterans Affairs, in coordination with the Secretary of Defense, the Secretary of Homeland Security, and the Secretary of Transportation, shall ensure that each individual who withdraws from, or otherwise does not complete service at, a service academy is provided\u2014\n**(1)**\ninformation on the potential eligibility of such individual for care and counseling relating to military sexual trauma provided through the Department of Veterans Affairs; and\n**(2)**\nthe option to receive copies of\u2014\n**(A)**\nthe individual's service treatment records or military personnel records that document military sexual trauma;\n**(B)**\nreporting forms of the Department of Defense, the Department of Homeland Security, or the Department of Transportation on sexual assault or sexual harassment for which the individual was the victim; and\n**(C)**\nany investigative reports into military sexual trauma that occurred during the individual's service in the Armed Forces and for which the individual was the victim.\n##### (b) Definitions\nIn this section:\n**(1) Military sexual trauma**\nThe term military sexual trauma \u2014\n**(A)**\nwith respect to eligibility for health care, has the meaning given such term in section 1720D(f) of title 38, United States Code, as added by section 301; and\n**(B)**\nwith respect to eligibility for compensation, has the meaning given such term in section 1166A(i) of title 38, United States Code, as added by section 203(a).\n**(2) Service academy**\nThe term service academy means any of the following:\n**(A)**\nThe United States Military Academy.\n**(B)**\nThe United States Naval Academy.\n**(C)**\nThe United States Air Force Academy.\n**(D)**\nThe United Stated Coast Guard Academy.\n**(E)**\nThe United States Merchant Marine Academy.",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-07-30",
        "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably."
      },
      "number": "1245",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Servicemembers and Veterans Empowerment and Support Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Assault and harassment offenses",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Evidence and witnesses",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-08-07T17:56:47Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-08-07T17:56:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T14:04:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119hr2576",
          "measure-number": "2576",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-01",
          "originChamber": "HOUSE",
          "update-date": "2026-01-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2576v00",
            "update-date": "2026-01-15"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Servicemembers and Veterans Empowerment and Support Act of 2025</strong></p><p>This bill modifies and implements policies and procedures related to Department of Veterans Affairs (VA) health care and benefits for veterans who have experienced military sexual trauma (MST), which is generally defined as physical assault of a sexual nature, battery of a sexual nature, or sexual harassment that occurred while the veteran was serving in the military.</p><p>In the case of any veteran who claims that a covered mental health condition (e.g., post-traumatic stress disorder) based on MST was incurred or aggravated by active service, the VA must consider (1) a diagnosis of the condition by a mental health professional, (2) a medically proven link between current symptoms and MST, and (3) credible corroborating evidence that MST occurred.</p><p>The VA may not deny a veteran's claim of compensation for a covered mental health condition based on MST without first (1) advising the veteran that nonmilitary evidence and behavioral evidence may constitute credible corroborating evidence, and (2) allowing the veteran an opportunity to furnish the corroborating evidence or advise the VA of potential sources of such evidence.</p><p>The Veterans Benefits Administration must conduct an annual special focus review on the accuracy of the processing of claims for disability compensation for disabilities relating to MST.</p><p>Additionally, the bill (1) expands eligibility for MST counseling and treatment to former members of the reserve components regardless of duty status, and (2) requires various outreach by the VA to inform potentially eligible individuals about MST care.</p>"
        },
        "title": "Servicemembers and Veterans Empowerment and Support Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2576.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Servicemembers and Veterans Empowerment and Support Act of 2025</strong></p><p>This bill modifies and implements policies and procedures related to Department of Veterans Affairs (VA) health care and benefits for veterans who have experienced military sexual trauma (MST), which is generally defined as physical assault of a sexual nature, battery of a sexual nature, or sexual harassment that occurred while the veteran was serving in the military.</p><p>In the case of any veteran who claims that a covered mental health condition (e.g., post-traumatic stress disorder) based on MST was incurred or aggravated by active service, the VA must consider (1) a diagnosis of the condition by a mental health professional, (2) a medically proven link between current symptoms and MST, and (3) credible corroborating evidence that MST occurred.</p><p>The VA may not deny a veteran's claim of compensation for a covered mental health condition based on MST without first (1) advising the veteran that nonmilitary evidence and behavioral evidence may constitute credible corroborating evidence, and (2) allowing the veteran an opportunity to furnish the corroborating evidence or advise the VA of potential sources of such evidence.</p><p>The Veterans Benefits Administration must conduct an annual special focus review on the accuracy of the processing of claims for disability compensation for disabilities relating to MST.</p><p>Additionally, the bill (1) expands eligibility for MST counseling and treatment to former members of the reserve components regardless of duty status, and (2) requires various outreach by the VA to inform potentially eligible individuals about MST care.</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119hr2576"
    },
    "title": "Servicemembers and Veterans Empowerment and Support Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Servicemembers and Veterans Empowerment and Support Act of 2025</strong></p><p>This bill modifies and implements policies and procedures related to Department of Veterans Affairs (VA) health care and benefits for veterans who have experienced military sexual trauma (MST), which is generally defined as physical assault of a sexual nature, battery of a sexual nature, or sexual harassment that occurred while the veteran was serving in the military.</p><p>In the case of any veteran who claims that a covered mental health condition (e.g., post-traumatic stress disorder) based on MST was incurred or aggravated by active service, the VA must consider (1) a diagnosis of the condition by a mental health professional, (2) a medically proven link between current symptoms and MST, and (3) credible corroborating evidence that MST occurred.</p><p>The VA may not deny a veteran's claim of compensation for a covered mental health condition based on MST without first (1) advising the veteran that nonmilitary evidence and behavioral evidence may constitute credible corroborating evidence, and (2) allowing the veteran an opportunity to furnish the corroborating evidence or advise the VA of potential sources of such evidence.</p><p>The Veterans Benefits Administration must conduct an annual special focus review on the accuracy of the processing of claims for disability compensation for disabilities relating to MST.</p><p>Additionally, the bill (1) expands eligibility for MST counseling and treatment to former members of the reserve components regardless of duty status, and (2) requires various outreach by the VA to inform potentially eligible individuals about MST care.</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119hr2576"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2576ih.xml"
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
      "title": "Servicemembers and Veterans Empowerment and Support Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Servicemembers and Veterans Empowerment and Support Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to expand health care and benefits from the Department of Veterans Affairs for military sexual trauma, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:26Z"
    }
  ]
}
```
