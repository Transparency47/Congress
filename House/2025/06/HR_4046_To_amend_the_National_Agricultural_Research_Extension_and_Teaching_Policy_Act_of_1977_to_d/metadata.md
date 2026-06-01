# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4046?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4046
- Title: Cybersecurity in Agriculture Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4046
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2025-07-11T17:36:42Z
- Update date including text: 2025-07-11T17:36:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4046",
    "number": "4046",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Cybersecurity in Agriculture Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-11T17:36:42Z",
    "updateDateIncludingText": "2025-07-11T17:36:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:04:05Z",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4046ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4046\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Nunn of Iowa (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the National Agricultural Research, Extension, and Teaching Policy Act of 1977 to direct the Secretary of Agriculture to establish a program providing for the establishment of Agriculture Cybersecurity Centers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cybersecurity in Agriculture Act of 2025 .\n#### 2. Agriculture Cybersecurity Centers\nSubtitle K of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3319 et seq. ) is amended by adding at the end the following:\n1473I. Agriculture Cybersecurity Centers (a) In general The Secretary, acting through the Director of the National Institute of Food and Agriculture, and in consultation with the Secretary of Homeland Security, shall establish a program under which the Secretary will\u2014 (1) on a competitive basis, award grants to, or enter into cooperative agreements with, eligible entities to establish 5 Regional Agriculture Cybersecurity Centers to carry out research, development, and education on agriculture cybersecurity, with respect to seed agriculture, horticulture, animal agriculture, and the agriculture supply chain; (2) establish a national network of such Regional Agricultural Cybersecurity Centers; and (3) designate one college or university to coordinate the activities of such national network. (b) Duties A Regional Agriculture Cybersecurity Center shall\u2014 (1) conduct research on cybersecurity systems for the agriculture sector, including developing cybersecurity situational awareness systems to monitor cybersecurity threats, intrusions, and anomalies; (2) develop a security operations center for the agriculture sector to analyze cybersecurity threats, intrusions, and anomalies and to recommend mitigation actions; (3) develop cybersecurity technologies and tools for the agricultural sector, including domain-specific intrusion and anomaly detection systems, domain-specific intrusion prevention systems, domain specific role-based access control and user authentication systems, lightweight device authentication protocols, and secure network architectures; (4) build live cybersecurity testbeds to assess and refine cybersecurity technologies, tools, and systems developed for the agricultural sector; (5) conduct attack/defense exercises to validate and evaluate cybersecurity solutions for field deployment and agriculture industry adoption; (6) develop cybersecurity education and training programs for agricultural stakeholders; (7) conduct cybersecurity training using the testbeds referred to in paragraph (4); and (8) build a regional research and development collaboration network. (c) Eligible entity In this section, the term eligible entity means a college or university that has programs in food and agriculture sciences and cybersecurity that coordinates regional industry partners, cooperatives, government authorities and other stakeholders to strengthen security, privacy and resiliency, bolster the independent networks, and develop a skilled workforce. (d) Authorization of appropriations There are authorized to be appropriated to carry out this section $25,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-06-17",
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
        "updateDate": "2025-07-11T17:36:42Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4046ih.xml"
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
      "title": "Cybersecurity in Agriculture Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T12:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cybersecurity in Agriculture Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Agricultural Research, Extension, and Teaching Policy Act of 1977 to direct the Secretary of Agriculture to establish a program providing for the establishment of Agriculture Cybersecurity Centers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T12:18:22Z"
    }
  ]
}
```
