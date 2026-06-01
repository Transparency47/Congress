# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5466?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5466
- Title: GUARD Act
- Congress: 119
- Bill type: HR
- Bill number: 5466
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-01-14T05:04:07Z
- Update date including text: 2026-01-14T05:04:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Armed Services.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5466",
    "number": "5466",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "GUARD Act",
    "type": "HR",
    "updateDate": "2026-01-14T05:04:07Z",
    "updateDateIncludingText": "2026-01-14T05:04:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:07:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5466ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5466\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Jackson of Texas (for himself, Mr. Fallon , Mr. McCaul , Mr. Nehls , and Mr. Williams of Texas ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo authorize the Secretary of Defense to establish a National Security and Defense Artificial Intelligence Institute, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Growing University AI Research for Defense Act or the GUARD Act .\n#### 2. National Security and Defense Artificial Intelligence Institute\n##### (a) In general\nThe Secretary of Defense may establish at least one National Security and Defense Artificial Intelligence Institute (referred to in this section as an Institute ) at an eligible host institution.\n##### (b) Institute described\nA National Security and Defense Artificial Intelligence Institute referred to in subsection (a) is an artificial intelligence research institute that\u2014\n**(1)**\nis focused on a cross-cutting challenge or foundational science for artificial intelligence systems in the national security and defense sector;\n**(2)**\nestablishes partnerships among public and private organizations, including, as appropriate, Federal agencies, institutions of higher education, including community colleges, nonprofit research organizations, Federal laboratories, State, local, and Tribal governments, and industry, including the Defense Industrial Base and startup companies;\n**(3)**\nhas the potential to create an innovation ecosystem, or enhance existing ecosystems, to translate Institute research into applications and products used to enhance national security and defense capabilities;\n**(4)**\nsupports interdisciplinary research and development across multiple institutions of higher education and organizations; and\n**(5)**\nsupports workforce development in artificial intelligence related disciplines in the United States.\n##### (c) Financial assistance authorized\n**(1) In general**\nThe Secretary of Defense may seek to award financial assistance to an eligible host institution, or consortia thereof, to establish and support one or more Institutes.\n**(2) Use of funds**\nFinancial assistance awarded under paragraph (1) may be used by an Institute for\u2014\n**(A)**\nmanaging and making available to researchers accessible, curated, standardized, secure, and privacy protected data sets from the public and private sectors for the purposes of training and testing artificial intelligence systems and for research using artificial intelligence systems with regard to national security and defense;\n**(B)**\ndeveloping and managing testbeds for artificial intelligence systems, including sector-specific test beds, designed to enable users to evaluate artificial intelligence systems prior to deployment;\n**(C)**\nconducting research and education activities involving artificial intelligence systems to solve challenges with national security implications;\n**(D)**\nproviding or brokering access to computing resources, networking, and data facilities for artificial intelligence research and development relevant to the Institute\u2019s research goals;\n**(E)**\nproviding technical assistance to users, including software engineering support, for artificial intelligence research and development relevant to the Institute\u2019s research goals;\n**(F)**\nengaging in outreach and engagement to broaden participation in artificial intelligence research and the artificial intelligence workforce; and\n**(G)**\nsuch other activities as may determined by the Secretary of Defense.\n**(3) Duration**\nFinancial assistance under paragraph (1) shall be awarded for a five-year period, and may be renewed for not more than one additional five-year period.\n**(4) Application for financial assistance**\nA eligible host institution or consortia thereof seeking financial assistance under paragraph (1) shall submit to the Secretary of Defense an application at such time, in such manner, and containing such information as the Secretary may require.\n**(5) Competitive, merit review**\nIn awarding financial assistance under paragraph (1), the Secretary of Defense shall use a competitive, merit-based review process.\n**(6) Collaboration**\nIn awarding financial assistance under paragraph (1), the Secretary of Defense may collaborate other departments and agencies of the Federal Government with missions that relate to or have the potential to be affected by the national security implications of artificial intelligence systems.\n**(7) Limitation**\nNo financial assistance authorized in this section shall be awarded to an entity outside of the United States. All recipients of financial assistance under this section, including subgrantees, shall be based in the United States and shall meet such other eligibility criteria as may be established by the Secretary of Defense.\n##### (d) Definition\nIn this section, the term eligible host institution means a senior military college (as defined in section 2111a(f) of title 10, United States Code).",
      "versionDate": "2025-09-18",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-11",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "3454",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "GUARD Act of 2025",
      "type": "S"
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
        "updateDate": "2025-11-25T18:38:10Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5466ih.xml"
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
      "title": "GUARD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GUARD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Growing University AI Research for Defense Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Defense to establish a National Security and Defense Artificial Intelligence Institute, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:39Z"
    }
  ]
}
```
