# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/560?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/560
- Title: Second Job Tax Relief Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 560
- Origin chamber: House
- Introduced date: 2025-01-20
- Update date: 2025-02-25T20:01:35Z
- Update date including text: 2025-02-25T20:01:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-01-20: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-20: Introduced in House

## Actions

- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-20",
    "latestAction": {
      "actionDate": "2025-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/560",
    "number": "560",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Second Job Tax Relief Act of 2025",
    "type": "HR",
    "updateDate": "2025-02-25T20:01:35Z",
    "updateDateIncludingText": "2025-02-25T20:01:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-20",
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
      "actionDate": "2025-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-20",
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
          "date": "2025-01-20T15:00:20Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr560ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 560\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2025 Mr. Bacon introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude compensation from secondary employment for certain taxpayers from the income tax and payroll taxes.\n#### 1. Short title\nThis Act may be cited as the Second Job Tax Relief Act of 2025 .\n#### 2. Exclusion of compensation for certain secondary employment from income and payroll tax\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Earned income from additional employment (a) In general In the case of a qualifying taxpayer, gross income shall not include secondary employment compensation. (b) Phase-Out The amount of compensation excluded from gross income under subsection (a) (determined without regard to this subsection) shall be reduced (but not below zero) by the amount which bears the same ratio to the amount which is so excludable as\u2014 (1) the excess (if any) of\u2014 (A) the taxpayer\u2019s modified adjusted gross income (as defined in section 36(b)(2)(B)) for such taxable year, over (B) $100,000 ($150,000 in the case of a married couple filing jointly), bears to (2) $50,000. (c) Secondary employment compensation (1) In general For purposes of this section, the term secondary employment compensation means compensation received for employment during a taxable year with respect to which an individual has made an election under paragraph (2) for an employer other than the primary employer of such individual. (2) Primary employer (A) Election A taxpayer may elect to designate, with respect to a taxable year, a primary employer if such individual was compensated on an hourly basis for not less than 2080 hours of work by such employer. (B) Definition For purposes of this section, the term primary employer means, with respect to a taxable year, an employer designated by the taxpayer under subparagraph (A). (d) Sunset Subsection (a) shall not apply to compensation earned in taxable years beginning after the date is that is 5 years after the date of the enactment of this section. .\n##### (b) Application to employment taxes\n**(1) Social security taxes**\n**(A) In general**\nSection 3121(a) of such Code is amended by striking or at the end of paragraph (22), by striking the period at the end of paragraph (23) and inserting ; or , and by inserting after paragraph (23) the following new paragraph:\n(24) any amount of compensation which is excludable from gross income under section 139J. .\n**(B) Trust funds held harmless**\nThere are hereby appropriated to the Federal Old-Age and Survivors Insurance Trust Fund, the Federal Disability Insurance Trust Fund, and the Federal Hospital Insurance Trust Fund amounts equivalent to the reduction in revenues to each such Trust Fund, respectively, by reason of the amendment made by subparagraph (A) (determined without regard to this subparagraph). Amounts appropriated by the preceding sentence shall be transferred from the general fund at such times and in such manner as to replicate to the extent possible the transfers which would have occurred to such Trust Fund had this section not been enacted.\n**(2) Unemployment Taxes**\nSection 3306(b) of such Code is amended by striking or at the end of paragraph (19), by striking the period at the end of paragraph (20) and inserting ; or , and by inserting after paragraph (20) the following new paragraph:\n(21) any amount of compensation which is excludable from gross income under section 139J. .\n**(3) Wage withholding**\nSection 3401(a) of such Code is amended by striking or at the end of paragraph (22), by striking the period at the end of paragraph (23) and inserting ; or , and by inserting after paragraph (23) the following new paragraph:\n(24) any amount of compensation which is excludable from gross income under section 139J. .\n##### (c) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Earned income from additional employment. .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts received after the date of the enactment of this Act.",
      "versionDate": "2025-01-20",
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
        "name": "Taxation",
        "updateDate": "2025-02-25T20:01:35Z"
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
      "date": "2025-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr560ih.xml"
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
      "title": "Second Job Tax Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Second Job Tax Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude compensation from secondary employment for certain taxpayers from the income tax and payroll taxes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T04:18:31Z"
    }
  ]
}
```
