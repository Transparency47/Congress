# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4644?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4644
- Title: ABLE Employment Flexibility Act
- Congress: 119
- Bill type: HR
- Bill number: 4644
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-30T08:05:48Z
- Update date including text: 2026-05-30T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4644",
    "number": "4644",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000629",
        "district": "3",
        "firstName": "Sharice",
        "fullName": "Rep. Davids, Sharice [D-KS-3]",
        "lastName": "Davids",
        "party": "D",
        "state": "KS"
      }
    ],
    "title": "ABLE Employment Flexibility Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:48Z",
    "updateDateIncludingText": "2026-05-30T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:11:15Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4644ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4644\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Davids of Kansas (for herself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow employers to contribute to ABLE accounts in lieu of retirement plan contributions.\n#### 1. Short title\nThis Act may be cited as the ABLE Employment Flexibility Act .\n#### 2. Protecting working ABLE individuals from losing benefits because of retirement plan rules\n##### (a) In general\nSection 414 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(dd) ABLE account contributions (1) In general An applicable employer plan (as defined in subsection (v)(6)(A)) which is a defined contribution plan shall not be treated as failing to meet any requirement of this title solely because the plan provides that an eligible ABLE individual may elect for a plan year that employer contributions which would otherwise be made under the terms of the plan for such plan year shall (in lieu of contribution to the plan) be contributed by the employer to a qualified ABLE program described in section 529A on behalf of such eligible ABLE individual. (2) Treatment of contributions (A) No deduction for amounts contributed to ABLE account Except as provided in subparagraph (B), a contribution to a qualified ABLE program pursuant to an election under paragraph (1) shall not be treated as a contribution to an applicable employer plan. (B) Application of nondiscrimination rules Under rules prescribed by the Secretary, for purposes of applying sections 401(a)(4), 401(k)(3), 401(k)(12), 401(k)(13), 401(m)(2), 403(b)(12), 408(k)(3), 408(p)(2)(iii), 408(p)(2)(B), 410, and 416, contributions made to a qualified ABLE program pursuant to an election under paragraph (1) shall be treated as if such contributions were made to the plan. (3) Universal availability Paragraph (1) shall not apply unless the plan provides that the election described therein is available to all eligible ABLE individuals who are eligible to participate in the plan. (4) Cash or deferred arrangement A plan shall not fail to be treated as including a qualified cash or deferred arrangement described in section 401(k)(1) solely because such plan provides for the election described in paragraph (1). (5) Eligible ABLE individual For purposes of this subsection, the term eligible ABLE individual means an employee who, as of the first day of a plan year, is an eligible individual within the meaning of section 529A(e)(1) for the taxable year containing such first day of the plan year. (6) Treatment of permissive withdrawals An eligible ABLE individual may direct amounts eligible for withdrawal from an eligible contribution arrangement pursuant to section 414(w) to be contributed to a qualified ABLE program described in section 529A on behalf of such eligible ABLE individual. .\n##### (b) Treatment as beneficiary contribution\nSection 529A(b)(7) of the Internal Revenue Code of 1986 is amended by redesignating subparagraph (B) as subparagraph (C) and by inserting after subparagraph (A) the following new subparagraph:\n(B) Employer contributions Contributions made to a qualified ABLE program by an employer on behalf of a designated beneficiary described in this paragraph pursuant to paragraph (1) or (6) of section 414(dd) shall be treated as made by the designated beneficiary. .\n##### (c) Clarification of availability of employer contributions\nSection 529A(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(7) Employer contributions An employer of an eligible individual may contribute to any qualified ABLE program for which the eligible individual is the designated beneficiary, including through a contribution matching a contribution made by such eligible individual to the qualified ABLE program. .\n##### (d) Deduction for contributions remitted by employer to a qualified ABLE program\nNot later than 1 year after the date of the enactment of this Act, the Secretary of the Treasury shall\u2014\n**(1)**\namend the regulations under section 162 of the Internal Revenue Code of 1986 to confirm that contributions made by an employer to a qualified ABLE program described in section 529A of such Code on behalf of an eligible ABLE individual described in section 414(dd)(5) of such Code who is an employee of such employer shall be considered a reasonable allowance for salaries or other compensation for personal service if such contribution for a year, taking into account all other contributions to such qualified ABLE program, does not exceed the maximum contribution described in section 529A(b)(2)(B) of such Code with respect to such individual; and\n**(2)**\nupdate the publications issued for employers to encourage employers offering a retirement plan with automatic enrollment to notify employees who elect not to contribute to the plan and who may be eligible to contribute to a qualified ABLE program to notify such employees of the possibility of a contribution under section 529A(b)(2)(B)(ii) of such Code.\n##### (e) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall apply to plan and taxable years beginning after the date of the enactment of this Act.\n**(2) Clarifications**\nThe amendment made by subsection (c) and the amendments made pursuant to subsection (d)(1) shall apply to plan and taxable years beginning before, on, or after the date of the enactment of this Act.\n##### (f) Model amendment authority\nThe Secretary of the Treasury (or such Secretary\u2019s delegate) shall promulgate model amendments which plans may adopt to implement contributions to qualified ABLE programs pursuant to the amendments made by this section.\n##### (g) Contributions disregarded for purposes of certain means-Tested Federal programs\n**(1) In general**\nNotwithstanding any other provision of Federal law that requires consideration of one or more financial circumstances (including income) of an individual, for the purpose of determining eligibility to receive, or the amount of, any assistance or benefit authorized by such provision to be provided to or for the benefit of such individual, a contribution to a qualified ABLE program pursuant to paragraph (1) or (6) of section 414(dd) of the Internal Revenue Code of 1986 shall be disregarded (including disregarded as income) for such purpose with respect to any period during which such individual maintains, makes contributions to, or receives distributions from such ABLE program.\n**(2) Cross reference**\nFor additional rules relating to the treatment of qualified ABLE programs for purposes of certain means-tested Federal programs, see section 103 of the Stephen Beck, Jr., ABLE Act of 2014 (division B of Public Law 113\u2013295 ).",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2459",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ABLE Employment Flexibility Act",
      "type": "S"
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
        "updateDate": "2025-08-01T17:00:17Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4644ih.xml"
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
      "title": "ABLE Employment Flexibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ABLE Employment Flexibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T04:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow employers to contribute to ABLE accounts in lieu of retirement plan contributions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T04:03:20Z"
    }
  ]
}
```
