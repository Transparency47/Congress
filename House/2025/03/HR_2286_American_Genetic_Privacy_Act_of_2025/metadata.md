# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2286?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2286
- Title: American Genetic Privacy Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2286
- Origin chamber: House
- Introduced date: 2025-03-24
- Update date: 2025-08-02T08:05:36Z
- Update date including text: 2025-08-02T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-24: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-24: Introduced in House

## Actions

- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2286",
    "number": "2286",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "American Genetic Privacy Act of 2025",
    "type": "HR",
    "updateDate": "2025-08-02T08:05:36Z",
    "updateDateIncludingText": "2025-08-02T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
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
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T16:03:20Z",
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
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "FL"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2286ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2286\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2025 Mr. Burchett (for himself, Mrs. Luna , and Mr. Davidson ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the disclosure of certain genetic information to the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Genetic Privacy Act of 2025 .\n#### 2. Prohibition on disclosure of certain genetic information to People\u2019s Republic of China\n##### (a) Prohibitions\n**(1) Sales**\nNo individual or entity may sell or offer for sale covered information, including aggregated covered information\u2014\n**(A)**\nto the People\u2019s Republic of China; or\n**(B)**\nto any entity under the influence, control, or ownership of the People\u2019s Republic of China.\n**(2) Disclosures by commercial DNA testing services**\nNo commercial DNA testing service may disclose, in any manner, covered information, including aggregated covered information\u2014\n**(A)**\nto the People\u2019s Republic of China; or\n**(B)**\nto any entity under the influence, control, or ownership of the People\u2019s Republic of China.\n##### (b) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nThe Federal Trade Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made part of this section. Any person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (c) Definitions\nIn this section:\n**(1) Commercial DNA testing service**\nThe term commercial DNA testing service means a person that provides genealogical or ancestry-related information based on an individual\u2019s DNA.\n**(2) Covered information**\nThe term covered information means the genetic information of an individual that was originally acquired from such individual through the use, by such individual, of a commercial DNA testing service.\n**(3) Genetic information**\nThe term genetic information means, with respect to any individual, information about such individual\u2019s genetic tests.\n**(4) Genetic test**\nThe term genetic test has the meaning given such term by section 201 of the Genetic Information Nondiscrimination Act of 2008 ( Public Law 110\u2013233 ; 42 U.S.C. 2000ff ).",
      "versionDate": "2025-03-24",
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
        "name": "Commerce",
        "updateDate": "2025-05-14T13:42:05Z"
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
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2286ih.xml"
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
      "title": "American Genetic Privacy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Genetic Privacy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the disclosure of certain genetic information to the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:22Z"
    }
  ]
}
```
