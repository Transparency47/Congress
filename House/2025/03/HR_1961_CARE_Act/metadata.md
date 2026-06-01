# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1961?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1961
- Title: CARE Act
- Congress: 119
- Bill type: HR
- Bill number: 1961
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-05-06T08:05:33Z
- Update date including text: 2025-05-06T08:05:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1961",
    "number": "1961",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "CARE Act",
    "type": "HR",
    "updateDate": "2025-05-06T08:05:33Z",
    "updateDateIncludingText": "2025-05-06T08:05:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "DC"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "GA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1961ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1961\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Torres of New York introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to direct the Secretary of Health and Human Services to establish and implement a department-wide after-action program and a risk communication strategy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Coordinated Agency Response Enhancement Act or the CARE Act .\n#### 2. HHS after-action program\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following:\n399V\u20138. Department-wide after-action program (a) In general The Secretary shall establish, maintain, and implement an after-action program to\u2014 (1) identify and implement solutions for issues found following any response by the Department of Health and Human Services to a determination of a public health emergency under section 319(a); and (2) encourage collaboration among the agencies of the Department, including by integrating any public health emergency after-action programs of such agencies. (b) Deadline The Secretary shall establish and begin implementation of the after-action program under subsection (a) not later than 2 years after the date of enactment of this section. (c) Coordination with stakeholders The after-action program under subsection (a) shall include input from, and coordinate with, relevant external stakeholders involved in each public health emergency response of the Department of Health and Human Services, such as\u2014 (1) other Federal agencies; (2) other jurisdictions, including the health departments of States, Indian Tribes, and territories of the United States and municipalities thereof; and (3) nongovernmental partners. (d) Oversight by Inspector General The Inspector General of the Department of Health and Human Services shall, whenever the Inspector General determines appropriate, based on assessed risks and emerging needs\u2014 (1) evaluate the efficacy of the after-action program under subsection (a), including by evaluating the ability of the program to identify challenges and propose solutions; and (2) submit to Congress a report summarizing the evaluation under paragraph (1). (e) Comprehensive guidelines for after-Action program reports (1) In general The Secretary shall, as the Secretary determines appropriate, incorporate in any report of the after-action program under subsection (a) the elements described in subparagraphs (A) through (M) of paragraph (2). (2) Elements described (A) Emergency operations plan, continuity of operations plan, and business continuity plan reviews A description of the process and outcomes of reviewing and updating emergency operations plans, continuity of operations plans, and business continuity plans both annually and after significant public health emergencies. Such description may include insights into the relevancy and efficiency of such plans in practice. (B) Information sharing, situational awareness A description of the establishment and effectiveness of protocols for efficient information sharing (consistent with applicable disclosure laws) and situational awareness among health care facilities and partners, including the development and deployment of an integrated joint information system. (C) Coordination with national, State, and local coalitions and community partners Descriptions of\u2014 (i) strategies for coordination with national, State, and local health care patient and public health coalitions and community partners, focusing on active engagement and information sharing (consistent with applicable disclosure laws); (ii) information technology solutions used for coordination during public health emergencies; and (iii) how medical operations coordination cells were implemented for effective patient load balancing during surges to assure regional health care coordination. (D) Incident management A description of incident management structures, including the maintenance of the incident command system and the establishment of an incident action planning process. (E) Communications, information sharing A description of strategies for the development and maintenance of a dynamic communications framework for real-time information sharing (consistent with applicable disclosure laws) and situational awareness. (F) Staff, space, and resident management A description of strategies for comprehensive staff management plans, scalable space management strategies, and policies adopted to maintain patient and resident well-being. (G) Logistics and supply chain management A description of strategies for developing comprehensive logistics and supply chain management strategies to ensure a steady and sufficient supply of personal protective equipment, medical equipment, pharmaceuticals, and other items. (H) Resource management A description of strategies for implementing crisis standards of care protocols to optimize the allocation and use of medical and non-medical assets during emergencies, including guidelines for the conservation, reuse, or repurposing of supplies. (I) Infection prevention A description of strategies for enhancing infection prevention measures, including staff training, environmental cleaning, and patient screening, to mitigate the spread of infectious diseases within health care facilities. (J) Treatment, transport, and discharge protocols A description of how treatment, transport, and discharge protocols were standardized to ensure consistency and efficiency in patient care and movement, including the incorporation of telehealth and remote monitoring solutions where feasible, explaining the technologies used and the outcomes of the interventions. (K) Case management protocols Descriptions of\u2014 (i) how case management protocols were refined to address both clinical and non-clinical needs of patients and residents; and (ii) the measures taken to ensure coordinated care and support throughout the treatment and recovery phases, detailing the challenges faced and the strategies employed to overcome such challenges. (L) Medical countermeasures Descriptions of\u2014 (i) the strategy employed to accelerate the development, distribution, and administration of medical countermeasures, such as vaccines, therapeutics, diagnostic tests, and treatments; and (ii) the challenges encountered in making such medical countermeasures available for use during the public health emergency and how such challenges were addressed. (M) Recovery A description of any implemented recovery strategies focusing on administrative, financial, policy, and equity considerations. (f) Authorization of appropriations There is authorized to be appropriated, to remain available until expended\u2014 (1) $3,500,000 to carry out subsections (a), (b), (c), and (e), including the first 4 reports of the after-action program; and (2) such sums as may be necessary to carry out subsection (d). .\n#### 3. Risk communication strategy\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ), as amended by section 2, is further amended by adding at the end the following:\n399V\u20139. Risk communication strategy (a) In general The Secretary shall establish, maintain, and implement a comprehensive strategy to ensure that communications about infectious diseases and other public health risks by agencies and offices of the Department of Health and Human Services, including the Centers for Disease Control and Prevention, are clear, accurate, and prioritize the populations most at risk. (b) Components The strategy under subsection (a) shall be designed to\u2014 (1) clearly identify at-risk populations during public health emergencies; and (2) ensure that communications are targeted, understandable, and accessible. (c) Initial strategy The Secretary shall establish and begin implementation of the initial strategy under subsection (a) not later than 1 year after the date of enactment of this section. .",
      "versionDate": "2025-03-06",
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
        "name": "Health",
        "updateDate": "2025-03-25T14:45:17Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1961ih.xml"
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
      "title": "CARE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CARE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Coordinated Agency Response Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to direct the Secretary of Health and Human Services to establish and implement a department-wide after-action program and a risk communication strategy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:33:18Z"
    }
  ]
}
```
