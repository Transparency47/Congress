# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2463?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2463
- Title: Eviction Right to Counsel Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2463
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2025-12-05T22:48:01Z
- Update date including text: 2025-12-05T22:48:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2463",
    "number": "2463",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Eviction Right to Counsel Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:48:01Z",
    "updateDateIncludingText": "2025-12-05T22:48:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-24",
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
          "date": "2025-07-24T18:49:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "MD"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-24",
      "state": "VT"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2463is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2463\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Booker (for himself, Mr. Van Hollen , Mr. Wyden , Mr. Sanders , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo provide grants to State and local governments that enact or are fiscally responsible for implementing right to counsel legislation for low-income tenants facing eviction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Eviction Right to Counsel Act of 2025 .\n#### 2. Eviction right to counsel fund\n##### (a) Definitions\nIn this section:\n**(1) Covered individual**\nThe term covered individual means a tenant with an income that is equal to or less than 200 percent of the Federal poverty line.\n**(2) Covered proceeding**\nThe term covered proceeding means a civil action in a court or administrative forum for\u2014\n**(A)**\neviction, or an equivalent ejectment, from the primary residence of the tenant; or\n**(B)**\nthe termination of a housing subsidy.\n**(3) Eligible entity**\nThe term eligible entity means a State government, a local government, or an Indian Tribal government.\n**(4) Fund**\nThe term Fund means the Eviction Right to Counsel Fund established under subsection (b).\n**(5) Indian Tribal government**\nThe term Indian Tribal government has the meaning given the term Indian tribal government in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ).\n**(6) Right to counsel legislation**\nThe term right to counsel legislation means legislation that specifies that full legal representation shall be provided at no cost to all covered individuals in a covered proceeding.\n**(7) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(8) State**\nThe term State means each of the 50 States, the District of Columbia, and any territory or possession of the United States.\n##### (b) Establishment of fund\n**(1) In general**\nThere is established in the Treasury of the United States a fund to be known as the Eviction Right to Counsel Fund consisting of the amounts authorized to be appropriated under paragraph (2).\n**(2) Deposits to the fund**\nThere are authorized to be appropriated to the Fund $100,000,000 for each of fiscal years 2026 through 2030 for the cost of making grants under subsection (c).\n##### (c) Grants\n**(1) In general**\nThe Secretary shall establish a program to provide grants to eligible entities that enact right to counsel legislation or are fiscally responsible for implementing right to counsel legislation.\n**(2) Application**\n**(A) In general**\nAn eligible entity that desires a grant from the Secretary under this subsection shall submit to the Secretary an application at such time, in such manner, and accompanied by such information as the Secretary may reasonably require.\n**(B) Requirement**\nAn application submitted under subparagraph (A) shall include a certification that the eligible entity has enacted right to counsel legislation or is fiscally responsible for implementing right to counsel legislation.\n**(3) Priority**\nIn selecting applicants under this section, the Secretary shall prioritize funding for eligible entities that\u2014\n**(A)**\nhave enacted, or are fiscally responsible for implementing, laws that\u2014\n**(i)**\nlimit the causes for which a landlord can evict a tenant or refuse to renew the lease of a tenant when the tenant is not at fault or in violation of any law;\n**(ii)**\nrequire adequate written notice periods of not less than 30 days for tenants facing eviction;\n**(iii)**\nestablish eviction diversion programs; or\n**(iv)**\nprovide emergency rental assistance to tenants; or\n**(B)**\nwill prioritize using grant funds for the training and recruitment of attorneys to provide representation for covered individuals in a covered proceeding.\n**(4) Use of funds**\nA recipient of a grant under this section may use the grant funds for the costs incurred by right to counsel legislation, including providing training resources for attorneys representing covered individuals in covered proceedings.",
      "versionDate": "2025-07-24",
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
        "actionDate": "2025-07-25",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4761",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Eviction Right to Counsel Act of 2025",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-12T18:21:10Z"
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
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2463is.xml"
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
      "title": "Eviction Right to Counsel Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Eviction Right to Counsel Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide grants to State and local governments that enact or are fiscally responsible for implementing right to counsel legislation for low-income tenants facing eviction, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:57Z"
    }
  ]
}
```
