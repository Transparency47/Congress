# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7367?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7367
- Title: TANF Hygiene Access Act
- Congress: 119
- Bill type: HR
- Bill number: 7367
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-05-13T08:06:03Z
- Update date including text: 2026-05-13T08:06:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7367",
    "number": "7367",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "TANF Hygiene Access Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:03Z",
    "updateDateIncludingText": "2026-05-13T08:06:03Z"
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
          "date": "2026-02-04T15:02:10Z",
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
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "DE"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NJ"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "WA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "NY"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7367ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7367\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mr. Lawler (for himself and Ms. McBride ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish a demonstration pilot program to test the innovative use of funds and outcomes-oriented benchmarks for initiatives to support low income households in accessing hygiene materials.\n#### 1. Short title\nThis Act may be cited as the TANF Hygiene Access Act .\n#### 2. Demonstration program to test initiatives to support low income households in accessing hygiene materials\n##### (a) In general\nThe Secretary of Health and Human Services (in this Act referred to as the Secretary ), through the Office of Family Assistance, shall conduct a demonstration program to test innovative uses of funds and outcomes-oriented benchmarks for initiatives to improve the access of low income households to hygiene materials.\n##### (b) Definition of hygiene materials\nIn this Act, the term hygiene materials includes soap, deodorant, toothpaste, toothbrush, toilet paper, feminine hygiene products, shampoo, diapers, baby wipes, postpartum pads, antibacterial hand soap, laundry detergent, dish soap. and any other product related to hygiene as determined by the Secretary.\n##### (c) Applications\n**(1) Submission**\n**(A) In general**\nAn eligible entity may submit to the Secretary an application for a grant under this section.\n**(B) Eligible entity defined**\nIn this Act, the term eligible entity means a State, an Indian tribe, or a tribal organization, as such terms are defined in section 419 of the Social Security Act.\n**(2) Consideration**\n**(A) Competitive basis**\nThe Secretary shall establish a process for considering applications submitted pursuant to this section on a competitive basis.\n**(B) Factors to be considered**\nThe Secretary shall select applicants to receive grants under this section on the basis of\u2014\n**(i)**\nthe strength of the design of the hygiene access initiative described in the application submitted by the applicant;\n**(ii)**\nthe capacity of the initiative to serve the population targeted by the initiative;\n**(iii)**\nthe extent to which the applicant will partner with basic needs banks or similar entities with demonstrated experience in collecting, warehousing, and distributing hygiene materials or basic needs items;\n**(iv)**\nthe readiness of the applicant to evaluate the initiative;\n**(v)**\nthe cost-effectiveness of the initiative;\n**(vi)**\nthe past performance of the applicant in carrying out the program of the applicant that is funded under part A of title IV of the Social Security Act; and\n**(vii)**\ngeographic diversity.\n**(3) Publication**\nOn receipt of an application submitted pursuant to this section, the Secretary shall make a copy of the application available on the website of the Department of Health and Human Services.\n##### (d) Administration\nThe Secretary shall administer this section in a way that advances the goal of expanding access to hygiene materials for a significant number of low-income households.\n##### (e) Disbursement of grant\nThe Secretary shall disburse each grant awarded under this section, on the 1st day of the fiscal year for which the grant is awarded.\n##### (f) Use of grant\n**(1) In general**\nAn entity to which a grant is made under this section may use the grant only to provide hygiene materials to low income households.\n**(2) Limitation on use for administrative expenses**\nNot more than 15 percent of a grant made under this section may be used for administrative expenses.\n##### (g) Evaluation\nAn entity to which a grant is made under this section shall submit to the Secretary a report on the performance of the initiative carried out with the grant funds, as assessed using the following indicators:\n**(1)**\nThe geographic area served.\n**(2)**\nThe number of families served.\n**(3)**\nThe number of materials distributed.\n**(4)**\nThe frequency of distributions.\n##### (h) Funding\nOut of any money in the Treasury of the United States not otherwise appropriated, there are appropriated to carry out this Act\u2014\n**(1)**\n$25,000,000 for the 1st fiscal year that begins on or after the effective date of this Act;\n**(2)**\n$30,000,000 for each of the 2nd and 3rd fiscal years that begin on or after the effective date; and\n**(3)**\n$32,500,000 for each of the 4th and 5th fiscal years that begin on or after the effective date.\n##### (i) Effective date\nThis Act shall take effect 1 year after the date of the enactment of this Act.\n##### (j) Report on feasibility of large scale implementation\nBefore the 5th fiscal year that begins on or after the effective date of this Act, the Secretary shall submit to the Congress a report that contains an evaluation of the demonstration program conducted under this section, and the recommendation of the Secretary as to whether it would be feasible to implement a program of this type on a large scale.",
      "versionDate": "2026-02-04",
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
        "updateDate": "2026-02-20T13:57:36Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7367ih.xml"
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
      "title": "TANF Hygiene Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T05:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TANF Hygiene Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a demonstration pilot program to test the innovative use of funds and outcomes-oriented benchmarks for initiatives to support low income households in accessing hygiene materials.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:41Z"
    }
  ]
}
```
