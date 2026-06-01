# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2519?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2519
- Title: Medical Debt Relief Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2519
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2025-12-05T22:06:01Z
- Update date including text: 2025-12-05T22:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2519",
    "number": "2519",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Medical Debt Relief Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:06:01Z",
    "updateDateIncludingText": "2025-12-05T22:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:04:05Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CT"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "PA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "VT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "GA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2519is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2519\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Merkley (for himself, Mr. Blumenthal , Mr. Fetterman , Mr. Welch , Mr. Warnock , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Fair Credit Reporting Act to prohibit the inclusion of medical debt on a consumer report, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medical Debt Relief Act of 2025 .\n#### 2. Amendments to Fair Credit Reporting Act\n##### (a) Medical debt defined\nSection 603 of the Fair Credit Reporting Act ( 15 U.S.C. 1681a ) is amended by adding at the end the following:\n(bb) Medical debt The term medical debt means a debt related to, in whole or in part, transactions, accounts, or balances arising from the receipt of medical services, products, or devices. .\n##### (b) Exclusion for medical debt\n**(1) In general**\nSection 605(a) of the Fair Credit Reporting Act ( 15 U.S.C. 1681c(a) ) is amended by striking paragraph (6) and inserting the following:\n(6) Any adverse information related to a medical debt, including a medical debt that was placed for collection, charged to profit or loss, or subjected to any similar action. .\n**(2) Technical and conforming amendments**\nSection 604(g) of the Fair Credit Reporting Act ( 15 U.S.C. 1681b(g) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking (other than medical contact information treated in the manner required under section 605(a)(6)) ;\n**(ii)**\nin subparagraph (A), by adding or at the end;\n**(iii)**\nin subparagraph (B)(ii), by striking ; or and inserting a period; and\n**(iv)**\nby striking subparagraph (C); and\n**(B)**\nin paragraph (2), by striking (other than medical information treated in the manner required under section 605(a)(6)) .\n#### 3. Modification of regulations relating to prohibitions on use of medical debt information\n##### (a) Definitions\nIn this section, the terms credit and creditor have the meanings given those terms in section 702 of the Equal Credit Opportunity Act ( 15 U.S.C. 1691a ).\n##### (b) Requirement\nNot later than 1 year after the date of enactment of this Act, the Director of the Bureau of Consumer Financial Protection shall amend section 1022.30 of title 12, Code of Federal Regulations, or any successor regulation, to ensure that creditors are prohibited from obtaining or using information relating to the medical debt of a consumer in determining whether or not to extend credit to that consumer.",
      "versionDate": "2025-07-29",
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
        "actionDate": "2025-07-29",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "4827",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Medical Debt Relief Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-17T17:01:06Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2519is.xml"
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
      "title": "Medical Debt Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Medical Debt Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Fair Credit Reporting Act to prohibit the inclusion of medical debt on a consumer report, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:24Z"
    }
  ]
}
```
