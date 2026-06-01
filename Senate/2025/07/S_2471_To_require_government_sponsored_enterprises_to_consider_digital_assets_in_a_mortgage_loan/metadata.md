# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2471?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2471
- Title: 21st Century Mortgage Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2471
- Origin chamber: Senate
- Introduced date: 2025-07-28
- Update date: 2025-09-16T14:59:31Z
- Update date including text: 2025-09-16T14:59:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-28: Introduced in Senate
- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-28: Introduced in Senate

## Actions

- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-28",
    "latestAction": {
      "actionDate": "2025-07-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2471",
    "number": "2471",
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
    "title": "21st Century Mortgage Act of 2025",
    "type": "S",
    "updateDate": "2025-09-16T14:59:31Z",
    "updateDateIncludingText": "2025-09-16T14:59:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-28",
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
      "actionDate": "2025-07-28",
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
          "date": "2025-07-28T20:45:31Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2471is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2471\nIN THE SENATE OF THE UNITED STATES\nJuly 28, 2025 Ms. Lummis introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require government-sponsored enterprises to consider digital assets in a mortgage loan risk assessment.\n#### 1. Short title\nThis Act may be cited as the 21st Century Mortgage Act of 2025 .\n#### 2. Consideration of Digital Assets\n##### (a) Federal National Mortgage Association\nSection 302(b) of the Federal National Mortgage Association Charter Act ( 12 U.S.C. 1717(b) ) is amended by adding at the end the following:\n(8) Digital Assets in Mortgage Risk Assessments (A) Definitions In this paragraph: (i) Digital asset The term digital asset \u2014 (I) means any digital representation of value that is recorded on a cryptographically-secured distributed ledger; and (II) does not include any asset that\u2014 (aa) is not commercially fungible, including a digital collectible or other unique asset described in subclause (I); or (bb) represents ownership of, or control over, an asset that is not itself an asset described in subclause (I). (ii) Qualified Custodial Arrangement The term qualified custodial arrangement means\u2014 (I) custody of a digital asset by a third-party custodian who is chartered, licensed, or otherwise regulated under Federal or State law and is subject to the jurisdiction of the courts of the United States; or (II) a multi-party custodial arrangement in which a controlling quorum of any private key, account, or other control component sufficient to authorize a transfer of the digital asset is held by custodians described in subclause (I), and the arrangement is subject to an enforceable governing agreement under the laws of the United States. (B) Digital Assets as Reserves The corporation shall, in assessing the risk of a single-family mortgage loan, permit the holdings of a borrower in a digital asset, evidenced and maintained pursuant to a qualified custodial arrangement, to be included in the reserves of a borrower without conversion of the digital asset to United States dollars. (C) Risk Mitigation In carrying out subparagraph (B), the corporation shall\u2014 (i) apply any appropriate adjustment for market volatility and liquidity of the digital asset; (ii) apply any appropriate adjustment for concentration of digital assets as a portion of reserves; and (iii) periodically review and update any risk-based adjustment applied under clauses (i) and (ii). (D) Notice and Approval Prior to implementing or materially revising any methodology used to assess a digital asset under this paragraph, the corporation shall submit the proposed methodology to the board of directors of the corporation for approval and, upon approval, to the Director of the Federal Housing Finance Agency for review. .\n##### (b) Federal Home Loan Mortgage Corporation\nSection 305 of the Federal Home Loan Mortgage Corporation Charter Act ( 12 U.S.C. 1454 ) is amended by inserting at the end the following:\n(e) Digital Assets in Mortgage Risk Assessments (1) Definitions In this subsection: (A) Digital Asset The term digital asset \u2014 (i) means any digital representation of value recorded on a cryptographically-secured distributed ledger; and (ii) does not include any asset that\u2014 (I) is not commercially fungible, including a digital collectible or other unique asset described in clause (i); or (II) represents ownership of, or control over, as asset that is not itself an asset described in clause (i). (B) Qualified Custodial Arrangement The term qualified custodial arrangement means\u2014 (i) custody of a digital asset by a third-party custodian who is chartered, licensed, or otherwise regulated under Federal or State law and is subject to the jurisdiction of the courts of the United States; or (ii) a multi-party custodial arrangement in which a controlling quorum of any private key, account, or other control component sufficient to authorize a transfer of the digital asset is held by custodians described in clause (i), and the arrangement is subject to an enforceable governing agreement under the laws of the United States. (2) Digital Assets as Reserves The Corporation shall, in assessing the risk of a single-family mortgage loan, permit the holdings of a borrower in a digital asset, evidenced and maintained pursuant to a qualified custodial arrangement, to be included in the reserves of a borrower without conversion of the digital asset to United States dollars. (3) Risk Mitigation In carrying out paragraph (2), the Corporation shall\u2014 (A) apply any appropriate adjustment for market volatility and liquidity of the digital asset; (B) apply any appropriate adjustment for concentration of digital assets as a portion of reserves; and (C) periodically review and update any risk-based adjustment applied under subparagraphs (A) and (B). (4) Notice and Approval Prior to implementing or materially revising any methodology used to assess digital assets under this subsection, the Corporation shall submit the proposed methodology to the Board of Directors for approval and, upon approval, to the Director of the Federal Housing Finance Agency for review. .",
      "versionDate": "2025-07-28",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-09-16T14:59:31Z"
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
      "date": "2025-07-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2471is.xml"
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
      "title": "21st Century Mortgage Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "21st Century Mortgage Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require government-sponsored enterprises to consider digital assets in a mortgage loan risk assessment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:33:19Z"
    }
  ]
}
```
