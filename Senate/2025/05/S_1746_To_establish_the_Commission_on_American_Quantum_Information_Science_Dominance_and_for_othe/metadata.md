# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1746?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1746
- Title: Quantum LEAP Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1746
- Origin chamber: Senate
- Introduced date: 2025-05-13
- Update date: 2026-03-18T11:03:18Z
- Update date including text: 2026-03-18T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in Senate
- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-05-13: Introduced in Senate

## Actions

- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1746",
    "number": "1746",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Quantum LEAP Act of 2025",
    "type": "S",
    "updateDate": "2026-03-18T11:03:18Z",
    "updateDateIncludingText": "2026-03-18T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-13",
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
            "date": "2025-05-13T22:23:45Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-13T22:23:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NM"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1746is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1746\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2025 Mrs. Blackburn (for herself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish the Commission on American Quantum Information Science Dominance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quantum Leadership in Emerging Applications and Policy Act of 2025 or the Quantum LEAP Act of 2025 .\n#### 2. Commission on American quantum information science and technology dominance\n##### (a) Establishment\n**(1) In general**\nThere is hereby established, as of the date specified in paragraph (2), an independent commission in the legislative branch of the Federal Government to examine and make recommendations with respect to emerging quantum information science as it pertains to current and future missions and activities of the United States Government and the private sector.\n**(2) Date of establishment**\nThe date of establishment referred to in paragraph (1) is the date that is 30 days after the date of the enactment of this Act.\n**(3) Designation**\nThe commission established by paragraph (1) shall be known as the Commission on American Quantum Information Science and Technology Dominance (in this section referred to as the Commission ).\n##### (b) Membership\n**(1) Composition**\nThe Commission shall be composed of 12 members appointed as follows:\n**(A)**\nTwo members appointed by the Chairman of the Committee on Commerce, Science, and Transportation of the Senate, 1 of whom is a Member of the Senate and 1 of whom is not.\n**(B)**\nTwo members appointed by the Ranking Member of the Committee on Commerce, Science, and Transportation of the Senate, 1 of whom is a Member of the Senate and 1 of whom is not.\n**(C)**\nTwo members appointed by the Chairman of the Committee on Science, Space, and Technology of the House of Representatives, 1 of whom is a Member of the House of Representatives and 1 of whom is not.\n**(D)**\nTwo members appointed by the Ranking Member of the Committee on Science, Space, and Technology of the House of Representatives, 1 of whom is a Member of the House of Representatives and 1 of whom is not.\n**(E)**\nOne member appointed by the majority leader of the Senate.\n**(F)**\nOne member appointed by the minority leader of the Senate.\n**(G)**\nOne member appointed by the Speaker of the House of Representatives.\n**(H)**\nOne member appointed by the minority leader of the House of Representatives.\n**(2) Deadline for appointment**\nMembers shall be appointed to the Commission under paragraph (1) not later than 45 days after the Commission establishment date specified under subsection (a)(2).\n**(3) Effect of lack of appointment by appointment date**\nIf 1 or more of the appointments under paragraph (1) is not made by the appointment date specified in paragraph (2), the authority to make such appointment or appointments shall expire, and the number of members of the Commission shall be reduced by the number equal to the number of appointments so not made.\n**(4) Qualifications**\nThe members of the Commission who are not members of Congress and who are appointed under paragraph (1) shall be individuals from private civilian life who are recognized experts and have relevant professional experience in matters relating to\u2014\n**(A)**\ndiverse modalities and applications of emerging quantum information science and associated technologies;\n**(B)**\nuse of emerging quantum information science and associated technologies by national policy makers and business leaders; or\n**(C)**\nthe implementation, funding, or oversight of the national and economic security policies of the United States.\n##### (c) Chair and vice chair\n**(1) Chair**\nThe Chairman of the Committee on the Committee on Commerce, Science, and Transportation of the Senate and the Chairman of the Committee on Commerce, Science, and Transportation of the House of Representatives shall jointly designate 1 member of the Commission to serve as Chair of the Commission.\n**(2) Vice chair**\nThe Ranking Member of the Committee on Commerce, Science, and Transportation of the Senate and the Ranking Member of the Committee on Science, Space, and Technology of the House of Representatives shall jointly designate 1 member of the Commission to serve as Vice Chair of the Commission.\n##### (d) Period of appointment and vacancies\nMembers of the Commission shall be appointed for the life of the Commission. A vacancy in the Commission shall not affect its powers and shall be filled in the same manner as the original appointment was made.\n##### (e) Review\n**(1) In general**\nThe Commission shall carry out a review of advances in emerging quantum information science and associated technologies. In carrying out such review, the Commission shall consider the methods, means, and investments necessary to advance and secure the development of quantum information science and associated technologies by the United States to comprehensively address the national and economic security needs of the United States.\n**(2) Coordination**\nThe Commission shall coordinate with Federal agencies relevant to the National Quantum Strategy, including the Department of Commerce, the Department of Energy, the National Institute of Standards and Technology, the National Quantum Coordination Office within the Office of Science and Technology Policy, the Department of Defense, and the National Science Foundation.\n**(3) Scope**\nIn conducting the review required by paragraph (1), the Commission shall consider the following:\n**(A)**\nThe global competitiveness of the United States in quantum information science and associated technologies, including matters relating to national security, economic security, defense, domestic supply chain, public-private partnerships, and investments.\n**(B)**\nMeans, methods, and investments for the United States to maintain and protect a technological advantage in quantum information science and associated technologies relating to national security and defense.\n**(C)**\nDevelopments and trends in international cooperation and competitiveness, including foreign investments in quantum information science and associated technologies that are scientifically and materially related to national security, economic security, and defense.\n**(D)**\nMeans by which to foster greater emphasis and investments in basic and advanced research to stimulate government, industry, academic and combined initiatives in quantum information science and associated technologies.\n**(E)**\nMeans by which to foster greater emphasis and investments in advanced development and test and evaluation of quantum information science-enabled capabilities to stimulate the growth of the United States quantum information science commercial industry, while also supporting and improving acquisition and adoption of quantum information science and associated technologies for national security purposes.\n**(F)**\nBarriers to commercialization and recommended mechanisms to accelerate technology transfer, Federal procurement, and industry access to Federal testbeds.\n**(G)**\nWorkforce and education incentives and programs to attract, recruit, and retain leading talent in fields relevant to the development and sustainment of quantum information science and associated technologies.\n**(H)**\nMeans to establish international standards for the use of quantum information science application.\n**(I)**\nMeans to establish data sharing capabilities within and amongst government, industry, and academia to foster collaboration and accelerate innovation, while maintaining privacy and security for data as required for national security, intellectual property, and personal protection purposes.\n**(J)**\nConsideration of the transformative potential and rapidly-changing developments of quantum information science and associated technologies and appropriate mechanisms for managing such technology related to national security, economic security, and defense.\n**(K)**\nMeans by which to advance all quantum information science and associated technologies and modalities.\n**(L)**\nComparison of the near-term applications development programs in the United States compared to those of other countries.\n**(M)**\nAny other matters the Commission deems relevant.\n##### (f) Commission report and recommendations\n**(1) Final report**\nNot later than the date that is 2 years after the Commission establishment date specified in subsection (a)(2), the Commission shall submit to Congress and the President a final report on the findings of the Commission and such recommendations as the Commission may have for administrative or legislative action.\n**(2) Interim report**\nNot later than the date that is 1 year after the Commission establishment date specified in subsection (a)(2), the Commission shall submit to Congress and the President an interim report on the status of the review being carried out pursuant to subsection (e)(1), including a discussion of any interim recommendations legislative or administrative action the Commission may have.\n**(3) Form**\nEach report submitted to Congress under this subsection shall be submitted in unclassified form, but may include a classified annex.\n##### (g) Government cooperation\n**(1) Cooperation**\nIn carrying out its duties, the Commission shall receive the full and timely cooperation of the Secretary of Commerce and the heads of other Federal departments and agencies in providing the Commission with analysis, briefings, and other information necessary for the fulfillment of its responsibilities.\n**(2) Liaison**\nThe Secretary of Commerce shall designate at least 1 officer or employee of the Department of Commerce to serve as a liaison officer between the Department and the Commission.\n**(3) Detailees authorized**\nThe Secretary of Commerce and the heads of other departments and agencies of the Federal Government may provide, and the Commission may accept and employ, personnel detailed from the Department of Commerce and such other departments and agencies, without reimbursement.\n**(4) Facilitation**\n**(A) Independent, nongovernment institute**\nNot later than the date that is 45 days after the Commission establishment date specified in subsection (a)(2), the Secretary of Commerce may make available to the Commission the services of an independent, nongovernmental institute described in section 501(c)(3) of the Internal Revenue Code of 1986, and exempt from tax under section 501(a) of such Code, that has recognized credentials and expertise in quantum information science and associated technologies in order to facilitate the Commission\u2019s discharge of its duties under this section.\n**(B) Federally funded research and development center**\nOn request of the Commission, the Secretary of Commerce shall make available the services of a federally funded research and development center that is covered by a sponsoring agreement of the Department of Commerce in order to enhance the Commission\u2019s efforts to discharge its duties under this section.\n**(5) Expedition of security clearances**\nThe Office of Senate Security and the Office of House Security shall ensure the expedited processing of appropriate security clearances under processes developed for the clearance of legislative branch employees for any personnel appointed to the Commission by their respective offices of the Senate and House of Representatives and any personnel appointed by the Executive Director appointed under subsection (h).\n**(6) Services**\n**(A) Department of Commerce services**\nThe Secretary of Commerce may provide to the Commission, on a nonreimbursable basis, such administrative services, funds, staff, facilities, and other support services as are necessary for the performance of the Commission\u2019s duties under this section.\n**(B) Other agencies**\nIn addition to any support provided under paragraph (1), the heads of other Federal departments and agencies may provide to the Commission such services, funds, facilities, staff, and other support as the heads of such departments and agencies determine advisable and as may be authorized by law.\n##### (h) Staff\n**(1) Status as Federal employees**\nNotwithstanding the requirements of section 2105 of title 5, United States Code, including the required supervision under subsection (a)(3) of such section, any member of the Commission who is not a Member of Congress shall be considered to be a Federal employee.\n**(2) Executive director**\nThe Commission shall appoint and fix the rate of basic pay for an Executive Director in accordance with section 3161(d) of title 5, United States Code.\n**(3) Pay**\nThe Executive Director, with the approval of the Commission, may appoint and fix the rate of basic pay for additional personnel as staff of the Commission in accordance with section 3161(d) of title 5, United States Code.\n##### (i) Personal services\n**(1) Authority to procure**\nThe Commission may\u2014\n**(A)**\nprocure the services of experts or consultants (or of organizations of experts or consultants) in accordance with the provisions of section 3109 of title 5, United States Code; and\n**(B)**\npay in connection with such services travel expenses of individuals, including transportation and per diem in lieu of subsistence, while such individuals are traveling from their homes or places of business to duty stations.\n**(2) Maximum daily pay rates**\nThe daily rate paid an expert or consultant procured pursuant to paragraph (1) may not exceed the daily rate paid a person occupying a position at level IV of the Executive Schedule under section 5315 of title 5, United States Code.\n##### (j) Authority To accept gifts\nThe Commission may accept, use, and dispose of gifts or donations of services, goods, and property from non-Federal entities for the purposes of aiding and facilitating the work of the Commission. The authority in this subsection does not extend to gifts of money. Gifts accepted under this authority shall be documented, and conflicts of interest or the appearance of conflicts of interest shall be avoided. Subject to the authority in this section, members of the Commission shall otherwise comply with rules set forth by the Select Committee on Ethics of the Senate and the Committee on Ethics of the House of Representatives governing employees of the Senate and House of Representatives.\n##### (k) Legislative advisory committee\nThe Commission shall operate as a legislative advisory committee.\n##### (l) Contracting authority\nThe Commission may acquire administrative supplies and equipment for Commission use to the extent funds are available.\n##### (m) Use of government information\nThe Commission may secure directly from any department or agency of the Federal Government such information as the Commission considers necessary to carry out its duties. Upon such request of the chair of the Commission, the head of such department or agency shall furnish such information to the Commission.\n##### (n) Postal services\nThe Commission may use the United States mail in the same manner and under the same conditions as Federal departments and agencies.\n##### (o) Space for use of commission\nNot later than 30 days after the establishment date of the Commission, the Administrator of General Services, in consultation with the Commission, shall identify and make available suitable excess space within the Federal space inventory to house the operations of the Commission. If the Administrator is not able to make such suitable excess space available within such 30-day period, the Commission may lease space to the extent the funds are available.\n##### (p) Removal of members\nA member may be removed from the Commission for cause by the individual serving in the position responsible for the original appointment of such member under subsection (b)(1), provided that notice has first been provided to such member of the cause for removal and voted and agreed upon by \u00be of the members serving. A vacancy created by the removal of a member under this subsection shall not affect the powers of the Commission, and shall be filled in the same manner as the original appointment was made.\n##### (q) Termination\nThe Commission shall terminate on the date that is 540 days after the date on which it submits the final report required by subsection (f).",
      "versionDate": "2025-05-13",
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
        "actionDate": "2025-10-08",
        "text": "Referred to the House Committee on Science, Space, and Technology."
      },
      "number": "5712",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Quantum LEAP Act of 2025",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-30T13:11:57Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1746is.xml"
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
      "title": "Quantum LEAP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Quantum LEAP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Quantum Leadership in Emerging Applications and Policy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Commission on American Quantum Information Science Dominance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T01:03:30Z"
    }
  ]
}
```
