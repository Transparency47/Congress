# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6747?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6747
- Title: Olive Oil Standards Act
- Congress: 119
- Bill type: HR
- Bill number: 6747
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-01-09T16:29:23Z
- Update date including text: 2026-01-09T16:29:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6747",
    "number": "6747",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Olive Oil Standards Act",
    "type": "HR",
    "updateDate": "2026-01-09T16:29:23Z",
    "updateDateIncludingText": "2026-01-09T16:29:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:00:45Z",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6747ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6747\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Harder of California (for himself and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, to establish a standard of identify for individual grades of olive oil and a grade standard for individual olive oil and olive-pomace oil grades, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Olive Oil Standards Act .\n#### 2. Standards of identify and grade standards for olive oil\n##### (a) Establishment of standards of identify\nThe Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs (in this section referred to as the Secretary ), shall establish a standard of identify under section 401 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 341 ) for individual grades of olive oil.\n##### (b) Establishment of grade standards\n**(1) In general**\nThe Secretary shall establish for commercial producers, bottlers, and marketers in the United States a grade standard for individual olive oil and olive-pomace oil grades.\n**(2) Contents**\nThe grade standards shall include the following:\n**(A)**\nQuality and purity parameters for the following olive oil and olive-pomace oil grades:\n**(i)**\nExtra virgin olive oil.\n**(ii)**\nVirgin olive oil.\n**(iii)**\nOlive oil.\n**(iv)**\nRefined olive oil.\n**(v)**\nLampante olive oil.\n**(vi)**\nOlive-pomace oil.\n**(vii)**\nRefined olive-pomace oil.\n**(viii)**\nCrude olive-pomace oil.\n**(B)**\nMethods of analysis, according to American Oil Chemist Society, International Organization for Standardization, or International Olive Oil Council accreditation methods, to determine the characteristics of olive oils and olive-pomace oils.\n**(C)**\nMandatory labeling requirements that are\u2014\n**(i)**\nconsistent with the establishment of grade standards under this paragraph; and\n**(ii)**\nin compliance with the requirements of subchapters A, B, D, E, and F of part 101 of title 21, Code of Federal Regulations (or successor regulations).\n**(3) Special rules**\n**(A) Extra virgin olive oil**\nThe quality parameters developed for extra virgin olive oil under paragraph (2)(A)(i) shall include pyropheophytin a (PPP) and 1,2 diacylglycerols (DAG) parameters.\n**(B) Labeling**\nIn developing labeling standards under paragraph (2)(C), the Secretary shall ensure that\u2014\n**(i)**\nthe name of the product is consistent with the stated grade; and\n**(ii)**\nthe descriptions of the product on the package avoid inappropriate and misleading messages.\n##### (c) Report to Congress\nNot later than 120 days after the date of enactment of this Act, the Secretary shall transmit to Congress a report on the actions taken under this section.",
      "versionDate": "2025-12-16",
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
        "updateDate": "2026-01-09T16:29:23Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6747ih.xml"
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
      "title": "Olive Oil Standards Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Olive Oil Standards Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, to establish a standard of identify for individual grades of olive oil and a grade standard for individual olive oil and olive-pomace oil grades, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T11:18:17Z"
    }
  ]
}
```
