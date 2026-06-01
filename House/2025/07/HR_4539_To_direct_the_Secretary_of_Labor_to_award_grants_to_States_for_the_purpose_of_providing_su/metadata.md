# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4539?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4539
- Title: Texture Positive Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4539
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2025-09-11T17:08:12Z
- Update date including text: 2025-09-11T17:08:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4539",
    "number": "4539",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "V000081",
        "district": "7",
        "firstName": "Nydia",
        "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
        "lastName": "Vel\u00e1zquez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Texture Positive Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-11T17:08:12Z",
    "updateDateIncludingText": "2025-09-11T17:08:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
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
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:03:40Z",
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
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NJ"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "WA"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "DC"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4539ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4539\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Ms. Vel\u00e1zquez (for herself, Mrs. Cherfilus-McCormick , Ms. S\u00e1nchez , Mrs. McIver , Ms. Strickland , Mr. Meeks , Ms. Norton , Mr. Espaillat , Mr. Johnson of Georgia , Ms. Kamlager-Dove , Ms. Crockett , and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Labor to award grants to States for the purpose of providing subgrants to eligible entities for education and technical training on how to perform cosmetology services on textured hair.\n#### 1. Short title\nThis Act may be cited as the Texture Positive Act of 2025 .\n#### 2. Grants for education and technical training on textured hair\n##### (a) Grants authorized\nThe Secretary shall award, on a competitive basis, grants to States for the purpose of awarding subgrants in accordance with this section.\n##### (b) Application\nA State seeking a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may reasonably require, including a summary of the information submitted under subsection (c)(2) by each eligible entity that the State plans to award a subgrant to under such subsection.\n##### (c) Subgrants\n**(1) In general**\nA State that receives a grant under this section shall use such grant to award, on a competitive basis, subgrants to eligible entities for the purpose of carrying out the activities described in paragraph (3).\n**(2) Application**\nAn eligible entity seeking a subgrant under this subsection shall submit an application to the State at such time, in such manner, and containing such information as the State may reasonably require, including\u2014\n**(A)**\na description of how the eligible entity plans to carry out the activities described in paragraph (3);\n**(B)**\nan estimate of\u2014\n**(i)**\nthe cost of conducting the activities described in paragraph (3), including the cost per student of providing the education and technical training required under subparagraph (A) of such paragraph; and\n**(ii)**\nthe number of students the eligible entity plans to instruct; and\n**(C)**\na description of how the eligible entity plans to increase access to the education and technical training required under paragraph (3)(A).\n**(3) Use of funds**\nAn eligible entity that receives a subgrant under this subsection\u2014\n**(A)**\nshall use such subgrant funds to provide, as part of the curriculum of cosmetology schools, education and technical training to students of such cosmetology schools on how to shampoo, deep condition, braid, twist, and style textured hair; and\n**(B)**\nmay use such subgrant funds to, in order to better provide such education and technical training\u2014\n**(i)**\ndevelop such education and technical training;\n**(ii)**\nhire and train instructors; and\n**(iii)**\nprovide digital training, including through prerecorded videos.\n**(4) Determination of amount of award**\nA State shall award a subgrant under this subsection in an amount that the State determines appropriate based on the estimate submitted under paragraph (2)(B).\n##### (d) Duration; renewal\n**(1) Grants**\nA grant awarded under this section shall be for a term of 4 years and may be renewed by the Secretary.\n**(2) Subgrants**\nA subgrant awarded under subsection (c) shall be for a term of 6 months and may be renewed by the State that awarded the subgrant. In determining whether to renew such subgrant, the State shall take into consideration the information submitted under subsection (e).\n##### (e) Reporting requirements\n**(1) Eligible entities**\nNot later than 60 days before each date that is the final date of the term described in subsection (d)(2), a recipient of a subgrant under subsection (c) shall submit to the State that awarded the subgrant a report including\u2014\n**(A)**\na description of how the subgrant was used;\n**(B)**\nan identification of the cosmetology schools that the eligible entity worked with to provide the education and technical training required under subsection (c)(3)(A);\n**(C)**\nthe number of instructors that the eligible entity trained to provide the education and technical training required under subsection (c)(3)(A); and\n**(D)**\nthe number of students that received the education and technical training required under subsection (c)(3)(A).\n**(2) States**\nNot later than 60 days after each date that is the final date of the term described in subsection (d)(1), a State that receives a grant under this section shall submit to the Secretary a report including\u2014\n**(A)**\nan identification of the State agency that awards subgrants under this section; and\n**(B)**\na summary of the information submitted under paragraph (1).\n##### (f) Definitions\nIn this section:\n**(1) Cosmetology school**\nThe term cosmetology school means a school that provides training to prepare students for gainful employment in an occupation related to cosmetology.\n**(2) Eligible entity**\nThe term eligible entity \u2014\n**(A)**\nmeans a corporation, limited liability company, association, or company that\u2014\n**(i)**\nwas established not less than 5 years before the date of enactment of this Act;\n**(ii)**\nhas experience in providing the education and technical training required under subsection (c)(3)(A);\n**(iii)**\nhas an employer identification number issued by the Internal Revenue Service; and\n**(iv)**\nhas a Minority- or Women-owned Business Enterprise certificate; and\n**(B)**\ndoes not include\u2014\n**(i)**\na consortium of cosmetology schools, including an association of such schools;\n**(ii)**\nan individual; or\n**(iii)**\na cosmetology school that has received, at any point, Federal funds other than through a subgrant under subsection (c).\n**(3) Secretary**\nThe term Secretary means the Secretary of Labor.\n**(4) State**\nThe term State means each of the several States, the District of Columbia, and any commonwealth, territory, or possession of the United States.\n**(5) Textured hair**\nThe term textured hair means hair that is coiled, curly, or wavy in its natural state.",
      "versionDate": "2025-07-17",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-11T17:08:12Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4539ih.xml"
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
      "title": "Texture Positive Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Texture Positive Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Labor to award grants to States for the purpose of providing subgrants to eligible entities for education and technical training on how to perform cosmetology services on textured hair.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:36Z"
    }
  ]
}
```
