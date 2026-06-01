# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2962?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2962
- Title: Small Business Investor Tax Parity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2962
- Origin chamber: Senate
- Introduced date: 2025-10-01
- Update date: 2026-05-08T14:42:41Z
- Update date including text: 2026-05-08T14:42:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-01: Introduced in Senate
- 2025-10-01 - IntroReferral: Introduced in Senate
- 2025-10-01 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-10-01: Introduced in Senate

## Actions

- 2025-10-01 - IntroReferral: Introduced in Senate
- 2025-10-01 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-01",
    "latestAction": {
      "actionDate": "2025-10-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2962",
    "number": "2962",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Small Business Investor Tax Parity Act of 2025",
    "type": "S",
    "updateDate": "2026-05-08T14:42:41Z",
    "updateDateIncludingText": "2026-05-08T14:42:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-01",
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
      "actionDate": "2025-10-01",
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
            "date": "2025-10-01T16:42:04Z",
            "name": "Referred To"
          },
          {
            "date": "2025-10-01T16:42:04Z",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "MT"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2962is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2962\nIN THE SENATE OF THE UNITED STATES\nOctober 1, 2025 Mr. Banks introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow the deduction under section 199A to apply to qualified BDC interest dividends in the same manner as qualified REIT dividends.\n#### 1. Short title\nThis Act may be cited as the Small Business Investor Tax Parity Act of 2025 .\n#### 2. Deduction for qualified business income to apply to certain interest dividends of qualified business development companies\n##### (a) In general\nSubsections (b)(1)(B) and (c)(1) of section 199A of the Internal Revenue Code of 1986 are each amended by inserting , qualified BDC interest dividends, after qualified REIT dividends .\n##### (b) Qualified BDC interest dividend defined\nSection 199A(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(5) Qualified BDC interest dividend (A) In general The term qualified BDC interest dividend means any dividend from an electing business development company received during the taxable year which is attributable to net interest income of such company which is properly allocable to a qualified trade or business of such company. (B) Electing business development company For purposes of this paragraph, the term electing business development company means a business development company (as defined in section 2(a) of the Investment Company Act of 1940) which has an election in effect under section 851 to be treated as a regulated investment company. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.",
      "versionDate": "2025-10-01",
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
        "actionDate": "2026-04-21",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "8415",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Small Business Tax Cut Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-23",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "652",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Small Business Investor Tax Parity Act of 2025",
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
        "updateDate": "2025-11-20T18:00:49Z"
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
      "date": "2025-10-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2962is.xml"
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
      "title": "Small Business Investor Tax Parity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Small Business Investor Tax Parity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow the deduction under section 199A to apply to qualified BDC interest dividends in the same manner as qualified REIT dividends.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-21T11:18:17Z"
    }
  ]
}
```
