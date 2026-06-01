# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2222?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2222
- Title: Lowering Egg Prices Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2222
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2026-04-16T08:06:42Z
- Update date including text: 2026-04-16T08:06:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2222",
    "number": "2222",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000622",
        "district": "19",
        "firstName": "Josh",
        "fullName": "Rep. Riley, Josh [D-NY-19]",
        "lastName": "Riley",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Lowering Egg Prices Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:42Z",
    "updateDateIncludingText": "2026-04-16T08:06:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:03:20Z",
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
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "SD"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MI"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "WI"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "MD"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "AR"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "AL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MI"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "OR"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "DE"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
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
      "sponsorshipDate": "2025-05-15",
      "state": "PA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MD"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "IN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "VA"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "TN"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AL"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "AR"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "IN"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "NE"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2222ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2222\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Riley of New York (for himself, Mr. Johnson of South Dakota , Ms. McDonald Rivet , Mr. Harrigan , Mr. Wied , Mr. Harris of Maryland , Mr. Womack , Mr. Palmer , Mr. Lawler , Mr. Thanedar , Ms. Salinas , and Ms. McBride ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo make inapplicable to surplus broiler hatching eggs certain regulations relating to shell eggs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lowering Egg Prices Act of 2025 .\n#### 2. Inapplicability of certain shell egg rule provisions to surplus broiler hatching eggs sold to egg breakers\n##### (a) Inapplicability of current rule\nEffective beginning on the date of the enactment of this Act, section 118.4(e) of title 21, Code of Federal Regulations (or successor regulations) shall not apply with respect to surplus broiler hatching eggs that are intended to be sold to an egg breaker for purposes of processing such eggs as liquid egg products subject to regulation under the Egg Products Inspection Act ( 21 U.S.C. 1031 et seq. ).\n##### (b) Revised rule required\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, and in consultation with the Secretary of Agriculture, shall issue a rule revising section 118.4 of title 21, Code of Federal Regulations (or successor regulations), to allow for surplus broiler hatching eggs to be held at such temperature and for such period of time at such temperature, so as to be compatible with conditions for hatching chicks and to allow for the sale of such eggs to egg breakers for the purposes described in subsection (a).\n##### (c) Definitions\nIn this Act:\n**(1)**\nThe terms egg and egg product have the meanings given such terms in section 4 of the Egg Products Inspection Act ( 21 U.S.C. 1033 ).\n**(2)**\nThe term egg breaker means a facility in the commercial sector that processes eggs by breaking the eggs out of their shells and selling the resulting liquid egg product in bulk to food manufacturers.\n**(3)**\nThe term broiler hatching egg means an egg intended for use by broiler hatcheries for the production of baby chicks.\n**(4)**\nThe term broiler hatchery means a facility where fertilized eggs from broiler breeder chickens are incubated and hatched into day-old chicks, which are then raised on farms to produce meat as broiler chickens.",
      "versionDate": "2025-03-18",
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
        "actionDate": "2025-12-10",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3423",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lowering Egg Prices Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-07T14:30:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-18",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr2222",
          "measure-number": "2222",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-18",
          "originChamber": "HOUSE",
          "update-date": "2025-11-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2222v00",
            "update-date": "2025-11-21"
          },
          "action-date": "2025-03-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Lowering Egg Prices Act of 2025</strong></p><p>This bill permits unrefrigerated surplus eggs originally intended for hatching to be repurposed for use in pasteurized liquid egg products intended for consumption.</p><p>Under current regulations, most eggs intended for consumption must be refrigerated within 36 hours of being laid. The bill would exempt from this requirement surplus broiler hatching eggs (eggs originally intended to be hatched and raised for meat) that are repurposed for sale to an egg breaker (a facility that sells liquid egg to food manufacturers).</p><p>(Broiler hatching eggs are generally held at a warmer temperature than other eggs in order to facilitate incubation. Because these eggs are not refrigerated, current regulations prohibit the sale of any surplus broiler hatching eggs to egg breakers for use in liquid egg products. Liquid egg products distributed for consumption are separately required under current law to be pasteurized, or treated to destroy bacteria.)</p><p>The bill also requires the Food and Drug Administration to revise the refrigeration requirement to permit surplus broiler hatching eggs held at temperatures suitable for hatching chicks to be sold to egg breakers for processing as liquid egg products.</p>"
        },
        "title": "Lowering Egg Prices Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2222.xml",
    "summary": {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Lowering Egg Prices Act of 2025</strong></p><p>This bill permits unrefrigerated surplus eggs originally intended for hatching to be repurposed for use in pasteurized liquid egg products intended for consumption.</p><p>Under current regulations, most eggs intended for consumption must be refrigerated within 36 hours of being laid. The bill would exempt from this requirement surplus broiler hatching eggs (eggs originally intended to be hatched and raised for meat) that are repurposed for sale to an egg breaker (a facility that sells liquid egg to food manufacturers).</p><p>(Broiler hatching eggs are generally held at a warmer temperature than other eggs in order to facilitate incubation. Because these eggs are not refrigerated, current regulations prohibit the sale of any surplus broiler hatching eggs to egg breakers for use in liquid egg products. Liquid egg products distributed for consumption are separately required under current law to be pasteurized, or treated to destroy bacteria.)</p><p>The bill also requires the Food and Drug Administration to revise the refrigeration requirement to permit surplus broiler hatching eggs held at temperatures suitable for hatching chicks to be sold to egg breakers for processing as liquid egg products.</p>",
      "updateDate": "2025-11-21",
      "versionCode": "id119hr2222"
    },
    "title": "Lowering Egg Prices Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Lowering Egg Prices Act of 2025</strong></p><p>This bill permits unrefrigerated surplus eggs originally intended for hatching to be repurposed for use in pasteurized liquid egg products intended for consumption.</p><p>Under current regulations, most eggs intended for consumption must be refrigerated within 36 hours of being laid. The bill would exempt from this requirement surplus broiler hatching eggs (eggs originally intended to be hatched and raised for meat) that are repurposed for sale to an egg breaker (a facility that sells liquid egg to food manufacturers).</p><p>(Broiler hatching eggs are generally held at a warmer temperature than other eggs in order to facilitate incubation. Because these eggs are not refrigerated, current regulations prohibit the sale of any surplus broiler hatching eggs to egg breakers for use in liquid egg products. Liquid egg products distributed for consumption are separately required under current law to be pasteurized, or treated to destroy bacteria.)</p><p>The bill also requires the Food and Drug Administration to revise the refrigeration requirement to permit surplus broiler hatching eggs held at temperatures suitable for hatching chicks to be sold to egg breakers for processing as liquid egg products.</p>",
      "updateDate": "2025-11-21",
      "versionCode": "id119hr2222"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2222ih.xml"
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
      "title": "Lowering Egg Prices Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lowering Egg Prices Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make inapplicable to surplus broiler hatching eggs certain regulations relating to shell eggs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:28Z"
    }
  ]
}
```
