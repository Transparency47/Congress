# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6043?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6043
- Title: MY DATA Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6043
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2025-12-09T22:18:18Z
- Update date including text: 2025-12-09T22:18:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6043",
    "number": "6043",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "T000482",
        "district": "3",
        "firstName": "Lori",
        "fullName": "Rep. Trahan, Lori [D-MA-3]",
        "lastName": "Trahan",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "MY DATA Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-09T22:18:18Z",
    "updateDateIncludingText": "2025-12-09T22:18:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
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
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:00:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6043ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6043\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mrs. Trahan introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit covered entities from preventing the use of certain data by individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Manage Your Data and Allow Only Trusted Access Act of 2025 or the MY DATA Act of 2025 .\n#### 2. Prohibition on covered entity action against consumer privacy\n##### (a) Prohibition\n**(1) In general**\nA covered entity may not prevent an individual from using de-identified data or cloaked data.\n**(2) Exception**\nThe prohibition described in paragraph (1) does not apply to a covered entity to the extent that the covered entity acts as a service provider.\n##### (b) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of subsection (a)(1) shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of the Commission**\nThe Federal Trade Commission shall enforce subsection (a)(1) in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section, and any person who violates subsection (a)(1) shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (c) Definitions\nIn this section:\n**(1) Cloaked data**\nThe term cloaked data means unique persistent identifiers that serve to adequately replace and conceal the covered data and identity of an individual while enabling communication between a covered entity and the individual.\n**(2) Covered data**\nThe term covered data means information that identifies or is linked or reasonably linkable (alone or in combination with other information) to an individual (or a device that identifies or is linked or reasonably linkable to an individual).\n**(3) Covered entity**\n**(A) In general**\nThe term covered entity means any person (other than an individual acting in a non-commercial context) who (alone or jointly with others) collects, processes, or transfers covered data.\n**(B) Exclusions**\nThe term covered entity does not include any of the following:\n**(i)**\nA Federal, State, or local government entity, such as a body, authority, board, bureau, commission, district, agency, or political subdivision of the Federal Government or a State or local government.\n**(ii)**\nAn entity that serves as a congressionally designated nonprofit, national resource center, and clearinghouse to provide assistance to victims, families, child-serving professionals, and the general public on issues relating to missing and exploited children.\n**(4) De-identified data**\nThe term de-identified data means information that does not identify and is not linked or reasonably linkable to an individual (or a device that identifies or is linked or reasonably linkable to an individual), regardless of whether such information is aggregated.\n**(5) Unique persistent identifier**\nThe term unique persistent identifier means an identifier\u2014\n**(A)**\nto the extent that such identifier is linked or reasonably linkable to an individual (or a device that identifies or is linked or reasonably linkable to an individual); and\n**(B)**\nthat is created uniquely for communication between such individual and a covered entity.",
      "versionDate": "2025-11-12",
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
        "updateDate": "2025-12-09T22:18:18Z"
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
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6043ih.xml"
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
      "title": "MY DATA Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MY DATA Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Manage Your Data and Allow Only Trusted Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit covered entities from preventing the use of certain data by individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:31Z"
    }
  ]
}
```
