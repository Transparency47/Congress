# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1457?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1457
- Title: IDs for an Inclusive Democracy Act
- Congress: 119
- Bill type: HR
- Bill number: 1457
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-04-17T08:07:03Z
- Update date including text: 2026-04-17T08:07:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1457",
    "number": "1457",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "IDs for an Inclusive Democracy Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:03Z",
    "updateDateIncludingText": "2026-04-17T08:07:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:37:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "PA"
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
      "sponsorshipDate": "2025-02-21",
      "state": "PA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "MI"
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
      "sponsorshipDate": "2025-02-21",
      "state": "PA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "IL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MI"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1457ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1457\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Casten (for himself, Ms. Lee of Pennsylvania , Ms. Scanlon , Mr. Thanedar , Mr. Deluzio , Ms. Kelly of Illinois , and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the Commissioner of the Social Security Administration to produce and make available at no cost to certain individuals in the United States an identification for the purpose of allowing such individuals to meet certain identification requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the IDs for an Inclusive Democracy Act .\n#### 2. Federal identification cards\n##### (a) In general\nNot later than 3 years after the date of the enactment of this Act, the Commissioner of the Social Security Administration shall produce and make available at no cost to individuals in the United States who submit an application under subsection (f) an identification pursuant to the requirements in the report issued by the Task Force on Federal Identification Cards under section 3(i) that can be presented by such individuals to satisfy certain identification requirements.\n##### (b) Use of identification\nWith respect to an individual, the identification described in subsection (a) shall be deemed sufficient to satisfy identification requirements to the same extent and for the same purposes that any driver\u2019s license or identification card issued by a State is accepted to satisfy such requirements.\n##### (c) Content of identification\nWith respect to an individual, the identification described in subsection (a) shall include\u2014\n**(1)**\nthe full name of the individual;\n**(2)**\nthe date of birth of the individual;\n**(3)**\nthe gender of the individual, which shall include an option for male, female, and X (representing an unspecified or other gender identity), as attested by the individual;\n**(4)**\na photograph of the individual;\n**(5)**\na unique identification number;\n**(6)**\nthe date the identification was issued to the individual; and\n**(7)**\nthe date on which the identification is no longer valid.\n##### (d) Security features of identification\nThe identification described in subsection (a) shall include\u2014\n**(1)**\nphysical security features to make the identification resistant to tampering, counterfeiting, duplicating, and fraudulent use; and\n**(2)**\ncommon machine-readable identity information based on defined minimum data elements as determined by the Task Force on Federal Identification Cards established under section 3(a) .\n##### (e) Period of validity of identification\n**(1) In general**\nExcept as provided in paragraph (2) , with respect to an individual, the identification described in subsection (a) shall be valid for the 10-year period which begins on the date the identification is issued by the Commissioner of the Social Security Administration to the individual.\n**(2) Special rule for certain individuals**\nNotwithstanding paragraph (1) , in the case of an individual with a valid identification\u2014\n**(A)**\nwho is under the age of 18, such identification shall only be valid during the period beginning on the date the identification is issued to the individual and ending on the date the individual reaches the age of 18, after which the individual may submit an application for a renewal under subsection (f)(2) ; and\n**(B)**\nwho reaches 65 years of age or older during the period the identification is valid, the identification of such individual shall be deemed valid upon the expiration of the 10-year validity period for such identification without requiring a renewal of such identification.\n##### (f) Eligibility requirements\n**(1) In general**\nTo receive an identification under this section, an individual who is at least 14 years of age or older shall submit an application at such time and containing such information as the Task Force on Federal Identification Cards established under section 3(a) determines appropriate.\n**(2) Renewal application**\nTo receive a renewal of the identification described in subsection (a) , an individual shall submit an application at such time and containing such information as the Task Force on Federal Identification Cards established under section 3(a) determines appropriate, except that an individual shall not be required to provide documents that include the personally identifiable information of such individual unless any of such personally identifiable information has changed with respect to the most recent application submitted by the individual.\n##### (g) Public education campaign\nNot later than 6 months before the date the identification is made available to individuals under subsection (a) , the Commissioner of the Social Security Administration shall develop and implement a campaign to educate the public with respect to the identification described in subsection (a) , including how an individual can receive and use such an identification to satisfy certain identification requirements.\n##### (h) Postal Service application process\n**(1) In general**\nNot later than 2 years after the date of the enactment of this Act, the Postmaster General of the United States Postal Service shall, in consultation with the Commissioner of the Social Security Administration, develop and implement a process pursuant to the requirements of paragraph (2) that enables individuals to apply for the identification described in subsection (a) through the United States Postal Service, including a process with respect to an application for a first-time identification and a renewal of such identification, which shall be modeled after the process with respect to applications for a passport through the Postal Service.\n**(2) Process requirements**\nThe process developed under paragraph (1) shall include, with respect to an individual, an option to\u2014\n**(A)**\nreceive full service at a post office location, including by providing photography services at no cost to the individual;\n**(B)**\nsubmit an application online through the website of the Postal Service;\n**(C)**\nmail a written application described in subsection (f) through the mail service of the Postal Service at no cost to the individual; and\n**(D)**\nwith respect to an approved identification of an individual, receive such identification through mail service to the individual\u2019s address or a post office location, at the option of the individual.\n##### (i) State defined\nIn this section, the term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.\n#### 3. Task Force on Federal Identification Cards\n##### (a) Establishment\nThere is established a Task Force on Federal Identification Cards (in this section referred to as the Task Force ) for the purpose of determining the requirements to produce and make available the identification described in section 2(a) .\n##### (b) Membership\nThe Task Force shall be composed of at least 9 members as follows:\n**(1)**\nThe Commissioner of the Social Security Administration.\n**(2)**\nAt least 1 representative from the Election Assistance Commission.\n**(3)**\nAt least 1 representative from the Domestic Policy Council.\n**(4)**\nAt least 1 representative from the United States Postal Service.\n**(5)**\nAt least 1 representative from the Consumer Financial Protection Bureau.\n**(6)**\nAt least 1 representative from the Department of Housing and Urban Development.\n**(7)**\nAt least 1 representative from the Department of Education.\n**(8)**\nAt least 1 representative from the Department of Labor.\n**(9)**\nAt least 1 representative from the Department of Veterans Affairs.\n**(10)**\nThe Commissioner of the Social Security Administration, in collaboration with the representatives described in paragraphs (2) through (9), may appoint such other individuals with relevant expertise or experience as the Task Force shall determine appropriate and the Task Force shall, with respect to any such appointees, make efforts to ensure that populations that have been disproportionately affected by the lack of access to identification are represented.\n##### (c) Deadline for appointment\nAll appointments to the Task Force shall be made not later than 8 months after the date of the enactment of this Act.\n##### (d) Vacancies\nAny vacancy in the Task Force shall be filled in the same manner as the original appointment.\n##### (e) Prohibition on compensation of Federal employees\nMembers of the Task Force who are full-time officers or employees of the United States may not receive additional pay, allowances, or benefits by reason of their service on the Task Force.\n##### (f) Travel expenses\nExcept as provided in subsection (e) , each member shall receive travel expenses, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter I of chapter 57 of title 5, United States Code.\n##### (g) Support staff; administrative services\n**(1) Support staff**\nThe Commissioner of the Social Security Administration, any representatives from the Election Assistance Commission, and any representatives from the Domestic Policy Council shall provide support staff for the Task Force.\n**(2) Administrative services**\nUpon the request of the Task Force, the Commissioner of the Social Security Administration, any representatives from the Election Assistance Commission, and any representatives from the Domestic Policy Council shall provide any information, administrative services, and supplies that such Commissioner and representatives jointly consider necessary for the Task Force to carry out its duties under this section.\n##### (h) Nonapplicability of Federal Advisory Committee Act\nThe Federal Advisory Committee Act (5 U.S.C. App.) shall not apply to the Task Force.\n##### (i) Report on requirements for producing and making identifications available\n**(1) Report**\nNot later than 1 year after the date of the enactment of this Act, the Task Force shall issue a report regarding the requirements to produce and make available the identification described in section 2(a) .\n**(2) Prohibiting unauthorized disclosure of information**\nThe Task Force shall include in the report issued under this subsection a requirement that the Commissioner of Social Security and the Postmaster General shall establish procedures to prevent the unauthorized disclosure of any information obtained with respect to individuals who seek assistance in obtaining the identification described in section 2(a).\n##### (j) Development of voluntary best practices\nNot later than 1 year after the date of the enactment of this Act, the Task Force shall develop and publish recommendations for voluntary best practices for nonprofit organizations and entities that provide services to vulnerable populations with respect to how such organizations and entities can assist individuals to obtain the identification described in section 2(a) , which shall include\u2014\n**(1)**\nrecommendations with respect to how such organizations and entities can provide full service to individuals to obtain such identification; and\n**(2)**\nrecommendations to minimize the barriers faced by such individuals, including individuals from groups which have been disproportionately affected by the lack of access to identification, in obtaining documentation of the information necessary to obtain the identification.\n##### (k) Termination\nThe Task Force shall terminate on the date the identification is made available to individuals under section 2(a) .\n#### 4. Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out this Act.",
      "versionDate": "2025-02-21",
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
            "name": "Advisory bodies",
            "updateDate": "2025-07-22T13:22:46Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-22T13:22:38Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-07-22T13:22:51Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-07-22T13:22:42Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2025-07-22T13:22:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-05-02T14:57:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1457",
          "measure-number": "1457",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-08-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1457v00",
            "update-date": "2025-08-12"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>IDs for an Inclusive Democracy Act</strong></p><p>This bill directs the Social Security Administration (SSA) to produce and make available at no cost to individuals over the age of 14 a\u00a0means of\u00a0identification (ID) sufficient to satisfy certain identification requirements (i.e., requirements otherwise satisfied by a driver's license or state ID).</p><p>The ID must include a photograph, specified information, and certain security features, and must generally be valid for 10 years.</p><p>SSA must develop and implement a campaign to educate the public about the ID, including how an individual can obtain and use one.</p><p>The U.S. Postal Service (USPS)\u00a0must develop and implement a process that enables individuals to apply for and renew an ID through USPS, modeled after the process for passport applications.</p><p>The bill also establishes a task force to set forth requirements for the production and distribution of the new IDs. The task force must (1) issue a report outlining such requirements, including procedures to prevent the unauthorized disclosure of any information obtained from applicants seeking assistance with the ID process; and (2) develop and publish voluntary best practices for nonprofit organizations and entities that serve vulnerable populations on assisting individuals with the application process.</p>"
        },
        "title": "IDs for an Inclusive Democracy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1457.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>IDs for an Inclusive Democracy Act</strong></p><p>This bill directs the Social Security Administration (SSA) to produce and make available at no cost to individuals over the age of 14 a\u00a0means of\u00a0identification (ID) sufficient to satisfy certain identification requirements (i.e., requirements otherwise satisfied by a driver's license or state ID).</p><p>The ID must include a photograph, specified information, and certain security features, and must generally be valid for 10 years.</p><p>SSA must develop and implement a campaign to educate the public about the ID, including how an individual can obtain and use one.</p><p>The U.S. Postal Service (USPS)\u00a0must develop and implement a process that enables individuals to apply for and renew an ID through USPS, modeled after the process for passport applications.</p><p>The bill also establishes a task force to set forth requirements for the production and distribution of the new IDs. The task force must (1) issue a report outlining such requirements, including procedures to prevent the unauthorized disclosure of any information obtained from applicants seeking assistance with the ID process; and (2) develop and publish voluntary best practices for nonprofit organizations and entities that serve vulnerable populations on assisting individuals with the application process.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hr1457"
    },
    "title": "IDs for an Inclusive Democracy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>IDs for an Inclusive Democracy Act</strong></p><p>This bill directs the Social Security Administration (SSA) to produce and make available at no cost to individuals over the age of 14 a\u00a0means of\u00a0identification (ID) sufficient to satisfy certain identification requirements (i.e., requirements otherwise satisfied by a driver's license or state ID).</p><p>The ID must include a photograph, specified information, and certain security features, and must generally be valid for 10 years.</p><p>SSA must develop and implement a campaign to educate the public about the ID, including how an individual can obtain and use one.</p><p>The U.S. Postal Service (USPS)\u00a0must develop and implement a process that enables individuals to apply for and renew an ID through USPS, modeled after the process for passport applications.</p><p>The bill also establishes a task force to set forth requirements for the production and distribution of the new IDs. The task force must (1) issue a report outlining such requirements, including procedures to prevent the unauthorized disclosure of any information obtained from applicants seeking assistance with the ID process; and (2) develop and publish voluntary best practices for nonprofit organizations and entities that serve vulnerable populations on assisting individuals with the application process.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hr1457"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1457ih.xml"
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
      "title": "IDs for an Inclusive Democracy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T13:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "IDs for an Inclusive Democracy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Commissioner of the Social Security Administration to produce and make available at no cost to certain individuals in the United States an identification for the purpose of allowing such individuals to meet certain identification requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:18:20Z"
    }
  ]
}
```
