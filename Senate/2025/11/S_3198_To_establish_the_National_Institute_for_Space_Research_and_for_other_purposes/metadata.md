# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3198?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3198
- Title: Space RACE Act
- Congress: 119
- Bill type: S
- Bill number: 3198
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2025-12-18T15:36:03Z
- Update date including text: 2025-12-18T15:36:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3198",
    "number": "3198",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Space RACE Act",
    "type": "S",
    "updateDate": "2025-12-18T15:36:03Z",
    "updateDateIncludingText": "2025-12-18T15:36:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:44:58Z",
          "name": "Referred To"
        }
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CO"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "MS"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NM"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3198is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3198\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. Cornyn (for himself, Mr. Hickenlooper , Mr. Wicker , Mr. Luj\u00e1n , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish the National Institute for Space Research, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Space Research And Continuing Exploration Act or Space RACE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the National Aeronautics and Space Administration.\n**(2) Institute**\nThe term Institute means the National Institute for Space Research established under section 3.\n**(3) ISS**\nThe term ISS means the International Space Station.\n**(4) Microgravity research**\nThe term microgravity research means research and development conducted while in orbit in space.\n**(5) Qualified national microgravity project**\nThe term qualified national microgravity project \u2014\n**(A)**\nmeans a project led by a nongovernmental entity using a next-generation microgravity platform that reflects 1 or more microgravity research and development priorities of the United States Government, as identified by the Institute; and\n**(B)**\nincludes a project with United States Government funding or subsidy that\u2014\n**(i)**\nis led by 1 or more\u2014\n**(I)**\ninstitutions of higher education (as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ));\n**(II)**\nstudents; or\n**(III)**\nnonprofit organizations; or\n**(ii)**\nis\u2014\n**(I)**\na commercial venture; or\n**(II)**\na joint project with the United States Government, of which the United States Government\u2014\n**(aa)**\nis not the lead party for the project; and\n**(bb)**\nserves in a supporting role.\n**(6) Research project**\nThe term research project means an in-space research and development project that\u2014\n**(A)**\nuses a next-generation microgravity platform;\n**(B)**\nreflects national priorities of the United States; and\n**(C)**\nis led, funded, or sponsored by a department or agency of the United States Government other than the National Aeronautics and Space Administration.\n**(7) Special Government employee**\nThe term special Government employee has the meaning given the term in section 202(a) of title 18, United States Code, except that for purposes of this Act, such an employee may be retained, designated, appointed, or employed to perform, with or without compensation, for more than 130 days during a 365-day period.\n#### 3. National Institute for Space Research\n##### (a) Establishment\nNot earlier than January 1, 2026, and subject to appropriations, the Administrator may establish a National Institute for Space Research, which shall be operated by a non-Federal entity under a contractual agreement with the Administrator, to support\u2014\n**(1)**\nthe use of in-space research and development capabilities and facilities available on next-generation microgravity platforms;\n**(2)**\nthe use of in-space research and development capabilities for United States national security purposes;\n**(3)**\nthe United States microgravity ecosystem in preparation for the decommissioning of the ISS;\n**(4)**\neducation and workforce development in the United States with respect to space research; and\n**(5)**\nthe transition of United States microgravity research and development from the ISS to next-generation microgravity platforms.\n##### (b) Board of Directors\n**(1) In general**\nThe Institute shall have a Board of Directors (referred to in this section as the Board ).\n**(2) Membership**\nThe Board shall be composed of the following:\n**(A)**\nAn employee of the National Aeronautics and Space Administration, who shall\u2014\n**(i)**\nbe appointed by the Administrator; and\n**(ii)**\nserve as Chairperson of the Board.\n**(B)**\nAn employee of the Office of Science and Technology Policy, appointed by the Science Advisor to the President.\n**(C)**\nAn employee of the Department of Commerce, appointed by the Secretary of Commerce, to represent perspectives of the National Institute of Standards and Technology and the National Oceanic and Atmospheric Administration.\n**(D)**\nAn employee of the Department of Education, appointed by the Secretary of Education.\n**(E)**\nAn employee of the National Science Foundation, appointed by the Director of the National Science Foundation.\n**(F)**\nAn employee of the National Institutes of Health, appointed by the Director of the National Institutes of Health.\n**(G)**\nAn employee appointed by the President of the National Academy of Sciences and who shall be considered a special government employee.\n**(H)**\nAn employee of the Food and Drug Administration, appointed by the Commissioner of the Food and Drug Administration.\n**(I)**\nAn employee of the Department of Energy, appointed by the Secretary of Energy.\n**(J)**\nAn employee of the Department of Defense, appointed by the Secretary of Defense.\n**(K)**\nA qualified scientist with professional experience in space research and development, who shall be\u2014\n**(i)**\nappointed by the Chairperson; and\n**(ii)**\nconsidered a special Government employee.\n**(L)**\nA qualified professional with executive management experience in the aerospace industry, who shall be\u2014\n**(i)**\nappointed by the Chairperson; and\n**(ii)**\nconsidered a special government employee.\n**(3) Terms**\nA member of the Board shall be appointed for a term of 6 years, except that of the members first appointed, so as to stagger the terms\u2014\n**(A)**\nthe Chairperson shall be appointed for a term of 6 years;\n**(B)**\neach member appointed under subparagraphs (B) through (E) of paragraph (2) shall be appointed for a term of 2 years;\n**(C)**\neach member appointed under subparagraphs (F) through (J) of paragraph (2) shall be appointed for a term of 4 years; and\n**(D)**\neach remaining member shall be appointed for a term of 6 years.\n**(4) Conflicts of interest**\n**(A) In general**\nNo member of the Board shall have a financial interest (including an employment relationship) in an entity seeking a grant or cooperative agreement under this section.\n**(B) Code of conduct**\nThe Board shall establish a code of conduct to govern the behavior of the Board, which shall\u2014\n**(i)**\ninclude avoidance of conflicts of interest; and\n**(ii)**\nuse the Federal Standards of Conduct for all members of the Board.\n**(5) Vacancies**\n**(A) In general**\nIn the case of a vacancy on the Board, not later than 90 days after the vacancy occurs, the vacancy shall be filled in the manner in which the original appointment was made.\n**(B) Filling unexpired term**\nAn individual chosen to fill a vacancy shall be appointed for the unexpired term of the member replaced.\n**(6) Duties**\n**(A) In general**\nThe duties of the Board shall be\u2014\n**(i)**\nto develop all budget requests, policies, and standard operating procedures of the Institute;\n**(ii)**\nto supervise the operations of the Institute;\n**(iii)**\nto appoint and supervise an Executive Director for the Institute;\n**(iv)**\nto set research priorities for the Institute; and\n**(v)**\nfor fiscal year 2028 and each fiscal year thereafter, to submit to the appropriate committees of Congress a budget request for Institute operations, including grants or cooperative agreements under subsection (e).\n**(B) Appropriate committees of Congress defined**\nIn this paragraph, the term appropriate committees of Congress means\u2014\n**(i)**\nthe Committee on Appropriations and the Committee on Commerce, Science, and Transportation of the Senate; and\n**(ii)**\nthe Committee on Appropriations and the Committee on Science, Space, and Technology of the House of Representatives.\n**(7) Prohibition on use of funds for compensation**\nNone of the amounts made available for the Institute may be used to provide compensation to any member of the Board.\n**(8) Rule of construction**\nNothing in this section may be construed to authorize the Institute to regulate, review, or otherwise oversee a microgravity project of an private entity unless the private entity is a recipient of Federal funds.\n##### (c) Executive Director\n**(1) In general**\nThe Institute shall be headed by an Executive Director, who\u2014\n**(A)**\nshall be knowledgeable in matters relating to microgravity research opportunities;\n**(B)**\nshall be appointed and supervised by the Board; and\n**(C)**\nshall serve at the pleasure of the Board until such time as the Board considers appropriate.\n**(2) Appointment**\nIn making an appointment for the Executive Director, the Board shall consider an individual's technical qualifications, professional standing, and demonstrated knowledge in the field of health, advanced manufacturing, research, or engineering.\n**(3) Duties**\nThe Executive Director shall\u2014\n**(A)**\nensure the efficient and transparent implementation of this Act; and\n**(B)**\nin coordination with the Board, carry out activities of the Institute.\n**(4) Appointment of staff**\nThe Executive Director may enter into a contract with a nongovernmental entity to staff additional personnel to implement and oversee the activities carried out by the Institute under subsection (d).\n**(5) Compensation**\nThe Chairperson of the Board may fix the compensation of the Executive Director.\n##### (d) Activities\nThe Institute shall\u2014\n**(1)**\nidentify, publish, and maintain a current list of next-generation microgravity platforms available for use by the Institute;\n**(2)**\ndevelop and implement guidelines and project selection criteria, and engage with relevant entities, for use of next-generation microgravity platforms by all microgravity research projects and qualified national microgravity projects of Government agencies;\n**(3)**\nprovide competitively awarded grants or cooperative agreements to facilitate the development of research projects and qualified national microgravity projects, with matching funds, as described in subsection (e);\n**(4)**\nfacilitate cooperation among the National Aeronautics and Space Administration, other Government departments and agencies, the States, and academia so as to ensure the enhancement and sustained operations of the Institute;\n**(5)**\ncoordinate flight opportunities on next-generation microgravity platforms, subject to the availability of appropriations, for any research project or qualified national microgravity project\u2014\n**(A)**\nconsidered to be sensitive to the national interest of the United States; and\n**(B)**\nthat reflects the microgravity priorities of the United States; and\n**(6)**\ncoordinate with the National Aeronautics and Space Administration, the ISS National Laboratory, next-generation microgravity platform providers, and researchers to gather lessons learned that may be used to support the transition of United States microgravity research and development from the ISS National Laboratory to a new structure.\n##### (e) Grants or cooperative agreements\n**(1) Coordination of projects**\nThe Institute, in coordination with Government entities represented on the Board, shall coordinate microgravity research projects and qualified national microgravity projects on next generation microgravity platforms.\n**(2) Award of grants**\nSubject to the availability appropriations, the Institute may award any appropriated grants to, or enter into cooperative agreements with, eligible entities on a competitive basis for the purpose of conducting microgravity research and development projects using next-generation microgravity platforms.\n**(3) Applications**\n**(A) Submission of materials**\n**(i) In general**\nAn entity seeking a grant under this subsection for any research project or qualified national microgravity project shall submit to the Institute an application at such time, in such a manner, and containing such information as may be reasonably required and made available to the public on the internet website of the Institute\n**(ii) Exception**\nWith respect to a proposed research project or qualified national microgravity project for which a entity submits an application under this subsection, the Institute shall not make application information available to the public under clause (i) if\u2014\n**(I)**\ndisclosure of such information presents a national security risk; or\n**(II)**\nthe application contains proprietary information.\n**(B) Contents**\nTo be approved for a grant under this subsection, an application for proposed project shall demonstrate the manner in which the project advances sound scientific principles and aligns with the national scientific priorities and interests of the Government.\n**(4) Eligible entities**\nEntities eligible for a grant under this subsection include domestic\u2014\n**(A)**\npublic entities;\n**(B)**\nprivate entities;\n**(C)**\nnonprofit organizations; and\n**(D)**\nfor-profit organizations.\n**(5) Partnerships**\nThe Institute, in consultation with the Board, may partner with Government entities to co-fund (or otherwise support grants awarded by other Government entities), on a competitive basis and subject to the availability of appropriations, research projects and qualified national microgravity projects for the purpose of promoting microgravity research and development projects using next-generation microgravity platforms.\n**(6) Use of next-generation microgravity platforms**\n**(A) In general**\nThe recipient of a grant under this subsection may contract with any next-generation microgravity platform unless the Board determines that the project concerned is sensitive to the national interest of the United States.\n**(B) Coordination**\n**(i) In general**\nIn the case of a determination that such a project is sensitive to the national interest of the United States, in the Administrator shall coordinate with the grant recipient and the Institute to allow the grant recipient to use the allocated crew time of the National Aeronautics and Space Administration onboard a next-generation microgravity platform, as available.\n**(ii) Limitation**\nUse by a grant recipient of allocated crew time under clause (i) may exceed 50 percent of such crew time.\n**(7) Federal grants and consultation**\nThe head of a Government agency may\u2014\n**(A)**\nwithin an appropriated grant, award to the Institute or an eligible entity described in paragraph (3) 1 or more subgrants for space research; and\n**(B)**\nconsult with the Institute for technical assistance, enter into a partnership with the Institute, and coordinate with the Institute for purposes of evaluate microgravity research and development projects.\n##### (f) Prohibition on interference with Government-Funded activities\nNotwithstanding any other provision of law, the Institute shall not interfere with any agreement between the United States Government and a microgravity platform provider with respect to the conduct of research and development activities in partnership with any Federal entity other than the Institute.\n##### (g) Minimizing costs, constraints and burdens on other activities\nThe Institute shall, to the extent practicable, implement a policy that seeks to administer the activities of the Institute in a manner that places minimal costs, constraints, and burdens on other authorized activities.\n##### (h) Rule of construction\nNotwithstanding any other provision of law, nothing in this section may be construed to constrain a department or agency of the United States Government from entering into an agreement with a next-generation microgravity platform provider other than through a grant provided by the Institute.\n##### (i) Funds authorized\n**(1) In general**\nThe Administrator is authorized to provide funds for the implementation of the activities described in this section, subject to appropriations and compliance with this Act.\n**(2) Administrative expenses**\nNot more than 5 percent of the amounts provided pursuant to paragraph (1) may be used for administrative expenses of the Institute, including staff salaries.\n#### 4. ISS national laboratory and ISS cooperative agreement\nNot later than 180 days after ISS research operations have ceased, the Administrator shall terminate the ISS National Laboratory and the cooperative agreement with the ISS management entity under section 504(a) of the National Aeronautics and Space Administration Authorization Act of 2010 ( 42 U.S.C. 18354(a) ).",
      "versionDate": "2025-11-19",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-18T15:36:03Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3198is.xml"
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
      "title": "Space RACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T04:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Space RACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Space Research And Continuing Exploration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the National Institute for Space Research, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T04:18:26Z"
    }
  ]
}
```
