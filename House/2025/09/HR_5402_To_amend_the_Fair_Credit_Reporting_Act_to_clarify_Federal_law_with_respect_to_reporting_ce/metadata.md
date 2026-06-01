# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5402?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5402
- Title: Credit Access and Inclusion Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5402
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2026-03-10T23:41:16Z
- Update date including text: 2026-03-10T23:41:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5402",
    "number": "5402",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Credit Access and Inclusion Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-10T23:41:16Z",
    "updateDateIncludingText": "2026-03-10T23:41:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OR"
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
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5402ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5402\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mrs. Kim (for herself and Ms. Bynum ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Fair Credit Reporting Act to clarify Federal law with respect to reporting certain full-file consumer credit information to consumer reporting agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Credit Access and Inclusion Act of 2025 .\n#### 2. Full-file reporting permitted\n##### (a) In general\nSection 623 of the Fair Credit Reporting Act ( 15 U.S.C. 1681s\u20132 ) is amended by adding at the end the following:\n(f) Full-File credit reporting (1) Definitions In this subsection: (A) Energy utility firm The term energy utility firm means an entity that provides gas or electric utility services to the public. (B) Utility or telecommunication firm The term utility or telecommunication firm means an entity that provides utility services to the public through pipe, wire, landline, wireless, cable, or other connected facilities, or radio, electronic, or similar transmission (including the extension of such facilities). (2) Information relating to lease agreements, utilities, and telecommunications services Subject to the limitations in paragraph (3), and notwithstanding any other provision of law, a person or the Secretary of Housing and Urban Development may furnish to a consumer reporting agency information relating to the performance of a consumer in making payments\u2014 (A) under a lease agreement with respect to a dwelling, including such a lease in which the Department of Housing and Urban Development provides subsidized payments for occupancy in a dwelling; or (B) pursuant to a contract for a utility or telecommunications service. (3) Limitation Information about the usage by a consumer of any utility service provided by a utility or telecommunication firm may be furnished to a consumer reporting agency only to the extent that the information relates to the payment by the consumer for the service of the utility or telecommunication service or other terms of the provision of the services to the consumer, including any deposit, discount, or conditions for interruption or termination of the service. (4) Payment plan An energy utility firm may not report payment information to a consumer reporting agency with respect to an outstanding balance of a consumer as late if\u2014 (A) the energy utility firm and the consumer have entered into a payment plan (including a deferred payment agreement, an arrearage management program, or a debt forgiveness program) with respect to such outstanding balance; and (B) the consumer is meeting the obligations of the payment plan, as determined by the energy utility firm. (5) Opt-out A consumer may opt-out of the furnishing of the information described in paragraph (2) by submitting a written request to the furnisher of such information. .\n##### (b) Limitation on liability\nSection 623(c) of the Fair Credit Reporting Act ( 15 U.S.C. 1681s\u20132(c) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking or at the end;\n**(2)**\nby redesignating paragraph (3) as paragraph (4); and\n**(3)**\nby inserting after paragraph (2) the following:\n(3) subsection (f) of this section, including any regulations issued thereunder; or .\n##### (c) GAO study and report\nNot later than 2 years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Congress a report\u2014\n**(1)**\non the impact that furnishing information pursuant to subsection (f) of section 623 of the Fair Credit Reporting Act ( 15 U.S.C. 1681s\u20132 ), as added by subsection (a) of this section, has had on consumers; and\n**(2)**\nthat analyzes the effect on consumer credit scores of reporting consumer cash flow data to consumer credit agencies.",
      "versionDate": "2025-09-16",
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1465",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Credit Access and Inclusion Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-26T14:28:22Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5402ih.xml"
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
      "title": "To amend the Fair Credit Reporting Act to clarify Federal law with respect to reporting certain full-file consumer credit information to consumer reporting agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-25T06:55:46Z"
    },
    {
      "title": "Credit Access and Inclusion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-25T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Credit Access and Inclusion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-25T06:53:15Z"
    }
  ]
}
```
