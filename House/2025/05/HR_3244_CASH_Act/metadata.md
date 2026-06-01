# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3244?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3244
- Title: CASH Act
- Congress: 119
- Bill type: HR
- Bill number: 3244
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2025-10-09T00:11:25Z
- Update date including text: 2025-10-09T00:11:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3244",
    "number": "3244",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "L000491",
        "district": "3",
        "firstName": "Frank",
        "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
        "lastName": "Lucas",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "CASH Act",
    "type": "HR",
    "updateDate": "2025-10-09T00:11:25Z",
    "updateDateIncludingText": "2025-10-09T00:11:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T14:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3244ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3244\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Mr. Lucas introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo require certain entities to clearly disclose to small business concerns key information about factoring facility agreements prior to entering such agreements with such concerns, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Capital Access for Small Businesses Harmonization Act or the CASH Act .\n#### 2. Disclosures for small businesses that enter into factoring facility agreements\n##### (a) In general\nPrior to entering into a factoring facility agreement with a small business concern, the provider for such agreement shall provide to such small business concern a written disclosure of the terms of factoring transactions under such agreement if\u2014\n**(1)**\nthe aggregate dollar amount of factoring transactions authorized under such agreement, including any fees and other charges, is less than $500,000; or\n**(2)**\nsuch agreement does not specify the aggregate dollar amount of factoring transactions authorized under such agreement, such provider and the small business concern reasonably believe that the aggregate dollar amount of factoring transactions under such agreement, including any fees and other charges, will be less than $500,000.\n##### (b) Disclosure contents\nEach disclosure required under subsection (a) with respect to a factoring facility agreement shall include the following:\n**(1)**\nThe amount or percentage, as applicable, of the difference between the face value of a claim for payment sold in a factoring transaction and the amount the provider will pay to small business concern for such claim under such factoring facility agreement.\n**(2)**\nA list of any fees that may be charged under such factoring facility agreement.\n**(3)**\nThe amount and terms of any reserve under such factoring facility agreement.\n**(4)**\nThe duration of such factoring facility agreement.\n**(5)**\nAn example of a factoring transaction under such factoring facility agreement for a claim for payment sold in a factoring transaction with a face value of $10,000 that demonstrates\u2014\n**(A)**\nthe amount or percentage described in paragraph (1);\n**(B)**\nany fees that apply with respect to factoring transactions under such factoring facility agreement;\n**(C)**\nthe maximum amount of the reserve for such factoring transactions under such factoring facility agreement; and\n**(D)**\nthe net amount the provider pays to the small business concern for such claim in such factoring transaction.\n##### (c) Rule of construction\nNothing in this section shall be construed to require a provider to provide to a small business concern the disclosure required under subsection (a) with respect to the modification of a factoring facility agreement.\n#### 3. Federal preemption\nNo State or political subdivision of a State may impose a requirement that is in addition to, or inconsistent with, the requirements of this Act with respect to requiring providers to make disclosures to small business concerns regarding the terms of factoring transactions under a factoring facility agreement.\n#### 4. Definitions\nIn this Act:\n**(1) Factoring transaction**\nThe term factoring transaction means an agreement for the sale of accounts receivable of a small business concern for goods the small business concern has supplied, or services the small business concern has rendered, but for which payment has not yet been made and for which the primary source of repayment to the provider is payment by the account debtor on the account receivable being purchased. For purposes of this Act, the parties\u2019 characterization of a transaction as a purchase and sale of accounts receivable shall be conclusive that the transaction is a true sale and considered a factoring transaction. The term factoring transaction excludes a loan or an advance of money to a small business that is to be repaid by the small business from the proceeds of future accounts receivable which are not in existence when the loan or advance is made.\n**(2) Factoring facility agreement**\nThe term factoring facility agreement means an agreement between a provider and another entity that establishes the terms of factoring transactions between such provider and another entity.\n**(3) Provider**\nThe term provider means an individual or entity that\u2014\n**(A)**\nis a purchaser in a factoring transaction; and\n**(B)**\nis engaged in interstate commerce.\n**(4) Reserve**\nThe term reserve means the portion of any payment under a factoring transaction that the provider may withhold from the small business concern with respect to claims for payment sold under such factoring transaction, or any portion of such claims, until such claims, or the portion thereof, are paid.\n**(5) Small business concern**\nThe term small business concern has the meaning given such term under section 3 of the Small Business Act ( 15 U.S.C. 632 ).",
      "versionDate": "2025-05-07",
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
        "updateDate": "2025-05-21T12:49:05Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3244ih.xml"
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
      "title": "To require certain entities to clearly disclose to small business concerns key information about factoring facility agreements prior to entering such agreements with such concerns, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:25Z"
    },
    {
      "title": "CASH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T03:39:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CASH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Capital Access for Small Businesses Harmonization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:24Z"
    }
  ]
}
```
