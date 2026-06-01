# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1874?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1874
- Title: To amend the Coastal Zone Management Act of 1972 to establish a conclusive presumption that a State concurs to certain activities, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 1874
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-02-17T20:11:37Z
- Update date including text: 2026-02-17T20:11:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-03-06 - IntroReferral: Sponsor introductory remarks on measure. (CR H1032-1033)
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-03-06 - IntroReferral: Sponsor introductory remarks on measure. (CR H1032-1033)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1874",
    "number": "1874",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000401",
        "district": "3",
        "firstName": "Kevin",
        "fullName": "Rep. Kiley, Kevin [R-CA-3]",
        "lastName": "Kiley",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "To amend the Coastal Zone Management Act of 1972 to establish a conclusive presumption that a State concurs to certain activities, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-02-17T20:11:37Z",
    "updateDateIncludingText": "2026-02-17T20:11:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1032-1033)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1874ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1874\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Kiley of California introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Coastal Zone Management Act of 1972 to establish a conclusive presumption that a State concurs to certain activities, and for other purposes.\n#### 1. Conclusive presumption for certain activities\nSection 307 of the Coastal Zone Management Act of 1972 ( 16 U.S.C. 1456 ) is amended by adding at the end:\n(j) Conclusive presumption for certain activities (1) In general Except as provided in paragraph (3), with respect to a covered activity, a coastal state shall be conclusively presumed to concur with\u2014 (A) a consistency determination provided to the coastal state by a Federal agency under subsection (c)(1)(C); (B) a determination or other finding of a Federal agency under subsection (c)(2) that a development project in the coastal zone of the coastal state is consistent with the enforceable policies of the approved state management program of the coastal state; (C) a certification provided to the coastal state by an applicant under subsection (c)(3)(A) or person under subsection (c)(3)(B); and (D) a determination or other finding of a State or local government under subsection (d) that an application for Federal assistance submitted by such State or local government is consistent with the enforceable policies of the approved state management program of the coastal state. (2) Limitation on objection An objection or other challenge by a coastal state to an activity subject to a conclusive presumption of concurrence under paragraph (1) may not delay or otherwise prevent the activity from proceeding. (3) Review of presumptive concurrence (A) In general Not later than 30 days after the Secretary receives a consistency determination, certification, or other relevant finding under this section, the Secretary may issue a written determination with respect to an activity subject to a conclusive presumption of concurrence under paragraph (1) that nullifies the conclusive presumption of concurrence if the Secretary finds that the activity is not a covered activity. (B) Presumption of finality If the Secretary does not issue a written determination under subparagraph (A) with respect to an activity subject to a conclusive presumption of concurrence under paragraph (1) within the time period described in that subparagraph, the conclusive presumption of concurrence shall be final and binding. (4) Definitions In this subsection: (A) Activity with a significant national or regional economic impact The term activity with a significant national or regional economic impact means an activity\u2014 (i) that is authorized or funded in whole or in part by the Federal Government; and (ii) that is carried out in\u2014 (I) an area with a low per capita income; or (II) an area with a high unemployment rate. (B) Area with a high unemployment rate The term area with a high unemployment rate means an area where the unemployment rate, for the most recent 24-month period for which data is available, is at least 1 percentage point higher than the national average unemployment rate for such period, as determined by the Secretary using the most recent data available from\u2014 (i) the Bureau of Economic Analysis of the Department of Commerce; (ii) the Bureau of Labor Statistics of the Department of Labor; (iii) another Federal source the Secretary determines appropriate; or (iv) if no recent Federal data is available, data from the State agencies of such area the Secretary determines appropriate. (C) Area with a low per capita income The term area with low per capita income means an area where the per capita income is not more than 20 percent less than the national average per capita income, as determined by the Secretary using the most recent data available from\u2014 (i) the Bureau of Economic Analysis of the Department of Commerce; or (ii) another Federal source the Secretary determines appropriate. (D) Covered activity The term covered activity means\u2014 (i) a national security activity; (ii) a critical infrastructure project; (iii) a disaster recovery or mitigation activity; or (iv) an activity with a significant national or regional economic impact. (E) Critical infrastructure The term critical infrastructure has the meaning given the term in section 1016(e) of the USA PATRIOT Act ( 42 U.S.C. 5195c(e) ). (F) Critical infrastructure project The term critical infrastructure project means any project\u2014 (i) that is authorized or funded in whole or in part by the Federal Government; and (ii) that involves\u2014 (I) the planning, construction, maintenance, or improvement of critical infrastructure; (II) a facility or an activity associated with any critical infrastructure sectors; or (III) a material or asset that is essential to the operation, maintenance, or development of critical infrastructure. (G) Critical infrastructure sectors The term critical infrastructure sectors has the meaning given the term in section 2001 of the Homeland Security Act of 2002 ( 6 U.S.C. 601 ). (H) Disaster recovery or mitigation activity The term disaster recovery or mitigation activity means an activity\u2014 (i) that is authorized or funded in whole or in part by the Federal Government; and (ii) that is carried out to prevent, prepare for, respond to, recover from, or mitigate the effects of\u2014 (I) an emergency; (II) a major disaster; or (III) any other incident or threat that the Administrator of the Federal Emergency Management Agency determines poses a significant risk to public health, safety, or property. (I) Emergency; major disaster The terms emergency and major disaster have such meanings given such terms in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ). (J) Intelligence community The term intelligence community has the meaning given the term in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 ). (K) National security activity The term national security activity means an activity that is carried out by or on behalf of\u2014 (i) the Department of Defense; (ii) the Department of Homeland Security; or (iii) the intelligence community. .",
      "versionDate": "2025-03-05",
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
            "name": "Intergovernmental relations",
            "updateDate": "2026-02-17T20:11:36Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2026-02-17T20:11:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-20T13:07:55Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1874ih.xml"
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
      "title": "To amend the Coastal Zone Management Act of 1972 to establish a conclusive presumption that a State concurs to certain activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:48:32Z"
    },
    {
      "title": "To amend the Coastal Zone Management Act of 1972 to establish a conclusive presumption that a State concurs to certain activities, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T09:06:10Z"
    }
  ]
}
```
