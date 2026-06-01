# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2866?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2866
- Title: Cybersecurity in Agriculture Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2866
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2025-12-16T19:02:58Z
- Update date including text: 2025-12-16T19:02:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2866",
    "number": "2866",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Cybersecurity in Agriculture Act of 2025",
    "type": "S",
    "updateDate": "2025-12-16T19:02:58Z",
    "updateDateIncludingText": "2025-12-16T19:02:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-09-18T16:49:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NV"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "IN"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2866is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2866\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Budd (for himself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the National Agricultural Research, Extension, and Teaching Policy Act of 1977 to direct the Secretary of Agriculture to establish a program providing for the establishment of Agriculture Cybersecurity Centers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cybersecurity in Agriculture Act of 2025 .\n#### 2. Agriculture Cybersecurity Centers\nSubtitle K of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3310 et seq. ) is amended by adding at the end the following:\n1473I. Agriculture Cybersecurity Centers (a) In general The Secretary, acting through the Director of the National Institute of Food and Agriculture, and in consultation with the Secretary of Homeland Security, shall establish a program under which the Secretary shall\u2014 (1) on a competitive basis, award grants to, or enter into cooperative agreements with, eligible entities to establish 5 Regional Agriculture Cybersecurity Centers to carry out research, development, and education on agriculture cybersecurity, with respect to seed agriculture, horticulture, animal agriculture, and the agriculture supply chain; (2) establish a national network of such Regional Agriculture Cybersecurity Centers; and (3) designate one eligible entity to coordinate the activities of such national network. (b) Duties A Regional Agriculture Cybersecurity Center shall\u2014 (1) conduct research on cybersecurity systems for the agriculture sector, including developing cybersecurity situational awareness systems to monitor cybersecurity threats, intrusions, and anomalies; (2) develop a security operations center for the agriculture sector\u2014 (A) to analyze cybersecurity threats, intrusions, and anomalies; and (B) to recommend mitigation actions; (3) develop cybersecurity technologies and tools for the agriculture sector, including\u2014 (A) domain-specific intrusion and anomaly detection systems; (B) domain-specific intrusion prevention systems; (C) domain-specific role-based access control and user authentication systems; (D) lightweight device authentication protocols; and (E) secure network architectures; (4) build live cybersecurity testbeds to assess and refine cybersecurity technologies, tools, and systems developed for the agriculture sector; (5) conduct attack/defense exercises to validate and evaluate cybersecurity solutions for field deployment and agriculture industry adoption; (6) develop cybersecurity education and training programs for agricultural stakeholders; (7) conduct cybersecurity training using the testbeds referred to in paragraph (4); (8) build a regional research and development collaboration network; and (9) ensure that the research described in paragraph (1), the technologies and tools described in paragraph (3), and the attack/defense exercises described in paragraph (5) are specifically designed to prevent cyberattacks from\u2014 (A) the People\u2019s Republic of China; (B) the Democratic People\u2019s Republic of Korea; (C) the Russian Federation; (D) the Islamic Republic of Iran; and (E) such other countries as the Secretary, in consultation with the Secretary of Homeland Security, determines to be appropriate. (c) Definition of eligible entity In this section, the term eligible entity means a land-grant college or university that\u2014 (1) has programs in the food and agricultural sciences and cybersecurity; and (2) coordinates regional industry partners, cooperatives, government authorities, and other stakeholders\u2014 (A) to strengthen the security, privacy, and resiliency of agricultural systems; (B) to bolster the resiliency of cybersecurity infrastructure used by independent, noncentralized, locally owned and operated agricultural networks; and (C) to develop a skilled workforce equipped to manage and protect agricultural systems from cyberattacks. (d) Authorization of appropriations There is authorized to be appropriated to carry out this section $25,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-12-16T19:02:58Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2866is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-12-16T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Cybersecurity in Agriculture Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Agricultural Research, Extension, and Teaching Policy Act of 1977 to direct the Secretary of Agriculture to establish a program providing for the establishment of Agriculture Cybersecurity Centers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:22Z"
    }
  ]
}
```
