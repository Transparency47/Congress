# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4292?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4292
- Title: Improving Retirement Security for Family Caregivers Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4292
- Origin chamber: Senate
- Introduced date: 2026-04-14
- Update date: 2026-04-27T22:28:56Z
- Update date including text: 2026-04-27T22:28:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in Senate
- 2026-04-14 - IntroReferral: Introduced in Senate
- 2026-04-14 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-04-14: Introduced in Senate

## Actions

- 2026-04-14 - IntroReferral: Introduced in Senate
- 2026-04-14 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4292",
    "number": "4292",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001035",
        "district": "",
        "firstName": "Susan",
        "fullName": "Sen. Collins, Susan M. [R-ME]",
        "lastName": "Collins",
        "party": "R",
        "state": "ME"
      }
    ],
    "title": "Improving Retirement Security for Family Caregivers Act of 2026",
    "type": "S",
    "updateDate": "2026-04-27T22:28:56Z",
    "updateDateIncludingText": "2026-04-27T22:28:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-14",
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
      "actionDate": "2026-04-14",
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
          "date": "2026-04-14T20:38:36Z",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4292is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4292\nIN THE SENATE OF THE UNITED STATES\nApril 14, 2026 Ms. Collins (for herself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow certain family caregivers to contribute to a Roth IRA.\n#### 1. Short title\nThis Act may be cited as the Improving Retirement Security for Family Caregivers Act of 2026 .\n#### 2. Roth IRA contributions for certain family caregivers\n##### (a) In general\nSubsection (c) of section 408A of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(7) Special rule for Roth IRA contributions of qualified family caregivers (A) In general In the case of an individual who is a qualified family caregiver as of the close of the taxable year, in applying section 219 for purposes of paragraph (2), the limitation of paragraph (1) of section 219(b) shall be equal to the dollar amount in effect under section 219(b)(1)(A) for the taxable year. (B) Qualified family caregiver For purposes of this paragraph\u2014 (i) In general The term qualified family caregiver means an individual who, during the taxable year\u2014 (I) has completed 500 or more hours as a family caregiver, and (II) has completed fewer than 500 hours of paid employment (including self-employment). (ii) Family caregiver The term family caregiver means an unpaid family member, a foster parent, or another unpaid adult, who is unemployed or severely underemployed (as determined by the Secretary) and who provides in-home care, monitoring, management, supervision, or treatment of\u2014 (I) a child, or (II) an adult with a special need (as defined in section 2901 of the Public Health Service Act), including an elderly adult who requires care or supervision due to an age-related condition. (iii) Hours An individual shall be treated as serving as a family caregiver during the hours in which the individual is engaged in caregiving tasks including assistance with bathing or grooming, dressing, laundry, food shopping or preparation, housekeeping, managing medications, transportation, and mobility assistance. (C) Coordination with spousal IRA In the case of an individual to whom section 219(c)(1) applies for the taxable year, subparagraph (A) shall be applied notwithstanding such section. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-04-14",
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
        "actionDate": "2026-04-14",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "8274",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Improving Retirement Security for Family Caregivers Act of 2026",
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
        "updateDate": "2026-04-27T22:28:55Z"
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
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4292is.xml"
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
      "title": "Improving Retirement Security for Family Caregivers Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T05:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Retirement Security for Family Caregivers Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T05:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow certain family caregivers to contribute to a Roth IRA.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T05:48:28Z"
    }
  ]
}
```
