# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8278?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8278
- Title: Fostering the Use of Technology to Uphold Regulatory Effectiveness in Supervision Act
- Congress: 119
- Bill type: HR
- Bill number: 8278
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-05-14T08:08:02Z
- Update date including text: 2026-05-14T08:08:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.
- Latest action: 2026-04-14: Introduced in House

## Actions

- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8278",
    "number": "8278",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001188",
        "district": "3",
        "firstName": "Marlin",
        "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
        "lastName": "Stutzman",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Fostering the Use of Technology to Uphold Regulatory Effectiveness in Supervision Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:02Z",
    "updateDateIncludingText": "2026-05-14T08:08:02Z"
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.",
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
      "actionDate": "2026-04-14",
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
      "actionDate": "2026-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-14",
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
            "date": "2026-05-13T15:55:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-14T16:03:30Z",
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
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8278ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8278\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Mr. Stutzman (for himself and Mr. Foster ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require certain supervisory agencies to assess their technological capabilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fostering the Use of Technology to Uphold Regulatory Effectiveness in Supervision Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nBanking regulators continue to examine and monitor depository institutions without sufficient access to real-time information.\n**(2)**\nSupervisory regulators should leverage technologies to more effectively carry out their duties.\n**(3)**\nWhen updating supervisory technology, risks surrounding technology procurement must be effectively managed.\n**(4)**\nAgencies\u2019 reliance on outdated technology can create vulnerabilities for the financial system, through\u2014\n**(A)**\ndifficulties in collecting, compiling, and analyzing relevant information about risks and noncompliance at supervised firms;\n**(B)**\nreliance on information that is inaccurate, incomplete, or not timely;\n**(C)**\nreliance on limited and outdated tools for data analysis;\n**(D)**\ndifficulties in using data to identify risk trends;\n**(E)**\ndifficulties in producing accurate and timely reports;\n**(F)**\ninadequacy of cybersecurity safeguards; and\n**(G)**\nfailure to detect illegal activities.\n**(5)**\nThe rapid expansion of financial firms\u2019 use of artificial intelligence may generate opportunities to improve the financial system while also introducing a range of risks, making it essential that agencies be equipped with the technology, expertise, and skills needed to analyze these opportunities and potential risks.\n**(6)**\nWhile agencies assess their supervisory capabilities on an ongoing basis, it is imperative that there be a unified goal of enhancing supervisory technologies that ensure effective and sustainable oversight.\n#### 3. Technological capabilities and procurement practices assessment\n##### (a) In general\n**(1) Technological capabilities assessment**\nEach covered agency shall, not later than 180 days after the date of the enactment of this section, assess how existing technologies used by the covered agency pose challenges to the covered agency in conducting adequate, real-time supervisory assessments of entities over which the covered agency has supervisory authority. Such technologies include, as applicable\u2014\n**(A)**\ncore information technology infrastructure;\n**(B)**\ntechnologies used to supervise entities;\n**(C)**\ntechnologies for monitoring general market risks using reported data and external data; and\n**(D)**\ntechnologies for data collection, storage, processing, and security.\n**(2) Procurement practices assessment**\nEach covered agency shall, not later than 180 days after the date of the enactment of this section\u2014\n**(A)**\nassess the procurement rules and protocols adhered to by such covered agency when such covered agency acquires or develops new technological systems; and\n**(B)**\nidentify any opportunities to further streamline procurement rules and protocols, including an assessment of the impact such rules or protocols have on the ability of the covered agency to test new technological systems, that are within the covered agency\u2019s authority to streamline.\n##### (b) Report\nNot later than 18 months after the completion of the assessments required under subsection (a), and for every 5 years thereafter, the covered agencies shall coordinate and jointly submit to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate, in a manner that does not pose a risk to the integrity or security of any technologies, systems, or capabilities of covered agencies, regulated entities, or market participants, a report that includes, as applicable, the following with respect to each covered agency:\n**(1)**\nA general overview of hardware and software used for information gathering and advanced analytics during supervision activities, including categories of technology purchased from vendors and developed by the covered agency or contractors of the covered agency.\n**(2)**\nA description of the procurement practices and protocols of the covered agency, including a description of\u2014\n**(A)**\nwhether such processes are voluntarily adhered to or mandated; and\n**(B)**\nany opportunities to further streamline procurement rules and protocols, including an assessment of the impact such rules or protocols have on the ability of the covered agency to test new technological systems.\n**(3)**\nA general overview of the portion of the workforce of the covered agency that is engaged materially in technology development within the covered agency, including\u2014\n**(A)**\nan overview of the ability of the covered agency to recruit and retain appropriate technology experts; and\n**(B)**\na description of the degree to which the covered agency relies on contractors to design, develop, or deploy technology and perform technology-related tasks.\n**(4)**\nA general description of the processes used by the covered agency to obtain information from entities supervised by the covered agency and any impediments thereto, including regulatory obstacles.\n**(5)**\nGeneral information about market and technology trends and risks in the underlying regulated markets including, specific to the covered agency\u2019s jurisdiction\u2014\n**(A)**\nmarket developments influenced by the adoption of new technologies;\n**(B)**\nthe use of new technologies by supervised entities for compliance and risk management purposes;\n**(C)**\nthe impact of new technologies on the collection and analysis of data submitted to the covered agencies by supervised entities as required by regulation, including on data quality, interoperability, and standardization; and\n**(D)**\npotential risks, including risks of illicit activity, related to new technologies.\n**(6)**\nA general description of the ways in which the covered agency shares information or system access with other covered agencies and any impediments thereto, including regulatory obstacles.\n**(7)**\nAn estimate of the costs for supervised entities to modify systems to share data with covered agencies, as appropriate.\n**(8)**\nA general description of any plans of the covered agency to implement future upgrades to the technology it uses to supervise entities, including\u2014\n**(A)**\nthe anticipated timeline for any planned upgrades;\n**(B)**\nthe costs of any planned upgrades;\n**(C)**\nany impediments to procuring relevant technologies;\n**(D)**\nplans for hiring and training individuals in connection with technological upgrades;\n**(E)**\nany aspects of any planned upgrades that should be addressed on an interagency basis;\n**(F)**\nany anticipated challenges and opportunities associated with entities supervised by the covered agency adapting to the covered agency\u2019s reporting process, including\u2014\n**(i)**\nestimates of transition costs; and\n**(ii)**\nestimates of any potential cost reductions; and\n**(G)**\nas applicable, the covered agency\u2019s relationships with other covered agencies in their capacity as delegated examiners.\n##### (c) Covered agency defined\nIn this section, the covered agency means the Board of Governors of the Federal Reserve System, the Bureau of Consumer Financial Protection, the Federal Deposit Insurance Corporation, the Department of the Treasury, including the Office of the Comptroller of the Currency and the Financial Crimes Enforcement Network, the Federal Housing Finance Agency, and the National Credit Union Administration.",
      "versionDate": "2026-04-14",
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
        "updateDate": "2026-04-22T16:00:35Z"
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
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8278ih.xml"
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
      "title": "Fostering the Use of Technology to Uphold Regulatory Effectiveness in Supervision Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T09:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fostering the Use of Technology to Uphold Regulatory Effectiveness in Supervision Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T09:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require certain supervisory agencies to assess their technological capabilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T09:18:57Z"
    }
  ]
}
```
