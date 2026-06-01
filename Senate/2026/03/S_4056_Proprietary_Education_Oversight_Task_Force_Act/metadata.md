# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4056?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4056
- Title: Proprietary Education Oversight Task Force Act
- Congress: 119
- Bill type: S
- Bill number: 4056
- Origin chamber: Senate
- Introduced date: 2026-03-11
- Update date: 2026-04-01T15:47:44Z
- Update date including text: 2026-04-01T15:47:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-11: Introduced in Senate
- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1011-1015)
- Latest action: 2026-03-11: Introduced in Senate

## Actions

- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1011-1015)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-11",
    "latestAction": {
      "actionDate": "2026-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4056",
    "number": "4056",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
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
    "title": "Proprietary Education Oversight Task Force Act",
    "type": "S",
    "updateDate": "2026-04-01T15:47:44Z",
    "updateDateIncludingText": "2026-04-01T15:47:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1011-1015)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-11",
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
          "date": "2026-03-11T18:25:50Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "CT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "OR"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
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
      "sponsorshipDate": "2026-03-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4056is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4056\nIN THE SENATE OF THE UNITED STATES\nMarch 11, 2026 Mr. Durbin (for himself, Mr. Blumenthal , Mr. Merkley , Mr. Schiff , Ms. Smith , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish the Proprietary Education Interagency Oversight Committee and to facilitate the disclosure and reporting of information regarding complaints and investigations related to proprietary institutions of higher education eligible to receive Federal education assistance.\n#### 1. Short title\nThis Act may be cited as the Proprietary Education Oversight Task Force Act .\n#### 2. Definitions\nIn this Act:\n**(1) Accrediting agency**\nThe term accrediting agency means a private educational association that acts as a reliable authority on the quality of education or training provided by an institution of higher education and is recognized by the Secretary under section 496 of the Higher Education Act of 1965 ( 20 U.S.C. 1099b ).\n**(2) Department**\nUnless otherwise expressly provided, the term Department means the Department of Education.\n**(3) Executive officer**\nThe term executive officer , with respect to a proprietary institution of higher education that is a publicly traded corporation, means\u2014\n**(A)**\nthe president of the corporation;\n**(B)**\na vice president of the corporation who is in charge of a principal business unit, division, or function of the corporation, such as sales, administration, or finance; or\n**(C)**\nany other officer or person who performs a policy-making function for the corporation, including an executive officer of a subsidiary of the corporation if the officer performs a policy making function for the corporation.\n**(4) Federal education assistance**\nThe term Federal education assistance when used with respect to a proprietary institution of higher education, means Federal funds that are disbursed or delivered by the Department, the Department of Veterans Affairs, or the Department of Defense to, or on behalf of, a student to be used for tuition, fees, instruction, or any other component of the student\u2019s cost of attendance (as defined in section 472 of the Higher Education Act of 1965 ( 20 U.S.C. 1087ll )) to attend the institution.\n**(5) Institutional debt**\nThe term institutional debt means any debt owed by a student or the parent of a student to an institution of higher education, including\u2014\n**(A)**\ndebt owed through a private loan program, income-share agreement, or other financing product operated by the institution;\n**(B)**\ndebt owed from a return of student assistance made, insured, or guaranteed under title IV of the Higher Education Act 1965 ( 20 U.S.C. 1070 et seq. ) to the Department; and\n**(C)**\ndebt owed from the student\u2019s nonpayment of institutional charges or fees.\n**(6) Private education loan**\nThe term private education loan \u2014\n**(A)**\nmeans a loan provided by a private educational lender (as defined in section 140(a) of the Truth in Lending Act ( 15 U.S.C. 1650(a) )) that\u2014\n**(i)**\nis not made, insured, or guaranteed under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. );\n**(ii)**\nis issued expressly for postsecondary educational expenses to a borrower, regardless of whether the loan is provided through the educational institution that the subject student attends or directly to the borrower from the private educational lender (as so defined); and\n**(iii)**\nis not made, insured, or guaranteed under title VII or title VIII of the Public Health Service Act ( 42 U.S.C. 292 et seq. and 296 et seq.); and\n**(B)**\ndoes not include an extension of credit under an open-end consumer credit plan, a reverse mortgage transaction, a residential mortgage transaction, or any other loan that is secured by real property or a dwelling.\n**(7) Proprietary institution of higher education**\nThe term proprietary institution of higher education has the meaning given the term in section 102(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1002(b) ).\n**(8) Recruiting and marketing activities**\n**(A) In general**\nExcept as provided in subparagraph (B), the term recruiting and marketing activities means activities that include any of the following:\n**(i)**\nAdvertising and promotional activities, including paid announcements in newspapers, magazines, radio, television, billboards, electronic media, naming rights, or any other public medium of communication, including paying for displays or promotions at job fairs, military installations, or college recruiting events, that are made directly or indirectly to a student, a prospective student, the public, an accrediting agency, a State agency, or to the Secretary by a proprietary institution of higher education, one of its representatives, or any person with whom the institution has an agreement to provide educational programs, advertising, or admissions services.\n**(ii)**\nMisleading statement, misrepresentation, and substantial misrepresentation (as defined in section 668.71(c) of title 34, Code of Federal Regulations, or any successor regulation).\n**(iii)**\nEfforts to identify and attract prospective students, either directly or through a contractor or other third party, including contact concerning a prospective student\u2019s potential enrollment or application for a grant, a loan, or work assistance under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. ) or participation in preadmission or advising activities, including soliciting an individual to provide contact information to a proprietary institution of higher education, including through websites established for that purpose and funds paid to third parties for that purpose.\n**(iv)**\nOther activities as the Secretary may prescribe, including paying for promotion or sponsorship of education or military-related associations.\n**(B) Exceptions**\nAny activity that is required as a condition of the receipt of funds by an institution of higher education under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. ), is specifically authorized under that title, or is otherwise specified by the Secretary, is not a recruiting and marketing activity under subparagraph (A).\n**(9) Secretary**\nUnless otherwise expressly provided, the term Secretary means the Secretary of Education.\n**(10) State approval agency**\nThe term State approval agency means any State agency that determines whether an institution of higher education is legally authorized within the State to provide a program of education beyond secondary education.\n**(11) Veterans service organization**\nThe term veterans service organization means an organization that is\u2014\n**(A)**\nrecognized by the Secretary of Veterans Affairs for the representation of veterans under section 5902 of title 38, United States Code;\n**(B)**\ncongressionally chartered under title 36, United States Code, and serves or represents veterans;\n**(C)**\nrecognized by the Secretary of Veteran Affairs under section 14.628 of title 38, Code of Federal Regulations (or a successor regulation), as a national organization, State organization, tribal organization, or regional or local organization; or\n**(D)**\nan organization that has a record of demonstrating expertise in, assists in, or serves the interests of veterans in education.\n#### 3. Establishment of Proprietary Education Interagency Oversight Committee\n##### (a) Establishment\nThere is established the Proprietary Education Interagency Oversight Committee (referred to in this Act as the Committee ) to be composed of the head (or the designee of the head who is designated under subsection (d)) of each of the following:\n**(1)**\nThe Department.\n**(2)**\nThe Consumer Financial Protection Bureau.\n**(3)**\nThe Department of Justice.\n**(4)**\nThe Securities and Exchange Commission.\n**(5)**\nThe Department of Defense.\n**(6)**\nThe Department of Veterans Affairs.\n**(7)**\nThe Federal Trade Commission.\n**(8)**\nThe Department of Labor.\n**(9)**\nThe Internal Revenue Service.\n**(10)**\nAt the discretion of the President, any other relevant Federal agency.\n##### (b) Purposes\nThe Committee shall have the following purposes:\n**(1)**\nTo improve enforcement of applicable Federal laws and regulations.\n**(2)**\nTo increase accountability of proprietary institutions of higher education to students and taxpayers.\n**(3)**\nTo ensure the promotion of high-quality education programs.\n**(4)**\nTo reduce and prevent fraud and abuse by proprietary institutions of higher education.\n##### (c) Responsibilities\nTo meet the purposes described in subsection (b), the Committee shall\u2014\n**(1)**\ncoordinate administrative oversight of proprietary institutions of higher education\u2014\n**(A)**\nsuch that the Federal agencies represented on the Committee may develop a memorandum of understanding to specify responsibilities of each of those agencies in creating the report under section 6;\n**(B)**\nto encourage information-sharing, to the extent practicable, among those agencies related to Federal investigations, audits, or inquiries of proprietary institutions of higher education; and\n**(C)**\nto increase coordination and cooperation between Federal and State agencies, including State Attorneys General and State approval agencies, with respect to improving oversight and accountability of proprietary institutions of higher education; and\n**(2)**\nsynthesize cross-agency industry data on proprietary institutions of higher education to\u2014\n**(A)**\ndevelop an annual report under section 6;\n**(B)**\npublish a For-Profit College Warning List for Parents and Students , in accordance with section 7; and\n**(C)**\ndevelop consistency among Federal and State agencies in the dissemination of consumer information regarding proprietary institutions of higher education to ensure that students, parents, and other stakeholders have easy access to that information.\n##### (d) Membership\n**(1) Designees**\nThe head of a Federal agency listed in subsection (a) may designate a high-ranking official of the agency to serve as a designee on the Committee. The designee shall be, whenever possible, the head of the portion of the agency that is most relevant to the purposes described in subsection (b).\n**(2) Chairperson**\nThe Secretary or the Secretary's designee shall serve as the Chairperson of the Committee.\n**(3) Committee support**\nThe Chairperson of the Committee shall ensure that appropriate staff and officials at the Department are available to support Committee-related work.\n##### (e) Committee meetings\nThe members of the Committee shall meet regularly, but not less often than once during each quarter of each fiscal year, to carry out the purposes described in subsection (b) and the responsibilities described in subsection (c).\n##### (f) Notification to individuals who submit complaints\nThe head of each Federal agency listed in subsection (a) shall notify each individual who submits to the Federal agency a complaint with respect to a proprietary institution of higher education that information from the complaint may be used to carry out the purposes described in subsection (b).\n#### 4. Proprietary Education Oversight Advisory Committee\n##### (a) In general\nThe Department shall establish a Proprietary Education Oversight Advisory Committee (referred to in this Act as the Advisory Committee ) to advise the Committee. The Advisory Committee shall meet not less often than twice each fiscal year.\n##### (b) FACA applicability\nThe Advisory Committee shall be subject to chapter 10 of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act ).\n##### (c) Membership\n**(1) In general**\nThe Advisory Committee shall have 13 members, of which\u2014\n**(A)**\n4 members shall be representatives from State attorneys general\u2014\n**(i)**\n2 of whom shall be appointed by the Speaker of the House of Representatives, 1 of whom shall be appointed on the recommendation of the majority leader of the House of Representatives, and 1 of whom shall be appointed on the recommendation of the minority leader of the House of Representatives; and\n**(ii)**\n2 of whom shall be appointed by the President pro tempore of the Senate, 1 of whom shall be appointed on the recommendation of the majority leader of the Senate, and 1 of whom shall be appointed on the recommendation of the minority leader of the Senate; and\n**(B)**\n9 members shall be appointed by the Secretary, of whom\u2014\n**(i)**\n1 member shall be a representative from a State approval agency;\n**(ii)**\n1 member shall be a representative from a veterans service organization;\n**(iii)**\n1 member shall be a representative from an accrediting agency;\n**(iv)**\n1 member shall be a representative from a civil rights organization;\n**(v)**\n1 member shall be a representative from a proprietary institution of higher education;\n**(vi)**\n1 member shall be a current student of a proprietary institution of higher education who is a dependent student;\n**(vii)**\n1 member shall be a current student of a proprietary institution of higher education who is an independent student;\n**(viii)**\n1 member shall be a representative from a consumer advocate organization; and\n**(ix)**\n1 member shall be a representative from a legal assistance organization that represents students or borrowers.\n**(2) Qualifications**\nIndividuals shall be appointed as members of the Advisory Committee\u2014\n**(A)**\non the basis of the individuals' experience, integrity, impartiality, and good judgment; and\n**(B)**\non the basis of the individuals' technical qualifications, professional standing, and demonstrated knowledge in the field of proprietary education.\n**(3) Terms of members**\nThe term of office of each member of the Advisory Committee shall be for 6 years, except that any member appointed to fill a vacancy occurring prior to the expiration of the term for which the member's predecessor was appointed shall be appointed for the remainder of such term.\n**(4) Vacancy**\nA vacancy on the Advisory Committee shall be filled in the same manner as the original appointment was made not later than 90 days after the vacancy occurs. If a vacancy occurs in a position to be filled by the Secretary, the Secretary shall publish a Federal Register notice soliciting nominations for the position not later than 30 days after being notified of the vacancy.\n##### (d) Duties\nThe Advisory Committee shall provide advice and recommendations to the Committee with respect to\u2014\n**(1)**\ncomplaints filed against proprietary institutions of higher education with State attorneys general or State approval agencies;\n**(2)**\nState enforcement actions against proprietary institutions of higher education;\n**(3)**\nminority enrollment in proprietary institutions of higher education;\n**(4)**\nveteran enrollment in proprietary institutions of higher education;\n**(5)**\noutcome measures at proprietary institutions of higher education, including\u2014\n**(A)**\ngraduation rates;\n**(B)**\npercent of graduates earning more than a high school graduate;\n**(C)**\nlicensure pass rates; and\n**(D)**\npercent of graduates working in a field related to their degree;\n**(6)**\nstudent loan burden from enrollment at proprietary institutions of higher education, including\u2014\n**(A)**\nmedian amount owed disaggregated by degree type;\n**(B)**\ncohort default rate;\n**(C)**\npercent of students in repayment; and\n**(D)**\nannual debt-to-earnings rates, as calculated under section 668.403 of title 34, Code of Federal Regulations, or any successor regulation;\n**(7)**\nmarketing and recruitment practices at proprietary institutions of higher education;\n**(8)**\nper pupil expenditure for instructional purposes at proprietary institutions of higher education;\n**(9)**\nenforcement actions the Federal Government should take against proprietary institutions of higher education; and\n**(10)**\npreparation of the report under section 6.\n##### (e) Sharing of data from complaints\nTo carry out the duties described under subsection (d), the Advisory Committee may share among the members of the Advisory Committee and the Committee information from complaints filed against proprietary institutions of higher education consistent with the protection of the privacy and confidentiality of personally identifiable information.\n#### 5. Collection and tracking of complaints\n##### (a) In general\n**(1) Centralized collection, monitoring, and response**\nIn consultation with the Committee, the Secretary shall establish a single, toll-free telephone number, a website, and a database (or use an existing database) to facilitate the centralized collection of, monitoring of, and response to student complaints regarding the services or activities of any proprietary institution of higher education that is eligible for Federal education assistance.\n**(2) Coordination**\nThe Committee shall coordinate with the Federal agencies represented on the Committee to route complaints to those agencies, where appropriate, and consistent with\u2014\n**(A)**\nthe protection of the privacy and confidentiality of personally identifiable information; and\n**(B)**\ndata security and integrity.\n##### (b) Use of complaint information\nInformation collected from complaints under subsection (a) shall be used\u2014\n**(1)**\nto facilitate coordination among the Federal agencies represented on the Committee;\n**(2)**\nto facilitate investigations and enforcement actions against proprietary institutions of higher education;\n**(3)**\nto prepare the report under section 6; and\n**(4)**\nto prepare the For-Profit College Warning List for Parents and Students under section 7.\n##### (c) Routing complaints to States\nTo the extent practicable, State approval agencies may receive appropriate complaints from the systems established under subsection (a), if\u2014\n**(1)**\nthe State approval agency system has the functional capacity to receive calls or electronic reports routed by the systems of the Department;\n**(2)**\nthe State approval agency has satisfied any conditions of participation in the system that the Department may establish, including treatment of personally identifiable information and sharing of information on complaint resolution or related compliance procedures and resources; and\n**(3)**\nparticipation by the State approval agency includes measures necessary to provide for protection of personally identifiable information that conform to the Federal laws and standards for protection of the privacy and confidentiality of personally identifiable information and for data integrity and security that apply to the Federal agencies described in subsection (d).\n##### (d) Data-Sharing required\n**(1) In general**\nTo facilitate preparation of the reports required under section 6, supervision and enforcement activities, and monitoring of the market for educational services provided by any proprietary institution of higher education that is eligible for Federal education assistance, the Committee members shall share student complaint information with accrediting agencies, the Federal Trade Commission, other Federal agencies, and State agencies, subject to the Federal laws and standards applicable to Federal agencies for the protection of the privacy and confidentiality of personally identifiable information and for data security and integrity.\n**(2) Sharing of data with the department**\nThe accrediting agencies, the Federal Trade Commission, and other Federal agencies shall share data relating to student complaints regarding educational services provided by any proprietary institution of higher education with the Department, subject to the Federal laws and standards applicable to Federal agencies for the protection of the privacy and confidentiality of personally identifiable information and for data security and integrity.\n#### 6. Report\n##### (a) In general\nThe Committee shall submit an annual report to the Committee on Health, Education, Labor, and Pensions of the Senate, the Committee on Education and Workforce of the House of Representatives, and any other committee of Congress that the Committee determines appropriate.\n##### (b) Confidentiality and public access\nThe report described in subsection (a)\u2014\n**(1)**\nshall not contain any personally identifiable information; and\n**(2)**\nshall be made available to the public in a manner that is easily accessible to parents, students, and other stakeholders.\n##### (c) Contents\n**(1) In general**\nThe report described in subsection (a) shall include\u2014\n**(A)**\na description of the role of each member of the Committee in achieving the purposes described in section 3(b);\n**(B)**\nan accounting of any negative or adverse action taken by the Federal Government, any member agency of the Committee, or a State to enforce Federal or State laws and regulations applicable to a proprietary institution of higher education;\n**(C)**\na summary of complaints received, resolved, or pending against each proprietary institution of higher education during the applicable year, including\u2014\n**(i)**\nstudent complaints collected by the complaint system established under section 5 or received by any member agency of the Committee;\n**(ii)**\nany complaint filed by a Federal or State agency in a Federal, State, local, or Tribal court;\n**(iii)**\nany administrative proceeding by a Federal or State agency involving noncompliance of any applicable law or regulation;\n**(iv)**\nany other review, audit, or administrative process by any Federal or State agency that results in a penalty, suspension, or termination from any Federal or State program; and\n**(v)**\nany complaint, review, audit, or administrative process by an accrediting agency that results in probation or equivalent action, denial, withdrawal, suspension, or termination of accreditation;\n**(D)**\nthe data described in paragraph (2) and any other data relevant to proprietary institutions of higher education that the Committee determines appropriate; and\n**(E)**\nrecommendations of the Committee for the legislative and administrative actions as the Committee determines are necessary to\u2014\n**(i)**\nimprove enforcement of applicable Federal laws;\n**(ii)**\nincrease accountability of proprietary institutions of higher education to students, parents, and taxpayers;\n**(iii)**\nreduce and prevent fraud and abuse by proprietary institutions of higher education; and\n**(iv)**\nensure the promotion of quality education programs.\n**(2) Data**\n**(A) Industry-wide data**\nThe report described in subsection (a) shall include data on all proprietary institutions of higher education that consists of information regarding\u2014\n**(i)**\nthe total amount of Federal education assistance that proprietary institutions of higher education received for the previous academic year, and the percentage of the total amount of Federal education assistance provided to institutions of higher education (as defined in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 )) for the previous academic year that reflects the total amount of Federal education assistance provided to proprietary institutions of higher education for the previous academic year;\n**(ii)**\nthe total amount of Federal education assistance that proprietary institutions of higher education received for the previous academic year, disaggregated by\u2014\n**(I)**\neducational assistance in the form of a loan provided under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. );\n**(II)**\neducational assistance in the form of a grant provided under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. );\n**(III)**\neducational assistance provided under chapter 33 of title 38, United States Code;\n**(IV)**\nassistance for tuition and expenses under section 2007 of title 10, United States Code;\n**(V)**\nassistance provided under section 1784a of title 10, United States Code; and\n**(VI)**\nFederal education assistance not described in subclauses (I) through (V);\n**(iii)**\nthe percentage of the total amount of Federal education assistance provided to institutions of higher education (as defined in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 )) for the previous academic year for each of the programs described in subclauses (I) through (VI) of clause (ii), that reflects the total amount of Federal education assistance provided to proprietary institutions of higher education for the previous academic year for each of those programs;\n**(iv)**\nthe average retention and graduation rates for students pursuing a degree at proprietary institutions of higher education;\n**(v)**\nthe average cohort default rate (as defined in section 435(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1085(m) )) and average annual debt-to-earnings rate (as calculated under section 668.403 of title 34, Code of Federal Regulations, or any successor regulation) for proprietary institutions of higher education, and the cohort default rate and annual debt-to-earnings rate for each proprietary institution of higher education;\n**(vi)**\nthe average pre-enrollment expenditures on a per-enrolled-student basis, including expenditures on recruiting and marketing activities;\n**(vii)**\nthe average educational and general expenditures (as defined in section 502 of the Higher Education Act of 1965 ( 20 U.S.C. 1101a )) per student, excluding all pre-enrollment expenditures, disaggregated by educational expenditures and general expenditures;\n**(viii)**\nfor careers requiring the passage of a licensing examination\u2014\n**(I)**\nthe passing rate of individuals who attended a proprietary institution of higher education taking the examination to pursue such a career; and\n**(II)**\nthe passing rate of all individuals taking the exam to pursue such a career;\n**(ix)**\nthe use of private education loans at proprietary institutions of higher education that includes\u2014\n**(I)**\nan estimate of the total number of those loans;\n**(II)**\ninformation on the average debt, default rate, and interest rate of those loans; and\n**(III)**\nthe names of each lender providing private education loans to borrowers with respect to each proprietary institution of higher education in the prior academic year, including\u2014\n**(aa)**\nthe number of borrowers receiving loans from each lender; and\n**(bb)**\nthe volume of dollars provided to borrowers with respect to the proprietary institution of higher education by each lender; and\n**(x)**\nthe percent of graduates of proprietary institutions of higher education working in a field related to their degree.\n**(B) Data on publicly traded corporations**\n**(i) In general**\nThe report described in subsection (a) shall include data on proprietary institutions of higher education that are publicly traded corporations, consisting of information on\u2014\n**(I)**\nany pre-tax profit of those proprietary institutions of higher education\u2014\n**(aa)**\nreported as a total amount and an average percent of revenue for all those proprietary institutions of higher education; and\n**(bb)**\nreported for each of those proprietary institutions of higher education;\n**(II)**\nrevenue for those proprietary institutions of higher education spent on recruiting and marketing activities, student instruction, and student support services, reported\u2014\n**(aa)**\nas a total amount and an average percentage of revenue for all those proprietary institutions of higher education; and\n**(bb)**\nfor each of those proprietary institutions of higher education;\n**(III)**\ntotal compensation packages, including bonuses, of the executive officers of each of those proprietary institutions of higher education;\n**(IV)**\na list of institutional loan programs offered by each of those proprietary institutions of higher education that includes information on the default and interest rates of those programs; and\n**(V)**\nthe data described in clauses (ii) and (iii).\n**(ii) Disaggregated by ownership**\nThe report shall include data on proprietary institutions of higher education that are publicly traded corporations, disaggregated by corporate or parent entity, brand name, and campus, consisting of\u2014\n**(I)**\nthe average total cost of attendance at each proprietary institution of higher education, and information comparing the total cost for each program to\u2014\n**(aa)**\nthe average total cost of attendance\u2014\n(AA)\nat each public institution of higher education; and\n(BB)\nat each public institution of higher education that offers the same level of education degree or certification as the proprietary institution of higher education; and\n**(bb)**\nthe average total cost of attendance\u2014\n(AA)\nat all institutions of higher education, including institutions that are public and institutions that are private; and\n(BB)\nat all institutions of higher education that offer the same level of education degree or certification as the proprietary institution of higher education, including institutions that are public and institutions that are private;\n**(II)**\ntotal enrollment, disaggregated by\u2014\n**(aa)**\nindividuals enrolled in programs taken online;\n**(bb)**\nindividuals enrolled in programs that are not taken online; and\n**(cc)**\nindividuals enrolled in programs taken both online and not online;\n**(III)**\nthe average retention and graduation rates for students pursuing a degree at proprietary institutions of higher education;\n**(IV)**\nthe percentage of students enrolled in proprietary institutions of higher education who complete a program of an institution within\u2014\n**(aa)**\nthe standard period of completion for the program; and\n**(bb)**\na period that is 150 percent of the standard period of completion;\n**(V)**\nthe average total cost of attendance for each program at proprietary institutions of higher education;\n**(VI)**\nthe average cohort default rate, as defined in section 435(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1085(m) ), for proprietary institutions of higher education, and an annual list of cohort default rates (as so defined) for all proprietary institutions of higher education;\n**(VII)**\nthe median Federal educational debt incurred by students who complete a program at a proprietary institution of higher education;\n**(VIII)**\nthe median Federal educational debt incurred by students who start but do not complete a program at a proprietary institution of higher education;\n**(IX)**\nthe job placement rate for students who complete a program at a proprietary institution of higher education and the type of employment obtained by those students;\n**(X)**\nfor careers requiring the passage of a licensing examination, the passing rate for individuals who attended a proprietary institution of higher education and passed the examination;\n**(XI)**\nthe number of complaints from students enrolled in proprietary institutions of higher education who have submitted a complaint to any member agency of the Committee; and\n**(XII)**\nthe volume of institutional debt, number of students who owe institutional debts, average amount of institutional debt owed by each student, and annual debt-to-earnings rate (as calculated under section 668.403 of title 34, Code of Federal Regulations, or any successor regulation).\n**(iii) Department of Defense and Veterans Affairs assistance**\n**(I) In general**\nTo the extent practicable, the report described in subsection (a) shall provide information on the data described in clause (ii) for individuals using, to pay for the costs of attending a proprietary institution of higher education, Federal education assistance provided under\u2014\n**(aa)**\nchapter 33 of title 38, United States Code;\n**(bb)**\nsection 2007 of title 10, United States Code; and\n**(cc)**\nsection 1784a of title 10, United States Code.\n**(II) Revenue**\nThe report shall provide information on the revenue of proprietary institutions of higher education that are publicly traded corporations that is derived from the Federal education assistance described in subclause (I).\n**(C) Comparison data**\nTo the extent practicable, the report shall provide information comparing the data described in subparagraph (B) for proprietary institutions of higher education that are publicly traded corporations with data for public institutions of higher education disaggregated by State.\n**(3) Accounting of any action**\nAs used in paragraph (1)(B), the term any negative or adverse action includes\u2014\n**(A)**\na complaint filed by a Federal or State agency in a local, State, Federal, or Tribal court;\n**(B)**\nan administrative proceeding by a Federal or State agency involving noncompliance with any applicable law or regulation; or\n**(C)**\nany other review, audit, or administrative process by any Federal or State agency that results in a penalty, suspension, or termination from any Federal or State program.\n#### 7. For-profit college warning list for parents and students\n##### (a) In general\nEach academic year, the Secretary on behalf of the Committee shall publish a list to be known as the For-Profit College Warning List for Parents and Students to be comprised of the names of proprietary institutions of higher education\u2014\n**(1)**\nthat have been sued for financial relief by a Federal or State authority, or through a qui tam action in which the Federal Government has intervened;\n**(2)**\nthat are required to pay a debt or incur a liability from a settlement, arbitration proceeding, or final judgment in a judicial proceeding with a Federal or State agency and the case addresses misrepresentation, fraud, liability under sections 3729 through 3733 of title 31, United States Code (commonly known as the False Claims Act ), or other borrower-defense-to-repayment claims;\n**(3)**\nthat have pending claims for borrower relief discharge under the borrower defense to repayment regulations from students or former students of the institution and the Secretary has formed a group process to consider the claims;\n**(4)**\nthat have had any eligibility for participation withdrawn or suspended with respect to\u2014\n**(A)**\neducational assistance in the form of a loan provided under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. );\n**(B)**\neducational assistance in the form of a grant provided under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. );\n**(C)**\neducational assistance provided under chapter 33 of title 38, United States Code;\n**(D)**\nassistance for tuition and expenses under section 2007 of title 10, United States Code;\n**(E)**\nassistance provided under section 1784a of title 10, United States Code; or\n**(F)**\nFederal education assistance not described in subparagraphs (A) through (E); or\n**(5)**\nthat have been deemed ineligible to receive Federal education assistance for the next year or required to repay Federal education assistance previously received in an applicable report year.\n##### (b) Summary\nThe For-Profit College Warning List for Parents and Students shall include a summary in plain language of the basis of each proprietary institution of higher education\u2019s inclusion on the list.\n##### (c) Procedures\nThe Committee shall establish and apply review procedures for the For-Profit College Warning List for Parents and Students, including evaluation and withdrawal proceedings that provide\u2014\n**(1)**\nfor adequate written specification of\u2014\n**(A)**\nthe procedure for identifying proprietary intuitions of higher education for inclusion on the list; and\n**(B)**\nidentified deficiencies at the proprietary institutions of higher education; and\n**(2)**\nfor sufficient opportunity for a written response by a proprietary institution of higher education regarding any deficiencies identified by the Committee\u2014\n**(A)**\nwithin a timeframe determined by the Committee; and\n**(B)**\nprior to the final publication of the For-Profit College Warning List for Parents and Students.\n##### (d) Publication\n**(1) In general**\nNot later than July 1 of each fiscal year, on behalf of the Committee, the Secretary shall publish the For-Profit College Warning List for Parents and Students prominently and in a manner that\u2014\n**(A)**\nis easily accessible to parents, current students, prospective students, and other stakeholders; and\n**(B)**\ndoes not contain any personally identifiable information.\n**(2) Use of preexisting platform**\nThe Secretary may incorporate the For-Profit College Warning List for Parents and Students into preexisting, widely used platforms.",
      "versionDate": "2026-03-11",
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
        "name": "Education",
        "updateDate": "2026-04-01T15:47:44Z"
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
      "date": "2026-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4056is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Proprietary Education Interagency Oversight Committee and to facilitate the disclosure and reporting of information regarding complaints and investigations related to proprietary institutions of higher education eligible to receive Federal education assistance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:33Z"
    },
    {
      "title": "Proprietary Education Oversight Task Force Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Proprietary Education Oversight Task Force Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:19Z"
    }
  ]
}
```
