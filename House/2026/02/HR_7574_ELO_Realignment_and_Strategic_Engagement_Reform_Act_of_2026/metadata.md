# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7574?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7574
- Title: ELO Realignment and Strategic Engagement Reform Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7574
- Origin chamber: House
- Introduced date: 2026-02-13
- Update date: 2026-05-30T08:05:50Z
- Update date including text: 2026-05-30T08:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-13: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-14 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-02-13: Introduced in House

## Actions

- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-14 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-13",
    "latestAction": {
      "actionDate": "2026-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7574",
    "number": "7574",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "E000300",
        "district": "8",
        "firstName": "Gabe",
        "fullName": "Rep. Evans, Gabe [R-CO-8]",
        "lastName": "Evans",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "ELO Realignment and Strategic Engagement Reform Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:50Z",
    "updateDateIncludingText": "2026-05-30T08:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-14",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-13",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-13",
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
          "date": "2026-02-13T15:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-05-14T13:56:45Z",
                "name": "Reported by"
              },
              {
                "date": "2026-05-14T04:00:00Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-14T14:55:51Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7574ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7574\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2026 Mr. Evans of Colorado introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo provide for the reorganization and realignment of the Engagement, Liaison, and Outreach Office of the Department of Homeland Security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ELO Realignment and Strategic Engagement Reform Act of 2026 .\n#### 2. Plan for reorganization and realignment of DHS Engagement, Liaison, and Outreach Office\n##### (a) In general\nNot later than 120 days after the date of the enactment of this Act, the Secretary shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a comprehensive plan to carry out the following:\n**(1)**\nAn identification of redundant or non-essential positions, programs, or functions within the Engagement, Liaison, and Outreach office, including how reorganization of the Office will address such redundant or non-essential positions, programs, or functions.\n**(2)**\nRealign the essential functions and personnel of the ELO Office within the Partner Engagement directorate of I&A.\n**(3)**\nImprove the management and coordination of strategic relationships with priority law enforcement agencies, including by carrying out the following:\n**(A)**\nEstablishing clear communication protocols.\n**(B)**\nCentralizing points of contact for law enforcement engagement.\n**(C)**\nEnhancing information-sharing mechanisms.\n**(D)**\nReducing duplication of outreach across Department of Homeland Security components.\n**(E)**\nImproving accountability and performance metrics related to stakeholder engagement.\n##### (b) Plan requirements\nThe plan required under subsection (a) shall include the following:\n**(1)**\nOrganizational analysis justifying the reorganization and realignment, including cost-benefit estimates, under paragraph (1) of such subsection.\n**(2)**\nDetailed staffing proposals, including reassignment plans.\n**(3)**\nA transition timeline for implementing the realignment within the Partner Engagement directorate of I&A, in accordance with paragraph (2) of such subsection.\n**(4)**\nInternal oversight mechanisms to monitor implementation of such plan.\n**(5)**\nRecommendations for future engagement models that reduce redundancy and improve efficiency in managing law enforcement and homeland security partnerships with priority law enforcement agencies.\n**(6)**\nAssurance of continuity of intelligence support and convenings currently being provided to SLTT entity partners through the ELO office, including relevant HSIN-INTEL access.\n##### (c) Certification\nThe Secretary of Homeland Security shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a certification not later than 60 days after commencing implementation of the plan required under subsection (a).\n##### (d) Limitation on expansion\nUntil such time as the Secretary of Homeland Security submits the plan required under subsection (a) and certifies commencement of the implementation of such plan under subsection (c), the Secretary may not\u2014\n**(1)**\nexpand the staffing, budget, or programmatic scope of the ELO Office; or\n**(2)**\nestablish new offices in the Department duplicating the mission of the ELO Office or the Partner Engagement directorate of I&A without specific congressional authorization.\n##### (e) Definitions\nIn this section:\n**(1) Department**\nThe term Department means the Department of Homeland Security.\n**(2) ELO Office**\nThe term ELO Office means the Engagement, Liaison, and Outreach office within the Office of Intelligence and Analysis (I&A) of the Department of Homeland Security.\n**(3) I&A**\nThe term I&A means the Office of Intelligence and Analysis of the Department of Homeland Security.\n**(4) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n**(5) SLTT entity**\nThe term SLTT entity has the meaning given such term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ).\n**(6) Priority law enforcement agencies**\nThe term priority law enforcement agencies means Federal, State, and local law enforcement agencies identified by the Secretary as key partners for national security, counterterrorism, emergency response, or other mission-critical operations.",
      "versionDate": "2026-02-13",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-19T15:40:40Z"
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
      "date": "2026-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7574ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ELO Realignment and Strategic Engagement Reform Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-14T09:23:23Z"
    },
    {
      "title": "ELO Realignment and Strategic Engagement Reform Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-14T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the reorganization and realignment of the Engagement, Liaison, and Outreach Office of the Department of Homeland Security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-14T09:18:24Z"
    }
  ]
}
```
