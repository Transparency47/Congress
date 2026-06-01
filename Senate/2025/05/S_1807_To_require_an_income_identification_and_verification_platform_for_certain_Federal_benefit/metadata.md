# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1807?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1807
- Title: Timely and Accurate Benefits Act
- Congress: 119
- Bill type: S
- Bill number: 1807
- Origin chamber: Senate
- Introduced date: 2025-05-19
- Update date: 2025-06-23T18:18:47Z
- Update date including text: 2025-06-23T18:18:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in Senate
- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-19: Introduced in Senate

## Actions

- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1807",
    "number": "1807",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "Timely and Accurate Benefits Act",
    "type": "S",
    "updateDate": "2025-06-23T18:18:47Z",
    "updateDateIncludingText": "2025-06-23T18:18:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
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
          "date": "2025-05-20T00:10:31Z",
          "name": "Referred To"
        }
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1807is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1807\nIN THE SENATE OF THE UNITED STATES\nMay 19, 2025 Mr. Banks (for himself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require an income identification and verification platform for certain Federal benefit funds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Timely and Accurate Benefits Act .\n#### 2. Requirements of States; enhanced income verification platform required\nTo be eligible to receive Federal funds for a covered Federal benefit program, a State, not later than 1 year after the date of the enactment of this Act, shall procure, contract, and use an Enhanced Income Identification and Verification Platform.\n#### 3. Definitions\nIn this Act:\n**(1) Covered Federal benefit program**\nThe term covered Federal benefit program means any program administered by the Federal government, or by a State or local government using Federal funds, in which eligibility for benefits, or the amount of benefits, is determined, in whole or in part, based on the income of an individual or household.\n**(2) Enhanced gross income**\nThe term enhanced gross income means\u2014\n**(A)**\nwages, salaries, tips included and not included on pay stubs, and other compensation from all forms of employment, including traditional W-2 employment not provided by existing data sources, contract work, self-employment, and participation in the gig economy;\n**(B)**\nunemployment compensation;\n**(C)**\nany benefits paid under the Old-Age and Survivors Insurance and Disability Insurance programs and associated benefits under title II of the Social Security Act ( 42 U.S.C. 401 et seq. );\n**(D)**\nSupplemental Security Income (SSI) benefits paid under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. );\n**(E)**\ninterest and dividends;\n**(F)**\nshort-term and long-term rental income;\n**(G)**\nroyalties;\n**(H)**\nchild support and alimony payments received;\n**(I)**\ncash assistance from government programs;\n**(J)**\nregular or recurring gifts or contributions from individuals or organizations;\n**(K)**\ndistributions from trusts or estates;\n**(L)**\nany other source of income, whether taxable or non-taxable, that is available to the individual or household to meet their needs, as determined by the Secretary of the Treasury; and\n**(M)**\nother income identified and verified through consumer-permissioned direct access to deposit account transaction data.\n**(3) Enhanced Income Identification and Verification Platform**\nThe term Enhanced Income Identification and Verification Platform means\u2014\n**(A)**\nservices incorporating automated, real-time data matching and analytics to proactively identify and verify potential instances of unreported or underreported enhanced gross income, inconsistent income reporting, or other indicators of potential ineligibility or improper payments;\n**(B)**\nreceiving and analyzing applicant-permissioned deposit account transactional data that identifies and verifies sources of enhanced gross income not currently obtained through existing data sources that provide for payroll, new-hire and latent State and Federal tax data, with the option for the claimant to review and attest to the accuracy of the data; and\n**(C)**\nthe ability to identify and consolidate overlapping data to avoid double-counting of financial records.\n**(4) State**\nThe term State means each of the 50 States, the District of Columbia, and each territory and possession of the United States.",
      "versionDate": "2025-05-19",
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
        "actionDate": "2025-02-27",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "1755",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Timely and Accurate Benefits Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-23T18:18:47Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1807is.xml"
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
      "title": "Timely and Accurate Benefits Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-29T01:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Timely and Accurate Benefits Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require an income identification and verification platform for certain Federal benefit funds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T01:03:36Z"
    }
  ]
}
```
