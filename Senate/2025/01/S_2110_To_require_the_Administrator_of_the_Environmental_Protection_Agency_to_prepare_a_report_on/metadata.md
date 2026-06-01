# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2110?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2110
- Title: REUSE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2110
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2026-02-20T19:44:51Z
- Update date including text: 2026-02-20T19:44:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Ordered to be reported without amendment favorably.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 225.
- 2025-11-20 - Floor: Message on Senate action sent to the House.
- 2025-11-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8398; text: CR S8398)
- 2025-11-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-11-20 17:44:05 - Floor: Received in the House.
- 2025-11-20 18:18:38 - Floor: Held at the desk.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Ordered to be reported without amendment favorably.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 225.
- 2025-11-20 - Floor: Message on Senate action sent to the House.
- 2025-11-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8398; text: CR S8398)
- 2025-11-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-11-20 17:44:05 - Floor: Received in the House.
- 2025-11-20 18:18:38 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2110",
    "number": "2110",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "REUSE Act of 2025",
    "type": "S",
    "updateDate": "2026-02-20T19:44:51Z",
    "updateDateIncludingText": "2026-02-20T19:44:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-11-20",
      "actionTime": "18:18:38",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-11-20",
      "actionTime": "17:44:05",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S8398; text: CR S8398)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 225.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
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
        "item": [
          {
            "date": "2025-10-29T21:32:13Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-29T14:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-18T16:32:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2110is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2110\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Merkley (for himself and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo require the Administrator of the Environmental Protection Agency to prepare a report on reuse and refill systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Research for Environmental Uses and Sustainable Economies Act of 2025 or the REUSE Act of 2025 .\n#### 2. Report on reuse and refill systems\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Reuse and refill system**\nThe term reuse and refill system means a set of mechanisms relating to refillable or reusable products and beverage containers, as determined by the Administrator, that is supported by adequate infrastructure at the producer level, and adequate convenient availability and retail infrastructure at the consumer level, to ensure that the products and beverage containers can be\u2014\n**(A)**\nrepeatedly recovered, inspected, repaired (if necessary), and reissued by producers into the supply chain for reuse or refill for multiple cycles; and\n**(B)**\nconveniently and safely reused or refilled by producers and consumers for multiple cycles.\n**(3) State**\nThe term State has the meaning given the term in section 1004 of the Solid Waste Disposal Act ( 42 U.S.C. 6903 ).\n##### (b) Report\nNot later than 2 years after the date of enactment of this Act, the Administrator shall make publicly available a report describing the feasibility of, and best practices relating to, reuse and refill systems for various sectors, as determined by the Administrator, which may include food service, consumer food and beverage products, consumer cleaning products, personal care products, transportation and shipping of wholesale and retail goods, and public educational institutions, including institutions of higher education.\n##### (c) Objectives\nThe report under subsection (b) shall include an evaluation and summary of\u2014\n**(1)**\ntypes of reuse and refill systems for product delivery that can be best used at different scales;\n**(2)**\nmethods to ensure equitable distribution of reuse and refill systems, where economically feasible, for product delivery in communities of varying population size;\n**(3)**\njob creation opportunities through the use or expansion of reuse and refill systems;\n**(4)**\neconomic costs and benefits for\u2014\n**(A)**\nbusinesses that deploy reuse and refill system technologies; and\n**(B)**\nparties responsible for waste collection and management;\n**(5)**\ntypes of local, State, and Federal support needed to expand the use of reuse and refill systems; and\n**(6)**\nexisting barriers to the widespread implementation of reuse and refill systems.\n##### (d) Considerations\nIn preparing the report under subsection (b), the Administrator shall\u2014\n**(1)**\ntake into consideration relevant information relating to reuse and refill system programs and approaches in States, units of local government, and foreign countries; and\n**(2)**\nconsult with relevant reuse and refill system stakeholders.",
      "versionDate": "2025-06-18",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2110rs.xml",
      "text": "II\nCalendar No. 225\n119th CONGRESS\n1st Session\nS. 2110\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Merkley (for himself and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nOctober 29, 2025 Reported by Mrs. Capito , without amendment\nA BILL\nTo require the Administrator of the Environmental Protection Agency to prepare a report on reuse and refill systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Research for Environmental Uses and Sustainable Economies Act of 2025 or the REUSE Act of 2025 .\n#### 2. Report on reuse and refill systems\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Reuse and refill system**\nThe term reuse and refill system means a set of mechanisms relating to refillable or reusable products and beverage containers, as determined by the Administrator, that is supported by adequate infrastructure at the producer level, and adequate convenient availability and retail infrastructure at the consumer level, to ensure that the products and beverage containers can be\u2014\n**(A)**\nrepeatedly recovered, inspected, repaired (if necessary), and reissued by producers into the supply chain for reuse or refill for multiple cycles; and\n**(B)**\nconveniently and safely reused or refilled by producers and consumers for multiple cycles.\n**(3) State**\nThe term State has the meaning given the term in section 1004 of the Solid Waste Disposal Act ( 42 U.S.C. 6903 ).\n##### (b) Report\nNot later than 2 years after the date of enactment of this Act, the Administrator shall make publicly available a report describing the feasibility of, and best practices relating to, reuse and refill systems for various sectors, as determined by the Administrator, which may include food service, consumer food and beverage products, consumer cleaning products, personal care products, transportation and shipping of wholesale and retail goods, and public educational institutions, including institutions of higher education.\n##### (c) Objectives\nThe report under subsection (b) shall include an evaluation and summary of\u2014\n**(1)**\ntypes of reuse and refill systems for product delivery that can be best used at different scales;\n**(2)**\nmethods to ensure equitable distribution of reuse and refill systems, where economically feasible, for product delivery in communities of varying population size;\n**(3)**\njob creation opportunities through the use or expansion of reuse and refill systems;\n**(4)**\neconomic costs and benefits for\u2014\n**(A)**\nbusinesses that deploy reuse and refill system technologies; and\n**(B)**\nparties responsible for waste collection and management;\n**(5)**\ntypes of local, State, and Federal support needed to expand the use of reuse and refill systems; and\n**(6)**\nexisting barriers to the widespread implementation of reuse and refill systems.\n##### (d) Considerations\nIn preparing the report under subsection (b), the Administrator shall\u2014\n**(1)**\ntake into consideration relevant information relating to reuse and refill system programs and approaches in States, units of local government, and foreign countries; and\n**(2)**\nconsult with relevant reuse and refill system stakeholders.",
      "versionDate": "2025-10-29",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2110es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 2110\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo require the Administrator of the Environmental Protection Agency to prepare a report on reuse and refill systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Research for Environmental Uses and Sustainable Economies Act of 2025 or the REUSE Act of 2025 .\n#### 2. Report on reuse and refill systems\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Reuse and refill system**\nThe term reuse and refill system means a set of mechanisms relating to refillable or reusable products and beverage containers, as determined by the Administrator, that is supported by adequate infrastructure at the producer level, and adequate convenient availability and retail infrastructure at the consumer level, to ensure that the products and beverage containers can be\u2014\n**(A)**\nrepeatedly recovered, inspected, repaired (if necessary), and reissued by producers into the supply chain for reuse or refill for multiple cycles; and\n**(B)**\nconveniently and safely reused or refilled by producers and consumers for multiple cycles.\n**(3) State**\nThe term State has the meaning given the term in section 1004 of the Solid Waste Disposal Act ( 42 U.S.C. 6903 ).\n##### (b) Report\nNot later than 2 years after the date of enactment of this Act, the Administrator shall make publicly available a report describing the feasibility of, and best practices relating to, reuse and refill systems for various sectors, as determined by the Administrator, which may include food service, consumer food and beverage products, consumer cleaning products, personal care products, transportation and shipping of wholesale and retail goods, and public educational institutions, including institutions of higher education.\n##### (c) Objectives\nThe report under subsection (b) shall include an evaluation and summary of\u2014\n**(1)**\ntypes of reuse and refill systems for product delivery that can be best used at different scales;\n**(2)**\nmethods to ensure equitable distribution of reuse and refill systems, where economically feasible, for product delivery in communities of varying population size;\n**(3)**\njob creation opportunities through the use or expansion of reuse and refill systems;\n**(4)**\neconomic costs and benefits for\u2014\n**(A)**\nbusinesses that deploy reuse and refill system technologies; and\n**(B)**\nparties responsible for waste collection and management;\n**(5)**\ntypes of local, State, and Federal support needed to expand the use of reuse and refill systems; and\n**(6)**\nexisting barriers to the widespread implementation of reuse and refill systems.\n##### (d) Considerations\nIn preparing the report under subsection (b), the Administrator shall\u2014\n**(1)**\ntake into consideration relevant information relating to reuse and refill system programs and approaches in States, units of local government, and foreign countries; and\n**(2)**\nconsult with relevant reuse and refill system stakeholders.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2026-02-04",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "7370",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "REUSE Act of 2026",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-12-03T21:40:17Z"
          },
          {
            "name": "Air quality",
            "updateDate": "2025-12-03T21:41:35Z"
          },
          {
            "name": "Alcoholic beverages",
            "updateDate": "2025-12-03T21:39:50Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2025-12-03T21:43:22Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-12-03T21:41:42Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-12-03T21:40:53Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-03T21:43:09Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-12-03T21:39:35Z"
          },
          {
            "name": "Ecology",
            "updateDate": "2025-12-03T21:41:28Z"
          },
          {
            "name": "Environmental Protection Agency (EPA)",
            "updateDate": "2025-12-03T21:39:58Z"
          },
          {
            "name": "Environmental education",
            "updateDate": "2025-12-03T21:42:46Z"
          },
          {
            "name": "Environmental health",
            "updateDate": "2025-12-03T21:40:28Z"
          },
          {
            "name": "Environmental regulatory procedures",
            "updateDate": "2025-12-03T21:40:07Z"
          },
          {
            "name": "Food industry and services",
            "updateDate": "2025-12-03T21:39:43Z"
          },
          {
            "name": "Food supply, safety, and labeling",
            "updateDate": "2025-12-03T21:42:05Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-12-03T21:42:35Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-12-03T21:41:58Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2025-12-03T21:41:09Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-12-03T21:43:01Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-12-03T21:42:54Z"
          },
          {
            "name": "Low- and moderate-income housing",
            "updateDate": "2025-12-03T21:41:02Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-12-03T21:39:25Z"
          },
          {
            "name": "Marine pollution",
            "updateDate": "2025-12-03T21:39:17Z"
          },
          {
            "name": "Poverty and welfare assistance",
            "updateDate": "2025-12-03T21:40:38Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2025-12-03T21:42:15Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-12-03T21:40:43Z"
          },
          {
            "name": "Railroads",
            "updateDate": "2025-12-03T21:43:16Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-12-03T21:42:24Z"
          },
          {
            "name": "Soil pollution",
            "updateDate": "2025-12-03T21:41:17Z"
          },
          {
            "name": "Solid waste and recycling",
            "updateDate": "2025-12-03T21:39:11Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-12-03T21:41:49Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-12-03T21:43:29Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2025-12-03T21:41:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-07-21T15:04:41Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2110is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2110rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2110es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "REUSE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T11:58:21Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "REUSE Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-11-21T05:23:23Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Research for Environmental Uses and Sustainable Economies Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-11-21T05:23:23Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Research for Environmental Uses and Sustainable Economies Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-31T04:23:13Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "REUSE Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-31T04:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REUSE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Research for Environmental Uses and Sustainable Economies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the Environmental Protection Agency to prepare a report on reuse and refill systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:19:13Z"
    }
  ]
}
```
