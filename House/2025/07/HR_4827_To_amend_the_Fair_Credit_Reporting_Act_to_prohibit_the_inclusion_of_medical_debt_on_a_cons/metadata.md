# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4827?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4827
- Title: Medical Debt Relief Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4827
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2026-03-05T09:07:03Z
- Update date including text: 2026-03-05T09:07:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4827",
    "number": "4827",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Medical Debt Relief Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-05T09:07:03Z",
    "updateDateIncludingText": "2026-03-05T09:07:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:04:45Z",
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "IL"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "PA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "IL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MS"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WI"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "MI"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "IL"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NY"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "CT"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NY"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "RI"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NY"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4827ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4827\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Ms. Williams of Georgia (for herself, Mr. Correa , Mr. Krishnamoorthi , Ms. Scanlon , Mr. Kennedy of New York , Mr. Garc\u00eda of Illinois , Mr. Thompson of Mississippi , Mr. Pocan , Mr. Mullin , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Fair Credit Reporting Act to prohibit the inclusion of medical debt on a consumer report, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medical Debt Relief Act of 2025 .\n#### 2. Amendments to Fair Credit Reporting Act\n##### (a) Medical debt defined\nSection 603 of the Fair Credit Reporting Act ( 15 U.S.C. 1681a ) is amended by adding at the end the following:\n(bb) Medical debt The term medical debt means a debt related to, in whole or in part, transactions, accounts, or balances arising from the receipt of medical services, products, or devices. .\n##### (b) Exclusion for medical debt\n**(1) In general**\nSection 605(a) of the Fair Credit Reporting Act ( 15 U.S.C. 1681c(a) ) is amended by striking paragraph (6) and inserting the following:\n(6) Any adverse information related to a medical debt, including a medical debt that was placed for collection, charged to profit or loss, or subjected to any similar action. .\n**(2) Technical and conforming amendments**\nSection 604(g) of the Fair Credit Reporting Act ( 15 U.S.C. 1681b(g) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking (other than medical contact information treated in the manner required under section 605(a)(6)) ;\n**(ii)**\nin subparagraph (A), by adding or at the end;\n**(iii)**\nin subparagraph (B)(ii), by striking ; or and inserting a period; and\n**(iv)**\nby striking subparagraph (C); and\n**(B)**\nin paragraph (2), by striking (other than medical information treated in the manner required under section 605(a)(6)) .\n#### 3. Modification of regulations relating to prohibitions on use of medical debt information\n##### (a) Definitions\nIn this section, the terms credit and creditor have the meanings given those terms in section 702 of the Equal Credit Opportunity Act ( 15 U.S.C. 1691a ).\n##### (b) Requirement\nNot later than 1 year after the date of enactment of this Act, the Director of the Bureau of Consumer Financial Protection shall amend section 1022.30 of title 12, Code of Federal Regulations, or any successor regulation, to ensure that creditors are prohibited from obtaining or using information relating to the medical debt of a consumer in determining whether or not to extend credit to that consumer.",
      "versionDate": "2025-07-29",
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
        "actionDate": "2025-07-29",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2519",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Medical Debt Relief Act of 2025",
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
        "updateDate": "2025-09-17T17:01:57Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4827ih.xml"
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
      "title": "Medical Debt Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-14T10:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medical Debt Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-14T10:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Credit Reporting Act to prohibit the inclusion of medical debt on a consumer report, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-14T10:18:17Z"
    }
  ]
}
```
