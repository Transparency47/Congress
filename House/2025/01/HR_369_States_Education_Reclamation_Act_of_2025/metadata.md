# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/369?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/369
- Title: States’ Education Reclamation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 369
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-08-09T08:05:53Z
- Update date including text: 2025-08-09T08:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/369",
    "number": "369",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "States\u2019 Education Reclamation Act of 2025",
    "type": "HR",
    "updateDate": "2025-08-09T08:05:53Z",
    "updateDateIncludingText": "2025-08-09T08:05:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:02:15Z",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "MD"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MI"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "NC"
    },
    {
      "bioguideId": "K000405",
      "district": "13",
      "firstName": "Brad",
      "fullName": "Rep. Knott, Brad [R-NC-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Knott",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "AL"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "SC"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "IA"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "OH"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr369ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 369\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Rouzer introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo provide for the elimination of the Department of Education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the States\u2019 Education Reclamation Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nPrinciples of federalism embodied in the Constitution of the United States entrust authority over issues of educational policy to the States and the people and a Federal Department of Education is inconsistent with such principles.\n**(2)**\nTradition and experience dictate that the governance and management of schools in the United States are best performed by parents, teachers, and communities.\n**(3)**\nThe education of the Nation\u2019s students is suffering under a managerial government.\n**(4)**\nThe Department of Education has weakened the ability of parents to make essential decisions about their children\u2019s education and has undermined the capacity of communities to govern their schools.\n**(5)**\nIn the 41 years of its existence, the Department of Education has grown from a budget of $14 billion to almost $73.5 billion in annual discretionary appropriations administering around 100 programs. Meanwhile, education performance for 17-year-olds has stagnated since 1971.\n**(6)**\nThe Department of Education has fostered overregulation, standardization, bureaucratization, and litigation in United States education.\n**(7)**\nThe Department of Education expends large amounts of money on its own maintenance and overhead. While the average national salary for public school teachers is $61,730 the average salary for a Department of Education employee is $112,724.\n**(8)**\nIn certain States, the average State salary for a public school teacher is less than the national average. In North Carolina, the average salary for a public school teacher is $53,975.\n**(9)**\nRecent tests reflect poor results in mathematics, science, and reading for American students compared with students from other nations.\n**(10)**\nOnly through initiatives led by parents and local communities with the power to act can the United States elevate educational performance toward an acceptable level.\n**(11)**\nThe current system of top-down education uniformity is detrimental to local businesses and communities, the economic needs of the States, and the Nation\u2019s ability to compete globally for jobs.\n**(12)**\nThe Department of Education has been hostile to many promising reforms, including reforms that would empower parents, teachers, and local communities. The United States, once a laboratory of innovation through the experiments of the States, is moving toward education standardization that does not consider the individual educational needs of our diverse population of students.\n#### 3. Abolition of Department of Education\nThe Department of Education is abolished, and, with the exception of the programs transferred under section 7, any program for which the Secretary of Education or the Department of Education has administrative responsibility as provided by law or by delegation of authority pursuant to law is repealed, including each program under the following:\n**(1)**\nThe Department of Education Organization Act ( 20 U.S.C. 3401 et seq. ).\n**(2)**\nThe General Education Provisions Act ( 20 U.S.C. 1221 et seq. ).\n#### 4. Grants to States for elementary and secondary and for postsecondary education programs\n##### (a) In general\nSubject to the requirements of this Act, each State is entitled to receive from the Secretary of the Treasury, by not later than July 1 of the preceding fiscal year\u2014\n**(1)**\na grant for fiscal year 2025 and each succeeding fiscal year through fiscal year 2033, that is equal to the amount of funds appropriated for the State for Federal elementary school and secondary school programs for fiscal year 2025 (except for the funds appropriated for fiscal year 2025 for such programs for such State that are being transferred under section 7); and\n**(2)**\na grant for fiscal year 2025 and each succeeding fiscal year through fiscal year 2033, that is equal to the amount of funds appropriated for the State for Federal postsecondary education programs for fiscal year 2025 (except for the funds appropriated for fiscal year 2025 for such programs for such State that are being transferred under section 7).\n##### (b) Appropriation\nOut of any money in the Treasury of the United States not otherwise appropriated, there are appropriated for fiscal years 2025 through 2033, such sums as are necessary for grants under subsection (a).\n##### (c) Requirements relating to intergovernmental financing\nThe Secretary of the Treasury shall make the transfer of funds under grants under subsection (a) directly to each State in accordance with the requirements of section 6503 of title 31, United States Code.\n##### (d) Expenditure of funds\nAmounts received by a State under this section for any fiscal year shall be expended by the State in such fiscal year or in the succeeding fiscal year.\n##### (e) Use of funds\nFunds made available to a State\u2014\n**(1)**\nunder subsection (a)(1), shall be used by the State for any elementary or secondary education purpose permitted by State law, including increases in teacher salaries; and\n**(2)**\nunder subsection (a)(2), shall be used by the State for any postsecondary education purpose permitted by State law.\n##### (f) Supplement, not supplant\nA grant received under subsection (a) shall only be used to supplement the amount of funds that would, in the absence of such grant, be made available from non-Federal sources for elementary school and secondary school programs or postsecondary education programs, and not to supplant those funds.\n#### 5. Administrative and fiscal accountability\n##### (a) Audits\n**(1) Contract with approved auditing entity**\nNot later than October 1, 2025, and annually thereafter, a State shall contract with an approved auditing entity (as defined under paragraph (3)(B)) for purposes of conducting an audit under paragraph (2) (with respect to the fiscal year ending September 30 of such year).\n**(2) Audit requirement**\nUnder a contract under paragraph (1), an approved auditing entity shall conduct an audit of the expenditures or transfers made by a State from amounts received under a grant under section 4, with respect to the fiscal year which such audit covers, to determine the extent to which such expenditures and transfers were expended in accordance with section 4.\n**(3) Entity conducting audit**\n**(A) In general**\nWith respect to a State, the audit under paragraph (2) shall be conducted by an approved auditing entity in accordance with generally accepted auditing principles.\n**(B) Approved auditing entity**\nFor purposes of this section, the term approved auditing entity means, with respect to a State, an entity that is\u2014\n**(i)**\napproved by the Secretary of the Treasury;\n**(ii)**\napproved by the chief executive officer of the State; and\n**(iii)**\nindependent of any Federal, State, or local agency.\n**(4) Submission of audit**\nNot later than April 30, 2026, and annually thereafter, a State shall submit the results of the audit under paragraph (2) (with respect to the fiscal year ending on September 30 of such year) to the State legislature and to the Secretary of the Treasury.\n##### (b) Reimbursement and penalty\nIf, through an audit conducted under subsection (a), an approved auditing entity finds that a State violated the requirements of subsection (d) or (e) of section 4, the State shall pay to the Treasury of the United States 100 percent of the amount of State funds that were used in violation of section 4 as a penalty. Insofar as a State fails to pay any such penalty, the Secretary of the Treasury shall offset the amount not so paid against the amount of any grant otherwise payable to the State under this Act.\n##### (c) Annual reporting requirements\n**(1) In general**\nNot later than January 31, 2026, and annually thereafter, each State shall submit to the Secretary of the Treasury and the State legislature a report on the activities carried out by the State during the most recently completed fiscal year with funds received by the State under a grant under section 4 for such fiscal year.\n**(2) Content**\nA report under paragraph (1) shall, with respect to a fiscal year\u2014\n**(A)**\ncontain the results of the audit conducted by an approved auditing entity for a State for such fiscal year, in accordance with the requirements of subsection (a) of this section;\n**(B)**\nspecify the amount of the grant made to the State under section 4; and\n**(C)**\nbe in such form and contain such other information as the State determines is necessary to provide\u2014\n**(i)**\nan accurate description of the activities conducted by the State for the purpose described under section 4; and\n**(ii)**\na complete record of the purposes for which amounts were expended in accordance with this section.\n**(3) Public availability**\nA State shall make copies of the reports required under this section available on a public website and shall make copies available in other formats upon request.\n##### (d) Failure To comply with requirements\nThe Secretary of the Treasury shall not make any payment to a State under a grant authorized by section 4\u2014\n**(1)**\nif an audit for a State is not submitted as required under subsection (a) during the period between the date such audit is due and the date on which such audit is submitted;\n**(2)**\nif a State fails to submit a report as required under subsection (c) during the period between the date such report is due and the date on which such report is submitted; or\n**(3)**\nif a State violates a requirement of section 4 during the period beginning on the date the Secretary becomes aware of such violation and the date on which such violation is corrected by the State.\n##### (e) Administrative supervision and oversight\n**(1) Limited role for Secretary of the Treasury**\nThe authority of the Secretary of the Treasury under this Act is limited to\u2014\n**(A)**\npromulgating regulations, issuing rules, or publishing guidance documents to the extent necessary for purposes of implementing subsection (a)(3)(B), subsection (b), and subsection (d);\n**(B)**\nmaking payments to the States under grants under section 4;\n**(C)**\napproving entities under subsection (a)(3)(B) for purposes of the audits required under subsection (a);\n**(D)**\nwithholding payment to a State of a grant under subsection (d) or offsetting a payment of such a grant to a State under subsection (b); and\n**(E)**\nexercising the authority relating to nondiscrimination that is specified in section 6(b).\n**(2) Limited role for Attorney general**\nThe authority of the Attorney General to supervise the amounts received by a State under section 4 is limited to the authority under section 6(b).\n##### (f) Reservation of state powers\nNothing in this section shall be construed to limit the power of a State, including the power of a State to pursue civil and criminal penalties under State law against any individual or entity that misuses, or engages in fraud or abuse related to, the funds provided to a State under section 4.\n#### 6. Nondiscrimination provisions\n##### (a) No discrimination against individuals\nNo individual shall be excluded from participation in, denied the benefits of, or subjected to discrimination under, any program or activity funded in whole or in part with amounts paid to a State under section 4 on the basis of such individual\u2019s\u2014\n**(1)**\ndisability under section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 );\n**(2)**\nsex under title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ); or\n**(3)**\nrace, color, or national origin under title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ).\n##### (b) Compliance\n**(1) In general**\nIf the Attorney General determines that a State or an entity that has received funds from amounts paid to a State under a grant under section 4 has failed to comply with a provision of law referred to in subsection (a), the Secretary of the Treasury shall notify the chief executive officer of the State of such failure to comply and shall request that such chief executive officer secure such compliance.\n**(2) Enforcement**\nIf, not later than 60 days after receiving notification under paragraph (1), the chief executive officer of a State fails or refuses to secure compliance with the provision of law referred to in such notification, the Attorney General may\u2014\n**(A)**\ninstitute an appropriate civil action; or\n**(B)**\nexercise the powers and functions provided under section 505 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794a ), title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ), or title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ) (as applicable).\n#### 7. Transfer of certain department of education programs\n##### (a) Transfer of certain programs\nNot later than 24 months after the date of the enactment of this Act\u2014\n**(1)**\neach job training program under the jurisdiction of the Department of Education, including the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2301 et seq. ), shall be transferred to the Department of Labor;\n**(2)**\neach special education grant program under the Individuals with Disabilities Education Act ( 20 U.S.C. 1460 et seq. ) shall be transferred to the Department of Health and Human Services;\n**(3)**\neach Indian education program under the jurisdiction of the Department of Education shall be transferred to the Department of the Interior;\n**(4)**\neach Impact Aid program under title VIII of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7701 et seq. ) shall be transferred to the Department of Defense;\n**(5)**\nthe Federal Pell Grant program under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070a ) shall be transferred to the Department of the Treasury;\n**(6)**\neach Federal student loan program under the jurisdiction of the Department of Education shall be transferred to the Department of the Treasury;\n**(7)**\neach program under the jurisdiction of the Institute of Education Sciences shall be transferred to the Department of Health and Human Services; and\n**(8)**\neach program under the jurisdiction of the D.C. Opportunity Scholarship Program shall be transferred to the Department of Health and Human Services.\n##### (b) Limitation on transfer of certain programs\nThe transfer of programs pursuant to subsection (a) is limited to only the transfer of administrative responsibility as provided by law or the delegation of authority pursuant to law and does not extend to the transfer of personnel employed by the Department of Education to carry out such programs.\n#### 8. GAO report\nNot later than 90 days after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Education and the Workforce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate report, which shall include\u2014\n**(1)**\na review and evaluation as to the feasibility of enhancing the ability of States and local communities to fund education by reducing the Federal tax burden and commensurately eliminating Federal Government involvement in providing grants for education programs; and\n**(2)**\nan evaluation of the feasibility of the successor Federal agencies for maintaining the programs to be transferred under section 7.\n#### 9. Plan for closure of the Department of Education\nNot later than 365 days after the date of the enactment of this Act, the President shall submit to the Congress a plan to implement closure of the Department of Education in accordance with this Act.\n#### 10. Definitions\nIn this Act:\n**(1) Elementary school; secondary school**\nThe terms elementary school and secondary school have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 102 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 1002 ).\n**(3) State**\nThe term State has the meaning given the term in section 103 of the Higher Education Act of 1965 ( 20 U.S.C. 1003 ).",
      "versionDate": "2025-01-13",
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
            "name": "Accounting and auditing",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Appropriations",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Department of Education",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Disability and health-based discrimination",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Special education",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2025-02-24T20:31:17Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2025-02-24T20:31:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-02-13T19:33:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr369",
          "measure-number": "369",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr369v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>States' Education Reclamation Act of </strong><strong>2025</strong></p><p>This bill abolishes the Department of Education (ED) and repeals any program for which it has administrative responsibility.</p><p>The Department of the Treasury must provide grants to states, for FY2025-FY2033, for elementary, secondary, and postsecondary education purposes permitted by state law. The level of funding is set at the amount provided to states for federal elementary and secondary education programs and the amount provided for federal postsecondary education programs, respectively, for FY2025, minus the funding provided for education programs that the bill transfers to other federal agencies.</p><p>States must contract for an annual audit of their expenditures or transfers of grant funds.</p><p>Program administrative responsibility and delegation of authority are transferred as follows:</p><ul><li>ED's job training programs to the Department of Labor,</li><li>each special education grant program under the Individuals with Disabilities Education Act to the Department of Health and Human Services (HHS),</li><li>ED's Indian education programs to the Department of the Interior,</li><li>each Impact Aid program under the Elementary and Secondary Education Act of 1965 to the Department of Defense,</li><li>the Federal Pell Grant program and each federal student loan program to Treasury, and</li><li>programs under the jurisdiction of the Institute of Education Sciences or the D.C. Opportunity Scholarship Program to HHS.</li></ul><p>The\u00a0Government Accountability Office must report to Congress on (1) the feasibility of reducing the federal tax burden and eliminating federal involvement in providing grants for education programs, and (2) the feasibility of successor federal agencies maintaining transferred education programs.</p>"
        },
        "title": "States\u2019 Education Reclamation Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr369.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>States' Education Reclamation Act of </strong><strong>2025</strong></p><p>This bill abolishes the Department of Education (ED) and repeals any program for which it has administrative responsibility.</p><p>The Department of the Treasury must provide grants to states, for FY2025-FY2033, for elementary, secondary, and postsecondary education purposes permitted by state law. The level of funding is set at the amount provided to states for federal elementary and secondary education programs and the amount provided for federal postsecondary education programs, respectively, for FY2025, minus the funding provided for education programs that the bill transfers to other federal agencies.</p><p>States must contract for an annual audit of their expenditures or transfers of grant funds.</p><p>Program administrative responsibility and delegation of authority are transferred as follows:</p><ul><li>ED's job training programs to the Department of Labor,</li><li>each special education grant program under the Individuals with Disabilities Education Act to the Department of Health and Human Services (HHS),</li><li>ED's Indian education programs to the Department of the Interior,</li><li>each Impact Aid program under the Elementary and Secondary Education Act of 1965 to the Department of Defense,</li><li>the Federal Pell Grant program and each federal student loan program to Treasury, and</li><li>programs under the jurisdiction of the Institute of Education Sciences or the D.C. Opportunity Scholarship Program to HHS.</li></ul><p>The\u00a0Government Accountability Office must report to Congress on (1) the feasibility of reducing the federal tax burden and eliminating federal involvement in providing grants for education programs, and (2) the feasibility of successor federal agencies maintaining transferred education programs.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr369"
    },
    "title": "States\u2019 Education Reclamation Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>States' Education Reclamation Act of </strong><strong>2025</strong></p><p>This bill abolishes the Department of Education (ED) and repeals any program for which it has administrative responsibility.</p><p>The Department of the Treasury must provide grants to states, for FY2025-FY2033, for elementary, secondary, and postsecondary education purposes permitted by state law. The level of funding is set at the amount provided to states for federal elementary and secondary education programs and the amount provided for federal postsecondary education programs, respectively, for FY2025, minus the funding provided for education programs that the bill transfers to other federal agencies.</p><p>States must contract for an annual audit of their expenditures or transfers of grant funds.</p><p>Program administrative responsibility and delegation of authority are transferred as follows:</p><ul><li>ED's job training programs to the Department of Labor,</li><li>each special education grant program under the Individuals with Disabilities Education Act to the Department of Health and Human Services (HHS),</li><li>ED's Indian education programs to the Department of the Interior,</li><li>each Impact Aid program under the Elementary and Secondary Education Act of 1965 to the Department of Defense,</li><li>the Federal Pell Grant program and each federal student loan program to Treasury, and</li><li>programs under the jurisdiction of the Institute of Education Sciences or the D.C. Opportunity Scholarship Program to HHS.</li></ul><p>The\u00a0Government Accountability Office must report to Congress on (1) the feasibility of reducing the federal tax burden and eliminating federal involvement in providing grants for education programs, and (2) the feasibility of successor federal agencies maintaining transferred education programs.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr369"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr369ih.xml"
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
      "title": "States\u2019 Education Reclamation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T09:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "States\u2019 Education Reclamation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T09:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the elimination of the Department of Education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T09:03:35Z"
    }
  ]
}
```
