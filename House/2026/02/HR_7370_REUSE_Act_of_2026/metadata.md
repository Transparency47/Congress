# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7370?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7370
- Title: REUSE Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7370
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-05-01T08:09:17Z
- Update date including text: 2026-05-01T08:09:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7370",
    "number": "7370",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "REUSE Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-01T08:09:17Z",
    "updateDateIncludingText": "2026-05-01T08:09:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:02:20Z",
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
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7370ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7370\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mr. Neguse (for himself, Mr. Buchanan , and Mr. Correa ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Administrator of the Environmental Protection Agency to prepare a report on reuse and refill systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Research for Environmental Uses and Sustainable Economies Act of 2026 or the REUSE Act of 2026 .\n#### 2. Report on reuse and refill systems\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Reuse and refill system**\nThe term reuse and refill system means a set of mechanisms relating to refillable or reusable products and beverage containers, as determined by the Administrator, that is supported by adequate infrastructure at the producer level, and adequate convenient availability and retail infrastructure at the consumer level, to ensure that the products and beverage containers can be\u2014\n**(A)**\nrepeatedly recovered, inspected, repaired (if necessary), and reissued by producers into the supply chain for reuse or refill for multiple cycles; and\n**(B)**\nconveniently and safely reused or refilled by producers and consumers for multiple cycles.\n**(3) State**\nThe term State has the meaning given the term in section 1004 of the Solid Waste Disposal Act ( 42 U.S.C. 6903 ).\n##### (b) Report\nNot later than 2 years after the date of enactment of this Act, the Administrator shall make publicly available a report describing the feasibility of, and best practices relating to, reuse and refill systems for various sectors, as determined by the Administrator, which may include food service, consumer food and beverage products, consumer cleaning products, personal care products, transportation and shipping of wholesale and retail goods, and public educational institutions, including institutions of higher education.\n##### (c) Objectives\nThe report under subsection (b) shall include an evaluation and summary of\u2014\n**(1)**\ntypes of reuse and refill systems for product delivery that can be best used at different scales;\n**(2)**\nmethods to ensure equitable distribution of reuse and refill systems, where economically feasible, for product delivery in communities of varying population size;\n**(3)**\njob creation opportunities through the use or expansion of reuse and refill systems;\n**(4)**\neconomic costs and benefits for\u2014\n**(A)**\nbusinesses that deploy reuse and refill system technologies; and\n**(B)**\nparties responsible for waste collection and management;\n**(5)**\ntypes of local, State, and Federal support needed to expand the use of reuse and refill systems; and\n**(6)**\nexisting barriers to the widespread implementation of reuse and refill systems.\n##### (d) Considerations\nIn preparing the report under subsection (b), the Administrator shall\u2014\n**(1)**\ntake into consideration relevant information relating to reuse and refill system programs and approaches in States, units of local government, and foreign countries; and\n**(2)**\nconsult with relevant reuse and refill system stakeholders.",
      "versionDate": "2026-02-04",
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
        "actionDate": "2025-11-20",
        "actionTime": "18:18:38",
        "text": "Held at the desk."
      },
      "number": "2110",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "REUSE Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2026-02-20T19:44:58Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7370ih.xml"
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
      "title": "REUSE Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T07:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REUSE Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T07:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Research for Environmental Uses and Sustainable Economies Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T07:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Environmental Protection Agency to prepare a report on reuse and refill systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T07:48:26Z"
    }
  ]
}
```
