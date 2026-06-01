# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6385?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6385
- Title: Farm Transitions Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6385
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-05-16T08:07:01Z
- Update date including text: 2026-05-16T08:07:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Sponsor introductory remarks on measure. (CR H4977)
- 2025-12-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2026-01-13 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-12-02: Introduced in House

## Actions

- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Sponsor introductory remarks on measure. (CR H4977)
- 2025-12-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2026-01-13 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6385",
    "number": "6385",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "D000230",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Davis, Donald G. [D-NC-1]",
        "lastName": "Davis",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Farm Transitions Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:01Z",
    "updateDateIncludingText": "2026-05-16T08:07:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H4977)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-02",
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
          "date": "2025-12-03T15:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2026-01-13T20:02:20Z",
                "name": "Referred to"
              }
            },
            "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
            "systemCode": "hsag16"
          },
          {
            "activities": {
              "item": {
                "date": "2026-01-13T20:02:20Z",
                "name": "Referred to"
              }
            },
            "name": "Conservation, Research, and Biotechnology Subcommittee",
            "systemCode": "hsag14"
          }
        ]
      },
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
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "IA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6385ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6385\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. Davis of North Carolina (for himself and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agriculture Improvement Act of 2018 to reauthorize the Commission on Farm Transitions-Needs for 2050, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farm Transitions Act of 2025 .\n#### 2. Commission on Farm Transitions\u2014Needs for 2050\nSection 12609 of the Agriculture Improvement Act of 2018 ( Public Law 115\u2013334 ; 132 Stat. 5009) is amended\u2014\n**(1)**\nin subsection (a), by striking There is established and inserting Not later than 60 days after the date of the enactment of the Farm Transitions Act of 2025 , the Secretary shall establish ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin the subsection heading, by inserting and recommendations after Study ;\n**(B)**\nin the matter preceding paragraph (1), by inserting , and make recommendations relating to, after study on ;\n**(C)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (B), by inserting and timely after affordable ; and\n**(ii)**\nby striking subparagraph (D) and inserting the following:\n(D) apprenticeships, mentoring programs, business training, and technical assistance programs; .\n**(D)**\nin paragraph (3)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking existing and new Federal tax policies and inserting existing and new State and Federal policies, including tax policies ; and\n**(ii)**\nin subparagraph (A), by inserting or impede after facilitate ;\n**(E)**\nin paragraph (4), by striking and at the end;\n**(F)**\nin paragraph (5), by striking the period at the end and inserting a semicolon; and\n**(G)**\nby adding at the end the following:\n(6) heirs\u2019 property and succession of agricultural land; (7) any unique barriers faced by historically underserved and women farmers and ranchers in the ability to transfer, inherit, or purchase agricultural assets, including land; and (8) leasing and ownership trends, including leasing and ownership trends by foreign persons or entities. ;\n**(3)**\nin subsection (f), by striking 1 year after the date of enactment of this Act and inserting 2 years after the date of enactment of the Farm Transitions Act of 2025 ; and\n**(4)**\nin subsection (m), by striking 2023 and inserting 2029 .",
      "versionDate": "2025-12-03",
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
        "actionDate": "2026-04-30",
        "actionTime": "11:15:02",
        "text": "The Clerk was authorized to correct section numbers, punctuation, and cross references, and to make other necessary technical and conforming corrections in the engrossment of H.R. 7567."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-07T16:01:53Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6385ih.xml"
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
      "title": "To amend the Agriculture Improvement Act of 2018 to reauthorize the Commission on Farm Transitions-Needs for 2050, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T12:39:54Z"
    },
    {
      "title": "Farm Transitions Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Farm Transitions Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T12:08:22Z"
    }
  ]
}
```
