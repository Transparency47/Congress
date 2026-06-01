# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1525?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1525
- Title: Common Cents Act
- Congress: 119
- Bill type: S
- Bill number: 1525
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2025-07-01T11:06:18Z
- Update date including text: 2025-07-01T11:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1525",
    "number": "1525",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Common Cents Act",
    "type": "S",
    "updateDate": "2025-07-01T11:06:18Z",
    "updateDateIncludingText": "2025-07-01T11:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T15:35:10Z",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1525is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1525\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Ms. Lummis (for herself and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo direct the Secretary of the Treasury to stop minting the penny, to require cash transactions to be rounded up or down to the nearest 5 cents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Common Cents Act .\n#### 2. Elimination of production of one-cent coin\n##### (a) Elimination\nExcept as provided in subsection (b), and notwithstanding any other provision of law (including section 5112(a)(6) of title 31, United States Code), beginning on a date that is not later than 1 year after the date of enactment of this Act, the Secretary of the Treasury shall cease minting and issuing one-cent coins.\n##### (b) Exception\n**(1) In general**\nOn and after the date described in subsection (a), the Secretary of the Treasury shall continue to mint and issue one-cent coins as appropriate solely to meet the needs of numismatic collectors of the one-cent coin.\n**(2) Sale**\nAny one-cent coin minted and issued under this subsection shall be sold in accordance with section 5132(a) of title 31 United States Code, and any other provisions of law governing numismatic coins.\n**(3) Net receipts**\nThe net receipts from the sale of a one-cent coin minted and issued under this subsection shall equal or exceed the total cost of production, including variable costs and the appropriate share of fixed costs of production, as determined by the Secretary of the Treasury.\n##### (c) No effect on legal tender\nAll coins and currencies of the United States, including one-cent coins, regardless of when coined, printed, minted, or issued, shall continue to be legal tender for all debts, public and private, public charges, taxes, duties, and dues, in accordance with law.\n#### 3. Cash transaction rounding\n##### (a) In general\nNotwithstanding any other provision of law, any person selling goods or services in a cash transaction, entering into any other transaction that results in a payment or transfer of cash between the parties to the transaction, or paying cash wages to an employee as compensation shall round the payment in the following manner:\n**(1) Rounding down**\nIn any case in which the total transaction amount, including any taxes, ends with 1 cent, 2 cents, 6 cents, or 7 cents as the final digit, the amount of cents in the sum shall be rounded down to the nearest amount divisible by 5 for any person seeking to make payment with legal tender.\n**(2) Rounding up**\nIn any case in which the total transaction amount, including any taxes, ends with 3 cents, 4 cents, 8 cents, or 9 cents as the final digit, the amount of cents in the sum shall be rounded up to the nearest amount divisible by 5 for any person seeking to make payment with legal tender.\n##### (b) Exception\nSubsection (a) shall not apply to a transaction\u2014\n**(1)**\nin which the total transaction amount, including any taxes, totals $0.01 or $0.02, in which case that transaction amount shall be rounded up to $.05 for any person seeking to make payment with legal tender; or\n**(2)**\nfor which payment is made by any demand or negotiable instrument, electronic fund transfer, check, gift card, money order, credit card, or other similar instrument or method.\n##### (c) Effective date\nThis section shall take effect on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2025-04-30",
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
        "actionDate": "2025-04-29",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "3074",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Common Cents Act",
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
        "updateDate": "2025-05-21T12:19:33Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1525is.xml"
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
      "title": "Common Cents Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Common Cents Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of the Treasury to stop minting the penny, to require cash transactions to be rounded up or down to the nearest 5 cents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:26Z"
    }
  ]
}
```
