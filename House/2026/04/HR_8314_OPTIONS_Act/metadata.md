# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8314?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8314
- Title: OPTIONS Act
- Congress: 119
- Bill type: HR
- Bill number: 8314
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-04-27T22:31:55Z
- Update date including text: 2026-04-27T22:31:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8314",
    "number": "8314",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "OPTIONS Act",
    "type": "HR",
    "updateDate": "2026-04-27T22:31:55Z",
    "updateDateIncludingText": "2026-04-27T22:31:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T14:02:15Z",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8314ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8314\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Steube (for himself and Ms. DelBene ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish that employers may offer employees a choice among tax-favored employer contributions.\n#### 1. Short title\nThis Act may be cited as the Optimizing Participant Tax Incentives through Optional Noncash Selections Act or the OPTIONS Act .\n#### 2. Exclusion of certain employer-provided benefits under a qualified benefit options plan\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 125 the following new section:\n125A. Qualified benefit options plans (a) In general Except as provided in subsection (c), no amount shall be included in the gross income of a participant in a qualified benefit options plan solely because, under the plan, the participant may choose among the benefits of the plan. (b) Qualified benefit options plan For purposes of this section\u2014 (1) In general The term qualified benefit options plan means a written plan or arrangement offered by an employer to employees and former employees (including retired employees) of the employer, under which participants\u2014 (A) may elect to allocate employer contributions among qualified benefits, and (B) may not elect to receive cash or any other taxable benefit instead of qualified benefits. (2) Qualified benefits The term qualified benefits includes\u2014 (A) non-elective employer contributions which are excluded from gross income under section 402 or 403, (B) contributions to a health reimbursement arrangement or health savings account which are excluded from gross income under section 105 or 106, (C) amounts paid by an employer pursuant to a qualified educational assistance program which are excluded from gross income under section 127, and (D) other benefits which are excluded from gross income under any other provision of this chapter. (c) Exception for highly compensated participants and key employees, etc Rules similar to the rules of subsections (b), (c), (e), and (g) of section 125 shall apply for purposes of this section. (d) Application of nondiscrimination rules For purposes of applying the requirements of sections 401(a)(4) and 416, in the case of any qualified plan described in section 401(a) that is included as a qualified benefit under this section, the amount of any employer contribution made available to a participant shall be treated as an employer contribution made to such plan, without regard to whether the participant elects to have any portion of such amount contributed to such plan. (e) Cross-Reference For reporting and recordkeeping requirements, see section 6039D. .\n##### (b) Reporting and recordkeeping\nSubsection (d) of section 6039D of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby inserting , 125A after 125 in paragraph (1), and\n**(2)**\nby adding at the end of paragraph (2) the following: In the case of a qualified benefit options plan under section 125A, such term means, with respect to such plan, the section under which each qualified benefit (as defined in section 125A(b)(2)) included in the plan is excludable from gross income. .\n##### (c) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 125 the following new item:\nSec. 125A. Qualified benefit options plans. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-04-15",
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
        "updateDate": "2026-04-27T22:31:55Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8314ih.xml"
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
      "title": "OPTIONS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T05:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "OPTIONS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Optimizing Participant Tax Incentives through Optional Noncash Selections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish that employers may offer employees a choice among tax-favored employer contributions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T05:48:33Z"
    }
  ]
}
```
