# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8273?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8273
- Title: Catching Up Family Caregivers Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8273
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-04-27T22:27:11Z
- Update date including text: 2026-04-27T22:27:11Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8273",
    "number": "8273",
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
    "title": "Catching Up Family Caregivers Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-27T22:27:11Z",
    "updateDateIncludingText": "2026-04-27T22:27:11Z"
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
          "date": "2026-04-14T16:03:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8273ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8273\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Ms. Pettersen (for herself and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow additional catch-up contributions for certain family caregivers.\n#### 1. Short title\nThis Act may be cited as the Catching Up Family Caregivers Act of 2026 .\n#### 2. Additional catch-up contributions for certain family caregivers\n##### (a) In general\nSubparagraph (A) of section 414(v)(5) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking who would and inserting \u201cwho\u2014\n(i) would ,\n**(2)**\nby adding or at the end, and\n**(3)**\nby adding at the end the following new clause:\n(ii) is a qualified family caregiver for the taxable year, .\n##### (b) Qualified family caregiver\nParagraph (6) of section 414(v) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraphs:\n(D) Qualified family caregiver (i) In general Except as provided in clause (ii), the term qualified family caregiver means an individual who\u2014 (I) has completed 500 or more hours as a family caregiver during the taxable year or any 1 previous taxable year, and (II) during the same taxable year, has completed fewer than 500 hours of paid employment (including self-employment). (ii) Limitation An individual shall be treated as a qualified family caregiver for not more than a total of, consecutively or nonconsecutively, the lesser of\u2014 (I) 1 taxable year for each taxable year during which such individual met the requirements of subclauses (I) and (II) of clause (i), or (II) 5 taxable years. (iii) Family caregiver The term family caregiver means an unpaid family member, a foster parent, or another unpaid adult, who is unemployed or severely underemployed (as determined by the Secretary) and who provides in-home care, monitoring, management, supervision, or treatment of\u2014 (I) a child, or (II) an adult with a special need (as defined in section 2901 of the Public Health Service Act), including an elderly adult who requires care or supervision due to an age-related condition. (iv) Hours An individual shall be treated as serving as a family caregiver during the hours in which the individual is engaged in caregiving tasks including assistance with bathing or grooming, dressing, laundry, food shopping or preparation, housekeeping, managing medications, transportation, and mobility assistance. (v) Plan reliance on self-certification An applicable employer plan is entitled to rely on the written representation of an individual that the individual was a qualified family caregiver for a taxable year. (E) Applicable dollar amount for qualified family caregivers An individual who is an eligible participant for the taxable year by reason of being a qualified family caregiver shall be treated for purposes of paragraph (2) in the same manner as an eligible participant who would attain age 60 but would not attain age 64 before the close of the taxable year. .\n##### (c) IRA catch-up contributions\nClause (i) of section 219(b)(5)(B) of the Internal Revenue Code of 1986 is amended by striking who has attained the age of 50 before the close of the taxable year, the deductible amount and inserting \u201cwho\u2014\n(I) has attained the age of 50 before the close of the taxable year, or (II) is a qualified family caregiver (as defined in section 414(v)(6)(D)) for the taxable year, the deductible amount .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.",
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
        "text": "Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S1741-1742)"
      },
      "number": "4291",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Catching Up Family Caregivers Act of 2026",
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
        "updateDate": "2026-04-21T01:25:47Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8273ih.xml"
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
      "title": "Catching Up Family Caregivers Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T03:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Catching Up Family Caregivers Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T03:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow additional catch-up contributions for certain family caregivers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T03:33:28Z"
    }
  ]
}
```
