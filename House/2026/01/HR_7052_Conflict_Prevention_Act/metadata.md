# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7052?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7052
- Title: Conflict Prevention Act
- Congress: 119
- Bill type: HR
- Bill number: 7052
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-01-28T17:35:17Z
- Update date including text: 2026-01-28T17:35:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7052",
    "number": "7052",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000305",
        "district": "51",
        "firstName": "Sara",
        "fullName": "Rep. Jacobs, Sara [D-CA-51]",
        "lastName": "Jacobs",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Conflict Prevention Act",
    "type": "HR",
    "updateDate": "2026-01-28T17:35:17Z",
    "updateDateIncludingText": "2026-01-28T17:35:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7052ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7052\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Ms. Jacobs (for herself and Mr. McCaul ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo establish a Center for Conflict Analysis, Planning, and Prevention in the Department of State, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Conflict Prevention Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nbetter understanding and responding to conflict and supporting peace processes and complex political negotiations will further United States national security and foreign policy interests;\n**(2)**\nthe Department of State should possess an institutional hub to help regional bureaus and embassies efficiently and effectively address violent conflict, peace processes, and complex political negotiations; and\n**(3)**\nsuch an institutional hub should be staffed by subject matter experts that can equip United States diplomats in conflict analysis and peace negotiations.\n#### 3. Center for conflict analysis, planning, and prevention at the Department of State\n##### (a) Authorization\nThere shall be in the Department of State a Director for Conflict Analysis, Planning, and Prevention, who shall be responsible to the Secretary of State, acting through the Under Secretary for Political Affairs, for matters relating to conflict prevention, mitigation, and negotiations to develop policy options and provide expertise for the Under Secretary of Political Affairs and for the Assistant Secretaries of each regional bureau.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Director and the Center established under subsection (c) may carry out the following, as appropriate:\n**(1)**\nDeveloping advanced analytic methodologies, data, and tools to understand global conflict dynamics, produce conflict trend assessments, and inform the Department\u2019s efforts to prevent and mitigate conflict and crises of top priority to the United States.\n**(2)**\nForecasting potential hotspots of violent conflict in foreign countries to best identify risks to United States national security interests or opportunities for advancing United States foreign policy priorities.\n**(3)**\nConducting in-depth analyses of conflict dynamics in foreign countries to\u2014\n**(A)**\nadvise regional bureaus on program goals and approaches to burden-sharing with foreign partners; and\n**(B)**\nprovide quantifiable metrics to inform effective use of the Department\u2019s resources.\n**(4)**\nSupporting peace processes by providing expertise to the Under Secretary of Political Affairs, regional bureaus, and chiefs of mission, to enable and inform peace negotiation and mediation strategies, implementation, and monitoring.\n**(5)**\nAt the direction of the Under Secretary, coordinating with regional and relevant functional bureaus on the implementation of the Global Fragility Act of 2019 ( 22 U.S.C. 9801 et seq. ).\n**(6)**\nProviding strategic gaming, red team (contrarian-structured analytic techniques to challenge assumptions and test vulnerabilities), and table-top exercises, to rigorously test foreign policy options and strategies.\n**(7)**\nSupporting the development of training for Foreign Service officers on conflict prevention and mediation skills, including the trainings required under the Elie Wiesel Genocide and Atrocities Prevention Act of 2018.\n**(8)**\nSuch other functions as the Under Secretary for Political Affairs may designate from time to time.\n##### (c) Establishment\nThere shall be in the Department a Center for Conflict Analysis, Planning, and Prevention (in this section referred to as the Center ), led by the Director appointed pursuant to the authorization under subsection (a), which shall perform functions related to data analysis and strategic planning on emerging or ongoing foreign conflicts to develop policy options and provide expertise for the Under Secretary of Political Affairs and for the Assistant Secretaries of each regional bureau.\n##### (d) Dissemination of analytic products\nThe Under Secretary shall ensure that the Center\u2019s analytic products are disseminated to relevant stakeholders within the Department, as well as other elements of the United States Government, as appropriate.\n##### (e) Membership\nThe Center shall be comprised of not more than 20 full-time Department employees, including a contingent capable of temporary deployments to support embassies\u2014\n**(1)**\nin conflict-affected regions; or\n**(2)**\nin regions that the Under Secretary for Political Affairs determines to be at risk of conflict or civil strife.",
      "versionDate": "2026-01-14",
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
        "name": "International Affairs",
        "updateDate": "2026-01-16T18:54:18Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7052ih.xml"
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
      "title": "Conflict Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Conflict Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a Center for Conflict Analysis, Planning, and Prevention in the Department of State, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T05:33:44Z"
    }
  ]
}
```
