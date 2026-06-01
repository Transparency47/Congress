# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8274
- Title: Improving Retirement Security for Family Caregivers Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8274
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-04-27T22:28:46Z
- Update date including text: 2026-04-27T22:28:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-14: Introduced in House

## Actions

- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Ways and Means.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8274",
    "number": "8274",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000620",
        "district": "7",
        "firstName": "Brittany",
        "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
        "lastName": "Pettersen",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Improving Retirement Security for Family Caregivers Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-27T22:28:46Z",
    "updateDateIncludingText": "2026-04-27T22:28:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-14",
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
          "date": "2026-04-14T16:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8274ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8274\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Ms. Pettersen (for herself and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow certain family caregivers to contribute to a Roth IRA.\n#### 1. Short title\nThis Act may be cited as the Improving Retirement Security for Family Caregivers Act of 2026 .\n#### 2. Roth IRA contributions for certain family caregivers\n##### (a) In general\nSubsection (c) of section 408A of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(7) Special rule for Roth IRA contributions of qualified family caregivers (A) In general In the case of an individual who is a qualified family caregiver as of the close of the taxable year, in applying section 219 for purposes of paragraph (2), the limitation of paragraph (1) of section 219(b) shall be equal to the dollar amount in effect under section 219(b)(1)(A) for the taxable year. (B) Qualified family caregiver For purposes of this paragraph\u2014 (i) In general The term qualified family caregiver means an individual who, during the taxable year\u2014 (I) has completed 500 or more hours as a family caregiver, and (II) has completed fewer than 500 hours of paid employment (including self-employment). (ii) Family caregiver The term family caregiver means an unpaid family member, a foster parent, or another unpaid adult, who is unemployed or severely underemployed (as determined by the Secretary) and who provides in-home care, monitoring, management, supervision, or treatment of\u2014 (I) a child, or (II) an adult with a special need (as defined in section 2901 of the Public Health Service Act), including an elderly adult who requires care or supervision due to an age-related condition. (iii) Hours An individual shall be treated as serving as a family caregiver during the hours in which the individual is engaged in caregiving tasks, including assistance with bathing or grooming, dressing, laundry, food shopping or preparation, housekeeping, managing medications, transportation, and mobility assistance. (C) Coordination with spousal IRA In the case of an individual to whom section 219(c)(1) applies for the taxable year, subparagraph (A) shall be applied notwithstanding such section. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2026.",
      "versionDate": "2026-04-14",
      "versionType": "Introduced in House"
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
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4292",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Improving Retirement Security for Family Caregivers Act of 2026",
      "type": "S"
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
        "updateDate": "2026-04-21T01:25:07Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8274ih.xml"
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
      "title": "Improving Retirement Security for Family Caregivers Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T03:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Retirement Security for Family Caregivers Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T03:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow certain family caregivers to contribute to a Roth IRA.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T03:33:33Z"
    }
  ]
}
```
