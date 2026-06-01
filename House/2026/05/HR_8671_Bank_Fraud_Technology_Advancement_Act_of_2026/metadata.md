# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8671?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8671
- Title: Bank Fraud Technology Advancement Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8671
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-21T14:51:43Z
- Update date including text: 2026-05-21T14:51:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 1.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 1.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8671",
    "number": "8671",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Bank Fraud Technology Advancement Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T14:51:43Z",
    "updateDateIncludingText": "2026-05-21T14:51:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 1.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
        "item": [
          {
            "date": "2026-05-13T15:57:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-07T13:04:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8671ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8671\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Flood introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Federal banking agencies to conduct a study on the use of advanced technologies in fraud detection and prevention, with particular attention to community financial institutions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bank Fraud Technology Advancement Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Advanced fraud detection technology**\nThe term advanced fraud detection technology includes artificial intelligence, machine learning, predictive analytics, behavioral biometrics, network analytics, data fusion tools, distributed ledger-based monitoring tools, blockchain tracing tools, and other emerging technologies used to detect, prevent, or mitigate financial fraud.\n**(2) Artificial intelligence**\nThe term artificial intelligence has the meaning given that term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(3) Credit union**\nThe term credit union means a State credit union or Federal credit union, as such terms are defined, respectively, in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ).\n**(4) Federal banking agency**\nThe term Federal banking agency \u2014\n**(A)**\nhas the meaning given such term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nmeans the National Credit Union Administration.\n**(5) Insured depository institution**\nThe term insured depository institution has the meaning given such term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ).\n**(6) Machine learning**\nThe term machine learning has the meaning given that term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n#### 3. Study on advanced technologies in fraud detection and prevention\n##### (a) In general\nThe Federal banking agencies, in consultation with the Secretary of the Treasury, the Financial Crimes Enforcement Network, the Federal Trade Commission, the Bureau of Consumer Financial Protection, and appropriate law enforcement agencies, shall jointly conduct a comprehensive study on the use of advanced fraud detection technology by insured depository institutions and credit unions.\n##### (b) Required elements\nThe study required under subsection (a) shall evaluate the following:\n**(1) Current use and effectiveness**\nThe current use and effectiveness of advanced fraud detection technology, including\u2014\n**(A)**\nthe extent to which insured depository institutions and credit unions of varying asset sizes deploy advanced fraud detection technology;\n**(B)**\nmeasurable outcomes relating to fraud reduction, loss mitigation, and consumer protection; and\n**(C)**\nbarriers to adoption, including cost, interoperability constraints, regulatory uncertainty, data access limitations, and liability concerns.\n**(2) Community financial institution access**\nCommunity financial institution access to advanced fraud detection technology, including\u2014\n**(A)**\nchallenges faced by community financial institutions in accessing or deploying advanced fraud detection tools;\n**(B)**\nwhether economies of scale disadvantage smaller community financial institutions relative to large community financial institutions;\n**(C)**\noptions to facilitate shared services, utility models, managed-service providers, or consortium-based fraud detection platforms; and\n**(D)**\nrecommendations to ensure regulatory guidance is appropriately tailored to avoid discouraging adoption by smaller community financial institutions.\n**(3) Artificial intelligence and machine learning**\nArtificial intelligence and machine learning, including\u2014\n**(A)**\nthe use of artificial intelligence and machine learning models, applications, and tools in detecting fraud patterns, anomalies, synthetic identity fraud, and real-time payment fraud;\n**(B)**\ngovernance frameworks used by insured depository institutions and credit unions to manage fraud model risk, explainability, and validation; and\n**(C)**\ninteractions between fraud detection models and consumer protection laws.\n**(4) Information sharing and public-private partnerships**\nInformation sharing and public-private partnerships, including\u2014\n**(A)**\nthe effectiveness of existing information-sharing frameworks;\n**(B)**\nwhether expanded public-private partnerships or centralized fraud utilities would enhance detection capabilities;\n**(C)**\nthe feasibility of a voluntary fraud analytics consortium accessible to community financial institutions; and\n**(D)**\nprivacy, data protection, and cybersecurity considerations associated with expanded data sharing.\n**(5) Payments system risks**\nPayments system risk, including\u2014\n**(A)**\nfraud risks associated with electronic funds transfers and checks; and\n**(B)**\nwhether advanced analytics can reduce fraud while preserving settlement finality and payment system stability.\n**(6) Regulatory and supervisory considerations**\nRegulatory and supervisory considerations, including\u2014\n**(A)**\nwhether existing supervisory expectations create barriers to innovation;\n**(B)**\nthe need for interagency guidance, regulatory clarity, or safe harbors to support technology adoption;\n**(C)**\nopportunities to harmonize expectations across Federal banking agencies; and\n**(D)**\nwhether additional training for Federal banking agencies staff is necessary to promote effective regulation and supervision of financial institutions\u2019 use of advanced fraud detection technology, especially for community financial institutions.\n##### (c) Report and recommendations\n**(1) Report**\nNot later than 18 months after the date of enactment of this Act, the Federal banking agencies shall issue a report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate containing all findings and determinations made in carrying out the study required under this section, and make such report publicly available, except for classified or supervisory information.\n**(2) Recommendations**\nThe report required under paragraph (1) shall include legislative, regulatory, or supervisory recommendations which may include\u2014\n**(A)**\nproposals to support shared fraud detection utilities or consortium-based analytics platforms;\n**(B)**\nguidance or safe harbors to encourage responsible artificial intelligence use in fraud prevention;\n**(C)**\npilot programs tailored to community financial institutions; and\n**(D)**\nrecommendations to strengthen public-private information sharing consistent with privacy and civil liberties protections.\n#### 4. Community bank fraud technology pilot program\n##### (a) In general\nNot later than 1 year after submission of the study under section 3, the Federal banking agencies may jointly establish a voluntary pilot program to facilitate community financial institution access to advanced fraud detection tools.\n##### (b) Program features\nThe pilot program described in subsection (a) may include\u2014\n**(1)**\npooled procurement or shared services models;\n**(2)**\nmodel validation assistance or technical support;\n**(3)**\nstandardized vendor risk management templates;\n**(4)**\nregulatory clarity regarding model governance expectations; and\n**(5)**\ncollaboration with the Department of the Treasury and law enforcement to provide anonymized fraud typology data feeds.",
      "versionDate": "2026-05-07",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-05-21T14:51:43Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8671ih.xml"
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
      "title": "Bank Fraud Technology Advancement Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T08:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bank Fraud Technology Advancement Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T08:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Federal banking agencies to conduct a study on the use of advanced technologies in fraud detection and prevention, with particular attention to community financial institutions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T08:18:39Z"
    }
  ]
}
```
