# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5363?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5363
- Title: Expanding Childcare in Rural America Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5363
- Origin chamber: House
- Introduced date: 2025-09-15
- Update date: 2026-03-04T09:06:47Z
- Update date including text: 2026-03-04T09:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-09-15: Introduced in House

## Actions

- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5363",
    "number": "5363",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Expanding Childcare in Rural America Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-04T09:06:47Z",
    "updateDateIncludingText": "2026-03-04T09:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T16:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "sponsorshipDate": "2025-09-15",
      "state": "KS"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "IL"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "IN"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "NC"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5363ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5363\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 15, 2025 Ms. Perez (for herself, Mr. Mann , Ms. Underwood , and Mr. Baird ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo authorize the Secretary of Agriculture to carry out an initiative to develop, expand, and improve rural childcare, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding Childcare in Rural America Act of 2025 .\n#### 2. Expanding Childcare in Rural America Initiative\n##### (a) Definitions\nIn this section:\n**(1) Childcare**\n**(A) In general**\nThe term childcare means any program that\u2014\n**(i)**\nprovides quality care and early education for young children who\u2014\n**(I)**\nare in kindergarten; or\n**(II)**\nhave not yet entered kindergarten; and\n**(ii)**\nis operated by\u2014\n**(I)**\nan eligible childcare provider described in section 658P(6)(A) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858n(6)(A) ); or\n**(II)**\na childcare provider that, on the date of enactment of this Act\u2014\n**(aa)**\nis licensed, regulated, or registered in the State, territory, or Indian Tribe in which the provider is located; and\n**(bb)**\nmeets applicable State, Tribal, territorial, and local health and safety requirements.\n**(B) Inclusions**\nThe term childcare includes\u2014\n**(i)**\na school-based program described in subparagraph (A);\n**(ii)**\na facility used for a program described in subparagraph (A); and\n**(iii)**\na service provided under a program described in subparagraph (A).\n**(2) Initiative**\nThe term Initiative means the Expanding Childcare in Rural America Initiative established under subsection (b).\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (b) Establishment\nThe Secretary shall establish an initiative, to be known as the Expanding Childcare in Rural America Initiative , under which the Secretary shall provide, for each of fiscal years 2026 through 2030, priority in accordance with subsection (c) to address the availability, quality, and cost of childcare in agricultural and rural communities.\n##### (c) Childcare priorities\n**(1) In general**\nNotwithstanding any other provision of law, in selecting recipients of loans and grants under a program described in paragraph (2), the Secretary shall give priority to any qualified applicant that proposes to use the loan or grant to address the availability, quality, or cost of childcare in an agricultural or rural community.\n**(2) Description of programs**\nThe programs referred to in paragraph (1) are the following:\n**(A)**\nThe essential community facilities loan and grant programs authorized under section 306(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a) ).\n**(B)**\nThe technical assistance and training grant program authorized under section 306(a) of that Act ( 7 U.S.C. 1926(a) ).\n**(C)**\nThe rural business development grant program authorized under section 310B(c) of that Act ( 7 U.S.C. 1932(c) ).\n**(D)**\nThe business and industry direct and guaranteed loan program authorized under section 310B(g) of that Act ( 7 U.S.C. 1932(g) ).\n**(E)**\nThe rural microentrepreneur assistance program authorized under section 379E of that Act ( 7 U.S.C. 2008s ).\n**(F)**\nThe rural innovation stronger economy (RISE) grant program authorized under section 379I of that Act ( 7 U.S.C. 2008w ).\n##### (d) Requirements\nIn providing funding in accordance with the Initiative, the Secretary shall\u2014\n**(1)**\ngive priority to communities in farming-dependent counties, as described in the 2015 county typology codes published by the Economic Research Service (as revised); and\n**(2)**\nensure a balanced geographical distribution of the benefits under the Initiative.\n##### (e) Use of intermediaries\nIn providing funding in accordance with the Initiative, the Secretary may make awards through a childcare resource and referral organization, a staffed family child care network, a community development financial institution, a nonprofit organization, or a network of nonprofit organizations, with demonstrated expertise in\u2014\n**(1)**\nproviding technical or financial assistance for the acquisition, construction, renovation, or improvement of childcare facilities;\n**(2)**\nproviding technical, financial, or managerial assistance to childcare providers; or\n**(3)**\nsecuring private sources of capital financing for childcare or other low-income community development.\n##### (f) Evaluation; report\n**(1) Evaluation**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall conduct a comprehensive quantitative and qualitative evaluation of the projects carried out using assistance provided under the Initiative, including\u2014\n**(A)**\na description of\u2014\n**(i)**\nthe types of projects carried out;\n**(ii)**\nthe communities in which the projects are carried out;\n**(iii)**\nthe organizations and entities participating in the projects; and\n**(iv)**\nthe types of partnerships developed to carry out the projects; and\n**(B)**\nthe economic and social impacts of the investments in the projects.\n**(2) Report**\nNot later than 3 years after the date of enactment of this Act, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House Representatives a report describing the evaluation conducted under paragraph (1), including a thorough analysis of the outcomes of the evaluation.",
      "versionDate": "2025-09-15",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-09-25T15:24:01Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5363ih.xml"
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
      "title": "Expanding Childcare in Rural America Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Childcare in Rural America Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Agriculture to carry out an initiative to develop, expand, and improve rural childcare, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T06:33:18Z"
    }
  ]
}
```
