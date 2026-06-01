# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8304?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8304
- Title: CREATES Act
- Congress: 119
- Bill type: HR
- Bill number: 8304
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-05-21T08:08:31Z
- Update date including text: 2026-05-21T08:08:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8304",
    "number": "8304",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001208",
        "district": "6",
        "firstName": "Lucy",
        "fullName": "Rep. McBath, Lucy [D-GA-6]",
        "lastName": "McBath",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "CREATES Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:31Z",
    "updateDateIncludingText": "2026-05-21T08:08:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T14:01:30Z",
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
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "UT"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8304ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8304\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mrs. McBath (for herself and Mr. Owens ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo require the Secretary of Labor to establish a grant program for States to improve or establish a credential repository, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Credential Repository and Transparency in States Act or the CREATES Act .\n#### 2. Purpose\nThe purpose of this Act is to provide assistance to States for the collection, development, analysis, and sharing of information on\u2014\n**(1)**\nall of the credentials offered in each State;\n**(2)**\nthe quality of such credentials, including their use by employers for making employment-related decisions;\n**(3)**\neducation and career pathways that lead to such credentials and occupations in a State; and\n**(4)**\nthe sharing of such information with individuals in each State, enabling them to make informed education and career choices.\n#### 3. Program Authorized\n##### (a) Authorization and limitations\n**(1) In general**\nFrom amounts made available under section 4, the Secretary, in consultation with the Secretary of Education, shall award grants, on a competitive basis, to States to establish, expand, or improve a State credential repository that contains information on each covered program, credential, and training provider in the State.\n**(2) Duration**\nA grant awarded under this Act shall be awarded for a period of 3 years.\n**(3) Amount**\nIn awarding a grant under this Act, the Secretary\u2014\n**(A)**\nmay not award a grant in excess of $10,000,000; and\n**(B)**\nin deciding the amount of a grant, shall take into consideration\u2014\n**(i)**\nthe number of credentials offered in the State; and\n**(ii)**\nthe number of training providers in the State.\n**(4) Timing**\nNot later than 90 days after the Secretary receives an application submitted under subsection (b), the Secretary shall make a determination as to whether the State that submitted such application will receive a grant under this Act.\n**(5) Limit**\nThe Secretary may only award one grant to a State.\n##### (b) Application\nTo be eligible to receive a grant, a State shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary shall require, including\u2014\n**(1)**\ninformation on how the State will establish, expand, or improve a credential repository that satisfies requirements under subsection (d);\n**(2)**\ninformation on the data policy a State will establish under subsection (c)(1)(B);\n**(3)**\na description of any products, tools, services, or resources that a State develops pursuant to subsection (c)(1)(E);\n**(4)**\nan assurance that the credential repository will be interoperable with other State credential repositories; and\n**(5)**\nan assurance that the State will establish and maintain the credential repository in accordance with the requirements under subsection (d).\n##### (c) Uses of funds\n**(1) Mandatory use**\nA State awarded a grant under this Act shall\u2014\n**(A)**\nestablish a credential repository, as described in subsection (d), through a process that includes input from the public;\n**(B)**\nestablish a data policy for such repository that addresses how the State will ensure that the repository meets the requirements described in subsection (d);\n**(C)**\nassist training providers in the State in the collection of information on the primary indicators of performance described in section 116(b)(2)(A) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3141(b)(2)(A) ) for each covered program;\n**(D)**\nprovide guidance to education, job, and career counselors in the State on how to use the credential repository; and\n**(E)**\ndevelop or facilitate access to products, tools, services, and other resources, using the information and linked, open, and interoperable data contained in the credential repository, that benefit workers, employers, educators, counselors, policymakers, and others.\n**(2) Authorized use**\nIf a State carries out all of the activities under paragraph (1), the State may use any excess grant funds to publicize the repository of the State to individuals in the State.\n##### (d) Credential repository\nA State that receives a grant under this Act shall establish a publicly accessible credential repository that\u2014\n**(1)**\nidentifies\u2014\n**(A)**\neach credential offered in the State; and\n**(B)**\neach training provider in the State;\n**(2)**\nincludes information on\u2014\n**(A)**\nwith respect to each training provider in the State\u2014\n**(i)**\nprocess and outcome quality indicators of such training provider for each covered program offered by such training provider; and\n**(ii)**\neach credential for which such training provider offers a covered program;\n**(B)**\nwith respect to each covered program offered in the State\u2014\n**(i)**\nthe competencies and skills an individual develops by completing such covered program; and\n**(ii)**\nthe cost of enrollment for an individual to enroll in such program; and\n**(C)**\nwith respect to each credential offered in the State\u2014\n**(i)**\nthe training providers that offer such credential;\n**(ii)**\nany assessment that an individual is required to take to earn such credential;\n**(iii)**\nthe cost to an individual of each such assessment;\n**(iv)**\nany postsecondary credit or equivalent transfer value recommendations of such credential, such as the recommendations provided by the American Council on Education\u2019s National Guide, guidance from a statewide education coordinating entity, or recommendations or guidance from a comparably similar entity, as available and appropriate;\n**(v)**\nthe career pathway or program of study that such credential is a part, as applicable;\n**(vi)**\nthe outcomes associated with such credential, including\u2014\n**(I)**\nthe earning and employment status of individuals after earning such credential;\n**(II)**\nthe completion and pass rates of individuals in each career pathway or program of study for which the individual earned such credential; and\n**(III)**\nother calculations, including the return on investment, as determined by the State, for an individual after earning such credential;\n**(vii)**\nthe job skills an individual develops in earning such credential; and\n**(viii)**\nthe industries and occupations for which such credential prepares an individual;\n**(3)**\naligns with, complements, and enhances eligibility lists or criteria for training providers, such as the eligibility criteria established under section 122(a) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3152(b) ), or a program or pathway approval process required by the Carl D. Perkins Career and Technical Education Act of 2006 (U.S.C.) or chapter 33 of title 38, United States Code (otherwise known as the Post 9/11 Education Assistance Program);\n**(4)**\nis updated on a continuous basis to ensure the accuracy and recency of the information and data in the repository;\n**(5)**\nuses data formats that\u2014\n**(A)**\nare transparent, linked, open, and interoperable with other State credential repositories;\n**(B)**\nare aligned with widely recognized and adopted standards, which may include the use of credential transparency description language specifications; and\n**(C)**\nallow for open access to the data in the repository across State and national borders and industry sectors for guidance counseling, career navigation, and other comparably similar activities;\n**(6)**\nhas functions to search, discover, compare, and analyze each credential, covered program, and training provider in the State; and\n**(7)**\nincludes any other information as determined by the Secretary, in consultation with the Secretary of Education.\n##### (e) Privacy protections\nIn carrying out the activities under this Act, a State shall not collect or include in the repository any personally identifiable information.\n##### (f) Report\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, and on an annual basis thereafter, a State that receives a grant under this Act shall submit to the Secretary a report at such time, in such manner, and containing such information as the Secretary may require, including information on the improvement or development and implementation of the credential repository in such State.\n**(2) Reduced burden**\nThe Secretary, in coordination with the Secretary of Education, and in consultation with the States receiving a grant under this Act, shall implement processes to reduce the burden of reporting information required to be reported under this Act.\n##### (g) Definitions\nIn this Act:\n**(1) Covered program**\nThe term covered program means a program that is offered to individuals to earn a credential.\n**(2) Credential**\nThe term credential means an education or occupational qualification or achievement used to indicate suitability for a future educational opportunity or career opportunity, including diplomas, digital badges, certificates, certifications, a recognized postsecondary credential, occupational or professional licenses, microcredentials, and degrees of all types and levels.\n**(3) Secretary**\nThe term Secretary , unless otherwise specified in this Act, means the Secretary of Labor.\n**(4) Training provider**\nThe term training provider means an entity that offers a covered program.\n**(5) WIOA terms**\nThe terms career pathway , recognized postsecondary credential , and State have the meanings given such terms in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3113 ).\n#### 4. Authorization of appropriations\n##### (a) In general\nThere are authorized to be appropriated such sums as may be necessary to carry out this Act for fiscal year 2028.\n##### (b) Remain available\nThe funds appropriated under this section shall remain available until September 30, 2029.",
      "versionDate": "2026-04-15",
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
        "updateDate": "2026-04-22T13:14:25Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8304ih.xml"
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
      "title": "CREATES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T06:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CREATES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T06:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Credential Repository and Transparency in States Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T06:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Labor to establish a grant program for States to improve or establish a credential repository, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T06:03:37Z"
    }
  ]
}
```
