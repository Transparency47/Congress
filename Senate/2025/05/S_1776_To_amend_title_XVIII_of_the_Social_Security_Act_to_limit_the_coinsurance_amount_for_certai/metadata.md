# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1776?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1776
- Title: Medicare Beneficiary Co-Pay Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 1776
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2025-12-05T22:59:07Z
- Update date including text: 2025-12-05T22:59:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1776",
    "number": "1776",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Medicare Beneficiary Co-Pay Fairness Act",
    "type": "S",
    "updateDate": "2025-12-05T22:59:07Z",
    "updateDateIncludingText": "2025-12-05T22:59:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T15:55:17Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1776is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1776\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mr. Cassidy (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to limit the coinsurance amount for certain services furnished in an ambulatory surgical center.\n#### 1. Short title\nThis Act may be cited as the Medicare Beneficiary Co-Pay Fairness Act .\n#### 2. Limitation on coinsurance amount\n##### (a) In general\nSection 1833 of the Social Security Act ( 42 U.S.C. 1395l ) is amended\u2014\n**(1)**\nin subsection (a)(1)(G), by inserting subject to subsection (ee), before with respect to facility services ; and\n**(2)**\nby adding at the end the following new subsection:\n(ee) Limitation on coinsurance amount for certain services furnished in an ambulatory surgical center In the case that application of subsection (a)(1)(G) would result in the imposition of a coinsurance amount with respect to facility services described in such subsection furnished during a year with respect to a surgical procedure that exceeds the amount of the inpatient hospital deductible established under section 1813(b) for such year, the Secretary shall\u2014 (1) reduce the amount of such coinsurance to an amount equal to such deductible; and (2) pay to the supplier furnishing such services an amount equal to such reduction. .\n##### (b) Effective date\nThe amendments made by this section shall apply to services furnished on or after January 1, 2026.",
      "versionDate": "2025-05-15",
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
        "actionDate": "2025-04-24",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3006",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend title XVIII of the Social Security Act to limit the coinsurance amount for certain services furnished in an ambulatory surgical center.",
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
        "updateDate": "2025-05-30T13:13:43Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1776is.xml"
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
      "title": "Medicare Beneficiary Co-Pay Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Medicare Beneficiary Co-Pay Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to limit the coinsurance amount for certain services furnished in an ambulatory surgical center.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:19Z"
    }
  ]
}
```
