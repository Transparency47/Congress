# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2459?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2459
- Title: ABLE Employment Flexibility Act
- Congress: 119
- Bill type: S
- Bill number: 2459
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2026-05-28T21:53:02Z
- Update date including text: 2026-05-28T21:53:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2459",
    "number": "2459",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "ABLE Employment Flexibility Act",
    "type": "S",
    "updateDate": "2026-05-28T21:53:02Z",
    "updateDateIncludingText": "2026-05-28T21:53:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
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
      "actionDate": "2025-07-24",
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
          "date": "2025-07-24T18:40:34Z",
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
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "MO"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "MD"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2459is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2459\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Ms. Klobuchar (for herself, Mr. Schmitt , Mr. Van Hollen , and Mr. Moran ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code to allow employers to contribute to ABLE accounts in lieu of retirement plan contributions.\n#### 1. Short title\nThis Act may be cited as the ABLE Employment Flexibility Act .\n#### 2. Protecting working ABLE individuals from losing benefits because of retirement plan rules\n##### (a) In general\nSection 414 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(dd) ABLE account contributions (1) In general An applicable employer plan (as defined in subsection (v)(6)(A)) which is a defined contribution plan shall not be treated as failing to meet any requirement of this title solely because the plan provides that an eligible ABLE individual may elect for a plan year that employer contributions which would otherwise be made under the terms of the plan for such plan year shall (in lieu of contribution to the plan) be contributed by the employer to a qualified ABLE program described in section 529A on behalf of such eligible ABLE individual. (2) Treatment of contributions (A) No deduction for amounts contributed to ABLE account Except as provided in subparagraph (B), a contribution to a qualified ABLE program pursuant to an election under paragraph (1) shall not be treated as a contribution to an applicable employer plan. (B) Application of nondiscrimination rules Under rules prescribed by the Secretary, for purposes of applying sections 401(a)(4), 401(k)(3), 401(k)(12), 401(k)(13), 401(m)(2), 403(b)(12), 408(k)(3), 408(p)(2)(iii), 408(p)(2)(B), 410, and 416, contributions made to a qualified ABLE program pursuant to an election under paragraph (1) shall be treated as if such contributions were made to the plan. (3) Universal availability Paragraph (1) shall not apply unless the plan provides that the election described therein is available to all eligible ABLE individuals who are eligible to participate in the plan. (4) Cash or deferred arrangement A plan shall not fail to be treated as including a qualified cash or deferred arrangement described in section 401(k)(1) solely because such plan provides for the election described in paragraph (1). (5) Eligible ABLE individual For purposes of this subsection, the term eligible ABLE individual means an employee who, as of the first day of a plan year, is an eligible individual within the meaning of section 529A(e)(1) for the taxable year containing such first day of the plan year. (6) Treatment of permissive withdrawals An eligible ABLE individual may direct amounts eligible for withdrawal from an eligible contribution arrangement pursuant to section 414(w) to be contributed to a qualified ABLE program described in section 529A on behalf of such eligible ABLE individual. .\n##### (b) Treatment as beneficiary contribution\nSection 529A(b)(7) of the Internal Revenue Code of 1986 is amended by redesignating subparagraph (B) as subparagraph (C) and by inserting after subparagraph (A) the following new subparagraph:\n(B) Employer contributions Contributions made to a qualified ABLE program by an employer on behalf of a designated beneficiary described in this paragraph pursuant to paragraph (1) or (6) of section 414(dd) shall be treated as made by the designated beneficiary. .\n##### (c) Clarification of availability of employer contributions\nSection 529A(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(7) Employer contributions An employer of an eligible individual may contribute to any qualified ABLE program for which the eligible individual is the designated beneficiary, including through a contribution matching a contribution made by such eligible individual to the qualified ABLE program. .\n##### (d) Deduction for contributions remitted by employer to a qualified ABLE program\nNot later than 1 year after the date of the enactment of this Act, the Secretary of the Treasury shall\u2014\n**(1)**\namend the regulations under section 162 of the Internal Revenue Code of 1986 to confirm that contributions made by an employer to a qualified ABLE program described in section 529A of such Code on behalf of an eligible ABLE individual described in section 414(dd)(5) of such Code who is an employee of such employer shall be considered a reasonable allowance for salaries or other compensation for personal service if such contribution for a year, taking into account all other contributions to such qualified ABLE program, does not exceed the maximum contribution described in section 529A(b)(2)(B) of such Code with respect to such individual; and\n**(2)**\nupdate the publications issued for employers to encourage employers offering a retirement plan with automatic enrollment to notify employees who elect not to contribute to the plan and who may be eligible to contribute to a qualified ABLE program to notify such employees of the possibility of a contribution under section 529A(b)(2)(B)(ii) of such Code.\n##### (e) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall apply to plan and taxable years beginning after the date of the enactment of this Act.\n**(2) Clarifications**\nThe amendment made by subsection (c) and the amendments made pursuant to subsection (d)(1) shall apply to plan and taxable years beginning before, on, or after the date of the enactment of this Act.\n##### (f) Model amendment authority\nThe Secretary of the Treasury (or such Secretary's delegate) shall promulgate model amendments which plans may adopt to implement contributions to qualified ABLE programs pursuant to the amendments made by this section.",
      "versionDate": "2025-07-24",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "4644",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ABLE Employment Flexibility Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-12",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4498",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ABLE Tomorrow Act",
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
        "updateDate": "2025-09-05T19:28:15Z"
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
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2459is.xml"
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
      "title": "ABLE Employment Flexibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ABLE Employment Flexibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code to allow employers to contribute to ABLE accounts in lieu of retirement plan contributions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:51Z"
    }
  ]
}
```
