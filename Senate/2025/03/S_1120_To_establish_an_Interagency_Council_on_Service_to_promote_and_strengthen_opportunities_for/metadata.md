# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1120?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1120
- Title: Unity through Service Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1120
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-12-05T21:46:34Z
- Update date including text: 2025-12-05T21:46:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (Sponsor introductory remarks on measure: CR S1837)
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (Sponsor introductory remarks on measure: CR S1837)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1120",
    "number": "1120",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "R000122",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Reed, Jack [D-RI]",
        "lastName": "Reed",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Unity through Service Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:46:34Z",
    "updateDateIncludingText": "2025-12-05T21:46:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (Sponsor introductory remarks on measure: CR S1837)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T19:40:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "IN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "DE"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1120is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1120\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Reed (for himself, Mr. Young , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo establish an Interagency Council on Service to promote and strengthen opportunities for military service, national service, and public service for all people of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Unity through Service Act of 2025 .\n#### 2. Interagency council on service\n##### (a) Establishment\n**(1) In general**\nThere is established an Interagency Council on Service (in this section referred to as the Council ).\n**(2) Functions**\nThe Council shall\u2014\n**(A)**\nadvise the President with respect to promoting, strengthening, and expanding opportunities for military service, national service, and public service for all people of the United States; and\n**(B)**\nreview, assess, and coordinate holistic recruitment strategies and initiatives of the executive branch to foster an increased sense of service and civic responsibility among all people of the United States and to explore ways of enhancing connectivity of interested applicants to national service programs and opportunities.\n##### (b) Composition\n**(1) Membership**\nThe Council shall be composed of members who are representatives of\u2014\n**(A)**\nthe Secretary of State;\n**(B)**\nthe Secretary of Defense;\n**(C)**\nthe Attorney General;\n**(D)**\nthe Secretary of the Interior;\n**(E)**\nthe Secretary of Commerce;\n**(F)**\nthe Secretary of Labor;\n**(G)**\nthe Secretary of Health and Human Services;\n**(H)**\nthe Secretary of Education;\n**(I)**\nthe Secretary of Veterans Affairs;\n**(J)**\nthe Secretary of Homeland Security;\n**(K)**\nthe Director of the Office of Management and Budget;\n**(L)**\nthe Director of National Intelligence;\n**(M)**\nthe Director of the Office of Personnel Management;\n**(N)**\nthe Director of the Peace Corps;\n**(O)**\nthe Director of the Selective Service System;\n**(P)**\nthe Chief Executive Officer of the Corporation for National and Community Service; and\n**(Q)**\nsuch other officers as the President may designate.\n**(2) Chair**\nThe President shall annually designate to serve as the Chair of the Council a member of the Council under paragraph (1), the appointment of whom as an officer or employee of the Federal Government was made by the President by and with the advice and consent of the Senate.\n**(3) Meetings**\nThe Council shall meet on a quarterly basis or more frequently as the Chair of the Council may direct.\n##### (c) Responsibilities of the council\nThe Council shall\u2014\n**(1)**\nassist and advise the President in the establishment of strategies, goals, objectives, and priorities to promote service and civic responsibility among all people of the United States;\n**(2)**\ndevelop and recommend to the President common recruitment strategies and outreach opportunities for increasing the participation, and propensity of people of the United States to participate, in military service, national service, and public service in order to address national security and domestic investment;\n**(3)**\nserve as a forum for Federal officials responsible for military service, national service, and public service programs to, as feasible and practicable\u2014\n**(A)**\ncoordinate and share best practices for service recruitment; and\n**(B)**\ndevelop common interagency, cross-service initiatives and pilots for service recruitment;\n**(4)**\nlead a strategic, interagency coordinated effort on behalf of the Federal Government to develop joint awareness and recruitment, retention, and marketing initiatives involving military service, national service, and public service;\n**(5)**\nconsider approaches for assessing impacts of service on the needs of the United States and individuals participating in and benefitting from such service;\n**(6)**\nconsult, as the Council considers advisable, with representatives of non-Federal entities, including State, local, and Tribal governments, State and local educational agencies, State Service Commissions, institutions of higher education, nonprofit organizations, faith-based organizations, philanthropic organizations, and the private sector, in order to promote and develop initiatives to foster and reward military service, national service, and public service;\n**(7)**\nnot later than 2 years after the date of enactment of this Act, and quadrennially thereafter, prepare and submit to the President and Congress a Service Strategy, which shall set forth\u2014\n**(A)**\na review of programs and initiatives of the Federal Government relating to the mandate of the Council;\n**(B)**\na review of Federal Government online content relating to the mandate of the Council, including user experience with such content;\n**(C)**\ncurrent and foreseeable trends for service to address the needs of the United States;\n**(D)**\nrecommended service recruitment strategies and branding opportunities to address outreach and communication deficiencies identified by the Council; and\n**(E)**\nto the extent practical, a joint service messaging strategy for military service, national service, and public service;\n**(8)**\nidentify any notable initiatives by State, local, and Tribal governments and by public and nongovernmental entities to increase awareness of and participation in national service programs; and\n**(9)**\nperform such other functions as the President may direct.\n#### 3. Joint market research to advance military and national service\n##### (a) Program authorized\nThe Secretary of Defense, the Chief Executive Officer of the Corporation for National and Community Service, and the Director of the Peace Corps may carry out a joint market research, market studies, recruiting, and advertising program to complement the existing programs of the military departments, the national service programs administered by the Corporation, and the Peace Corps.\n##### (b) Information sharing permitted\nSection 503 of title 10, United States Code, shall not be construed to prohibit sharing of information among, or joint marketing efforts of, the Department of Defense, the Corporation for National and Community Service, and the Peace Corps to carry out this section.\n#### 4. Transition opportunities for military servicemembers and national service participants\n##### (a) Employment assistance\nSection 1143(c)(1) of title 10, United States Code, is amended by inserting the Corporation for National and Community Service, after State employment agencies, .\n##### (b) Employment assistance, job training assistance, and other transitional services: Department of Labor\nSection 1144 of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (b), by adding at the end the following:\n(11) Provide information on public service opportunities, training on public service job recruiting, and the advantages of careers with the Federal Government. ; and\n**(2)**\nin subsection (f)(1)(D)\u2014\n**(A)**\nby redesignating clause (v) as clause (vi); and\n**(B)**\nby inserting after clause (iv) the following new clause:\n(v) National and community service, taught in conjunction with the Chief Executive Officer of the Corporation for National and Community Service. .\n##### (c) Authorities and duties of the chief executive officer\nSection 193A(b) of the National and Community Service Act of 1990 ( 42 U.S.C. 12651d(b) ) is amended\u2014\n**(1)**\nin paragraph (24), by striking and at the end;\n**(2)**\nin paragraph (25), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new paragraph:\n(26) ensure that individuals completing a partial or full term of service in a program under subtitle C or E or part A of title I of the Domestic Volunteer Service Act of 1973 ( 42 U.S.C. 4951 et seq. ) receive information about military and public service opportunities for which they may qualify or in which they may be interested. .\n#### 5. Joint report to congress on initiatives to integrate military and national service\n##### (a) Reporting requirement\nNot later than 4 years after the date of enactment of this Act and quadrennially thereafter, the Chair of the Interagency Council on Service, in coordination with the Secretary of Defense, the Chief Executive Officer of the Corporation for National and Community Service, and the Director of the Peace Corps, shall submit a joint report on cross-service marketing, research, and promotion, including recommendations for increasing joint advertising and recruitment initiatives for the Armed Forces, programs administered by the Corporation for National and Community Service, and the Peace Corps, to the following congressional committees:\n**(1)**\nThe Committee on Homeland Security and Governmental Affairs of the Senate.\n**(2)**\nThe Committee on Homeland Security of the House of Representatives.\n**(3)**\nThe Committee on Oversight and Accountability of the House of Representatives.\n**(4)**\nThe Committee on Armed Services of the Senate.\n**(5)**\nThe Committee on Armed Services of the House of Representatives.\n**(6)**\nThe Committee on Foreign Relations of the Senate.\n**(7)**\nThe Committee on Foreign Affairs of the House of Representatives.\n**(8)**\nThe Committee on Health, Education, Labor, and Pensions of the Senate.\n**(9)**\nThe Committee on Education and Workforce of the House of Representatives.\n##### (b) Contents of report\nEach report under subsection (a) shall include the following:\n**(1)**\nThe number of Peace Corps volunteers and participants in national service programs administered by the Corporation for National and Community Service, who previously served as a member of the Armed Forces.\n**(2)**\nThe number of members of the Armed Forces who previously served in the Peace Corps or in a program administered by the Corporation for National and Community Service.\n**(3)**\nAn assessment of existing (as of the date of the report submission) joint recruitment and advertising initiatives undertaken by the Department of Defense, the Peace Corps, or the Corporation for National and Community Service.\n**(4)**\nAn assessment of the feasibility and cost of expanding such existing initiatives.\n**(5)**\nAn assessment of ways to improve the ability of the reporting agencies to recruit individuals from the other reporting agencies.\n**(6)**\nA description of the information and data used to develop any initiative or campaign intended to advance military service or national service, including with respect to any activity carried out under section 3.\n##### (c) Consultation\nThe Chair of the Interagency Council on Service, the Secretary of Defense, the Chief Executive Officer of the Corporation for National and Community Service, and the Director of the Peace Corps shall undertake studies of recruiting efforts that are necessary to carry out the provisions of this section. Such studies may be conducted using any funds appropriated to those entities under Federal law other than this Act.\n#### 6. Reports to Congress on lessons learned regarding retention and recruitment\nThe Chair of the Interagency Council on Service shall\u2014\n**(1)**\nconduct a study on\u2014\n**(A)**\nthe effectiveness of past advertising campaigns for military service, national service, and public service; and\n**(B)**\nthe role of vaccine requirements on the retention and recruitment of individuals for military service, national service, and public service; and\n**(2)**\nnot later than 270 days after the date of enactment of this Act, submit a report on the findings of and lessons learned from the study under paragraph (1) to\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate; and\n**(B)**\nthe Committee on Homeland Security of the House of Representatives.\n#### 7. Definitions\nIn this Act:\n**(1) Interagency Council on Service**\nThe term Interagency Council on Service means the Interagency Council on Service established by section 2(a).\n**(2) Military department**\nThe term military department means each of the military departments listed in section 102 of title 5, United States Code.\n**(3) Military service**\nThe term military service means active service (as defined in subsection (d)(3) of section 101 of title 10, United States Code) or active status (as defined in subsection (d)(4) of such section) in one of the Armed Forces (as defined in subsection (a)(4) of such section).\n**(4) National service**\nThe term national service means participation, other than military service or public service, in a program that\u2014\n**(A)**\nis designed to enhance the common good and meet the needs of communities, the States, or the United States;\n**(B)**\nis funded or facilitated by\u2014\n**(i)**\nan institution of higher education as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ); or\n**(ii)**\nthe Federal Government or a State, Tribal, or local government; and\n**(C)**\nis a program authorized in\u2014\n**(i)**\nthe Peace Corps Act ( 22 U.S.C. 2501 et seq. );\n**(ii)**\nsection 171 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3226 ) relating to the YouthBuild Program;\n**(iii)**\nthe Domestic Volunteer Service Act of 1973 ( 42 U.S.C. 4950 et seq. ); or\n**(iv)**\nthe National and Community Service Act of 1990 ( 42 U.S.C. 12501 et seq. ).\n**(5) Public service**\nThe term public service means civilian employment in the Federal Government or a State, Tribal, or local government.\n**(6) Service**\nThe term service means a personal commitment of time, energy, and talent to a mission that contributes to the public good by protecting the Nation and the citizens of the United States, strengthening communities, States, or the United States, or promoting the general social welfare.\n**(7) State service commission**\nThe term State Service Commission means a State Commission on National and Community Service maintained by a State pursuant to section 178 of the National and Community Service Act of 1990 ( 42 U.S.C. 12638 ).\n#### 8. No additional funds\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act.\n#### 9. GAO report\nNot later than 30 months after the date of enactment of this Act, the Comptroller General of the United States shall report to Congress on the effectiveness of this Act and the amendments made by this Act.",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-03-25",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on Armed Services, Foreign Affairs, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2324",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Unity through Service Act of 2025",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-20T18:08:59Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1120is.xml"
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
      "title": "Unity through Service Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-08T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Unity through Service Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish an Interagency Council on Service to promote and strengthen opportunities for military service, national service, and public service for all people of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T04:18:22Z"
    }
  ]
}
```
