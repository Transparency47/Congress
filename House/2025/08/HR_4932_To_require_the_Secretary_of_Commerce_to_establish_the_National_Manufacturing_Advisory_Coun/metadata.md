# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4932?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4932
- Title: National Manufacturing Advisory Council for the 21st Century Act
- Congress: 119
- Bill type: HR
- Bill number: 4932
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2025-10-22T08:05:48Z
- Update date including text: 2025-10-22T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-08-08: Introduced in House

## Actions

- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4932",
    "number": "4932",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "National Manufacturing Advisory Council for the 21st Century Act",
    "type": "HR",
    "updateDate": "2025-10-22T08:05:48Z",
    "updateDateIncludingText": "2025-10-22T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:33:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "KS"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "RI"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4932ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4932\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Neguse (for himself and Mr. Mann ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Commerce to establish the National Manufacturing Advisory Council within the Department of Commerce, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Manufacturing Advisory Council for the 21st Century Act .\n#### 2. National Manufacturing Advisory Council\n##### (a) Definitions\nIn this section:\n**(1) Advisory Council**\nThe term Advisory Council means the National Manufacturing Advisory Council established under subsection (b).\n**(2) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate;\n**(B)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate;\n**(C)**\nthe Committee on Energy and Natural Resources of the Senate;\n**(D)**\nthe Committee on Armed Services of the Senate;\n**(E)**\nthe Committee on Appropriations of the Senate;\n**(F)**\nthe Committee on Small Business and Entrepreneurship of the Senate;\n**(G)**\nthe Committee on Energy and Commerce of the House of Representatives;\n**(H)**\nthe Committee on Education and Workforce of the House of Representatives;\n**(I)**\nthe Committee on Science, Space, and Technology of the House of Representatives;\n**(J)**\nthe Committee on Armed Services of the House of Representatives;\n**(K)**\nthe Committee on Appropriations of the House of Representatives; and\n**(L)**\nthe Committee on Small Business of the House of Representatives.\n**(3) Economically distressed area**\nThe term economically distressed area means an area that meets 1 or more of the requirements described in section 301(a) of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3161(a) ).\n**(4) Secretary**\nThe term Secretary means the Secretary of Commerce.\n##### (b) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary, in consultation with the Secretary of Labor, the Secretary of Defense, the Secretary of Energy, the United States Trade Representative, and the Secretary of Education, shall establish within the Department of Commerce the National Manufacturing Advisory Council.\n##### (c) Mission\nThe mission of the Advisory Council shall be to\u2014\n**(1)**\nprovide a forum for\u2014\n**(A)**\nregular communication between the Federal Government and the manufacturing sector, including manufacturing workers, in the United States; and\n**(B)**\ndiscussing and proposing solutions to problems relating to the manufacturing sector in the United States, including the manufacturing workforce, supply chain interruptions, and other logistical challenges;\n**(2)**\nadvise the Secretary regarding policies and programs of the Federal Government that affect manufacturing, including the manufacturing workforce, in the United States; and\n**(3)**\nannually produce a national strategic plan, as described in subsection (g), that provides recommendations to the Secretary and the appropriate committees of Congress regarding how to help the United States remain the preeminent destination throughout the world for investment in manufacturing, which shall be based on the execution of the duties of the Advisory Council.\n##### (d) Duties\nThe duties of the Advisory Council shall include the following:\n**(1)**\nMeeting not less frequently than once every 180 days, in a manner to be determined by the Secretary, in order to provide independent advice and recommendations to the Secretary regarding issues involving manufacturing in the United States.\n**(2)**\nIdentifying and assessing the impact that technological developments, critical production capacity, skill availability, investment patterns, and emerging defense needs have on the manufacturing competitiveness of the United States and providing advice and recommendations to the Secretary regarding that impact.\n**(3)**\nSoliciting input from the public and private sectors and academia relating to emerging trends in manufacturing, and the responsiveness of Federal programming with respect to manufacturing, and providing advice and recommendations to the Secretary for areas of increased Federal attention with respect to manufacturing.\n**(4)**\nIdentifying, and providing advice and recommendations to the Secretary regarding, global and domestic manufacturing trends and threats to the manufacturing sector in the United States, including on matters such as supply chain interruptions, logistical challenges, and technological changes affecting the manufacturing base in the United States.\n**(5)**\nProviding advice and recommendations to the Secretary on matters relating to investment in, and support of, the manufacturing workforce in the United States, including on matters such as\u2014\n**(A)**\nworker participation, including through labor organizations and through other methods determined by the Advisory Council, in planning for the deployment of new technologies across the manufacturing sector in the United States and within workplaces in that sector;\n**(B)**\ntraining and education priorities for the Federal Government and employers to assist workers in adapting the skills and experiences of those workers to fit the demands of the manufacturing sector in the United States in the 21st century;\n**(C)**\nhow the development of new technologies and processes have impacted, and will impact, the manufacturing workforce of the United States and the economy of the United States, which shall be based on input from manufacturing workers;\n**(D)**\nmanagement practices in the manufacturing sector in the United States that lead to worker employment, job quality, worker protection, worker participation and power in decision making, and investment in worker career success;\n**(E)**\npolicies and procedures that expand access to jobs, career advancement opportunities, and management opportunities for underrepresented populations; and\n**(F)**\nhow to improve access to demand-driven manufacturing-related education, training, and re-training for workers, including at community and technical colleges, through other institutions of higher education, and through apprenticeships and work-based learning opportunities.\n**(6)**\nProviding recommendations to the Secretary on ways to\u2014\n**(A)**\nprovide\u2014\n**(i)**\nmanufacturing-related worker education, training, and development; and\n**(ii)**\nentrepreneurship training relating to manufacturing;\n**(B)**\nconnect individuals and businesses with services described in subparagraph (A) that are offered in the communities of those individuals or businesses;\n**(C)**\ncoordinate services relating to manufacturing employee engagement, including employee ownership and workforce training;\n**(D)**\nconnect manufacturers with community and technical colleges, other institutions of higher education, State or local workforce development boards established under section 101 or 107 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3111 , 3122), labor organizations, and nonprofit job training providers to develop and support training and job placement services, and apprenticeship and online learning platforms, for new and incumbent manufacturing workers;\n**(E)**\ndevelop programming to prevent manufacturing job losses in the United States as entities adopt new technologies and processes; and\n**(F)**\ndevelop best practices for manufacturers to incorporate, or transition to, employee ownership structures.\n**(7)**\nWith respect to the matters described in paragraphs (1) through (6), soliciting input from\u2014\n**(A)**\neconomically distressed areas; and\n**(B)**\nareas of the United States in which foreign competition has resulted in mass layoffs in the manufacturing sector.\n**(8)**\nCompleting other specific tasks requested by the Secretary.\n##### (e) Membership\n**(1) In general**\nThe Advisory Council shall\u2014\n**(A)**\nconsist of individuals appointed by the Secretary with a balance of backgrounds, experiences, and viewpoints; and\n**(B)**\ninclude individuals with manufacturing experience who represent\u2014\n**(i)**\nprivate industry, including small and medium-sized manufacturers and any relevant standards development organizations or relevant trade associations;\n**(ii)**\nacademia; and\n**(iii)**\nlabor.\n**(2) Public participation**\nThe Secretary shall, to the maximum extent practicable, accept recommendations from the public regarding the appointment of individuals under paragraph (1).\n**(3) Period of appointment; vacancies**\n**(A) In general**\nEach member of the Advisory Council shall be appointed by the Secretary for a term of 3 years.\n**(B) Renewal**\nThe Secretary may renew an appointment made under subparagraph (A) for not more than 2 additional terms.\n**(C) Stagger terms**\nThe Secretary may stagger the terms of the members of the Advisory Council to ensure that the terms of those members expire during different years.\n**(D) Vacancies**\n**(i) In general**\nSubject to clause (ii), a member appointed to fill a vacancy on the Advisory Council occurring before the expiration of the term for which the predecessor of the newly appointed member was appointed shall be appointed only for the remainder of that term of the predecessor.\n**(ii) Further service**\nA member of the Advisory Council who is appointed for the remainder of a term of a predecessor under clause (i) may serve after the expiration of that term of the predecessor and until the date on which the Secretary has appointed a successor.\n##### (f) Transfer of functions\n**(1) In general**\nAll functions of the United States Manufacturing Council of the International Trade Administration of the Department of Commerce, including the personnel, assets, and obligations of the United States Manufacturing Council of the International Trade Administration of the Department of Commerce, as in existence on the day before the date of enactment of this Act, shall be transferred to the Advisory Council.\n**(2) Deeming of name**\nAny reference in any law, regulation, document, paper, or other record of the United States to the United States Manufacturing Council of the International Trade Administration of the Department of Commerce shall be deemed a reference to the Advisory Council.\n**(3) Unexpended balances**\nUnexpended balances of appropriations, authorization, allocations, or other funds related to the United States Manufacturing Council of the International Trade Administration of the Department of Commerce shall be available for use by the Advisory Council for the purpose for which the appropriations, authorizations, allocations, or other funds were originally made available.\n**(4) Existing advisory committee**\nAny Federal advisory committee of the Department of Commerce that is operating on the day before the date of enactment of this Act under a charter filed in accordance with section 1008(c) of title 5, United States Code, for the purpose of addressing the purposes and duties described in this section shall satisfy the requirement under subsection (b) to establish the Advisory Council if, not later than 90 days after that date of enactment, the Federal advisory committee is modified, as necessary, to comply with the requirements of this section.\n##### (g) National strategic plan\nNot later than 180 days after the date on which the Advisory Council holds the initial meeting of the Advisory Council, and annually thereafter, the Advisory Council shall submit to the Secretary and the appropriate committees of Congress\u2014\n**(1)**\na national strategic plan for manufacturing in the United States that is based on the execution of the duties of the Advisory Council under subsection (d); and\n**(2)**\na detailed statement of the activities that the Advisory Council conducted to carry out the duties of the Advisory Council under subsection (d).\n##### (h) Departmental support\nIn accordance with prevailing laws and regulations, the Secretary, as the Secretary considers appropriate, shall furnish to the Advisory Council relevant information that\u2014\n**(1)**\nis in the possession of the Department of Commerce; and\n**(2)**\nrelates to the mission of the Advisory Council.\n##### (i) Inapplicability of certain provisions\nChapter 10 of title 5, United States Code, shall not apply with respect to the Advisory Council or the activities of the Advisory Council.\n##### (j) Sunset\nThe Advisory Council shall terminate on September 30 of the fifth year after the year in which the Advisory Council holds the first meeting of the Advisory Council.",
      "versionDate": "2025-08-08",
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
        "name": "Commerce",
        "updateDate": "2025-09-18T19:55:58Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4932ih.xml"
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
      "title": "National Manufacturing Advisory Council for the 21st Century Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Manufacturing Advisory Council for the 21st Century Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Commerce to establish the National Manufacturing Advisory Council within the Department of Commerce, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T04:18:39Z"
    }
  ]
}
```
