# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7443?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7443
- Title: I&A Mission Reorientation Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7443
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-05-30T08:06:08Z
- Update date including text: 2026-05-30T08:06:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-10 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-10 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7443",
    "number": "7443",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "I&A Mission Reorientation Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:08Z",
    "updateDateIncludingText": "2026-05-30T08:06:08Z"
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
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-09",
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
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:01:15Z",
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
                "date": "2026-05-14T13:53:12Z",
                "name": "Reported by"
              },
              {
                "date": "2026-05-14T13:52:42Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-10T14:51:41Z",
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
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "RI"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7443ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7443\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Pfluger (for himself and Mr. Magaziner ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to realign the mission of the Office of Intelligence and Analysis of the Department of Homeland Security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the I&A Mission Reorientation Act of 2026 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe Office of Intelligence and Analysis (I&A) of the Department of Homeland Security plays a critical role in supporting homeland security by providing actionable intelligence to Federal, State, local, Tribal, and territorial governments and private sector entities.\n**(2)**\nThe Office\u2019s foundational mission is to serve as an intelligence component that supports such governments and entities by fusing law enforcement and intelligence information.\n**(3)**\nThe Office\u2019s effectiveness depends on the mutual flow of information, collaboration, and trust between the Department and such governments and entities.\n**(4)**\nEmerging and evolving threats require a proactive approach to intelligence collection, analysis, and dissemination.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Office of Intelligence and Analysis of the Department of Homeland Security should fully execute its statutory role in supporting State, local, Tribal, and territorial governments and private sector entities through actionable, relevant, and timely intelligence;\n**(2)**\nconsistent with the requirements of section 201(d)(6) of the Homeland Security Act of 2002 ( 6 U.S.C. 121(d)(6) ), the Department should avoid an intelligence posture that promotes a one-directional flow of information from field entities to the intelligence community (as such term is defined in section 3(4) of the National Security Act of 1947 ( 50 U.S.C. 3003(4) )), and should actively foster two-way collaboration; and\n**(3)**\nintelligence support to the Secretary of Homeland Security should complement the Office\u2019s broader stakeholder-facing mission.\n#### 3. Realignment of mission of DHS Office of Intelligence and Analysis\n##### (a) In general\nSubsection (d) of section 201 of the Homeland Security Act of 2002 ( 6 U.S.C. 121 ) is amended by adding at the end the following new paragraph:\n(24) To ensure the Office of Intelligence and Analysis\u2019s operational mission of providing timely and efficient intelligence support to State, local, Tribal, and territorial governments and private sector entities is equally prioritized and resourced relevant to support provided to elements of the intelligence community by carrying out the following: (A) Identifying and addressing emerging threats through forward-deployed intelligence capabilities. (B) Facilitating two-way information sharing characterized by both the receipt of intelligence from such governments and entities, and the dissemination of actionable intelligence to such governments and entities. (C) Maintaining robust and sustained engagement with fusion centers (as such term is defined in section 210A). (D) Ensuring intelligence support from the Office provided to departmental leadership, including the Secretary, does not hinder or deprioritize broader responsibilities of the Office to State, local, Tribal, and territorial governments and private sector entities. .\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, the Under Secretary for Intelligence and Analysis of the Department of Homeland Security shall submit to the Committee on Homeland Security and the Permanent Select Committee on Intelligence of the House of Representatives and the Committee on Homeland Security and Governmental Affairs and the Select Committee on Intelligence of the Senate a report detailing the following:\n**(1)**\nSteps taken to implement the mission realignment of the Office of Intelligence and Analysis of the Department in accordance with paragraph (24) of section 201(d) of the Homeland Security Act of 2002, as added by subsection (a).\n**(2)**\nProgress in enhancing two-way information sharing between the Office and State, local, Tribal, and territorial governments and private sector entities, in accordance with such paragraph (24).\n**(3)**\nMetrics used to evaluate the effectiveness of the Office\u2019s intelligence activitiese in support of State, local, Tribal, and territorial governments and private sector entities.\n**(4)**\nAny resource or organizational changes to the Office required to sustain such realignment.\n##### (c) Rule of construction\nNothing in this section may be construed to alter or otherwise change the watchlisting functions of the Office of Intelligence and Analysis.",
      "versionDate": "2026-02-09",
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
        "updateDate": "2026-02-20T17:41:16Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7443ih.xml"
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
      "title": "I&A Mission Reorientation Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T06:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "I&A Mission Reorientation Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to realign the mission of the Office of Intelligence and Analysis of the Department of Homeland Security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T06:48:24Z"
    }
  ]
}
```
