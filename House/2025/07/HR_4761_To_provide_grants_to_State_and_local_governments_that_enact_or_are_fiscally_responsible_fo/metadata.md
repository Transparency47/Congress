# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4761?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4761
- Title: Eviction Right to Counsel Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4761
- Origin chamber: House
- Introduced date: 2025-07-25
- Update date: 2025-12-05T22:49:02Z
- Update date including text: 2025-12-05T22:49:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-25: Introduced in House
- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-25: Introduced in House

## Actions

- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-25",
    "latestAction": {
      "actionDate": "2025-07-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4761",
    "number": "4761",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "L000602",
        "district": "12",
        "firstName": "Summer",
        "fullName": "Rep. Lee, Summer L. [D-PA-12]",
        "lastName": "Lee",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Eviction Right to Counsel Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:49:02Z",
    "updateDateIncludingText": "2025-12-05T22:49:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-25",
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
          "date": "2025-07-25T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "NJ"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "GA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "MI"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "IL"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "WA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "CA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "AZ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NJ"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "PA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4761ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4761\nIN THE HOUSE OF REPRESENTATIVES\nJuly 25, 2025 Ms. Lee of Pennsylvania (for herself, Mrs. McIver , Mr. Johnson of Georgia , Ms. Tlaib , Mr. Jackson of Illinois , Mrs. Ramirez , Ms. Jayapal , and Ms. Simon ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide grants to State and local governments that enact or are fiscally responsible for implementing right to counsel legislation for low-income tenants facing eviction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Eviction Right to Counsel Act of 2025 .\n#### 2. Eviction right to counsel fund\n##### (a) Definitions\nIn this section:\n**(1) Covered individual**\nThe term covered individual means a tenant with an income that is equal to or less than 200 percent of the Federal poverty line.\n**(2) Covered proceeding**\nThe term covered proceeding means a civil action in a court or administrative forum for\u2014\n**(A)**\neviction, or an equivalent ejectment, from the primary residence of the tenant; or\n**(B)**\nthe termination of a housing subsidy.\n**(3) Eligible entity**\nThe term eligible entity means a State government, a local government, or an Indian Tribal government.\n**(4) Fund**\nThe term Fund means the Eviction Right to Counsel Fund established under subsection (b).\n**(5) Indian Tribal government**\nThe term Indian Tribal government has the meaning given the term Indian tribal government in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ).\n**(6) Right to counsel legislation**\nThe term right to counsel legislation means legislation that specifies that full legal representation shall be provided at no cost to all covered individuals in a covered proceeding.\n**(7) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(8) State**\nThe term State means each of the 50 States, the District of Columbia, and any territory or possession of the United States.\n##### (b) Establishment of fund\n**(1) In general**\nThere is established in the Treasury of the United States a fund to be known as the Eviction Right to Counsel Fund consisting of the amounts authorized to be appropriated under paragraph (2).\n**(2) Deposits to the fund**\nThere are authorized to be appropriated to the Fund $100,000,000 for each of fiscal years 2026 through 2030 for the cost of making grants under subsection (c).\n##### (c) Grants\n**(1) In general**\nThe Secretary shall establish a program to provide grants to eligible entities that enact right to counsel legislation or are fiscally responsible for implementing right to counsel legislation.\n**(2) Application**\n**(A) In general**\nAn eligible entity that desires a grant from the Secretary under this subsection shall submit to the Secretary an application at such time, in such manner, and accompanied by such information as the Secretary may reasonably require.\n**(B) Requirement**\nAn application submitted under subparagraph (A) shall include a certification that the eligible entity has enacted right to counsel legislation or is fiscally responsible for implementing right to counsel legislation.\n**(3) Priority**\nIn selecting applicants under this section, the Secretary shall prioritize funding for eligible entities that\u2014\n**(A)**\nhave enacted, or are fiscally responsible for implementing, laws that\u2014\n**(i)**\nlimit the causes for which a landlord can evict a tenant or refuse to renew the lease of a tenant when the tenant is not at fault or in violation of any law;\n**(ii)**\nrequire adequate written notice periods of not less than 30 days for tenants facing eviction;\n**(iii)**\nestablish eviction diversion programs; or\n**(iv)**\nprovide emergency rental assistance to tenants; or\n**(B)**\nwill prioritize using grant funds for the training and recruitment of attorneys to provide representation for covered individuals in a covered proceeding.\n**(4) Use of funds**\nA recipient of a grant under this section may use the grant funds for the costs incurred by right to counsel legislation, including providing training resources for attorneys representing covered individuals in covered proceedings.",
      "versionDate": "2025-07-25",
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2463",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Eviction Right to Counsel Act of 2025",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-12T18:21:16Z"
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
      "date": "2025-07-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4761ih.xml"
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
      "title": "Eviction Right to Counsel Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T03:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Eviction Right to Counsel Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide grants to State and local governments that enact or are fiscally responsible for implementing right to counsel legislation for low-income tenants facing eviction, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:24Z"
    }
  ]
}
```
