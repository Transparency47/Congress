# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1587?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1587
- Title: Fair Prescription Drug Prices for Americans Act
- Congress: 119
- Bill type: S
- Bill number: 1587
- Origin chamber: Senate
- Introduced date: 2025-05-05
- Update date: 2025-12-05T22:49:35Z
- Update date including text: 2025-12-05T22:49:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-05: Introduced in Senate
- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-05: Introduced in Senate

## Actions

- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1587",
    "number": "1587",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Fair Prescription Drug Prices for Americans Act",
    "type": "S",
    "updateDate": "2025-12-05T22:49:35Z",
    "updateDateIncludingText": "2025-12-05T22:49:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-05",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T19:36:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1587is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1587\nIN THE SENATE OF THE UNITED STATES\nMay 5, 2025 Mr. Hawley (for himself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require that the retail list price for certain prescription drugs and biological products may not exceed the average retail list price for the drug or biological product among certain nations.\n#### 1. Short title\nThis Act may be cited as the Fair Prescription Drug Prices for Americans Act .\n#### 2. International reference pricing for prescription drugs and biological products\n##### (a) Definitions\nIn this section:\n**(1) Biological product**\nThe term biological product means a biological product licensed under subsection (a) or (k) of section 351 of the Public Health Service Act ( 42 U.S.C. 262 ).\n**(2) Drug**\nThe term drug means a drug approved under subsection (c) or (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ).\n**(3) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n##### (b) Cap on retail list price of prescription drugs and biological products\nThe retail list price in the United States for a drug or a biological product may not exceed the average retail list price for the drug or biological product among Canada, France, Germany, Italy, Japan, and the United Kingdom, as calculated under subsection (c).\n##### (c) Calculation of average retail list price\nThe Secretary shall calculate on an annual basis the average retail list price for each drug and biological product sold in Canada, France, Germany, Italy, Japan, and the United Kingdom, through a combination of data reported by manufacturers of drugs and biological products under subsection (e) and data obtained through review of publicly filed materials by manufacturers of drugs and biological products in such countries.\n##### (d) Civil monetary penalty\n**(1) In general**\nAny manufacturer that violates subsection (b) with respect to a drug or biological product shall be subject to a civil monetary penalty imposed by the Secretary in amount equal to the product obtained by multiplying\u2014\n**(A)**\nthe difference between\u2014\n**(i)**\nthe list price for the drug or biological product sold in the United States; and\n**(ii)**\nthe average retail list price for the drug or biological product sold in Canada, France, Germany, Italy, Japan, and the United Kingdom, as calculated under subsection (c); and\n**(B)**\n10.\n**(2) Requirement**\nThe amount of a civil monetary penalty under paragraph (1) shall be calculated and charged for each unit of drug or biological product sold.\n##### (e) Data collection\nEach manufacturer of a drug or biological product shall submit to the Secretary on an annual basis\u2014\n**(1)**\nthe list price for the drug or biological product sold in the United States; and\n**(2)**\nthe list price for the drug or biological product sold in each of Canada, France, Germany, Italy, Japan, and the United Kingdom.\n##### (f) Guidance and regulations\nThe Secretary shall issue guidance and promulgate regulations to implement this section.",
      "versionDate": "2025-05-05",
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
        "actionDate": "2025-05-13",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3375",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fair Prescription Drug Prices for Americans Act",
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
        "name": "Health",
        "updateDate": "2025-06-04T15:25:13Z"
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
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1587is.xml"
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
      "title": "Fair Prescription Drug Prices for Americans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-16T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Prescription Drug Prices for Americans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-16T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require that the retail list price for certain prescription drugs and biological products may not exceed the average retail list price for the drug or biological product among certain nations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T03:18:19Z"
    }
  ]
}
```
