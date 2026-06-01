# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2121?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2121
- Title: Commission to Study the Creation of a National Museum of Irish American History
- Congress: 119
- Bill type: HR
- Bill number: 2121
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-08-27T08:05:24Z
- Update date including text: 2025-08-27T08:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-14 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-14 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2121",
    "number": "2121",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Commission to Study the Creation of a National Museum of Irish American History",
    "type": "HR",
    "updateDate": "2025-08-27T08:05:24Z",
    "updateDateIncludingText": "2025-08-27T08:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-14T13:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "N000015",
      "district": "1",
      "firstName": "Richard",
      "fullName": "Rep. Neal, Richard E. [D-MA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Neal",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "PA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MA"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "VA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NY"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "PA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NY"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "PA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "DE"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NV"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NJ"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2121ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2121\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Fitzpatrick (for himself, Mr. Neal , Mr. Kelly of Pennsylvania , Mr. McGovern , Mr. Moulton , Mr. Connolly , Mr. Lawler , Mr. Tonko , Mr. Keating , Ms. Scanlon , Mr. Suozzi , Mr. Deluzio , Ms. McBride , Ms. Lee of Nevada , and Mr. Kennedy of New York ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish the Commission to study the potential creation of a National Museum of Irish American History, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Commission to Study the Creation of a National Museum of Irish American History .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Commission to study the potential creation of a National Museum of Irish American History established by section 3(a).\n**(2) Museum**\nThe term Museum means the National Museum of Irish American History.\n#### 3. Establishment of commission\n##### (a) Establishment of commission\n**(1) In general**\nThere is established the Commission to study the potential creation of an Irish American Museum.\n**(2) Membership**\nThe Commission shall consist of 23 members appointed not later than 6 months after the date of the enactment of this Act as follows:\n**(A)**\nThe President shall appoint 7 voting members.\n**(B)**\nThe Speaker of the House of Representatives, the Minority Leader of the House of Representatives, the Majority Leader of the Senate, and the Minority Leader of the Senate shall each appoint\u2014\n**(i)**\n3 voting members; and\n**(ii)**\n1 nonvoting member.\n**(3) Qualifications**\nMembers of the Commission shall be chosen from individuals, or representatives of institutions or entities, who possess either\u2014\n**(A)**\na demonstrated commitment to the research, study, or promotion of Irish-American life, art, history, political or economic status, or culture, together with\u2014\n**(i)**\nexpertise in museum administration;\n**(ii)**\nexpertise in fundraising for nonprofit or cultural institutions;\n**(iii)**\nexperience in the study and teaching of Irish-American culture and history at the post-secondary level;\n**(iv)**\nexperience in studying the issue of the Smithsonian Institution\u2019s representation of Irish-American art, life, history, and culture; or\n**(v)**\nextensive experience in public or elected service; or\n**(B)**\nexperience in the administration of, or the planning for the establishment of, museums devoted to the study and promotion of the role of ethnic, racial, or cultural groups in American history.\n**(4) Vacancies**\nA vacancy in the Commission\u2014\n**(A)**\nshall not affect the powers of the Commission; and\n**(B)**\nshall be filled in the same manner as the original appointment was made.\n**(5) Chairperson**\nThe Commission shall, by majority vote of all of the members, select 1 member of the Commission to serve as the Chairperson of the Commission.\n#### 4. Duties of the commission\n##### (a) Reports\n**(1) Plan of action for the establishment and maintenance of museum**\nThe Commission shall submit a report to the President and the Congress containing its recommendations with respect to a plan of action for the establishment and maintenance of an Irish-American Museum in Washington, DC.\n**(2) Report on issues**\nThe Commission shall examine, in consultation with the Secretary of the Smithsonian Institution, and submit a report to the President and the Congress on the following issues:\n**(A)**\nThe availability and cost of collections to be acquired and housed in the Museum.\n**(B)**\nThe impact of the Museum on regional Irish-American-related museums.\n**(C)**\nPossible locations for the Museum in Washington, DC and its environs, to be considered in consultation with the National Capital Planning Commission and the Commission of Fine Arts, the Department of the Interior, and Smithsonian Institution.\n**(D)**\nWhether the Museum should be located within the Smithsonian Institution.\n**(E)**\nThe governance and organizational structure from which the Museum should operate.\n**(F)**\nHow to engage the Irish-American community in the development and design of the Museum.\n**(G)**\nThe cost of constructing, operating, and maintaining the Museum.\n##### (b) Fundraising plan\n**(1) In general**\nThe Commission shall develop a fundraising plan to support the establishment, operation, and maintenance of the Museum through contributions from the public.\n**(2) Considerations**\nIn developing the fundraising plan under paragraph (1), the Commission shall consider issues relating to funding the operations and maintenance of the Museum in perpetuity without reliance on appropriations of Federal funds.\n##### (c) Independent review\nThe Commission shall obtain an independent review of the viability of the plan developed under subsection (b)(1) and such review shall include an analysis as to whether the plan is likely to achieve the level of resources necessary to fund the construction of the Museum and the operations and maintenance of the Museum in perpetuity without reliance on appropriations of Federal funds.\n##### (d) Submission\nThe Commission shall submit the plan developed under subsection (b)(1) and the review conducted under paragraph (3) to the Committees on Transportation and Infrastructure, House Administration, Natural Resources, and Appropriations of the House of Representatives and the Committees on Rules and Administration, Energy and Natural Resources, and Appropriations of the Senate.\n##### (e) Recommendations for legislation To carry out plan of action\nBased on the recommendations contained in the report submitted under subsection (a), the Commission shall submit for consideration recommendations for a legislative plan of action to create and construct the Museum to\u2014\n**(1)**\nthe Committee on Transportation and Infrastructure of the House of Representatives;\n**(2)**\nthe Committee on House Administration of the House of Representatives;\n**(3)**\nthe Committee on Rules and Administration of the Senate;\n**(4)**\nthe Committee on Natural Resources of the House of Representatives;\n**(5)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(6)**\nthe Committees on Appropriations of the House of Representatives and the Senate.\n##### (f) Deadline for submission of reports\nThe Commission shall submit final versions of the reports and plans required\u2014\n**(1)**\nunder subsection (a) and (b) not later than 24 months after the date of the Commission\u2019s first meeting; and\n**(2)**\nunder subsection (e) not later than 12 months after the date that the reports and plans referred to in paragraph (1) are submitted.\n##### (g) National conference\nIn carrying out its functions under this section, not later than 18 months after the commission members are selected, the Commission may host a national conference on the Museum, comprised of individuals committed to the advancement of Irish-American life, art, history, and culture.\n#### 5. Director and staff of commission\n##### (a) Director and staff\n**(1) In general**\nThe Commission may employ and compensate an executive director and any other additional personnel that are necessary to enable the Commission to perform the duties of the Commission.\n**(2) Rates of pay**\nRates of pay for persons employed under paragraph (1) shall be consistent with the rates of pay allowed for employees of a temporary organization under section 3161 of title 5, United States Code.\n##### (b) Not federal employment\nAny individual employed under this Act shall not be considered a Federal employee for the purpose of any law governing Federal employment.\n##### (c) Technical assistance\n**(1) In general**\nSubject to paragraph (2), on request of the Commission the head of a Federal agency may provide technical assistance to the Commission.\n**(2) Detailees**\nNo Federal employees may be detailed to the Commission.\n#### 6. Administrative provisions\n##### (a) Compensation\n**(1) In general**\nA member of the Commission\u2014\n**(A)**\nshall not be considered to be a Federal employee for any purpose by reason of service on the Commission; and\n**(B)**\nshall serve without pay.\n**(2) Travel expenses**\nA member of the Commission shall be allowed a per diem allowance for travel expenses, at rates consistent with those authorized under subchapter I of chapter 57 of title 5, United States Code.\n##### (b) Gifts, bequests, devises\nThe Commission may solicit, accept, use, and dispose of gifts, bequests, or devises of money, services, or real or personal property for the purpose of aiding or facilitating the work of the Commission.\n##### (c) Federal advisory committee act\nThe Commission is not subject to the provisions of the Federal Advisory Committee Act.\n#### 7. Termination\nThe Commission shall terminate on the date that is 30 days after the date on which the final versions of the reports and plans required under section 4 are submitted.\n#### 8. Authorization for appropriations\nThere are authorized to be appropriated for carrying out the activities of the Commission\u2014\n**(1)**\n$2,100,000 for the first fiscal year beginning after the date of the enactment of this Act; and\n**(2)**\n$1,100,000 for the second fiscal year beginning after the date of the enactment of this Act.",
      "versionDate": "2025-03-14",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-04-01T11:26:45Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2121ih.xml"
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
      "title": "Commission to Study the Creation of a National Museum of Irish American History",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Commission to Study the Creation of a National Museum of Irish American History",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T06:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Commission to study the potential creation of a National Museum of Irish American History, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T06:18:33Z"
    }
  ]
}
```
