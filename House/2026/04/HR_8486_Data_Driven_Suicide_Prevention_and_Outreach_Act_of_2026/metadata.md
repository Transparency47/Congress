# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8486?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8486
- Title: Data Driven Suicide Prevention and Outreach Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8486
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-18T18:57:16Z
- Update date including text: 2026-05-18T18:57:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8486",
    "number": "8486",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001230",
        "district": "7",
        "firstName": "Ryan",
        "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
        "lastName": "Mackenzie",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Data Driven Suicide Prevention and Outreach Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-18T18:57:16Z",
    "updateDateIncludingText": "2026-05-18T18:57:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8486ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8486\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Mackenzie (for himself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to carry out a program to award grants for the development of predictive models to evaluate risk factors that contribute to the incidence of suicide among veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Data Driven Suicide Prevention and Outreach Act of 2026 .\n#### 2. Department of Veterans Affairs grant program for predictive models to evaluate risk factors that contribute to suicide among veterans\n##### (a) Establishment\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs, acting through the Center for Innovation for Care and Payment of the Department of Veterans Affairs, shall establish and carry out a program (in this section referred to as the Program ) to award grants to eligible organizations described in subsection (b) to use artificial intelligence to develop a predictive model to evaluate risk factors contributing to the incidence of suicide among veterans.\n##### (b) Eligibility\nAn eligible organization described in this subsection is a nonprofit entity, academic institution, private research organization, or other entity with demonstrated capability and experience\u2014\n**(1)**\ndeveloping and deploying artificial intelligence and machine learning solutions;\n**(2)**\nanalyzing health care data, including de-identification and protection of\u2014\n**(A)**\npersonally identifiable information; and\n**(B)**\nprotected health information;\n**(3)**\ndeveloping predictive models or decision-support tools used in clinical or population health settings;\n**(4)**\napplying advanced statistical methods or machine learning techniques to large, complex health datasets; and\n**(5)**\ncomplying with Department data security and interoperability standards.\n##### (c) Applications\nAn eligible organization desiring a grant under the Program shall submit to the Secretary an application in such form, at such time, and containing such information and assurances as the Secretary determines appropriate.\n##### (d) Selection procedures\n**(1) Number**\nSubject to paragraph (4), the Secretary shall select not fewer than two eligible organizations to which to award a grant under the Program.\n**(2) Criteria**\nIn selecting an eligible organization pursuant to paragraph (1), the Secretary shall consider the following criteria:\n**(A)**\nWith respect to the VISN in which the organization is located\u2014\n**(i)**\nthe geographic distribution;\n**(ii)**\nthe complexity of applicable Veterans Health Administration facilities; and\n**(iii)**\nthe density of the veteran population.\n**(B)**\nGeographic proximity to Veterans Health Administration facilities.\n**(C)**\nDemonstrated experience in collaborating with local Department facilities and community partners.\n**(D)**\nDemonstrated capability to deploy a predictive analysis solution in a health care system that serves more than 500,000 patients and beneficiaries.\n**(3) Priority**\nIn evaluating the criteria described in paragraph (2), the Secretary shall give priority for selection under paragraph (1) to eligible organizations\u2014\n**(A)**\nlocated in areas with\u2014\n**(i)**\na high rate of suicide among veterans;\n**(ii)**\na high rate of calls to the Veterans Crisis Line; and\n**(iii)**\nlong wait times for mental health care services at Department facilities;\n**(B)**\nwith experience in administering predictive analytics or population health solutions for Government-owned health care systems pursuant to an agreement with the Federal Government (including the Department of Veterans Affairs, the Department of Defense, and the Centers for Medicare and Medicaid Services);\n**(C)**\nwith a demonstrated capability to deliver tools that are\u2014\n**(i)**\nexplicable;\n**(ii)**\ninteroperable; and\n**(iii)**\nclinically actionable;\n**(D)**\nthat employ data scientists, clinicians, and suicide prevention specialists;\n**(E)**\nwith existing infrastructure for secure data storage and transmission that complies with Federal cybersecurity requirements; and\n**(F)**\nthat agree to make any predictive model or finding resulting from activities funded with a grant under this section available to the Secretary for Department of Veterans Affairs-wide implementation and evaluation.\n**(4) Limitation**\nThe Secretary may not, pursuant to paragraph (1), select an eligible organization located in a VISN in which another eligible organization in receipt of a grant under the Program is located.\n##### (e) Capability\nEach eligible organization in receipt of a grant under the Program shall ensure that the predictive model developed using such grant has the capability to integrate data under the jurisdiction of the Veterans Benefits Administration, including the military service records of veterans, with clinical data under the jurisdiction of the Veterans Health Administration.\n##### (f) Rule of construction\nNothing in subsection (d) may be construed to require an eligible organization in receipt of a grant under the Program to transfer to the Secretary ownership of the predictive model developed using such grant, or any proprietary technology associated with such predictive model.\n##### (g) Termination date\nThe authority of the Secretary to carry out the pilot program under this section shall terminate on September 30, 2029.\n##### (h) Definitions\nIn this section:\n**(1)**\nThe term artificial intelligence has the meaning given such term in section 238 of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. 2358 note).\n**(2)**\nThe term veteran has the meaning given such term in section 101 of title 38, United States Code.\n**(3)**\nThe term Veterans Crisis Line means the toll-free hotline for veterans established and operated under section 1720F of such title.\n**(4)**\nThe term VISN means a Veteran Integrated Services Network.",
      "versionDate": "2026-04-23",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-18T18:57:15Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8486ih.xml"
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
      "title": "Data Driven Suicide Prevention and Outreach Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T06:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Data Driven Suicide Prevention and Outreach Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T06:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to carry out a program to award grants for the development of predictive models to evaluate risk factors that contribute to the incidence of suicide among veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T06:03:34Z"
    }
  ]
}
```
