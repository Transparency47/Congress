# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3130?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3130
- Title: FACTS Act
- Congress: 119
- Bill type: HR
- Bill number: 3130
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-02-25T18:05:23Z
- Update date including text: 2026-02-25T18:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3130",
    "number": "3130",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
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
    "title": "FACTS Act",
    "type": "HR",
    "updateDate": "2026-02-25T18:05:23Z",
    "updateDateIncludingText": "2026-02-25T18:05:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:03:35Z",
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
          "date": "2025-05-01T13:03:30Z",
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
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "VA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "CO"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NJ"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "WA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MN"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "IA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "OR"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3130ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3130\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Ms. Bonamici (for herself, Mr. Wittman , Mr. Neguse , and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish education partnership programs between public schools and public health agencies to prevent the misuse and overdose of synthetic opioids by youth, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Fentanyl Awareness for Children and Teens in Schools Act or the FACTS Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title; table of contents.\nSec.\u20022.\u2002Purposes.\nSec.\u20023.\u2002Definitions.\nTitle I\u2014Partnership grants for local and State educational agencies\nSec.\u2002101.\u2002Synthetic opioid misuse and overdose education, awareness, and prevention pilot program.\nSec.\u2002102.\u2002Authorization of appropriations; reservation.\nTitle II\u2014Establishment of an interagency task force\nSec.\u2002201.\u2002Interagency Task Force on Preventing Synthetic Opioid Misuse and Overdose Among Youth.\nSec.\u2002202.\u2002Rule of construction.\nTitle III\u2014Amendments to the Elementary and Secondary Education Act of 1965\nSec.\u2002301.\u2002Professional development for school personnel.\nSec.\u2002302.\u2002Amendments to local educational agency plans.\nSec.\u2002303.\u2002Amendments to State educational agency plans.\nTitle IV\u2014Amendments to Department of Education data collection\nSec.\u2002401.\u2002National Center for Education Statistics School Crime and Safety Data.\nTitle V\u2014School-based health centers and reporting\nSec.\u2002501.\u2002Naloxone in school-based health centers.\nSec.\u2002502.\u2002Amendments to the Monitoring the Future survey.\nSec.\u2002503.\u2002Youth Risk Behavior Survey.\nSec.\u2002504.\u2002Evaluation of the effectiveness and reach of the State Unintentional Drug Overdose Reporting System.\n#### 2. Purposes\nThe purposes of this Act are to\u2014\n**(1)**\nestablish education partnership programs between public schools and public health agencies to prevent the misuse of and overdose with synthetic opioids by youth;\n**(2)**\ndevelop a whole-of-government approach to identify and disseminate best practices in education and prevention regarding the misuse of and overdose with synthetic opioids by youth;\n**(3)**\nincrease opportunities for employees of elementary and secondary schools receiving Federal funds to receive professional development on the dangers of the misuse of and overdose with synthetic opioids by youth; and\n**(4)**\nimprove the availability and usability of data regarding the proliferation of synthetic opioids.\n#### 3. Definitions\nIn this Act:\n**(1) Classified school employee**\nThe term classified school employee means an employee of a State or of any political subdivision of a State, or an employee of a nonprofit organization, who works in any grade from prekindergarten through high school in any of the following occupational specialties:\n**(A)**\nParaprofessional, including paraeducator services.\n**(B)**\nClerical and administrative services.\n**(C)**\nTransportation services.\n**(D)**\nFood and nutrition services.\n**(E)**\nCustodial and maintenance services.\n**(F)**\nSecurity services.\n**(G)**\nHealth and student services.\n**(H)**\nTechnical services.\n**(I)**\nSkilled trades.\n**(2) ESEA terms**\nThe terms educational service agency , evidence-based , local educational agency , parent , secondary school , and State have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(3) Secretary**\nThe term Secretary , unless otherwise specified, refers to the Secretary of Health and Human Services.\n**(4) Synthetic opioids**\nThe term synthetic opioids means substances, including fentanyl and any substituted derivative of fentanyl, that\u2014\n**(A)**\nare synthesized in a laboratory; and\n**(B)**\nact on the same targets in the brain as natural opioids to produce analgesic effects.\nI\nPartnership grants for local and State educational agencies\n#### 101. Synthetic opioid misuse and overdose education, awareness, and prevention pilot program\n##### (a) In general\nThe Secretary, in consultation with the Secretary of Education, shall administer a pilot program to eligible partnerships to provide financial assistance for the prevention of, treatment of, and recovery from, disorders stemming from the misuse of synthetic opioids by secondary school-aged children.\n##### (b) Definitions\nIn this section:\n**(1) Eligible partnership**\nThe term eligible partnership means a partnership of\u2014\n**(A)**\na local educational agency, a State educational agency, a Bureau of Indian Education school, an educational service agency, or a consortium of entities that includes a State, local, territorial, or Tribal education agency or organization seeking to establish or expand a program to reduce the misuse of synthetic opioids and establish recovery programs or services for children, adolescents, and young adults; and\n**(B)**\na State, local, territorial, or Tribal health agency or organization, a qualified nongovernmental entity with appropriate expertise in providing substance use disorder education, prevention, and treatment services or programs for secondary school-aged children, as defined by the Secretary, or a consortium of entities that includes a State, local, territorial, or Tribal health agency or organization.\n**(2) Recovery program**\nThe term recovery program means a program\u2014\n**(A)**\nto help secondary school-aged children who are recovering from substance use disorders to initiate, stabilize, and maintain healthy and productive lives in the community; and\n**(B)**\nthat includes peer-to-peer support delivered by individuals with lived experience in recovery, and communal activities to build recovery skills and supportive social networks.\n##### (c) Pilot program authorized\nThe Secretary, in consultation with the Secretary of Education, shall award 3-year grants, on a competitive basis, to up to 25 eligible partnerships to enable such partnerships to prevent the misuse of synthetic opioids by secondary school-aged children.\n##### (d) Use of funds\nAn eligible partnership that receives a grant under this section shall use amounts made available through such grant for evidence-based activities, which may include any of the following:\n**(1)**\nDeveloping evidence-based materials for teachers to use as a component of classroom instruction, and sharing these materials with parents and families.\n**(2)**\nDesigning evidence-based professional development for teachers, school leaders, specialized instructional support personnel, classified school employees, and other school staff members.\n**(3)**\nDeveloping in- and out-of-school workshops and accessible and tailored content for students, families, and teachers to attain information about the misuse of synthetic opioids.\n**(4)**\nCreating efficient and effective multimedia communication campaigns, including through social media, to maximize outreach efforts to students, parents, and families.\n**(5)**\nAwarding contracts to nonprofit organizations\u2014\n**(A)**\nspecializing in substance misuse prevention education efforts;\n**(B)**\nwith demonstrated success in reaching, engaging, and supporting local and State educational agencies, Bureau of Indian Education schools, and other schools; and\n**(C)**\nwith expertise in designing recovery programs for synthetic opioid misuse and overdose prevention.\n**(6)**\nEstablishing peer-to-peer counseling programs for students at secondary schools to support the work of school-based mental health professionals in preventing the misuse of synthetic opioids.\n**(7)**\nOther purposes as may be specified by the Secretary.\n##### (e) Applications and assurances\nTo seek a grant under this section, an eligible partnership shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may reasonably require, which shall include the following:\n**(1)**\nA description, containing qualitative and quantitative information, of the existing need for such a grant in the area proposed to be served through the grant, which description may include information on\u2014\n**(A)**\nthe rate of misuse of and overdoses attributable to synthetic opioids among youth under the age of 21;\n**(B)**\nif available, data indicating the trend of synthetic opioid misuse and overdoses among youth under the age of 21 over the past 5 years; and\n**(C)**\nthe availability of synthetic opioids.\n**(2)**\nA description of the initiatives, activities, or programs the eligible partnership will fund through the grant, including how such initiatives, activities, or programs will reduce the misuse of and overdoses attributable to synthetic opioids in the area proposed to be served through the grant.\n**(3)**\nA description of how the eligible partnership will establish a local interagency agreement to ensure adequate and effective collaboration among entities in the partnership to carry out the initiatives, activities, or programs described in paragraph (2).\n**(4)**\nA description of how the initiatives, activities, or programs described in paragraph (2) will be linguistically appropriate and culturally responsive for students and families served by the eligible partnership.\n**(5)**\nA description of how the initiatives, activities, or programs described in paragraph (2) will support students and families served by the eligible partnership in reversing individual and community-wide effects of synthetic opioid misuse and overdoses.\n**(6)**\nAn assurance that\u2014\n**(A)**\npersons providing services through the grant awarded to the eligible partnership will be adequately trained to provide such services; and\n**(B)**\nteachers, school leaders, administrators, specialized instructional support personnel, representatives of local Indian Tribes or Tribal organizations as appropriate, other school personnel, and parents or guardians of students participating in services funded through a grant under this section will be engaged in the design and implementation of the initiatives, activities, or programs described in paragraph (2).\n**(7)**\nA description of how the eligible partnership will support and integrate existing school, local educational agency, and State initiatives, activities, or programs with the initiatives, activities, or programs described in paragraph (2) to provide synthetic opioid misuse and overdose prevention services for students, as appropriate.\n##### (f) Priority\nIn awarding grants under this section, the Secretary shall give priority to eligible entities that have a higher rate of youth illicit drug use, including the use of fentanyl and other synthetic opioids.\n##### (g) Distribution of awards\nSubject to subsection (f), the Secretary shall ensure that grants awarded under this section are equitably distributed among the geographical regions of the United States and among Tribal, urban, suburban, and rural populations.\n##### (h) Supplement, not supplant\nAny services provided through initiatives, activities, or programs carried out under this section shall supplement, not supplant, other Federal or State funds available to carry out activities described in this title.\n##### (i) Accountability\n**(1) Review**\nIn accordance with section 102(b), the Secretary shall regularly review the initiatives, activities, or programs of eligible partnerships receiving a grant under this section to ensure that such partnerships are using the grant for the purposes for which it was provided.\n**(2) Notification of reports**\nNot later than 90 days after the Secretary awards grants for the first year of the program under this section, the Secretary shall\u2014\n**(A)**\nrequire eligible partnerships receiving a grant under this section to submit reports, on an annual basis, detailing the initiatives, activities, or programs funded through such grant; and\n**(B)**\nnotify such eligible partnerships of such reporting requirement.\n**(3) Timeline of reports**\nEach eligible partnership receiving a grant under this section shall submit the first report described in paragraph (2) to the Secretary not later than one year after receiving a grant under this section.\n**(4) Content of reports**\nEach report required under paragraph (2) shall include, at minimum, the following information:\n**(A)**\nThe effectiveness of the grant awarded under this section in reducing synthetic opioid misuse and overdose among the students served by the eligible partnership.\n**(B)**\nDetails regarding the initiatives, activities, or programs funded through the grant and further details about any subgrants awarded by the eligible partnership to help carry out planned initiatives, activities, or programs.\n**(C)**\nTo the extent practicable, narrative statements from teachers, school leaders, specialized instructional support personnel, or other relevant stakeholders describing the process of implementing the initiatives, activities, or programs developed through the grant.\n**(D)**\nIf applicable, any challenges faced by the eligible partnership in reaching or engaging parents, students, teachers, school leaders, specialized instructional support personnel, and other relevant stakeholders with the initiatives, activities, or programs developed through the grant.\n**(E)**\nAny other information the Secretary may require.\n**(5) Submission of reports**\nNot later than 180 days after receiving reports from eligible partnerships receiving a grant under this section, the Secretary shall submit such reports and a brief overview of the data and outcomes described in such reports to the Committees on Education and Workforce and Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate.\n##### (j) Publication of programs\nEach eligible partnership receiving a grant under this section shall\u2014\n**(1)**\npost on the eligible partnership\u2019s website the initiatives, activities, and programs supported through the grant; and\n**(2)**\ndisseminate to families served by the eligible partnership, in widely accessible formats, content from and information about such initiatives, activities, and programs.\n##### (k) Sharing of best practices\nThe Secretary shall\u2014\n**(1)**\ncollect content from and information about all initiatives, activities, and programs developed by each eligible partnerships through a grant under this section; and\n**(2)**\nin conjunction with the Secretary of Education, make such content and information publicly available and widely accessible.\n#### 102. Authorization of appropriations; reservation\n##### (a) Authorization\nThere is authorized to be appropriated to carry out section 101 such sums as may be necessary for each of fiscal years 2026 through 2028.\n##### (b) Reservation for evaluation and technical assistance\nThe Secretary may reserve not more than 5 percent of the funds appropriated under subsection (a) for any fiscal year to\u2014\n**(1)**\nconduct a rigorous, independent evaluation of the initiatives, activities, or programs funded under section 101;\n**(2)**\nprovide technical assistance and share best practices with respect to initiatives, activities, or programs that are developed by eligible partnerships through grants under section 101; and\n**(3)**\nprovide technical assistance to eligible partnerships applying for a grant under section 101, through the use of webinars, direct emails, mailed outreach, and other strategies designed to reach underserved eligible partnerships, including eligible partnerships located in rural and remote areas.\nII\nEstablishment of an interagency task force\n#### 201. Interagency Task Force on Preventing Synthetic Opioid Misuse and Overdose Among Youth\n##### (a) Establishment\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish a task force, to be known as the Interagency Task Force on Preventing Opioid Misuse and Overdose Among Youth (in this section referred to as the Task Force ) to identify, evaluate, and make recommendations to coordinate and improve Federal responses to synthetic opioid overdose and misuse in youth.\n##### (b) Membership\nThe membership of the Task Force shall include\u2014\n**(1)**\nthe officials serving under paragraphs (1) through (9) of subsection (c); and\n**(2)**\nthe members serving under paragraphs (10), (11), and (12) of subsection (c), to be appointed by the Secretary.\n##### (c) Composition\nThe Task Force shall be composed of at least 12, but not more than 17, members as follows:\n**(1)**\nThe Secretary of Health and Human Services, who shall serve as Chair of the Task Force.\n**(2)**\nThe Secretary of Education.\n**(3)**\nThe Assistant Secretary for Mental Health and Substance Use.\n**(4)**\nThe Assistant Secretary for Children and Families.\n**(5)**\nThe Director of the Centers for Disease Control and Prevention.\n**(6)**\nThe Assistant Secretary for Elementary and Secondary Education.\n**(7)**\nThe Director of the Agency for Healthcare Research and Quality.\n**(8)**\nThe Surgeon General of the United States.\n**(9)**\nThe Director of the National Institute of Mental Health of the National Institutes of Health.\n**(10)**\nAt least two, and not more than three, non-Federal representatives who are parents of youth who died from an overdose of fentanyl or another synthetic opioid.\n**(11)**\nAt least one, and not more than two, non-Federal representatives of one or more nationally-recognized nonprofit organizations working to raise awareness about and prevent misuse of synthetic opioids by youth.\n**(12)**\nSuch other Federal or non-Federal representatives as determined by the Secretary.\n##### (d) Duties\nThe Task Force shall\u2014\n**(1)**\ndevelop and regularly update a report that identifies, analyzes, and evaluates the state of Federal, State, and local programs to address synthetic opioid misuse and overdose in youth, and identifies best practices including\u2014\n**(A)**\na set of evidence-based, evidence-informed, and promising practices with respect to\u2014\n**(i)**\nprevention strategies for youth at risk of fentanyl and synthetic opioids misuse and overdose;\n**(ii)**\nthe identification, screening, diagnosis, intervention, and treatment of youth affected by synthetic opioid misuse;\n**(iii)**\nthe expeditious referral to, and implementation of, practices and supports that prevent and mitigate the effects of synthetic opioid misuse and overdose in youth; and\n**(iv)**\ncommunity-based or multigenerational practices that support youth and families affected by synthetic opioid misuse and overdose; and\n**(B)**\nFederal and State programs and activities to prevent, screen, diagnose, intervene, and treat synthetic opioid misuse and overdose in youth; and\n**(2)**\ndevelop and regularly update a national strategy for\u2014\n**(A)**\nyouth synthetic opioid misuse and overdose prevention, taking into consideration the findings of the reports under paragraph (1); and\n**(B)**\nhow the Task Force and Federal departments and agencies represented on the Task Force will prioritize options for, and implement a coordinated approach to, addressing synthetic opioid misuse and overdose.\n#### 202. Rule of construction\nNothing in this title shall be construed to limit or otherwise alter the authority of any of the Federal agencies referred to in section 201(c) to carry out programs to reduce synthetic opioid overdose and misuse under other provisions of law.\nIII\nAmendments to the Elementary and Secondary Education Act of 1965\n#### 301. Professional development for school personnel\nSection 2101(c)(4)(B) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6611(c)(4)(B) ) is amended\u2014\n**(1)**\nby redesignating clauses (xvi) through (xxi) as clauses (xvii) through (xxii), respectively; and\n**(2)**\nby inserting after clause (xv) the following:\n(xvi) Providing training for all school personnel, including teachers, principals, other school leaders, specialized instructional support personnel, paraprofessionals, counselors, and mental health professionals, regarding how to address and prevent the misuse of synthetic opioids, including fentanyl or any substituted derivative of fentanyl, among students. .\n#### 302. Amendments to local educational agency plans\nSection 1112(b) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6312(b) ) is amended\u2014\n**(1)**\nin paragraph (12)(B), by striking and at the end;\n**(2)**\nby redesignating paragraph (13) as paragraph (14); and\n**(3)**\nby inserting after paragraph (12) the following:\n(13) how the local educational agency will engage teachers and school leaders, in consultation with parents, local educational agency administrators, public health officials, paraprofessionals, specialized instructional support personnel, school counselors, and school psychologists, to address and prevent the misuse of synthetic opioids, including fentanyl or any substituted derivative of fentanyl, among students; and .\n#### 303. Amendments to State educational agency plans\nSection 1111(g)(1) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(g)(1) ) is amended\u2014\n**(1)**\nin subparagraph (F), by striking and at the end;\n**(2)**\nby redesignating subparagraph (G) as subparagraph (H); and\n**(3)**\nby inserting after subparagraph (F) the following:\n(G) how the State educational agency will provide support to local educational agencies receiving assistance under this part in addressing and preventing the misuse of synthetic opioids, including fentanyl or any substituted derivative of fentanyl, among students; and .\nIV\nAmendments to Department of Education data collection\n#### 401. National Center for Education Statistics School Crime and Safety Data\nSection 153(a)(1)(H) of the Education Sciences Reform Act of 2002 ( 20 U.S.C. 9543(a)(1)(H) ) is amended\u2014\n**(1)**\nin clause (ii), by striking and at the end;\n**(2)**\nin clause (iii), by inserting and at the end; and\n**(3)**\nby adding at the end the following:\n(iv) access to synthetic opioids, including fentanyl, on school premises, and the effects of such substances on school safety and student health and well-being; .\nV\nSchool-based health centers and reporting\n#### 501. Naloxone in school-based health centers\nSection 399Z\u20131(f)(1)(A) of the Public Health Service Act ( 42 U.S.C. 280h\u20135(f)(1)(A) ) is amended\u2014\n**(1)**\nin clause (iv), by striking and at the end and inserting or ; and\n**(2)**\nby adding at the end the following:\n(v) the purchase of naloxone to reverse the effects of opioid overdose, and the establishment of other programs to address and prevent the misuse of synthetic opioids, including fentanyl or any substituted derivative of fentanyl; and .\n#### 502. Amendments to the Monitoring the Future survey\nBeginning on January 1, 2026, the Director of the National Institute on Drug Abuse, in collaboration with the Secretary and the Director of the National Institutes of Health, shall require the survey funded by the National Institute on Drug Abuse and titled Monitoring the Future to include\u2014\n**(1)**\nindicators to measure the use of, perception of harm of, and access to counterfeit or synthetic opioids among youth; and\n**(2)**\nwhere applicable, indicators to measure the extent to which respondents are aware of the counterfeit or synthetic nature of any opioids used or encountered by such respondents.\n#### 503. Youth Risk Behavior Survey\nBeginning on January 1, 2026, the Director of the Centers for Disease Control and Prevention shall require the data collection survey for the Youth Risk Behavior Surveillance System to include\u2014\n**(1)**\nquestions related to the use of, awareness regarding, and exposure to counterfeit or synthetic opioids, including fentanyl; and\n**(2)**\nwhere applicable, indicators to measure the extent to which respondents are aware of the counterfeit or synthetic nature of any opioids used or encountered by such respondents.\n#### 504. Evaluation of the effectiveness and reach of the State Unintentional Drug Overdose Reporting System\n##### (a) Evaluation\nBeginning on or after January 1, 2026, the Director of the Centers for Disease Control and Prevention shall conduct an evaluation determining the effectiveness of the State Unintentional Drug Overdose Reporting System in collecting and reporting data regarding specific synthetic opioids causing or contributing to overdose and death among secondary school-aged children.\n##### (b) Reports\nNot later than 180 days after concluding such evaluation, the Director of the Centers for Disease Control and Prevention shall develop and submit to the Committees on Energy and Commerce and Education and Workforce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate the findings of the evaluation and, if applicable, recommendations to improve the quality and availability of data described in subsection (a).\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated such sums as may be necessary for fiscal year 2026 to carry out this section.",
      "versionDate": "2025-05-01",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-21T11:04:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-01",
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
          "measure-id": "id119hr3130",
          "measure-number": "3130",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-01",
          "originChamber": "HOUSE",
          "update-date": "2026-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3130v00",
            "update-date": "2026-02-25"
          },
          "action-date": "2025-05-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fentanyl Awareness for Children and Teens in Schools Act or the FACTS Act</strong></p><p>This bill establishes grant programs and requires strategies and studies to address the\u00a0misuse of synthetic opioids (i.e., laboratory-derived substances\u00a0such as\u00a0fentanyl and its derivatives) among youth.</p><p>The bill requires the Department of Health and Human Services (HHS) to award grants to partnerships between educational and health organizations for prevention, treatment, and recovery efforts related to the use of synthetic opioids by middle and high school-aged children. It also allows school-based health centers\u00a0to use existing HHS grants to purchase naloxone to reverse the effects of opioid overdoses and to establish programs to address misuse of synthetic\u00a0opioids. \u00a0</p><p>Also, the bill authorizes state educational agencies to use certain Department of Education (ED) grant funds to provide training to school personnel on addressing students\u2019 misuse of synthetic opioids. State and local educational agencies must also address such misuse in their educational plans in order to qualify for certain ED grants.</p><p>Finally, the bill (1) establishes an interagency taskforce to coordinate federal efforts to address synthetic opioid misuse among youth, (2)\u00a0requires an evaluation of the State Unintentional Drug Overdose Reporting System\u2019s effectiveness in identifying the specific synthetic opioids causing youth overdoses, (3) expands the data reported by the National Center for Education Statistics to include information about the use of synthetic opioids in schools, and (4) requires two recurring\u00a0HHS surveys to include questions on youth exposure to synthetic opioids. \u00a0 \u00a0</p>"
        },
        "title": "FACTS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3130.xml",
    "summary": {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fentanyl Awareness for Children and Teens in Schools Act or the FACTS Act</strong></p><p>This bill establishes grant programs and requires strategies and studies to address the\u00a0misuse of synthetic opioids (i.e., laboratory-derived substances\u00a0such as\u00a0fentanyl and its derivatives) among youth.</p><p>The bill requires the Department of Health and Human Services (HHS) to award grants to partnerships between educational and health organizations for prevention, treatment, and recovery efforts related to the use of synthetic opioids by middle and high school-aged children. It also allows school-based health centers\u00a0to use existing HHS grants to purchase naloxone to reverse the effects of opioid overdoses and to establish programs to address misuse of synthetic\u00a0opioids. \u00a0</p><p>Also, the bill authorizes state educational agencies to use certain Department of Education (ED) grant funds to provide training to school personnel on addressing students\u2019 misuse of synthetic opioids. State and local educational agencies must also address such misuse in their educational plans in order to qualify for certain ED grants.</p><p>Finally, the bill (1) establishes an interagency taskforce to coordinate federal efforts to address synthetic opioid misuse among youth, (2)\u00a0requires an evaluation of the State Unintentional Drug Overdose Reporting System\u2019s effectiveness in identifying the specific synthetic opioids causing youth overdoses, (3) expands the data reported by the National Center for Education Statistics to include information about the use of synthetic opioids in schools, and (4) requires two recurring\u00a0HHS surveys to include questions on youth exposure to synthetic opioids. \u00a0 \u00a0</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119hr3130"
    },
    "title": "FACTS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fentanyl Awareness for Children and Teens in Schools Act or the FACTS Act</strong></p><p>This bill establishes grant programs and requires strategies and studies to address the\u00a0misuse of synthetic opioids (i.e., laboratory-derived substances\u00a0such as\u00a0fentanyl and its derivatives) among youth.</p><p>The bill requires the Department of Health and Human Services (HHS) to award grants to partnerships between educational and health organizations for prevention, treatment, and recovery efforts related to the use of synthetic opioids by middle and high school-aged children. It also allows school-based health centers\u00a0to use existing HHS grants to purchase naloxone to reverse the effects of opioid overdoses and to establish programs to address misuse of synthetic\u00a0opioids. \u00a0</p><p>Also, the bill authorizes state educational agencies to use certain Department of Education (ED) grant funds to provide training to school personnel on addressing students\u2019 misuse of synthetic opioids. State and local educational agencies must also address such misuse in their educational plans in order to qualify for certain ED grants.</p><p>Finally, the bill (1) establishes an interagency taskforce to coordinate federal efforts to address synthetic opioid misuse among youth, (2)\u00a0requires an evaluation of the State Unintentional Drug Overdose Reporting System\u2019s effectiveness in identifying the specific synthetic opioids causing youth overdoses, (3) expands the data reported by the National Center for Education Statistics to include information about the use of synthetic opioids in schools, and (4) requires two recurring\u00a0HHS surveys to include questions on youth exposure to synthetic opioids. \u00a0 \u00a0</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119hr3130"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3130ih.xml"
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
      "title": "FACTS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FACTS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fentanyl Awareness for Children and Teens in Schools Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish education partnership programs between public schools and public health agencies to prevent the misuse and overdose of synthetic opioids by youth, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:18:22Z"
    }
  ]
}
```
