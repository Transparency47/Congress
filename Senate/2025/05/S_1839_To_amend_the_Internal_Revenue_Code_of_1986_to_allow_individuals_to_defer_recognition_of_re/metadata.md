# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1839?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1839
- Title: Generating Retirement Ownership through Long-Term Holding
- Congress: 119
- Bill type: S
- Bill number: 1839
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2026-05-01T11:03:33Z
- Update date including text: 2026-05-01T11:03:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1839",
    "number": "1839",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Generating Retirement Ownership through Long-Term Holding",
    "type": "S",
    "updateDate": "2026-05-01T11:03:33Z",
    "updateDateIncludingText": "2026-05-01T11:03:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-21",
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
        "item": [
          {
            "date": "2025-05-21T18:13:14Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-21T18:13:14Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1839is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1839\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mr. Cornyn introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow individuals to defer recognition of reinvested capital gains distributions from regulated investment companies.\n#### 1. Short title\nThis Act may be cited as the Generating Retirement Ownership through Long-Term Holding .\n#### 2. Deferral of reinvested capital gain dividends of regulated investment companies\n##### (a) In general\nPart III of subchapter O of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 1045 the following new section:\n1046. Reinvested capital gain dividends of regulated investment companies (a) Nonrecognition of gain In the case of an individual, no gain shall be recognized on the receipt of a capital gain dividend distributed by a regulated investment company to which part I of subchapter M applies if such capital gain dividend is automatically reinvested in additional shares of the company pursuant to a dividend reinvestment plan. (b) Definitions and special rules For purposes of this section\u2014 (1) Capital gain dividend The term capital gain dividend has the meaning given to such term by section 852(b)(3)(C). (2) Recognition of deferred capital gain dividends (A) In general Gain treated as unrecognized in accordance with subsection (a) shall be recognized in accordance with subparagraph (B)\u2014 (i) upon a subsequent sale or redemption by such individual of stock in the distributing company, or (ii) upon the death of the individual. (B) Gain recognition (i) In general Upon a sale or redemption described in subparagraph (A), the taxpayer shall recognize that portion of total gain treated as unrecognized in accordance with subsection (a) (and not previously recognized pursuant to this subparagraph) that is equivalent to the portion of the taxpayer\u2019s shares in the distributing company that are sold or redeemed. (ii) Death of individual Except as provided by regulations, any portion of such total gain not recognized under clause (i) prior to the taxpayer\u2019s death shall be recognized upon the death of the taxpayer and included in the taxpayer\u2019s gross income for the taxable year ending on the date of the taxpayer\u2019s death. (3) Holding period The taxpayer\u2019s holding period in shares acquired through reinvestment of a capital gain dividend to which subsection (a) applies shall be determined by treating the shareholder as having held such shares for one year and a day as of the date such shares are acquired. (c) Section not To apply to certain taxpayers This section shall not apply to\u2014 (1) an individual with respect to whom a deduction under section 151 is allowable to another taxpayer for a taxable year beginning in the calendar year in which such individual\u2019s taxable year begins, or (2) an estate or trust. (d) Regulations The Secretary shall prescribe such regulations as may be necessary to carry out the purposes of this section. .\n##### (b) Conforming amendments\n**(1)**\nSection 852(b)(3)(B) of such Code is amended by adding at the end the following new sentence: For rules regarding nonrecognition of gain with respect to reinvested capital gain dividends received by individuals, see section 1046. .\n**(2)**\nThe table of sections for part III of subchapter O of chapter 1 of such Code is amended by inserting after the item relating to section 1045 the following new item:\nSec. 1046. Reinvested capital gain dividends of regulated investment companies. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years ending after the date of the enactment of this Act.",
      "versionDate": "2025-05-21",
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
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2089",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Generating Retirement Ownership through Long-Term Holding",
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
        "name": "Taxation",
        "updateDate": "2025-06-06T20:39:49Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1839is.xml"
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
      "title": "Generating Retirement Ownership through Long-Term Holding",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T11:03:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Generating Retirement Ownership through Long-Term Holding",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow individuals to defer recognition of reinvested capital gains distributions from regulated investment companies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:28Z"
    }
  ]
}
```
