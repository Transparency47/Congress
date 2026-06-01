# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3454?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3454
- Title: GUARD Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3454
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-01-14T05:01:04Z
- Update date including text: 2026-01-14T05:01:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3454",
    "number": "3454",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "GUARD Act of 2025",
    "type": "S",
    "updateDate": "2026-01-14T05:01:04Z",
    "updateDateIncludingText": "2026-01-14T05:01:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T19:01:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3454is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3454\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Cornyn (for himself and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo authorize the Secretary of Defense to establish one or more National Security and Defense Artificial Intelligence Institutes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Growing University Artificial Intelligence Research for Defense Act of 2025 or the GUARD Act of 2025 .\n#### 2. National Security and Defense Artificial Intelligence Institute\n##### (a) In general\nThe Secretary of Defense may establish one or more National Security and Defense Artificial Intelligence Institutes (referred to in this section as Institutes ) at eligible host institutions.\n##### (b) Institute described\nA National Security and Defense Artificial Intelligence Institute referred to in subsection (a) is an artificial intelligence research institute that\u2014\n**(1)**\nis focused on a cross-cutting challenge or foundational science for artificial intelligence systems in the national security and defense sector;\n**(2)**\nestablishes partnerships among public and private organizations, including, as appropriate, Federal agencies, institutions of higher education, including community colleges, nonprofit research organizations, Federal laboratories, State, local, and Tribal governments, and industry, including the Defense Industrial Base and startup companies;\n**(3)**\nhas the potential to create an innovation ecosystem, or enhance existing ecosystems, to translate Institute research into applications and products used to enhance national security and defense capabilities;\n**(4)**\nsupports interdisciplinary research and development across multiple institutions of higher education and organizations; and\n**(5)**\nsupports workforce development in artificial intelligence related disciplines in the United States.\n##### (c) Financial assistance authorized\n**(1) In general**\nThe Secretary of Defense may award financial assistance to an eligible host institution, or consortia thereof, to establish and support one or more Institutes.\n**(2) Use of funds**\nFinancial assistance awarded under paragraph (1) may be used by an Institute for\u2014\n**(A)**\nmanaging and making available to researchers accessible, curated, standardized, secure, and privacy protected data sets from the public and private sectors for the purposes of training and testing artificial intelligence systems and for research using artificial intelligence systems with regard to national security and defense;\n**(B)**\ndeveloping and managing testbeds for artificial intelligence systems, including sector-specific test beds, designed to enable users to evaluate artificial intelligence systems prior to deployment;\n**(C)**\nconducting research and education activities involving artificial intelligence systems to solve challenges with national security implications;\n**(D)**\nproviding or brokering access to computing resources, networking, and data facilities for artificial intelligence research and development relevant to the Institute\u2019s research goals;\n**(E)**\nproviding technical assistance to users, including software engineering support, for artificial intelligence research and development relevant to the Institute\u2019s research goals;\n**(F)**\nengaging in outreach and engagement to broaden participation in artificial intelligence research and the artificial intelligence workforce; and\n**(G)**\nsuch other activities as may determined by the Secretary of Defense.\n**(3) Duration**\nFinancial assistance under paragraph (1) shall be awarded for a five-year period, and may be renewed for not more than one additional five-year period.\n**(4) Application for financial assistance**\nAn eligible host institution or consortia thereof seeking financial assistance under paragraph (1) shall submit to the Secretary of Defense an application at such time, in such manner, and containing such information as the Secretary may require.\n**(5) Competitive, merit review**\nIn awarding financial assistance under paragraph (1), the Secretary of Defense shall use a competitive, merit-based review process.\n**(6) Collaboration**\nIn awarding financial assistance under paragraph (1), the Secretary of Defense may collaborate with other departments and agencies of the Federal Government with missions that relate to or have the potential to be affected by the national security implications of artificial intelligence systems.\n**(7) Limitation**\nNo financial assistance authorized in this section shall be awarded to an entity outside of the United States. All recipients of financial assistance under this section, including subgrantees, shall be based in the United States and shall meet such other eligibility criteria as may be established by the Secretary of Defense.\n##### (d) Definition\nIn this section, the term eligible host institution means\u2014\n**(1)**\nan institution of higher education (as defined in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 )) in the United States that conducts research sponsored by the Department of Defense; or\n**(2)**\na senior military college (as defined in section 2111a(f) of title 10, United States Code).",
      "versionDate": "2025-12-11",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-09-18",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "5466",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "GUARD Act",
      "type": "HR"
    },
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
        "actionDate": "2025-09-30",
        "text": "Received in the Senate."
      },
      "number": "3838",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Streamlining Procurement for Effective Execution and Delivery and National Defense Authorization Act for Fiscal Year 2026",
      "type": "HR"
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
        "updateDate": "2026-01-09T20:32:29Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3454is.xml"
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
      "title": "GUARD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GUARD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Growing University Artificial Intelligence Research for Defense Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Secretary of Defense to establish one or more National Security and Defense Artificial Intelligence Institutes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:19Z"
    }
  ]
}
```
