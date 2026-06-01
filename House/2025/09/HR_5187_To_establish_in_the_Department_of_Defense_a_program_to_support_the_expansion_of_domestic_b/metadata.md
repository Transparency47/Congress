# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5187?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5187
- Title: To establish in the Department of Defense a program to support the expansion of domestic bioindustrial manufacturing capacity.
- Congress: 119
- Bill type: HR
- Bill number: 5187
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2025-09-23T19:34:17Z
- Update date including text: 2025-09-23T19:34:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5187",
    "number": "5187",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000389",
        "district": "17",
        "firstName": "Ro",
        "fullName": "Rep. Khanna, Ro [D-CA-17]",
        "lastName": "Khanna",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To establish in the Department of Defense a program to support the expansion of domestic bioindustrial manufacturing capacity.",
    "type": "HR",
    "updateDate": "2025-09-23T19:34:17Z",
    "updateDateIncludingText": "2025-09-23T19:34:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
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
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
          "date": "2025-09-08T16:02:40Z",
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
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "CA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5187ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5187\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Mr. Khanna (for himself, Mr. Garamendi , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo establish in the Department of Defense a program to support the expansion of domestic bioindustrial manufacturing capacity.\n#### 1. Bioindustrial commercialization program\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense may establish a program to support the expansion of the domestic capacity for bioindustrial manufacturing of critical biomanufactured products at a commercial level through awards to eligible entities for establishing, upgrading, and retooling of eligible bioindustrial manufacturing facilities.\n##### (b) Awards\n**(1) In general**\nAn entity seeking an award under the program shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary determines appropriate.\n**(2) Competitive awards**\nThe Secretary shall make each award under the program to an eligible entity in a competitive manner.\n**(3) Award criteria**\nIn selecting eligible entities to receive awards under the program, the Secretary shall consider the following criteria:\n**(A)**\nThe potential of the technology of such eligible entity to improve domestic resilience and protect critical supply chains for critical biomanufactured products.\n**(B)**\nHow the technology of such eligible entity could help meet the demand for the capabilities required by the next generation of warfighters.\n**(C)**\nThe ability of the eligible bioindustrial manufacturing facility with respect to which such eligible entity is seeking such award to be repurposed and the range of products that such eligible bioindustrial manufacturing facility is capable of producing.\n**(D)**\nWhether the eligible bioindustrial manufacturing facility with respect to which such eligible entity is seeking such award supports the goal of wide geographic distribution of bioindustrial manufacturing facility across the United States.\n**(E)**\nWhether the eligible bioindustrial manufacturing facility with respect to which such eligible entity is seeking such award is located in geographic proximity to sources of input materials for the production of critical biomanufactured products or areas with established biomanfuacturing capabilities.\n**(F)**\nSuch additional considerations that the Secretary deems appropriate.\n**(4) Use of award funds**\nA recipient of an award under the program may use funds received under such award for the establishment, upgrading, or retooling of one or more eligible bioindustrial manufacturing facilities to produce critical biomanufactured products, including the development of business or technical plans related to such establishment, upgrading, or retooling.\n##### (c) Oversight\nIf the Secretary establishes the program, the Secretary shall establish reporting requirements for recipients of awards under the program which shall include requirements for period reports on the following:\n**(1)**\nThe progress of the recipient in establishing, upgrading, or retooling the eligible bioindustrial manufacturing facility with respect to which such recipient received such award.\n**(2)**\nThe estimated timeline and funding requirements for the recipient to begin biomanufacturing at the eligible bioindustrial manufacturing facility described in paragraph (1).\n**(3)**\nThe products, including the critical biomanufactured products, that are or will be produced at the eligible bioindustrial manufacturing facility described in paragraph (1).\n**(4)**\nThe progress of the recipient in entering into an agreement with the Department of Defense or an element thereof to provide critical biomanufactured products, that are or will be produced at the eligible bioindustrial manufacturing facility described in paragraph (1) once such eligible bioindustrial manufacturing facility begins biomanufacturing.\n##### (d) Reports to Congress\n**(1) Initial report**\nNot later than 90 days after the date of the enactment of this Act, the Secretary shall submit to the Committees on Armed Services of the House of Representatives and Senate a report on the plan of the Secretary for allocating amounts appropriated to the Department of Defense to fund the program.\n**(2) Annual reports**\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Secretary shall submit to the Committees on Armed Services of the House of Representatives and Senate a report on the activities under the program, including\u2014\n**(A)**\na list of the awards made under the program as of the date on which the report is submitted, including, for each such award\u2014\n**(i)**\nthe name of the entity that received the award;\n**(ii)**\nthe location of the eligible bioindustrial manufacturing facility with respect to which such entity received the award;\n**(iii)**\nthe amount of the award, disaggregated by the initial amount of the award and any additional amounts provided under the award;\n**(iv)**\nan explanation of the criteria supporting making the award to such entity, including a description of any notable technologies of such entity relevant to the award;\n**(v)**\nif applicable, an explanation of the rational for providing additional amounts under the award; and\n**(vi)**\nto the extent practicable, and explanation of the effects of the award;\n**(B)**\nan identification of amounts available to the Department of Defense for making awards under the program as of the date on which the report is submitted and an explanation of any plans for the use of such amounts;\n**(C)**\nan explanation of the communication between the Secretary and eligible entities seeking an award under the program regarding requirements and timelines for such awards; and\n**(D)**\nan explanation of how the establishment, upgrading, or retooling of the eligible bioindustrial manufacturing facility for which awards were made under the program aligns with priorities and needs of the Department of Defense and national security.\n##### (e) Sunset\n**(1) In general**\nExcept as provided by paragraph (2), this section shall terminate on the date that is 10 years after the date of the enactment of this Act.\n**(2) Extension**\nThe Secretary may change the date on which this section terminates to a date that is later than the date on which this section would terminate under paragraph (1) if the President determines that the continuation of the program is necessary to meet national economic and national security needs.\n##### (f) Definitions\nIn this section:\n**(1)**\nThe term biomanufacturing means the utilization of biological systems to develop new and advance existing products, tools, and processes at commercial scale.\n**(2)**\nThe term critical biomanufactured product means a chemical, material, and other product that is manufactured using biomanufacturing and is relevant to the Department of Defense.\n**(3)**\nThe term eligible bioindustrial manufacturing facility means a bioindustrial manufacturing facility that\u2014\n**(A)**\nis or, if not yet established, will be located in the United States; and\n**(B)**\nis or, pursuant to an award under the program, will produce critical biomanufactured products.\n**(4)**\nThe term eligible entity means an entity that\u2014\n**(A)**\nis a private entity;\n**(B)**\napplied for an award under the program in accordance with subsection (b)(1); and\n**(C)**\nmeets such other criteria for eligibility for an award under the program as determined by the Secretary.\n**(5)**\nThe term program means the program established under subsection (a).\n**(6)**\nThe term Secretary means the Secretary of Defense.",
      "versionDate": "2025-09-08",
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
        "actionDate": "2025-09-10",
        "actionTime": "17:56:43",
        "text": "The Clerk was authorized to correct section numbers, punctuation, and cross references, and to make other necessary technical and conforming corrections in the engrossment of H.R. 3838."
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
        "updateDate": "2025-09-23T18:26:58Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5187ih.xml"
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
      "title": "To establish in the Department of Defense a program to support the expansion of domestic bioindustrial manufacturing capacity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T10:03:19Z"
    },
    {
      "title": "To establish in the Department of Defense a program to support the expansion of domestic bioindustrial manufacturing capacity.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T08:05:50Z"
    }
  ]
}
```
